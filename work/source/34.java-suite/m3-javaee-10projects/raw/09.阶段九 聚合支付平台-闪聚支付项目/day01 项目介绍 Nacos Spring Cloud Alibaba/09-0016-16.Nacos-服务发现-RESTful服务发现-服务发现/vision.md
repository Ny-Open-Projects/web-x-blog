# 画面线理解：16.Nacos-服务发现-RESTful服务发现-服务发现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\16.Nacos-服务发现-RESTful服务发现-服务发现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:34, 01:32, 02:38, 03:52, 04:36, 05:29, 06:00, 06:24, 07:00, 07:21, 08:03, 08:33, 09:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:24:37

1) 这一组画面整体在讲如何使用 Nacos 作为服务注册与发现中心，结合 Spring Cloud LoadBalancer 实现服务消费者通过服务名调用服务提供者，并演示了负载均衡的实现。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 IntelliJ IDEA 启动界面，项目名为 nacos-restful-provider，当前打开的文件为 application.yml。
画面2: 显示项目结构，选中 nacos-restful-provider 模块，编辑器中高亮显示了 pom.xml 文件中的依赖部分，包含 spring-boot-starter-web 和 spring-cloud-starter-alibaba-nacos-discovery。
画面3: 编辑器中显示 RestConsumerController.java 文件内容，高亮部分为通过服务名拼接 URL 的代码。
画面4: 鼠标悬停在代码中 serviceId 变量上，弹出的提示框显示了该变量的类型和值。
画面5: 编辑器中显示 RestConsumerController.java 文件内容，高亮部分为使用 LoadBalancerClient 的 choose 方法选择服务实例的代码。
画面6: 显示 PPT 页面，标题为“2.3.4 负载均衡”，内容包括执行流程和负载均衡的定义。
画面7: 显示控制台输出，服务启动成功，端口为 5000。
画面8: 显示 RestConsumerController.java 文件内容，高亮部分为注释“通过服务名调用”。
画面9: 显示控制台输出，服务启动成功，端口为 5000。
画面10: 显示控制台输出，服务启动成功，端口为 5000。
画面11: 显示 application.yml 文件内容，配置了服务名、Nacos 服务发现中心地址。
画面12: 浏览器显示 Whitelabel Error Page，提示 Internal Server Error。
画面13: 显示 application.yml 文件内容，配置了服务提供方的地址。
画面14: 显示 PPT 页面，标题为“2.3.4 负载均衡”，内容包括执行流程和负载均衡的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```xml
<modelVersion>4.0.0</modelVersion>
<groupId>com.alibaba.cloud</groupId>
<artifactId>nacos-restful-provider</artifactId>
<packaging>jar</packaging>
<version>0.0.1-SNAPSHOT</version>
<name>nacos-restful-provider</name>
<description>Demo project for Spring Boot</description>

<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.7.RELEASE</version>
    <relativePath/>
</parent>

<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <java.version>1.8</java.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
    </dependency>
</dependencies>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Hoxton.SR1</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面3:
```java
@RestController
public class RestConsumerController {

    @Value("${server.port}")
    private String port;

    @Autowired
    private LoadBalancerClient loadBalancerClient;

    @GetMapping(value = "/service")
    public String service() {
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject("http://"+provider+"/service", String.class);
        return "consumer invoke | "+result;
    }
}
```

画面5:
```java
@RestController
public class RestConsumerController {

    @Value("${server.port}")
    private String port;

    @Autowired
    private LoadBalancerClient loadBalancerClient;

    @GetMapping(value = "/service")
    public String service() {
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject("http://"+provider+"/service", String.class);
        return "consumer invoke | "+result;
    }
}
```

画面11:
```yaml
server:
  port: 5000

spring:
  application:
    name: nacos-restful-provider #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

画面13:
```yaml
server:
  port: 5000

spring:
  application:
    name: nacos-restful-provider #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6:
标题：2.3.4 负载均衡
内容：
执行流程：
1. 服务提供方将自己注册到服务注册中心
2. 服务消费者从注册中心获取服务地址
3. 进行远程调用

画面14:
标题：2.3.4 负载均衡
内容：
执行流程：
1. 服务提供方将自己注册到服务注册中心
2. 服务消费者从注册中心获取服务地址
3. 进行远程调用

5) 不要评价画面美观，不要输出与课程无关的内容。
