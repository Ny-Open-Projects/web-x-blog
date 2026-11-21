package com.carl.ai.transfer;

import static org.assertj.core.api.Assertions.assertThat;

import com.carl.ai.transfer.config.TraceIdFilter;
import org.junit.jupiter.api.Test;
import org.slf4j.MDC;
import org.springframework.mock.web.MockHttpServletRequest;
import org.springframework.mock.web.MockHttpServletResponse;

/**
 * TraceIdFilter 的 W3C traceparent 兼容行为测试：
 * 上游链路继承、非法头回退、响应头下发、MDC 清理。
 */
class TraceIdFilterTest {

    private static final String UPSTREAM_TRACE_ID = "4bf92f3577b34da6a3ce929d0e0e4736";
    private static final String UPSTREAM_PARENT_ID = "00f067aa0ba902b7";
    private static final String UPSTREAM_TRACEPARENT =
            "00-" + UPSTREAM_TRACE_ID + "-" + UPSTREAM_PARENT_ID + "-01";

    private final TraceIdFilter filter = new TraceIdFilter();

    @Test
    void noTraceparent_generatesFreshTraceId() throws Exception {
        MockHttpServletRequest request = new MockHttpServletRequest();
        MockHttpServletResponse response = new MockHttpServletResponse();

        filter.doFilter(request, response, (req, res) -> {});

        String traceId = response.getHeader("X-Trace-Id");
        assertThat(traceId).isNotNull().hasSize(32).matches("[0-9a-f]{32}");
        assertThat(traceId).isNotEqualTo(UPSTREAM_TRACE_ID);
    }

    @Test
    void validTraceparent_inheritsUpstreamTraceId() throws Exception {
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.addHeader("traceparent", UPSTREAM_TRACEPARENT);
        MockHttpServletResponse response = new MockHttpServletResponse();

        filter.doFilter(request, response, (req, res) -> {});

        assertThat(response.getHeader("X-Trace-Id")).isEqualTo(UPSTREAM_TRACE_ID);
    }

    @Test
    void responseExposesTraceparentWithOwnSpanId() throws Exception {
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.addHeader("traceparent", UPSTREAM_TRACEPARENT);
        MockHttpServletResponse response = new MockHttpServletResponse();

        filter.doFilter(request, response, (req, res) -> {});

        String traceparent = response.getHeader("traceparent");
        String spanId = response.getHeader("X-Trace-Span-Id");
        assertThat(traceparent).isEqualTo("00-" + UPSTREAM_TRACE_ID + "-" + spanId + "-01");
        assertThat(spanId).isNotNull().hasSize(16).matches("[0-9a-f]{16}");
        // 本服务生成的是新 span，不是上游的 parent-id
        assertThat(spanId).isNotEqualTo(UPSTREAM_PARENT_ID);
    }

    @Test
    void invalidTraceparent_isRejectedAndFallbackToNewTraceId() throws Exception {
        String[] invalidHeaders = {
                "00-00000000000000000000000000000000-" + UPSTREAM_PARENT_ID + "-01",
                "00-" + UPSTREAM_TRACE_ID + "-0000000000000000-01",
                "00-" + UPSTREAM_TRACE_ID + "-" + UPSTREAM_PARENT_ID,
                "not-a-traceparent",
                "00-" + UPSTREAM_TRACE_ID + "-" + UPSTREAM_PARENT_ID + "-01-extra",
        };
        for (String invalid : invalidHeaders) {
            MockHttpServletRequest request = new MockHttpServletRequest();
            request.addHeader("traceparent", invalid);
            MockHttpServletResponse response = new MockHttpServletResponse();

            filter.doFilter(request, response, (req, res) -> {});

            assertThat(response.getHeader("X-Trace-Id"))
                    .as("非法 traceparent 应回退自建: %s", invalid)
                    .isNotNull()
                    .isNotEqualTo(UPSTREAM_TRACE_ID);
        }
    }

    @Test
    void tracestate_isEchoedBack() throws Exception {
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.addHeader("traceparent", UPSTREAM_TRACEPARENT);
        request.addHeader("tracestate", "vendor=abc123");
        MockHttpServletResponse response = new MockHttpServletResponse();

        filter.doFilter(request, response, (req, res) -> {});

        assertThat(response.getHeader("tracestate")).isEqualTo("vendor=abc123");
    }

    @Test
    void mdcIsPopulatedDuringChainAndClearedAfter() throws Exception {
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.addHeader("traceparent", UPSTREAM_TRACEPARENT);
        MockHttpServletResponse response = new MockHttpServletResponse();
        String[] captured = new String[2];

        filter.doFilter(request, response, (req, res) -> {
            captured[0] = MDC.get("traceId");
            captured[1] = MDC.get("spanId");
        });

        assertThat(captured[0]).isEqualTo(UPSTREAM_TRACE_ID);
        assertThat(captured[1]).isNotNull().hasSize(16);
        assertThat(MDC.get("traceId")).isNull();
        assertThat(MDC.get("spanId")).isNull();
    }
}
