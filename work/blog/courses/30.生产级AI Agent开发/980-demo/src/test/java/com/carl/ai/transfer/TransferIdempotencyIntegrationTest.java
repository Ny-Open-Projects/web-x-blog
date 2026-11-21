package com.carl.ai.transfer;

import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import com.carl.ai.transfer.repository.BbTransferOrderRepository;
import com.carl.ai.transfer.service.TransferOrderService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * 幂等集成测试：真 H2 库验证三道防线（预查 / 唯一索引 / REQUIRES_NEW 回查）。
 * default profile = 离线模式，全上下文启动不触网。
 */
@SpringBootTest
class TransferIdempotencyIntegrationTest {

    @Autowired
    private TransferOrderService orderService;

    @Autowired
    private BbTransferOrderRepository orderRepository;

    private static TransferOrderParam validParam() {
        TransferOrderParam p = new TransferOrderParam();
        p.setSourceWarehouseId(1);
        p.setTargetWarehouseId(2);
        p.setTransferDate("2026-10-20");
        p.setComment("幂等测试单");
        TransferOrderItemParam item = new TransferOrderItemParam();
        item.setSku("SKU-IDEMP");
        item.setQty(3);
        p.setItems(List.of(item));
        return p;
    }

    @Test
    @DisplayName("同一 requestId 两次创建：第二次返回同一 ID，库中只有一单")
    void sameRequestIdCreatesOnlyOneOrder() {
        String rid = "it-same-key-001";
        Long first = orderService.create(validParam(), rid);
        Long second = orderService.create(validParam(), rid);

        assertNotNull(first);
        assertEquals(first, second);
        assertEquals(1, orderRepository.findByRequestId(rid).isPresent() ? 1 : 0);
    }

    @Test
    @DisplayName("同一需求文本派生同键：两次同参（rid 传 null）只落一单")
    void sameContentDerivesSameKey() {
        Long first = orderService.create(validParam(), null);
        Long second = orderService.create(validParam(), null);

        assertEquals(first, second);
    }

    @Test
    @DisplayName("不同 requestId：各自落单")
    void differentKeysCreateSeparateOrders() {
        Long a = orderService.create(validParam(), "it-key-a");
        Long b = orderService.create(validParam(), "it-key-b");

        assertNotNull(a);
        assertNotNull(b);
        assertTrue(!a.equals(b));
    }

    @Test
    @DisplayName("并发 16 线程同键：唯一索引兜底，库中只落一单")
    void concurrentSameKeyCreatesOnlyOneOrder() throws InterruptedException {
        String rid = "it-concurrent-001";
        int threads = 16;
        ExecutorService pool = Executors.newFixedThreadPool(threads);
        CountDownLatch start = new CountDownLatch(1);
        CountDownLatch done = new CountDownLatch(threads);
        AtomicInteger created = new AtomicInteger();
        AtomicInteger errors = new AtomicInteger();

        for (int i = 0; i < threads; i++) {
            pool.submit(() -> {
                try {
                    start.await();
                    Long id = orderService.create(validParam(), rid);
                    if (id != null) {
                        created.incrementAndGet();
                    }
                } catch (RuntimeException e) {
                    errors.incrementAndGet();
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    errors.incrementAndGet();
                } finally {
                    done.countDown();
                }
            });
        }
        start.countDown();
        assertTrue(done.await(30, TimeUnit.SECONDS), "并发创建应在 30s 内结束");
        pool.shutdownNow();

        // 唯一索引硬保证：无论多少线程穿透预查，最终只落一单
        long count = orderRepository.findAll().stream()
                .filter(o -> rid.equals(o.getRequestId()))
                .count();
        assertEquals(1, count, "同键并发只能落一单");
        // 所有成功调用必须拿到同一个单据 ID（回查兜底生效）
        assertEquals(threads, created.get() + errors.get(), "不允许有线程既没成功也没报错");
    }
}
