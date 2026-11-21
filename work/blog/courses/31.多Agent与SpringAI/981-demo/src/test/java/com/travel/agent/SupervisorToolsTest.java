package com.travel.agent.agent;

import com.travel.agent.a2a.A2aHttpAgentTransport;
import com.travel.agent.a2a.AgentTransport;
import com.travel.agent.a2a.InProcessAgentRegistry;
import com.travel.agent.a2a.NacosAgentRegistry;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.junit.jupiter.MockitoSettings;
import org.mockito.quality.Strictness;
import org.springframework.beans.factory.ObjectProvider;

import java.util.Optional;
import java.util.function.Supplier;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * 主管工具箱分发逻辑测试（P0 修复的回归防线）：
 * ① 进程内注册表未命中时，必须回落到 Nacos 远程注册表（prod 链路断裂回归）；
 * ② 成员调用失败必须降级为「暂时不可用」文案而不是把异常抛给 ReAct 循环；
 * ③ 全部未注册时降级文案（orElseThrow 的 IllegalStateException 被 catch 成降级）。
 */
@ExtendWith(MockitoExtension.class)
@MockitoSettings(strictness = Strictness.LENIENT)
class SupervisorToolsTest {

    @Mock
    private InProcessAgentRegistry registry;

    @Mock
    private NacosAgentRegistry nacosRegistry;

    @Mock
    private CircuitBreakerRegistry circuitBreakerRegistry;

    private SupervisorTools tools;

    /** 最小 ObjectProvider stub：有值/无值两种形态。 */
    private static ObjectProvider<NacosAgentRegistry> providerOf(NacosAgentRegistry value) {
        return new ObjectProvider<>() {
            @Override
            public NacosAgentRegistry getObject() {
                return value;
            }

            @Override
            public NacosAgentRegistry getObject(Object... args) {
                return value;
            }

            @Override
            public NacosAgentRegistry getIfAvailable() {
                return value;
            }

            @Override
            public NacosAgentRegistry getIfUnique() {
                return value;
            }

            @Override
            public Stream<NacosAgentRegistry> stream() {
                return value == null ? Stream.empty() : Stream.of(value);
            }

            @Override
            public java.util.Iterator<NacosAgentRegistry> iterator() {
                return java.util.List.of(value).iterator();
            }
        };
    }

    private void buildTools(NacosAgentRegistry nacos) {
        when(circuitBreakerRegistry.circuitBreaker(any()))
                .thenReturn(io.github.resilience4j.circuitbreaker.CircuitBreaker.ofDefaults("test"));
        tools = new SupervisorTools(registry, providerOf(nacos), circuitBreakerRegistry);
    }

    @Test
    @DisplayName("P0 回归：in-process 未命中时回落到 Nacos 解析")
    void fallsBackToNacos() {
        buildTools(nacosRegistry);
        AgentTransport remote = mock(A2aHttpAgentTransport.class);
        when(remote.call("规划三天路线")).thenReturn("远程成员产出");
        when(registry.resolve(TeamMembers.ROUTE_MAKING_AGENT)).thenReturn(Optional.empty());
        when(nacosRegistry.resolve(TeamMembers.ROUTE_MAKING_AGENT)).thenReturn(Optional.of(remote));

        String result = tools.askRouteMaking("规划三天路线");

        assertTrue(result.contains("远程成员产出"), "应拿到 Nacos 远程成员产出，实际: " + result);
    }

    @Test
    @DisplayName("成员调用抛异常 -> 降级文案，不向上抛")
    void memberFailureDegrades() {
        buildTools(null);
        AgentTransport broken = mock(AgentTransport.class);
        when(broken.call(any())).thenThrow(new IllegalStateException("boom"));
        when(registry.resolve(TeamMembers.ROUTE_MAKING_AGENT)).thenReturn(Optional.of(broken));

        String result = tools.askRouteMaking("规划三天路线");

        assertTrue(result.contains("暂时不可用"), "应降级，实际: " + result);
    }

    @Test
    @DisplayName("两处注册表都解析不到 -> 抛 IllegalStateException（回灌模型自我纠正，不伪装成暂时不可用）")
    void nowhereRegisteredThrows() {
        buildTools(nacosRegistry);
        when(registry.resolve(TeamMembers.ATTRACTION_AGENT)).thenReturn(Optional.empty());
        when(nacosRegistry.resolve(TeamMembers.ATTRACTION_AGENT)).thenReturn(Optional.empty());

        org.junit.jupiter.api.Assertions.assertThrows(IllegalStateException.class,
                () -> tools.askAttraction("推荐景点"));
    }

    @Test
    @DisplayName("in-process 命中时绝不走 Nacos（本地优先）")
    void inProcessTakesPrecedence() {
        buildTools(nacosRegistry);
        AgentTransport local = mock(AgentTransport.class);
        when(local.call(any())).thenReturn("本地成员产出");
        when(registry.resolve(TeamMembers.ROUTE_MAKING_AGENT)).thenReturn(Optional.of(local));

        String result = tools.askRouteMaking("规划三天路线");

        assertTrue(result.contains("本地成员产出"));
        // nacos 不应被查询
        org.mockito.Mockito.verifyNoInteractions(nacosRegistry);
        assertFalse(result.contains("Nacos"));
    }

    @Test
    @DisplayName("无 Nacos bean（in-process 模式）时 ObjectProvider.stream() 为空，不 NPE")
    void noNacosBeanIsSafe() {
        buildTools(null);
        AgentTransport local = mock(AgentTransport.class);
        when(local.call(any())).thenReturn("本地产出");
        when(registry.resolve(TeamMembers.ROUTE_MAKING_AGENT)).thenReturn(Optional.of(local));

        String result = tools.askRouteMaking("x");

        assertTrue(result.contains("本地产出"));
    }
}
