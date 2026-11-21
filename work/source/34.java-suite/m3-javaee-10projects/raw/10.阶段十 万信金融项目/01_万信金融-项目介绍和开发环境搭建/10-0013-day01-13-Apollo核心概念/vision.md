# 画面线理解：day01-13-Apollo核心概念

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-13-Apollo核心概念_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:16, 01:44, 02:11, 02:32, 03:46, 05:07, 05:54, 06:04, 06:20, 06:30, 07:07, 07:27, 07:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:08:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Apollo 配置中心创建项目、查看和管理微服务的配置，以及在 IntelliJ IDEA 中配置 Spring Cloud 服务的相关属性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Apollo 配置中心的主界面，展示已有的项目（如 uaa-service、depository-agent-service 等）和“创建项目”按钮。
画面 2: 在 IntelliJ IDEA 中打开 `application.yml` 文件，显示 Eureka 服务配置，包括 `server.port: 53000` 和 `eureka.client.serviceUrl.defaultZone`。
画面 3: 显示 Apollo 配置中心的“创建项目”页面，包含“部门”、“应用ID”、“应用名称”、“应用负责人”、“项目管理员”等输入框。
画面 4: Apollo 配置中心页面空白，可能为页面加载或跳转后的状态。
画面 5: Apollo 配置中心页面空白，可能为页面加载或跳转后的状态。
画面 6: Apollo 配置中心显示“consumer-service”项目的配置列表，包括 `micro_service.spring-boot-http`、`micro_service.spring-eureka` 等配置项。
画面 7: 显示 PPT 页面“3.4 核心概念”，内容包括项目（appID）、环境（env）、集群（cluster）、命名空间（namespaces）的定义。
画面 8: 在 IntelliJ IDEA 中显示 `application.yml` 文件，内容与画面 2 相同。
画面 9: 在 IntelliJ IDEA 中显示 `application.properties` 文件，包含 `spring.application.name=consumer-service`、`server.servlet.context-path=/consumer`、`swagger.enable=true`、`logging.config=classpath:log4j2-dev.xml`、`spring.mvc.throw-exception-if-no-handler-found=true`、`spring.http.encoding.charset=UTF-8`、`spring.http.encoding.force=true`、`spring.http.encoding.enabled=true` 等配置。
画面 10: 在 IntelliJ IDEA 中显示 `application.properties` 文件，内容与画面 9 相同，但高亮显示了 `springCloud eureka配置` 部分。
画面 11: 在 IntelliJ IDEA 中显示 `application.properties` 文件，高亮显示 `ribbon.MaxAutoRetries=2` 和 `ribbon.ConnectTimeout=3000` 等配置。
画面 12: Apollo 配置中心显示“consumer-service”项目的公共配置，包括 `micro_service.spring-boot-redis`、`micro_service.mybatis-plus`、`micro_service.spring-boot-druid`、`micro_service.spring-rocketmq`、`micro_service.files`、`micro_service.spring-cloud-hmily` 等。
画面 13: 在 IntelliJ IDEA 中显示 `application.properties` 文件，内容与画面 11 相同。
画面 14: 显示 PPT 页面“3.5 玩转Apollo”，内容与画面 7 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```yaml
spring:
  application:
    name: nrmic-discovery
server:
  port: 53000

eureka:
  server:
    enable-self-preservation: false
    eviction-interval-timer-in-ms: 10000
    should-discard-only-response-cache: true
  client:
    register-with-eureka: false
    fetch-registry: false
    serviceUrl:
      defaultZone: http://localhost:${server.port}/eureka/
    instance:
      hostname: ${spring.cloud.client.ip-address}
```

画面 9:
```properties
# 应用程序名称
spring.application.name=consumer-service

# 指定服务访问路径
server.servlet.context-path=/consumer

# 开启 swagger
swagger.enable=true

# 日志配置
logging.config=classpath:log4j2-dev.xml

# spring 全局异常处理
spring.mvc.throw-exception-if-no-handler-found=true

# 中文乱码处理
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
spring.http.encoding.enabled=true
```

画面 10:
```properties
# springCloud eureka配置
eureka.client.serviceUrl.defaultZone=http://localhost:53000/eureka/
# 本项目使用 ip 地址，不使用服务名
eureka.instance.preferIpAddress=true
eureka.instance.instance-id=${spring.cloud.client.ip-address}:${server.port}

# springCloud ribbon配置
ribbon.MaxAutoRetries=2
# 最大重试次数，当 eureka 中可以找到服务，但是服务法不上时将会重试
ribbon.ConnectTimeout=3000
# 对所有请求都进行重试，如果是 get 可以，如果是 post、put 等报告有实现幂等的情况下是不被复的，所以设置为 false
ribbon.OkToRetryOnAllOperations=false
# 请求处理的超时时间
ribbon.ReadTimeout=30000
# 外部实例的重试次数
ribbon.MaxAutoRetriesNextServer=2
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7:
标题：3.4 核心概念
内容：
1. 项目（应用）
   - 关键字：appID
2. environment（环境）
   - 关键字：env
3. cluster（集群）
   - 关键字：cluster
4. namespace（命名空间）
   - 关键字：namespaces

画面 14:
标题：3.5 玩转Apollo
内容：
与画面 7 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
