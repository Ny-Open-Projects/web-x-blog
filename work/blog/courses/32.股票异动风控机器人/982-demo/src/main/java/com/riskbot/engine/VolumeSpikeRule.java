package com.riskbot.engine;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.time.Instant;
import java.util.List;
import java.util.Optional;

/**
 * 成交量异动规则：成交量超过基准量的 ratio 倍 -> WARNING。
 * 演示用基准 800 万手，生产应改为滚动均值或配置项（已支持 risk.rules.volume-spike-base 外置）。
 */
@Component
public class VolumeSpikeRule implements RiskRule, InitializingBean {

    @Value("${risk.rules.volume-spike-ratio:2.0}")
    private double ratio = 2.0;

    @Value("${risk.rules.volume-spike-base:8000000}")
    private long baseVolume = 8_000_000L;

    /**
     * 启动期校验：ratio 为 NaN 或 <= 0 时规则会静默失效（恒 false）或误报风暴（恒 true），
     * 必须在启动时炸出来，而不是等线上漏报。
     */
    @Override
    public void afterPropertiesSet() {
        if (!(ratio > 0)) { // 同时覆盖 NaN 与 <= 0
            throw new IllegalStateException("risk.rules.volume-spike-ratio 必须为正数，当前值: " + ratio);
        }
        if (baseVolume <= 0) {
            throw new IllegalStateException("risk.rules.volume-spike-base 必须为正数，当前值: " + baseVolume);
        }
    }

    @Override
    public String name() {
        return "成交量异动";
    }

    @Override
    public Optional<RiskAlert> evaluate(StockTick tick) {
        if (tick.volume() > baseVolume * ratio) {
            return Optional.of(new RiskAlert(
                    tick.symbol(), tick.market(), "WARNING",
                    List.of(String.format("成交量 %d 超过基准 %d 的 %.1f 倍", tick.volume(), baseVolume, ratio)),
                    tick, Instant.now()));
        }
        return Optional.empty();
    }
}
