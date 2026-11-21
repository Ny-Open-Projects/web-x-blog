package com.riskbot.engine;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

/**
 * 规则引擎：聚合所有 RiskRule，对一笔 tick 求并集告警。
 * Spring 自动注入全部 RiskRule 实现（可插拔扩展）。
 */
@Component
public class RuleEngine {

    private final List<RiskRule> rules;

    public RuleEngine(List<RiskRule> rules) {
        this.rules = rules;
    }

    public List<RiskAlert> evaluate(StockTick tick) {
        return rules.stream()
                .map(r -> r.evaluate(tick))
                .filter(Optional::isPresent)
                .map(Optional::get)
                .toList();
    }
}
