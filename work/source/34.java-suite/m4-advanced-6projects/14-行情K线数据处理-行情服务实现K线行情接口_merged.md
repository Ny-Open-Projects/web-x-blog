# 14-行情K线数据处理-行情服务实现K线行情接口 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面我们开始学习行情服务提供K线的获取接口

首先我们要确保行情服务引入了GRBC的相关依赖配置

打开行情服务的控母文件

我们将GRBC的依赖加入进来

将组件名称做个调整

使Bus开头

让它导入生效

导入完成之后增加GRBC的服务端配置

在这里添加GRBC服务端配置

进行GRBC

SERVER

给它一个服务端口

1997

我们要去实现GRBC获取行情K线的接口

我们重新创建一个包

New Package

GRBC

新建一个类

New Class

GRBC Stock

Klan Service

它要继承获取行情K线的GRBC接口

我们要去实现GRBC获取行情K线的接口

我们现在来看看

Stock Klan Service Implement Base

给它添加对应的注写

GRBC Service

添加日志插件

将数据层接口注入进来

Shared Stock Klan

WebSite里

通过JPA实现的数据层接口

Auto-Wide

这个是行情K线的数据层接口

我们现在看一下数据层接口这一块提供了哪些功能

我们现在看一下数据层接口这一块提供了哪些功能

这里是保存股票K线数据

这里是保存股票K线数据

注意一下

注意一下

它对保存方法做了一个重写

它对保存方法做了一个重写

为什么要去重写呢

因为K线数据获取这一块

采用了缓存功能

保存K线的时候对K线数据做了更新

那么它就要让缓存信息失效

这样下一次查询就会从数据库当中

加载最新内容更新到缓存里面

我们可以看到

它提供了一个根据时间段范围查询K线数据的接口

传递的是股票编号

起始时间

结束时间

缓存的Key值是stock call的KlanKey

这里加入缓存的目的也就是为了提升K线数据检索的速度

如果所有客户端都是直接查询数据库

给服务器会造成巨大的压力

提供了缓存功能

就要考虑数据的一致性问题

那么针对于K线数据的修改

这里重写了它的C5方法

C5对K线数据进行更新的时候

就会让缓存信息失效

那么下一次K线数据查询的接口

发现缓存里面没有数据信息

就会从数据库里面加载内容

然后更新至缓存里面

好

这个就是数据省接口的处理

我们继续回到GRBC

业务省接口的处理逻辑当中

Edit Insert去重写它的方法

Get K-dan

这个是获取K线行情数据接口

接下来做具体的实现

首先打印字

process if get kdan method

将请求三数信息打印出来

接着我们梳理下整个的实现方法

我们来做个实现

一步根据股票代码

以及时间范围

获取K线数据

第二步将K线数据做便利处理

转换为ProBuffer PB对象

最后一步将数据返回给GRBC

调用客户端

好

那我们来做个实现

这个是一个集合

Store K-dan

K-dan List

通过数据层接口

查询K-dan信息

传递股票编号

传递起始时间

Time Start

最后传递结束时间

做一个放行

接下来拿到数据之后

做便利

将数据转换为PB对象

Get K-dan

Response

Uder

New Builder

设置处理状态

Global

Consistency

Stays OK

然后对K线数据做一个围攻判断

K线必须有数据

我们才能做便利处理

采用流逝方式进行便利

K-dan List

Stream

For Each

K-dan

循环内部做数据导转换

创建K-dan Data PB对象

然后咱们通过一个工具

将对象做一个copy

这个参数是原数据

将K-dan

也就是查询的数据

转换为PB的数据结构

这里为什么会采用

自定义的工具去做封装呢

因为在对象复制的时候

PB数据结构

针对于基础类型

它不能去做一层包装

如果给基础类型

复制闹属性就会报错

所以我们采用一个工具做封装

排除闹属性

避免

封装与基础类型转换时

出现报错的问题

就比如说一个Long型

封装的类型是可以支持闹对象

但是PB数据结构

内部定义的长者型类型int64

它生成的是Long基础类型

这个是不支持闹属性的

所以咱们如果是通过Splint工具下面的

复制方法

它会将闹属性一并copy

这样将闹属性放置PB对象里面的

基础Long型就会出现错误

这一点大家要注意一下

对象转换完成之后

咱们就要将对象填兴到集合当中

Add Keyline Later

要进行构建

最后呢

就是将数据返回给GRBC

调用客户端

Response

Op.Z5

OnNext

Response

Build

然后标记完成

回到讲义当中

这一讲咱们就完成了行情服务

提供K线获取的接口

