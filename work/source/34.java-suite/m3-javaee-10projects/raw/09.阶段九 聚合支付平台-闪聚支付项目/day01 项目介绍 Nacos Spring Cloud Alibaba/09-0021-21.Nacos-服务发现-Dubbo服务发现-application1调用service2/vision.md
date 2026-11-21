# 画面线理解：21.Nacos-服务发现-Dubbo服务发现-application1调用service2

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\21.Nacos-服务发现-Dubbo服务发现-application1调用service2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:40, 00:56, 01:17, 01:49, 02:12, 02:46, 03:13, 03:50, 04:13, 04:22, 04:48, 05:07, 05:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:27:38

1) 这一组画面整体在讲如何在 Nacos 服务发现与配置管理环境下，通过 Dubbo 实现 application1 调用 service2 的远程服务调用。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程文档中“2.4.4 application1调用service2”章节，说明将 nacos-restful-consumer 作为 application1，实现对 service2 的调用。
画面2: 在 IntelliJ IDEA 中打开 nacos-restful-consumer 项目，展示 pom.xml 文件内容，其中包含 <dependency> 标签引用 service2-api。
画面3: 在 IDEA 中选中 nacos-restful-consumer 项目，展示其目录结构。
画面4: 在 IDEA 中展示 pom.xml 文件，其中包含 <dependency> 标签引用 spring-cloud-starter-dubbo。
画面5: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面6: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面7: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service1") 和 RestTemplate restTemplate = new RestTemplate();。
画面8: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面9: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面10: 在 IDEA 中展示 application.yml 文件，位于 resources 目录下。
画面11: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面12: 在 IDEA 中展示 RestConsumerController.java 文件，代码中定义了 @GetMapping(value = "/service2") 和 service2Api.dubboService();。
画面13: 展示课程文档中“2.4.4.2 实现远程调用”章节，通过架构图说明服务发现和负载均衡的问题。
画面14: 展示课程文档中“Nacos - 服务发现和配置管理”章节，列出教学目标。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
<dependency>
    <groupId>com.itheima.nacos</groupId>
    <artifactId>service2-api</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>

画面4:
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>

画面5:
@GetMapping(value = "/service1")
public String service1() {
    //远程调用
    RestTemplate restTemplate = new RestTemplate();
    //发现一个地址
    ServiceInstance serviceInstance = loadBalancerClient.choose(serviceId);
    //获取一个http://开头的地址，包括ip和端口
    URI uri = serviceInstance.getUri();
    String result = restTemplate.getForObject(uri + "/service", String.class);
    return "consumer invoke:" + result;
}

画面8:
@GetMapping(value = "/service2")
public String service2() {
    //远程调用service2
    service2Api.dubboService();
    return "consumer dubbo invoke " + providerResult;
}

画面10:
application.yml

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13:
架构图：
Service A → Service B 实例1
Service A → Service B 实例2
Service B 实例1 → 动态增加实例，增加 Service B 实例2
Service B 实例2 → 动态增加实例，增加 Service B 实例1

5) 不要评价画面美观，不要输出与课程无关的内容。
