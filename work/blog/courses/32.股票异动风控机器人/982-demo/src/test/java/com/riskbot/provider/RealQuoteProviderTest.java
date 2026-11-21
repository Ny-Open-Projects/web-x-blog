package com.riskbot.provider;

import static org.assertj.core.api.Assertions.assertThat;

import com.riskbot.domain.StockTick;
import io.github.resilience4j.core.IntervalFunction;
import io.github.resilience4j.retry.Retry;
import io.github.resilience4j.retry.RetryConfig;
import java.net.http.HttpClient;
import java.time.Duration;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import org.junit.jupiter.api.Test;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.web.client.RestClient;

/**
 * {@link RealQuoteProvider} 单测（prod 行情网关）：
 * ① 空白 URL → 不发起调用直接返回空（不浪费重试）；
 * ② 瞬时故障 → 按 maxAttempts 重试后降级为空，且 doFetch 确实被调用了 N 次（确定性，不依赖网络）。
 */
class RealQuoteProviderTest {

    private static RestClient restClientWithConnectTimeout(long ms) {
        HttpClient httpClient = HttpClient.newBuilder().connectTimeout(Duration.ofMillis(ms)).build();
        JdkClientHttpRequestFactory factory = new JdkClientHttpRequestFactory(httpClient);
        return RestClient.builder().requestFactory(factory).build();
    }

    @Test
    void blankUrl_returnsEmptyWithoutCall() {
        Retry retry = Retry.of("t", RetryConfig.custom().maxAttempts(3).build());
        RealQuoteProvider provider = new RealQuoteProvider(retry, "", restClientWithConnectTimeout(200));
        assertThat(provider.nextTicks()).isEmpty();
        // 空白 URL 直接返回，根本没进重试圈
        assertThat(retry.getMetrics().getNumberOfTotalCalls()).isZero();
    }

    @Test
    void transientFailure_retriesThenDegradesToEmpty() {
        Retry retry = Retry.of("t", RetryConfig.custom()
                .maxAttempts(3)
                .intervalFunction(IntervalFunction.ofExponentialBackoff(1, 2.0))
                .build());
        // 匿名子类重写 doFetch 确定性抛异常：验证重试圈确实跑了 maxAttempts 次并降级为空
        AtomicInteger calls = new AtomicInteger();
        RealQuoteProvider provider = new RealQuoteProvider(retry, "http://dummy/quote", restClientWithConnectTimeout(200)) {
            @Override
            List<StockTick> doFetch() {
                calls.incrementAndGet();
                throw new IllegalStateException("行情网关临时不可用");
            }
        };

        List<StockTick> ticks = provider.nextTicks();

        assertThat(ticks).isEmpty();
        assertThat(calls.get()).isEqualTo(3);
    }
}
