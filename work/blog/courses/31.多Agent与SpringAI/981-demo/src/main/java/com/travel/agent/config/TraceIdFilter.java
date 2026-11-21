package com.travel.agent.config;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Locale;
import java.util.UUID;
import org.slf4j.MDC;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

/**
 * 请求级链路关联过滤器：为每个进入的 HTTP 请求确定 traceId / spanId 并写入 SLF4J MDC，
 * 使同一次请求的所有日志行都带上同一 traceId，便于跨日志检索与问题定位。
 *
 * <p>分布式场景下，本过滤器实现了 W3C Trace Context 规范的最小可用子集：
 * <ul>
 *   <li><b>入站</b>：解析请求头 {@code traceparent}（格式 {@code 00-{trace-id}-{parent-id}-{flags}}）。
 *       命中且合法时<b>沿用上游 traceId</b>，本服务生成新的 spanId 作为该链路的下一段；不合法或缺失时自建。</li>
 *   <li><b>出站</b>：把本服务当前上下文以 {@code traceparent} 响应头回写，调用方可直接继续向下游传播，
 *       链路不断裂；{@code tracestate} 原样透传。</li>
 *   <li>同时保留既有的 {@code X-Trace-Id} 响应头，并新增 {@code X-Trace-Span-Id}。</li>
 * </ul>
 *
 * <p>说明：本工程（981）运行于 Boot 3.5.7，Micrometer Tracing 自动配置仍可用；但为与 980/982
 * （Boot 4.1.1，已从核心移除 tracing 自动配置）保持完全一致的实现与日志形态，三个工程统一采用本过滤器。
 *
 * <p>本实现不依赖 brave / micrometer-tracing 任何类，纯 JDK 手写解析，
 * 与 {@code brave-propagation-tracecontext} 的 W3C 语义对齐，因此离线构建零新增依赖。</p>
 */
@Component
@Order(Ordered.HIGHEST_PRECEDENCE)
public class TraceIdFilter implements Filter {

    public static final String TRACE_ID = "traceId";
    public static final String SPAN_ID = "spanId";

    /** W3C Trace Context 标准头名。 */
    public static final String TRACEPARENT_HEADER = "traceparent";
    /** W3C Trace Context 标准头名（厂商自定义跟踪状态）。 */
    public static final String TRACESTATE_HEADER = "tracestate";
    /** 本服务 traceId 的响应头名（自研、与上游无关的既有约定）。 */
    public static final String TRACE_ID_RESPONSE_HEADER = "X-Trace-Id";
    /** 本服务 spanId 的响应头名。 */
    public static final String SPAN_ID_RESPONSE_HEADER = "X-Trace-Span-Id";

    /** W3C traceparent 的版本字段，当前固定 00。 */
    private static final String VERSION = "00";
    /** W3C 规范规定的非法（全零）trace-id。 */
    private static final String INVALID_TRACE_ID = "00000000000000000000000000000000";
    /** W3C 规范规定的非法（全零）parent-id。 */
    private static final String INVALID_SPAN_ID = "0000000000000000";
    /** flags 字段：01 = 已采样。 */
    private static final String FLAGS_SAMPLED = "01";

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        String inboundTraceparent = null;
        String inboundTracestate = null;
        String traceId = null;

        if (request instanceof HttpServletRequest http) {
            inboundTraceparent = http.getHeader(TRACEPARENT_HEADER);
            inboundTracestate = http.getHeader(TRACESTATE_HEADER);
            TraceContext context = parseTraceParent(inboundTraceparent);
            if (context != null) {
                traceId = context.traceId();
            }
        }
        if (traceId == null) {
            traceId = newTraceId();
        }
        String spanId = newSpanId();

        MDC.put(TRACE_ID, traceId);
        MDC.put(SPAN_ID, spanId);
        try {
            if (response instanceof HttpServletResponse http) {
                http.setHeader(TRACE_ID_RESPONSE_HEADER, traceId);
                http.setHeader(SPAN_ID_RESPONSE_HEADER, spanId);
                http.setHeader(TRACEPARENT_HEADER, formatTraceParent(traceId, spanId));
                if (inboundTracestate != null && !inboundTracestate.isBlank()) {
                    http.setHeader(TRACESTATE_HEADER, inboundTracestate);
                }
            }
            chain.doFilter(request, response);
        } finally {
            MDC.remove(TRACE_ID);
            MDC.remove(SPAN_ID);
        }
    }

    /** 取当前请求的 traceId（供业务代码出站调用时手动加头），无上下文时返回 {@code null}。 */
    public static String currentTraceId() {
        return MDC.get(TRACE_ID);
    }

    /** 取当前请求的 spanId（供业务代码出站调用时手动加头），无上下文时返回 {@code null}。 */
    public static String currentSpanId() {
        return MDC.get(SPAN_ID);
    }

    /**
     * 生成可直接放入出站请求头的 {@code traceparent}；无上下文时返回 {@code null}。
     * 出站 HTTP 调用（如调用外部行情接口）把它加到请求头即可延续链路。
     */
    public static String currentTraceParent() {
        String traceId = currentTraceId();
        String spanId = currentSpanId();
        if (traceId == null || spanId == null) {
            return null;
        }
        return formatTraceParent(traceId, spanId);
    }

    /**
     * 解析 W3C {@code traceparent} 头。
     *
     * @return 合法时返回上下文；缺失或非法时返回 {@code null}（调用方应自建新链路）
     */
    static TraceContext parseTraceParent(String header) {
        if (header == null || header.isBlank()) {
            return null;
        }
        String[] parts = header.trim().split("-");
        if (parts.length != 4) {
            return null;
        }
        String version = parts[0];
        String traceId = parts[1];
        String parentId = parts[2];
        String flags = parts[3];
        if (version.length() != 2 || !isHex(version) || "ff".equalsIgnoreCase(version)) {
            return null;
        }
        if (traceId.length() != 32 || !isHex(traceId) || INVALID_TRACE_ID.equalsIgnoreCase(traceId)) {
            return null;
        }
        if (parentId.length() != 16 || !isHex(parentId) || INVALID_SPAN_ID.equalsIgnoreCase(parentId)) {
            return null;
        }
        if (flags.length() != 2 || !isHex(flags)) {
            return null;
        }
        return new TraceContext(traceId.toLowerCase(Locale.ROOT), parentId.toLowerCase(Locale.ROOT));
    }

    /** 按 W3C 规范拼装 {@code traceparent}。 */
    static String formatTraceParent(String traceId, String spanId) {
        return VERSION + "-" + traceId + "-" + spanId + "-" + FLAGS_SAMPLED;
    }

    private static boolean isHex(String value) {
        for (int i = 0; i < value.length(); i++) {
            if (Character.digit(value.charAt(i), 16) < 0) {
                return false;
            }
        }
        return true;
    }

    /** W3C trace-id：32 位（16 字节）十六进制。 */
    private static String newTraceId() {
        return UUID.randomUUID().toString().replace("-", "");
    }

    /** W3C parent-id（span-id）：16 位（8 字节）十六进制。 */
    private static String newSpanId() {
        return UUID.randomUUID().toString().replace("-", "").substring(0, 16);
    }

    /** W3C traceparent 解析结果。 */
    record TraceContext(String traceId, String parentId) {
    }
}
