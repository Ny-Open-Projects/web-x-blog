# 画面线理解：12-Eureka Server高可用配置

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\12-Eureka Server高可用配置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:48, 03:22, 04:01, 06:14, 07:51, 08:27, 08:36, 08:59, 09:26, 09:47, 10:32, 10:55, 11:12, 13:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:13:26

1) 这一组画面整体在讲什么（一句话）：
演示如何配置和启动两个Eureka Server实例以实现高可用集群，并配置客户端服务注册到该集群。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT“6.4. Eureka详解”中的“6.4.1 基础架构”部分，介绍Eureka服务注册中心、服务提供者和服务消费者三个核心角色。
画面2：展示PPT中的架构图，说明客户端需要向每个Eureka Server注册，以及三个Eureka Server实例之间需要互相注册。
画面3：展示需要修改的Eureka Server配置文件application.yml内容，用于搭建两个Eureka Server集群。
画面4：展示IDEA中Run/Debug Configurations窗口，为EurekaServerApplication配置了两个运行实例（端口10086和10087）。
画面5：展示IDEA中Run/Debug Configurations窗口，为EurekaServerApplication配置了两个运行实例（端口10086和10087）。
画面6：展示IDEA中EurekaServerApplication10087的运行日志，显示服务启动过程。
画面7：展示IDEA中EurekaServerApplication10087的运行日志，显示服务启动过程。
画面8：展示IDEA中EurekaServerApplication10087的运行日志，显示服务启动过程。
画面9：展示IDEA中EurekaServerApplication10087的运行日志，显示服务启动过程。
画面10：展示浏览器访问Eureka Server 10086的页面，显示服务状态和实例信息。
画面11：展示IDEA中user-service的application.yml配置文件，设置服务名和Eureka Server地址。
画面12：展示浏览器访问Eureka Server 10087的页面，显示服务状态和实例信息。
画面13：展示IDEA中user-service的application.yml配置文件，设置服务名和Eureka Server地址。
画面14：展示课程PPT“12. Eureka Server高可用配置”和“13. Eureka客户端配置”部分，说明目标和分析。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
server:
  port: ${port:10086}
spring:
  application:
    name: eureka-server
  eureka:
    client:
      service-url:
        # eureka 服务地址，如果是集群的话，需要指定其它eureka地址
        defaultZone: ${defaultZone:http://127.0.0.1:10086/eureka}

画面11：
spring:
  application:
    name: user-service
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka

画面14：
spring:
  application:
    name: consumer-demo
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10086/eureka

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“6.4. Eureka详解”，子标题“6.4.1 基础架构”，内容包括三个核心角色：服务注册中心、服务提供者、服务消费者。
画面2：架构图，Client指向两个Eureka Server，两个Eureka Server之间有双向箭头。
画面14：PPT标题“12. Eureka Server高可用配置”，内容包括目标、分析、高可用配置；PPT标题“13. Eureka客户端配置”，内容包括目标、分析。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
