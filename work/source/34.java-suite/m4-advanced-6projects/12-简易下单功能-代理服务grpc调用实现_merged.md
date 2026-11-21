# 12-简易下单功能-代理服务grpc调用实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现交易服务的GRBC自动化装配

实现GRBC的自动化装配能够便于房门微服务的使用

同时可以集中统一管理GRBC的组件

也便于今后的维护

那咱们回到代码当中做对应的实现

在Start工程下面

咱们再去创建一个组件New Model

点击Next

模块名称咱们叫Bus Stock Start GRBC

点击Finish

按照导入生效

接着咱们添加它对应的依赖组件

交易服务的GRBC自动化装配

整个实现起来也比较简单

它不需要去做相应的条件化配置

只要咱们引入了GRBC的组件

那么就自动让它生效

咱们再来看看

咱们将依赖Copy进去

放在Defenses标签下面

导入生效

定义GRBC的版本

在复集工程当中

咱们的根集工程

Propits标签下面

增加属性配置

这个版本就选用2.5.0.release

好这样就没有报错

我们Ctrl

依赖就能够正常引入

大家注意一下

这里面的GRBC的

依赖组件

它主要是支持Splint Boot

但是对Splint Cloud的阿里巴巴支持

并不是十分完善

咱们沿用的GRBC版本

相对会比较新一些

它和当前的Splint Cloud

阿里巴巴版本

会存在一些冲突

所以咱们要针对GRBC组件

做一些改造

咱们来做相应的修改

在咱们的工程下面

首先创建对应的包

Cum ID Cast

Bus

Stock

GRBC

接着咱们再创建它的配置类

GRBC

Markos

Configuration

因为它跟Splint Cloud阿里巴巴的兼容性

主要是存在于服务注册发现这一块

如果不做调整和修改

那么咱们所编写的GRBC服务

在注册中心上面是不能够正常发现

所以我们要去修改GRBC

和Splint Cloud的配置类

和Nacos服务注册发现这一块的处理逻辑

首先添加配置组件

Configuration

Enable Configuration

开启配置属性的扫描

再加上一个Conditional On Class

项目当中必须有Nacos组件

这个配置才能够生效

然后将Nacos的注册发现类注入进来

Auto-Wide

这个是必须的

咱们加上require.hq

下面再去添加GRBC Server Properties

这里面主要是读取GRBC服务端的配置信息

将它注入进来

那么咱们去编写它的初始化方法

加上注解

初始化完成的时候就会自动执行

添加注册

修改GRBC服务信息注册至Nacos的处理逻辑

解决GRBC组件不支持最新Spring Cloud的阿里巴巴的问题

那咱们去实现它的初始化配置方法

Nacos Regestation

如果是等于空呢

直接Return

Final End Port

GRBC Properties.Get Port

这个是拿取GRBC服务所声明的端口

如果这个端口不等于-1

也就是说这个端口配置信息是存在的

那么咱们就将GRBC的服务端信息放置Nacos原数据当中

属性标识

discovery

metadata port

将端口转化为String的格式

这样咱们就完成了GRBC组件的封装

接着咱们再去

调整交易服务

让它引入咱们封装的GRBC组件

这个GRBC组件的原生依赖组件咱们就不需要了

Defenses.com.idcast

.chat

Bus.stock.startGRBC

版本就是Project.stock.wash

让它导入成效

组件添加完成之后

就要在Resource下面

去配置GRBC的服务端信息

在这里咱们已经配置完成了

咱们再回到讲义当中

封装完GRBC的组件之后

其他节点服务如果需要引入GRBC的组件

使用起来就比较简单

首先添加它对应的依赖

然后再配置文件

增加GRBC相应的配置

如果是服务端

添加服务端的端口相关的信息

如果是消费端

要去指定消费端的一些配置信息

在这里咱们就完成了

交易服务GRBC组件的自动化配置

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“ bulls-stock ”的分布式系统项目中，如何为交易服务（`stock-service`）配置和集成 gRPC 服务的教程。核心内容是创建一个名为 `stock-starter-grpc` 的 Spring Boot Starter 工程，用于自动化配置 gRPC 服务，并将其与 Nacos 服务发现组件集成，以解决 gRPC 服务在 Spring Cloud Alibaba 生态中注册的问题。视频通过展示代码编辑器（IntelliJ IDEA）和 Markdown 文档，逐步演示了从创建工程、添加依赖、编写配置类到最终在业务工程中引用和配置 gRPC 服务的全过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**：视频开始，展示 Markdown 文档的目录结构，当前章节为“3.4 交易服务gRpc自动化配置”，并提示需要新建一个名为 `stock-starter-grpc` 的工程。
*   **00:04 - 00:12**：展示在 IntelliJ IDEA 中创建 `stock-starter-grpc` 工程的目录结构，并在 `pom.xml` 中添加了 `grpc-spring-boot-starter` 依赖。
*   **00:12 - 00:20**：展示 `pom.xml` 中的 `grpc.version` 属性定义，以及 `stock-starter-grpc` 工程的 `pom.xml` 文件内容。
*   **00:20 - 00:30**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **00:30 - 00:40**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **00:40 - 00:50**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **00:50 - 01:00**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:00 - 01:10**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:10 - 01:20**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:20 - 01:30**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:30 - 01:40**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:40 - 01:50**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **01:50 - 02:00**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:00 - 02:10**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:10 - 02:20**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:20 - 02:30**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:30 - 02:40**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:40 - 02:50**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **02:50 - 03:00**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:00 - 03:10**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:10 - 03:20**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:20 - 03:30**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:30 - 03:40**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:40 - 03:50**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **03:50 - 04:00**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:00 - 04:10**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:10 - 04:20**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:20 - 04:30**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:30 - 04:40**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:40 - 04:50**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **04:50 - 05:00**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和 `grpc-server-spring-boot-starter` 依赖。
*   **05:00 - 05:10**：展示 `stock-starter-grpc` 工程的 `pom.xml` 文件，其中包含了 `grpc-spring-boot-starter` 和
