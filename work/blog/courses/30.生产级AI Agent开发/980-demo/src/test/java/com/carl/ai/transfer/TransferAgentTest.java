package com.carl.ai.transfer;

import com.carl.ai.transfer.agent.TransferAgent;
import com.carl.ai.transfer.common.BizException;
import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import com.carl.ai.transfer.extract.TransferOrderExtractor;
import com.carl.ai.transfer.service.TransferOrderService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * Agent 层降级路径测试：抽取器返回 null（熔断兜住绑定失败）时
 * 必须抛 BizException(400)，而不是 NPE 变 500。
 * 另覆盖幂等短路：命中既有单据时<b>不得</b>再调 LLM。
 */
@ExtendWith(MockitoExtension.class)
class TransferAgentTest {

    @Mock
    private TransferOrderExtractor extractor;

    @Mock
    private TransferOrderService orderService;

    @InjectMocks
    private TransferAgent agent;

    private static TransferOrderParam validParam() {
        TransferOrderParam p = new TransferOrderParam();
        p.setSourceWarehouseId(1);
        p.setTargetWarehouseId(2);
        TransferOrderItemParam item = new TransferOrderItemParam();
        item.setSku("SKU-A");
        item.setQty(10);
        p.setItems(List.of(item));
        return p;
    }

    @Test
    @DisplayName("P1 回归：extractor 返回 null 时抛 BizException 而非 NPE")
    void nullParamFromExtractorIsRejected() {
        // 注意：Mockito 对 Long 返回类型默认给 0L 而非 null，必须显式 stub 为 null，
        // 否则 agent 的「existing != null」短路会被 0L 蒙过（2026-10-23 踩坑）
        when(orderService.findIdByRequestId(any())).thenReturn(null);
        when(extractor.extract(any())).thenReturn(null);

        BizException ex = assertThrows(BizException.class,
                () -> agent.createTransferFromText("把华北仓货调往华东仓", null));
        assertEquals("抽取失败：模型未返回有效调拨单", ex.getMessage());
        verify(orderService, never()).create(any(), any());
    }

    @Test
    @DisplayName("param 缺源仓库 ID 时拒绝入库")
    void missingSourceWarehouseRejected() {
        when(orderService.findIdByRequestId(any())).thenReturn(null);
        TransferOrderParam p = validParam();
        p.setSourceWarehouseId(null);
        when(extractor.extract(any())).thenReturn(p);

        assertThrows(BizException.class, () -> agent.createTransferFromText("随便一句", null));
        verify(orderService, never()).create(any(), any());
    }

    @Test
    @DisplayName("合法 param：委托 service 入库并返回带 orderId 的摘要")
    void happyPathDelegates() {
        when(orderService.findIdByRequestId(any())).thenReturn(null);
        when(extractor.extract(any())).thenReturn(validParam());
        when(orderService.create(any(), any())).thenReturn(99L);

        String result = agent.createTransferFromText("把华北仓 10 件 SKU-A 调往华东仓", null);

        verify(orderService, times(1)).create(any(), any());
        assertEquals("调拨单已创建：orderId=99", result);
    }

    @Test
    @DisplayName("幂等命中：不再调 LLM 抽取，直接返回既有单据")
    void idempotentHitSkipsLlm() {
        when(orderService.findIdByRequestId(any())).thenReturn(88L);

        String result = agent.createTransferFromText("把华北仓 10 件 SKU-A 调往华东仓", "client-key-1");

        verify(extractor, never()).extract(any());
        verify(orderService, never()).create(any(), any());
        assertEquals("调拨单已存在（幂等命中）：orderId=88", result);
    }

    @Test
    @DisplayName("显式 Idempotency-Key 优先于文本派生：按原键预查")
    void explicitKeyTakesPrecedence() {
        when(orderService.findIdByRequestId("client-key-2")).thenReturn(null);
        when(extractor.extract(any())).thenReturn(validParam());
        when(orderService.create(any(), eq("client-key-2"))).thenReturn(7L);

        String result = agent.createTransferFromText("把华北仓 10 件 SKU-A 调往华东仓", " client-key-2 ");

        verify(orderService, times(1)).findIdByRequestId("client-key-2");
        verify(orderService, times(1)).create(any(), eq("client-key-2"));
        assertEquals("调拨单已创建：orderId=7", result);
    }
}
