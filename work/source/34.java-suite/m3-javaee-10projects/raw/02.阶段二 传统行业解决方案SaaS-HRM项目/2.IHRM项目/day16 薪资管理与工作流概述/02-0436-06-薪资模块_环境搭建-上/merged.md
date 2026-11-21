# 06-薪资模块：环境搭建-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\06-薪资模块：环境搭建-上_【海量资源尽在 ubkz.com】.mp4
- 时长 3分31秒（音频 212s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们刚才呢一起对新资这个模块的需求呢做了一个分析同时呢我们也说过这几个模块的代码呢基本上都是大同小异的那我们接下来就来快速的把新资模块这个环境呢给它搭建出来那首先呢回到我们的idea创建一个工程就叫做IHR MercedesOK我这个名字呢从讲一场Ctrl C靠过这边了那找到复工程New一个modelNext
[00:33] 工程名称我直接拷过来了点击nextokfinish好了工程创建好了之后呢我们接下来呢就需要引入相应的这些坐标那坐标在今天的相应资料当中都给各位准备好了找到今天资料找到D16好了里面的资料分成了比较详细了我们现在用的是新资模块相同代码找到POM文件把POM文件里面的相应内容呢全部给它copy过来一大堆Ctrl C拿过来
[01:09] Ctrl A那接下来呢咱们这个里面需要很多的一些配置文件比如说它的启动类等等好了这些呢我就不再一行一行去写了写过很多次了同样在今天资料当中呢也给各位准备好了那一个启动类还有一个我们的配置Ctrl C把这两个类呢也拷过来好了先来看一下就是我们这两个类呢写到哪个包下了哎回到这边先去创建一个包Package那接下来找到资料
[01:43] 同样的把这两个Ctrl C 拷过来好了现在呢咱已经把相应的启动类还有我们的基本的配置呢准备好了那接下来Sprim Boot这个工程呢需要我们的application.yml同样的也copy过来Ctrl C拷过来好了拷过来之后呢简单的来看一下我们的应用名称哎就是薪资模块那这边呢有数据库联机好了那接下来呢这边有我们的服务的端口那注意啊我们这个端口起的是0
[02:15] 这边到07可能不对啊咱之前的这个端口到哪了呢刚到05咱们这边就是06OK好了那这样一来呢咱们这个基本的工程搭建第一个小步骤呢就已经搞定了其实就是创建了一个工程引入了相应的这些配置和配置类当然了还有一步就是在我们的网关部分需要添加相应的网关的支持
[02:43] 好了我这个找到网关找到里面的这个配置那我就写到上面了薪资薪资模块的路由那这边呢我们可以就直接从讲义上把这一大段呢咱们拷过来就行了Ctrl C拿到这边Ctrl V好了就是一个我们的薪资模块
[03:15] 要把它对齐OK好了那这样一来咱们对应的这个环境搭建呢其实就已经咱们把它建好了其实这一步呢没什么难度基本上全部都是一些公共的一些配置内容咱们之前也写过很多次了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务项目（含薪资、考勤、网关模块）的目录结构、配置文件（pom.xml、application.yml）及核心代码（启动类、配置类）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 IntelliJ IDEA 中项目结构，当前选中模块为 `ihrm_attendance`，目录包含 `ihrm_common`、`ihrm_company` 等子模块，以及 `pom.xml`。
画面2：与画面1相同，仅鼠标指针位置不同。
画面3：展示 Windows 资源管理器，路径为 `day16 > 03-资料`，文件夹内无内容，仅显示“正在处理它...”。
画面4：Notepad++ 编辑器中显示 `pom.xml` 文件内容，包含多个依赖项，如 `spring-cloud-starter-netflix-Eureka-client` 和 `spring-cloud-starter-openfeign`。
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
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
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
            <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
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
Eureka:
  client:
    Service-url: http://localhost:8888/Eureka/
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
Eureka:
  client:
    Service-url: http://localhost:8888/Eureka/
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
Eureka:
  client:
    Service-url

