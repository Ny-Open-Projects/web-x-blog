package com.riskbot;

import com.riskbot.provider.MockQuoteProvider;
import com.riskbot.provider.QuoteProvider;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * default(离线) profile 启动装配测试：上下文必须能拉起，QuoteProvider 唯一且为 mock 源。
 * 任何 bean 歧义 / 配置缺失都会在上下文启动时暴露。
 */
@SpringBootTest(properties = {
        // 关掉周期扫描：测试只验装配，不跑定时任务
        "risk.scan.enabled=false"
})
class RiskBotApplicationTest {

    @Autowired
    private QuoteProvider quoteProvider;

    @Test
    @DisplayName("default(离线) 下上下文可装配，QuoteProvider 唯一且为 mock 源")
    void defaultContextLoads() {
        assertNotNull(quoteProvider);
        assertInstanceOf(MockQuoteProvider.class, quoteProvider);
    }
}
