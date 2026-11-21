# 画面线理解：2.12 配置网关路由规则

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.12 配置网关路由规则_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:40, 00:45, 01:07, 01:24, 03:24, 03:49, 03:52, 04:03, 04:34, 04:39, 05:10, 05:31, 05:38, 05:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:58:24

1) 这一组画面整体在讲如何配置和测试一个基于 Spring Cloud Gateway 的 API 网关服务，使其能通过 Eureka 发现服务并转发请求。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IntelliJ IDEA 中，编辑 application.yml 文件，配置 Spring Cloud Gateway 的基础属性，如 cloud、spring、server 等。
画面 2: 继续编辑 application.yml，配置 server 的 context-path 为 /cold。
画面 3: 编辑 application.yml，配置 gateway 的 discovery.locator.enabled 为 true。
画面 4: 编辑 application.yml，配置 gateway 的 routes 路由规则，id 为 cold-user-router，uri 为 lb://cold-user，predicates 为 Path=/cold/user/**。
画面 5: 在 Postman 中创建一个 GET 请求，准备测试网关。
画面 6: 在 IDEA 中，application.yml 文件中 routes 路由规则已配置完成。
画面 7: IDEA 控制台显示 GatewayApplication 启动日志，包括 Eureka 发现客户端初始化和端口更新。
画面 8: 浏览器访问 Eureka 服务注册中心页面，显示 COLD-GATEWAY 和 COLD-USER 服务已注册。
画面 9: IDEA 控制台显示 GatewayApplication 启动日志，包括 Eureka 注册和初始化。
画面 10: 浏览器访问 Eureka 服务注册中心页面，显示 COLD-GATEWAY 和 COLD-USER 服务已注册，但出现 Eureka 可能错误地将实例标记为 UP 的警告。
画面 11: 在 Postman 中创建一个 POST 请求，用于测试用户登录接口。
画面 12: 在 Postman 中，请求体中填写用户名和密码，准备发送登录请求。
画面 13: 展示 PPT 页面，标题为“使用 API 网关后的优点”，并包含一个架构图，显示 Web 前端通过 API 网关访问后端服务。
画面 14: IDEA 控制台显示 GatewayApplication 启动日志，包括 DispatcherServlet 初始化和用户服务启动。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 2:
```yaml
server:
  context-path: /cold
```

画面 3:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
```

画面 4:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 6:
```yaml
spring:
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
      routes:
        - id: cold-user-router
          uri: lb://cold-user
          predicates:
            - Path=/cold/user/**
```

画面 13:
架构图结构：
- Web 前端 → API 网关
- API 网关 → 服务
- API 网关 → 服务
- API 网关 → 服务

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13:
标题：使用 API 网关后的优点：
- 易于监控。可以在网关收集监控数据并将其发送到外部系统进行分析。
- 易于认证。可以在网上进行认证，然后再将请求转发到后端的服务，而无需在每个微服务中进行认证。
- 减少了客户端与各个微服务之间的交互次数。

架构图结构：
- Web 前端 → API 网关
- API 网关 → 服务
- API 网关 → 服务
- API 网关 → 服务

表格数据：
画面 8 和 10:
| Application | AMIs | Availability Zones | Status |
|-------------|------|--------------------|--------|
| COLD-EUREKA-SERVER | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-eureka-server:8001 |
| COLD-GATEWAY | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-gateway:8080 |
| COLD-USER | n/a (1) | (1) | UP (1) - 192.168.145.128:cold-user:8185 |

画面 10:
| Name | Value |
|------|-------|
| total-avail-memory | 33mb |
| environment | test |
| num-of-cpus | 4 |

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
