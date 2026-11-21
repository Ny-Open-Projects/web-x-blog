# 画面线理解：02-Feign负载均衡及熔断（了解）

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\02-Feign负载均衡及熔断（了解）_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 02:55, 04:16, 05:44, 06:53, 08:23, 09:53, 11:32, 12:47, 14:16, 15:05, 15:49, 16:53, 17:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:20:56

1) 这一组画面整体在讲如何在 Spring Cloud 中使用 Feign 客户端配置 Ribbon 负载均衡、Hystrix 熔断以及日志级别，并通过代码和配置文件进行演示。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Feign 客户端接口定义，用于调用 user-service 服务，并介绍目标是配置 Ribbon 和 Hystrix 的配置。
画面2: 展示 application.yml 中的 client、ribbon 和 hystrix 配置，包括服务发现地址、超时时间、熔断阈值等。
画面3: 展示 Feign 内置 Ribbon 的超时配置说明，并提示修改 application.yml 文件。
画面4: 展示 UserClient 接口定义，包含注解 @FeignClient 和 @GetMapping。
画面5: 展示 UserClientFallback 类的实现，用于处理服务调用失败时的降级逻辑。
画面6: 展示浏览器访问 localhost:8080/c/6，返回用户信息 JSON 数据。
画面7: 展示 application.yml 中 hystrix 配置项，包括 enabled、compression、request、response 等。
画面8: 展示如何通过修改 application.yml 设置日志级别，并创建 FeignConfig 类来定义日志级别。
画面9: 展示在 IntelliJ IDEA 中右键点击目录，选择新建文件或类。
画面10: 展示 FeignConfig 类的代码，用于配置 Feign 客户端的 fallback 类。
画面11: 展示 UserClient 接口定义，包含 @FeignClient 注解和 @GetMapping 注解。
画面12: 展示 UserClient 的调用日志，显示服务调用成功和失败的详细信息。
画面13: 展示 UserController 类的代码，包含 @RestController 注解和 queryById 方法。
画面14: 展示最终的配置文件内容，包括 ribbon、hystrix、feign、logging 等配置项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2:
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10000/eureka
    # 服务注册中心的刷新间隔，默认30秒
    registry-fetch-interval-seconds: 10
  hystrix:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 2000
    circuitBreaker:
      errorThresholdPercentage: 50 # 装载阈值，超过50%会触发熔断
      sleepWindowInMilliseconds: 10000 # 熔断后等待时间，单位毫秒
      requestVolumeThreshold: 10 # 熔断触发的请求数量，单位请求
    ribbon:
      ConnectTimeout: 1000 # 连接超时时间
      ReadTimeout: 2000 # 读取超时时间
      MaxAutoRetries: 0 # 最大重试次数
      MaxAutoRetriesNextServer: 0 # 重试多少次服务
      OkToRetryOnAllOperations: false # 是否对所有的请求方式重试
```

画面3:
```yaml
ribbon:
  ConnectTimeout: 1000 # 连接超时时间
  ReadTimeout: 2000 # 读取超时时间
  MaxAutoRetries: 0 # 最大重试次数
  MaxAutoRetriesNextServer: 0 # 重试多少次服务
  OkToRetryOnAllOperations: false # 是否对所有的请求方式重试
```

画面7:
```yaml
hystrix:
  enabled: true # 开启hystrix熔断功能
  compression:
    request:
      enabled: true # 开启请求压缩
      mime-types: text/html,application/xml,application/json # 设置压缩的响应类型
      min-request-size: 2048 # 设置触发压缩的最小大小
    response:
      enabled: true # 开启响应压缩
```

画面8:
```java
package com.ithema.consumer.config;

import feign.Logger;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FeignConfig {

    @Bean
    Logger.Level feignLoggerLevel() {
        // 记录所有请求和响应，包括头信息、请求体、元数据
        return Logger.Level.FULL;
    }
}
```

画面10:
```java
package com.ithema.consumer.client;

import com.ithema.consumer.client.fallback.UserClientFallback;
import com.ithema.consumer.pojo.User;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(value = "user-service", fallback = UserClientFallback.class, configuration = FeignConfig.class)
public interface UserClient {

    @GetMapping("/user/{id}")
    User queryById(@PathVariable Long id);
}
```

画面13:
```java
package com.ithema.user.controller;

import com.ithema.user.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/{id}")
    public User queryById(@PathVariable Long id) {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return userService.queryById(id);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: PPT 标题为“2. Feign负载均衡及熔断”，目标是配置 Feign 内置 Ribbon 和 Hystrix 的配置。
画面3: PPT 标题为“1.4. Hystrix支持(了解)”，内容包括 Feign 内置 Ribbon 的超时配置说明。
画面8: PPT 标题为“2.2. 日志级别”，内容包括如何通过修改 application.yml 设置日志级别。
画面14: PPT 标题为“小结”，内容包括在消费者工程 consumer-demo 中的配置文件内容。

5) 无。
