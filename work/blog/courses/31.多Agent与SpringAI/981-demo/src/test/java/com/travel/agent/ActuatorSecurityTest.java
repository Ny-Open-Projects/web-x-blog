package com.travel.agent;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.test.context.ActiveProfiles;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

/**
 * 端点暴露管控回归（P0 安全防线）：
 * <ol>
 *   <li>/actuator/health 匿名 200：探针与负载均衡健康检查必须可达；</li>
 *   <li>/actuator/metrics 匿名 401、带 Basic Auth 200：观测端点不裸奔（与 /actuator/prometheus
 *       同走 SecurityFilterChain 的 {@code /actuator/**} 规则，一条防线全覆盖）；</li>
 *   <li>业务 API（POST /api/travel/plan）匿名 200：多 Agent 联调与课程演示保持开箱即用。</li>
 * </ol>
 * 凭证取 SecurityConfig 的默认值（ACTUATOR_USER=admin / ACTUATOR_PASSWORD=travel-actuator）。
 * test-offline profile 离线跑通主管→成员全链路，无需 API Key。
 *
 * <p>注：Boot 3.5 的 spring-boot-test-autoconfigure 默认给测试上下文设
 * {@code management.defaults.metrics.export.enabled=false}（DisableObservabilityContextCustomizer，
 * 且优先级高于 @SpringBootTest(properties)），因此测试上下文里 prometheus 端点不注册，
 * 这里改断言语义等价的 /actuator/metrics。真实应用的 prometheus 管控（匿名 401 / 带凭证 200）
 * 已由冒烟实测验证。</p>
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test-offline")
class ActuatorSecurityTest {

    private final HttpClient client = HttpClient.newHttpClient();

    @LocalServerPort
    private int port;

    private HttpResponse<String> get(String path, String basicToken) throws Exception {
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create("http://localhost:" + port + path)).GET();
        if (basicToken != null) {
            builder.header("Authorization", "Basic " + basicToken);
        }
        return client.send(builder.build(), HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
    }

    private HttpResponse<String> post(String path, String json) throws Exception {
        HttpRequest request = HttpRequest.newBuilder(URI.create("http://localhost:" + port + path))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(json, StandardCharsets.UTF_8))
                .build();
        return client.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
    }

    private static String basicOf(String user, String pass) {
        return Base64.getEncoder().encodeToString((user + ":" + pass).getBytes(StandardCharsets.UTF_8));
    }

    @Test
    @DisplayName("health 匿名可达")
    void healthIsPublic() throws Exception {
        assertEquals(200, get("/actuator/health", null).statusCode());
    }

    @Test
    @DisplayName("metrics 匿名 401、Basic Auth 后 200（/actuator/** 同一规则覆盖 prometheus）")
    void metricsRequiresAuth() throws Exception {
        assertEquals(401, get("/actuator/metrics", null).statusCode());

        HttpResponse<String> authed = get("/actuator/metrics", basicOf("admin", "travel-actuator"));
        assertEquals(200, authed.statusCode());
        assertNotNull(authed.body());
    }

    @Test
    @DisplayName("业务 API 匿名可达（安全管控不误伤业务）")
    void businessApiStaysPublic() throws Exception {
        HttpResponse<String> response = post("/api/travel/plan", "{\"requirement\":\"杭州三日游，要景点推荐\"}");
        assertEquals(200, response.statusCode());
    }
}
