package com.riskbot.scheduler;

import com.riskbot.domain.RiskAlert;
import com.riskbot.service.RiskEvaluationService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * 周期扫描调度器（感知->决策 的定时触发）。
 * 任务本身由虚拟线程 {@code TaskScheduler}（见 {@code RiskBotApplication#taskScheduler()}）承载；
 * 直接在本方法内执行，配合 {@code fixedDelay} 天然避免上一轮未跑完就触发下一轮（防重叠）。
 */
@Component
@ConditionalOnProperty(prefix = "risk.scan", name = "enabled", havingValue = "true", matchIfMissing = true)
public class RiskScanScheduler {

    private static final Logger log = LoggerFactory.getLogger(RiskScanScheduler.class);

    private final RiskEvaluationService evaluationService;

    public RiskScanScheduler(RiskEvaluationService evaluationService) {
        this.evaluationService = evaluationService;
    }

    @Scheduled(fixedDelayString = "${risk.scan.fixed-delay-ms:30000}")
    public void scan() {
        // 单轮容错：provider 或引擎异常时记日志降级，绝不让异常吃掉整轮告警
        // （风控场景漏报 = 真实风险，异常必须可见）
        try {
            List<RiskAlert> alerts = evaluationService.scanAll();
            // 每轮必打一条轮次日志：DEPLOY.md 的周期调度验收就是「grep -c 风控扫描轮次」数它
            log.info("[风控扫描轮次] 完成，本轮告警 {} 条", alerts.size());
            alerts.forEach(a -> log.warn("[风控告警] level={} symbol={} market={} reasons={}",
                    a.level(), a.symbol(), a.market(), a.reasons()));
        } catch (Exception e) {
            log.error("本轮风控扫描失败，已跳过，等待下一轮", e);
        }
    }
}
