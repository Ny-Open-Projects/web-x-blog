# 25-环境搭建-网关服务搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们继续来创建网关服务工程

那网关服务工程这一块呢

该怎么去搭建

怎么去配置

如何去集成Splitcoin Cloud的阿里巴巴服务呢

我们就来左手操作一下

打开我们的16股服务工程

然后呢

创建一个模块

点击Next

在这里呢

我给它一个名称

叫BuzzTalk Gateway

点击Next

将名字调整一下

要有那个分割线

然后呢

点击Finish

注意它在BuzzTalk的目录下面

对不对

好

那么在BuzzTalk下面

它就新增出了一个新的模块

叫BuzzTalk Gateway

我们导入Maven让它自动生效

在这里呢

我们先去实现它的Home的依赖配置

Home这块它要加入哪些依赖呢

我们看一下

将它拷贝过来

在这里的依赖可以看到

第一是Gateway网关的依赖

对不对

然后是Splendid Boot的依赖

因为我们是什么

是Splendid Boot实现的微服务

所以我们要把Splendid Boot的依赖加入进来

然后还有什么

Narcos的服务注册发现依赖

这个是网关服务的核心的三个依赖组件

依赖实现完成之后

我们就要去创建它对应的启动

首先创建对应的包

叫com.itcast

然后呢

点Bus

Stock

Gateway

好

在实际生产环境当中呢

我们建议大家还是要另外再创建一个包

Startup

这个呢是专门用于放置启动内的

我们去创建它的启动内

叫Bus

叫Stock

Gateway

Application

这个的话呢

因为我们已经套用了一个模板

这个没关系

我们把它删除掉

然后呢

去创建它的启动方法

JSVM

然后Tab键

在这里它会把我们自动完成

然后呢

我们去通过Splendid Boot进行一个启动

Splendid Boot Application

Splendid Boot去加载这个启动内

然后呢

Stock

Gateway

Application

这个呢是Cast

然后呢Ax参数

这张参数呢也传得进来

然后这里呢要加上对应的注解

这个注解呢要注意一下

这个注解的话呢

首先是要加上什么Splendid Boot Application

这个标识你为一个Splendid Boot服务

那么呢

还有什么

还要

因为我们是加上了Narcos的依赖对不对

那么呢

你还要开启Narcos的注册发现

Enable

Discovery Plant

好

最后呢

我们要注意一下

因为我们是将它呢放在Startup这个包下面

如果说你在这里面的话呢

有多个包的层级

那么的话呢

它默认是扫描不到的

所以呢

我们还必须要加上一个什么注解

Compand Skin

在这里呢

Base Package指向你的扫描的基准目录

那基准目录呢

我们就让它扫描到我们的根目录

Compand Cost

好

这样呢

就完成了启动内

那么接下来还有实现了网关服务的配置

那网关服务这一块呢

要做哪些配置呢

这个呢

就要去创建一个配置文件

LICTIONT40

大家注意

如果说你配置文件的名称

先写错误了

这个图标它就不会显示出来了

大家呢

要注意一下

所以的话呢

如果是发现这个图标不对

要立马检查一下

这个配置文件名称是不是写错了

那么我们呢

要去定义呢

它的端口

这个端口呢

我们就给它10680

然后呢

还定义什么

服务的名称

对吧

我有这么多服务

你应该告诉我

你叫什么名字

那叫Store Gateway

还有什么呢

还要去配置Narcos的服务注册地址

对吧

好

那我们再来创建一下

Splint.Cloud.Narcos

然后呢

Discovery

Serve Address

这个地址呢

我们刚才是不是启动了Narcos服务啊

那就直接指向本地的Narcos服务端口的地址

那么8818

其他的话呢

就暂时不用再配置了

因为我们是要注册到微服务当中

对不对

注册到Narcos当中

要告诉你

我是一个微服务

接入进来

所以呢

我们最好再给Narcos做一个配置

告诉你呢

我的服务名称

Store Gateway

当然的话呢

你不配置也没有关系

因为你是网关服对不对

不会有用户业务服务去调用你网关服

但是呢

你的应用服务或者业务服务的话呢

一定要告诉Narcos他的服务名称

如果说你的名称不指定

他会产生什么

默认的服务名称

好

这点呢

大家稍微注意一下

那这个呢

就是网关服务的一个创建

以及呢

他的一个基本配置

接下来呢

我们就可以启动一下右键

让运行

看呢

是否启动OK

如果是启动成功之后呢

他可以在Narcos上面进行一个注册

在Narcos管理后台呢

到时候我们就可以看到这个服务节点

好

这个时候呢

他已经启动完成

监听端口呢

是10680

看到没有NetStart的

说明呢

SpinCloud Gateway

它是基于什么

这个呢

我们不拓展去讲

我们来看一下刷新Narcos服务

在这里面的话呢

找到服务列表

点击

这个时候是不是看到

SpinCloud Gateway已经成功注册进去

那么在这里呢

