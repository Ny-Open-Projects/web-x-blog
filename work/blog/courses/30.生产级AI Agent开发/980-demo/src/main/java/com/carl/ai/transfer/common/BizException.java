package com.carl.ai.transfer.common;

/**
 * 业务异常：入参非法、抽取失败等可预期错误，由 {@link GlobalExceptionHandler} 映射为 HTTP 400。
 */
public class BizException extends RuntimeException {

    public BizException(String message) {
        super(message);
    }

    public BizException(String message, Throwable cause) {
        super(message, cause);
    }
}
