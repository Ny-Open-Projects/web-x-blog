package com.carl.ai.transfer.domain.param;

/** 调拨单子项入参（复刻 5-15）。 */
public class TransferOrderItemParam {

    private String sku;
    private Integer qty;

    public String getSku() { return sku; }
    public void setSku(String v) { this.sku = v; }
    public Integer getQty() { return qty; }
    public void setQty(Integer v) { this.qty = v; }
}
