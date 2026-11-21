package com.travel.agent;

import static org.assertj.core.api.Assertions.assertThat;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.Map;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.web.client.HttpStatusCodeException;

/**
 * 入参校验回归（离线链路，不需要 API Key）：
 * <ol>
 *   <li>POST /api/travel/plan：空 body / 缺 requirement / 空白 / 超长（&gt;2000）统一收敛 400，
 *       入口 {@code @RequestBody(required = false)} 让 null 进方法体，由方法内校验抛 BizException；</li>
 *   <li>POST /a2a/{agent}：空 body 走 JSON-RPC error 结构（500 + error 节点），未知 agent 返回 404。</li>
 * </ol>
 * 这些行为此前由手工回归验证，此处固化为自动化用例，防止后续改动回退。
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test-offline")
class TravelControllerValidationTest {

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @LocalServerPort
    private int port;

    private final TestRestTemplate rest = new TestRestTemplate();

    /** status + body 小载体：出错状态码时 TestRestTemplate 可能直接返回也可能抛异常，两条路径都解析。 */
    private record Reply(int status, Map<String, Object> body) {}

    @Test
    void plan_rejectsEmptyBody() {
        Reply reply = post("/api/travel/plan", "");
        assertThat(reply.status()).isEqualTo(400);
        assertThat(reply.body()).containsKey("error");
    }

    @Test
    void plan_rejectsMissingRequirement() {
        Reply reply = post("/api/travel/plan", "{}");
        assertThat(reply.status()).isEqualTo(400);
        assertThat(reply.body().get("message").toString()).contains("requirement");
    }

    @Test
    void plan_rejectsBlankRequirement() {
        Reply reply = post("/api/travel/plan", "{\"requirement\":\"   \"}");
        assertThat(reply.status()).isEqualTo(400);
    }

    @Test
    void plan_rejectsOversizedRequirement() {
        String payload = "{\"requirement\":\"" + "x".repeat(2001) + "\"}";
        Reply reply = post("/api/travel/plan", payload);
        assertThat(reply.status()).isEqualTo(400);
    }

    @Test
    void a2a_rejectsEmptyBodyWithJsonRpcError() {
        Reply reply = post("/a2a/RouteMakingAgent", "");
        assertThat(reply.status()).isEqualTo(500);
        assertThat(reply.body()).containsKey("error");
    }

    @Test
    void a2a_unknownAgentReturns404() {
        Reply reply = post("/a2a/NoSuchAgent",
                "{\"jsonrpc\":\"2.0\",\"id\":\"1\",\"method\":\"message/send\"}");
        assertThat(reply.status()).isEqualTo(404);
    }

    private Reply post(String path, String json) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<String> request = new HttpEntity<>(json, headers);
        try {
            ResponseEntity<String> response = rest.exchange(
                    "http://localhost:" + port + path, HttpMethod.POST, request, String.class);
            return new Reply(response.getStatusCode().value(), parse(response.getBody()));
        } catch (HttpStatusCodeException e) {
            return new Reply(e.getStatusCode().value(), parse(e.getResponseBodyAsString()));
        }
    }

    private Map<String, Object> parse(String json) {
        if (json == null || json.isBlank()) {
            return Map.of();
        }
        try {
            return MAPPER.readValue(json, new TypeReference<Map<String, Object>>() {});
        } catch (Exception e) {
            throw new IllegalStateException("响应体不是合法 JSON: " + json, e);
        }
    }
}
