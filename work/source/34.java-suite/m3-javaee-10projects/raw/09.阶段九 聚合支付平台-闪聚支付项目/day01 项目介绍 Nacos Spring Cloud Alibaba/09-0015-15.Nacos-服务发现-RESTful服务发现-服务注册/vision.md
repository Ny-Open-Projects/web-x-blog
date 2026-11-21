# 画面线理解：15.Nacos-服务发现-RESTful服务发现-服务注册

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\15.Nacos-服务发现-RESTful服务发现-服务注册【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:42, 01:07, 01:28, 01:51, 02:18, 02:51, 03:06, 04:07, 04:28, 05:31, 05:54, 06:34, 07:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:23:59

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Nacos 服务注册中心中，配置并启动一个基于 Spring Cloud Alibaba 的 RESTful 服务提供者和消费者，实现服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档目录，当前章节为“2.3 RESTful服务发现”，并聚焦于“2.3.1 测试环境”，介绍 Spring Cloud Alibaba 作为测试环境。
画面 2: 文档目录中高亮“2.3.2 服务注册”，并展示服务消费者配置文件中 Nacos 服务发现的配置。
画面 3: 在 IntelliJ IDEA 中打开 `RestConsumerController.java`，展示消费者服务中使用 `RestTemplate` 调用服务的代码。
画面 4: 展示 Windows 资源管理器，路径为 `course-pa.../nacos`，显示 `nacos` 文件夹。
画面 5: 文档目录中高亮“2.3.1 测试环境”，并展示在 `nacos-discovery` 工程中添加依赖的 Maven 配置片段。
画面 6: 展示 `pom.xml` 文件中添加 Spring Cloud Alibaba 依赖的配置，版本为 `2.1.0.RELEASE`。
画面 7: 展示 `pom.xml` 文件中 Spring Cloud Alibaba 依赖的配置，版本为 `2.1.0.RELEASE`。
画面 8: 展示 Nacos 控制台，服务名称为 `nacos-restful-provider`，服务实例数为 1，并解释服务名称和实例的概念。
画面 9: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `nacos-restful-provider` 服务的依赖配置，包含 `spring-cloud-starter-alibaba-nacos-discovery`。
画面 10: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `server.port` 配置为 `56010`。
画面 11: 在 IntelliJ IDEA 中打开 `application.yml` 文件，展示 `spring.cloud.nacos.discovery.server-addr` 配置为 `127.0.0.1:8848`。
画面 12: 在 IntelliJ IDEA 中，`application.yml` 文件配置完成，点击运行后，控制台显示服务启动日志，服务名为 `nacos-restful-provider`。
画面 13: 屏幕空白，无内容。
画面 14: 文档目录中高亮“2.3.2 服务注册”，并展示服务提供者配置文件中 Nacos 服务发现的配置，以及 Nacos 控制台显示服务已注册成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
服务消费：
spring:
  application:
    name: nacos-restful-consumer
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848
```

画面 5:
```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>2.1.3.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.cloud</groupId>
      <artifactId>spring-cloud-dependencies</artifactId>
      <version>Greenwich.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
    <dependency>
      <groupId>com.alibaba.cloud</groupId>
      <artifactId>spring-cloud-alibaba-dependencies</artifactId>
      <version>2.1.0.RELEASE</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

画面 6:
```
<dependency>
  <groupId>org.springframework.cloud</groupId>
  <artifactId>spring-cloud-dependencies</artifactId>
  <version>Greenwich.RELEASE</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-alibaba-dependencies</artifactId>
  <version>2.1.0.RELEASE</version>
  <type>pom</type>
  <scope>import</scope>
</dependency>
```

画面 9:
```
modelVersion>4.0.0</modelVersion>
<artifactId>nacos-restful-provider</artifactId>
<dependencies>
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
  </dependency>
  <dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
  </dependency>
</dependencies>
```

画面 10:
```
server:
  port: 56010
```

画面 11:
```
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

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PPT 标题为“2.3.3 服务发现”，下方有文字说明“服务名称：每个服务在服务注册中心的标识，相当于java中的类名。服务实例：网络中提供服务的实例，具有IP和端口，相当于java中的对象，一个实例即为运行在服务器上的一个进程。”
画面 14: PPT 标题为“2.3.2 服务注册”，下方有文字说明“在服务提供工程中配置nacos服务发现相关的配置：服务提供：”，并展示配置内容，以及 Nacos 控制台显示服务已注册成功。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
