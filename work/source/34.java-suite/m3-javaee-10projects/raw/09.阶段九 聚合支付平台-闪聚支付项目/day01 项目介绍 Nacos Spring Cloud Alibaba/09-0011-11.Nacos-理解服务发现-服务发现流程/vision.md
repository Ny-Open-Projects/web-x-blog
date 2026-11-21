# 画面线理解：11.Nacos-理解服务发现-服务发现流程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\11.Nacos-理解服务发现-服务发现流程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:39, 01:14, 01:30, 01:42, 02:45, 03:39, 04:03, 07:06, 07:33, 07:37, 07:48, 08:01, 08:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:21:37

1) 这一组画面整体在讲什么（一句话）：
讲解微服务架构中服务发现的必要性、问题及 Nacos 服务发现机制的工作流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前位于“1.2 理解服务发现”下的“1.2.1 测试环境”章节，右侧显示了 Spring Boot 启动代码和 application.yml 配置文件内容。
画面 2: 展示“1.2.1 测试环境”章节内容，包含一个服务调用流程图（Service A 调用 Service B），并说明通过 Spring Boot 可以创建 nacos-discovery 父工程。
画面 3: 展示浏览器访问 http://127.0.0.1:56020/service 的结果，返回内容为 “consumer invoke | provider invoke”。
画面 4: 展示 pom.xml 文件内容，定义了 nacos-discovery 父工程和 nacos-restful-provider 依赖。
画面 5: 展示“1.2.2 服务发现流程”章节内容，指出静态配置方式的不足，并引出服务发现的必要性。
画面 6: 展示 pom.xml 文件中 <dependencyManagement> 部分的内容，定义了 Spring Boot 的版本。
画面 7: 展示服务发现问题的引言，并引出服务发现的定义和流程图。
画面 8: 展示服务发现中心的架构图，包含 Service A 和 Service B 两个服务实例，以及服务发现中心，图中显示了服务注册和发现的流程。
画面 9: 展示服务发现机制的说明，包括服务注册表、服务发现客户端的工作原理。
画面 10: 展示服务发现中心的架构图，与画面 8 类似，但图中 Service A 的网络地址被修改。
画面 11: 展示服务发现中心的架构图，与画面 8 类似，但图中 Service B 的网络地址被修改。
画面 12: 展示服务发现中心的架构图，与画面 8 类似，但图中 Service A 的网络地址被修改。
画面 13: 展示服务发现中心的架构图，与画面 8 类似，但图中 Service B 的网络地址被修改。
画面 14: 展示服务发现机制的总结，强调服务发现中心的作用和动态服务发现的必要性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
SpringApplication.run(SpringRestConsumerBootstrap.class, args);
```
```yaml
server.port = 56020
# 服务生产方地址
provider.address = 127.0.0.1:56010
```

画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>nacos-discovery</artifactId>
        <groupId>com.ithema.nacos</groupId>
        <version>1.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>nacos-restful-provider</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面 6:
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>2.1.3.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题：1.2.1 测试环境
流程图：Service A → 调用 → Service B
Service B → 配置文件 → Service-B 192.168.25.4:8080

画面 5:
标题：1.2.2 服务发现流程
流程图：Service A → 当网络地址变化如何访问？ → Service B 实例1
Service A → 如何发现实例2，并实现负载均衡？ → 动态增加实例，增加并发、可用性 → Service B 实例2

画面 7:
标题：服务发现
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service A → (2) 获取服务注册表 → API
Service A → (3) 调用 Service-B → Service B

画面 8:
标题：服务发现中心
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 9:
标题：服务发现机制
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 10:
标题：服务发现中心
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 11:
标题：服务发现中心
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 12:
标题：服务发现中心
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 13:
标题：服务发现中心
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表 → Service A
服务发现中心 → (2) 获取服务注册表 → Service B
Service A → (3) 调用 Service-B → Service B

画面 14:
标题：服务发现机制
流程图：Service A → (1) 上报 Service-A 192.168.25.3:8080 → 服务发现中心
Service B → (1) 上报Service-B 192.168.25.4:8080 → 服务发现中心
服务发现中心 → (2) 获取服务注册表
