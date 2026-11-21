# 画面线理解：17-线程隔离&服务降级

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\17-线程隔离&服务降级_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:26, 03:02, 04:24, 05:40, 07:04, 08:26, 10:56, 12:03, 13:34, 14:48, 15:49, 17:07, 18:01, 18:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:17:08

1) 这一组画面整体在讲如何在 Spring Cloud 项目中集成 Hystrix 熔断器，实现服务的线程隔离与降级处理。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 页面，标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。
画面 2: 展示 PPT 页面，详细解释 Hystrix 的线程隔离和降级机制。
画面 3: 展示 PPT 页面，标题为“8.3.2. 手动实践”，内容包括引入依赖和开启熔断的步骤。
画面 4: 展示 IDEA 编辑器界面，显示 consumer-demo 项目的目录结构和 ConsumerApplication.java 文件内容，其中包含 @EnableDiscoveryClient 和 @EnableCircuitBreaker 注解。
画面 5: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 6: 展示 IDEA 编辑器界面，显示运行日志，显示服务已启动。
画面 7: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 queryById 和 defaultFallback 方法。
画面 8: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 9: 展示 IDEA 编辑器界面，显示 application.yml 文件内容，其中包含 Hystrix 的配置。
画面 10: 展示 IDEA 编辑器界面，显示 UserController.java 文件内容，其中包含 queryById 方法。
画面 11: 展示 IDEA 编辑器界面，显示 UserController.java 文件内容，其中包含 queryById 方法。
画面 12: 展示课程 PPT 页面，标题为“17. 线程隔离&服务降级”，并列出“添加依赖”、“开启熔断”、“降级逻辑”、“修改超时配置”等要点。
画面 13: 展示 IDEA 编辑器界面，显示 ConsumerController.java 文件内容，其中包含 @HystrixCommand 注解和 queryById 方法。
画面 14: 展示课程 PPT 页面，标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-hystrix</artifactId>
</dependency>
```
```java
@SpringBootApplication
@EnableDiscoveryClient
@EnableCircuitBreaker
public class ConsumerApplication {
    // ...
}
```
```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
```
画面 4:
```java
package com.itheima.consumer;

import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.circuitbreaker.HystrixCommand;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ConsumerController {
    @Autowired
    private RestTemplate restTemplate;
    @Autowired
    private DiscoveryClient discoveryClient;
    @RequestMapping("/consumer")
    public String queryById(Long id) {
        String url = "http://user-service/user/" + id;
        return restTemplate.getForObject(url, String.class);
    }
}
```
画面 5:
```java
@HystrixCommand(fallbackMethod = "queryByIdFallback")
public String queryById(Long id) {
    String url = "http://user-service/user/" + id;
    return restTemplate.getForObject(url, String.class);
}
```
画面 7:
```java
public String queryByIdFallback(Long id) {
    log.error("查询用户信息失败，id: {}", id);
    return "对不起，网络太拥挤了！";
}
```
画面 9:
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    eureka:
      client:
        service-url:
          defaultZone: http://127.0.0.1:10006/eureka
        # 注册服务和拉取服务列表的时间间隔，默认30秒
        registry-fetch-interval-seconds: 10
    hystrix:
      command:
        default:
          execution:
            timeoutInMilliseconds: 2000
```
画面 10:
```java
package com.itheima.user.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;
    @RequestMapping("/user")
    public User queryById(Long id) {
        return userService.queryById(id);
    }
}
```
画面 11:
```java
package com.itheima.user.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;
    @RequestMapping("/user")
    public User queryById(Long id) {
        return userService.queryById(id);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。
画面 2: 标题为“17. 线程隔离&服务降级”，并列出“线程隔离”和“服务降级”的分析内容。
画面 3: 标题为“8.3.2. 手动实践”，并列出“引入依赖”和“开启熔断”的步骤。
画面 12: 标题为“17. 线程隔离&服务降级”，并列出“添加依赖”、“开启熔断”、“降级逻辑”、“修改超时配置”等要点。
画面 14: 标题为“16. 熔断器Hystrix简介”和“17. 线程隔离&服务降级”，并列出目标和分析内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
