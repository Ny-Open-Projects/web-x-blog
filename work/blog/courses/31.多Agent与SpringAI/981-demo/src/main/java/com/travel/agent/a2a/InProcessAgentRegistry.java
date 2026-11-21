package com.travel.agent.a2a;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 进程内成员注册表（default profile）。
 *
 * <p>对应课程 11-2 的注册中心角色：主管 Agent 启动时把团队成员的 Agent Card 收拢到一处，
 * 按名字解析出调用通道。生产环境用 {@link NacosAgentRegistry} 平替，解析语义一致。
 */
public class InProcessAgentRegistry {

    private final Map<String, AgentTransport> members = new ConcurrentHashMap<>();

    public void register(AgentTransport transport) {
        members.put(transport.card().name(), transport);
    }

    /** 解析成员通道；对应课程 11-3「主管 Agent 获取团队成员」。 */
    public Optional<AgentTransport> resolve(String name) {
        return Optional.ofNullable(members.get(name));
    }

    /** 列出全部成员名片（对应课程里打印远程智能体描述）。 */
    public List<AgentCard> listMembers() {
        return members.values().stream().map(AgentTransport::card).toList();
    }

    public boolean isEmpty() {
        return members.isEmpty();
    }
}
