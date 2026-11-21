package com.carl.ai.transfer.service;

import com.carl.ai.transfer.common.BizException;
import com.carl.ai.transfer.common.RequestIdFactory;
import com.carl.ai.transfer.convert.TransferOrderConvert;
import com.carl.ai.transfer.domain.model.BbTransferOrder;
import com.carl.ai.transfer.domain.model.BbTransferOrderItem;
import com.carl.ai.transfer.domain.param.TransferOrderItemParam;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import com.carl.ai.transfer.repository.BbTransferOrderItemRepository;
import com.carl.ai.transfer.repository.BbTransferOrderRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.support.TransactionTemplate;

import java.time.format.DateTimeParseException;
import java.util.List;

/**
 * 调拨单服务实现（复刻 5-15 / 5-16 的 {@code TransferOrderServiceImpl}）。
 * <p>
 * 流程：MapStruct 把 param 转 model → 存主单（取回自增 ID）→ 子单 set 主单 ID → 批量存。
 * 两表操作，异常整体回滚（{@link Transactional}）。
 * <p>
 * 加固（param 来自 LLM 抽取，不可当可信输入）：入参统一走 {@link #validateParam} fail-fast，
 * 日期格式错误收敛为 400 业务异常，避免脏数据穿透到 JPA 层变成 500。
 * <p>
 * 幂等（生产加固）：同一 requestId 只落一单。三道防线——
 * <ol>
 *   <li>插入前预查：命中直接返回既有单据 ID；</li>
 *   <li>库层唯一索引：并发双写第二方在 flush 时抛 {@link DataIntegrityViolationException}；</li>
 *   <li>唯一索引冲突后用 REQUIRES_NEW 新事务回查既有单（原事务已回滚，同事务内查会
 *       UnexpectedRollbackException，必须换事务）。</li>
 * </ol>
 */
@Service
public class TransferOrderServiceImpl implements TransferOrderService {

    private static final Logger log = LoggerFactory.getLogger(TransferOrderServiceImpl.class);

    /** H2 默认 VARCHAR(255)，超长 comment 直接截断，避免 DataIntegrityViolationException。 */
    private static final int MAX_COMMENT_LENGTH = 255;

    private final BbTransferOrderRepository orderRepository;
    private final BbTransferOrderItemRepository itemRepository;

    /**
     * REQUIRES_NEW 事务模板：用于唯一索引冲突后的「既有单据回查」。
     * 此时原事务已标记 rollback-only，必须挂到新事务上执行，否则查询直接抛
     * UnexpectedRollbackException。
     */
    private final TransactionTemplate requiresNewTemplate;

    public TransferOrderServiceImpl(BbTransferOrderRepository orderRepository,
                                     BbTransferOrderItemRepository itemRepository,
                                     PlatformTransactionManager transactionManager) {
        this.orderRepository = orderRepository;
        this.itemRepository = itemRepository;
        this.requiresNewTemplate = new TransactionTemplate(transactionManager);
        this.requiresNewTemplate.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRES_NEW);
    }

    @Override
    public Long findIdByRequestId(String requestId) {
        if (requestId == null || requestId.isBlank()) {
            return null;
        }
        return orderRepository.findByRequestId(requestId.trim())
                .map(BbTransferOrder::getId)
                .orElse(null);
    }

    @Override
    @Transactional(rollbackFor = Exception.class)
    public Long create(TransferOrderParam param, String requestId) {
        // LLM 抽取结果零校验会直达 JPA：items 缺失 NPE、日期格式错误 500、
        // 超长 comment 触发约束违例——全部在入口拦停，转 400 业务异常
        validateParam(param);

        String rid = resolveRequestId(param, requestId);

        // 防线①：插入前预查。命中即重复提交，返回既有单据，不再写库
        Long existing = findIdByRequestId(rid);
        if (existing != null) {
            log.info("幂等命中：requestId={} 对应既有单据 orderId={}，跳过入库", rid, existing);
            return existing;
        }

        try {
            return insert(param, rid);
        } catch (DataIntegrityViolationException e) {
            // 防线②：并发双写穿透了预查窗口，唯一索引在 flush 时拦住第二方
            log.warn("requestId={} 唯一索引冲突（疑似并发重复提交），回查既有单据", rid);
            Long again = requiresNewTemplate.execute(status ->
                    orderRepository.findByRequestId(rid).map(BbTransferOrder::getId).orElse(null));
            if (again != null) {
                return again;
            }
            throw new BizException("创建失败：幂等键冲突且无法定位既有单据（requestId=" + rid + "）");
        }
    }

    /**
     * 实际写入（与 create 同一事务，私有方法同连接执行）。
     * 主单转换 + 入库（transferDate 为 String，MapStruct 内部 LocalDate.parse 可能抛解析异常），
     * 子单转换 + 回填主单 ID + 批量入库。
     */
    private Long insert(TransferOrderParam param, String requestId) {
        BbTransferOrder order;
        try {
            order = TransferOrderConvert.INSTANCE.paramToModel(param);
        } catch (DateTimeParseException e) {
            throw new BizException("transferDate 格式应为 yyyy-MM-dd，当前值: " + param.getTransferDate());
        }
        order.setRequestId(requestId);
        orderRepository.save(order);
        Long orderId = order.getId();

        List<BbTransferOrderItem> items = TransferOrderConvert.INSTANCE.itemParamsToModel(param.getItems());
        items.forEach(it -> it.setOrderId(orderId));
        itemRepository.saveAll(items);
        return orderId;
    }

    /** 显式幂等键优先；未提供时按 param 内容派生，保证服务单独被调用也有幂等。 */
    private String resolveRequestId(TransferOrderParam param, String requestId) {
        if (requestId != null && !requestId.isBlank()) {
            return requestId.trim();
        }
        List<String[]> pairs = param.getItems() == null ? List.of() : param.getItems().stream()
                .filter(it -> it != null)
                .map(it -> new String[]{it.getSku(), String.valueOf(it.getQty())})
                .toList();
        return RequestIdFactory.fromFields(
                param.getSourceWarehouseId(), param.getTargetWarehouseId(),
                param.getTransferDate(), pairs);
    }

    /**
     * 抽取结果校验：模型漏字段 / 字段非法时抛 BizException（400），
     * 而不是带着 null 进 JPA 层抛 NPE / 约束违例（500）。
     */
    private void validateParam(TransferOrderParam param) {
        if (param.getSourceWarehouseId() == null || param.getTargetWarehouseId() == null) {
            throw new BizException("抽取失败：模型未返回源/目标仓库");
        }
        if (param.getSourceWarehouseId().equals(param.getTargetWarehouseId())) {
            throw new BizException("抽取失败：源仓库与目标仓库不能相同");
        }
        if (param.getItems() == null || param.getItems().isEmpty()) {
            throw new BizException("抽取失败：模型未返回调拨明细");
        }
        for (TransferOrderItemParam item : param.getItems()) {
            if (item == null || item.getSku() == null || item.getSku().isBlank()) {
                throw new BizException("抽取失败：调拨明细存在空 SKU");
            }
            if (item.getQty() == null || item.getQty() <= 0) {
                throw new BizException("抽取失败：SKU " + item.getSku() + " 的数量必须为正整数");
            }
        }
        if (param.getComment() != null && param.getComment().length() > MAX_COMMENT_LENGTH) {
            log.warn("comment 超长({})，截断至 {} 字符", param.getComment().length(), MAX_COMMENT_LENGTH);
            param.setComment(param.getComment().substring(0, MAX_COMMENT_LENGTH));
        }
    }
}
