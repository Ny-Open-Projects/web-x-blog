package com.carl.ai.transfer.config;

import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.metadata.ChatResponseMetadata;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.messages.AssistantMessage;
import reactor.core.publisher.Flux;

import java.util.List;

/**
 * 离线 ChatModel（复刻 982-demo 的 OfflineChatModel 思路）。
 * <p>
 * 实现 Spring AI 2.0.1 的 {@link ChatModel} 接口，固定返回一段合法调拨单 JSON 串，
 * 使「LLM 生成 → BeanOutputConverter 提取 → MapStruct 转换 → 入库」链路在
 * <b>default profile（不联网、不填 Key）</b>下也能完整跑通。生产 prod profile 由真实模型替换。
 */
public class OfflineChatModel implements ChatModel {

    private final String cannedJson;

    public OfflineChatModel(String cannedJson) {
        this.cannedJson = cannedJson;
    }

    @Override
    public ChatResponse call(Prompt prompt) {
        AssistantMessage message = new AssistantMessage(cannedJson);
        Generation generation = new Generation(message);
        return new ChatResponse(List.of(generation), ChatResponseMetadata.builder().build());
    }

    @Override
    public Flux<ChatResponse> stream(Prompt prompt) {
        return Flux.just(call(prompt));
    }
}
