# 15-行情K线数据处理-代理服务实现K线接口调用 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去完成代理服务实现K线接口的调用

首先我们要增加行情服务的处理器

这个处理器专门用于处理调用行情服务接口

我们回到工程当中

在代理服务下面

Process包下面我们创建一个新的类

名称叫做StockportProcessor

继承附类AppStack的StockportProcessor

实现公用的接口

iBase StockportProcessor

加上注解

加上日志插件

Org4G2

实现对应的接口

先将行情服务的GRBC接口注入进来

Stock

Kline

ServiceGRBC

StockKline

Blocking

采用GRBC Client进行注入

这个并非

Odd-Wide

这点大家要注意一下

GRBC

Quart

Sew

这个是需要指向工程当中的GRBC服务端的配置

稍后再做实现

先来实现业务处理逻辑

添加注释

GRBC

行情服务接口

这里也添加注释

处理

客户端请求

这里介绍的是客户端所发过来的请求信息

首先第一步

要获取客户端传递的请求参数信息

KlineData

StockMessage

获取KlineData请求参数

注意一下

这个包不要导入错误

这里面出现了一个同名

它是要导入Netimuru下面的对象

我们做个调整

这个包自动修正过来

接下来要构造GRBC的调用请求信息

内部通讯的请求参数信息

GET

KlineRequest

GET

KlineRequest New Build

设置股票ID

KlineData

GET Stock ID

设置股票编号

KlineData

GET Stock Code

然后设置它的查询时间范围

起始时间

KlineData

GET Time Start

设置结束时间

KlineData

GET Time End

最后调用Build方法进行构建

接着要调用

调用远程GRBC行情服务接口

获取K线数据

定义返回接收对象

GET Kline Response

通过GRBC接口进行调用

传递Request的参数

然后打印下调用结果

Process

In

Call

GRBC

Result

Response

接着返回报文

设置头部信息

Stock

Add Plot

Stock Add

通过复利方法

生成头部信息

Stock Message

GET Stock Add

调用结果stays OK

然后第五个步骤

将GRBC返回的K线数据

我们要做一个转换

转换为客户端的响应数据结构

转换为客户端接收的行情数据结构

让客户端能够正常识别处理

我们要将结果信息做一个围攻判断

GET Kline Data List

并且例此当中

也会有一个维工判断

我们要做一个维工判断

也要有数据

不能为空

然后要做个编辑处理

转换数据对象

Response

Response

GET Kline Data List

通过流逝方式

做编辑处理

PoEach

Kline

Stock

Plot

Plot

Kline

Data Response

构建响应参数

Kline

Data

Response

Response

New Builder

创建一个新的对象

采用咱们封装的工具

做对象属性的copy

将Kline信息转换为KlineData

Response

将转换的对象

添加至响应集合当中

GET Data

Response

List

咱们先在外层做个定义

因为内部不需要每次都创建一个集合

我们要将集合放在外面

Builder

Kline

Data

Mask

Mask

List

Stock

Plot

KlineData

Response List

-New Builder

好那我们呢

就可以将转换的对象

添加至KlineData

List集合当中

Add KlineData

最后

要将结果

输出返回给客户端

要构建Response

Message

响应消息

Message

Response

Message

New Builder

将头部信息设置进去

Stockhead

再设置咱们的K线数据

Kline

Data

Response List

所以这里要调用

Builder方法进行构建

外层也要做一个构建

通过客户端的连接通道

将数据输出给客户端

Mind and Flash

Response

Message

Message

最后添加打印日志

标记方法处理结束

这样方法名称也copy过来

提示处理结束

Rosses

Complete

好

我们回到讲义当中

再回顾一下主要的实现流程

首先构造了请求参数

通过GRPC方式

对行情服务的K线

行情接口

进行了调用

然后我们将GRPC接口所拿到的数据

做一个报文转换

注意在这里的便利处理

不能采用并行流

采用普通的stream

做对应的转换

否则的话

会出现ProBuffer List

现成安全的一个问题

因为ProBuffer里面的这个集合

它就是一个普通的List

非现成安全

这一点要注意一下

将K线数据转换完成之后

最后就通过Channel连接通道

将数据输出给客户端

接下来我们还去修改工厂方法

