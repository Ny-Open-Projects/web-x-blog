package com.travel.agent.agent;

import com.travel.agent.a2a.A2aHttpAgentTransport;
import com.travel.agent.a2a.AgentTransport;
import com.travel.agent.a2a.InProcessAgentRegistry;
import com.travel.agent.a2a.NacosAgentRegistry;
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import io.agentscope.core.tool.Tool;
import io.agentscope.core.tool.ToolParam;
import java.util.function.Supplier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.stereotype.Component;

/**
 * 主管 Agent 的工具箱：每个团队成员都是一枚工具（Agent as Tool）。
 *
 * <p>对应课程 11-4「主管 Agent 调动团队成员执行任务」与 11-7「自主分发任务给远程成员」：
 * 主管在 ReAct 循环里决定把子任务分发给哪个成员，本类通过 {@link AgentTransport}
 * 完成实际调用；远程调用包了 resilience4j 熔断，成员不可用时降级提示而不是拖垮主管。
 *
 * <p>解析顺序（修复 prod 链路断裂）：先查进程内注册表，未命中再查 Nacos 远程注册表
 * （discovery=nacos 时才存在 bean）。此前只注入了 InProcessAgentRegistry，
 * prod 模式下成员走 Nacos 注册，主管永远解析不到，ask_* 恒返回「成员不可用」。</p>
 */
@Component
public class SupervisorTools {

    private static final Logger log = LoggerFactory.getLogger(SupervisorTools.class);

    private final InProcessAgentRegistry registry;
    private final ObjectProvider<NacosAgentRegistry> nacosRegistry;
    private final CircuitBreakerRegistry circuitBreakerRegistry;

    public SupervisorTools(InProcessAgentRegistry registry,
                           ObjectProvider<NacosAgentRegistry> nacosRegistry,
                           CircuitBreakerRegistry circuitBreakerRegistry) {
        this.registry = registry;
        this.nacosRegistry = nacosRegistry;
        this.circuitBreakerRegistry = circuitBreakerRegistry;
    }

    /** 让路线制定专员执行任务（课程 11-4 的远程调用）。 */
    @Tool(name = "ask_route_making_agent", description = "让路线制定专员规划路线与通勤方案")
    public String askRouteMaking(@ToolParam(name = "task", description = "任务描述，如 杭州三天路线") String task) {
        return dispatch(TeamMembers.ROUTE_MAKING_AGENT, task);
    }

    /** 让景点推荐 SubAgent 执行任务（课程 12-5）。 */
    @Tool(name = "ask_attraction_agent", description = "让景点推荐专员按城市与偏好推荐景点")
    public String askAttraction(@ToolParam(name = "task", description = "任务描述，如 杭州自然风光景点") String task) {
        return dispatch(TeamMembers.ATTRACTION_AGENT, task);
    }

    private String dispatch(String memberName, String task) {
        AgentTransport transport = registry
                .resolve(memberName)
                .or(() -> nacosRegistry.stream()
                        .flatMap(r -> r.resolve(memberName).stream())
                        .findFirst())
                .orElseThrow(() -> new IllegalStateException("团队成员未注册: " + memberName));

        // 熔断只护远程通道：进程内成员失败通常是代码缺陷，熔断它反而会把
        // 本该暴露的本地故障掩盖成"不可用"降级文案
        if (transport instanceof A2aHttpAgentTransport) {
            CircuitBreaker cb = circuitBreakerRegistry.circuitBreaker("remote-member-" + memberName);
            Supplier<String> guarded = CircuitBreaker.decorateSupplier(cb, () -> transport.call(task));
            try {
                return guarded.get();
            } catch (Exception t) {
                log.warn("远程成员调用失败: {} -> {}", memberName, t.toString());
                return degradeText(memberName, t);
            }
        }
        try {
            return transport.call(task);
        } catch (Exception t) {
            log.warn("成员调用失败: {} -> {}", memberName, t.toString());
            return degradeText(memberName, t);
        }
    }

    private String degradeText(String memberName, Throwable t) {
        return "成员「%s」暂时不可用，已停止该子任务（原因：%s）"
                .formatted(memberName, String.valueOf(t.getMessage()));
    }
}
