# 画面线理解：20.Nacos-服务发现-Dubbo服务发现-service2微服务

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\20.Nacos-服务发现-Dubbo服务发现-service2微服务【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:59, 03:54, 04:35, 05:16, 06:03, 07:22, 08:27, 09:07, 09:50, 11:30, 12:52, 14:05, 15:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:27:10

1) 这一组画面整体在讲什么（一句话）：
演示如何基于 Nacos 和 Dubbo 构建并配置一个名为 service2 的微服务，包括创建工程、定义接口、配置服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，说明本架构采用 Nacos 作为服务发现和配置中心，支持 RESTful 及 Dubbo 服务注册。文档中提到 service1 需要新建，service2 需要新建，api 网关后边课程讲解。
画面2：在 IntelliJ IDEA 中，打开 “Project Structure” 对话框，准备添加新模块。
画面3：在 “Select Module Content Root” 对话框中，选择目录 “/teach/changjing/model2/code/nacos-discovery” 作为模块内容根目录。
画面4：在项目结构中，选中 “service2-server” 模块，右侧编辑器显示其 pom.xml 文件内容。
画面5：在 “Create New Class” 对话框中，准备创建新类。
画面6：在编辑器中，显示创建的 ServiceApi.java 接口文件内容。
画面7：展示课程文档，讲解微服务架构概念，并附带一个电商系统架构图，图中显示 App/Web 通过 REST API 连接多个服务。
画面8：在 pom.xml 文件中，显示添加了 spring-cloud-starter-dubbo 依赖。
画面9：在 pom.xml 文件中，显示添加了 spring-cloud-starter-alibaba-nacos-discovery 依赖。
画面10：在项目结构中，选中 “service2-server” 模块，右侧编辑器显示其 bootstrap.yml 文件。
画面11：在 bootstrap.yml 文件中，显示 dubbo 配置，包括 base-packages、protocol、name、port、registry 等。
画面12：在 bootstrap.yml 文件中，显示 registry 配置，address 值为 nacos://127.0.0.1:8848。
画面13：展示课程文档，解释 bootstrap.yml 中以 dubbo 开头的配置项含义，以及 spring.application.name 的作用。
画面14：展示课程文档，列出 service2 的接口定义，以及创建 service2-server 工程的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>nacos-dubbo-service2</artifactId>
        <groupId>com.ithema.nacos</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>service2-server</artifactId>
</project>
```

画面6：
```java
package com.ithema.microservice.service2.api;

/**
 * Created by Administrator.
 */
public interface ServiceApi {
    public String dubboService();
}
```

画面8：
```xml
<dependencies>
    <dependency>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>service2-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-dubbo</artifactId>
    </dependency>
</dependencies>
```

画面9：
```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
```

画面10：
```yaml
cloud:
  nacos:
    discovery:
      server-addr: 127.0.0.1:8848
  dubbo:
    scan:
      base-packages: com.ithema.microservice.service2.service
    protocol:
      name: dubbo
      port: 2081
    registry:
      address: nacos://127.0.0.1:8848
      application:
        qos-enable: false
        consumer:
          check: false
```

画面13：
```yaml
dubbo:
  scan:
    base-packages: com.ithema.microservice.service2.service
  protocol:
    name: dubbo
    port: 2081
  registry:
    address: nacos://127.0.0.1:8848
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：
标题：1.1 微服务架构
架构图：
- App/Web
  - REST API
  - REST API
  - REST API
  - （指向下方的多个服务模块）
- （下方的多个服务模块，每个模块之间无直接连接，但都通过 REST API 与 App/Web 交互）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
