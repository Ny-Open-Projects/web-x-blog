package com.travel.agent.a2a;

/**
 * A2A 协议层错误：远端正常响应但业务上返回了 JSON-RPC error（第三方 A2A 服务常见）。
 * <p>
 * 与「网络抖动 / 超时 / 5xx」不同，这类错误是契约/业务层面的，重试没有意义——
 * {@link A2aHttpAgentTransport} 的重试策略会把它列入 ignoreExceptions，不重发请求。
 */
public class A2aProtocolException extends RuntimeException {

    public A2aProtocolException(String message) {
        super(message);
    }
}
