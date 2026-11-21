# 27-环境搭建-网关路由配置与测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们就可以对网关服务以及用户服务做个测试和验证

分别启动这两个服务

然后就可以去调用去测试

这个Splunkar的阿里巴巴服务是否集成成功

微服务之间流转是否正常

在进行调用之前

我们要去修改一下网关服务

要增加对应的路由转发配置

就在这里面

我们可以将它扣一扣去

然后我们看一下Gateway

找到它对应的配置文件

追加以下路由的转发配置

这些路由是什么意思呢

我们可以看到

转发配置呢

Splunkar的Gateway

后面是Lose

对不对

也就是说用户服务呢

可能是我们网关的转发的一个业务

对吧

可能还会有什么资金服啊

交易服啊等等

那所以呢

会存在多个的转发配置

只不过说

目前呢

我们只做一个简单的演示

所以只存在一个服务节点

那么呢

如果是有多个服务的话呢

我们还可以再去配置

比如说路的杠一

对吧

路的杠二都可以

接下来呢

就是它这边的一个ID

ID呢

就是标识

你是要转发到哪个服务

这个呢

最好跟服务模块名称保持一致

然后再往下面是什么呢

是它的一个URI的相对入境地址

这个URI跟URL是不一样的

对不对

那这里面呢

这里面呢

我们可以看到

它配置的值呢

是什么

LB

然后呢

stock user

这是什么意思呢

它是load balance

说明呢

它是支持负载均衡的调用

然后再往下面呢

是什么

project case

这个project case呢

它要告诉我

哪些路径才会触发对应的转发

那在这里呢

它配置了pass

变量的值呢

是杠星星

也就是说

所有的路径呢

所有的路径

它都会转发过去

这个呢

是做一个简单的测试

那么我们可以配置所有路径

对吧

但是在实际生产环境当中呢

如果说你有多个微幅节点

那么这块路由配置的时候呢

就应该要根据它不同的模块分类

做对应的转发配置

比如说user服务就是杠user

对吧

然后呢

订单服务就是杠order

然后下面的所有的请求路径

是这么一回事

好

这个呢

就是路由的转发配置

那么呢

解解完成之后呢

我们就可以起动

重新启动一下Gateway

然后呢

找到我们的Gateway服务

重新启动一下

之前呢

我们已经是验证了user服务

它是能够正常访问的

对吧

好

网关服务启动完成之后呢

那为了更直观的去测试验证

我们呢

再次访问一下我们的用户服务

是否正常

681

10

我们看一下它的端口

10681

对不对

没有错误

Welcome

这个呢

是正常的

那我们呢

要通过网关服务

网关服务是什么

10680

对吧

网关服务

它是没有写这个接口的

大家可以看到

对吧

没有这么一个接口

那么的话呢

它能不能转发到用户服务下面

能不能返回成功呢

我们就来测试看一下

刷新一下

好

这个呢

不能点刷新

我们直接点

敲回车

好

可以看到

我们多刷新几遍

这个时候呢

10680

它返回的结果

跟用户服务呢

返回的结果都是一致的

对吧

这个呢

就说明我们网关呢

它是正常启动

并且呢

它的路由配置也是生效的

那么

从这个测试验证的话呢

我们也可以知道

我们的开发环境呢

就已经搭建完成

SlimCow的阿里巴巴的微服呢

也能够成功集成到我们项目当中

好

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段为一个关于 Spring Cloud Alibaba 微服务架构的实战教学课程。讲师通过演示如何搭建一个包含网关（Gateway）和用户服务（User Service）的微服务系统，并集成 Nacos 作为服务注册与发现中心。核心内容包括：
- **环境搭建**：使用 IntelliJ IDEA 编辑器，配置 Maven 项目，引入 Spring Cloud Alibaba 的依赖。
- **服务注册**：配置 `application.properties` 文件，使 `stock-user` 和 `stock-gateway` 两个服务成功注册到 Nacos 服务发现中心。
- **网关路由**：在网关服务中配置路由规则，将 `/welcome` 等请求转发至用户服务。
- **功能验证**：通过浏览器访问网关服务，成功返回用户服务的欢迎信息，证明整个系统架构已成功搭建并运行。

整个过程强调了遵循《阿里巴巴JAVA开发手册》的规范，以及 Spring Cloud Alibaba 生态的典型使用方式。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节划分是基于画面内容和逻辑顺序进行的推断：