是服务器的名称

对吧

他的一个分组默认主编

因为我们没有指定他的Globe

然后集群的数量

实地数量

健康实地数

这个呢

大家注意一下

如果说你在这里面的话呢

发现我的服务也

也有对不对

但是呢

健康实地数为0

那么就要注意

他的服务呢

是不可用的

可能呢

你的服务出现的假死

或者是崩溃的一个情况

在开发实际使用过程当中呢

大家要注意一下

好

这个呢

就是SpinCloud Gateway

网关服务的创建

以及启动验证

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于使用 Spring Cloud Alibaba 构建微服务网关（Gateway）的实战教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个名为 `stock-gateway` 的网关服务工程。主要内容包括：创建项目结构、配置 Maven 依赖（特别是 Spring Cloud Gateway 和 Nacos 服务发现组件）、编写主启动类 `StockGatewayApplication` 并添加 `@SpringBootApplication` 注解、配置 `application.properties` 文件以指定服务端口和名称，最后运行项目并成功启动，验证了网关服务的正常工作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 IDE 中展示项目结构，提到将创建两个工程：`GATEWAY` 和 `USER`。
*   **00:00:05 - 00:00:15**: 讲师在项目中创建名为 `stock-gateway` 的模块，并展示其目录结构。
*   **00:00:15 - 00:00:30**: 讲师打开 `pom.xml` 文件，开始添加依赖。首先添加了 Spring Cloud Gateway 的依赖。
*   **00:00:30 - 00:00:45**: 讲师继续在 `pom.xml` 中添加 Spring Boot 的核心依赖。
*   **00:00:45 - 00:01:00**: 讲师添加了 Nacos 服务注册与发现的依赖。
*   **00:01:00 - 00:01:15**: 讲师在 `StockGatewayApplication.java` 文件中，通过 `Ctrl+Shift+O` 快捷键查看 `SpringApplication` 类的可用方法。
*   **00:01:15 - 00:01:30**: 讲师在 `StockGatewayApplication.java` 中添加 `@SpringBootApplication` 注解。
*   **00:01:30 - 00:01:45**: 讲师在 `application.properties` 文件中配置服务端口 `server.port=10680` 和服务名称 `spring.application.name=stock-gateway`。
*   **00:01:45 - 00:02:00**: 讲师右键点击主类，选择“Run 'StockGatewayApplication'”来启动服务。
*   **00:02:00 - 00:02:15**: 服务成功启动，控制台输出了服务注册成功的日志信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   左侧大纲显示了课程章节，如“4. 小结”、“第2章 工程规范与环境搭建”、“3.1 工程结构规范”、“3.2 环境搭建”。
    *   视频中多次出现的提示文字，如“网关依赖”、“spring boot 依赖”、“Nacos服务注册发现依赖”。

*   **代码关键内容**:

    *   **Maven 依赖配置 (pom.xml)**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        ```

    *   **主启动类 (StockGatewayApplication.java)**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast")
        public class StockGatewayApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockGatewayApplication.class, args);
            }
        }
        ```

    *   **配置文件 (application.properties)**:
        ```properties
        server.port=10680
        spring.application.name=stock-gateway
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建网关工程**
    *   讲师在 IntelliJ IDEA 中，通过右键菜单在项目 `bulls-stock` 下创建了一个名为 `stock-gateway` 的模块。
    *   展示了该模块的目录结构，包括 `src/main/java` 和 `src/main/resources`。

*   **场景二：配置 Maven 依赖**
    *   讲师打开 `pom.xml` 文件，逐步添加了三个关键依赖：
        1.  **Spring Cloud Gateway**: 用于实现网关路由功能。
        2.  **Spring Boot Actuator**: 用于提供监控和管理端点。
        3.  **Nacos Discovery**: 用于服务注册与发现。

*   **场景三：编写启动类**
    *   讲师在 `src/main/java/com.itcast.bulls.stock.gateway/startup` 包下创建了 `StockGatewayApplication.java`。
    *   使用 `Ctrl+Shift+O` 快捷键查看 `SpringApplication` 类的可用方法。
    *   在类上添加了 `@SpringBootApplication` 注解，用于启动 Spring Boot 应用。
    *   添加了 `@EnableDiscoveryClient` 注解，用于启用服务发现功能。
    *   使用 `@ComponentScan` 注解指定组件扫描的包路径。

*   **场景四：配置服务信息**
    *   讲师在 `src/main/resources` 目录下创建了 `application.properties` 文件。
    *   配置了服务端口 `server.port=10680` 和服务名称 `spring.application.name=stock-gateway`。

*   **场景五：启动并验证服务**
    *   讲师右键点击 `StockGatewayApplication.java`，选择“Run 'StockGatewayApplication'”。
    *   控制台输出了服务启动成功的日志，包括“Initializing RemoteService”、“Started StockGatewayApplication in 0.08 seconds”等信息，表明服务已成功启动并注册到服务发现中心。
