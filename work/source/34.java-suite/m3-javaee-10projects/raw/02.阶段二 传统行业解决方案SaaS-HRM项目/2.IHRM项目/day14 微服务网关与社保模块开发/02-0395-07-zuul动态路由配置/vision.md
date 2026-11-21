# 画面线理解：07-zuul动态路由配置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\07-zuul动态路由配置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:53, 01:51, 03:55, 04:10, 04:31, 04:40, 05:07, 05:25, 05:59, 06:51, 07:28, 07:47, 07:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:13:56

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Cloud 项目中配置 Zuul 网关路由规则，并集成 Eureka 服务发现功能，实现微服务间的动态路由。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT页面，讲解Zuul路由规则，代码示例为在application.xml中配置路由规则。
画面2：在IDEA中展示Zuul网关的application.yml配置文件，包含server端口、spring配置、application名称及zuul路由规则。
画面3：展示一个架构图，说明Vue前端通过网关（Zuul, Spring Cloud Gateway）访问后端微服务，微服务注册到Eureka注册中心。
画面4：在IDEA中展示项目结构，选中了“ihrm_gate”模块，同时显示了application.yml文件。
画面5：在IDEA中展示“ihrm_company”服务的application.yml配置，包含Eureka客户端配置、服务端口、数据库连接等。
画面6：在IDEA中展示“ihrm_system”服务的application.yml配置，右键菜单显示了“Split Vertically”等选项。
画面7：在绘图工具中展示架构图，弹出窗口提示“1.所有的微服务都需要注册到注册中心”、“2.网关服务需要开启服务发现功能”、“3.微服务相关的配置文件，使用application.yml”。
画面8：在IDEA中展示项目结构，选中了“ihrm_system”模块。
画面9：在IDEA中展示“GateApplication.java”文件，包含@EnableZuulProxy和@EnableDiscoveryClient注解。
画面10：在IDEA中展示项目结构，选中了“ihrm_gate”模块。
画面11：在IDEA中展示“ihrm_company”服务的application.yml配置，正在编辑server端口。
画面12：在IDEA中展示“ihrm_gate”服务的application.yml配置，正在编辑路由规则，将serviceId改为“ihrm-company”。
画面13：在IDEA中展示“ihrm_gate”服务的运行日志，显示服务启动成功。
画面14：在IDEA中展示“ihrm_gate”服务的运行界面，准备运行服务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
zuul:
  routes:
    ihrm-company: # 这里是路由id，随意写
      path: /company/** # 这里是映射路径
      url: http://127.0.0.1:9001 # 映射到对应的实际url地址

画面2：
server:
  port: 9000
spring:
  application:
    name: ihrm-gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面4：
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm-gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面5：
#注册到eureka的服务地址
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:8088/eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm_company #指定服务名
#数据库配置
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf-8
  username: root
  password: 111111
  hikari:
    maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
#JPA

画面6：
#注册到eureka的服务地址
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:8088/eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm_system #指定服务名
#数据库配置
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf-8
  username: root
  password: 111111
  hikari:
    maximum-pool-size: 2
redis:
  host: 127.0.0.1
  port: 6379
#JPA

画面9：
package com.ihrm.gate;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
@SpringBootApplication
@EnableZuulProxy
@EnableDiscoveryClient
public class GateApplication {
    public static void main(String[] args) {
        SpringApplication.run(GateApplication.class, args);
    }
}

画面12：
#注册到eureka的服务地址
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:8088/eureka/
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务配置
server:
  port: 9000
spring:
  application:
    name: ihrm gate #指定服务名
zuul:
  routes:
    ihrm-company:
      path: /company/** #需要映射的路径地址
      url: http://127.0.0.1:9001 #映射路径对应的实际微服务的url路径
      stripPrefix: false #不删除请求的前缀

画面13：
2019-08-26 14:20:29.851 INFO 32836 --- [main] com.ihrm.gate.GateApplication: Refreshing Spring Boot context...
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c.c.DefaultListableBeanFactory: Overriding bean definition for bean 'BeanFactory'
2019-08-26 14:20:29.851 INFO 32836 --- [main] o.s.c
