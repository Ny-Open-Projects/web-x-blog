# 画面线理解：2.4 Springboot与Eureka集成

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.4 Springboot与Eureka集成_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:46, 02:35, 03:28, 04:08, 04:36, 05:33, 05:48, 06:20, 07:12, 07:48, 10:10, 10:31, 10:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:52:21

1) 这一组画面整体在讲什么（一句话）：
使用 Spring Cloud 创建并运行一个 Eureka 服务注册中心。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Eureka 服务注册中心的架构图，说明服务消费者通过 Eureka 获取服务列表，服务提供者向 Eureka 注册，服务消费者调用服务。
画面 2: 在 IDEA 中新建项目，选择 Maven 项目，准备创建 Spring Boot 项目。
画面 3: 在 Spring Initializr 网站上配置项目，选择 Java 语言、Spring Boot 2.2.2 版本，Group 为 com.itheima，Artifact 为 cold-eureka，点击 Generate。
画面 4: 在 IDEA 中打开项目，显示 pom.xml 文件内容，包含 Maven 配置和版本信息。
画面 5: 在 pom.xml 中添加 Spring Cloud Eureka Server 依赖。
画面 6: 显示 Spring Initializr 生成的项目结构和 EurekaApplication.java 文件内容。
画面 7: 在 IDEA 中打开 EurekaApplication.java 文件，准备编写代码。
画面 8: 在 EurekaApplication.java 中添加 Spring Boot 注解和主方法。
画面 9: 在 application.yml 文件中配置服务器端口和 Eureka 服务名称。
画面 10: 在 EurekaApplication.java 中添加 EurekaServer 注解。
画面 11: 在 application.yml 中配置 Eureka 服务名称为 cold-eureka-server。
画面 12: 运行 EurekaApplication，控制台显示服务启动日志。
画面 13: 在浏览器中访问 http://localhost:8001，显示 Eureka 服务注册页面。
画面 14: 在浏览器中访问 Eureka 服务注册页面，显示服务实例信息和服务器状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itheima</groupId>
    <artifactId>cold-eureka</artifactId>
    <version>1.0-SNAPSHOT</version>

</project>
```

画面 5:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
    <exclusions>
        <exclusion>
            <groupId>org.junit.vintage</groupId>
            <artifactId>junit-vintage-engine</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面 6:
```java
package com.itheima.cold.eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ColdEurekaApplication {
    public static void main(String[] args) {
        SpringApplication.run(ColdEurekaApplication.class, args);
    }
}
```

画面 9:
```yaml
server:
  port: 8001
spring:
  application:
    name: cold-eureka-server
```

画面 10:
```java
package com.itheima.cold.eureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class EurekaApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaApplication.class, args);
    }
}
```

画面 11:
```yaml
server:
  port: 8001
spring:
  application:
    name: cold-eureka-server
eureka:
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 架构图，服务注册中心指向服务消费者和提供者，服务消费者指向服务注册中心，服务提供者指向服务注册中心。
画面 14: 表格数据，显示服务实例信息和服务器状态，包括 Application、AMIs、Availability Zones、Status、Name、Value 等列。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
