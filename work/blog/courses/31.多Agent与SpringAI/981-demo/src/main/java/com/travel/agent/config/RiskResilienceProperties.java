package com.travel.agent.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

import java.time.Duration;

/**
 * 远程成员调用熔断配置（绑定 {@code app.risk.*}，替代原先硬编码在 {@code AgentConfig} 的写死值）。
 * 之前这些配置项声明在 application.yml 里却从不生效，现在由 {@code AgentConfig} 真正读取。
 */
@ConfigurationProperties(prefix = "app.risk")
public class RiskResilienceProperties {

    /** 打开熔断器所需的失败率阈值（%）。 */
    private int failureRateThreshold = 50;

    /** 熔断后等待多久进入半开状态。 */
    private Duration waitDurationInOpenState = Duration.ofSeconds(10);

    /** 滑动窗口大小（统计样本数）。 */
    private int slidingWindowSize = 10;

    /** 触发统计的最小调用次数。 */
    private int minimumNumberOfCalls = 3;

    public int getFailureRateThreshold() {
        return failureRateThreshold;
    }

    public void setFailureRateThreshold(int failureRateThreshold) {
        this.failureRateThreshold = failureRateThreshold;
    }

    public Duration getWaitDurationInOpenState() {
        return waitDurationInOpenState;
    }

    public void setWaitDurationInOpenState(Duration waitDurationInOpenState) {
        this.waitDurationInOpenState = waitDurationInOpenState;
    }

    public int getSlidingWindowSize() {
        return slidingWindowSize;
    }

    public void setSlidingWindowSize(int slidingWindowSize) {
        this.slidingWindowSize = slidingWindowSize;
    }

    public int getMinimumNumberOfCalls() {
        return minimumNumberOfCalls;
    }

    public void setMinimumNumberOfCalls(int minimumNumberOfCalls) {
        this.minimumNumberOfCalls = minimumNumberOfCalls;
    }
}