那这一讲内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个名为“ bulls-stock-quote ”的 Java 项目，重点讲解如何在行情服务中使用 gRPC 协议提供 K 线数据的获取接口。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从引入 gRPC 依赖、配置服务端、定义服务接口、实现数据访问层，到最终在 `getKline` 方法中处理数据并将其转换为 gRPC 响应对象的完整开发流程。核心内容是将数据库中的 K 线数据（`TradeStockKline` 实体）通过 gRPC 的 `StreamObserver` 接口，以流式方式返回给客户端。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，当前章节为 **3.5 行情服务提供K线获取接口**。
*   **00:05 - 00:15**: 讲师在 `pom.xml` 文件中演示如何引入 gRPC 的公共数据结构依赖（`stock-struct-proto`）和相关组件依赖（`bulls-stock-starter-grpc`）。
*   **00:15 - 00:25**: 讲师切换到 `bootstrap-dev.yml` 配置文件，展示 gRPC 服务端的配置，包括 `server.port: 19997`。
*   **00:25 - 00:35**: 讲师在 `GrpcStockKlineService` 接口文件中，展示其继承自 `StockKlineServiceGrpc.StockKlineServiceImplBase`，并定义了 `getKline` 方法。
*   **00:35 - 00:45**: 讲师在 `GrpcStockKlineService` 实现类中，通过 `@Autowired` 注解注入 `TradeStockKlineRepository` 数据访问层。
*   **00:45 - 00:55**: 讲师在 `getKline` 方法中，调用 `tradeStockKlineRepository.findAllByStockCodeAndTimeBetween(...)` 查询数据库。
*   **00:55 - 01:05**: 讲师开始处理查询结果，将 `List<TradeStockKline>` 转换为 `GetKlineResponse`。
*   **01:05 - 01:15**: 讲师使用 `KlineData.Builder` 构建响应对象，并通过 `BeanAssistant.copyNotNullProps` 方法进行属性复制，以避免 `null` 值导致的类型转换错误。
*   **01:15 - 01:25**: 讲师将构建好的 `KlineData` 对象通过 `responseObserver.onNext(...)` 方法发送给客户端。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.5 行情服务提供K线获取接口`
    *   **子标题**: `1. 引入gRpc配置`
    *   **PPT 文本**: 展示了 `pom.xml` 中的依赖配置，包括 `stock-struct-proto` 和 `bulls-stock-starter-grpc`。

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <!-- gRPC 公用数据结构依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>stock-struct-proto</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- gRPC 相关组件依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-starter-grpc</artifactId>
            <version>${project.stock.version}</version>
        </dependency>
        ```
    *   **`bootstrap-dev.yml` 配置**:
        ```yaml
        # gRPC服务端配置
        grpc:
          server:
            port: 19997
        ```
    *   **`GrpcStockKlineService` 接口定义**:
        ```java
        @GrpcService
        public interface GrpcStockKlineService extends StockKlineServiceGrpc.StockKlineServiceImplBase {
            // 定义 getKline 方法
        }
        ```
    *   **`GrpcStockKlineServiceImpl` 实现类**:
        ```java
        @GrpcService
        public class GrpcStockKlineServiceImpl extends StockKlineServiceGrpc.StockKlineServiceImplBase {
            @Autowired
            private TradeStockKlineRepository tradeStockKlineRepository;

            @Override
            public void getKline(GetKlineRequest request, StreamObserver<GetKlineResponse> responseObserver) {
                // 1. 根据股票代码和时间范围，获取K线数据
                List<TradeStockKline> klineList = tradeStockKlineRepository.findAllByStockCodeAndTimeBetween(
                    request.getStockCode(), request.getTimeStart(), request.getTimeEnd()
                );

                // 2. 将K线数据遍历处理，转换为PB对象
                if (klineList != null && !klineList.isEmpty()) {
                    klineList.stream().forEach(kline -> {
                        // 数据对象转换
                        KlineData.Builder klineData = KlineData.newBuilder();
                        BeanAssistant.copyNotNullProps(kline, klineData);
                        // 将转换后的对象发送给客户端
                        responseObserver.onNext(klineData.build());
                    });
                }
            }
        }
        ```
    *   **`BeanAssistant.copyNotNullProps` 方法**:
        该方法用于将源对象（`kline`）的非空属性复制到目标对象（`klineData`）中，避免 `null` 值导致的类型转换错误。

---

### 4) 关键场景与演示描述

*   **场景一：引入 gRPC 依赖** (00:05 - 00:15)
    *   **描述**: 讲师在 `pom.xml` 文件中，通过鼠标点击和键盘输入，添加了两个 gRPC 依赖项：`stock-struct-proto` 和 `bulls-stock-starter-grpc`。这为后续的 gRPC 服务开发奠定了基础。

*   **场景二：配置 gRPC 服务端** (00:15 - 00:25)
    *   **描述**: 讲师切换到 `bootstrap-dev.yml` 文件，定位到 `grpc.server.port` 配置项，并将其设置为 `19997`。这定义了 gRPC 服务监听的端口。

*   **场景三：实现 gRPC 服务接口** (00:25 - 00:45)
    *   **描述**: 讲师在 `GrpcStockKlineService` 接口文件中，通过 `@GrpcService` 注解定义了服务，并在实现类中通过 `@Autowired` 注解注入了数据访问层 `TradeStockKlineRepository`。

*   **场景四：数据查询与转换** (00:45 - 01:15)
    *   **描述**: 讲师在 `getKline` 方法中，首先调用 `tradeStockKlineRepository.findAllByStockCodeAndTimeBetween(...)` 查询数据库。然后，通过 `BeanAssistant.copyNotNullProps` 方法将查询到的 `TradeStockKline` 对象转换为 `KlineData` 对象，并通过 `responseObserver.onNext(...)` 方法将转换后的对象发送给客户端。

*   **场景五：流式响应** (01:15 - 01:25)
    *   **描述**: 讲师在 `getKline` 方法中，使用 `responseObserver.onNext(...)` 方法将转换后的 `KlineData` 对象发送给客户端。这实现了 gRPC 的流式响应，客户端可以逐个接收数据。
