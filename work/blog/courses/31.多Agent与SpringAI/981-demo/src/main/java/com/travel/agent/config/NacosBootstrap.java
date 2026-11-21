package com.travel.agent.config;

import com.travel.agent.a2a.NacosAgentRegistry;
import com.travel.agent.agent.SupervisorAgent;
import com.travel.agent.agent.TeamMembers;
import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import java.net.InetAddress;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

/**
 * prod 模式启动引导（课程 11-2）：把本容器的成员 A2A 端点注册到 Nacos，
 * 让其他容器里的主管 Agent 能发现自己。
 *
 * <p>工程加固：注册失败（Nacos 宕机 / DNS 异常）只记日志不中断启动——
 * 原实现里 @PostConstruct 抛异常 = bean 初始化失败 = Spring 上下文起不来，
 * 「Nacos 挂了能否本地运行」的答案必须是可以。</p>
 */
@Component
public class NacosBootstrap {

    private static final Logger log = LoggerFactory.getLogger(NacosBootstrap.class);

    private final AgentProperties props;
    private final Environment env;
    /** discovery=in-process 时没有 NacosAgentRegistry bean，用 ObjectProvider 弱依赖。 */
    private final ObjectProvider<NacosAgentRegistry> nacosRegistry;

    public NacosBootstrap(AgentProperties props, Environment env,
                          ObjectProvider<NacosAgentRegistry> nacosRegistry) {
        this.props = props;
        this.env = env;
        this.nacosRegistry = nacosRegistry;
    }

    @PostConstruct
    public void registerToNacos() {
        if (!props.isNacos()) {
            return;
        }
        NacosAgentRegistry nacos = nacosRegistry.getIfAvailable();
        if (nacos == null) {
            log.warn("discovery=nacos 但 NacosAgentRegistry bean 不存在，跳过注册");
            return;
        }
        try {
            String ip = resolveAdvertiseIp();
            int port = Integer.parseInt(env.getProperty("server.port", "8080"));
            nacos.registerSelf(TeamMembers.ROUTE_MAKING_AGENT, ip, port);
            nacos.registerSelf(TeamMembers.ATTRACTION_AGENT, ip, port);
            log.info("团队成员已注册 Nacos（主管名={}）", SupervisorAgent.TRAVEL_MANAGER_AGENT);
        } catch (Exception e) {
            // 容器 DNS 异常 / 端口解析失败等：不阻断启动，本地链路仍可运行
            log.error("Nacos 注册流程失败，降级为本地运行", e);
        }
    }

    /**
     * 注册 IP 优先用显式配置（app.agent.advertise-ip，容器/多网卡场景必填），
     * 为空才回退 getLocalHost()——后者在容器 DNS 异常时会抛 UnknownHostException。
     */
    private String resolveAdvertiseIp() throws Exception {
        String configured = props.getAdvertiseIp();
        if (configured != null && !configured.isBlank()) {
            return configured.trim();
        }
        return InetAddress.getLocalHost().getHostAddress();
    }

    @PreDestroy
    public void shutdown() {
        nacosRegistry.ifAvailable(NacosAgentRegistry::close);
    }
}
