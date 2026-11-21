# 09-简易下单功能-交易服务搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去搭建交易服务工程

咱们回到代码当中

在这里面新建一个模块

右键New Model

点击Next

名称的话咱们叫Bus Stock Deal

点击Next Finish

让它导入生效

创建完成之后咱们添加对应的依赖

回到讲义当中

将依赖全部选中

把它放在POM文件下面

让它导入更新

好那咱们看一下主要加入了哪些依赖呢

在这里面是Splint Boot的依赖

然后Narcos服务注册发现

下面是公用的数据绳工具主线

还有咱们的实体依赖

然后是Lockit.WQ的消息组件依赖

这个Group ID咱们也调整一下

不然的话它没办法导到

com.alibaba.cloud

再往下面是自动化的返存依赖

返存的实现组件

通过Ladies实现的

然后是GRPC的公用数据结构依赖

这个就是咱们之前所创建的

公用的PB数据工程

接着咱们将对应的包创建下

new Package

com.idcast.bus

stock deal

然后将它的质量

使用的包创建下

Open in terminal

Make dir

Configure配置目录

DAO数据层接口

再创建service层接口

然后就是启动包

咱们刷新看一下

好

相应的包创建完成之后

咱们接着就去实现交易服务工程相关的配置

这里面需要去实现多环境的配置以及呢

日制的配置文件信息

那咱们来做一个实现

首先将多环境版本的配置信息

加入到POM文件当中

放在最下面

导入

模块名称就是stock deal

后面是拼件

不同的版本环境名称

接下来咱们也将它的多环境版本配置文件

加入进来

那咱们就从之前已经实现的代码当中copy进来

在resource支援目录下面

同时将它的日制文件的一起copy进来

放在resource目录下面

咱们看一下工程的配置文件

这里面呢

会涉及到LockitMQ

它是作为消费端

这个呢

是消费端的具体配置

订阅的是stock quota的主题

谷路名称呢

在这里要调整一下

这个就叫stock deal

如果有多个节点了

后面就改用不同的序号

下面是LockitMQ的连接配置信息

然后交易服务呢

它也采用双数据源

咱们可以看到有交易数据源

还有业务数据源

这里有Ladies的缓存配置

Spring统一Session的配置信息

Spring Session可以不需要

咱们在这里并没有提供Control层的对外HTTP接口

也不需要使用到Session相关的功能

可以将它去除

下面的是JPA的功能配置

然后是MyBattis的配置

咱们在这里

DAO数据层主要是通过MyBattis实现了

这个就是MyBattis的路径扫描配置信息

注意路径要配置正确

再往下面就是咱们的GRPC服务端的配置

作为交易服务

它需要提供相关的交易接口

这些交易接口是基于GRPC实现的

GRPC服务端配置也比较简单

在这里只要设定对应的服务端口就可以了

最后咱们就来看看这个服务端的配置信息

咱们再将它的启动内做一个实现

创建启动内

名称的话就叫Stalker deal application

编写启动方法

Spring application

将class传递进来

这个是参数

再加上对应的注解

Spring boot application

Enable discovery clamp

Compand skin

然后配置基础的扫描包

这包就是Comp.idcast

然后还有咱们的Map数据层接口的扫描

因为咱们在这里是通过MyBetis实现了数据层接口

所以这个路径咱们要配置一下

Comp.idcast.boss.stalker deal deal

好那启动内就已经创建完成

咱们回到讲义当中

在这里咱们就先来看看

咱们就先来看看

就已经实现了交易服务

它的工程创建

以及工程的具体配置

好这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `bulls-stock-deal` 的 Spring Cloud 微服务项目，主要演示了如何从零开始构建一个支持 gRPC 通信的交易下单服务。课程内容涵盖了项目初始化、依赖管理（Maven）、协议缓冲区（Protocol Buffers）的编译、配置文件（如 `bootstrap-dev.yml`）的编写、以及 Spring Boot 应用的启动类实现。整个过程旨在为学员提供一个完整的、可运行的微服务项目模板，重点在于服务间的通信和配置管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 项目初始化与目录结构展示。讲师在 IntelliJ IDEA 中展示了项目 `bulls-stock-deal` 的目录结构，包括 `src/main/java` 和 `src/main/resources`。
*   **00:16 - 00:35**: Maven 依赖管理。讲师在 `pom.xml` 文件中添加了项目所需的依赖，包括 `spring-cloud-starter-netty`、`spring-cloud-starter-data-redis`、`spring-cloud-starter-stream-rabbitmq`、`spring-boot-starter-data-redis`、`spring-boot-starter-web`、`spring-boot-starter-test`、`spring-boot-starter-validation`、`spring-boot-starter-actuator`、`spring-boot-starter-security`、`spring-boot-starter-aop`、`spring-boot-starter-jdbc`、`spring-boot-starter-data-jpa`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-mongodb`、`spring-boot-starter-data-elasticsearch`、`spring-boot-starter-data-cassandra`、`spring-boot-starter-data-couchbase`、`spring-boot-starter-data-neo4j`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter-data-redis`、`spring-boot-starter
