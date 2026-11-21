package com.travel.agent.config;

import com.travel.agent.a2a.AgentTransport;
import com.travel.agent.a2a.InProcessAgentRegistry;
import com.travel.agent.a2a.NacosAgentRegistry;
import com.travel.agent.agent.TeamMembers;
import io.agentscope.core.ReActAgent;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import java.time.Duration;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

/**
 * 装配：熔断注册表、成员注册表（进程内/Nacos 两种发现模式）。
 */
@Configuration
@EnableConfigurationProperties({AgentProperties.class, RiskResilienceProperties.class, BaiduMapProperties.class})
public class AgentConfig {

    @Bean
    @ConditionalOnMissingBean(CircuitBreakerRegistry.class)
    public CircuitBreakerRegistry circuitBreakerRegistry(RiskResilienceProperties props) {
        CircuitBreakerConfig config = CircuitBreakerConfig.custom()
                .failureRateThreshold(props.getFailureRateThreshold())
                .waitDurationInOpenState(props.getWaitDurationInOpenState())
                .slidingWindowSize(props.getSlidingWindowSize())
                .minimumNumberOfCalls(props.getMinimumNumberOfCalls())
                .build();
        return CircuitBreakerRegistry.of(config);
    }

    /**
     * Nacos 成员注册表（discovery=nacos 时才创建）。
     *
     * <p>放在 Spring 管理下而不是各处 new：① 构造失败不再炸启动（类内降级）；
     * ② NacosBootstrap 注册、SupervisorTools 解析共享同一个客户端；
     * ③ 停机时可统一 close。</p>
     *
     * <p>注意：havingValue 与 AgentProperties.isNacos() 同为小写 "nacos" 语义，
     * 配置时请统一写 nacos。</p>
     */
    @Bean
    @ConditionalOnProperty(name = "app.agent.discovery", havingValue = "nacos")
    public NacosAgentRegistry nacosAgentRegistry(AgentProperties props) {
        return new NacosAgentRegistry(props.getNacosServerAddr());
    }

    /**
     * 成员注册表：
     * <ul>
     *   <li>in-process（默认）：把本进程成员直接注册，主管本地调用；</li>
     *   <li>nacos：成员容器通过 {@link com.travel.agent.config.NacosBootstrap} 注册到 Nacos，
     *       主管侧解析走 {@link NacosAgentRegistry} 远程通道。</li>
     * </ul>
     *
     * <p>统一按 {@code app.agent.discovery} 属性判断（不再看 profile）：
     * 避免「激活 prod profile 但 discovery=in-process」时注册表空、Nacos 不注册、
     * 主管也无远程解析的三重瘫痪组合。</p>
     */
    @Bean
    public InProcessAgentRegistry agentRegistry(
            ReActAgent routeMakingAgent, ReActAgent attractionAgent,
            AgentProperties props, Environment env) {
        InProcessAgentRegistry registry = new InProcessAgentRegistry();
        if (props.isNacos()) {
            // nacos 模式：远程成员经 NacosAgentRegistry 解析，本地注册表留空
            return registry;
        }
        String base = "http://localhost:" + env.getProperty("server.port", "8080");
        registry.register(new com.travel.agent.a2a.InProcessAgentTransport(
                TeamMembers.routeCard(base + "/a2a/" + TeamMembers.ROUTE_MAKING_AGENT), routeMakingAgent));
        registry.register(new com.travel.agent.a2a.InProcessAgentTransport(
                TeamMembers.attractionCard(base + "/a2a/" + TeamMembers.ATTRACTION_AGENT), attractionAgent));
        return registry;
    }
}
