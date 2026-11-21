# 6.11 实时数据查询 - 主程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.11 实时数据查询 - 主程序_【海量资源尽在 666java.com】.mp4
- 时长 2分55秒（音频 175s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 根据我们这个代码的这个结构呢我们来开发我们这个CodeMonitor里边的主要的类主要的一些方法那首先的话我们看我们这个工程的这个application-yaml文件和application-dv的yaml文件这两个文件和其他的工程里边的这种yaml文件比较类似它使用了server-Tomcat然后端口以及我们的context-path也就是说我们URL的一个路径然后呢包括我们当前这个工程CodeMonitor它的一个名字在这里边都会
[00:30] 写上然后另外一个就是我们当前使用哪一个profile也就是说我们使用的是application-dv的-dv这个样本文件里边一个是说我们的这种Urequra服务制作中心它的一个地址另外一个是我们的Spring的一个就是GTBC的databasedatasource到底是配置的是什么样的它使用的是我们GTBC的mycircle然后连接用户名密码
[00:59] 这是我们的配置还有一些其他的配置属性这些和我们其他工程里边的查询MySQL数据库都比较类似在这里不得详细的讲解下面我们来开发我们的主程序那么这个主程序我们叫做MonitorApplication我们在这可以开发一个主要的我们先加上了一个package就是包名com.rtk码对吧com.rtk码在这里的时候
[01:30] 我们创建我们的Main函数这个Main函数叫MonitorApplicationOK这个MonitorApplication它是我们的主函数是一个Spring Boot的一个程序那么我们需要在这里边添加我们的Main函数然后呢我们再添加我们的这个注解这个注解的话一个是Spring Boot Application
[02:08] 这是一个注解那么另外一个的话是我们叫EnableDiscoveryPlant这个是我们把我们当前这个程序连把它注册到我们的Ulker服务注册中心里面去那下一步的话我们要添加在main函数里面添加我们的Spring Boot的一个程序程序体Spring Boot Application然后Spring Boot Application点Run在Run的话就是Run这个
[02:40] monitor当前类obligation.class然后args这样的时候我们当前的主程序其实就已经添加完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置 Spring Boot 项目的 application-dev.yml 文件，包括服务器、数据库和监控相关配置，并编写启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 application-dev.yml 文件内容，配置 server、spring.application.name 和 profiles。
画面 2: 与画面 1 几乎相同，鼠标在 application-dev.yml 文件上。
画面 3: 鼠标选中 application-dev.yml 文件，显示其内容，包含 Eureka 和 datasource 配置。
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
  Tomcat:
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
Eureka:
  client:
    Service-url: http://areka.itmaa.com:8001/areka

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

