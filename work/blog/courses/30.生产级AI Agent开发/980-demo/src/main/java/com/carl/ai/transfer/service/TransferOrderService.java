package com.carl.ai.transfer.service;

import com.carl.ai.transfer.domain.param.TransferOrderParam;

/**
 * 调拨单服务（复刻 5-15 接口定义）。
 * <p>
 * 幂等语义（生产加固）：{@link #create} 带 requestId 参数，
 * 同一 requestId 重复调用返回首次落库的单据 ID，不会重复插入。
 */
public interface TransferOrderService {

    /**
     * 创建调拨单：param → model（MapStruct）→ 入库主单 + 子单，事务回滚。
     *
     * @param param     LLM 抽取出的调拨单（不可信输入，内部 fail-fast 校验）
     * @param requestId 幂等键；null / 空白时按 param 内容派生
     * @return 主单 ID（幂等命中时为既有单据 ID）
     */
    Long create(TransferOrderParam param, String requestId);

    /** 按幂等键查既有单据 ID：不存在返回 null。Agent 层在抽取前调用以短路省成本。 */
    Long findIdByRequestId(String requestId);
}
