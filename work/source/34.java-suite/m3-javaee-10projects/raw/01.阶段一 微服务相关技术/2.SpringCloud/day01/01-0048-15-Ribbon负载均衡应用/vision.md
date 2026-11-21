# 画面线理解：15-Ribbon负载均衡应用

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\15-Ribbon负载均衡应用_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 03:31, 04:46, 05:16, 06:36, 07:45, 08:09, 08:42, 09:06, 09:38, 10:13, 10:42, 11:12, 11:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:15:36

1) 这一组画面整体在讲如何使用 Spring Cloud Ribbon 实现服务的负载均衡，通过修改 ConsumerController 中的 RestTemplate 调用方式，使其能自动从 Eureka 服务列表中选择一个可用实例进行请求。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 consumer-demo 项目的结构，重点是 ConsumerController.java 文件，其中包含使用 RestTemplate 和 DiscoveryClient 的代码，用于根据用户 ID 获取用户信息。
画面2: 展示了课程 PPT 的“15. Ribbon负载均衡应用”章节，列出了实现步骤：启动多个 user-service 实例、修改 RestTemplate 实例化方法、修改 ConsumerController。
画面3: 展示了 user-service 的 application.yml 配置文件，其中配置了服务名、端口、数据库连接、Eureka 服务注册地址等。
画面4: 展示了 ConsumerController.java 文件，代码中注释了“//代码中url中的user-service”并显示了硬编码的 URL。
画面5: 展示了 ConsumerController.java 文件，代码中使用了 discoveryClient 获取服务实例，但 URL 仍为硬编码。
画面6: 展示了 consumer-demo 项目的 pom.xml 文件，其中包含了 spring-cloud-starter-netflix-eureka-client 依赖。
画面7: 展示了 Maven 仓库中 spring-cloud-commons-2.1.1.RELEASE.jar 的内容，显示了其内部的 META-INF 和 spring-configuration 目录。
画面8: 展示了 spring-cloud-commons 源码中的 LoadBalancerAutoConfiguration.java 文件，其中包含 @Configuration 和 @ConditionalOnMissingBean 注解。
画面9: 展示了 LoadBalancerAutoConfiguration.java 文件，代码中定义了 loadBalancedRestTemplateInitializerDeprecated 方法。
画面10: 展示了 RibbonLoadBalancerClient.java 文件，其中包含 execute 方法，用于选择服务实例并执行请求。
画面11: 展示了调试界面，显示了 RibbonLoadBalancerClient 的 execute 方法执行过程，变量 server 的值为 "127.0.0.1:9092"。
画面12: 展示了浏览器访问 http://localhost:8080/consumer/8 的结果，返回了用户信息 JSON 数据。
画面13: 展示了课程 PPT 的“在RestTemplate的配置方法上添加@LoadBalanced注解”部分，以及修改 ConsumerController.java 的代码示例。
画面14: 展示了课程 PPT 的“15. Ribbon负载均衡应用”章节，其中包含“小结”和“16. 熔断器Hystrix简介”章节的标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class ConsumerController {
    @Autowired
    private RestTemplate restTemplate;
    @Autowired
    private DiscoveryClient discoveryClient;

    @RequestMapping("/id")
    public User queryById(@PathVariable Long id) {
        String url = "http://localhost:9091/user/" + id;
        return restTemplate.getForObject(url, User.class);
    }
}
```

画面2:
```markdown
小结：
Ribbon提供了轮询、随机两种负载均衡算法（默认是轮询）可以实现从地址列表中使用负载均衡算法获取地址进行服务调用。

15. Ribbon负载均衡应用

目标：配置启动两个用户服务，在consumer-demo中使用服务名实现根据用户id获取用户

分析：
需求：可以使用RestTemplate访问http://user-service/user/获取服务数据。
可以使用Ribbon负载均衡：在执行RestTemplate发送服务地址请求的时候，使用负载均衡拦截器拦截，根据服务名获取服务地址列表，使用Ribbon负载均衡算法从服务地址列表中选择一个服务地址，访问该地址获取服务数据。

