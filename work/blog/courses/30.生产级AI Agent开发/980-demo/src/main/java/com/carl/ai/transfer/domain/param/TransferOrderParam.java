package com.carl.ai.transfer.domain.param;

import java.util.List;

/**
 * 大模型抽取出的调拨单入参（复刻 5-15 / 5-16）。
 * <p>
 * 关键坑（见博客 5-16）：调拨日期必须用 {@code String} 接收。
 * 大模型返回的 JSON 里日期是字符串，MapStruct 转 {@code LocalDate} 时会调用
 * {@code LocalDate.parse(String)}——如果 param 也定义成 LocalDate，则 parse 收到的是
 * LocalDate 对象而非字符串，直接抛异常。课程的正确修法：param 用 String 接日期。
 */
public class TransferOrderParam {

    private Integer sourceWarehouseId;
    private Integer targetWarehouseId;
    private Integer status;
    private Integer transferType;
    /** 必须为 String：大模型 JSON 日期串；经 MapStruct 转 LocalDate。 */
    private String transferDate;
    private String comment;
    private String createdBy;
    private List<TransferOrderItemParam> items;

    // getters / setters
    public Integer getSourceWarehouseId() { return sourceWarehouseId; }
    public void setSourceWarehouseId(Integer v) { this.sourceWarehouseId = v; }
    public Integer getTargetWarehouseId() { return targetWarehouseId; }
    public void setTargetWarehouseId(Integer v) { this.targetWarehouseId = v; }
    public Integer getStatus() { return status; }
    public void setStatus(Integer v) { this.status = v; }
    public Integer getTransferType() { return transferType; }
    public void setTransferType(Integer v) { this.transferType = v; }
    public String getTransferDate() { return transferDate; }
    public void setTransferDate(String v) { this.transferDate = v; }
    public String getComment() { return comment; }
    public void setComment(String v) { this.comment = v; }
    public String getCreatedBy() { return createdBy; }
    public void setCreatedBy(String v) { this.createdBy = v; }
    public List<TransferOrderItemParam> getItems() { return items; }
    public void setItems(List<TransferOrderItemParam> v) { this.items = v; }
}
