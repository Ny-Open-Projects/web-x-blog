package com.carl.ai.transfer.agent;

import com.carl.ai.transfer.common.BizException;
import com.carl.ai.transfer.common.RequestIdFactory;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import com.carl.ai.transfer.extract.TransferOrderExtractor;
import com.carl.ai.transfer.service.TransferOrderService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * 工具节点 Agent（复刻课程「工作流/状态机节点」——5-1 全局状态机、CreateInventoryTransferNode）。
 * <p>
 * 把「自然语言 → 抽取 → 入库」封装成一个动作，对应课程的 {@code NodeAction.apply(OverallState)} 节点。
 * 课程里工作流依次执行「大模型生成 → 提取 JSON → 入库」，本工程用 {@link TransferOrderExtractor}
 * 完成前两步、用 {@link TransferOrderService} 完成后一步，串成闭环。
 * <p>
 * 幂等短路（生产加固）：LLM 抽取既花钱又慢，重复提交应在<b>抽取之前</b>就拦掉。
 * 键来源：客户端 {@code Idempotency-Key} 头优先，否则按需求文本哈希派生。
 */
@Component
public class TransferAgent {

    private static final Logger log = LoggerFactory.getLogger(TransferAgent.class);

    private final TransferOrderExtractor extractor;
    private final TransferOrderService orderService;

    public TransferAgent(TransferOrderExtractor extractor, TransferOrderService orderService) {
        this.extractor = extractor;
        this.orderService = orderService;
    }

    /**
     * 节点动作：自然语言 → 抽取 → 入库，返回结果摘要（含主单 ID）。
     *
     * @param requirement    自然语言需求（已 trim）
     * @param idempotencyKey 客户端幂等键，可为 null（null 时按 requirement 派生）
     */
    public String createTransferFromText(String requirement, String idempotencyKey) {
        String requestId = RequestIdFactory.normalizeClientKey(idempotencyKey);
        if (requestId == null) {
            requestId = RequestIdFactory.fromText(requirement);
        }

        // 幂等短路：命中既有单据直接返回，不再调用 LLM（省 token 成本与延迟）
        Long existing = orderService.findIdByRequestId(requestId);
        if (existing != null) {
            log.info("幂等命中：requestId={} -> 既有单据 orderId={}，跳过 LLM 抽取", requestId, existing);
            return "调拨单已存在（幂等命中）：orderId=" + existing;
        }

        TransferOrderParam param = extractor.extract(requirement);
        // extractor 降级路径可能返回 null（如 entity() 绑定失败被熔断兜住），
        // 这里必须兜底：null param 直接 getter 会 NPE 变 500
        if (param == null || param.getSourceWarehouseId() == null) {
            throw new BizException("抽取失败：模型未返回有效调拨单");
        }
        Long orderId = orderService.create(param, requestId);
        return "调拨单已创建：orderId=" + orderId;
    }
}
