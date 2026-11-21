package com.riskbot;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;
import com.riskbot.engine.PriceVolatilityRule;
import com.riskbot.engine.RiskRule;
import com.riskbot.engine.RuleEngine;
import com.riskbot.provider.QuoteProvider;
import com.riskbot.service.RiskEvaluationService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * 风控编排服务的弹性测试：规则引擎异常 / 行情源异常时必须降级为空，
 * 且异常必须被服务层记录（风控场景静默吞异常 = 漏报真实风险）。
 */
class RiskEvaluationServiceTest {

    private static StockTick tick(String pct) {
        return new StockTick("600519", "A", new BigDecimal("1680"),
                new BigDecimal(pct), 12_000_000, Instant.now());
    }

    /** 故意抛异常的规则：模拟脏数据穿透到引擎内部的场景。 */
    static class ExplodingRule implements RiskRule {
        @Override
        public String name() {
            return "exploding";
        }

        @Override
        public Optional<RiskAlert> evaluate(StockTick tick) {
            throw new NullPointerException("模拟引擎内部故障");
        }
    }

    private static QuoteProvider fixedProvider(StockTick... ticks) {
        return new QuoteProvider() {
            @Override
            public String market() {
                return "TEST";
            }

            @Override
            public List<StockTick> nextTicks() {
                return List.of(ticks);
            }
        };
    }

    @Test
    @DisplayName("规则抛异常 -> 该 tick 降级为空，不向外抛")
    void ruleFailureDegradesToEmpty() {
        RiskEvaluationService svc = new RiskEvaluationService(
                fixedProvider(tick("7.8")),
                new RuleEngine(List.of(new ExplodingRule(), new PriceVolatilityRule())));
        // 7.8% 本来应命中涨跌幅规则，但同 tick 上一条规则爆炸：
        // RuleEngine 按 tick 聚合，异常由 RiskEvaluationService 熔断兜底 -> 空
        assertTrue(svc.scanAll().isEmpty());
    }

    @Test
    @DisplayName("行情源抛异常 -> scanAll 向上抛由调度器兜底（调度层已 try-catch）")
    void providerFailurePropagatesToScheduler() {
        QuoteProvider broken = new QuoteProvider() {
            @Override
            public String market() {
                return "BROKEN";
            }

            @Override
            public List<StockTick> nextTicks() {
                throw new IllegalStateException("行情网关不可用");
            }
        };
        RiskEvaluationService svc = new RiskEvaluationService(
                broken, new RuleEngine(List.of(new PriceVolatilityRule())));
        // provider 层异常不进单 tick 熔断（熔断只包 evaluate），直接抛给调度器
        org.junit.jupiter.api.Assertions.assertThrows(IllegalStateException.class, svc::scanAll);
    }

    @Test
    @DisplayName("按代码查询：命中返回告警，未命中返回空")
    void evaluateBySymbol() {
        RiskEvaluationService svc = new RiskEvaluationService(
                fixedProvider(tick("7.8"), tick("1.2")),
                new RuleEngine(List.of(new PriceVolatilityRule())));
        assertEquals(1, svc.evaluate("600519").size());
        assertTrue(svc.evaluate("000001").isEmpty());
    }
}
