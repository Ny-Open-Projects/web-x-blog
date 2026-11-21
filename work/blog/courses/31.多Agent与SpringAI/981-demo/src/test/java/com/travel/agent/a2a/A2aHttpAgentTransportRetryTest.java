package com.travel.agent.a2a;

import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.atomic.AtomicInteger;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

/**
 * A2A 通道重试单测：用 JDK 内置 HttpServer 模拟远端，验证
 * ① 瞬时故障（前 N 次 500）重试后恢复；② 协议层错误（JSON-RPC error）不重试。
 */
class A2aHttpAgentTransportRetryTest {

    private HttpServer server;
    private String baseUrl;
    private final AtomicInteger postHits = new AtomicInteger();

    @BeforeEach
    void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/.well-known/agent.json", exchange -> {
            byte[] body = "{\"name\":\"route-agent\",\"description\":\"路线规划\"}"
                    .getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort();
    }

    @AfterEach
    void stopServer() {
        if (server != null) {
            server.stop(0);
        }
    }

    /** 前两次返回 500，第三次返回正常 JSON-RPC 结果：必须重试并拿到正文。 */
    @Test
    void retriesOnTransientFailureThenSucceeds() {
        postHits.set(0);
        server.createContext("/", exchange -> {
            int hit = postHits.incrementAndGet();
            if (hit < 3) {
                exchange.sendResponseHeaders(500, -1);
                exchange.close();
                return;
            }
            byte[] body = ("{\"jsonrpc\":\"2.0\",\"id\":\"1\",\"result\":{\"artifacts\":"
                    + "[{\"parts\":[{\"type\":\"text\",\"text\":\"杭州三日游路线\"}]}]}}")
                    .getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });

        A2aHttpAgentTransport transport = new A2aHttpAgentTransport(baseUrl);
        String result = transport.call("杭州三天路线");

        assertEquals("杭州三日游路线", result);
        assertEquals(3, postHits.get(), "前两次 500 应触发两次重试，第三次才成功");
    }

    /** 始终返回内嵌 JSON-RPC error：属协议层错误，不应重试（只发 1 次请求）。 */
    @Test
    void doesNotRetryOnProtocolError() {
        postHits.set(0);
        server.createContext("/", exchange -> {
            postHits.incrementAndGet();
            byte[] body = ("{\"jsonrpc\":\"2.0\",\"id\":\"1\",\"error\":"
                    + "{\"code\":-32603,\"message\":\"远端业务拒绝\"}}")
                    .getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
            exchange.sendResponseHeaders(200, body.length);
            exchange.getResponseBody().write(body);
            exchange.close();
        });

        A2aHttpAgentTransport transport = new A2aHttpAgentTransport(baseUrl);
        A2aProtocolException ex = assertThrows(A2aProtocolException.class,
                () -> transport.call("任意任务"));
        assertEquals(1, postHits.get(), "协议层错误不应重试");
    }
}
