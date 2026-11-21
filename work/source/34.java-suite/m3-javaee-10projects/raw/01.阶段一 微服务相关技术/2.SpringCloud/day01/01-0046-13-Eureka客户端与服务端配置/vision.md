# 画面线理解：13-Eureka客户端与服务端配置

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\13-Eureka客户端与服务端配置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:11, 03:59, 05:17, 06:32, 09:40, 11:14, 12:46, 13:53, 15:00, 15:48, 17:36, 18:48, 20:12, 20:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:14:15

1) 这一组画面整体在讲如何配置 Eureka Server 高可用集群以及 Eureka 客户端与服务端的注册与发现机制。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT，标题为“12. Eureka Server高可用配置”和“13. Eureka客户端与服务端配置”，说明目标是启动两个 Eureka Server 实例并配置客户端注册与发现。
画面2: IDE 中展示 consumer-demo 项目的 ConsumerController.java 代码，其中包含通过 EurekaClient 获取服务实例的逻辑，并在调试器中查看了服务实例信息。
画面3: IDE 中展示 user-service 项目的 application.yml 配置文件，其中配置了 service-url 为 http://127.0.0.1:10086/eureka，并在控制台查看了服务注册日志。
画面4: 展示课程 PPT，内容为服务注册的说明，包括服务提供者如何注册到 Eureka Server，以及如何配置 instance 以使用 IP 地址注册。
画面5: IDE 中展示 user-service 项目的 application.yml 配置文件，其中配置了 eureka.instance.prefer-ip-address: true，并在控制台查看了服务注册日志。
画面6: IDE 中展示 consumer-demo 项目的 application.yml 配置文件，其中配置了 eureka.client.service-url.defaultZone: http://127.0.0.1:10086/eureka，并在控制台查看了服务注册日志。
画面7: IDE 中展示 eureka-server 项目的 application.yml 配置文件，其中配置了 eureka.client.register-with-eureka: false 和 eureka.client.fetch-registry: false，并在控制台查看了服务注册日志。
画面8: IDE 中展示 eureka-server 项目的 application.yml 配置文件，其中配置了 eureka.client.register-with-eureka: false 和 eureka.client.fetch-registry: false，并在控制台查看了服务注册日志。
画面9: IDE 中展示 eureka-server 项目的 application.yml 配置文件，其中配置了 eureka.client.register-with-eureka: false 和 eureka.client.fetch-registry: false，并在控制台查看了服务注册日志。
画面10: IDE 中展示 user-service 项目的 application.yml 配置文件，其中配置了 eureka.instance.prefer-ip-address: true，并在控制台查看了服务注册日志。
画面11: IDE 中展示 eureka-server 项目的 application.yml 配置文件，其中配置了 eureka.client.register-with-eureka: false 和 eureka.client.fetch-registry: false，并在控制台查看了服务注册日志。
画面12: 展示课程 PPT，标题为“13. Eureka客户端与服务端配置”和“14. 负载均衡Ribbon简介”，说明目标是配置客户端注册与发现。
画面13: IDE 中展示 eureka-server 项目的 application.yml 配置文件，其中配置了 eureka.client.register-with-eureka: false 和 eureka.client.fetch-registry: false，并在控制台查看了服务注册日志。
画面14: 展示课程 PPT，内容为服务注册的说明，包括服务提供者如何注册到 Eureka Server，以及如何配置 instance 以使用 IP 地址注册。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2:
```java
public User queryById(@PathVariable long id) {
    String url = "http://localhost:8081/user/" + id;
    List<ServiceInstance> serviceInstances = discoveryClient.getInstances("user-service");
    url = "http://" + serviceInstance.getHost() + ":" + serviceInstance.getPort() + "/user/" + id;
    return restTemplate.getForObject(url, User.class);
}
```

画面3:
```yaml
eureka:
  service-url:
    defaultZone: http://127.0.0.1:10086/eureka
  instance:
    prefer-ip-address: true
    ip-address: 127.0.0.1
```

画面4:
```yaml
eureka:
  instance:
    ip-address: 127.0.0.1 # ip地址
    prefer-ip-address: true # 更倾向于使用ip，而不是hostname
```

画面5:
```yaml
eureka:
  instance:
    prefer-ip-address: true
    ip-address: 127.0.0.1
  lease-renewal-interval-in-seconds: 5
  lease-expiration-duration-in-seconds: 5
```

画面6:
```yaml
spring:
  application:
    name: consumer-demo
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    registry-fetch-interval-seconds: 10
```

画面7:
```yaml
server:
  port: 8086
spring:
  application:
    name: eureka-server
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
  server:
    eviction-interval-timer-in-ms: 60000
```

画面8:
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
  server:
    eviction-interval-timer-in-ms: 60000
```

画面9:
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
  server:
    eviction-interval-timer-in-ms: 60000
```

画面10:
```yaml
eureka:
  instance:
    prefer-ip-address: true
    ip-address: 127.0.0.1
  lease-renewal-interval-in-seconds: 5
  lease-expiration-duration-in-seconds: 5
```

画面11:
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
  server:
    eviction-interval-timer-in-ms: 60000
```

画面12:
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
```

画面13:
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://127.0.0.1:10086/eureka
    register-with-eureka: false
    fetch-registry: false
```

画面14:
```yaml
eureka:
  instance:
    ip-address: 127.0.0.1
    prefer-ip-address: true
  lease-renewal-interval-in-seconds: 5
  lease-expiration-duration-in-seconds: 5
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: 标题为“12. Eureka Server高可用配置”和“13. Eureka客户端与服务端配置”，目标是启动两个 Eureka Server 实例并配置客户端注册与发现。
画面4: 标题为“服务注册”，内容为服务提供者如何注册到 Eureka Server，以及如何配置 instance 以使用 IP 地址注册。
画面12: 标题为“13. Eureka客户端与服务端配置”和“14. 负载均衡Ribbon简介”，目标是配置客户端注册与发现。

5) 无。
