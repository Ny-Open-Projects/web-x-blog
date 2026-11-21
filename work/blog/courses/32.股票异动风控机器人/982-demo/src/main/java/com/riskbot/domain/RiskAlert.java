package com.riskbot.domain;

import java.time.Instant;
import java.util.List;

/**
 * 风控告警（决策层输出，执行层消费）。
 */
public record RiskAlert(
        String symbol,
        String market,
        String level,         // WARNING / DANGER
        List<String> reasons,
        StockTick tick,
        Instant timestamp
) {
}
