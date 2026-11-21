package com.riskbot.engine;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import org.springframework.beans.factory.InitializingBean;

import org.springframework.beans.factory.InitializingBean;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;
import java.util.Optional;

/**
 * 涨跌幅异动规则：|涨跌幅| 超阈值 -> WARNING；超 2 倍阈值 -> DANGER。
 */
@Component
public class PriceVolatilityRule implements RiskRule, InitializingBean {

    @Value("${risk.rules.price-change-threshold:5.0}")
    private BigDecimal threshold = new BigDecimal("5.0");

    @Override
    public void afterPropertiesSet() {
        // 启动期 fail-fast：阈值 <= 0 会造成全市场告警风暴，宁可不启动
        if (threshold == null || threshold.signum() <= 0) {
            throw new IllegalStateException("risk.rules.price-change-threshold 必须为正数，当前值: " + threshold);
        }
    }

    @Override
    public String name() {
        return "涨跌幅异动";
    }

    @Override
    public Optional<RiskAlert> evaluate(StockTick tick) {
        BigDecimal cp = tick.changePct().abs();
        if (cp.compareTo(threshold) > 0) {
            String level = cp.compareTo(threshold.multiply(BigDecimal.valueOf(2))) > 0 ? "DANGER" : "WARNING";
            return Optional.of(new RiskAlert(
                    tick.symbol(), tick.market(), level,
                    List.of(String.format("涨跌幅 %.2f%% 超过阈值 %.2f%%", tick.changePct(), threshold)),
                    tick, Instant.now()));
        }
        return Optional.empty();
    }
}
