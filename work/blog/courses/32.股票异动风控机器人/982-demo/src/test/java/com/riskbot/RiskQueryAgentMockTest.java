package com.riskbot;

import com.riskbot.agent.RiskQueryAgent;
import com.riskbot.common.LlmTokenBudget;
import com.riskbot.domain.RiskAlert;
import com.riskbot.engine.PriceVolatilityRule;
import com.riskbot.engine.RuleEngine;
import com.riskbot.engine.VolumeSpikeRule;
import com.riskbot.provider.MockQuoteProvider;
import com.riskbot.service.RiskEvaluationService;
import io.github.resilience4j.core.IntervalFunction;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import org.junit.jupiter.api.Test;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.metadata.ChatResponseMetadata;
import org.springframework.ai.chat.metadata.DefaultUsage;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import reactor.core.publisher.Flux;

import java.time.Duration;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * 离线 mock 测试：用 StubChatModel 替代真实大模型，验证 Agent 与风控服务的链路接通。
 * 不需联网、不需 Key —— 这是「工程真能跑」的兜底证据（v3 §4.1 硬约束）。
 * 同时固化问答入口的三重防线：Token 预算、重试、降级。
 */
class RiskQueryAgentMockTest {

    /** 测试专用重试：3 次、10ms 起步（不等 500ms，用例要快）。 */
    private static Retry testRetry() {
        return Retry.of("test", RetryConfig.custom()
                .maxAttempts(3)
                .intervalFunction(IntervalFunction.ofExponentialBackoff(Duration.ofMillis(10), 2.0))
                .build());
    }

    private static RiskEvaluationService svc() {
        return new RiskEvaluationService(
                new MockQuoteProvider(),
                new RuleEngine(List.of(new PriceVolatilityRule(), new VolumeSpikeRule())));
    }

    /** 带 usage 元数据的应答：验证预算记账。 */
    static ChatResponse withUsage(String text, int total) {
        return new ChatResponse(
                List.of(new Generation(new AssistantMessage(text))),
                ChatResponseMetadata.builder()
                        .usage(new DefaultUsage(3, total - 3, total))
                        .build());
    }

    static class StubChatModel implements ChatModel {
        @Override
        public ChatResponse call(Prompt prompt) {
            return new ChatResponse(
                    List.of(new Generation(new AssistantMessage("离线应答"))),
                    ChatResponseMetadata.builder().build());
        }

        @Override
        public Flux<ChatResponse> stream(Prompt prompt) {
            return Flux.just(call(prompt));
        }
    }

    /** 模拟 LLM 通道故障：call 直接抛（对应 prod 网络异常 / 限流 / 超时）。 */
    static class ThrowingChatModel implements ChatModel {
        @Override
        public ChatResponse call(Prompt prompt) {
            throw new IllegalStateException("模拟 LLM 通道故障");
        }

        @Override
        public Flux<ChatResponse> stream(Prompt prompt) {
            return Flux.error(new IllegalStateException("模拟 LLM 通道故障"));
        }
    }

    /** 前 failTimes 次抛异常，之后返回带 usage 的正常应答：验证重试后恢复。 */
    static class FlakyChatModel implements ChatModel {
        final AtomicInteger calls = new AtomicInteger();
        final int failTimes;

        FlakyChatModel(int failTimes) {
            this.failTimes = failTimes;
        }

        @Override
        public ChatResponse call(Prompt prompt) {
            if (calls.incrementAndGet() <= failTimes) {
                throw new IllegalStateException("瞬时故障 #" + calls.get());
            }
            return withUsage("抖动后恢复的应答", 30);
        }

        @Override
        public Flux<ChatResponse> stream(Prompt prompt) {
            return Flux.just(call(prompt));
        }
    }

    @Test
    void toolReturnsRealRiskWhenInvoked() {
        RiskQueryAgent agent = new RiskQueryAgent(
                ChatClient.builder(new StubChatModel()), svc(), new LlmTokenBudget(1000), testRetry());

        // 离线模型不触发工具调用，但工具方法本身直接可用，证明「Agent->服务->规则引擎」链路通
        List<RiskAlert> alerts = agent.queryRisk("600519");
        assertFalse(alerts.isEmpty(), "600519 应命中涨跌幅异动规则");
    }

    @Test
    void askDegradesToFallbackWhenLlmFails() {
        RiskQueryAgent agent = new RiskQueryAgent(
                ChatClient.builder(new ThrowingChatModel()), svc(), new LlmTokenBudget(1000), testRetry());

        // 通道故障不得冒泡（否则 /api/risk/query 500），必须降级为固定文案
        String answer = agent.ask("茅台今天有异动吗");
        assertEquals(RiskQueryAgent.FALLBACK_ANSWER, answer);
    }

    @Test
    void askRetriesAndSucceedsOnTransientFailure() {
        FlakyChatModel flaky = new FlakyChatModel(2);
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        RiskQueryAgent agent = new RiskQueryAgent(
                ChatClient.builder(flaky), svc(), budget, testRetry());

        String answer = agent.ask("茅台今天有异动吗");

        assertEquals("抖动后恢复的应答", answer);
        assertEquals(3, flaky.calls.get(), "前两次失败后第三次应成功：重试必须真的发生");
        assertEquals(30, budget.used(), "恢复后应按 usage 记账");
    }

    @Test
    void askReturnsBudgetFallbackWhenBudgetExhausted() {
        RiskQueryAgent agent = new RiskQueryAgent(
                ChatClient.builder(new StubChatModel()), svc(), new LlmTokenBudget(0), testRetry());

        // 预算 0：调用前即被拦截，不得把请求发给模型
        String answer = agent.ask("茅台今天有异动吗");
        assertEquals(RiskQueryAgent.BUDGET_FALLBACK_ANSWER, answer);
    }

    @Test
    void askSucceedsAndRecordsUsage() {
        LlmTokenBudget budget = new LlmTokenBudget(1000);
        RiskQueryAgent agent = new RiskQueryAgent(
                ChatClient.builder(new StubChatModel()), svc(), budget, testRetry());

        String answer = agent.ask("茅台今天有异动吗");

        assertEquals("离线应答", answer);
        // StubChatModel 无 usage 元数据：记账必须 null 安全（记 0），不炸链路
        assertEquals(0, budget.used());
        assertTrue(budget.remaining() > 0);
    }
}
