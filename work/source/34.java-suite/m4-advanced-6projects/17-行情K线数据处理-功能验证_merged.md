# 17-行情K线数据处理-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着咱们对本章功能做个回顾和总结

第二章的学习目标主要要掌握三点

第一点咱们要实现K线数据的生成

同时理解加工生成处理规则

第二点要实现行情服务和代理服务

对于分中K线获取接口的处理

由行情服务提供接口功能的实现

代理服务去负责调用

然后将数据转发给客户端

最后我们要编写模拟请求

验证K线的获取功能

以及缓存是否生效

同时我们也验证了K线的生成

以及K线获取分表查询的处理

这些都是能够正常处理

对于缓存功能的验证

我们可以通过Ladies客户端

连接到服务器上面

查看对应的缓存例子

这个呢

就是K线缓存的K值

它会根据我们传递的参数进行缓存的处理

我们可以看到它的参数信息

这个呢是股票编号

这个呢是时间范围

我们传递的是开始时间

从一开始结束时间

是去测试当时的时间

如果这些参数发生了变化

它会重新去生成一个缓存

我们可以看到结束时间发生了变化

它又生成了一条新的缓存记录

这个呢就是股票K线

获取借口缓存的处理

我们回到讲义当中

再回顾本章所讲解的具体内容

首先咱们对行情服务K线分表方案做了一个介绍

我们采用的是Sharding Spill

它提供的是一个分布式数据库中间件的解决方案

核心组件

它是由Sharding JDBC

加上Sharding Proxy

以及Sharding Setcar

这三款相互独立的产品组成

我们在这里侧重的是使用Sharding Spill

Sharding JDBC

Sharding JDBC的整个处理时间流程

咱们也做了一个讲解

在使用过程当中

要注意Sharding JDBC的一些功能限制

正是因为它要实现分表功能的处理

所以它就会产生一定的局限性

如果对于一些特殊需要

我们可以绕过Sharding JDBC

采用磁链数据源的方式去做对应的实现

下面是我们行情K线的分表处理时间方案

这里我们是基于不同的时间周期

生成的空间数据

如果是对于复杂的业务场景

要去做分表处理

我们可以采用多维度

比如说根据每个股票产品

划分不同的表

然后每个股票产品下面又可以根据时间周期

再去生成不同的数据表

这样每个表下面的就能存储更多的数据

提升整体的存储能力

对于高频发海量数据的应用场景

咱们还要考虑做好分表的数据归档

因为随着时间的增长

即便你采用多维度的分表方案

这些表数据还是会不断的膨胀

一般以一个年度周期作为归档处理就可以了

下面就是咱们行情服务K线分表

对于Sharding JDBC这个组件的集成配置

这里我们讲解了在多数据文当中

如何去实现Sharding JDBC的集成配置

如何去实现单库的分件配置

从中我们也演示了如何去做多库多片的配置

多库

可以基于咱们单户分片的配置规则

在上面加以调整就可以实现多户分片的配置

再往下面就讲解了行情服务K线生成功能的实现

大家要理解好K线生成的处理流程

它的具体处理规则

在这里我们都做了详细的讲解

K线生成完成之后

我们就可以提供K线行情的获取接口

首先定义RoboVo的数据结构

这里会将完整的K线数据

返回给服务端

要定义内部和外部的通讯数据结构

接着我们就在行情服务当中

提供了K线的获取接口

为了提升K线处理接口的获取速度

咱们加入了返存的功能

重写了JPA的C5方法

在查询结果当中加入了返存的功能

通过C5方法的重写

能够确保数据及时更新

获取最新有效的数据

再往下面咱们就在代理服务当中

实现了K线接口的调用

代理服务的处理器

是基于工厂模式做的实现

我们要去扩展一个新的行情服务处理器

对于新功能接口的扩展

工厂模式能够很好的去处理

不会影响咱们原有接口功能的处理流程

只需要在工厂当中

再增加新的处理器的扩展就可以了

我们现在就来看看

K线接口的调用

我们现在就来看看

接下来我们就在模拟客户团

增加了K线行情的调用接口

增加了对应的交付菜单操作指令

最后咱们也对整体功能

做了一个测试和验证

首先咱们测试了K线数据的生成功能

这个会根据咱们的分片配置规则

生成到对应的表当中

这个我们也从数据库做了验证

刷点JTBC的分片处理

是能够正常生效

接着

是通过模拟客户端

对行情获取接口

做了一个调用和验证

那我们也验证了分片的查询功能

刷点JTBC

对于查询的分片

也能够自动帮助咱们去实现

刷点JTBC的查询

能够自动将所有的分片信息

汇总到一起

形成一个完整的结果

最后我们也查看到缓存的数据

在这上面呢

也能够生成K线接口的缓存信息

好

最后咱们再来看看

我们的项目

再总结一下

本章实现了K线生成功能

以及获取接口

我们需要掌握K线的加工生成处理规则

要掌握它具体的实现流程

根据不同的行情员呢

采用不同的加工处理方式

因为在实际项目当中

咱们所对接的行情员

可能会各种各样

但是整体实现流程

基本上都是一致的

不同的是行情接口的对接方式

以及行情接口的结构方面的差异

在这里咱们通过了

NetEase的客户端

模拟了K线数据的获取功能

依据获取的分K数据

咱们也可以去尝试

模拟加工其他周期的K线数据

因为它们的处理机制都是一样的

好

在这里呢

就是对本章内容的回顾与总结

