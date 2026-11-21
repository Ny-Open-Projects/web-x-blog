# 画面线理解：08-搭建配置consumer-demo工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\08-搭建配置consumer-demo工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:37, 02:55, 03:31, 04:11, 04:34, 05:14, 05:37, 06:17, 06:39, 07:45, 08:14, 09:34, 11:03, 12:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:11:17

1) 这一组画面整体在讲如何搭建并实现一个使用 RestTemplate 调用远程服务的 Spring Cloud 消费者工程（consumer-demo），并引出后续将使用 Eureka 注册中心解决分布式服务面临的问题。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程目标与需求，说明要编写测试类使用 RestTemplate 调用 user-service 的数据。
画面2: 展示 consumer-demo 工程的 Maven 依赖配置，其中包含父工程、Spring Cloud 版本、Spring Boot 版本及当前模块的 artifactId。
画面3: 在 IDEA 中右键点击 consumer 模块，准备添加依赖。
画面4: 在 ConsumerApplication.java 中添加 @Bean 注解，用于创建 RestTemplate 实例。
画面5: 在 IDEA 中右键点击 consumer 模块，选择“Add Framework Support...”并选择 Web。
画面6: 在 ConsumerController.java 中定义一个 @RestController 和 @RequestMapping("/consumer") 的类。
画面7: 在 ConsumerController.java 中定义一个 queryById 方法。
画面8: 在 ConsumerController.java 中为 queryById 方法添加 @GetMapping("/id") 注解。
画面9: 在 ConsumerController.java 中为 queryById 方法添加 @Autowired 注解，用于注入 RestTemplate。
画面10: 在 ConsumerController.java 中为 queryById 方法添加 RestTemplate 类型的私有成员变量。
画面11: 在 ConsumerApplication.java 中定义一个 @Bean 方法，用于创建并返回 RestTemplate 实例。
画面12: 在 ConsumerController.java 中为 queryById 方法设置 URL 为 http://localhost:9091/user/{id}。
画面13: 展示 PPT 内容，介绍 Eureka 注册中心的作用，以及服务管理、状态监控、动态路由、负载均衡和配置统一等问题。
画面14: 展示课程目标与需求，说明要编写测试类使用 RestTemplate 调用 user-service 的数据，并列出后续要解决的服务管理、状态监控、动态路由、负载均衡、容灾问题和配置统一等问题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <artifactId>heima-springcloud</artifactId>
        <groupId>com.itheima</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>consumer-demo</artifactId>
</project>
```

画面4:
```java
package com.itheima.consumer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }
}
```

画面5:
```java
@RestController
@RequestMapping("/consumer")
public class ConsumerController {
}
```

画面6:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面7:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面8:
```java
@GetMapping("/id")
public User queryById(Long id) {
}
```

画面9:
```java
@Autowired
private RestTemplate restTemplate;
```

画面10:
```java
@Autowired
private RestTemplate restTemplate;
```

画面11:
```java
@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

画面12:
```java
@GetMapping("/id")
public User queryById(Long id) {
    String url = "http://localhost:9091/user/" + id;
    return restTemplate.getForObject(url, User.class);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13:
标题: 6. Eureka注册中心
子标题: 6.1. 认识Eureka
内容:
- user-service只有1台服务，不具备高可用性
- 即使user-service形成集群，consumer自己还不能实现负载均衡
- 其实上面的问题，概括一下就是分布式服务必然面临的问题：
  - 服务管理
    - 如何自动注册和发现
    - 如何实现状态监管
    - 如何实现动态路由
  - 服务如何实现负载均衡
  - 服务如何解决容灾问题
  - 服务如何实现统一配置
- 以上的问题，都将在SpringCloud中得到答案。

5) 不要评价画面美观，不要输出与课程无关的内容。
