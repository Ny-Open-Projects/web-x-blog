# 画面线理解：2.11 搭建网关服务

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.11 搭建网关服务_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:49, 02:14, 02:28, 02:53, 03:19, 03:51, 04:07, 05:04, 05:15, 05:49, 06:13, 06:56, 07:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:57:51

1) 这一组画面整体在讲什么（一句话）：
使用 Spring Initializr 创建 Spring Cloud Gateway 项目，并配置其 Eureka 服务发现和核心服务端口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Spring Initializr 网站选择 Maven 项目，语言为 Java，Spring Boot 版本为 2.2.2，Group 为 com.example，Artifact 为 demo，选中 Gateway 和 Eureka Discovery Client 依赖。
画面2：在 Spring Initializr 页面，Package Name 设置为 com.ithema.cold.gateway，Packaging 为 Jar，Java 版本为 11，选中了 2 个依赖。
画面3：在 IntelliJ IDEA 中，通过“Import Project”对话框导入项目，路径为 D:\projects\cold-gateway。
画面4：在 IntelliJ IDEA 中，确认导入项目，选择“OK”完成导入。
画面5：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面6：在 IntelliJ IDEA 中，右键点击 application.properties 文件，选择“Add to Ignore List”。
画面7：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面8：在 IntelliJ IDEA 中，打开 application.yml 文件，准备进行配置。
画面9：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 eureka.client 配置。
画面10：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 spring.application.name 和 server.port 配置。
画面11：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 server.tomcat.accept-count 配置。
画面12：在 IntelliJ IDEA 中，编辑 application.yml 文件，添加 server.tomcat.max-threads 和 server.tomcat.min-spare-threads 配置。
画面13：在 IntelliJ IDEA 中，显示 GatewayApplication.java 文件，其中包含 SpringBootApplication 注解和 main 方法。
画面14：在 IntelliJ IDEA 中，显示 pom.xml 文件，其中包含 Spring Cloud Gateway 的依赖配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
无

画面2：
无

画面3：
无

画面4：
无

画面5：
package com.ithema.cold.gateway;
import org.springframework.boot.SpringApplication;
public class ColdGatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(ColdGatewayApplication.class, args);
    }
}

画面6：
无

画面7：
无

画面8：
无

画面9：
eureka:
  client:
    service-url:
      defaultZone: http://eureka.ithema.com:8001/eureka

画面10：
eureka:
  client:
    service-url:
      defaultZone: http://eureka.ithema.com:8001/eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    tomcat:

画面11：
eureka:
  client:
    service-url:
      defaultZone: http://eureka.ithema.com:8001/eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    tomcat:
      accept-count: 100

画面12：
eureka:
  client:
    service-url:
      defaultZone: http://eureka.ithema.com:8001/eureka
spring:
  application:
    name: cold-gateway
  server:
    port: 8080
    tomcat:
      accept-count: 100
      max-threads: 200
      min-spare-threads: 20

画面13：
无

画面14：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.2.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>

    <groupId>com.ithema</groupId>
    <artifactId>cold-gateway</artifactId>
    <version>2.0.1-SNAPSHOT</version>
    <name>cold-gateway</name>

</project>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
