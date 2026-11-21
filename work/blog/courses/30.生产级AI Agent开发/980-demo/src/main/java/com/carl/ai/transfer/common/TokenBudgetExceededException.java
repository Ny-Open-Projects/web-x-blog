package com.carl.ai.transfer.common;

/**
 * Token 预算耗尽异常：区别于「模型抖动」，这是配额级问题，
 * 应直接以 400 明确告知调用方（文案含上限值），而不是静默降级成空 param。
 * 继承 {@link BizException}：经全局异常处理器映射为 HTTP 400。
 */
public class TokenBudgetExceededException extends BizException {

    public TokenBudgetExceededException(String message) {
        super(message);
    }
}
