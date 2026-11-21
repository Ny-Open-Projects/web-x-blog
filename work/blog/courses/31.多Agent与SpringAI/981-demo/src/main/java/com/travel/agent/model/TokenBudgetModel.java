package com.travel.agent.model;

import com.travel.agent.common.LlmTokenBudget;
import io.agentscope.core.message.Msg;
import io.agentscope.core.model.ChatResponse;
import io.agentscope.core.model.GenerateOptions;
import io.agentscope.core.model.Model;
import io.agentscope.core.model.ToolSchema;
import java.util.List;
import reactor.core.publisher.Flux;

/**
 * Token 预算装饰器：包裹任意 {@link Model}，位于 ReActAgent 内部循环之中，
 * 因此能看到每次 LLM 调用的 {@link ChatResponse#getUsage()} 并自记账——
 * 这正是 981 接入 Token 上限的关键：AgentScope 的内部循环不向应用层暴露 usage，
 * 但装饰器作为「模型」被循环内部调用，天然能看到每一轮响应。
 *
 * <ul>
 *   <li>每次 stream 订阅前 {@link LlmTokenBudget#checkBudget()}：预算耗尽立即抛
 *       {@code TokenBudgetExceededException}（→ HTTP 400），不再把请求发给模型；</li>
 *   <li>每个 ChatResponse 落地后 {@link LlmTokenBudget#record}：离线模型 usage 已填、
 *       真实模型按实际计，两者统一累计；</li>
 *   <li>其余方法透传委托对象，不改变 ReAct 循环的任何行为。</li>
 * </ul>
 */
public class TokenBudgetModel implements Model {

    private final Model delegate;
    private final LlmTokenBudget budget;

    public TokenBudgetModel(Model delegate, LlmTokenBudget budget) {
        this.delegate = delegate;
        this.budget = budget;
    }

    @Override
    public Flux<ChatResponse> stream(List<Msg> messages, List<ToolSchema> tools, GenerateOptions options) {
        return Flux.defer(() -> {
            // 订阅时才检查：预算耗尽在真正要调模型这一刻拦截，避免白烧一轮
            budget.checkBudget();
            return delegate.stream(messages, tools, options)
                    .doOnNext(resp -> budget.record(resp == null ? null : resp.getUsage()));
        });
    }

    @Override
    public String getModelName() {
        return delegate.getModelName();
    }

    @Override
    public boolean supportsNativeStructuredOutput() {
        return delegate.supportsNativeStructuredOutput();
    }

    @Override
    public int getContextWindowSize() {
        return delegate.getContextWindowSize();
    }
}
