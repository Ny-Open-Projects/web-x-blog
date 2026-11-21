# 画面线理解：07-过滤器简介

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\07-过滤器简介_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:55, 01:38, 02:09, 03:15, 03:53, 04:10, 04:40, 04:50, 05:13, 06:16, 06:43, 07:47, 08:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:24:26

1) 这一组画面整体在讲什么（一句话）：
讲解 Spring Cloud Gateway 中的过滤器（Filter）机制，包括内置过滤器工厂、配置方式、执行生命周期及如何添加或去除请求头和路径前缀。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档中“2.7. 过滤器”章节的“2.7.1. 简介”，列出 Gateway 自带的过滤器名称及说明，如 AddRequestHeader、AddRequestParameters、AddResponseHeader、StripPrefix 等。
画面 2: 展示 IDE 中 Spring Cloud Gateway 的过滤器工厂类结构，列出如 AbstractGatewayFilterFactory、SecureHeadersGatewayFilterFactory、StripPrefixGatewayFilterFactory 等。
画面 3: 展示 Spring Cloud Gateway 官方文档“5.1 AddRequestHeader GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加请求头。
画面 4: 展示 Spring Cloud Gateway 官方文档“5.2 AddRequestParameter GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加请求参数。
画面 5: 展示 IDE 中 heima-gateway 项目的 application.yml 文件，配置了路由规则，其中 filters 部分包含 StripPrefix 和 AddResponseHeader 过滤器。
画面 6: 展示 Spring Cloud Gateway 官方文档“5.3 AddResponseHeader GatewayFilter Factory”部分，展示如何在 application.yml 中配置添加响应头。
画面 7: 展示浏览器开发者工具 Network 面板，请求 http://127.0.0.1:10010/api/user/8，响应头中包含 X-Response-Header: Bar。
画面 8: 展示 IDE 中 heima-gateway 项目的 application.yml 文件，配置了默认过滤器 default-filters，包含 AddResponseHeader 和 StripPrefix。
画面 9: 展示浏览器开发者工具 Network 面板，请求 http://127.0.0.1:10010/api/user/8，响应头中包含 X-Response-Header: Bar。
画面 10: 展示课程文档中“配置全局默认过滤器”部分，展示 application.yml 中的配置，包括 server、spring.application.name、gateway.default-filters 等。
画面 11: 展示课程文档中“2.7.2. 执行生命周期”部分，展示一个流程图，请求从上方进入，经过多个过滤器，最后到达微服务。
画面 12: 展示课程文档中“2.7.2. 执行生命周期”部分的流程图，图中显示请求和响应分别经过多个过滤器，然后流向微服务。
画面 13: 展示课程文档“7. 过滤器简介”和“8. 自定义局部过滤器”章节标题，说明过滤器的用法和类型（局部、全局）。
画面 14: 展示课程文档“7. 过滤器简介”和“8. 自定义局部过滤器”章节标题，与画面 13 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_header_route
          uri: http://example.org
          filters:
            - AddRequestHeader=X-Request-Foo, Bar
```

画面 4:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_parameter_route
          uri: http://example.org
          filters:
            - AddRequestParameter=foo, bar
```

画面 5:
```yaml
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        - id: user-service-route
          uri: http://127.0.0.1:8091
          predicates:
            - Path=/api/user/**
          filters:
            - StripPrefix=1
            - AddResponseHeader=X-Response-Zoo, Bar
      default-filters:
        - AddResponseHeader=X-Response-Zoo, Bar
        - StripPrefix=1
    eureka:
      client:
        service-url:
          defaultZone: http://127.0.0.1:10086/eureka
        prefer-ip-address: true
```

画面 6:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: add_request_header_route
          uri: http://example.org
          filters:
            - AddResponseHeader=X-Response-Foo, Bar
```

画面 8:
```yaml
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      default-filters:
        - AddResponseHeader=X-Response-Zoo, Bar
        - StripPrefix=1
    eureka:
      client:
        service-url:
          defaultZone: http://127.0.0.1:10086/eureka
        prefer-ip-address: true
```

画面 10:
```yaml
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      default-filters:
        - AddResponseHeader=X-Response-Default-MyName, itcast
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11: 标题为“2.7.2. 执行生命周期”，下方流程图显示“请求”从上方进入，经过“过滤器”、“过滤器”、“过滤器...”，最后指向“微服务”，响应从“微服务”返回，经过“过滤器”、“过滤器”、“过滤器...”，最后返回“请求”。
画面 12: 标题为“2.7.2. 执行生命周期”，下方流程图显示“请求”从上方进入，经过“过滤器”、“过滤器”、“过滤器...”，最后指向“微服务”，响应从“微服务”返回，经过“过滤器”、“过滤器”、“过滤器...”，最后返回“请求”。
画面 13: 标题为“7. 过滤器简介”和“8. 自定义局部过滤器”，其中“7. 过滤器简介”下有“目标”、“分析”、“小结”等子标题，“8. 自定义局部过滤器”下有“目标”、“分析”、“小结”等子标题。
画面 14: 标题为“7. 过滤器简介”和“8. 自定义局部过滤器”，与画面 13 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已满足）
