package com.carl.ai.transfer.domain.model;

import jakarta.persistence.*;

/** 调拨单子表实体（复刻 5-15）。 */
@Entity
@Table(name = "bb_transfer_order_item")
public class BbTransferOrderItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long orderId;
    private String sku;
    private Integer qty;

    public Long getId() { return id; }
    public void setId(Long v) { this.id = v; }
    public Long getOrderId() { return orderId; }
    public void setOrderId(Long v) { this.orderId = v; }
    public String getSku() { return sku; }
    public void setSku(String v) { this.sku = v; }
    public Integer getQty() { return qty; }
    public void setQty(Integer v) { this.qty = v; }
}
