# 画面线理解：day01-8-微服务基础工程测试

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-8-微服务基础工程测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:32, 01:09, 01:37, 02:05, 02:43, 03:00, 03:17, 03:41, 04:43, 05:08, 05:25, 06:13, 06:36, 07:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:04:35

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务架构，包含服务注册发现（Eureka）、API 网关（Zuul）和消费者服务，并通过浏览器访问网关路由到消费者服务的接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了微服务架构图，包含 waning2p-gateway-service、waning2p-api、waning2p-common、waning2p-consumer-service 和 waning2p-discover-server 五个服务模块，以及它们之间的调用关系（如网关调用 API，API 调用 Common，Consumer Service 调用 Common，Consumer Service 调用 Eureka 注册中心）。
画面 2: 在 IntelliJ IDEA 中，显示了 waning2p-consumer-service 项目的目录结构，选中了 test 目录。
画面 3: 展示了微服务架构图，与画面 1 类似，但顶部增加了 Spring Boot 模块，并标注了“2）基础工程关系图”。
画面 4: 在 IntelliJ IDEA 的 Run/Debug Configurations 中，配置了两个服务的启动参数：ConsumerService 的 VM options 为 -Dserver.port=3050，GatewayServer 的 VM options 为 -Dserver.port=32010。
画面 5: 在 IntelliJ IDEA 中，显示了多个服务（DiscoveryServer、GatewayServer、ConsumerService）正在运行，但未显示具体代码或配置。
画面 6: 在 IntelliJ IDEA 的 Console 中，显示了 DiscoveryClient 的日志，包括服务注册成功、心跳检测等信息。
画面 7: 在 IntelliJ IDEA 的 Console 中，显示了 Eureka Server 启动成功，端口为 10988。
画面 8: 在浏览器中访问 Eureka 服务注册中心，显示了服务注册信息，包括 CONSUMER-SERVICE 和 GATEWAY-SERVER 两个服务的实例状态为 UP。
画面 9: 浏览器地址栏为空，页面空白。
画面 10: 浏览器中显示了多个窗口的截图，包括 IDEA、浏览器、文件夹、记事本等。
画面 11: 在 IntelliJ IDEA 中，显示了 ConsumerController 的代码，包含 @RestController、@Api、@ApiOperation、@GetMapping 等注解，以及一个简单的 hello 接口。
画面 12: 在 IntelliJ IDEA 中，显示了 GatewayServer 的 ConsumerController 代码，与画面 11 的代码内容相同。
画面 13: 在 IntelliJ IDEA 中，显示了 GatewayServer 的 application.properties 配置文件，其中包含 Zuul 的路由配置，如 zuul.routes.consumer-service.path=/consumer/**、zuul.add-host-header=true、zuul.ignoredServices=。
画面 14: 在 IntelliJ IDEA 中，显示了 ConsumerService 的项目结构，选中了 controller 目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13 的 application.properties 配置：
```properties
# springCloud zuul相关配置
# 请求没有前缀，不用去除前缀进行请求转发
zuul.routes.consumer-service.stripPrefix=false
# 开启测试
zuul.retryable=true
# 网关转发请求头信息
zuul.add-host-header=true
# 关闭自路由配置，全部手动配置，更安全
zuul.ignoredServices=
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 3 的架构图：
- Spring Boot 指向 waning2p-gateway-service（通过“继承”关系）。
- waning2p-gateway-service 指向 waning2p-api（通过“请求”关系）。
- waning2p-api 指向 waning2p-common（通过“请求”关系）。
- waning2p-common 指向 waning2p-consumer-service（通过“请求”关系）。
- waning2p-consumer-service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-gateway-service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-api 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-consumer-service 指向 waning2p-discover-server（通过“请求”关系）。
- waning2p-common 指向 waning2p-discover-server（通过“请求”关系）。

画面 8 的表格数据：
- Application: CONSUMER-SERVICE, GATEWAY-SERVER
- AMIs: n/a (1), n/a (1)
- Availability Zones: (1), (1)
- Status: UP (1 - consumer-service:192.168.2.153:3050), UP (1 - gateway-server:192.168.2.153:32010)

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
