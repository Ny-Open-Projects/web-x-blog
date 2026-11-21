# 画面线理解：13-获取配置中心配置

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\13-获取配置中心配置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 01:41, 01:54, 02:03, 02:57, 04:25, 06:11, 06:20, 06:32, 07:06, 08:44, 09:08, 09:17, 09:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:28:25

1) 这一组画面整体在讲什么（一句话）：
演示如何将 Spring Cloud 服务的配置文件从本地修改为从配置中心（如 Git 仓库）动态获取，并展示相关配置文件的修改和启动过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中提到“将服务提供工程 user-service 的 application.yml 配置文件删除，修改为从配置中心 config server 中获取”。
画面 2: 在 IntelliJ IDEA 中，展示 user-service 项目的 pom.xml 文件，其中已添加 spring-cloud-starter-config 依赖。
画面 3: 在 IntelliJ IDEA 中，展示 config-server 项目的 pom.xml 文件，其中包含 spring-cloud-starter-config 依赖。
画面 4: 在 IntelliJ IDEA 中，右键点击项目目录，弹出“New”菜单，准备创建新文件。
画面 5: 在 IntelliJ IDEA 中，打开并编辑 bootstrap.yml 文件，其中包含 spring.cloud.config.label、spring.cloud.config.profile 等配置项。
画面 6: 在浏览器中访问 http://127.0.0.1:10000/user-dev.yml，显示了从配置中心获取的配置内容。
画面 7: 在 IntelliJ IDEA 中，运行 user-service 项目，控制台输出显示服务启动成功，并包含 Eureka 和 Config Server 的初始化信息。
画面 8: 在 IntelliJ IDEA 中，控制台输出显示服务正在从配置中心（http://localhost:12000）获取配置。
画面 9: 在浏览器中，地址栏输入 http://127.0.0.1:10000/api/user/8，准备访问服务。
画面 10: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。
画面 11: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中“小结”部分提到“将原来的 application.yml 删除；然后添加 bootstrap.yml 配置文件，该文件也是 spring boot 的默认配置文件，其内会经常配置一些项目中固定的配置项。如果是项目经常变动的应该配置到 application.yml 中，现在使用了配置中心就应该配置到 Git 仓库中对应的配置文件。”
画面 12: 在 IntelliJ IDEA 中，运行 user-service 项目，控制台输出显示服务启动成功，并包含 Eureka 和 Config Server 的初始化信息。
画面 13: 在 IntelliJ IDEA 中，编辑 bootstrap.yml 文件，其中包含 spring.cloud.config.label、spring.cloud.config.profile 等配置项。
画面 14: 显示课程 PPT 页面，标题为“13. 获取配置中心配置”，内容包括目标、分析、需求和实现步骤。其中“小结”部分提到“将原来的 application.yml 删除；然后添加 bootstrap.yml 配置文件，该文件也是 spring boot 的默认配置文件，其内会经常配置一些项目中固定的配置项。如果是项目经常变动的应该配置到 application.yml 中，现在使用了配置中心就应该配置到 Git 仓库中对应的配置文件。”，并显示一个 <dependency> 代码块。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
cloud:
  config:
    server:
      git:
        uri: https://gitee.com/goheima/heima-config.git
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka
```

画面 2:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.0</version>
    <relativePath/>
</parent>

<groupId>com.heima.user</groupId>
<artifactId>user-service</artifactId>
<version>0.0.1-SNAPSHOT</version>
<packaging>jar</packaging>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.1.3</version>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-openfeign</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-zookeeper-discovery</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-zookeeper-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-consul-discovery</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-consul-config</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-redis</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-rocketmq</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-activemq</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-amqp</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-gateway</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-oauth2</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-security</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-amqp</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-kafka</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-rabbitmq</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-redis</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-zookeeper</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-consul</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-vertx</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webmvc</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-websocket</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webmvc</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-websocket</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-bus-webflux</artifactId>
    </dependency
