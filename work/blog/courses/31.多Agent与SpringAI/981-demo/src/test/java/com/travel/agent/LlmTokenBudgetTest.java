package com.travel.agent;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.travel.agent.common.LlmTokenBudget;
import com.travel.agent.common.TokenBudgetExceededException;
import io.agentscope.core.model.ChatUsage;
import org.junit.jupiter.api.Test;

/**
 * {@link LlmTokenBudget} 纯单测：预算检查、记账、耗尽拦截、剩余额度计算。
 */
class LlmTokenBudgetTest {

    @Test
    void checkBudget_passesWhenUnderLimit() {
        LlmTokenBudget budget = new LlmTokenBudget(100);
        budget.checkBudget(); // 不抛即通过
        assertThat(budget.remaining()).isEqualTo(100);
    }

    @Test
    void checkBudget_throwsWhenExhausted() {
        LlmTokenBudget budget = new LlmTokenBudget(5);
        budget.record(new ChatUsage(5, 5, 10)); // 记 10，超过 5
        assertThat(budget.used()).isEqualTo(10);
        assertThatThrownBy(budget::checkBudget)
                .isInstanceOf(TokenBudgetExceededException.class)
                .hasMessageContaining("已用尽");
    }

    @Test
    void record_sumsInputPlusOutputWhenTotalZero() {
        // 离线 mock 用 ChatUsage(int,int,double)（input,output,time），total 常为 0，需回退求和
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        budget.record(new ChatUsage(5, 7, 10));
        assertThat(budget.used()).isEqualTo(12);
        assertThat(budget.remaining()).isEqualTo(988);
    }

    @Test
    void record_usesTotalWhenPositive() {
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        // 4 参构造为 (input, output, cached, time)；getTotalTokens() 返回 input+output = 7
        budget.record(new ChatUsage(3, 4, 9, 20));
        assertThat(budget.used()).isEqualTo(7);
    }

    @Test
    void record_nullUsageIsNoOp() {
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        budget.record(null);
        assertThat(budget.used()).isZero();
    }
}