增加行情服务处理器的调用

回到代码当中

找到StoreProcessorFactory

这里增加刚才所实现的处理器

iBase

将名称拷贝下

添加AutoWide注写

加上注释

这个是

行情服务的

处理器

然后在Switch里面加一个判断

Port Kline

Processor指定下

StockPort Processor

Flake

跳出

这样就完成了工厂的扩展

实现了行情服务的调用接口

我们回到讲义当中

最后呢

我们还在工程配置当中增加GRBC

行情服务的调用配置

将这一段配置copy进去

在Resource目录下面

最下面

缩进

保持它的层级顺序

上面这个是交易服务的配置

在这呢咱们就实现了

两个

GRBC的服务端配置

一个是交易服务一个是行情服务

配置信息基本上都是一样的

不同的是需要调用的服务名称

一个是StockDeal指向的是交易服务

一个是StockQuart指向的是行情服务

好那我们回到讲义当中

这一讲我们就完成了代理服务

实现K线接口的调用

那这一讲内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析。

---

### 1) 视频摘要

本视频片段属于一个关于“行情服务K线接口调用”的技术课程，主要讲解如何在代理服务中实现对远程K线行情服务的调用。讲师通过IDE（IntelliJ IDEA）演示了如何编写一个具体的处理器类 `StockQuoteProcessor`，该类继承自抽象基类并实现接口，用于处理客户端的K线请求。核心内容包括：1) 使用 `@GrpcClient` 注解注入gRPC客户端；2) 从客户端消息中提取K线参数；3) 构建gRPC请求对象；4) 调用远程gRPC服务；5) 将服务返回的Protobuf数据转换为客户端可识别的格式；6) 最终将结果写回客户端通道。整个过程体现了服务代理、远程调用、数据序列化与反序列化的完整链路。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示课程大纲，定位到“3.6 代理服务实现K线接口调用”章节。
*   **00:05 - 00:15**: 讲师在IDE中打开并展示 `StockQuoteProcessor.java` 文件，介绍其作为行情服务处理器的角色。
*   **00:15 - 00:30**: 讲师讲解并演示如何在类中注入gRPC客户端，使用 `@GrpcClient("grpc-quote-server")` 注解。
*   **00:30 - 00:45**: 讲师演示如何从接收到的 `StockMessage` 中提取 `KlineData` 参数。
*   **00:45 - 01:00**: 讲师演示如何使用 `GetKlineRequest.newBuilder()` 构建gRPC请求对象，并设置股票代码、开始时间、结束时间等字段。
*   **01:00 - 01:15**: 讲师演示如何调用远程gRPC服务，使用 `stockKlineServiceBlockingStub.getKline(request)` 方法。
*   **01:15 - 01:30**: 讲师演示如何将gRPC返回的 `GetKlineResponse` 中的 `KlineDataList` 转换为客户端所需的 `StockQuoteProto.KlineDataRespList`。
*   **01:30 - 01:45**: 讲师演示如何将转换后的数据写入响应消息 `ResponseMessage`。
*   **01:45 - 02:00**: 讲师演示如何将最终的响应消息通过 `channelHandlerContext.writeAndFlush()` 发送给客户端。
*   **02:00 - 02:15**: 讲师切换到 `StockProcessorFactory.java` 文件，展示如何在工厂类中注册并获取 `StockQuoteProcessor` 实例，以供服务调用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **章节标题**: “3.6 代理服务实现K线接口调用”。
    *   **核心步骤**:
        1.  构造请求参数，通过 `Rpc` 方式，对行情服务的K线接口进行调用。
        2.  将gRPC接口返回的报文进行转换，注意这里的遍历处理不能使用并行流，否则会出现protobuf list的线程安全问题。
        3.  将K线数据转换完成之后，通过channel输出至客户端。
        4.  修改 `StockProcessorFactory`，增加行情服务处理器的调用。

