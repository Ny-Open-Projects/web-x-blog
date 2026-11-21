# 画面线理解：10-搭建eureka-server工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\10-搭建eureka-server工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 02:00, 02:24, 03:01, 03:48, 04:52, 05:46, 07:10, 07:27, 07:59, 08:23, 08:49, 09:18, 09:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:12:24

1) 这一组画面整体在讲什么（一句话）：
搭建并运行一个基于 Spring Cloud 的 Eureka 服务注册中心（eureka-server），并演示其服务注册与发现功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：PPT 页面，标题为“10. 搭建eureka-server工程”，下方有“目标”、“分析”、“小结”等部分。
- 重点文字：
  目标：添加Eureka对应依赖和编写引导类搭建eureka服务并可访问eureka服务界面
  分析：
  Eureka是服务注册中心，只做服务注册；自身并不提供服务也不消费服务。可以搭建web工程使用Eureka，可以使用Spring Boot方式搭建。
  小结：
  11. 服务注册与发现
  目标：将user-service的服务注册到eureka并在consumer-demo中可以根据服务名称调用

画面 2：
- 内容：IDEA 中的 Maven 依赖管理界面，正在添加 Spring Cloud 依赖。
- 重点文字：
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-dependencies</artifactId>
        <version>${spring-cloud.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

画面 3：
- 内容：IDEA 中的 pom.xml 文件，展示 Eureka Server 的依赖配置。
- 重点文字：
  <groupId>com.ithema</groupId>
  <version>1.0-SNAPSHOT</version>
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.0.RELEASE</version>
  </parent>
  <artifactId>eureka-server</artifactId>
  <dependencies>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
    </dependency>
  </dependencies>

画面 4：
- 内容：IDEA 中的 pom.xml 文件，展示 Spring Cloud 的版本管理配置。
- 重点文字：
  <properties>
    <java.version>1.8</java.version>
    <spring-cloud.version>Finchley.SR1</spring-cloud.version>
    <mybatis.version>1.3.2</mybatis.version>
    <mysql.version>8.0.11</mysql.version>
  </properties>

画面 5：
- 内容：IDEA 中的 EurekaServerApplication.java 启动类文件。
- 重点文字：
  package com.ithema;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.cloud.netflix.eureka.EnableEurekaServer;
  @EnableEurekaServer
  @SpringBootApplication
  public class EurekaServerApplication {
      public static void main(String[] args) {
          SpringApplication.run(EurekaServerApplication.class, args);
      }
  }

画面 6：
- 内容：IDEA 中的 application.yml 配置文件，设置 Eureka 服务端口和名称。
- 重点文字：
  server:
    port: 10086
  spring:
    application:
      name: eureka-server
  eureka:
    instance:
      environment: test
    client:
      register-with-eureka: false
      fetch-registry: false

画面 7：
- 内容：IDEA 项目结构视图，显示了多个模块，如 consumer-demo、user-service、eureka-server。
- 重点文字：
  项目结构中包含：
  - heima-springcloud
  - consumer-demo
  - eureka-server
  - user-service
  - http-demo

画面 8：
- 内容：IDEA 中的 EurekaServerApplication.java 文件，右键菜单弹出，选择“Run 'EurekaServerApplication'”。
- 重点文字：
  无代码或配置，仅是右键菜单操作。

画面 9：
- 内容：IDEA 控制台输出，显示 Eureka Server 成功启动。
- 重点文字：
  Application Context: initialization completed in 1078 ms
  ...
  Eureka Server started.
  ...
  http://127.0.0.1:10086/eureka/

画面 10：
- 内容：浏览器访问 Eureka Server 的管理页面，显示“System Status”和“DS Replicas”。
- 重点文字：
  System Status:
  Environment: test
  Data center: default
  Current time: 2019-06-14T13:47:34.747+08:00
  Uptime: 00:00
  Lease expiration enabled: false
  Renew threshold: 1
  Renew (last min): 0
  DS Replicas:
  127.0.0.1

画面 11：
- 内容：浏览器访问 Eureka Server 的管理页面，显示“Instance Info”。
- 重点文字：
  Instance Info:
  Name: 192.168.174.1
  Status: UP

画面 12：
- 内容：PPT 页面，标题为“10. 搭建eureka-server工程”，下方有“搭建步骤”。
- 重点文字：
  搭建步骤：
  1. 创建工程；
  2. 添加启动依赖；
  3. 编写启动引导类（添加Eureka的服务注解）和配置文件；
  4. 修改配置文件（端口、应用名称...）；
  5. 启动测试
  小结：
  - 启动器依赖
  - 配置文件

画面 13：
- 内容：IDEA 中的 application.yml 配置文件，展示 Eureka Server 的配置。
- 重点文字：
  <Xml version="1.0" encoding="UTF-8">
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.1.0.RELEASE</version>
    </parent>
    <artifactId>eureka-server</artifactId>
    <dependencies>
      <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
      </dependency>
    </dependencies>
  </project>

画面 14：
- 内容：PPT 页面，标题为“11. 服务注册与发现”，下方有“目标”。
- 重点文字：
  目标：将user-service的服务注册到eureka并在consumer-demo中可以根据服务名称调用
