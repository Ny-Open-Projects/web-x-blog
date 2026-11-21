package com.carl.ai.transfer;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;

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
 *   <li>/actuator/metrics 匿名 401、带 Basic Auth 200：指标端点不裸奔；</li>
 *   <li>业务 API（POST /api/transfer/create）匿名 200：加安全不影响业务开箱即用。</li>
 * </ol>
 * 凭证取 SecurityConfig 的默认值（ACTUATOR_USER=admin / ACTUATOR_PASSWORD=transfer-actuator）。
 * default profile 本身离线（OfflineChatModel 返回 canned JSON），无需 API Key。
 * 用 JDK HttpClient 直连真实端口（Boot 4 已移除 TestRestTemplate）。
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
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

    private HttpResponse<String> post(String path, String body) throws Exception {
        HttpRequest request = HttpRequest.newBuilder(URI.create("http://localhost:" + port + path))
                .header("Content-Type", "text/plain;charset=UTF-8")
                .POST(HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8))
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
    @DisplayName("metrics 匿名 401、Basic Auth 后 200")
    void metricsRequiresAuth() throws Exception {
        assertEquals(401, get("/actuator/metrics", null).statusCode());

        HttpResponse<String> authed = get("/actuator/metrics", basicOf("admin", "transfer-actuator"));
        assertEquals(200, authed.statusCode());
        assertNotNull(authed.body());
    }

    @Test
    @DisplayName("业务 API 匿名可达（安全管控不误伤业务）")
    void businessApiStaysPublic() throws Exception {
        HttpResponse<String> response = post("/api/transfer/create", "把华北仓货调往华东仓");
        assertEquals(200, response.statusCode());
    }
}
