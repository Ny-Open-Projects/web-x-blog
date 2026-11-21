package com.travel.agent.web;

import com.travel.agent.a2a.InProcessAgentRegistry;
import com.travel.agent.agent.SupervisorAgent;
import com.travel.agent.common.BizException;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.agent.RuntimeContext;
import io.agentscope.core.message.Msg;
import java.util.List;
import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * 用户交互接口（课程 13-2：主管 Agent 暴露和用户交互的接口）。
 */
@RestController
@RequestMapping("/api/travel")
public class TravelController {

    private final ReActAgent supervisor;
    private final InProcessAgentRegistry registry;

    public TravelController(ReActAgent travelManagerAgent, InProcessAgentRegistry registry) {
        this.supervisor = travelManagerAgent;
        this.registry = registry;
    }

    /**
     * 提交旅行需求，主管统筹成员生成规划。
     * required=false：空 body 放行为 null，由下方校验统一收敛 400（否则参数解析阶段抛异常走 500）。
     */
    @PostMapping("/plan")
    public Map<String, Object> plan(@RequestBody(required = false) Map<String, String> body) {
        String requirement = body == null ? "" : body.getOrDefault("requirement", "");
        if (requirement.isBlank() || requirement.length() > 2000) {
            throw new BizException("requirement 不能为空且长度不超过 2000");
        }
        Msg response = supervisor.call(List.of(Msg.builder().textContent(requirement).build()), RuntimeContext.empty()).block();
        String plan = response == null ? "" : response.getTextContent();
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("supervisor", SupervisorAgent.TRAVEL_MANAGER_AGENT);
        result.put("requirement", requirement);
        result.put("plan", plan);
        return result;
    }

    /** 查看当前发现的团队成员（课程 11-3：主管获取团队成员）。 */
    @GetMapping("/members")
    public Map<String, Object> members() {
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("members", registry.listMembers());
        return result;
    }
}
