# 画面线理解：17.Nacos-服务发现-RESTful服务发现-客户端负载均衡和服务端负载均衡

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\17.Nacos-服务发现-RESTful服务发现-客户端负载均衡和服务端负载均衡【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:42, 03:10, 03:19, 03:24, 03:33, 03:54, 04:55, 04:59, 05:19, 05:32, 05:36, 05:47, 05:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:25:07

1) 这一组画面整体在讲什么（一句话）：
讲解微服务架构中负载均衡的概念，区分服务器端负载均衡与客户端负载均衡，并通过代码演示如何使用 Spring Cloud 的 LoadBalancerClient 实现客户端负载均衡。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDE界面，展示 `RestConsumerController.java` 代码，其中调用 `loadBalancerClient.choose(serviceId)` 获取服务实例，然后使用 `restTemplate.getForObject` 发起 HTTP 请求。
画面2：PPT页面，标题为“服务器端负载均衡”，图示客户端 → 负载均衡器 → Service 实例1/2，说明负载均衡器从服务注册表中选择实例。
画面3：PPT页面，与画面2内容相同，图示客户端 → 负载均衡器 → Service 实例1/2。
画面4：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面5：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面6：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面7：IDE界面，与画面1内容相同，展示 `RestConsumerController.java` 代码，其中调用 `loadBalancerClient.choose(serviceId)` 获取服务实例，然后使用 `restTemplate.getForObject` 发起 HTTP 请求。
画面8：PPT页面，标题为“客户端服务负载均衡”，图示客户端 → Service 实例1/2，文字说明 LoadBalancerClient 是客户端负载均衡器，使用 Ribbon 实现，Ribbon 通过负载均衡策略选择实例。
画面9：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面10：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面11：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。
画面12：PPT页面，图示客户端 → Service 实例1/2，文字说明 LoadBalancerClient 是客户端负载均衡器，使用 Ribbon 实现，Ribbon 通过负载均衡策略选择实例。
画面13：IDE界面，与画面1内容相同，展示 `RestConsumerController.java` 代码，其中调用 `loadBalancerClient.choose(serviceId)` 获取服务实例，然后使用 `restTemplate.getForObject` 发起 HTTP 请求。
画面14：PPT页面，图示客户端 → 负载均衡器 → Service 实例1/2，文字说明负载均衡器根据配置好的“负载均衡算法”选择实例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码：
```java
@GetMapping(value = "/service1")
public String service1() {
    //远程调用
    RestTemplate restTemplate = new RestTemplate();
    //发现一个地址
    ServiceInstance serviceInstance = loadBalancerClient.choose(serviceId);
    //获取一个http://开头的地址，包括主机和端口
    URI uri = serviceInstance.getUri();
    String result = restTemplate.getForObject(uri + "/service", String.class);
    return "consumer invoke:" + result;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2标题：“服务器端负载均衡”
图示结构：
- 客户端 → 负载均衡器
- 负载均衡器 → Service 实例1
- 负载均衡器 → Service 实例2
- 服务注册表（包含 Service-A 和 Service-B 的 IP 和端口）指向负载均衡器。

画面8标题：“客户端服务负载均衡”
图示结构：
- 客户端 → Service 实例1
- 客户端 → Service 实例2
- 服务注册表（包含 Service-A 和 Service-B 的 IP 和端口）指向 Service 实例1 和 Service 实例2。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
