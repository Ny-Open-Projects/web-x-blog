package com.travel.agent.a2a;

/**
 * 团队成员调用通道：主管 Agent 不关心成员在进程内还是在远程，只按 Agent Card 调用
 * （对应课程 11-3 / 11-4：主管 Agent 获取并调度远程成员）。
 */
public interface AgentTransport {

    /** 成员的能力名片（A2A Agent Card）。 */
    AgentCard card();

    /**
     * 让成员执行任务并返回文本结果。
     *
     * @param task 主管分发的任务描述（prompt）
     */
    String call(String task);
}
