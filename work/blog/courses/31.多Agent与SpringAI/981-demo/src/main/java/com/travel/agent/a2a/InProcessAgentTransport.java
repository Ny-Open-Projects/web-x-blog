package com.travel.agent.a2a;

import io.agentscope.core.ReActAgent;
import io.agentscope.core.agent.RuntimeContext;
import io.agentscope.core.message.Msg;
import java.util.List;

/**
 * 进程内成员通道（default profile）：主管直接调用本进程内的成员 ReActAgent。
 *
 * <p>离线演示 / 单元测试使用；生产环境换成 {@link A2aHttpAgentTransport} 或
 * {@link NacosAgentRegistry} 解析出的远程通道，调用方代码不变——这正是课程里
 * 「把成员对象统一收敛为 AgentBase」的工程价值。
 */
public class InProcessAgentTransport implements AgentTransport {

    private final AgentCard card;
    private final ReActAgent agent;

    public InProcessAgentTransport(AgentCard card, ReActAgent agent) {
        this.card = card;
        this.agent = agent;
    }

    @Override
    public AgentCard card() {
        return card;
    }

    @Override
    public String call(String task) {
        Msg response = agent.call(List.of(Msg.builder().textContent(task).build()), RuntimeContext.empty()).block();
        return response == null ? "" : response.getTextContent();
    }
}
