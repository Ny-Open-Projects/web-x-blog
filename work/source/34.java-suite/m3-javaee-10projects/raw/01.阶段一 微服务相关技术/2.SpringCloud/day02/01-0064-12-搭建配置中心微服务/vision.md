# 画面线理解：12-搭建配置中心微服务

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\12-搭建配置中心微服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:31, 02:30, 03:47, 04:15, 05:23, 06:05, 06:30, 07:02, 08:18, 08:55, 09:33, 09:47, 10:06, 11:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:27:34

1) 这一组画面整体在讲什么（一句话）：
搭建并配置 Spring Cloud 配置中心服务（config-server），使其从码云（Gitee）远程仓库获取配置文件，并集成 Eureka 服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“12. 搭建配置中心微服务”，目标是创建远程 git 仓库并搭建 config-server，分析部分提到使用 spring boot 方式搭建。
画面 2: 浏览器访问码云（Gitee）网站，准备创建新仓库。
画面 3: 在码云网站上创建名为 “heima-config” 的新仓库，选择 Java 语言和 Apache 2.0 协议。
画面 4: 在 IntelliJ IDEA 中新建模块，选择 Maven 项目，准备创建 config-server 项目。
画面 5: 显示 config-server 项目的 pom.xml 文件内容，包含 Spring Cloud Config Server 和 Eureka Client 的依赖。
画面 6: 显示 config-server 项目的 application.yml 文件，准备配置。
画面 7: 在 application.yml 文件中配置 server.port 和 spring.application.name。
画面 8: 在 application.yml 文件中配置 git 仓库地址和 Eureka 服务地址。
画面 9: 启动 config-server 服务，控制台显示服务启动成功并注册到 Eureka。
画面 10: 重复画面 1 的 PPT 内容，强调搭建配置中心的目标。
画面 11: 显示 config-server 启动后控制台的详细日志，确认服务已注册到 Eureka。
画面 12: 展示配置中心的配置文件内容，包括 server、spring.application.name、git 仓库地址和 Eureka 服务地址。
画面 13: 在码云仓库中编辑 user-dev.yml 文件，配置数据库连接信息和 Eureka 服务地址。
画面 14: 重复画面 12 的配置文件内容，强调配置文件的结构和关键参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5 的 pom.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.2.RELEASE</version>
        <relativePath/>
    </parent>

    <groupId>com.ithema.config</groupId>
    <artifactId>config-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>config-server</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

画面 6 的 application.yml:
```yaml
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/guheima/heima-config.git
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
```

画面 12 的配置文件内容：
```yaml
server:
  port: 12000
spring:
  application:
    name: config-server
  cloud:
    config:
      server:
        git:
          uri: https://gitee.com/guheima/heima-config.git
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
```

画面 13 的 user-dev.yml:
```yaml
uri: jdbc:mysql://localhost:3306/springcloud
username: root
password: root
application:
  name: user-service
  type: elasticsearch
  package: com.ithema.user
eureka:
  service-url:
    defaultZone: http://127.0.0.1:10086/eureka
  prefer-ip-address: true
  instance:
    ip-address: 127.0.0.1
  lease-renewal-interval-in-seconds: 5
  lease-expiration-duration-in-seconds: 10
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 10 的 PPT：
标题：12. 搭建配置中心微服务
目标：
- 创建 git 仓库：在码云上创建仓库
- 搭建配置中心 config-server：使用 spring boot 方式搭建和配置
标题：13. 获取配置中心配置
目标：改造用户微服务 user-service，配置文件信息不再由微服务项目提供，而是从配置中心获取

画面 1 的架构图：
- 用户（蓝色人形图标）指向“git 仓库（红色方框）”
- “git 仓库”指向“配置中心（紫色方框）”
- “配置中心”指向“服务 A（蓝色方框）”
- “配置中心”指向“服务 B（蓝色方框）”
- “配置中心”指向“服务 X（蓝色方框）”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
