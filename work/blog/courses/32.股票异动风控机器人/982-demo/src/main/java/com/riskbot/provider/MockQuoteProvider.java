package com.riskbot.provider;

import com.riskbot.domain.StockTick;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;

/**
 * 离线 mock 行情源：内置样本 tick，其中 600519(+7.8%) 必中涨跌幅规则，
 * 用于 default profile 与测试证明「感知→决策→执行」主链路通。
 *
 * <p>profile 限定为 !prod：prod 下由 RealQuoteProvider 独占 QuoteProvider 注入，
 * 否则两个同类型 bean 并存会触发 NoUniqueBeanDefinitionException 导致启动失败。</p>
 */
@Component
@Profile("!prod")
public class MockQuoteProvider implements QuoteProvider {

    @Override
    public String market() {
        return "MOCK";
    }

    @Override
    public List<StockTick> nextTicks() {
        return List.of(
                // 涨 7.8% -> 命中涨跌幅异动
                new StockTick("600519", "A", new BigDecimal("1680.00"), new BigDecimal("7.8"), 12_000_000, Instant.now()),
                // 正常
                new StockTick("AAPL", "US", new BigDecimal("229.50"), new BigDecimal("-2.1"), 48_000_000, Instant.now()),
                // 正常
                new StockTick("000001", "A", new BigDecimal("11.20"), new BigDecimal("1.2"), 6_500_000, Instant.now())
        );
    }
}
