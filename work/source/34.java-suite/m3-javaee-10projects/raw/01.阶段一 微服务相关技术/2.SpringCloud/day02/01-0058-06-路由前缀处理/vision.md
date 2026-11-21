# 画面线理解：06-路由前缀处理

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\06-路由前缀处理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:44, 02:46, 03:31, 04:19, 04:33, 04:39, 04:49, 04:51, 05:21, 06:41, 06:45, 07:03, 07:15, 07:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:23:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud Gateway 中通过配置路由前缀（PrefixPath）和去除前缀（StripPrefix）来动态处理请求路径。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，说明目标是使用 Eureka 注册的服务作为路由地址，分析指出路由地址写死不合理，可通过配置动态路由解决，小结说明需在 Eureka 注册服务名。
画面2：展示修改 gateway 项目配置文件，配置 server 端口和 application 名称，以及 gateway 路由配置，其中 routes 配置了 id、uri、predicates 和 filters。
画面3：展示配置文件中 filters 部分，说明 PrefixPath 用于添加前缀，举例说明添加前缀的效果。
画面4：展示配置文件中 filters 部分，说明 StripPrefix 用于去除前缀，举例说明去除前缀的效果。
画面5：展示浏览器访问 http://localhost:10010/8，返回用户信息 JSON 数据。
画面6：展示配置文件中 filters 部分，说明 StripPrefix 用于去除前缀，举例说明去除前缀的效果。
画面7：展示浏览器访问 http://localhost:10010/8，返回用户信息 JSON 数据。
画面8：展示课程文档，说明目标是通过配置 StripPrefix 过滤器实现去除路径前缀。
画面9：展示配置文件中 filters 部分，说明 StripPrefix 用于去除前缀，举例说明去除前缀的效果。
画面10：展示运行日志，显示 GatewayApplication 启动成功。
画面11：展示配置文件中 filters 部分，说明 StripPrefix 用于去除前缀，举例说明去除前缀的效果。
画面12：展示浏览器访问 http://localhost:10010/8，返回用户信息 JSON 数据。
画面13：展示配置文件中 filters 部分，说明 StripPrefix 用于去除前缀，举例说明去除前缀的效果。
画面14：展示课程文档，说明目标是通过配置 StripPrefix 过滤器实现去除路径前缀。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
server:
  port: 10010
spring:
  application:
    name: api-gateway
cloud:
  gateway:
    routes:
      - id: user-service-route
        uri: lb://user-service
        predicates:
          - Path=/**
        filters:
          - PrefixPath=/user

画面3：
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10006/eureka
    prefer-ip-address: true

画面4：
spring:
  application:
    name: api-gateway
cloud:
  gateway:
    routes:
      - id: user-service-route
        uri: lb://user-service
        predicates:
          - Path=/api/user/**
        filters:
          - PrefixPath=/user
          - StripPrefix=1

画面6：
spring:
  application:
    name: api-gateway
cloud:
  gateway:
    routes:
      - id: user-service-route
        uri: lb://user-service
        predicates:
          - Path=/api/user/**
        filters:
          - StripPrefix=1

画面9：
spring:
  application:
    name: api-gateway
cloud:
  gateway:
    routes:
      - id: user-service-route
        uri: lb://user-service
        predicates:
          - Path=/api/user/**
        filters:
          - StripPrefix=1

画面13：
spring:
  application:
    name: api-gateway
cloud:
  gateway:
    routes:
      - id: user-service-route
        uri: lb://user-service
        predicates:
          - Path=/api/user/**
        filters:
          - StripPrefix=1

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“6. 路由前缀处理”，目标是“可以对请求到相关服务的地址添加或去除前缀”，分析为“提供服务的地址：http://127.0.0.1:9091/user/8”，小结为“添加前缀：对请求地址添加前缀路径之后再作为代理的服务地址；去除前缀：将请求地址中路径去除一些前缀路径之后再作为代理的服务地址”。
画面8：PPT 标题为“2.6.2. 去除前缀”，内容为“在 gateway 中可以通过配置路由的过滤器 StripPrefix，实现映射路径中地址的去除”。
画面14：PPT 标题为“6. 路由前缀处理”，目标是“可以对请求到相关服务的地址添加或去除前缀”，分析为“提供服务的地址：http://127.0.0.1:9091/user/8”，小结为“添加前缀：对请求地址添加前缀路径之后再作为代理的服务地址；去除前缀：将请求地址中路径去除一些前缀路径之后再作为代理的服务地址”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
