package com.travel.agent;

import static org.assertj.core.api.Assertions.assertThat;

import com.travel.agent.agent.SupervisorAgent;
import com.travel.agent.agent.SupervisorTools;
import com.travel.agent.agent.TeamMembers;
import com.travel.agent.config.AgentProperties;
import com.travel.agent.tool.AttractionTools;
import com.travel.agent.tool.RouteMakingTools;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.agent.RuntimeContext;
import io.agentscope.core.tool.Toolkit;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.test.context.ActiveProfiles;

/**
 * 离线链路验证（default profile，不需要 API Key）：
 * <ol>
 *   <li>成员 Agent 独立运转：ReAct 循环调用自己的工具并汇总；</li>
 *   <li>主管 Agent 调度成员：Tool 调用 → 进程内通道 → 成员返回 → 汇总；</li>
 *   <li>A2A 端点：well-known Agent Card 与 JSON-RPC message/send 可用；</li>
 *   <li>REST：用户接口返回规划结果。</li>
 * </ol>
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test-offline")
class TravelPlanningFlowTest {

    @LocalServerPort
    private int port;

    private final TestRestTemplate rest = new TestRestTemplate();

    @Autowired
    private ReActAgent routeMakingAgent;

    @Autowired
    private ReActAgent attractionAgent;

    @Test
    void memberAgent_runsReactLoopOffline() {
        String result = routeMakingAgent
                .call(List.of(io.agentscope.core.message.Msg.builder().textContent("规划杭州东站到西湖的路线").build()),
                        RuntimeContext.empty())
                .block()
                .getTextContent();
        assertThat(result).contains("路线");
    }

    @Test
    void attractionAgent_runsReactLoopOffline() {
        String result = attractionAgent
                .call(List.of(io.agentscope.core.message.Msg.builder().textContent("推荐杭州自然风光景点").build()),
                        RuntimeContext.empty())
                .block()
                .getTextContent();
        assertThat(result).contains("景点").contains("西湖");
    }

    @Test
    void supervisor_dispatchesToMembers() {
        ReActAgent supervisor = buildSupervisorOffline();
        String plan = supervisor
                .call(List.of(io.agentscope.core.message.Msg.builder().textContent("帮我规划杭州三天行程，含景点和路线").build()),
                        RuntimeContext.empty())
                .block()
                .getTextContent();
        assertThat(plan).contains("行程规划");
    }

    @Test
    void a2a_wellKnownCardAndJsonRpc() {
        String card = rest.getForObject("http://localhost:" + port + "/a2a/RouteMakingAgent/.well-known/agent.json", String.class);
        assertThat(card).contains("RouteMakingAgent");

        Map<String, Object> rpc = Map.of(
                "jsonrpc", "2.0",
                "id", "test-1",
                "method", "message/send",
                "params", Map.of("message", Map.of("role", "user", "parts", java.util.List.of(Map.of("type", "text", "text", "西湖到灵隐寺怎么走")))));
        @SuppressWarnings("unchecked")
        Map<String, Object> resp = rest.postForObject(
                "http://localhost:" + port + "/a2a/RouteMakingAgent", rpc, Map.class);
        assertThat(resp).containsKey("result");
    }

    @Test
    void restApi_planEndpoint() {
        @SuppressWarnings("unchecked")
        Map<String, Object> resp = rest.postForObject(
                "http://localhost:" + port + "/api/travel/plan",
                Map.of("requirement", "杭州三日游，要景点推荐"),
                Map.class);
        assertThat(resp.get("plan").toString()).contains("行程规划");
    }

    /** 用离线模型手搓主管（不依赖 Spring 容器，验证调度逻辑本身）。 */
    private ReActAgent buildSupervisorOffline() {
        AgentProperties props = new AgentProperties();
        props.setModelMode("offline");

        Toolkit routeToolkit = new Toolkit();
        routeToolkit.registerTool(new RouteMakingTools(new com.travel.agent.config.BaiduMapProperties()));
        ReActAgent routeMember = ReActAgent.builder()
                .name(TeamMembers.ROUTE_MAKING_AGENT)
                .sysPrompt("路线专员")
                .model(new com.travel.agent.model.OfflineChatModel(
                        "offline-route-making",
                        TeamMembers.offlineRouteDecider()))
                .toolkit(routeToolkit)
                .build();

        Toolkit attToolkit = new Toolkit();
        attToolkit.registerTool(new AttractionTools());
        ReActAgent attMember = ReActAgent.builder()
                .name(TeamMembers.ATTRACTION_AGENT)
                .sysPrompt("景点专员")
                .model(new com.travel.agent.model.OfflineChatModel(
                        "offline-attraction",
                        TeamMembers.offlineAttractionDecider()))
                .toolkit(attToolkit)
                .build();

        com.travel.agent.a2a.InProcessAgentRegistry registry = new com.travel.agent.a2a.InProcessAgentRegistry();
        registry.register(new com.travel.agent.a2a.InProcessAgentTransport(
                TeamMembers.routeCard("local"), routeMember));
        registry.register(new com.travel.agent.a2a.InProcessAgentTransport(
                TeamMembers.attractionCard("local"), attMember));

        io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry cbr =
                io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry.ofDefaults();
        // 离线测试无 Nacos bean：ObjectProvider 传空实现（stream() 为空即走不到远程分支）
        SupervisorTools tools = new SupervisorTools(registry, emptyNacosProvider(), cbr);

        Toolkit supervisorToolkit = new Toolkit();
        supervisorToolkit.registerTool(tools);
        return ReActAgent.builder()
                .name(SupervisorAgent.TRAVEL_MANAGER_AGENT)
                .sysPrompt("旅行主管")
                .model(new com.travel.agent.model.OfflineChatModel(
                        "offline-supervisor", SupervisorAgent.supervisorDecider()))
                .toolkit(supervisorToolkit)
                .build();
    }

    /** 无 Nacos 环境的 ObjectProvider 空实现（stream() 恒空，模拟 discovery=in-process）。 */
    private static org.springframework.beans.factory.ObjectProvider<com.travel.agent.a2a.NacosAgentRegistry>
            emptyNacosProvider() {
        return new org.springframework.beans.factory.ObjectProvider<>() {
            @Override
            public com.travel.agent.a2a.NacosAgentRegistry getObject() {
                return null;
            }

            @Override
            public com.travel.agent.a2a.NacosAgentRegistry getObject(Object... args) {
                return null;
            }

            @Override
            public com.travel.agent.a2a.NacosAgentRegistry getIfAvailable() {
                return null;
            }

            @Override
            public com.travel.agent.a2a.NacosAgentRegistry getIfUnique() {
                return null;
            }

            @Override
            public java.util.stream.Stream<com.travel.agent.a2a.NacosAgentRegistry> stream() {
                return java.util.stream.Stream.empty();
            }

            @Override
            public java.util.Iterator<com.travel.agent.a2a.NacosAgentRegistry> iterator() {
                return java.util.Collections.emptyIterator();
            }
        };
    }
}
