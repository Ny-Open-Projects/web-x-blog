package com.riskbot.engine;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;

import java.util.Optional;

/**
 * 风控规则接口：单条规则对一笔 tick 给出 0..1 条告警。
 * 课程「风控规则引擎设计」章节 -> 规则可插拔、可配置。
 */
public interface RiskRule {
    String name();

    Optional<RiskAlert> evaluate(StockTick tick);
}
