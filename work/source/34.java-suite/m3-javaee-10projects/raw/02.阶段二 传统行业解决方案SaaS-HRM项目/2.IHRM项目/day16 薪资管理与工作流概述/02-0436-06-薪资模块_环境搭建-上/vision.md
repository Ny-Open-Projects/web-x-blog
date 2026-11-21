# 画面线理解：06-薪资模块：环境搭建-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\06-薪资模块：环境搭建-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:37, 00:50, 01:05, 01:22, 01:37, 01:42, 02:00, 02:10, 02:21, 02:39, 02:50, 03:04, 03:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:46:21

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务项目（含薪资、考勤、网关模块）的目录结构、配置文件（pom.xml、application.yml）及核心代码（启动类、配置类）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 中项目结构，当前选中模块为 `ihrm_attendance`，目录包含 `ihrm_common`、`ihrm_company` 等子模块，以及 `pom.xml`。
画面2：与画面1相同，仅鼠标指针位置不同。
画面3：展示 Windows 资源管理器，路径为 `day16 > 03-资料`，文件夹内无内容，仅显示“正在处理它...”。
画面4：Notepad++ 编辑器中显示 `pom.xml` 文件内容，包含多个依赖项，如 `spring-cloud-starter-netflix-eureka-client` 和 `spring-cloud-starter-openfeign`。
画面5：Windows 资源管理器，路径为 `day16 > 03-资料`，显示文件夹内有 `application.yml`、`pom.xml`、`SalaryApplication.java`、`ShiroConfiguration.java`。
画面6：IntelliJ IDEA 中打开 `ihrm_salaries` 模块，显示 `pom.xml` 文件内容，包含 `spring-boot-starter-data-jpa`、`mysql-connector-java`、`ihrm_common` 等依赖。
画面7：Windows 资源管理器，路径为 `day16 > 03-资料`，显示文件夹内有 `application.yml`、`pom.xml`、`SalaryApplication.java`、`ShiroConfiguration.java`。
画面8：IntelliJ IDEA 中打开 `SalaryApplication.java`，显示 Spring Boot 启动类，包含 `@SpringBootApplication`、`@EnableFeignClients` 注解，以及一个 `@Bean` 方法。
画面9：IntelliJ IDEA 中打开 `application.yml` 文件，显示数据库配置（MySQL）、Redis、Eureka 服务注册中心、服务端口等配置。
画面10：IntelliJ IDEA 中打开 `application.yml` 文件，显示 `ihrm_attendance` 模块的配置，包含 `holidays` 字段。
画面11：IntelliJ IDEA 中打开 `application.yml` 文件，显示 `ihrm_salaries` 模块的配置。
画面12：IntelliJ IDEA 中打开 `application.yml` 文件，显示 `ihrm_gate` 模块的配置，包含 `routes` 路由规则。
画面13：PDF 文档，标题为“2.2.2 环境搭建”，内容包含“（2）创建启动类”，并显示了 `pom.xml` 中的依赖项。
画面14：IntelliJ IDEA 中打开 `application.yml` 文件，显示 `ihrm_gate` 模块的路由配置，包含 `ihrm-salaries` 和 `ihrm-company` 两个路由规则。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```xml
<dependency>
    <groupId>com.ihrm</groupId>
    <artifactId>ihrm_common_model</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

画面6：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>ihrm_parent</artifactId>
        <groupId>com.ihrm</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>ihrm_salaries</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>
    <name>ihrm_salaries</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.23</version>
        </dependency>
        <dependency>
            <groupId>com.ihrm</groupId>
            <artifactId>ihrm_common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>com.ihrm</groupId>
            <artifactId>ihrm_common_model</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
    </dependencies>
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

画面8：
```java
package com.ihrm.salarys;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;

@SpringBootApplication(scanBasePackages = "com.ihrm")
@EnableFeignClients
public class SalarysApplication {
    public static void main(String[] args) {
        SpringApplication.run(SalarysApplication.class, args);
    }

    @Bean
    public IdWorker idWorker() {
        return new IdWorker();
    }
}
```

画面9：
```yaml
show-sql: true
open-in-view: true
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
  username: root
  password: 111111
  hikari:
    maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
eureka:
  client:
    service-url: http://localhost:8888/eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
server:
  port: 9007
```

画面10：
```yaml
#配置文件
spring:
  application:
    name: ihrm-attendance #指定服务名
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
    hikari:
      maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
eureka:
  client:
    service-url: http://localhost:8888/eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
server:
  port: 9006
#配置假期
holidays: 20191001,20191002,20191003,20191001,20190927
```

画面11：
```yaml
#配置文件
spring:
  application:
    name: ihrm-salaries #指定服务名
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
    hikari:
      maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
eureka:
  client:
    service-url
