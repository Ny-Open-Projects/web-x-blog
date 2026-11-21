package com.travel.agent.a2a;

import com.alibaba.nacos.api.naming.NamingService;
import com.alibaba.nacos.api.naming.pojo.Instance;
import com.alibaba.nacos.api.NacosFactory;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Nacos 成员注册表（prod profile）：对应课程 11-2「团队成员基于 A2A 协议注册到 Nacos」、
 * 11-3「主管 Agent 基于 A2A 协议获取团队成员」。
 *
 * <p>成员容器启动时以服务名 {@code a2a-<AgentName>} 注册本机地址；主管从这里解析健康实例，
 * 封装为 {@link A2aHttpAgentTransport} 调用。课程代码中的 {@code NacosAgentCardResolver}
 * 即承担同样的职责。
 *
 * <p>工程加固：① 客户端创建失败不再向上抛（否则 bean 构造失败 = Spring 上下文启动失败），
 * 降级为「远程发现不可用」，进程仍可以 in-process 模式本地运行；
 * ② resolve 结果按成员名缓存 transport，避免每次调用都走一次 Nacos 网络往返；
 * ③ close() 做显式注销——Nacos 3.x 的 NamingService 没有 shutdown()（客户端由 SDK
 * 内部托管为长生命周期单例），停机时 deregister 让注册中心立即剔除本节点，
 * 不必等临时实例心跳过期。</p>
 */
public class NacosAgentRegistry {

    private static final Logger log = LoggerFactory.getLogger(NacosAgentRegistry.class);

    /** 本进程注册过的实例，停机时用于显式注销。 */
    private record Registered(String serviceName, String ip, int port) {
    }

    private final NamingService namingService; // 客户端创建失败时为 null，方法级降级
    private final Map<String, AgentTransport> transportCache = new ConcurrentHashMap<>();
    private final Set<Registered> registered = ConcurrentHashMap.newKeySet();

    public NacosAgentRegistry(String serverAddr) {
        NamingService created = null;
        try {
            created = NacosFactory.createNamingService(serverAddr);
            log.info("Nacos 客户端已连接: {}", serverAddr);
        } catch (Exception e) {
            // 关键：不让 Nacos 不可用杀死整个应用——本地(in-process)链路仍可用
            log.error("Nacos 客户端创建失败（{}），远程成员发现降级为不可用，本地链路不受影响",
                    serverAddr, e);
        }
        this.namingService = created;
    }

    /** 把本进程的成员 A2A 端点注册到 Nacos（课程 11-2 的注册动作）。失败只记日志，不中断启动。 */
    public void registerSelf(String agentName, String ip, int port) {
        if (namingService == null) {
            log.warn("Nacos 客户端不可用，跳过注册: {}", agentName);
            return;
        }
        try {
            String serviceName = serviceName(agentName);
            namingService.registerInstance(serviceName, ip, port);
            registered.add(new Registered(serviceName, ip, port));
            log.info("成员已注册到 Nacos: {} -> {}:{}", serviceName, ip, port);
        } catch (Exception e) {
            log.error("成员注册 Nacos 失败: {} -> {}:{}，远程发现将拿不到本节点", agentName, ip, port, e);
        }
    }

    public Optional<AgentTransport> resolve(String name) {
        if (namingService == null) {
            return Optional.empty();
        }
        AgentTransport cached = transportCache.get(name);
        if (cached != null) {
            return Optional.of(cached);
        }
        try {
            List<Instance> instances = namingService.selectInstances(serviceName(name), true);
            if (instances.isEmpty()) {
                return Optional.empty();
            }
            Instance in = instances.get(0);
            String url = "http://" + in.getIp() + ":" + in.getPort() + "/a2a/" + name;
            AgentTransport transport = new A2aHttpAgentTransport(url);
            AgentTransport existing = transportCache.putIfAbsent(name, transport);
            return Optional.of(existing != null ? existing : transport);
        } catch (Exception e) {
            log.warn("Nacos 解析成员失败: {} -> {}", name, e.getMessage());
            return Optional.empty();
        }
    }

    /**
     * 停机时显式注销本进程注册的成员（Nacos 3.x 无 NamingService.shutdown()，
     * 注销即让注册中心剔除本节点；客户端连接由 SDK 内部托管，进程退出自然释放）。
     */
    public void close() {
        if (namingService == null || registered.isEmpty()) {
            return;
        }
        for (Registered r : registered) {
            try {
                namingService.deregisterInstance(r.serviceName(), r.ip(), r.port());
                log.info("成员已从 Nacos 注销: {} -> {}:{}", r.serviceName(), r.ip(), r.port());
            } catch (Exception e) {
                log.warn("成员注销 Nacos 失败: {}（心跳过期后仍会剔除）", r.serviceName(), e);
            }
        }
        registered.clear();
    }

    public static String serviceName(String agentName) {
        return "a2a-" + agentName;
    }
}
