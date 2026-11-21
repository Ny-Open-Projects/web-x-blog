package com.carl.ai.transfer.domain.model;

import jakarta.persistence.*;
import java.time.LocalDate;

/**
 * 调拨单主表实体（复刻 5-15 / 5-16 的 {@code BbTransferOrder}）。
 * 课程用 MyBatis Plus 生成，demo 用 JPA 实体 + H2，字段与转换规则一致。
 * 注意：model 层日期是 {@code LocalDate}，与 param 的 String 由 MapStruct 转换。
 */
@Entity
@Table(name = "bb_transfer_order")
public class BbTransferOrder {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Integer sourceWarehouseId;
    private Integer targetWarehouseId;
    private Integer status;
    private Integer transferType;
    private LocalDate transferDate;
    private String comment;
    private String createdBy;
    /**
     * 幂等键：同一 requestId 全局只允许落一单。
     * unique=true 在 create-drop 模式自动生效；prod（ddl-auto=update）不会给已有表补约束，
     * 由 IdempotencyIndexInitializer 启动时 best-effort 补齐。
     */
    @Column(name = "request_id", length = 64, unique = true)
    private String requestId;

    public Long getId() { return id; }
    public void setId(Long v) { this.id = v; }
    public Integer getSourceWarehouseId() { return sourceWarehouseId; }
    public void setSourceWarehouseId(Integer v) { this.sourceWarehouseId = v; }
    public Integer getTargetWarehouseId() { return targetWarehouseId; }
    public void setTargetWarehouseId(Integer v) { this.targetWarehouseId = v; }
    public Integer getStatus() { return status; }
    public void setStatus(Integer v) { this.status = v; }
    public Integer getTransferType() { return transferType; }
    public void setTransferType(Integer v) { this.transferType = v; }
    public LocalDate getTransferDate() { return transferDate; }
    public void setTransferDate(LocalDate v) { this.transferDate = v; }
    public String getComment() { return comment; }
    public void setComment(String v) { this.comment = v; }
    public String getCreatedBy() { return createdBy; }
    public void setCreatedBy(String v) { this.createdBy = v; }
    public String getRequestId() { return requestId; }
    public void setRequestId(String v) { this.requestId = v; }
}
