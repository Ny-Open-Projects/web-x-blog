package com.riskbot.config;

import org.springframework.ai.chat.model.ChatModel;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Profile;

/**
 * ChatModel 装配：default profile 用离线 stub（不联网、不填 Key），prod profile 由
 * spring-ai-starter-model-openai 的自动配置提供 OpenAiChatModel。
 * 离线 bean 标 @Primary，避免与自动配置共存时注入歧义。
 */
@Configuration
public class ChatModelConfig {

    @Bean
    @Primary
    @Profile("default")
    public ChatModel offlineChatModel() {
        return new OfflineChatModel("【离线模式】风控决策由规则引擎完成，未接入大模型。切 prod profile 并配置 SPRING_AI_OPENAI_API_KEY 后启用 Agent 问答。");
    }
}
