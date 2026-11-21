# 画面线理解：day04-13-集成UAA服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-13-集成UAA服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:35, 03:11, 04:00, 04:29, 05:40, 07:16, 08:09, 09:33, 10:07, 11:04, 11:45, 12:32, 12:58, 13:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:49:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在项目中集成 UAA 服务，并通过 Apollo 配置中心进行配置管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 中“3.1 UAA服务简介”内容，说明 UAA 服务是 P2P 平台的统一认证中心，集成认证与授权功能，使用 Spring Security 整合 OAuth2.0 实现授权服务器角色。
画面2：在 IntelliJ IDEA 中，通过“Project Structure”对话框，添加新模块“wanning2p-uaa-service”。
画面3：在 `pom.xml` 文件中，展示添加了 `spring-cloud-starter-netflix-eureka-client` 依赖。
画面4：在 `application.properties` 文件中，配置了不同环境的 `meta` 地址，如 `dev.meta`、`fat.meta`、`uat.meta`、`pro.meta`。
画面5：在 IntelliJ IDEA 中，右键点击项目，选择“Edit Configurations...”，准备启动服务。
画面6：展示 UAA 登录页面，包含“密码”、“安全提问”输入框和“提交”按钮。
画面7：展示课程 PPT 中关于 Apollo 配置中心的内容，说明需要新建一个项目 uaa-service，并关联 common-template 中的公共 namespace。
画面8：浏览器访问 `localhost:8070`，页面为空白，提示“正在等待导入缓存...”。
画面9：在 Apollo 配置中心页面，选择“应用”为 uaa-service，环境为 DEV，选择 namespace 并点击“提交”。
画面10：展示课程 PPT 中关于配置内容的说明，包括 `server.servlet.context-path=/uaa` 和 `spring.datasource.url` 的配置。
画面11：在 Apollo 配置中心页面，展示 `micro_service.spring-boot-druid` 的配置项，包括 `spring.datasource.url` 和 `spring.datasource.type`。
画面12：在 IntelliJ IDEA 的终端中，启动服务后，日志显示服务已启动并注册到 Eureka 服务发现中心。
画面13：在 IntelliJ IDEA 的终端中，日志显示 Apollo 配置中心同步失败，提示“Load config failed, will retry in 1 SECONDS”。
画面14：在 IntelliJ IDEA 的终端中，日志显示服务启动成功，包括 UAA 服务和 DiscoveryClient 的启动信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<groupId>cn.itcast.wanning2p</groupId>
<version>1.0-SNAPSHOT</version>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.0.RELEASE</version>
</parent>
<artifactId>wanning2p-uaa-service</artifactId>
<dependencies>
    <dependency>
        <groupId>cn.itcast.wanning2p</groupId>
        <artifactId>wanning2p-api</artifactId>
        <version>${project.version}</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
</dependencies>
```

画面4：
```properties
dev.meta=http://localhost:8080
fat.meta=http://211.103.136.242:7287
uat.meta=http://172.17.0.83:8080
pro.meta=http://211.103.136.242:7134
```

画面10：
```properties
server.servlet.context-path=/uaa
micro_service.spring-boot-http命名空间：
micro_service.spring-boot-druid命名空间：
spring.datasource.url=jdbc:mysql://localhost:3306/p2p_uaa?useUnicode=true
```

画面11：
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/p2p_uaa?useUnicode=true
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“3.集成UAA服务”，子标题“3.1 UAA服务简介”。
画面7：标题为“3.1 UAA服务简介”，内容包括“访问Apollo，新建一个项目uaa-service，关联common-template中的公共namespace”。
画面10：标题为“4.启动测试”，内容包括“server.servlet.context-path=/uaa”和“spring.datasource.url”配置。
画面11：在 Apollo 配置中心页面，展示“micro_service.spring-boot-druid”配置项，包括“Key”和“Value”列。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
