package com.carl.ai.transfer.config;

import io.github.resilience4j.core.IntervalFunction;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.Duration;

/**
 * LLM 通道弹性配置：抽取链路的重试策略。
 * <ul>
 *   <li>指数退避（首次 {@code transfer.llm.retry.wait-ms}，逐次 ×2）+ 限次
 *       （{@code transfer.llm.retry.max-attempts}）：兜住瞬时网络抖动与 Provider 限流 429；</li>
 *   <li>对全部异常重试：连接失败、5xx、超时都值得再试；预算耗尽不走重试（调用前拦截）；</li>
 *   <li>手动 core API 装配，与熔断器一致，规避 Boot 4 下 resilience4j starter 的兼容问题。</li>
 * </ul>
 */
@Configuration
public class LlmResilienceConfig {

    @Bean
    public Retry transferLlmRetry(
            @Value("${transfer.llm.retry.max-attempts:3}") int maxAttempts,
            @Value("${transfer.llm.retry.wait-ms:500}") long waitMs) {
        return Retry.of("transferLlm", RetryConfig.custom()
                .maxAttempts(maxAttempts)
                .intervalFunction(IntervalFunction.ofExponentialBackoff(waitMs, 2.0))
                .build());
    }
}