- **0:00 - 0:05**：开场，展示 Typora 文档编辑器，内容为课程大纲，引出本节主题“工程规范与环境搭建”。
- **0:06 - 0:15**：讲师讲解并展示 Nacos 控制台，确认 `stock-gateway` 和 `stock-user` 两个服务已成功注册。
- **0:16 - 0:30**：切换至 IntelliJ IDEA，展示 `stock-user` 服务的 `application.properties` 配置文件，重点讲解 `server.port`、`spring.application.name` 和 Nacos 服务发现配置。
- **0:31 - 0:45**：展示 `stock-gateway` 服务的 `application.properties` 配置文件，重点讲解网关路由配置 `spring.cloud.gateway.routes`。
- **0:46 - 1:00**：演示启动 `stock-gateway` 服务，观察控制台日志，确认服务启动成功。
- **1:01 - 1:15**：演示启动 `stock-user` 服务，观察控制台日志，确认服务启动成功。
- **1:16 - 1:30**：在浏览器中访问 `http://127.0.0.1:10681/welcome`，验证网关转发功能，成功返回“welcome bulls stock platform!”。
- **1:31 - 1:45**：展示 `StockGatewayApplication` 的主类代码，强调 `@EnableDiscoveryClient` 注解的作用。
- **1:46 - 2:00**：展示 `pom.xml` 文件中的 `maven-compiler-plugin` 配置，讲解项目构建规范。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 页面标题**：第 2 章 工程规范与环境搭建。
- **PPT 页面内容**：
  - **4. 小结**：
    - 掌握工程结构规范，遵循《阿里巴巴JAVA开发手册》的规范，养成良好的编程风格。
    - Spring Cloud Alibaba 微服务环境搭建，完成搭建网关、用户服务、Nacos 服务。

#### 代码关键内容

- **Maven 依赖配置**（`pom.xml`）：
  ```xml
  <dependency>
      <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
  </dependency>
  ```

- **`stock-user` 服务配置**（`application.properties`）：
  ```properties
  # 服务配置信息
  server.port=10681
  spring.application.name=stock-user
  spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
  management.endpoints.web.exposure.include=*
  ```

- **`stock-gateway` 服务配置**（`application.properties`）：
  ```properties
  # 服务配置信息
  server.port=10680
  spring.application.name=stock-gateway
  spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
  spring.cloud.nacos.discovery.service=stock-gateway

  # 转发配置
  spring.cloud.gateway.routes[0].id=stock-user
  spring.cloud.gateway.routes[0].uri=lb://stock-user
  spring.cloud.gateway.routes[0].predicates[0]=Path=/**
  ```

- **`StockGatewayApplication` 主类代码**：
  ```java
  @EnableDiscoveryClient
  @ComponentScan(basePackages = "com.icast")
  public class StockGatewayApplication {
      public static void main(String[] args) {
          SpringApplication.run(StockGatewayApplication.class, args);
      }
  }
  ```

- **`pom.xml` 中的 Maven 编译插件配置**：
  ```xml
  <plugin>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>${maven-compiler-plugin.version}</version>
      <configuration>
          <target>${maven.compiler.target}</target>
          <source>${maven.compiler.source}</source>
          <encoding>UTF-8</encoding>
          <skip>true</skip>
      </configuration>
  </plugin>
  ```

---

### 4) 关键场景与演示描述

- **场景一：服务注册验证**
  - **描述**：讲师首先在 Typora 文档中展示课程大纲，然后切换到 Nacos 控制台。在 Nacos 的服务列表中，清晰地显示了 `stock-gateway` 和 `stock-user` 两个服务均已成功注册，状态为“运行中”。
  - **技术点**：验证了服务注册中心（Nacos）的功能，确保服务能够被发现。

- **场景二：服务配置与启动**
  - **描述**：讲师在 IntelliJ IDEA 中分别打开 `stock-user` 和 `stock-gateway` 项目的 `application.properties` 文件，展示并讲解了各自的配置项。随后，依次点击“Run”按钮启动两个服务，控制台输出了详细的启动日志，包括服务端口、上下文路径、注册成功信息等。
  - **技术点**：演示了 Spring Boot 服务的启动流程，以及配置文件中关键属性的作用。

- **场景三：网关路由转发**
  - **描述**：在 `stock-gateway` 的配置文件中，讲师重点讲解了 `spring.cloud.gateway.routes` 的配置。通过设置 `id`、`uri` 和 `predicates`，定义了将所有以 `/` 开头的请求转发到 `stock-user` 服务。启动后，控制台日志显示“Started StockGatewayApplication”。
  - **技术点**：展示了 Spring Cloud Gateway 的路由功能，实现了服务间的请求转发。

- **场景四：功能端到端测试**
  - **描述**：讲师在浏览器中输入 `http://127.0.0.1:10681/welcome`，页面成功返回“welcome bulls stock platform!”。这表明请求从网关（10680 端口）被正确转发到用户服务（10681 端口），并返回了预期的响应。
  - **技术点**：完成了从客户端到网关再到后端服务的完整请求链路测试，验证了整个微服务架构的可用性。

- **场景五：项目结构与规范**
  - **描述**：讲师展示了 `StockGatewayApplication` 的主类代码，强调了 `@EnableDiscoveryClient` 注解用于启用服务发现功能。同时，通过展示 `pom.xml` 中的 Maven 编译插件配置，讲解了项目构建和编码规范的重要性。
  - **技术点**：强调了微服务项目中注解和配置文件的规范性，以及遵循《阿里巴巴JAVA开发手册》的必要性。
