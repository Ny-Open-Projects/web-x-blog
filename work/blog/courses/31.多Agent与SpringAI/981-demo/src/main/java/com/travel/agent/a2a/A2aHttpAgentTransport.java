package com.travel.agent.a2a;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.github.resilience4j.core.IntervalFunction;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import java.net.URI;
import java.net.http.HttpClient;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.function.Supplier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.web.client.RestClient;

/**
 * 远程成员通道（prod profile）：按 A2A 规范访问远端 Agent。
 *
 * <ul>
 *   <li>GET {@code /.well-known/agent.json} —— 能力发现（对应课程 11-3 获取团队成员描述）</li>
 *   <li>POST {@code /} —— JSON-RPC {@code message/send} 提交任务（对应课程 11-4 调动团队成员执行任务）</li>
 * </ul>
 * 同一进程内也可跨容器互调；配合 {@link NacosAgentRegistry} 即课程 11-2 的注册中心形态。
 *
 * <p>工程加固：① JDK HttpClient 默认无读超时，远程成员挂起会把主管的 Tomcat 线程
 * 无限阻塞直至级联打满线程池——连接/读取超时必须显式写死；
 * ② 名片获取失败不缓存「unknown」结果，一次网络抖动不应让进程存活期内永远发现不了能力；
 * ③ 识别 200 响应体内嵌的 JSON-RPC error，避免把远端错误当任务结果返回主管；
 * ④ 远程 POST 套 resilience4j 重试（指数退避 ×3）：兜住瞬时网络抖动 / 远端 5xx，
 * 但【协议层错误】（A2A 返回 JSON-RPC error）不重试——那是对端业务拒绝，重发无意义。
 * 重试在内、熔断（SupervisorTools 外层）在外，二者不冲突。</p>
 */
public class A2aHttpAgentTransport implements AgentTransport {

    private static final Logger log = LoggerFactory.getLogger(A2aHttpAgentTransport.class);
    private static final ObjectMapper MAPPER = new ObjectMapper();

    private static final Duration CONNECT_TIMEOUT = Duration.ofSeconds(3);
    private static final Duration READ_TIMEOUT = Duration.ofSeconds(10);

    /** 重试：最多 3 次、首次 300ms 指数退避。仅重试传输层故障，协议层错误 ignore。 */
    private static final Retry RETRY = Retry.of("a2aTransport",
            RetryConfig.custom()
                    .maxAttempts(3)
                    .intervalFunction(IntervalFunction.ofExponentialBackoff(Duration.ofMillis(300), 2.0))
                    .ignoreExceptions(A2aProtocolException.class)
                    .build());

    private final String baseUrl;
    private final RestClient client;
    private volatile AgentCard card;

    public A2aHttpAgentTransport(String baseUrl) {
        this.baseUrl = baseUrl.endsWith("/") ? baseUrl.substring(0, baseUrl.length() - 1) : baseUrl;
        HttpClient httpClient = HttpClient.newBuilder()
                .connectTimeout(CONNECT_TIMEOUT)
                .build();
        JdkClientHttpRequestFactory factory = new JdkClientHttpRequestFactory(httpClient);
        factory.setReadTimeout(READ_TIMEOUT);
        this.client = RestClient.builder()
                .baseUrl(this.baseUrl)
                .requestFactory(factory)
                .build();
    }

    @Override
    public AgentCard card() {
        if (card == null) {
            synchronized (this) {
                if (card == null) {
                    try {
                        String json = client.get()
                                .uri("/.well-known/agent.json")
                                .retrieve()
                                .body(String.class);
                        JsonNode root = MAPPER.readTree(json);
                        card = new AgentCard(
                                root.path("name").asText("unknown"),
                                root.path("description").asText(""),
                                baseUrl);
                    } catch (Exception e) {
                        // 不缓存失败结果：下次调用重试，网络抖动可自愈
                        log.warn("Agent Card 获取失败（不缓存，下次重试）: {} -> {}", baseUrl, e.getMessage());
                    }
                }
            }
        }
        return card != null ? card : new AgentCard("unknown", "", baseUrl);
    }

    @Override
    public String call(String task) {
        Map<String, Object> rpc = Map.of(
                "jsonrpc", "2.0",
                "id", "call-" + System.nanoTime(),
                "method", "message/send",
                "params", Map.of(
                        "message", Map.of(
                                "role", "user",
                                "parts", List.of(Map.of("type", "text", "text", task)))));
        // 重试包裹实际 HTTP 调用：传输层故障（连接/超时/5xx）自动退避重发；
        // 协议层错误（A2aProtocolException）被 ignoreExceptions 排除，不重发
        Supplier<String> guarded = Retry.decorateSupplier(RETRY, () -> doCall(rpc));
        return guarded.get();
    }

    private String doCall(Map<String, Object> rpc) {
        try {
            String body = client.post()
                    .uri(URI.create(baseUrl))
                    .body(rpc)
                    .retrieve()
                    .body(String.class);
            JsonNode root = MAPPER.readTree(body);
            // 200 响应也可能内嵌 JSON-RPC error（第三方 A2A 服务常见）：
            // 必须先识别，否则错误会被当任务结果返回主管
            if (root.has("error")) {
                throw new A2aProtocolException("远端返回 JSON-RPC 错误: "
                        + root.path("error").path("message").asText());
            }
            // 取 result.artifacts[].parts[].text 或 result.status.message 文本（演示级解析）
            JsonNode parts = root.path("result").path("artifacts");
            StringBuilder sb = new StringBuilder();
            for (JsonNode artifact : parts) {
                for (JsonNode part : artifact.path("parts")) {
                    if ("text".equals(part.path("type").asText())) {
                        sb.append(part.path("text").asText());
                    }
                }
            }
            return sb.length() > 0 ? sb.toString() : body;
        } catch (A2aProtocolException e) {
            throw e;
        } catch (Exception e) {
            throw new IllegalStateException("远程成员调用失败: " + baseUrl + " -> " + e.getMessage(), e);
        }
    }
}
