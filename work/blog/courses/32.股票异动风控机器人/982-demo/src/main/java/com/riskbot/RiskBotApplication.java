package com.riskbot;

import com.riskbot.service.RiskEvaluationService;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

/**
 * 受管 Bean 装配：CircuitBreakerRegistry（让风控熔断实例可被观测）、虚拟线程调度器（周期扫描）。
 */
@SpringBootApplication
@EnableScheduling
public class RiskBotApplication {

    public static void main(String[] args) {
        SpringApplication.run(RiskBotApplication.class, args);
    }

    /** 受管熔断注册表：风控评估的 CircuitBreaker 由此创建，便于统一配置与指标导出。 */
    @Bean
    public CircuitBreakerRegistry circuitBreakerRegistry() {
        return CircuitBreakerRegistry.ofDefaults();
    }

    /**
     * 虚拟线程调度器：@Scheduled 的周期扫描运行在虚拟线程上（高并发、轻量），
     * 同时保证 fixedDelay 的"等上一轮跑完"语义不被额外线程池打断。
     *
     * <p>注意：不要手动调用 initialize()——Bean 作为 InitializingBean 会由
     * Spring 生命周期自动初始化，手动再调一次属于重复初始化。</p>
     */
    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(4);
        scheduler.setThreadFactory(Thread.ofVirtual().factory());
        scheduler.setThreadNamePrefix("risk-scan-");
        return scheduler;
    }

    /**
     * 启动自检：打印工程能力边界，证明「感知→决策→执行」闭环已装配。
     * 真实风控逻辑由 RiskScanScheduler 周期触发，外部也可经 REST 主动触发。
     */
    @Bean
    CommandLineRunner banner(RiskEvaluationService svc) {
        return args -> {
            System.out.println("===================================================================");
            System.out.println(" stock-risk-bot (mksz982 配套) 已启动");
            System.out.println(" 行情源: mock(离线) / 真实(配置 risk.quote.api-url)");
            System.out.println(" 规则: 涨跌幅 / 成交量 异动 -> 告警");
            System.out.println(" REST: POST /api/risk/evaluate?symbol=   GET /api/risk/scan");
            System.out.println(" 健康检查: GET /actuator/health");
            System.out.println("===================================================================");
            svc.scanAll().forEach(a -> log.warn("[启动预扫] level={} symbol={} reasons={}",
                    a.level(), a.symbol(), a.reasons()));
        };
    }

    private static final Logger log = LoggerFactory.getLogger(RiskBotApplication.class);
}
