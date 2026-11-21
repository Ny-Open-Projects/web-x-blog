package com.carl.ai.transfer.repository;

import com.carl.ai.transfer.domain.model.BbTransferOrder;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

/** 调拨单主表仓储（H2；课程用 MyBatis Plus + MySQL，字段一致）。 */
public interface BbTransferOrderRepository extends JpaRepository<BbTransferOrder, Long> {

    /** 按幂等键查既有单据：命中即重复提交，直接返回既有结果。 */
    Optional<BbTransferOrder> findByRequestId(String requestId);
}
