# 画面线理解：day01-15-微服务集成Apollo客户端

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-15-微服务集成Apollo客户端_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:43, 02:52, 03:50, 05:17, 06:19, 06:50, 07:18, 07:34, 08:18, 08:52, 09:23, 09:57, 10:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:09:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务项目中集成并使用 Apollo 配置中心，包括配置文件的创建、客户端依赖的添加、以及在 Apollo 控制台中管理配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 显示 Apollo 配置中心的 Web 界面，应用名为 consumer-service，环境为 DEV。
- 列出多个配置项，包括 application、micro_service.spring-boot-http、micro_service.spring-eureka、micro_service.spring-hystrix、micro_service.spring-ribbon、micro_service.spring-boot-redis。

画面 2:
- 显示 IntelliJ IDEA 中的 application.properties 文件内容。
- 代码内容：
  ```
  # springCloud eureka配置
  eureka.client.serviceUrl.defaultZone=http://localhost:53000/eureka/
  # 此时使用 /v1/api，不使用原名
  eureka.instance.preferIpAddress=true
  eureka.instance.instanceId=${spring.cloud.client.ip-address}:${server.port}
  # springCloud ribbon配置
  # 最大重试次数，如果在eureka中可以找到服务，但是服务挂了上时将会重试
  ribbon.MaxAutoRetries=2
  # 重试间隔时间
  ribbon.ConnectTimeout=3000
  # 如果是get请求可以，如果是post、put等操作在实现幂等的情况下不是很危险的，所以设置为false
  ribbon.OkToRetryAllOperations=false
  # 请求处理的时间
  ribbon.ReadTimeout=20000
  # 轮询实例的重试次数
  ribbon.MaxAutoRetriesNextServer=2
  ```

画面 3:
- 显示 PPT 页面，标题为“3 使用 Apollo”，子标题“2.5.4 浏览全貌”。
- 架构图：用户（人形图标）→ 修改/发布配置 → Apollo 配置中心 → Apollo 客户端 → 本地应用（获取配置、更新通知）→ 本地文件缓存（sync）。

画面 4:
- 显示 Apollo 配置中心界面，同时分屏显示多个窗口，包括 Google Chrome 浏览器、PDF 文档、IDEA 编辑器等。
- 画面下方显示 Apollo 配置中心的配置项，包括 micro_service.spring-ribbon 和 micro_service.spring-boot-redis。

画面 5:
- 显示 PPT 页面，标题为“4.2 添加配置”，子标题“4.2.1 配置文件”。
- 代码内容：
  ```
  # 开发环境
  dev.meta=http://localhost:8080
  # 功能验收测试环境
  fat.meta=http://apollo.fat.xxx.com
  # 用户验收测试环境
  uat.meta=http://apollo.uat.xxx.com
  # 生产环境
  pro.meta=http://apollo.xxx.com
  ```

画面 6:
- 显示 PPT 页面，标题为“4.2 添加配置”，子标题“4.2.1 配置文件”。
- 代码内容：
  ```
  # 项目ID
  app.id=account-service
  ```

画面 7:
- 显示 Apollo 配置中心界面，同时分屏显示多个窗口，包括 Google Chrome 浏览器、PDF 文档、IDEA 编辑器等。
- 画面下方显示 Apollo 配置中心的配置项，包括 micro_service.spring-ribbon 和 micro_service.spring-boot-redis。

画面 8:
- 显示 Apollo 配置中心界面，应用名为 consumer-service，环境为 DEV。
- 列出多个配置项，包括 application、micro_service.spring-boot-http、micro_service.spring-eureka、micro_service.spring-hystrix、micro_service.spring-ribbon、micro_service.spring-boot-redis。

画面 9:
- 显示 Apollo 配置中心界面，应用名为 consumer-service，环境为 DEV。
- 选中 application 配置项，显示 Key 和 Value 列表，包括 swagger.enable=true 和 spring.mvc.throw-exception-if-no-handler-found=true。

画面 10:
- 显示 PPT 页面，标题为“4.2 添加配置”，子标题“4.2.2 启动参数”。
- 画面下方显示多个窗口，包括 PDF 文档、IDEA 编辑器等。

画面 11:
- 显示 PPT 页面，标题为“4.2 添加配置”，子标题“4.2.2 启动参数”。
- 代码内容：
  ```
  # 项目ID
  app.id=account-service
  # 启动时投递注入配置（提高优先级）
  apollo.bootstrap.enabled=true
  # 使用哪些命名空间中的配置项
  apollo.bootstrap.namespaces=application,micro_service.spring-boot-http,spring-rocketmq
  # 服务端口
  server.port=63000
  ```
- VM Options：
  ```
  -Denv=DEV -Dapollo.cluster=DEFAULT
  ```

画面 12:
- 显示 Apollo 配置中心界面，应用名为 consumer-service，环境为 DEV。
- 选中 application 配置项，显示 Key 和 Value 列表，包括 swagger.enable=true 和 spring.mvc.throw-exception-if-no-handler-found=true。

画面 13:
- 显示 PPT 页面，标题为“4.2 添加配置”，子标题“4.2.1 配置文件”。
- 代码内容：
  ```
  <dependency>
      <groupId>com.ctrip.framework.apollo</groupId>
      <artifactId>apollo-client</artifactId>
      <version>1.1.0</version>
  </dependency>
  ```

画面 14:
- 显示 PPT 页面，标题为“4 微服务集成 Apollo 客户端”，子标题“4.1 添加依赖”。
- 代码内容：
  ```
  <dependency>
      <groupId>com.ctrip.framework.apollo</groupId>
      <artifactId>apollo-client</artifactId>
      <version>1.1.0</version>
  </dependency>
  ```
