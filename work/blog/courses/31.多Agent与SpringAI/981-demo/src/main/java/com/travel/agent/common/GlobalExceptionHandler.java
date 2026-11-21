package com.travel.agent.common;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * 全局异常处理：统一收敛为结构化错误体，避免把堆栈直接抛给调用方。
 * <ul>
 *   <li>{@link BizException} / {@link IllegalArgumentException} → 400（业务/入参错误）</li>
 *   <li>请求体不可读（如 {"requirement":{"a":1}} 字段类型不匹配）→ 400（Jackson 参数层错误）</li>
 *   <li>其余 {@link Exception} → 500（记录日志，对外只给脱敏文案）</li>
 * </ul>
 */
@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(BizException.class)
    public ResponseEntity<Map<String, Object>> handleBiz(BizException e) {
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", e.getMessage()));
    }

    /**
     * Token 预算耗尽（配额级错误，区别于模型/网络抖动）：明确 400，
     * 并提示调高 {@code app.agent.max-token-budget}，引导运维而非无限重试。
     */
    @ExceptionHandler(TokenBudgetExceededException.class)
    public ResponseEntity<Map<String, Object>> handleTokenBudget(TokenBudgetExceededException e) {
        return ResponseEntity.badRequest().body(errorBody("TOKEN_BUDGET_EXCEEDED", e.getMessage()));
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<Map<String, Object>> handleIllegal(IllegalArgumentException e) {
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", e.getMessage()));
    }

    /**
     * 请求体 JSON 结构不匹配（如 requirement 传成对象/数组）：Jackson 在参数解析阶段抛
     * HttpMessageNotReadableException，不进 Controller 方法体，只能在这里兜成 400。
     */
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, Object>> handleNotReadable(HttpMessageNotReadableException e) {
        log.warn("请求体不是合法 JSON 或字段类型不正确: {}", e.getMessage());
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", "请求体不是合法 JSON 或字段类型不正确"));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, Object>> handleOther(Exception e) {
        log.error("未预期异常", e);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(errorBody("INTERNAL_ERROR", "服务内部错误，请联系管理员"));
    }

    private Map<String, Object> errorBody(String code, String message) {
        Map<String, Object> body = new LinkedHashMap<>();
        body.put("error", code);
        body.put("message", message);
        body.put("timestamp", Instant.now().toString());
        return body;
    }
}
