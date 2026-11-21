package com.riskbot.common;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.ai.chat.metadata.Usage;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.concurrent.atomic.AtomicLong;

/**
 * LLM Token 成本上限（进程内累计）：每次问答调用前检查预算，调用后记账。
 * <ul>
 *   <li>离线模型（OfflineChatModel）不带 usage 元数据，记 0，不影响预算；</li>
 *   <li>预算用 {@link AtomicLong} 累计，多线程问答入口下不会少记；</li>
 *   <li>耗尽后由调用方决定策略：982 的问答端点返回固定文案（保持 200），不硬抛。</li>
 * </ul>
 * 预算值走 {@code risk.llm.max-token-budget}，默认仅够演示，生产按成本预期调大。
 */
@Component
public class LlmTokenBudget {

    private static final Logger log = LoggerFactory.getLogger(LlmTokenBudget.class);

    private final long maxTokens;
    private final AtomicLong usedTokens = new AtomicLong();

    public LlmTokenBudget(@Value("${risk.llm.max-token-budget:200000}") long maxTokens) {
        this.maxTokens = maxTokens;
        log.info("[Token 预算] 初始化 max-token-budget={}", maxTokens);
    }

    /** 调用前检查：预算耗尽抛 {@link TokenBudgetExceededException}，别把请求发给模型。 */
    public void checkBudget() {
        if (usedTokens.get() >= maxTokens) {
            throw new TokenBudgetExceededException(
                    "LLM token 预算已用尽（%d/%d），请调高 risk.llm.max-token-budget 或等待重置"
                            .formatted(usedTokens.get(), maxTokens));
        }
    }

    /**
     * 记账：从响应元数据取 usage。模型不返回 usage（离线 stub / 部分 Provider）时按 0 记，
     * 不因 null 中断业务。
     */
    public void record(Usage usage) {
        if (usage == null) {
            return;
        }
        long total = usage.getTotalTokens() != null ? usage.getTotalTokens() : 0L;
        long now = usedTokens.addAndGet(total);
        if (now >= maxTokens) {
            log.warn("[Token 预算] 已达上限 {}/{}，后续问答将返回降级文案", now, maxTokens);
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
