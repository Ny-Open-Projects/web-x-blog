# 画面线理解：9.Sleuth&Zipkin集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\9.Sleuth&Zipkin集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 03:04, 04:23, 04:53, 05:29, 06:49, 07:24, 07:49, 09:45, 10:22, 10:44, 11:37, 12:07, 12:48, 14:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:09:47

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Cloud Sleuth 结合 Zipkin 实现微服务调用链追踪，并展示在 Zipkin 界面中查看追踪数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- PPT标题：3.2.1 案例简介
- 内容：我们对上面的Sleuth入门案例进行改造，采用Eureka作为服务注册与发现中心，采用Feign实现服务间调用，并将追踪日志上报至Zipkin服务端，最终使用Zipkin图形化展示服务调用链追踪情况。

画面2：
- 内容：启动Zipkin，启动注册中心和两个微服务，然后通过浏览器访问 http://localhost:58021/service-a/service1，得到以下输出：
  service-a-service1---->service-b-service---->service-a-service2
- 内容：查看控制台日志输出，如下图所示：
  Console -+ ServiceBootstrap
  42.830 INFO [sleuth-with-zipkin-service-a, ddbbcc256a353723, ddbbcc256a353723, true]
  42.830 INFO [sleuth-with-zipkin-service-a, ddbbcc256a353723, ddbbcc256a353723, true]
- 内容：使用浏览器访问 http://localhost:9411，点击查找，可以看到刚刚测试产生的服务调用链路信息。

画面3：
- IDE界面：IntelliJ IDEA，打开 service-b 的 application.properties 文件。
- 代码内容：
  spring.sleuth.enabled=true
  #指定zipkin server地址，上报跟踪日志
  spring.zipkin.base-url=http://localhost:9411
  #采样率，取值范围0-1
  spring.sleuth.sampler.probability=1

画面4：
- PPT标题：2.2 入门案例
- 子标题：2.2.1 案例简介
- 内容：创建两个微服务，并通过RestTemplate实现服务之间的调用，形成如下调用链：
  - 流程图：前端请求 → 服务A（节点1）→ 服务B（节点2）→ 服务A（节点3）
- 子标题：2.2.2 功能实现
- 子标题：2.2.1 微服务A
- 内容：1. 新建一个名字为SleuthDemo的Maven工程
- 内容：2. 引入依赖
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
  </parent>

画面5：
- PPT标题：3.3.3 功能测试
- 内容：测试细节：在application.properties中设置采样率
  #采样率，取值范围0-1
  spring.sleuth.sampler.probability=1
- 内容：追踪日志由Sleuth产生，日志的采集由Zipkin负责，采集多少数据可以通过采样率（取值范围0-1）进行控制。假设一次请求包含四次微服务调用，如果采样率设置为1，则所有调用产生的日志进行采集；如果采样率设置为0.5，则只对一半调用产生的日志进行采集。采样率越高，数据越丰富，但是采集压力和负担也越大，所以在实际开发中，采样率并不是越高越好，视情况而定。

画面6：
- PPT标题：3.2.2 功能实现
- 子标题：3.2.2.1 工程实现
- 内容：由于涉及到服务注册中心、服务A、服务B三个工程，因此可考虑使用maven工程来统一依赖管理。
- 内容：在父工程pom中引入spring boot及spring cloud依赖：

画面7：
- 浏览器地址栏：http://localhost:9411/zipkin/
- 页面内容：Zipkin - Investigate system behavior

画面8：
- Zipkin 界面：显示追踪详情
- 标题：sleuth-with-zipkin-service-b.get/service: 937.737ms
- 表格1：服务调用时间
  Date Time | Relative Time | Annotation | Address
  2019/11/7 下午10:26:43 | 584.500ms | Client Start | sleuth-with-zipkin-service-a
  2019/11/7 下午10:26:43 | 742.859ms | Server Start | sleuth-with-zipkin-service-b
  2019/11/7 下午10:26:44 | 1.533s | Client Finish | sleuth-with-zipkin-service-b
- 表格2：请求参数
  Key | Value
  http.method | GET
  http.path | /service-b/service
  mvc.controller.class | ServiceBController
  mvc.controller.method | service
  Client Address | 127.0.0.1:53992

画面9：
- IDE界面：IntelliJ IDEA，打开 service-b 的 application.properties 文件。
- 代码内容：
  eureka.client.serviceUrl.defaultZone = http://localhost:58020/eureka/
  #开启Sleuth
  spring.sleuth.enabled=true
  #指定zipkin server地址，上报跟踪日志
  spring.zipkin.base-url=http://localhost:9411
  #采样率，取值范围0-1
  spring.sleuth.sampler.probability=1

画面10：
- IDE界面：IntelliJ IDEA，打开 service-b 的 ServiceBController.java 文件。
- 代码内容：
  package com.libema.sleuth.serviceb.controller;
  import ...
  @RestController
  public class ServiceBController {
    @Autowired
    private ServiceAgent serviceAgent;
    @GetMapping("service")
    public String service() {
      String service = serviceAgent.service();
      return "service-b-service---->service2";
    }
  }

画面11：
- 浏览器地址栏：http://localhost:58021/service-a/service1
- 页面内容：service-a-service1---->service-b-service---->service-a-service2

画面12：
- Zipkin 界面：显示追踪详情
- 标题：sleuth-with-zipkin-service-b.get/service: 955.222ms
- 表格1：服务调用时间
  Date Time | Relative Time | Annotation | Address
  2019/11/7 下午10:32:32 | 2.424ms | Client Start | sleuth-with-zipkin-service-a
  2019/11/7 下午10:32:32 | 142.177ms | Server Start | sleuth-with-zipkin-service-b
  2019/11/7 下午10:32:33 | 957.646ms | Client Finish | sleuth-with-zipkin-service-a
- 表格2：请求参数
  Key | Value
  http.method | GET
  http.path | /service-b/service
  mvc.controller.class | ServiceBController
  mvc.controller.method | service
  Client Address | 127.0.0.1:53992

画面13：
- Zipkin 界面：显示追踪详情
- 标题：sleuth-with-zipkin-service-b.get/service: 955.222ms
- 表格1：服务调用时间
  Date Time | Relative Time | Annotation | Address
  2019/11/7 下午10:32:32 | 2.424ms | Client Start | sleuth-with-zipkin-service-a
  2019/11/7 下午10:32:32 | 142.177ms | Server Start | sleuth-with-zipkin-service-b
  2019/11/7 下午10:32:33 | 957.646ms | Client Finish | sleuth-with-zipkin-service-a
- 表格2：请求参数
  Key | Value
  http.method | GET
  http.path | /service-b/service
  mvc.controller.class | ServiceBController
  mvc.controller.method | service
  Client Address | 127.0.0.1:53992

画面14：
- Zipkin 界面：显示追踪详情
- 标题：sleuth-with-zipkin-service-b.get/service: 955.222ms
- 表格1：服务调用时间
  Date Time | Relative Time | Annotation
