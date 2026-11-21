package com.travel.agent.common;

import io.agentscope.core.model.ChatUsage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.concurrent.atomic.AtomicLong;

/**
 * LLM Token 成本上限（进程内累计）：每次问答调用前检查预算，调用后记账。
 *
 * <ul>
 *   <li>离线规则模型（{@code OfflineChatModel}）每次响应都带 {@code ChatUsage(10,20,30)}，
 *       按实际数字记账；真实模型按供应商返回的实际 usage 记账；</li>
 *   <li>预算用 {@link AtomicLong} 累计，多线程问答入口下不会少记；</li>
 *   <li>耗尽后 {@link #checkBudget()} 抛 {@link TokenBudgetExceededException}（→ HTTP 400），
 *       别把请求再发给模型。</li>
 * </ul>
 *
 * <p>预算值走 {@code app.agent.max-token-budget}，默认 200000（仅够演示），
 * 生产按成本预期调大；与 980/982 的 {@code risk.llm.max-token-budget} 同一思路，本工程用
 * {@code app.agent} 命名空间保持配置自洽。</p>
 */
@Component
public class LlmTokenBudget {

    private static final Logger log = LoggerFactory.getLogger(LlmTokenBudget.class);

    private final long maxTokens;
    private final AtomicLong usedTokens = new AtomicLong();

    public LlmTokenBudget(@Value("${app.agent.max-token-budget:200000}") long maxTokens) {
        this.maxTokens = maxTokens;
        log.info("[Token 预算] 初始化 max-token-budget={}", maxTokens);
    }

    /** 调用前检查：预算耗尽抛 {@link TokenBudgetExceededException}，别把请求发给模型。 */
    public void checkBudget() {
        if (usedTokens.get() >= maxTokens) {
            throw new TokenBudgetExceededException(
                    "LLM token 预算已用尽（%d/%d），请调高 app.agent.max-token-budget 或重启进程（预算进程内累计，不会自动重置）"
                            .formatted(usedTokens.get(), maxTokens));
        }
    }

    /**
     * 记账：从响应元数据取 usage。模型不返回 usage（部分 Provider）时按 0 记，不因 null 中断业务。
     * 离线 mock 用 {@code new ChatUsage(10,20,30)}（3 参构造是 input/output/time，total 可能为 0），
     * 故 total<=0 时回退 input+output 求和，保证离线也能真实累计。
     */
    public void record(ChatUsage usage) {
        if (usage == null) {
            return;
        }
        int total = usage.getTotalTokens();
        if (total <= 0) {
            total = usage.getInputTokens() + usage.getOutputTokens();
        }
        long now = usedTokens.addAndGet(total);
        if (now >= maxTokens) {
            log.warn("[Token 预算] 已达上限 {}/{}，后续问答将返回限流", now, maxTokens);
        }
    }

    public long used() {
        return usedTokens.get();
    }

    public long max() {
        return maxTokens;
    }

    public long remaining() {
        return Math.max(0, maxTokens - usedTokens.get());
    }
}
