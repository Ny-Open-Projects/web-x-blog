package com.carl.ai.transfer.common;

import org.junit.jupiter.api.Test;
import org.springframework.ai.chat.metadata.DefaultUsage;
import org.springframework.ai.chat.metadata.Usage;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Token 预算组件单测：验证「调用前检查 + 调用后记账 + 离线无 usage 不计」三件事。
 */
class LlmTokenBudgetTest {

    @Test
    void checkBudgetPassesWhenUnderLimit() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        assertDoesNotThrow(budget::checkBudget);
    }

    @Test
    void checkBudgetThrowsWhenExhausted() {
        LlmTokenBudget budget = new LlmTokenBudget(0);
        assertThrows(TokenBudgetExceededException.class, budget::checkBudget);
    }

    @Test
    void recordAddsTotalTokens() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        Usage usage = new DefaultUsage(10, 20, 30);
        budget.record(usage);
        assertEquals(30, budget.used());
        assertEquals(70, budget.remaining());
    }

    @Test
    void recordIgnoresNullUsage() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.record(null);
        assertEquals(0, budget.used());
    }
}