实现步骤：
1. 启动多个user-service实例（9091,9092）；
2. 修改RestTemplate实例化方法，添加负载均衡注解；
3. 修改ConsumerController；
```

画面3:
```yaml
server:
  port: 9091
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/springcloud
    username: root
    password: root
  application:
    name: user-service
  eureka:
    client:
      service-url:
        defaultZone: http://127.0.0.1:10066/eureka
      prefer-ip-address: true
      # eureka
      ip-address: 127.0.1
      lease-renewal-interval-in-seconds: 5
      lease-expiration-duration-in-seconds: 5
```

画面4:
```java
//代码中url中的user-service
List<ServiceInstance> serviceInstances = discoveryClient.getInstances("user-service");
ServiceInstance serviceInstance = serviceInstances.get(0);
String url = "http://" + serviceInstance.getHost() + ":" + serviceInstance.getPort() + "/user/" + id;
return restTemplate.getForObject(url, User.class);
```

画面5:
```java
//获取eureka中注册的user-service的实例
List<ServiceInstance> serviceInstances = discoveryClient.getInstances("user-service");
ServiceInstance serviceInstance = serviceInstances.get(0);
String url = "http://" + serviceInstance.getHost() + ":" + serviceInstance.getPort() + "/user/" + id;
return restTemplate.getForObject(url, User.class);
```

画面6:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>consumer-demo</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面7:
```text
META-INF
spring-configuration
spring-configuration-metadata.json
```

画面8:
```java
@RequiredArgsConstructor
private List<LoadBalancerRequestTransformer> transformers = Collections.emptyList();

@Bean
public SmartInitializingSingleton loadBalancedRestTemplateInitializerDeprecated(
        final ObjectProvider<List<RestTemplateCustomizer>> restTemplateCustomizers) {
    return () -> restTemplateCustomizers.orderedStream().forEach(
            (restTemplateCustomizer) -> {
                for (RestTemplate restTemplate : loadBalancedAutoConfiguration.this.restTemplates) {
                    restTemplateCustomizer.customize(restTemplate);
                }
            });
}

@Bean
@ConditionalOnMissingBean
public LoadBalancerRequestFactory loadBalancerRequestFactory(
        LoadBalancerClient loadBalancerClient, this.transformers) {
    return new LoadBalancerRequestFactory(loadBalancerClient, this.transformers);
}

@Configuration
@ConditionalOnMissingBean
static class LoadBalancerAutoConfiguration {
    @Autowired(required = false)
    private List<LoadBalancerRequestTransformer> transformers = Collections.emptyList();

    @Bean
    public SmartInitializingSingleton loadBalancedRestTemplateInitializerDeprecated(
            final ObjectProvider<List<RestTemplateCustomizer>> restTemplateCustomizers) {
        return () -> restTemplateCustomizers.orderedStream().forEach(
                (restTemplateCustomizer) -> {
                    for (RestTemplate restTemplate : loadBalancedAutoConfiguration.this.restTemplates) {
                        restTemplateCustomizer.customize(restTemplate);
                    }
                });
    }

    @Bean
    @ConditionalOnMissingBean
    public LoadBalancerRequestFactory loadBalancerRequestFactory(
            LoadBalancerClient loadBalancerClient, this.transformers) {
        return new LoadBalancerRequestFactory(loadBalancerClient, this.transformers);
    }
}
```

画面9:
```java
@RequiredArgsConstructor
private List<LoadBalancerRequestTransformer> transformers = Collections.emptyList();

@Bean
public SmartInitializingSingleton loadBalancedRestTemplateInitializerDeprecated(
        final ObjectProvider<List<RestTemplateCustomizer>> restTemplateCustomizers) {
    return () -> restTemplateCustomizers.orderedStream().forEach(
            (restTemplateCustomizer) -> {
                for (RestTemplate restTemplate : loadBalancedAutoConfiguration.this.restTemplates) {
                    restTemplateCustomizer.customize(restTemplate);
                }
            });
}

@Bean
@ConditionalOnMissingBean
public LoadBalancerRequestFactory loadBalancerRequestFactory(
        LoadBalancerClient loadBalancerClient, this.transformers) {
    return new LoadBalancerRequestFactory(loadBalancerClient, this.transformers);
}

@Configuration
@ConditionalOnMissingBean
static class LoadBalancerAutoConfiguration {
    @Autowired(required = false)
    private List<LoadBalancerRequestTransformer> transformers = Collections.emptyList();

    @Bean
    public SmartInitializingSingleton loadBalancedRestTemplateInitializerDeprecated(
            final ObjectProvider<List<RestTemplateCustomizer>>