那这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频课程聚焦于一个金融行情系统的后端开发，核心内容是实现K线数据的生成、存储、查询与分发。课程通过分章节讲解，从架构设计（如Sharding-JDBC分库分表）到具体实现（如K线数据的缓存、Protobuf接口定义、gRPC服务调用），并辅以Redis和Netty等技术进行数据模拟和验证。课程目标是构建一个能够处理实时行情数据、支持多周期K线查询、并具备高并发能力的系统。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **第3章：市价下单功能 (目标)**
    *   本章目标是实现市价下单功能，但视频内容主要围绕其依赖的行情数据处理模块展开。
*   **第2章：行情K线数据的处理 (实现)**
    *   **3.1 行情服务K线分表方案**：介绍使用Sharding-JDBC进行分库分表的架构。
    *   **3.2 行情服务K线分表ShardingJDBC集成配置**：讲解如何在项目中引入Sharding-JDBC依赖并配置分片规则。
    *   **3.3 行情服务K线生成功能实现**：核心内容，演示如何在服务中生成K线数据并缓存到Redis。
    *   **3.4 K线行情接口protobuf数据结构**：定义K线数据的Protobuf消息格式。
    *   **3.5 行情服务提供K线获取接口**：实现gRPC服务，对外提供K线数据查询接口。
    *   **3.6 代理服务实现K线接口调用**：通过代理服务将客户端请求路由到具体的业务处理器。
    *   **3.7 模拟客户端增加K线行情调用接口**：演示客户端如何调用服务。
    *   **3.8 功能验证**：通过Redis Desktop Manager工具验证数据缓存和查询功能。
*   **第4章：总结**
    *   总结K线数据处理的核心要点，包括数据生成规则、缓存机制和接口调用方式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **Sharding-JDBC架构图**：清晰展示了Sharding-JDBC如何在应用层和数据库层之间工作，包括SQL解析、改写、路由和结果归并等核心步骤。
    *   **Redis数据结构截图**：展示了K线数据在Redis中以`SimpleKey`形式存储的结构，如 `stock:quote:kline::SimpleKey [601398, 1]`，其中`601398`是股票代码，`1`是周期（如1分钟）。

*   **代码**:
    *   **Maven依赖配置**：
        ```xml
        <!-- sharding-jdbc 依赖 -->
        <dependency>
            <groupId>io.shardingsphere</groupId>
            <artifactId>sharding-jdbc-core</artifactId>
            <version>${sharding.jdbc.version}</version>
        </dependency>
        ```
        *   版本号为 `3.1.0`。
    *   **K线数据缓存逻辑**：
        ```java
        private void processKline(TradeStockQuoteLast quotelast) {
            TradeStockKline kline = klineMap.get(quotelast.getStockId());
            if (null == kline) {
                // 新K线
                kline = newKline(quotelast);
                klineMap.put(quotelast.getStockId(), kline);
            }
        }
        ```
    *   **Protobuf数据结构**：
        ```protobuf
        message GetKlineResponse{
            string status = 1;
            string message = 2;
            repeated KlineData klineData = 3;
        }
        ```
    *   **gRPC服务接口**：
        ```java
        @GrpcService
        @Log4j2
        public class GrpcStockKlineService extends StockKlineServiceGrpc.StockKlineServiceImplBase {
            @Autowired
            TradeStockKlineRepository tradeStockklineRepository;
            @Override
            public void getKline(GetKlineRequest request, StreamObserver<GetKlineResponse> responseObserver) {
                log.info("Process in GrpcStockKlineService.getKline, request: {}", request);
            }
        }
        ```
    *   **数据查询方法**：
        ```java
        @Cacheable(value=GlobalConstants.STOCK_QUOTE_KLINE_KEY)
        List<TradeStockKline> findByStockCodeAndTimeBetween(String stockCode, Long begin, Long end);
        ```
    *   **代理服务处理器生成逻辑**：
        ```java
        public IBaseStockProcessor generateStockProcessor(StockHeadProto.RequestType requestType) throws ComponentException {
            IBaseStockProcessor processor = null;
            switch (requestType) {
                case USER_LOGIN:
                    processor = stockUserProcessor;
                    break;
                case PLACE_ORDER:
                    processor = stockDealProcessor;
                    break;
                case QUOTE_KLINE:
                    processor = stockKlineProcessor;
                    break;
            }
            return processor;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：Sharding-JDBC分库分表架构演示**
    *   **描述**：通过PPT图示，讲解了Sharding-JDBC如何将应用层的SQL请求分发到不同的数据库实例，实现数据的水平拆分。图示中包含了SQL解析、改写、路由和结果归并等关键步骤，帮助理解其工作原理。

*   **场景二：K线数据缓存与Redis操作演示**
    *   **描述**：在代码中演示了如何将生成的K线数据缓存到Redis中。随后，通过Redis Desktop Manager工具，展示了缓存数据的结构，确认了数据已成功写入。同时，演示了如何通过gRPC接口查询缓存中的K线数据，并在控制台输出了查询结果。

*   **场景三：gRPC服务接口实现与调用**
    *   **描述**：演示了如何使用gRPC框架定义和实现一个K线数据查询服务。代码中包含了服务类的定义、依赖注入和接口方法的实现。通过代理服务，将客户端的请求路由到具体的处理器，最终调用数据库或缓存获取数据并返回。

*   **场景四：功能验证与数据查询**
    *   **描述**：在Redis Desktop Manager中，通过执行查询命令，验证了系统能够根据股票代码和时间范围查询到正确的K线数据。同时，通过控制台输出，确认了缓存机制有效，数据能够被正确获取和处理。
