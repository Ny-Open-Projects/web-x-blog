package com.carl.ai.transfer;

import com.carl.ai.transfer.common.LlmTokenBudget;
import com.carl.ai.transfer.common.TokenBudgetExceededException;
import com.carl.ai.transfer.config.OfflineChatModel;
import com.carl.ai.transfer.extract.TransferOrderExtractor;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import io.github.resilience4j.retry.Retry;
import org.junit.jupiter.api.Test;
import org.springframework.ai.chat.client.ChatClient;

import static org.junit.jupiter.api.Assertions.*;

/**
 * 抽取层单测（复刻 5-16「LLM 生成 → 提取 JSON」）。
 * 用 OfflineChatModel 返回固定 JSON，验证 {@code responseEntity()} 能把输出绑定成 POJO，
 * 全程离线、不联网、不填 Key。同时验证 Token 预算拦截。
 */
class TransferOrderExtractorTest {

    private TransferOrderExtractor buildExtractor(String json) {
        return new TransferOrderExtractor(
                ChatClient.builder(new OfflineChatModel(json)),
                Retry.ofDefaults("test"),
                new LlmTokenBudget(200000));
    }

    @Test
    void extractBindsCannedJsonToParam() {
        String json = "{\"sourceWarehouseId\":1,\"targetWarehouseId\":2,\"status\":0,"
                + "\"transferType\":1,\"transferDate\":\"2026-10-20\","
                + "\"comment\":\"demo\",\"createdBy\":\"agent\","
                + "\"items\":[{\"sku\":\"SKU-A\",\"qty\":10}]}";
        TransferOrderExtractor extractor = buildExtractor(json);

        TransferOrderParam param = extractor.extract("把华北仓 10 件 SKU-A 调往华东仓");

        assertNotNull(param);
        assertEquals(1, param.getSourceWarehouseId());
        assertEquals(2, param.getTargetWarehouseId());
        assertEquals("2026-10-20", param.getTransferDate());
        assertNotNull(param.getItems());
        assertEquals(1, param.getItems().size());
        assertEquals("SKU-A", param.getItems().get(0).getSku());
    }

    @Test
    void extractRejectsWhenBudgetExhausted() {
        // 预算设为 0：checkBudget 立即抛 TokenBudgetExceededException（BizException → 400）
        TransferOrderExtractor extractor = new TransferOrderExtractor(
                ChatClient.builder(new OfflineChatModel("{\"items\":[]}")),
                Retry.ofDefaults("test"),
                new LlmTokenBudget(0));
        assertThrows(TokenBudgetExceededException.class,
                () -> extractor.extract("任意需求"));
    }
}
