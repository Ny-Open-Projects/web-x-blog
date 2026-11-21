package com.riskbot;

import com.riskbot.provider.QuoteProvider;
import com.riskbot.provider.RealQuoteProvider;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * prod profile 启动装配防护测试（P0 回归防线）：
 * MockQuoteProvider 与 RealQuoteProvider 曾同为无 profile 限定的 @Component，
 * prod 下双 bean 触发 NoUniqueBeanDefinitionException 导致应用起不来、
 * docker compose 与 README 的 prod 运行方式全部失效。
 *
 * <p>properties 属性优先级高于 application-prod.yml：prod yml 里
 * api-key 走 ${SPRING_AI_OPENAI_API_KEY} 环境变量占位，此处直接覆写已解析属性，
 * 避免测试环境依赖真实 Key。</p>
 */
@SpringBootTest(properties = {
        "spring.profiles.active=prod",
        "spring.ai.openai.api-key=test-dummy-key",
        "spring.ai.openai.base-url=https://api.openai.com/v1",
        // 关掉周期扫描：测试只验装配，不跑定时任务
        "risk.scan.enabled=false"
})
class RiskBotProdProfileTest {

    @Autowired
    private QuoteProvider quoteProvider;

    @Test
    @DisplayName("prod 下 QuoteProvider 唯一且为真实源（mock 已按 @Profile(\"!prod\") 排除）")
    void quoteProviderIsUniqueAndReal() {
        assertNotNull(quoteProvider);
        assertInstanceOf(RealQuoteProvider.class, quoteProvider,
                "prod 下应注入 RealQuoteProvider；若为 Mock 说明 @Profile(\"!prod\") 回归");
    }
}
