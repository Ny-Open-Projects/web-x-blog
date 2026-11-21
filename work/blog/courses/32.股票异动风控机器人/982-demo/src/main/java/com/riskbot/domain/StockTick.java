package com.riskbot.domain;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.Objects;

/**
 * 行情快照（感知层输入）。
 * 字段与课程「行情接入」章节一致：代码 / 市场 / 现价 / 涨跌幅 / 成交量 / 时间。
 *
 * <p>紧凑构造器 fail-fast：行情数据来自外部网关，缺字段/负价/负量必须在
 * 构造时拦截，否则脏数据会穿透到规则引擎拆箱 NPE，污染整轮扫描。</p>
 */
public record StockTick(
        String symbol,
        String market,        // A = A股, US = 美股
        BigDecimal price,
        BigDecimal changePct, // 涨跌幅 %
        long volume,
        Instant timestamp
) {
    public StockTick {
        Objects.requireNonNull(symbol, "symbol 不能为空");
        Objects.requireNonNull(price, "price 不能为空");
        Objects.requireNonNull(changePct, "changePct 不能为空");
        Objects.requireNonNull(timestamp, "timestamp 不能为空");
        if (price.signum() < 0) {
            throw new IllegalArgumentException("price 不允许为负: " + price);
        }
        if (volume < 0) {
            throw new IllegalArgumentException("volume 不允许为负: " + volume);
        }
    }
}
