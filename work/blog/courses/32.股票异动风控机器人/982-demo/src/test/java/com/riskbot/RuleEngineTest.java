package com.riskbot;

import com.riskbot.domain.StockTick;
import com.riskbot.engine.PriceVolatilityRule;
import com.riskbot.engine.RuleEngine;
import com.riskbot.engine.VolumeSpikeRule;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RuleEngineTest {

    private final RuleEngine engine = new RuleEngine(
            List.of(new PriceVolatilityRule(), new VolumeSpikeRule()));

    private static StockTick tick(String changePct, long volume) {
        return new StockTick("600519", "A", new BigDecimal("1680"),
                new BigDecimal(changePct), volume, Instant.now());
    }

    @Test
    void shouldDetectPriceSpike() {
        StockTick tick = tick("7.8", 12_000_000);
        assertEquals(1, engine.evaluate(tick).size());
    }

    @Test
    void shouldIgnoreNormalTick() {
        StockTick tick = tick("1.2", 6_500_000);
        assertTrue(engine.evaluate(tick).isEmpty());
    }

    @Nested
    @DisplayName("涨跌幅规则边界（阈值 5.0，>2 倍阈值 = DANGER）")
    class PriceBoundary {

        @ParameterizedTest
        @DisplayName("<= 阈值（含正好等于）不告警")
        @ValueSource(strings = {"1.2", "4.99", "5.0", "0", "-5.0"})
        void atOrBelowThresholdIsSilent(String pct) {
            // -5.0 的 |值| 正好等于阈值：严格大于才算异动，语义为"超阈值"
            assertTrue(engine.evaluate(tick(pct, 1_000_000)).isEmpty(),
                    pct + " 不应触发涨跌幅告警");
        }

        @ParameterizedTest
        @DisplayName("刚超阈值 = WARNING")
        @ValueSource(strings = {"5.01", "-5.01", "9.99", "10.0"})
        void aboveThresholdIsWarning(String pct) {
            List<com.riskbot.domain.RiskAlert> alerts = engine.evaluate(tick(pct, 1_000_000));
            assertEquals(1, alerts.size(), pct + " 应触发 1 条告警");
            assertEquals("WARNING", alerts.get(0).level(), pct + " 应为 WARNING");
        }

        @ParameterizedTest
        @DisplayName("超 2 倍阈值 = DANGER")
        @ValueSource(strings = {"10.01", "15", "-20"})
        void beyondDoubleThresholdIsDanger(String pct) {
            List<com.riskbot.domain.RiskAlert> alerts = engine.evaluate(tick(pct, 1_000_000));
            assertEquals(1, alerts.size(), pct + " 应触发 1 条告警");
            assertEquals("DANGER", alerts.get(0).level(), pct + " 应为 DANGER");
        }
    }

    @Nested
    @DisplayName("成交量规则边界（基准 800 万 × ratio 2.0 = 1600 万）")
    class VolumeBoundary {

        @ParameterizedTest
        @DisplayName("<= 基准×倍数不告警")
        @ValueSource(longs = {0, 8_000_000, 15_999_999, 16_000_000})
        void atOrBelowBaseIsSilent(long volume) {
            assertTrue(engine.evaluate(tick("1.0", volume)).isEmpty(),
                    volume + " 不应触发成交量告警");
        }

        @Test
        @DisplayName("刚超基准×倍数告警")
        void aboveBaseAlerts() {
            List<com.riskbot.domain.RiskAlert> alerts = engine.evaluate(tick("1.0", 16_000_001));
            assertEquals(1, alerts.size());
            assertEquals("WARNING", alerts.get(0).level());
        }

        @Test
        @DisplayName("价格与成交量同时命中则两条规则并集")
        void unionOfBothRules() {
            List<com.riskbot.domain.RiskAlert> alerts = engine.evaluate(tick("7.8", 20_000_000));
            assertEquals(2, alerts.size());
        }
    }

    @Nested
    @DisplayName("StockTick 紧凑构造器 fail-fast")
    class StockTickValidation {

        @Test
        void rejectsNullChangePct() {
            assertThrows(NullPointerException.class, () ->
                    new StockTick("600519", "A", new BigDecimal("1680"), null, 100, Instant.now()));
        }

        @Test
        void rejectsNegativePriceOrVolume() {
            assertThrows(IllegalArgumentException.class, () ->
                    new StockTick("600519", "A", new BigDecimal("-1"), new BigDecimal("1"), 100, Instant.now()));
            assertThrows(IllegalArgumentException.class, () ->
                    new StockTick("600519", "A", new BigDecimal("1"), new BigDecimal("1"), -100, Instant.now()));
        }

        @Test
        void acceptsValidTick() {
            StockTick t = tick("0", 0);
            assertFalse(t.symbol().isEmpty());
        }
    }
}
