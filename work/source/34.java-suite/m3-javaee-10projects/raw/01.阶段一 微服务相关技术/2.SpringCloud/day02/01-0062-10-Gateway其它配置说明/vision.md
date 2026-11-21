# 画面线理解：10-Gateway其它配置说明

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\10-Gateway其它配置说明_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:53, 03:00, 04:15, 04:24, 05:29, 05:37, 05:49, 06:08, 07:06, 08:05, 08:23, 08:28, 09:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:26:26

1) 这一组画面整体在讲 Spring Cloud Gateway 的跨域配置、高可用性以及与 Feign 的区别。

2) 按时间顺序列出每张画面的要点：
画面1: 讲解 Gateway 默认集成的 Ribbon 负载均衡和 Hystrix 熔断机制，并展示配置示例。
画面2: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 Hystrix 与 Ribbon 的配置。
画面3: 讲解访问 Spring Cloud Gateway 时可能出现的跨域问题，并引出解决方案。
画面4: 展示 Gateway 的跨域配置，具体为 spring.cloud.gateway.globalcors 配置。
画面5: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。
画面6: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。
画面7: 展示浏览器访问用户服务的返回结果。
画面8: 展示浏览器访问用户服务的返回结果。
画面9: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。
画面10: 讲解 Gateway 的高可用性，以及外部访问时的代理方案。
画面11: 展示 Spring Cloud Gateway 的其它配置说明和 Spring Cloud Config 分布式配置中心简介。
画面12: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。
画面13: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。
画面14: 展示 Gateway 的 application.yml 配置文件，包含路由、过滤器和 CORS 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
hystrix:
  command:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 6000
ribbon:
  ConnectTimeout: 1000
  ReadTimeout: 2000
  MaxAutoRetries: 0
  MaxAutoRetriesNextServer: 0

画面2:
Path=/api/user/**
filters:
  # 添加请求路径的前缀
  - PrefixPath=/user
  # 表示过滤1个路径，2表示两个路径，以此类推
  StripPrefix=1
MyParamName
default-filters:
  - AddResponseHeader=X-Response-Foo, Bar
  - AddResponseHeader=abc-myname,heima
globalcors:
  corsConfigurations:
    '[/*]':
      # 这种写法或者下面的都可以，*表示全部
      allowedOrigins:
        - "http://docs.spring.io"
      allowedMethods:
        - GET

画面3:
spring:
  cloud:
    gateway:
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面4:
spring:
  cloud:
    gateway:
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面5:
cloud:
  gateway:
    routes:
      - id: user-service-route
        # 代理服务地址
        #uri: http://127.0.0.1:9091
        # 从eureka中获取真实服务
        uri: lb://user-service
        # 路由说明：可以匹配的路径
        predicates:
          - Path=/user/**
          - Path=/api/user/**
        filters:
          # 添加请求路径的前缀
          - PrefixPath=/user
          # 表示过滤1个路径，2表示两个路径，以此类推
          StripPrefix=1
          MyParamName
      default-filters:
        - AddResponseHeader=X-Response-Foo, Bar
        - AddResponseHeader=abc-myname,heima
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面6:
cloud:
  gateway:
    routes:
      - id: user-service-route
        # 代理服务地址
        #uri: http://127.0.0.1:9091
        # 从eureka中获取真实服务
        uri: lb://user-service
        # 路由说明：可以匹配的路径
        predicates:
          - Path=/user/**
          - Path=/api/user/**
        filters:
          # 添加请求路径的前缀
          - PrefixPath=/user
          # 表示过滤1个路径，2表示两个路径，以此类推
          StripPrefix=1
          MyParamName
      default-filters:
        - AddResponseHeader=X-Response-Foo, Bar
        - AddResponseHeader=abc-myname,heima
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面7:
{
  "id": 8,
  "username": "stuart",
  "password": "123456",
  "age": 21,
  "birthday": "2000-07-07T16:30:00.000+0000",
  "created": "2014-09-20T03:41:15.000+0000",
  "updated": "2014-09-20T03:41:15.000+0000",
  "note": "传智播客培训"
}

画面8:
{
  "id": 8,
  "username": "stuart",
  "password": "123456",
  "age": 21,
  "birthday": "2000-07-07T16:30:00.000+0000",
  "created": "2014-09-20T03:41:15.000+0000",
  "updated": "2014-09-20T03:41:15.000+0000",
  "note": "传智播客培训"
}

画面9:
cloud:
  gateway:
    routes:
      - id: user-service-route
        # 代理服务地址
        #uri: http://127.0.0.1:9091
        # 从eureka中获取真实服务
        uri: lb://user-service
        # 路由说明：可以匹配的路径
        predicates:
          - Path=/user/**
          - Path=/api/user/**
        filters:
          # 添加请求路径的前缀
          - PrefixPath=/user
          # 表示过滤1个路径，2表示两个路径，以此类推
          StripPrefix=1
          MyParamName
      default-filters:
        - AddResponseHeader=X-Response-Foo, Bar
        - AddResponseHeader=abc-myname,heima
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面10:
spring:
  cloud:
    gateway:
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面11:
spring:
  cloud:
    gateway:
      globalcors:
        corsConfigurations:
          '[/*]':
            # 这种写法或者下面的都可以，*表示全部
            allowedOrigins:
              - "http://docs.spring.io"
            allowedMethods:
              - GET

画面12:
cloud:
  gateway:
    routes:
      - id: user-service-route
        # 代理服务地址
        #uri: http://127.0.0.1:9091
        # 从eureka中获取真实服务
        uri: lb://user-service
        # 路由说明：可以匹配的路径
        predicates:
          - Path=/user/**
          - Path=/api/user/**
        filters:
          # 添加请求路径的前缀
          - PrefixPath=/user
          # 表示过滤1个路径，2表示两个路径，以此类推
          StripPrefix=1
          MyParamName
      default-filters:
        - AddResponseHeader=X-Response-Foo, Bar
        - AddResponseHeader=abc
