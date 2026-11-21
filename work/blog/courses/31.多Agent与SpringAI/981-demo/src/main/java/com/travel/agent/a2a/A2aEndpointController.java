package com.travel.agent.a2a;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.travel.agent.agent.TeamMembers;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.agent.RuntimeContext;
import io.agentscope.core.message.Msg;
import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 把本地成员暴露为 A2A 服务端点（对应课程 11-2 的注册前置）：
 * <ul>
 *   <li>GET {@code /a2a/{agent}/.well-known/agent.json} —— 能力发现（Agent Card）</li>
 *   <li>POST {@code /a2a/{agent}} —— JSON-RPC {@code message/send} 任务提交（A2A 规范）</li>
 * </ul>
 * 远程主管（含其他容器）按这两个端点即可调用本容器的成员。
 *
 * <p>JSON-RPC 2.0 合规加固：① 响应 id 必须回带请求 id（原实现用随机 UUID，调用方无法关联）；
 * ② 校验 method，未知方法返回 -32601 而不是一律当任务处理；
 * ③ task 空白返回 -32602（无效参数）；
 * ④ 内部异常只回固定文案，详情进日志，不把堆栈/内部消息泄露给远程调用方。</p>
 */
@RestController
@RequestMapping("/a2a")
public class A2aEndpointController {

    private static final Logger log = LoggerFactory.getLogger(A2aEndpointController.class);
    private static final ObjectMapper MAPPER = new ObjectMapper();

    private static final String METHOD_MESSAGE_SEND = "message/send";

    private final ReActAgent routeMakingAgent;
    private final ReActAgent attractionAgent;

    public A2aEndpointController(ReActAgent routeMakingAgent, ReActAgent attractionAgent) {
        this.routeMakingAgent = routeMakingAgent;
        this.attractionAgent = attractionAgent;
    }

    @GetMapping(value = "/{agent}/.well-known/agent.json", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> agentCard(@PathVariable String agent) {
        ReActAgent target = resolve(agent);
        if (target == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(card(agent).toJson());
    }

    /**
     * required=false：空 body 放行为 null 进入 try，由 readTree 抛错走 JSON-RPC error 响应，
     * 避免参数解析阶段的 HttpMessageNotReadableException 绕过 A2A 错误结构直接 500。
     */
    @PostMapping(value = "/{agent}", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Map<String, Object>> messageSend(
            @PathVariable String agent, @RequestBody(required = false) String body) {
        ReActAgent target = resolve(agent);
        if (target == null) {
            return ResponseEntity.notFound().build();
        }
        String requestId = null;
        try {
            JsonNode root = MAPPER.readTree(body);
            requestId = root.path("id").asText(null);
            String id = requestId != null ? requestId : UUID.randomUUID().toString();

            String method = root.path("method").asText("");
            if (!METHOD_MESSAGE_SEND.equals(method)) {
                // JSON-RPC 协议错误按 HTTP 200 + error 体返回（A2A/JSON-RPC 惯例）
                return ResponseEntity.ok(jsonRpcError(id, -32601, "方法不存在: " + method));
            }

            String task = root.path("params").path("message").path("parts").path(0).path("text").asText("");
            if (task.isBlank()) {
                return ResponseEntity.ok(jsonRpcError(id, -32602, "无效参数: params.message.parts[0].text 不能为空"));
            }

            Msg response = target.call(
                    List.of(Msg.builder().textContent(task).build()), RuntimeContext.empty()).block();
            String text = response == null ? "" : response.getTextContent();
            return ResponseEntity.ok(jsonRpcResult(id, task, text));
        } catch (Exception e) {
            String id = requestId != null ? requestId : UUID.randomUUID().toString();
            // 详情只进日志；对外给固定文案，防止内部消息泄露给远程调用方
            log.warn("A2A 任务执行失败: agent={} id={}", agent, id, e);
            return ResponseEntity.internalServerError()
                    .body(jsonRpcError(id, -32000, "成员执行失败，请稍后重试"));
        }
    }

    private ReActAgent resolve(String agent) {
        if (TeamMembers.ROUTE_MAKING_AGENT.equals(agent)) {
            return routeMakingAgent;
        }
        if (TeamMembers.ATTRACTION_AGENT.equals(agent)) {
            return attractionAgent;
        }
        return null;
    }

    /** 名片委托 TeamMembers 单一数据源（原来在此硬编码描述，改一处忘另一处）。 */
    private AgentCard card(String agent) {
        String base = "/a2a/" + agent;
        return TeamMembers.ROUTE_MAKING_AGENT.equals(agent)
                ? TeamMembers.routeCard(base)
                : TeamMembers.attractionCard(base);
    }

    /** A2A JSON-RPC 成功响应（Task + Artifact，演示级最小结构）。 */
    private Map<String, Object> jsonRpcResult(String id, String task, String text) {
        Map<String, Object> taskResult = new LinkedHashMap<>();
        taskResult.put("id", "task-" + UUID.randomUUID().toString().substring(0, 8));
        taskResult.put("status", Map.of("state", "completed", "timestamp", Instant.now().toString()));
        taskResult.put(
                "artifacts",
                List.of(Map.of(
                        "artifactId", "art-" + UUID.randomUUID().toString().substring(0, 8),
                        "parts", List.of(Map.of("type", "text", "text", text)),
                        "echo", task)));
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("jsonrpc", "2.0");
        result.put("id", id);
        result.put("result", taskResult);
        return result;
    }

    /** A2A JSON-RPC 错误响应（回带请求 id）。 */
    private Map<String, Object> jsonRpcError(String id, int code, String message) {
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("jsonrpc", "2.0");
        result.put("id", id);
        result.put("error", Map.of("code", code, "message", message));
        return result;
    }
}
