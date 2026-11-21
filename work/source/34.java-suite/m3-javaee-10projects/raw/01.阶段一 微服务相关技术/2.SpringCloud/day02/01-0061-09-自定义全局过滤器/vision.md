# 画面线理解：09-自定义全局过滤器

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\09-自定义全局过滤器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:49, 02:10, 03:06, 03:22, 04:10, 04:19, 04:43, 05:40, 06:10, 06:27, 06:50, 07:08, 07:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:25:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud Gateway 中自定义一个全局过滤器，用于检查请求中是否携带 token 参数，若无则返回 401 未授权状态码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“9. 自定义全局过滤器”的目标和需求分析，明确要实现的功能。
画面 2: 在 IDEA 中打开 `MyGlobalFilter.java` 文件，准备编写过滤器代码。
画面 3: 为 `MyGlobalFilter` 类选择实现 `GlobalFilter` 和 `Ordered` 接口。
画面 4: 编写 `MyGlobalFilter` 类的 `filter` 方法，打印日志并获取请求参数。
画面 5: 在 `filter` 方法中添加注释，说明后续要检查 token。
画面 6: 在 `filter` 方法中添加代码，获取请求参数中的 token。
画面 7: 在 `filter` 方法中添加代码，如果 token 为空则设置响应状态码为 401。
画面 8: 在 `filter` 方法中添加代码，设置响应状态码为 401 并完成响应。
画面 9: 在浏览器中访问 `http://127.0.0.1:10010/api/user/8`，页面显示 404 错误。
画面 10: 在浏览器中访问 `http://127.0.0.1:10010/api/user/8`，页面显示 404 错误。
画面 11: 使用 Advanced REST Client 发起 GET 请求到 `http://127.0.0.1:10010/api/user/8`，返回状态码 401 Unauthorized。
画面 12: 展示文件资源管理器中 `day02` 目录下的文件结构。
画面 13: 展示课程文档中“9. 自定义全局过滤器”的目标和需求分析，明确要实现的功能。
画面 14: 展示课程文档中“9. 自定义全局过滤器”的实现步骤，包括编写过滤器和测试。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ithema.gateway.filter;
```

画面 3:
```java
public class MyGlobalFilter implements GlobalFilter, Ordered {
```

画面 4:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        exchange.getRequest().getHeaders().forEach((k, v) -> {
            System.out.println(k + " : " + v);
        });
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
```

画面 5:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        exchange.getRequest().getHeaders().forEach((k, v) -> {
            System.out.println(k + " : " + v);
        });
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 6:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 7:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

画面 8:
```java
@Component
public class MyGlobalFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        System.out.println("------------全局过滤器MyGlobalFilter-------------");
        String token = exchange.getRequest().getQueryParams().getFirst("token");
        if (StringUtils.isBlank(token)) {
            //设置响应状态码为401
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() {
        //值越小优先级越高
        return 1;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
