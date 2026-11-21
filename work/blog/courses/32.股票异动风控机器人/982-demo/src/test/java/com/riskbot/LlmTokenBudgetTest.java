package com.riskbot;

import com.riskbot.common.LlmTokenBudget;
import com.riskbot.common.TokenBudgetExceededException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.ai.chat.metadata.DefaultUsage;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * Token 预算组件测试：累计、拦截、null 安全、剩余量。
 */
class LlmTokenBudgetTest {

    @Test
    @DisplayName("累计记账：remaining 随调用递减")
    void accumulatesUsage() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.record(new DefaultUsage(10, 20, 30));

        assertEquals(30, budget.used());
        assertEquals(70, budget.remaining());
    }

    @Test
    @DisplayName("超限拦截：checkBudget 抛 TokenBudgetExceededException")
    void checkBudgetThrowsWhenExhausted() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.record(new DefaultUsage(50, 50, 100));

        TokenBudgetExceededException e = assertThrows(TokenBudgetExceededException.class, budget::checkBudget);
        assertEquals(true, e.getMessage().contains("100"), "文案应带上限值: " + e.getMessage());
    }

    @Test
    @DisplayName("未超限不拦截")
    void checkBudgetPassesUnderLimit() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.record(new DefaultUsage(10, 20, 30));
        budget.checkBudget(); // 不抛即通过
        assertEquals(30, budget.used());
    }

    @Test
    @DisplayName("null usage 安全：离线模型无元数据时记 0，不炸链路")
    void nullUsageIsSafe() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.record(null);
        assertEquals(0, budget.used());
        budget.checkBudget();
    }
}
