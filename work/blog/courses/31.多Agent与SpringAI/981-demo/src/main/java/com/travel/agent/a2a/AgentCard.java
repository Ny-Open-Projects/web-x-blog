package com.travel.agent.a2a;

/**
 * A2A Agent Card（对应课程 11-2：团队成员基于 A2A 协议注册到 Nacos 时声明的能力名片）。
 *
 * <p>字段对齐 A2A 规范的 Agent Card 最小集：name / description / 服务基址。
 */
public record AgentCard(String name, String description, String baseUrl) {

    public String toJson() {
        return """
                {"name":"%s","description":"%s","url":"%s","capabilities":{"streaming":true}}\
                """.formatted(name, description, baseUrl);
    }
}
