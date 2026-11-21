# 画面线理解：05-面向服务的路由

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\05-面向服务的路由_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:53, 01:12, 01:44, 01:53, 02:22, 02:30, 02:42, 02:58, 03:01, 03:17, 03:31, 04:10, 04:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:23:13

1) 这一组画面整体在讲如何通过 Spring Cloud Gateway 实现面向服务的路由，利用 Eureka 注册中心动态获取服务地址并结合 Ribbon 实现负载均衡。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 gateway 配置文件中的路由规则，uri 指向固定 IP，predicates 为 /user/**，并说明了 Eureka 客户端配置。
画面2: 展示了 gateway 配置文件，uri 改为 lb://user-service，说明了使用服务名而非 IP，同时展示了目录结构和章节导航。
画面3: 说明了修改映射配置，通过 Eureka 获取服务地址，并展示了 application.yml 文件内容。
画面4: 说明了启动测试，再次启动 gateway 时会利用 Ribbon 进行负载均衡访问。
画面5: 与画面4内容相同，无新增要点。
画面6: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务。
画面7: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面8: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面9: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面10: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面11: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面12: 与画面4内容相同，无新增要点。
画面13: 展示了 IDEA 中的项目结构，application.yml 文件中 uri 为 http://127.0.0.1:9091，同时显示了运行中的服务和控制台日志。
画面14: 展示了文档内容，说明了面向服务的路由只需在配置文件中指定路由路径如 lb://user-service，并介绍了路由前缀处理。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
gateway:
  routes:
    - id: user-service-route
      # 代理的服务地址
      uri: http://127.0.0.1:9091
      # 路由断言：可以匹配的路径
      predicates:
        - Path=/user/**
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    instance:
      prefer-ip-address: true

画面2:
application:
  name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-service-route
          # 代理的服务地址：lb表示从eureka中获取具体服务
          uri: lb://user-service
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面3:
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-service-route
          # 代理的服务地址：lb表示从eureka中获取具体服务
          uri: lb://user-service
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面4:
uri: lb://user-service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面6:
server:
  port: 10010
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        # 路由id，可以随意写
        - id: user-service-route
          # 代理的服务地址：lb表示从eureka中获取具体服务
          uri: http://127.0.0.1:9091
          # 路由断言，可以配置规则路径
          predicates:
            - Path=/user/**

画面12:
uri: lb://user-service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面13:
uri: lb://user-service
# 路由断言，可以配置规则路径
predicates:
  - Path=/user/**

画面14:
# 路由断言：可以匹配的路径
predicates:
  - Path=/user/**

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 标题为“5. 面向服务的路由”，目标为“使用在eureka注册的服务作为路由地址”，分析为“如果将路由服务地址与死循环是不合理的；在 Spring Cloud Gateway 中可以通过配置动态路由来解决”，小结为“面向服务的路由：只需要在配置文件中指定路由路径类似：lb://user-service”。
画面2: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面4: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面12: 标题为“2.5.2 启动测试”，内容为“再次启动 heima-gateway，这次gateway进行代理时，会利用Ribbon进行负载均衡访问：http://localhost:10010/user/8”。
画面14: 标题为“5. 面向服务的路由”，目标为“使用在eureka注册的服务作为路由地址”，分析为“如果将路由服务地址与死循环是不合理的；在 Spring Cloud Gateway 中可以通过配置动态路由来解决”，小结为“面向服务的路由：只需要在配置文件中指定路由路径类似：lb://user-service”。
画面14: 标题为“6. 路由前缀处理”，目标为“可以对请求到相关服务的地址添加前缀”。

5) 无。
