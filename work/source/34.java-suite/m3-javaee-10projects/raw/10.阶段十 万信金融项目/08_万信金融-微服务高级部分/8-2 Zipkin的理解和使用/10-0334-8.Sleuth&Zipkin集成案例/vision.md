# 画面线理解：8.Sleuth&Zipkin集成案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\8.Sleuth&Zipkin集成案例_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:27, 02:30, 03:14, 04:04, 04:41, 05:58, 07:52, 08:59, 10:03, 11:04, 12:54, 14:03, 15:55, 16:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:08:46

1) 这一组画面整体在讲如何使用 Spring Cloud Sleuth 和 Zipkin 实现分布式服务链路追踪，并通过 Feign 实现服务间调用。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT，内容为“2.2 入门案例”下的“2.2.1 案例简介”，图示两个微服务（1、3）调用微服务B（2）。
画面2：在IDEA中打开项目结构，展示 `pom.xml` 文件，其中包含父依赖 `<parent>` 和 `<modules>` 配置。
画面3：在IDEA中打开 `discovery-server` 项目的 `application.properties` 文件，配置 Eureka 服务注册与发现。
画面4：在IDEA中打开 `service-a` 项目的 `pom.xml` 文件，配置 Spring Boot Web 和 Spring Cloud Sleuth 依赖。
画面5：展示课程PPT，内容为“3.2 Sleuth & Zipkin集成”下的“3.2.1 案例简介”，说明将使用 Eureka 作为注册中心、Feign 实现调用，并将日志上报至 Zipkin。
画面6：展示课程PPT，内容为“2.1 快速上手”，说明引入 Sleuth 依赖的步骤。
画面7：在IDEA中打开 `service-a` 项目的 `ServiceController.java` 文件，展示 `@RestController` 和 `@RequestMapping` 注解。
画面8：展示课程PPT，内容为“4. Feign代理”和“5. Controller类”，展示 Feign 客户端接口 `ServiceAgent` 和 Controller 类 `ServiceAController`。
画面9：在IDEA中打开 `service-b` 项目的 `ServiceController.java` 文件，展示 `@Autowired` 注解和 `serviceAgent.service()` 方法调用。
画面10：展示课程PPT，内容为“3.2 Sleuth & Zipkin集成”下的“3.2.2.2 启动类”和“4. Feign代理”，展示 `@SpringCloudApplication` 和 `@EnableFeignClients` 注解。
画面11：在IDEA中打开 `service-a` 项目的 `ServiceController.java` 文件，展示 `service1` 和 `service2` 两个方法。
画面12：在IDEA中打开 `service-b` 项目的 `application.properties` 文件，配置服务端口和 Eureka 服务地址。
画面13：在IDEA中打开 `service-a` 项目的 `application.properties` 文件，配置 `spring.sleuth.enabled=true`。
画面14：在IDEA中打开 `service-a` 项目的 `application.properties` 文件，配置 `spring.zipkin.base-url=http://localhost:9411`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>

<modules>
    <module>discovery-server</module>
    <module>service-a</module>
    <module>service-b</module>
</modules>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter</artifactId>
            <version>Greenwich.RELEASE</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面3：
```properties
spring.application.name=sleuth-discovery
server.port=58020
eureka.instance.hostname=localhost
eureka.client.register-with-eureka=false
eureka.client.fetch-registry=false
eureka.client.serviceUrl.defaultZone = http://${eureka.instance.hostname}:${server.port}/eureka/
```

画面4：
```xml
<parent>
    <artifactId>SleuthWithZipkinDemo</artifactId>
    <groupId>com.thema.sleuth</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>

<artifactId>service-a</artifactId>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
</dependencies>
```

画面6：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>

<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
</properties>
```

画面7：
```java
package com.thema.sleuth.servicea.controller;

import ...
@RestController
public class ServiceController {
    @RequestMapping("/hello")
    public String hello() {
        return "hello world";
    }
}
```

画面8：
```java
@RestController
public class ServiceAController {
    @Autowired
    private ServiceAgent serviceAgent;

    @GetMapping("/service1")
    public String service1(HttpServletResponse request) {
        String service = serviceAgent.service();
        return "service-a-service1" + "-->" + service;
    }
}
```

画面9：
```java
package com.thema.sleuth.serviceb.controller;

import ...
@RestController
public class ServiceController {
    @Autowired
    private ServiceAgent serviceAgent;

    public String service() {
        return serviceAgent.service();
    }
}
```

画面10：
```java
@SpringCloudApplication
@EnableFeignClients
public class ServiceBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(ServiceBootstrap.class, args);
    }
}
```

画面11：
```java
package com.thema.sleuth.servicea.controller;

import ...
@RestController
public class ServiceController {
    @Autowired
    private ServiceAgent serviceAgent;

    @GetMapping("/service1")
    public String service1() {
        String service = serviceAgent.service();
        return "service-a-service1" + "-->" + service;
    }

    @GetMapping("/service2")
    public String service2() {
        return "service-a-service2";
    }
}
```

画面12：
```properties
spring.application.name=sleuth-with-zipkin-service-b
server.port=58022
server.servlet.context-path=/service-b
eureka.client.serviceUrl.defaultZone = http://localhost:58020/eureka/
```

画面13：
```properties
spring.application.name=sleuth-with-zipkin-service-a
server.port=58021
server.servlet.context-path=/service-a
eureka.client.serviceUrl.defaultZone = http://localhost:58020/eureka/
# 开启Sleuth
spring.sleuth.enabled=true
```

画面14：
```properties
spring.application.name=sleuth-with-zipkin-service-a
server.port=58021
server.servlet.context-path=/service-a
eureka.client.serviceUrl.defaultZone = http://localhost:58020/eureka/
# 开启Sleuth
spring.sleuth.enabled=true
# 指定zipkin server的地址上报链路日志
spring.zipkin.base-url=http://localhost:9411
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题“2.2 入门案例”，子标题“2.2.1 案例简介”，图示：微服务A（包含服务1和3）通过调用链指向微服务B（服务2）。
画面5：PPT标题“3.2 Sleuth & Zipkin集成”，子标题“3.2.1 案例简介”，文字说明：采用Eureka作为服务注册与发现中心，采用Feign实现服务间调用，并将日志上报至Zipkin服务端，最终使用Zipkin图形化展示服务调用链路追踪情况。
画面6：PPT标题“2.1 快速上手”，文字说明：引入 Sleuth 依赖的步骤。
画面8：PPT标题“4. Feign代理”和“5. Controller类”，文字说明：展示 Feign 客户端接口 `ServiceAgent` 和 Controller 类 `ServiceAController`。
画面10：PPT标题“3.2 Sleuth & Zipkin集成”，子标题“3.2.2.2 启动类”和“4. Feign代理”，文字说明：展示 `@SpringCloudApplication` 和 `@EnableFeignClients` 注解。

5) 无。
