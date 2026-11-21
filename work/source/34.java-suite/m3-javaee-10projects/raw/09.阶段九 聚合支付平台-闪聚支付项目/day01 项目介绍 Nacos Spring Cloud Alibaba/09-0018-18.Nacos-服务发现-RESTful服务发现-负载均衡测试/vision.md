# 画面线理解：18.Nacos-服务发现-RESTful服务发现-负载均衡测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\18.Nacos-服务发现-RESTful服务发现-负载均衡测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 02:09, 03:28, 04:31, 05:15, 06:05, 07:07, 08:01, 08:35, 09:03, 10:01, 10:37, 11:21, 12:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:25:44

1) 这一组画面整体在讲 Spring Cloud 中 Ribbon 负载均衡组件的实现原理与使用方法，包括服务注册、配置、代码逻辑及负载均衡策略。

2) 按时间顺序列出每张画面的要点：
画面1：IDE启动界面，显示项目路径和当前打开的文件。
画面2：展示消费者端控制器代码，使用 RestTemplate 和 LoadBalancerClient 选择服务实例。
画面3：展示服务提供者端的 application.yml 配置文件，包含服务名和注册中心地址。
画面4：展示服务提供者端的 application.yml 配置文件，包含服务端口和注册中心地址。
画面5：服务提供者启动日志，显示服务已启动并监听端口 56010。
画面6：展示 Ribbon 的源码，重点是 choose 方法。
画面7：展示 Ribbon 的配置信息，包括服务列表和负载均衡策略。
画面8：展示 Ribbon 选择的服务实例信息，包括 IP 和端口。
画面9：展示 PPT 中关于 Ribbon 负载均衡策略的说明，包括 RoundRobinRule、RandomRule、AvailabilityFilteringRule 等。
画面10：展示消费者端的 application.yml 配置文件，包含服务名和注册中心地址。
画面11：展示启动配置界面，设置服务提供者端口为 56011。
画面12：展示 Ribbon 的源码，重点是 getServer 方法。
画面13：重复画面9的 PPT 内容，关于 Ribbon 负载均衡策略。
画面14：展示 PPT 中关于客户端负载均衡的架构图，说明 Nginx 与服务实例之间的关系。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2：
```java
@Autowired
LoadBalancerClient loadBalancerClient;

@GetMapping(value = "/service")
public String service() {
    //远程调用
    RestTemplate restTemplate = new RestTemplate();
    //发现一个地址
    ServiceInstance serviceInstance = loadBalancerClient.choose(serviceId);
    URL url = serviceInstance.getUri();
    String result = restTemplate.getForObject(url, String.class);
    return "consumer invoke:" + result;
}
```

画面3：
```yaml
spring:
  application:
    name: nacos-restful-provider #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面4：
```yaml
server:
  port: 56010

spring:
  application:
    name: nacos-restful-provider #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面6：
```java
public ServiceInstance choose(String serviceId, Object hint) {
    return this.choose(serviceId, hint);
}

public ServiceInstance choose(String serviceId, Object hint) {
    Server server = this.getServer(this.getLoadBalancer(serviceId, hint));
    return server == null ? null : new RibbonLoadBalancerClient().choose(server, this);
}
```

画面7：
```yaml
spring:
  application:
    name: nacos-restful-consumer #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面10：
```yaml
server:
  port: 56020

spring:
  application:
    name: nacos-restful-consumer #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面11：
```bash
-Dserver.port=56011
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面9：
标题：Ribbon核心组件IRule是负载均衡策略接口，它有如下实现，大家仅做了解：
- RoundRobinRule（默认）轮询，即按一定的顺序轮换获取实例的地址。
- RandomRule：随机，即随机的方式获取实例的地址。
- AvailabilityFilteringRule：会先过滤掉由于多次访问故障而处于断路器跳闸状态的服务，以及开发的连接数量超过阈值的服务，然后对剩余的服务列表按照轮询策略进行访问。
- WeightedResponseTimeRule：根据平均响应时间计算所有服务的权重，响应时间越快，服务权重越大，被选中的几率越高；刚启动时，如果统计信息不足，则使用RoundRobinRule策略，等统计信息足够时，会切换到WeightedResponseTimeRule。
- RetryRule：先按照RoundRobinRule的策略获取服务，如果获取服务失败，则在指定时间内进行重试，获取可用的服务。
- BestAvailableRule：会先过滤掉由于多次访问故障而处于断路器跳闸状态的服务，然后选择一个并发量最小的服务。
- ZoneAvoidanceRule：默认规则，复合判断server所在区域的性能和server的可用性选择服务。

画面14：
架构图：
- 客户端 → 负载均衡器 → Service 实例1
- 客户端 → 负载均衡器 → Service 实例2
- 服务注册表：
  - Service-A 192.168.25.3:8080
  - Service-B 192.168.25.4:8080
- 客户端 → 服务注册表 → 负载均衡器 → Service 实例1

5) 无
