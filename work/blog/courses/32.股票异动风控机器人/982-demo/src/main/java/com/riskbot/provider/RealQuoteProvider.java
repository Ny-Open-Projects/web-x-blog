package com.riskbot.provider;

import com.riskbot.domain.StockTick;
import io.github.resilience4j.retry.Retry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Profile;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;

import java.net.http.HttpClient;
import java.time.Duration;
import java.util.List;
import java.util.function.Supplier;

/**
 * 真实行情源（prod profile 才激活）。从配置的 REST 端点拉取并映射为 StockTick。
 * 离线 / 未配置 {@code risk.quote.api-url} 时返回空，调度器自动跳过，保证不崩。
 *
 * <p>生产加固（行情网关三重防线，与 LLM 通道同构）：
 * <ol>
 *   <li>超时配置外置：连接 / 读取超时走 {@code risk.quote.connect-timeout-ms} /
 *       {@code risk.quote.read-timeout-ms}（env 驱动），不再写死；JDK HttpClient 默认无读超时，
 *       网关挂起会拖死扫描线程，必须显式；</li>
 *   <li>重试：指数退避限次（{@code risk.quote.retry.*}），兜住瞬时网络抖动 / 行情网关 5xx；</li>
 *   <li>降级：重试耗尽或解析失败 → 本轮返回空，保住调度链与 Agent 链路可用。</li>
 * </ol>
 */
@Component
@Profile("prod")
public class RealQuoteProvider implements QuoteProvider {

    private static final Logger log = LoggerFactory.getLogger(RealQuoteProvider.class);

    private final RestClient restClient;
    private final Retry retry;
    private final String quoteApiUrl;

    @Autowired
    public RealQuoteProvider(Retry riskQuoteRetry,
            @Value("${risk.quote.api-url:}") String quoteApiUrl,
            @Value("${risk.quote.connect-timeout-ms:3000}") long connectTimeoutMs,
            @Value("${risk.quote.read-timeout-ms:5000}") long readTimeoutMs) {
        this.retry = riskQuoteRetry;
        this.quoteApiUrl = quoteApiUrl;
        // 超时配置外置 + 显式写死兜底默认值：网关挂起不能拖死扫描线程
        HttpClient httpClient = HttpClient.newBuilder()
                .connectTimeout(Duration.ofMillis(connectTimeoutMs))
                .build();
        JdkClientHttpRequestFactory factory = new JdkClientHttpRequestFactory(httpClient);
        factory.setReadTimeout(Duration.ofMillis(readTimeoutMs));
        this.restClient = RestClient.builder().requestFactory(factory).build();
    }

    /** 测试专用构造：注入预构建 RestClient 与 url（绕过 @Value / HttpClient 装配）。 */
    RealQuoteProvider(Retry retry, String quoteApiUrl, RestClient restClient) {
        this.retry = retry;
        this.quoteApiUrl = quoteApiUrl;
        this.restClient = restClient;
    }

    @Override
    public String market() {
        return "REAL";
    }

    @Override
    public List<StockTick> nextTicks() {
        if (quoteApiUrl == null || quoteApiUrl.isBlank()) {
            return List.of();
        }
        try {
            // 重试包住真实拉取：瞬时故障自愈；耗尽后由外层 catch 降级为空
            Supplier<List<StockTick>> guarded = Retry.decorateSupplier(retry, this::doFetch);
            return guarded.get();
        } catch (Exception e) {
            // 重试耗尽 / 解析失败：本轮降级为空，保住调度链与 Agent 链路可用
            log.warn("[行情网关] 拉取失败（已重试），本轮降级为空: {}", e.getMessage());
            return List.of();
        }
    }

    /**
     * 真实拉取：从 quoteApiUrl 拉取行情并映射为 StockTick[]（按行情网关返回结构实现）。
     * 包级可见以便测试通过子类重写做确定性验证。
     */
    List<StockTick> doFetch() {
        StockTick[] ticks = restClient.get().uri(quoteApiUrl).retrieve().body(StockTick[].class);
        return ticks != null ? List.of(ticks) : List.of();
    }
}
