package com.carl.ai.transfer.common;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.validation.BindException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;

/**
 * 全局异常处理：统一把异常收敛为结构化错误体，避免把堆栈直接抛给调用方。
 * <ul>
 *   <li>{@link BizException} / {@link IllegalArgumentException} → 400（业务/入参错误）</li>
 *   <li>请求体缺失或不可读、参数校验失败、参数类型不匹配 → 400（Spring MVC 参数层错误）</li>
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

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<Map<String, Object>> handleIllegal(IllegalArgumentException e) {
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", e.getMessage()));
    }

    /**
     * 请求体缺失或反序列化失败（如 POST 空 body 时 Spring MVC 在参数解析阶段抛出，
     * 根本进不到 Controller 方法体，只能在全局异常层兜住并转为 400）。
     */
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, Object>> handleNotReadable(HttpMessageNotReadableException e) {
        log.warn("请求体缺失或不可读: {}", e.getMessage());
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", "请求体缺失或格式错误"));
    }

    @ExceptionHandler(BindException.class)
    public ResponseEntity<Map<String, Object>> handleBind(BindException e) {
        String message = e.getBindingResult().getFieldErrors().isEmpty()
                ? "参数校验失败"
                : e.getBindingResult().getFieldErrors().get(0).getDefaultMessage();
        return ResponseEntity.badRequest().body(errorBody("BAD_REQUEST", message));
    }

    @ExceptionHandler(MissingServletRequestParameterException.class)
    public ResponseEntity<Map<String, Object>> handleMissingParam(MissingServletRequestParameterException e) {
        return ResponseEntity.badRequest()
                .body(errorBody("BAD_REQUEST", "缺少必需参数: " + e.getParameterName()));
    }

    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ResponseEntity<Map<String, Object>> handleTypeMismatch(MethodArgumentTypeMismatchException e) {
        return ResponseEntity.badRequest()
                .body(errorBody("BAD_REQUEST", "参数类型不匹配: " + e.getName()));
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
