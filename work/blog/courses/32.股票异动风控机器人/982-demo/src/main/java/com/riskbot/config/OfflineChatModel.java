package com.riskbot.config;

import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.metadata.ChatResponseMetadata;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.model.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import reactor.core.publisher.Flux;

import java.util.List;

/**
 * 离线占位 ChatModel：返回固定文本，仅用于 default profile 让工程「不联网也能起来」。
 * 真实问答能力在 prod profile 由 OpenAiChatModel 提供。
 */
public class OfflineChatModel implements ChatModel {

    private final String reply;

    public OfflineChatModel(String reply) {
        this.reply = reply;
    }

    @Override
    public ChatResponse call(Prompt prompt) {
        return new ChatResponse(
                List.of(new Generation(new AssistantMessage(reply))),
                ChatResponseMetadata.builder().build());
    }

    @Override
    public Flux<ChatResponse> stream(Prompt prompt) {
        return Flux.just(call(prompt));
    }
}
