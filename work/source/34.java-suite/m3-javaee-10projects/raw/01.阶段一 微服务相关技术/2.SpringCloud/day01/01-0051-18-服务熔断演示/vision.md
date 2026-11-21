# 画面线理解：18-服务熔断演示

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\18-服务熔断演示_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:16, 04:31, 05:06, 05:20, 06:13, 06:26, 06:53, 07:16, 08:32, 10:02, 11:13, 11:35, 11:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:17:58

1) 这一组画面整体在讲什么（一句话）：
讲解 Hystrix 服务熔断机制的原理和如何在 Spring Cloud 项目中通过配置文件进行实战操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录结构，当前位于“8.4. 服务熔断”章节，具体为“8.4.1. 熔断原理”。
画面 2: 展示 Hystrix 熔断器的“Closed”、“Open”状态转换图，图中包含“call / raise circuit open”、“fail [threshold reached]”、“reset timeout”等转换条件。
画面 3: 展示 Hystrix 熔断器的“Half Open”状态，图中显示从“Open”状态通过“reset timeout”后进入“Half Open”，并有“success”和“fail”流向。
画面 4: 展示 Hystrix 熔断器的三种状态（Closed、Open、Half Open）的文字说明，并进入“8.4.2. 动手实践”部分。
画面 5: 展示“8.4.2. 动手实践”部分，说明需要修改的文件路径：`consumer-demo/src/main/java/com/heima/consumer/controller/ConsumerController.java`。
画面 6: 展示在浏览器中访问 `localhost:8080/consumer/1` 和 `localhost:8080/consumer/2` 的结果，其中 `consumer/1` 返回“默认提示：对不起，网络太拥挤了！”，说明熔断器已触发。
画面 7: 展示在 IntelliJ IDEA 中打开 `ConsumerController.java` 文件，代码中包含 `@HystrixCommand` 注解和 `defaultFallback` 方法。
画面 8: 展示在 IntelliJ IDEA 中修改 `ConsumerController.java` 文件，添加 `@HystrixCommand` 注解，并在 `queryById` 方法中抛出异常。
画面 9: 展示在 IntelliJ IDEA 中修改 `ConsumerController.java` 文件，添加 `@HystrixCommand` 注解，并在 `queryById` 方法中添加 `@DefaultProperties` 注解和 `defaultFallback` 方法。
画面 10: 展示在浏览器中访问 `localhost:8080/consumer/8` 的结果，返回用户信息 JSON 数据。
画面 11: 展示在 IntelliJ IDEA 中打开 `application.yml` 文件，准备修改 Hystrix 配置。
画面 12: 展示在 IntelliJ IDEA 中修改 `application.yml` 文件，添加 Hystrix 配置项，并在控制台中查看应用启动日志。
画面 13: 展示 Typora 中的“18. 服务熔断演示”页面，包含 Hystrix 熔断器状态转换图，图中包含“关闭”、“打开”、“半开”状态及转换条件。
画面 14: 展示 Typora 中的“18. 服务熔断演示”页面，展示 Hystrix 熔断器的“Half Open”状态及配置参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 7 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 8 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 9 代码：
```java
@HystrixCommand
public String queryById(@PathVariable Long id) {
    if (id == 1) {
        throw new RuntimeException("太忙了");
    }
    String url = "http://user-service/user/" + id;
    String user = restTemplate.getForObject(url, String.class);
    return user;
}
```
画面 11 配置：
```yaml
spring:
  application:
    name: consumer-demo
  cloud:
    eureka:
      client:
        service-url:
          defaultZone: http://127.0.0.1:10000/eureka
      registry-fetch-interval-seconds: 10
hystrix:
  command:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 2000
```
画面 12 配置：
```yaml
hystrix:
  command:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 2000
  circuitBreaker:
    errorThresholdPercentage: 50 # 制定熔断阈值比例的配置， 默认值50%
    sleepWindowInMilliseconds: 10000 # 熔断后休眠时长， 默认值5秒
    requestVolumeThreshold: 10 # 熔断触发最小请求数， 默认值20
```
画面 13 配置：
```yaml
hystrix:
  command:
    default:
      execution:
        isolation:
          thread:
            timeoutInMilliseconds: 2000
  circuitBreaker:
    errorThresholdPercentage: 50 # 制定熔断阈值比例的配置， 默认值50%
    sleepWindowInMilliseconds: 10000 # 熔断后休眠时长， 默认值5秒
    requestVolumeThreshold: 10 # 熔断触发最小请求数， 默认值20
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图标题为“Circuit Breaker”，包含三个状态：“Closed”、“Open”、“Half Open”。从“Closed”状态出发，若“fail [threshold reached]”则指向“Open”状态；从“Open”状态出发，若“reset timeout”则指向“Closed”状态；从“Open”状态出发，若“fail”则指向“Half Open”状态；从“Half Open”状态出发，若“success”则指向“Closed”状态；从“Half Open”状态出发，若“fail”则指向“Open”状态。
画面 3: 架构图标题为“Circuit Breaker”，包含三个状态：“Closed”、“Open”、“Half Open”。从“Closed”状态出发，若“fail [under threshold]”则指向“Closed”状态；从“Closed”状态出发，若“fail [threshold reached]”则指向“Open”状态；从“Open”状态出发，若“reset timeout”则指向“Closed”状态；从“Open”状态出发，若“fail”则指向“Half Open”状态；从“Half Open”状态出发，若“success”则指向“Closed”状态；从“Half Open”状态出发，若“fail”则指向“Open”状态。
画面 13: 架构图标题为“Circuit Breaker”，包含三个状态：“关闭”、“打开”、“半开”。从“关闭”状态出发，若“fail [threshold reached]”则指向“打开”状态；从“打开”状态出发，若“reset timeout”则指向“关闭”状态；从“打开”状态出发，若“fail”则指向“半开”状态；从“半开”状态出发，若“success”则指向“关闭”状态；从“半开”状态出发，若“fail”则指向“打开”状态。
画面 14: 架构图标题为“Circuit Breaker”，包含三个状态：“关闭”、“打开”、“半开”。从“关闭”状态出发，若“fail [threshold reached]”则指向“打开”状态；从“打开”状态出发，若“reset timeout”则指向“关闭”状态；从“打开”状态出发，若“fail”则指向“半开”状态；从“半开”状态出发，若“success”则指向“关闭”状态；从“半开”状态出发，若“fail”则指向“打开”状态。

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
