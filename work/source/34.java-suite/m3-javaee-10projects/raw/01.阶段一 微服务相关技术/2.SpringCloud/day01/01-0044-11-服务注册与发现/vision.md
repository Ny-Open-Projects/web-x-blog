# 画面线理解：11-服务注册与发现

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\11-服务注册与发现_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 03:21, 04:02, 05:42, 06:23, 07:19, 08:08, 09:30, 10:31, 11:34, 12:02, 13:02, 13:45, 14:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:12:57

1) 这一组画面整体在讲如何在 Spring Cloud 项目中实现服务注册与发现，通过 Eureka Server 注册服务并由消费者通过 DiscoveryClient 获取服务地址。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT，标题为“11. 服务注册与发现”，目标是将 user-service 注册到 Eureka 并在 consumer-demo 中通过服务名调用；下方有“12. Eureka Server 高可用配置”标题。
画面 2: IDE 中展示项目结构，选中 consumer-demo 的 target 目录。
画面 3: IDE 中展示 user-service 的 UserApplication.java 文件，包含 @SpringBootApplication 和 @MapperScan 注解。
画面 4: IDE 中展示 user-service 的运行状态，控制台显示 EurekaServerApplication:10086 和 UserApplication 成功启动。
画面 5: 浏览器访问 Eureka Server 管理界面，显示 USER-SERVICE 服务实例已注册，状态为 UP。
画面 6: IDE 中编辑 consumer-demo 的 application.yml 文件，正在输入 spring.application.name。
画面 7: IDE 中展示 ConsumerController.java 文件，包含 @RestController 和 @Autowired 注解，定义了 queryById 方法。
画面 8: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 9: IDE 中展示 ConsumerApplication.java 文件，包含 @SpringBootApplication 和 @EnableDiscoveryClient 注解。
画面 10: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 11: IDE 中展示 ConsumerController.java 文件，正在修改 queryById 方法，使用 discoveryClient 获取服务实例。
画面 12: 展示课程 PPT，列出服务注册与发现的步骤，包括添加 Eureka 客户端依赖、修改启动类注解、修改配置文件。
画面 13: IDE 中展示 ConsumerApplication.java 文件，正在添加 @EnableDiscoveryClient 注解。
画面 14: 展示课程 PPT，列出添加 Eureka 客户端依赖、添加启动类注解、修改配置的步骤，并展示 application.yml 文件内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
spring:
  application:
    name: eureka-server
  eureka:
    client:
      service-url:
        # eureka 服务地址，如果集群的话，需要指定多个 eureka 地址
        defaultZone: http://127.0.0.1:10086/eureka
      # 不注册自己
      register-with-eureka: false
      # 不拉取服务
      fetch-registry: false

画面 6:
spring:
  application:
    name: consumer-demo
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka

画面 14:
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

画面 14:
spring:
  application:
    name: consumer-demo
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“11. 服务注册与发现”，目标“将user-service的服务注册到eureka并在consumer-demo中可以根据服务名称调用”，分析“服务注册：在服务提供工程user-service上添加eureka客户端依赖；服务发现：”，小结“添加Eureka客户端依赖；添加启动类注解；修改配置”。
画面 12: 标题“服务注册与发现”，分析“服务注册：在服务提供工程user-service上添加Eureka客户端依赖；自动将服务注册到EurekaServer服务地址列表。添加依赖：修改启动类注解：添加并开启Eureka客户端发现的注解；修改配置文件：设置Eureka服务地址。服务发现：在服务消费工程consumer-demo中添加Eureka客户端依赖；可以使用工具类根据服务名称获取对应的服务地址列表。添加依赖：改造启动类注解：添加开启Eureka客户端发现的注解；修改配置文件：设置Eureka服务地址；改造处理类ConsumerController，可以使用工具类DiscoveryClient根据服务名称获取对应服务地址列表。”，小结“添加Eureka客户端依赖；添加启动类注解；修改配置”。
画面 14: 标题“添加Eureka客户端依赖”，“添加启动类注解”，“修改配置”，并展示 application.yml 文件内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
