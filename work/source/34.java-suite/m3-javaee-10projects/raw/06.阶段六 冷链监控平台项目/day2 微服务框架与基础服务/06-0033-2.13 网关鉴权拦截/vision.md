# 画面线理解：2.13 网关鉴权拦截

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.13 网关鉴权拦截_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 02:24, 02:46, 03:29, 04:22, 05:14, 06:17, 07:08, 07:37, 08:03, 08:36, 09:29, 09:45, 11:05, 11:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:58:59

1) 这一组画面整体在讲如何在 Spring Cloud Gateway 中实现一个全局过滤器（TokenFilter），用于拦截并验证用户登录请求。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程目录结构，当前位于“6.2 常用API网关”章节，右侧是API网关技术选型图，包含 Nginx、Zuul/Zuul2、Spring Cloud Gateway 和 Kong。
画面2: 展示项目结构，选中了 GatewayApplication.java，这是网关服务的主类。
画面3: 在项目中右键点击，准备新建一个类文件。
画面4: 新建并选中 TokenFilter.java 文件，准备编写过滤器代码。
画面5: 在 TokenFilter.java 中编写实现 GlobalFilter 和 Ordered 接口的类骨架。
画面6: 在 TokenFilter.java 中编写 filter 方法，准备处理请求。
画面7: 在 TokenFilter.java 中编写获取请求路径和 token 的逻辑。
画面8: 在 TokenFilter.java 中使用 exchange.getRequest().getHeaders() 获取请求头。
画面9: 在 TokenFilter.java 中使用 exchange.getRequest().getHeaders().getFirst("token") 获取 token。
画面10: 在 TokenFilter.java 中编写 GatewayConfig 类的骨架。
画面11: 在 TokenFilter.java 中编写判断路径和 token 的逻辑，并设置响应状态码。
画面12: 在 TokenFilter.java 中编写设置响应状态码和返回链的逻辑。
画面13: 在终端中启动网关服务，同时显示 Postman 和 Typora 等工具窗口。
画面14: 在 TokenFilter.java 中编写完整的过滤器逻辑，包括获取 token、判断路径、设置响应状态码和返回链。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.ithema.cold_gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }
}
```

画面4:
```java
package com.ithema.cold_gateway.common;

import org.springframework.cloud.gateway.filter.GlobalFilter;

public class TokenFilter implements GlobalFilter {
}
```

画面5:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面6:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面7:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        if (!exchange.getRequest().getURI().getPath().equals("/tools/user/login")) {
            String token = exchange.getRequest().getHeaders().getFirst("token");
            if (token == null || token.isEmpty()) {
                System.out.println("token为空");
                exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
                return exchange.getResponse().setComplete();
            }
        }
        return null;
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

画面11:
```java
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.server.ServerHttpRequest;
import org.springframework.http.server.ServerHttpResponse;
import reactor.core.publisher.Mono;

public class TokenFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        if (!exchange.getRequest().getURI().getPath().equals("/tools/user/login")) {
            String token = exchange.getRequest().getHeaders().getFirst("token");
            if (token == null || token.isEmpty()) {
                System.out.println("token为空");
                exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
                return exchange.getResponse().setComplete();
            }
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: PPT标题为“6.2 常用API网关”，架构图中“API网关”指向“Nginx”、“Zuul/Zuul2”、“Spring Cloud Gateway”和“Kong”。

5) 不要评价画面美观，不要输出与课程无关的内容。
