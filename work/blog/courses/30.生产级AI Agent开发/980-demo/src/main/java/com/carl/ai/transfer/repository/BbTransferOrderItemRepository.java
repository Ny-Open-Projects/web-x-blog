package com.carl.ai.transfer.repository;

import com.carl.ai.transfer.domain.model.BbTransferOrderItem;
import org.springframework.data.jpa.repository.JpaRepository;

/** 调拨单子表仓储（H2）。 */
public interface BbTransferOrderItemRepository extends JpaRepository<BbTransferOrderItem, Long> {
}
