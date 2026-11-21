package com.carl.ai.transfer.config;

import org.springframework.ai.chat.model.ChatModel;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

/**
 * ChatModel 装配（复刻 982-demo 的 ChatModelConfig）。
 * <ul>
 *   <li>{@code transfer.offline=true}（default profile）：用 {@link OfflineChatModel} 返回固定 JSON。</li>
 *   <li>{@code transfer.offline=false}（prod profile）：由 Spring AI 2.0.1 的自动配置基于
 *       {@code spring.ai.openai.api-key}（可选 {@code spring.ai.openai.base-url} /
 *       {@code spring.ai.openai.chat.options.model}）创建 {@code OpenAiChatModel}，
 *       无需手写 {@code OpenAiApi}（2.0 起该类已被官方 OpenAI SDK 取代）。</li>
 * </ul>
 */
@Configuration
public class ChatModelConfig {

    @Bean
    @Primary
    @ConditionalOnProperty(name = "transfer.offline", havingValue = "true")
    public ChatModel offlineChatModel() {
        // 固定合法调拨单：华北仓 → 华东仓，1 个 SKU
        String json = "{\"sourceWarehouseId\":1,\"targetWarehouseId\":2,\"status\":0,"
                + "\"transferType\":1,\"transferDate\":\"2026-10-20\","
                + "\"comment\":\"demo auto-generated\",\"createdBy\":\"agent\","
                + "\"items\":[{\"sku\":\"SKU-A\",\"qty\":10}]}";
        return new OfflineChatModel(json);
    }
}
