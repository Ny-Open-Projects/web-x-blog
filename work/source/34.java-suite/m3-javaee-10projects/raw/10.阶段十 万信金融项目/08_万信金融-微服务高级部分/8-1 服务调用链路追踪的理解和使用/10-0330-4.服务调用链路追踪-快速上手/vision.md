# 画面线理解：4.服务调用链路追踪-快速上手

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\4.服务调用链路追踪-快速上手_【海量资源尽在 666java.com】.mp4
- 抽帧：11 帧 @ 00:19, 00:26, 00:57, 01:04, 01:07, 01:16, 01:18, 01:19, 01:20, 01:34, 01:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:05:29

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Spring Cloud Sleuth 以实现分布式链路追踪，并结合 Zipkin Server 进行数据存储与展示。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT 的目录结构，当前章节为“2.1 快速上手”，并显示了“Spring Cloud Sleuth”与“Zipkin Server”的架构图，说明 Sleuth 作为客户端将链路数据发送至 Zipkin Server。
画面2: 展示“2.1 快速上手”章节内容，介绍使用 Sleuth 的两步操作，第一部分是引入 Maven 依赖。
画面3: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面4: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面5: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面6: 展示“2.1 快速上手”章节内容，继续介绍引入 Maven 依赖。
画面7: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <parent> 配置块。
画面8: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencies> 配置块，包含 spring-boot-starter-web 和 spring-cloud-starter-sleuth。
画面9: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencyManagement> 配置块，包含 spring-cloud-dependencies。
画面10: 展示“2.1 快速上手”章节内容，展示 Maven 依赖的 <dependencyManagement> 配置块，包含 spring-cloud-dependencies 的 <version> 和 <scope>。
画面11: 展示“2.1 快速上手”章节内容，展示 Spring Boot 配置文件中的 sleuth 配置项。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面7:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>
```

画面8:
```xml
<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
</dependencies>
```

画面9:
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面11:
```properties
# 是否开启 sleuth
spring.sleuth.enabled=true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1: PPT 标题为“2. Spring Cloud Sleuth”，子标题“2.1 快速上手”。架构图中，“Zipkin Server”通过双向箭头指向“追踪数据存储”，“Zipkin Server”通过双向箭头指向“图形化展示”。
画面7-11: PPT 标题为“2.1 快速上手”，内容为文字说明和代码配置。

5) 无。
