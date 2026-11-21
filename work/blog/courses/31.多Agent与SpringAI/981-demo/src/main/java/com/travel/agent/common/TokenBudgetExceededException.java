package com.travel.agent.common;

/**
 * Token 预算耗尽异常：区别于「模型抖动 / 网络抖动」，这是配额级问题，
 * 调用方应给出明确文案（如「今日额度已用完」），而不是无限重试。
 *
 * <p>继承 {@link BizException}：经 {@link com.travel.agent.common.GlobalExceptionHandler}
 * 映射为 HTTP 400。</p>
 */
public class TokenBudgetExceededException extends BizException {

    public TokenBudgetExceededException(String message) {
        super(message);
    }
}
