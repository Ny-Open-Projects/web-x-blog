package com.carl.ai.transfer;

import com.carl.ai.transfer.agent.TransferAgent;
import com.carl.ai.transfer.common.BizException;
import com.carl.ai.transfer.controller.TransferController;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

/**
 * Controller 入参边界测试：空 / 空白 / 超长(>2000) 必须收敛 400，
 * 合法输入 trim 后委托 Agent，幂等键透传。
 */
@ExtendWith(MockitoExtension.class)
class TransferControllerTest {

    @Mock
    private TransferAgent transferAgent;

    private TransferController controller;

    @BeforeEach
    void setUp() {
        controller = new TransferController(transferAgent);
    }

    @Test
    @DisplayName("null body（空 JSON 请求）拒绝")
    void rejectsNullBody() {
        assertThrows(BizException.class, () -> controller.create(null, null));
        verify(transferAgent, never()).createTransferFromText(any(), any());
    }

    @Test
    @DisplayName("空白字符串拒绝")
    void rejectsBlank() {
        assertThrows(BizException.class, () -> controller.create("   ", null));
        verify(transferAgent, never()).createTransferFromText(any(), any());
    }

    @Test
    @DisplayName("超 2000 字符拒绝")
    void rejectsOversized() {
        assertThrows(BizException.class, () -> controller.create("x".repeat(2001), null));
        verify(transferAgent, never()).createTransferFromText(any(), any());
    }

    @Test
    @DisplayName("合法输入 trim 后委托（无幂等键）")
    void delegatesValidInput() {
        when(transferAgent.createTransferFromText("把华北仓货调往华东仓", null))
                .thenReturn("调拨单已创建：orderId=1");

        String body = controller.create("  把华北仓货调往华东仓  ", null).getBody();

        verify(transferAgent, times(1)).createTransferFromText("把华北仓货调往华东仓", null);
        assertEquals("调拨单已创建：orderId=1", body);
    }

    @Test
    @DisplayName("Idempotency-Key 透传给 Agent")
    void idempotencyKeyPassedThrough() {
        when(transferAgent.createTransferFromText(eq("调货"), eq("key-abc")))
                .thenReturn("调拨单已创建：orderId=2");

        String body = controller.create("调货", "key-abc").getBody();

        verify(transferAgent, times(1)).createTransferFromText("调货", "key-abc");
        assertEquals("调拨单已创建：orderId=2", body);
    }
}
