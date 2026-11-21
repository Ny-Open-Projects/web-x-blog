# 画面线理解：6.服务调用链路追踪-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\6.服务调用链路追踪-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:37, 01:13, 01:33, 01:51, 01:58, 02:29, 02:56, 03:26, 03:52, 05:27, 07:21, 09:26, 10:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:07:04

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Cloud Sleuth 实现微服务间的链路追踪，并通过浏览器访问接口查看调用链路。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `package com.theima.msa.sleuthdemo1;` 和 `import ...`。
画面2：PPT页面，标题为“5. Controller类”，展示 `TestController` 类代码，其中包含 `@Autowired private RestTemplate restTemplate;`，`@GetMapping("service1")`，`log.info("sleuth1_service");`，`String sleuth1_service2 = restTemplate.getForObject("http://localhost:58011/sleuth1/service2", String.class);`，`return "sleuth1_service2";`。
画面3：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`。
画面4：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`，下方终端显示启动日志。
画面5：PPT页面，标题为“2.2.3 功能测试”，展示通过浏览器访问 `http://localhost:58011/sleuth1/service1` 得到的输出 `sleuth1_service1--->sleuth2_service1--->sleuth1_service2`，并说明日志格式。
画面6：浏览器页面，显示访问 `http://localhost:58011/sleuth1/service1` 后的输出 `sleuth1_service1--->sleuth2_service1--->sleuth1_service2`。
画面7：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service1")`，`public String node1(){ log.info("Sleuth1_Service1"); String sleuth1_service2 = restTemplate.getForObject("http://localhost:58012/sleuth2/service2", String.class); return "sleuth1_service2--->" + sleuth1_service2; }`。
画面8：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`。
画面9：IDEA界面，显示项目结构，当前打开的是 `TestController.java`，内容为 `@GetMapping("service2")`，`public String node2(){ log.info("sleuth1_service2"); return "sleuth1_service2"; }`，下方终端显示启动日志。
画面10：PPT页面，标题为“2.2.3 功能测试”，展示通过浏览器访问 `http://localhost:58021/service-a/service1` 得到的输出 `service-a-service1--->service-b-service1--->service-a-service2`，并说明日志格式。
画面11：PPT页面，标题为“2.2.1 案例简介”，展示创建两个微服务并通过 RestTemplate 实现调用的架构图，图中“前端请求”指向“微服务A”，“微服务A”指向“微服务B”，“微服务B”指向“微服务A”。
画面12：PPT页面，标题为“2.2.2 功能实现”，展示“2.2.1 微服务A”部分，内容为“1. 新建一个名为 SleuthDemo1 的 Maven 工程”和“2. 引入依赖”，并显示 `<parent>` 和 `<dependency>` 配置。
画面13：PPT页面，标题为“3. Zipkin”，展示日志格式说明，内容为“applicationName, traceId, spanId, export”。
画面14：PPT页面，标题为“3. Zipkin”，展示日志格式说明，内容为“applicationName, traceId, spanId, export”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public class TestController {
    @Autowired
    private RestTemplate restTemplate;
    @GetMapping("service1")
    public String node1(){
        log.info("sleuth1_service");
        String sleuth1_service2 = restTemplate.getForObject("http://localhost:58011/sleuth1/service2", String.class);
        return "sleuth1_service2";
    }
}
```
画面3：
```java
@GetMapping("service2")
public String node2(){
    log.info("sleuth1_service2");
    return "sleuth1_service2";
}
```
画面7：
```java
@GetMapping("service1")
public String node1(){
    log.info("Sleuth1_Service1");
    String sleuth1_service2 = restTemplate.getForObject("http://localhost:58012/sleuth2/service2", String.class);
    return "sleuth1_service2--->" + sleuth1_service2;
}
```
画面12：
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.0.RELEASE</version>
</parent>
```
画面12：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11：
标题：2.2.1 案例简介
架构图：
- “前端请求” → “微服务A”
- “微服务A” → “微服务B”
- “微服务B” → “微服务A”

画面12：
标题：2.2.2 功能实现
内容：
- 2.2.1 微服务A
  - 1. 新建一个名为 SleuthDemo1 的 Maven 工程
  - 2. 引入依赖

画面13：
标题：3. Zipkin
内容：
- 上图中的红框内容是在引入 Sleuth 之后多出来的日志，日志的格式为：`applicationName, traceId, spanId, export`
- applicationName：应用的名称，也就是 application.properties 中的 spring.application.name 属性的值。
- traceId：一个请求的 ID，用来标识一条请求链路。
- spanId：表示一个基本的工作单元，一个请求可以包含多个步骤，每个步骤都有自己的 spanId。
- export：布尔类型，表示是否要将该信息输出到类似 Zipkin 这样的运维服务进行收集和展示。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
