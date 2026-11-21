package com.riskbot.config;

import io.github.resilience4j.core.IntervalFunction;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.Duration;

/**
 * 行情网关弹性配置：真实行情拉取链路的重试策略（与 LLM 通道 {@code LlmResilienceConfig} 同构）。
 * <ul>
 *   <li>指数退避（首次 {@code risk.quote.retry.wait-ms}，逐次 ×2）+ 限次
 *       （{@code risk.quote.retry.max-attempts}）：兜住瞬时网络抖动与行情网关 5xx；</li>
 *   <li>对全部异常重试：连接失败、超时、5xx 都值得再试；</li>
 *   <li>手动 core API 装配，规避 Boot 4 下 resilience4j starter 的兼容问题。</li>
 * </ul>
 */
@Configuration
public class QuoteResilienceConfig {

    @Bean
    public Retry riskQuoteRetry(
            @Value("${risk.quote.retry.max-attempts:3}") int maxAttempts,
            @Value("${risk.quote.retry.wait-ms:500}") long waitMs) {
        return Retry.of("riskQuote", RetryConfig.custom()
                .maxAttempts(maxAttempts)
                .intervalFunction(IntervalFunction.ofExponentialBackoff(waitMs, 2.0))
                .build());
    }
}
