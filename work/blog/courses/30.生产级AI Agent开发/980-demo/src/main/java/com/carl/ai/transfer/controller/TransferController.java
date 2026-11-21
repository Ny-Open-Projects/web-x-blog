package com.carl.ai.transfer.controller;

import com.carl.ai.transfer.agent.TransferAgent;
import com.carl.ai.transfer.common.BizException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * REST 入口（复刻课程「入库接口的业务逻辑实现」5-14）。
 * 提供「自然语言 → 调拨单入库」与列表查询，供前端/工作流调用。
 */
@RestController
@RequestMapping("/api/transfer")
public class TransferController {

    /** 自然语言需求长度上限：与错误文案共用，改一处即可。 */
    private static final int MAX_REQUIREMENT_LENGTH = 2000;

    /** 幂等键头：客户端重试 / 工作流重投时带同一值，服务端保证只落一单。 */
    public static final String IDEMPOTENCY_KEY_HEADER = "Idempotency-Key";

    private final TransferAgent transferAgent;

    public TransferController(TransferAgent transferAgent) {
        this.transferAgent = transferAgent;
    }

    /**
     * 根据自然语言创建调拨单。
     * 入参做轻量校验（非空 + 长度上限），非法请求直接 400，避免超大 body / 空串滥用。
     * required=false：空 body 在参数解析阶段会抛 HttpMessageNotReadableException，
     * 放行后由下方校验统一收敛为 400，错误响应格式与超长 body 保持一致。
     * Idempotency-Key 可选：不传则按需求文本派生（同一句需求重复提交同样去重）。
     */
    @PostMapping("/create")
    public ResponseEntity<String> create(@RequestBody(required = false) String requirement,
                                         @RequestHeader(value = IDEMPOTENCY_KEY_HEADER, required = false)
                                         String idempotencyKey) {
        if (requirement == null || requirement.isBlank() || requirement.length() > MAX_REQUIREMENT_LENGTH) {
            throw new BizException("requirement 不能为空且长度不超过 " + MAX_REQUIREMENT_LENGTH);
        }
        return ResponseEntity.ok(transferAgent.createTransferFromText(requirement.trim(), idempotencyKey));
    }

    @GetMapping("/health-demo")
    public String ping() {
        return "transfer-demo ok";
    }
}
