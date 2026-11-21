package com.travel.agent;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.travel.agent.common.LlmTokenBudget;
import com.travel.agent.common.TokenBudgetExceededException;
import com.travel.agent.model.TokenBudgetModel;
import io.agentscope.core.message.Msg;
import io.agentscope.core.message.TextBlock;
import io.agentscope.core.model.ChatResponse;
import io.agentscope.core.model.ChatUsage;
import io.agentscope.core.model.GenerateOptions;
import io.agentscope.core.model.Model;
import io.agentscope.core.model.ToolSchema;
import java.util.List;
import org.junit.jupiter.api.Test;
import reactor.core.publisher.Flux;

/**
 * {@link TokenBudgetModel} 装饰器单测：验证它位于模型调用内部、能读到 usage 并记账，
 * 且预算耗尽时拦截（抛 {@link TokenBudgetExceededException}）。这正是 981 接入 Token
 * 上限的关键——AgentScope 内部循环不向应用层暴露 usage，但装饰器作为「模型」能看到每一轮。
 */
class TokenBudgetModelTest {

    /** 固定返回带 usage 的单条响应的假模型。 */
    static final class FakeModel implements Model {
        private final ChatUsage usage;

        FakeModel(ChatUsage usage) {
            this.usage = usage;
        }

        @Override
        public Flux<ChatResponse> stream(List<Msg> messages, List<ToolSchema> tools, GenerateOptions options) {
            ChatResponse resp = ChatResponse.builder()
                    .id("r1")
                    .content(List.of(TextBlock.builder().text("ok").build()))
                    .usage(usage)
                    .build();
            return Flux.just(resp);
        }

        @Override
        public String getModelName() {
            return "fake-model";
        }

        @Override
        public boolean supportsNativeStructuredOutput() {
            return true;
        }

        @Override
        public int getContextWindowSize() {
            return 4096;
        }
    }

    @Test
    void recordsUsageFromEachResponse() {
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        TokenBudgetModel wrapped = new TokenBudgetModel(new FakeModel(new ChatUsage(5, 7, 20)), budget);

        ChatResponse r = wrapped.stream(List.of(), List.of(), null)
                .blockFirst();

        assertThat(r).isNotNull();
        assertThat(budget.used()).isEqualTo(12); // 离线回退 input+output
        // 透传方法
        assertThat(wrapped.getModelName()).isEqualTo("fake-model");
        assertThat(wrapped.supportsNativeStructuredOutput()).isTrue();
        assertThat(wrapped.getContextWindowSize()).isEqualTo(4096);
    }

    @Test
    void blocksWhenBudgetExhausted() {
        // 语义：调用前检查「当前已用量」，已超预算则拒绝发起新调用（不是中途掐断单次）
        LlmTokenBudget budget = new LlmTokenBudget(5);
        budget.record(new ChatUsage(5, 5, 10)); // 预置已用 10，超过上限 5
        TokenBudgetModel wrapped = new TokenBudgetModel(new FakeModel(new ChatUsage(5, 7, 20)), budget);

        assertThatThrownBy(() -> wrapped
                .stream(List.of(), List.of(), null)
                .blockFirst())
                .isInstanceOf(TokenBudgetExceededException.class);
    }
}
