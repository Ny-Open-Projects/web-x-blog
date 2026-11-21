package com.carl.ai.transfer;

import com.carl.ai.transfer.common.BizException;
import com.carl.ai.transfer.domain.model.BbTransferOrder;
import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import com.carl.ai.transfer.repository.BbTransferOrderItemRepository;
import com.carl.ai.transfer.repository.BbTransferOrderRepository;
import com.carl.ai.transfer.service.TransferOrderServiceImpl;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentCaptor;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.transaction.PlatformTransactionManager;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

/**
 * service 层校验测试：LLM 抽取结果不可信，各类脏数据必须在入口收敛为
 * BizException(400)，绝不允许穿透到 JPA 变 NPE / 500。
 * 幂等命中 / 唯一索引兜底的集成场景见 TransferIdempotencyIntegrationTest（真库）。
 */
@ExtendWith(MockitoExtension.class)
class TransferOrderServiceImplTest {

    @Mock
    private BbTransferOrderRepository orderRepository;

    @Mock
    private BbTransferOrderItemRepository itemRepository;

    @Mock
    private PlatformTransactionManager transactionManager;

    @InjectMocks
    private TransferOrderServiceImpl service;

    private static TransferOrderParam validParam() {
        TransferOrderParam p = new TransferOrderParam();
        p.setSourceWarehouseId(1);
        p.setTargetWarehouseId(2);
        p.setTransferDate("2026-10-20");
        TransferOrderItemParam item = new TransferOrderItemParam();
        item.setSku("SKU-A");
        item.setQty(10);
        p.setItems(List.of(item));
        return p;
    }

    @Test
    @DisplayName("合法 param：主单存 1 次、子单批量存 1 次，返回主单 ID")
    void validParamPersistsBothTables() {
        // JPA save 回填 id 由 mock 模拟：返回传入对象并置 id
        when(orderRepository.save(any())).thenAnswer(inv -> {
            BbTransferOrder o = inv.getArgument(0);
            o.setId(99L);
            return o;
        });

        Long id = service.create(validParam(), "rid-001");

        assertEquals(99L, id);
        verify(orderRepository, times(1)).save(any());
        verify(itemRepository, times(1)).saveAll(any());
    }

    @Test
    @DisplayName("P0 回归：items 为 null 时必须抛 BizException，而不是 NPE")
    void nullItemsRejected() {
        TransferOrderParam p = validParam();
        p.setItems(null);

        BizException ex = assertThrows(BizException.class, () -> service.create(p, "rid"));
        assertEquals("抽取失败：模型未返回调拨明细", ex.getMessage());
        verify(orderRepository, never()).save(any());
    }

    @Test
    @DisplayName("items 为空列表同样拒绝")
    void emptyItemsRejected() {
        TransferOrderParam p = validParam();
        p.setItems(List.of());

        assertThrows(BizException.class, () -> service.create(p, "rid"));
        verify(orderRepository, never()).save(any());
    }

    @Test
    @DisplayName("源仓 = 目标仓拒绝")
    void sameWarehouseRejected() {
        TransferOrderParam p = validParam();
        p.setTargetWarehouseId(1);

        assertThrows(BizException.class, () -> service.create(p, "rid"));
    }

    @Test
    @DisplayName("qty <= 0 或 null 拒绝")
    void invalidQtyRejected() {
        TransferOrderParam p = validParam();
        p.getItems().get(0).setQty(0);
        assertThrows(BizException.class, () -> service.create(p, "rid"));

        p.getItems().get(0).setQty(null);
        assertThrows(BizException.class, () -> service.create(p, "rid"));

        p.getItems().get(0).setQty(-5);
        assertThrows(BizException.class, () -> service.create(p, "rid"));
    }

    @Test
    @DisplayName("空 SKU 拒绝")
    void blankSkuRejected() {
        TransferOrderParam p = validParam();
        p.getItems().get(0).setSku("  ");
        assertThrows(BizException.class, () -> service.create(p, "rid"));
    }

    @Test
    @DisplayName("日期格式非法收敛为 BizException(400)，不裸抛 DateTimeParseException")
    void badDateRejectedAsBiz() {
        TransferOrderParam p = validParam();
        p.setTransferDate("2026/10/20");

        BizException ex = assertThrows(BizException.class, () -> service.create(p, "rid"));
        assertEquals("transferDate 格式应为 yyyy-MM-dd，当前值: 2026/10/20", ex.getMessage());
        verify(orderRepository, never()).save(any());
    }

    @Test
    @DisplayName("超长 comment 截断到 255 后正常入库")
    void longCommentTruncated() {
        TransferOrderParam p = validParam();
        p.setComment("x".repeat(300));
        when(orderRepository.save(any())).thenAnswer(inv -> inv.getArgument(0));

        assertDoesNotThrow(() -> service.create(p, "rid"));
        assertEquals(255, p.getComment().length());
    }

    @Test
    @DisplayName("幂等预查命中：直接返回既有单据 ID，不写库")
    void existingRequestIdShortCircuits() {
        BbTransferOrder existing = new BbTransferOrder();
        existing.setId(77L);
        when(orderRepository.findByRequestId("rid-hit")).thenReturn(Optional.of(existing));

        Long id = service.create(validParam(), "rid-hit");

        assertEquals(77L, id);
        verify(orderRepository, never()).save(any());
        verify(itemRepository, never()).saveAll(any());
    }

    @Test
    @DisplayName("未传 requestId 时按 param 内容派生键，且内容一致派生一致")
    void derivedRequestIdIsStable() {
        when(orderRepository.save(any())).thenAnswer(inv -> {
            BbTransferOrder o = inv.getArgument(0);
            o.setId(5L);
            return o;
        });

        Long first = service.create(validParam(), null);
        Long second = service.create(validParam(), "  ");

        assertEquals(5L, first);
        assertEquals(5L, second);
        // 两次派生的键必须一致，否则幂等失效
        ArgumentCaptor<String> keys = ArgumentCaptor.forClass(String.class);
        verify(orderRepository, times(2)).findByRequestId(keys.capture());
        assertEquals(keys.getAllValues().get(0), keys.getAllValues().get(1));
    }
}
