# 画面线理解：6.11 实时数据查询 - 主程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.11 实时数据查询 - 主程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:15, 00:37, 00:59, 01:05, 01:17, 01:19, 01:33, 02:03, 02:14, 02:29, 02:34, 02:39, 02:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:35:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置 Spring Boot 项目的 application-dev.yml 文件，包括服务器、数据库和监控相关配置，并编写启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 application-dev.yml 文件内容，配置 server、spring.application.name 和 profiles。
画面 2: 与画面 1 几乎相同，鼠标在 application-dev.yml 文件上。
画面 3: 鼠标选中 application-dev.yml 文件，显示其内容，包含 eureka 和 datasource 配置。
画面 4: 鼠标选中 application-dev.yml 文件，显示其内容，包含 datasource 配置。
画面 5: 鼠标选中 application-dev.yml 文件，显示其内容，包含 filter 配置。
画面 6: 鼠标在项目结构上右键，弹出菜单。
画面 7: 鼠标在项目结构上右键，弹出菜单。
画面 8: 鼠标在项目结构上右键，弹出菜单。
画面 9: 打开 MonitorApplication.java 文件，显示空的 main 方法。
画面 10: 在 MonitorApplication.java 文件中输入 @SpringBootApplication，IDE 提示相关注解。
画面 11: 在 MonitorApplication.java 文件中输入 @EnableDiscoveryClient，IDE 提示相关注解。
画面 12: 在 MonitorApplication.java 文件中输入 SpringApplication.run(MonitorApplication.class, args)，IDE 提示相关方法。
画面 13: 在 MonitorApplication.java 文件中输入 SpringApplication.run(MonitorApplication.class, args)，IDE 提示相关方法。
画面 14: 在 MonitorApplication.java 文件中输入 SpringApplication.run(MonitorApplication.class, args)，IDE 提示相关方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
server:
  tomcat:
    uri-encoding: UTF-8
    max-threads: 1000
    min-spare-threads: 30
    port: 8080
    connection-timeout: 10000ms
    servlet:
      context-path: /cold

spring:
  application:
    name: cold-monitor

  profiles:
    active: dev
# jackson
  jackson:
    time-zone: GMT+8
    date-format: yyyy-MM-dd HH:mm:ss
  servlet:
    multipart:

画面 3:
eureka:
  client:
    service-url: http://areka.itmaa.com:8001/areka

spring:
  datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      driver-class-name: com.mysql.jdbc.Driver
      url: jdbc:mysql://172.17.0.143:3006/cold?allowMultiQueries=true&useUnicode=true&characterEncoding=utf8
      username: cold
      password: cold123
      initial-size: 20
      max-active: 100
      min-idle: 10
      max-wait: 60000
      pool-prepared-statements: true
      max-pool-prepared-statement-per-connection-size: 20
      time-between-eviction-runs-millis: 60000
      min-evictable-idle-time-millis: 300000
      test-while-idle: true
      test-on-borrow: false
      test-on-return: false
      stat-view-servlet:
        enabled: true
        url-pattern: /druid/*

画面 5:
filter:
  stat:
    log-slow-sql: true
    slow-sql-millis: 1000
  wall:
    multi-statement-allow: true

画面 9:
package com.itheima;

public class MonitorApplication {
    public static void main(String[] args) {

    }
}

画面 10:
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

画面 12:
SpringApplication.run(MonitorApplication.class, args);

画面 14:
SpringApplication.run(MonitorApplication.class, args);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