*   **代码关键内容**:
    *   **类定义**:
        ```java
        @Service
        @Log4j2
        public class StockQuoteProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
        ```
    *   **gRPC客户端注入**:
        ```java
        @GrpcClient("grpc-quote-server")
        private StockKlineServiceGrpc.StockKlineServiceBlockingStub stockKlineServiceBlockingStub;
        ```
    *   **处理请求方法**:
        ```java
        @Override
        public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
            // 1. 获取客户端传递的请求参数信息
            KlineData klineData = stockMessage.getKlineData();

            // 2. 构造gRPC内部通讯的请求参数信息
            GetKlineRequest request = GetKlineRequest.newBuilder()
                .setStockCode(klineData.getStockCode())
                .setTimeStart(klineData.getTimeStart())
                .setTimeEnd(klineData.getTimeEnd())
                .build();

            // 3. 调用远程gRPC行情服务接口，获取K线数据
            final GetKlineResponse response = stockKlineServiceBlockingStub.getKline(request);

            // 4. 返回报文，设置头部信息
            StockHeadProto.StockHead stockHead = generateStockHead(stockMessage, getStockHead(), GlobalConstant.STOCK_HEAD);

            // 5. 将gRPC返回的报文转换为客户端前端的行情数据
            StockQuoteProto.KlineDataRespLists.Builder klineDataRespLists = StockQuoteProto.KlineDataRespLists.newBuilder();
            if (null != response.getKlineDataList() && !response.getKlineDataList().isEmpty()) {
                response.getKlineDataList().stream().forEach(kline -> {
                    StockQuoteProto.KlineDataResp.Builder klineDataResp = StockQuoteProto.KlineDataResp.newBuilder();
                    BeanAssistant.copyNotNullProps(kline, klineDataResp);
                    klineDataRespLists.addKlineDataResp(klineDataResp);
                });
            }

            // 6. 返回消息给客户端
            ResponseMessage responseMessage = ResponseMessage.newBuilder()
                .setStockHead(stockHead)
                .setKlineDataRespLists(klineDataRespLists.build())
                .build();
            channelHandlerContext.writeAndFlush(responseMessage);
        }
        ```
    *   **工厂类**:
        ```java
        @Autowired
        private IBaseStockProcessor stockQuoteProcessor;

        public IBaseStockProcessor generateStockProcessor(StockHeadProto.RequestType requestType) throws ComponentException {
            IBaseStockProcessor processor = null;
            switch (requestType) {
                case PLACE_ORDER:
                    processor = stockDealProcessor;
                    break;
                case USER_LOGIN:
                    processor = stockUserProcessor;
                    break;
                default:
                    break;
            }
            return processor;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建处理器类**
    *   **描述**: 讲师在IDE中打开 `StockQuoteProcessor.java` 文件，展示其作为 `IBaseStockProcessor` 接口的实现类。通过 `@Service` 注解将其标记为Spring服务，通过 `@GrpcClient` 注解注入远程gRPC服务客户端 `stockKlineServiceBlockingStub`。

*   **场景二：处理客户端请求**
    *   **描述**: 讲师在 `processRequest` 方法中，首先从 `StockMessage` 中提取 `KlineData` 对象。接着，使用 `GetKlineRequest.newBuilder()` 构建一个gRPC请求对象，并设置股票代码、开始时间、结束时间等参数。

*   **场景三：调用远程gRPC服务**
    *   **描述**: 讲师演示如何调用 `stockKlineServiceBlockingStub.getKline(request)` 方法，将构建好的请求发送给远程服务，并接收返回的 `GetKlineResponse` 对象。

*   **场景四：数据转换与响应构建**
    *   **描述**: 讲师演示如何将gRPC返回的 `KlineDataList` 转换为客户端所需的 `StockQuoteProto.KlineDataRespList`。通过 `stream().forEach()` 遍历数据列表，使用 `BeanAssistant.copyNotNullProps` 方法将数据对象转换为Protobuf对象，并添加到响应构建器中。

*   **场景五：返回响应给客户端**
    *   **描述**: 讲师演示如何将构建好的 `ResponseMessage` 通过 `channelHandlerContext.writeAndFlush(responseMessage)` 方法发送给客户端，完成整个请求-响应周期。

*   **场景六：工厂类集成**
    *   **描述**: 讲师切换到 `StockProcessorFactory.java` 文件，展示如何在工厂类中通过 `@Autowired` 注入 `StockQuoteProcessor`，并在 `generateStockProcessor` 方法中根据请求类型返回相应的处理器实例，从而实现服务的动态调用。
