package com.riskbot.service;

import com.riskbot.domain.RiskAlert;
import com.riskbot.domain.StockTick;
import com.riskbot.engine.RuleEngine;
import com.riskbot.provider.QuoteProvider;
import io.github.resilience4j.circuitbreaker.CallNotPermittedException;
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.function.Supplier;

/**
 * 风控编排服务（决策层）：把「行情(tick) -> 规则引擎 -> 告警」串成闭环。
 * 单 tick 评估用 resilience4j 熔断器包裹：规则引擎异常时降级返回空，避免一条脏
 * 数据拖垮整轮扫描（生产弹性）。
 */
@Service
public class RiskEvaluationService {

    private static final Logger log = LoggerFactory.getLogger(RiskEvaluationService.class);

    private final QuoteProvider quoteProvider;
    private final RuleEngine ruleEngine;
    private final CircuitBreaker circuitBreaker;

    /** 运行时由 Spring 注入受管熔断注册表（来自 RiskBotApplication 显式声明的 bean）。 */
    @Autowired
    public RiskEvaluationService(QuoteProvider quoteProvider, RuleEngine ruleEngine, CircuitBreakerRegistry registry) {
        this.quoteProvider = quoteProvider;
        this.ruleEngine = ruleEngine;
        this.circuitBreaker = registry.circuitBreaker("risk-eval");
    }

    /** 兼容无 Spring 上下文的单元测试：使用默认熔断注册表。 */
    public RiskEvaluationService(QuoteProvider quoteProvider, RuleEngine ruleEngine) {
        this(quoteProvider, ruleEngine, CircuitBreakerRegistry.ofDefaults());
    }

    /** 扫描当前全部 tick，返回所有命中告警。 */
    public List<RiskAlert> scanAll() {
        return quoteProvider.nextTicks().stream()
                .map(this::evaluate)
                .flatMap(List::stream)
                .toList();
    }

    /** 按代码查询。 */
    public List<RiskAlert> evaluate(String symbol) {
        return quoteProvider.nextTicks().stream()
                .filter(t -> t.symbol().equalsIgnoreCase(symbol))
                .findFirst()
                .map(this::evaluate)
                .orElse(List.of());
    }

    /** 对单笔 tick 评估（熔断保护）。 */
    public List<RiskAlert> evaluate(StockTick tick) {
        try {
            return CircuitBreaker.decorateSupplier(circuitBreaker, () -> ruleEngine.evaluate(tick)).get();
        } catch (CallNotPermittedException e) {
            // 熔断 OPEN 期间的快速失败：正常降级路径，warn 一行即可（不打堆栈，避免 30s 一轮刷屏）
            log.warn("熔断 OPEN，跳过评估（symbol={}），等待半开探测", tick.symbol());
            return List.of();
        } catch (Exception e) {
            // 关键：异常必须可见——风控场景里静默吞掉 = 漏报真实风险。
            // 降级返回空列表（单条脏数据不拖垮整轮），但必须记完整堆栈供排查。
            log.error("规则引擎评估失败，降级为空（symbol={}）", tick.symbol(), e);
            return List.of();
        }
    }
}
