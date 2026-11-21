# 13-简易下单功能-代理服务工厂方法封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着实现代理服务

对交易服务下单接口的标用处理逻辑

之前咱们在代理服务当中

已经完成了GRBC服务的调用

接着咱们再去对工厂做一层封装

在Processor包下面去创建一个类

名称叫做Stalker Processor Factory

这个是代理服务处理器里面的工厂

将咱们刚才实现的交易服务调用的处理器注入进来

Flyed

iBase

Stalker Processor

Stalker

View Processor

添加AutoWire的注解

Factory也添加相应的注解

它作为一个Compound的组件

添加日志注解

这个是交易服务的处理器

那么这个工厂

怎么去获取到对应的处理器呢

咱们还去编写一个方法

Public

iBase

Stalker Processor

将它的Stalker Head里面的请求类型传递进来

Request Type

咱们抛出对应一场

首先定义iBase Stalker Processor

处理器的公用接口

咱们根据它的请求类型去找到对应的处理器

请求类型它是一个枚举

在这里可以采用

Switch的语法

如果接口比较多

建议大家不要采用if的判断

尽量采用Switch去做判断处理

case

这个是下单的接口

Place Order

Processor

将Stalker Deal Processor赋予给该对象

如果是没找到

咱们给出一个提示信息

before log.add

or says if not found

Processor

然后咱们再抛出一个异常

这样它也无法进行下面的业务逻辑处理

所以要将异常的抛出去

not found Processor

最后将找到的处理器返回出去

咱们再添加对应的注释

这个接口是根据请求参数

获取指定的业务处理器

这里出现了一个错误提示

咱们注意在case处理完成之后

要加上break

跳出switch语句

否则的话它会进入defort的处理逻辑

好

咱们回到讲义当中

在这里咱们就完成了代理服务的

简易下单的接口

以及工厂模式的封装处理

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段主要讲解了在基于 Spring Boot 和 gRPC 的微服务架构中，如何实现一个“代理工厂模式”（Proxy Factory Pattern）来动态创建和管理不同的业务处理器（Processor）。讲师通过 `StockProcessorFactory` 类的实现，演示了如何根据传入的请求类型（如 `PLACE_ORDER`）来实例化并返回对应的处理器（如 `StockDealProcessor`）。视频重点在于展示代码的编写逻辑、异常处理机制（抛出 `ComponentException`），以及如何在 `StockDealProcessor` 中调用 gRPC 服务来处理具体的业务请求（如下单）。整个过程旨在说明如何解耦业务逻辑，提高系统的可扩展性和可维护性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `StockDealProcessor` 类的代码，讲解其核心功能：从请求中提取数据、构建 gRPC 请求、调用 gRPC 服务并封装返回结果。
*   **00:05 - 00:10**: 转到 `StockProcessorFactory` 类，介绍其作为“工厂”的角色，负责根据请求类型创建处理器。
*   **00:10 - 00:20**: 编写 `StockProcessorFactory` 的 `generateStockProcessor` 方法，初始化 `processor` 变量并使用 `switch` 语句根据 `requestType` 进行判断。
*   **00:20 - 00:30**: 在 `switch` 语句中，为 `PLACE_ORDER` 类型设置 `processor = stockDealProcessor;`。
*   **00:30 - 00:40**: 为 `default` 分支添加错误日志和抛出 `ComponentException` 异常，以处理未知的请求类型。
*   **00:40 - 00:50**: 完善 `default` 分支，将异常抛出的类型从 `Exception` 改为 `ComponentException(ApplicationErrorEnum.NOT_FOUND_PROCESSOR)`，以提供更精确的错误信息。
*   **00:50 - 01:00**: 在 `switch` 语句后添加 `return processor;`，使方法能够返回处理器实例。
*   **01:00 - 01:10**: 展示 `StockDealProcessor` 类的结构，包括其继承自 `AbstractStockProcessor` 并实现 `IBaseStockProcessor` 接口，以及其内部的 gRPC 客户端 `stockTradeDealServiceStub`。
*   **01:10 - 01:20**: 展示 `StockDealProcessor` 中的 `processRequest` 方法，用于处理客户端请求。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   在视频末尾，讲师切换到一个 Markdown 文件（`Day13.md`），其中列出了本章的目录结构，包括“3.5 代理工厂模式封装”、“3.6 代理服务Netty集成与Websocket支持”等小节，这为整个课程内容提供了上下文。

*   **关键代码**:
    *   **`StockDealProcessor.java` (核心业务处理器)**:
        ```java
        // 从请求中提取数据
        PlaceOrderData orderData = stockMessage.getPlaceOrderData();
        // 构建 gRPC 请求
        PlaceOrderRequest request = PlaceOrderRequest.newBuilder()
            .setDirection(orderData.getDirection())
            .setExecPrice(orderData.getExecPrice())
            .setStockId(orderData.getStockId())
            .setType(orderData.getType())
            .setExprice(orderData.getExprice())
            .build();
        // 调用 gRPC 服务端下单的接口
        final PlaceOrderResponse response = stockTradeDealServiceBlockingStub.placeOrder(request);
        // 封装返回的报文信息
        StockHeadProto.StockHead stockHead = generateStockHead(stockMessage.getStockHead(), GlobalContext.getGlobalContext());
        PlaceOrderResp orderResp = PlaceOrderResp.newBuilder().setDealId(response.getDealId()).build();
        ResponseMessage responseMessage = ResponseMessage.newBuilder().setStockHead(stockHead).setPlaceOrderResp(orderResp).build();
        channelHandlerContext.writeAndFlush(responseMessage);
        ```
    *   **`StockProcessorFactory.java` (工厂类)**:
        ```java
        @Component
        @Log4j2
        public class StockProcessorFactory {
            @Autowired
            private IBaseStockProcessor stockDealProcessor;
            
            public IBaseStockProcessor generateStockProcessor(StockHeadProto.RequestType requestType) throws ComponentException {
                IBaseStockProcessor processor = null;
                switch (requestType) {
                    case PLACE_ORDER:
                        processor = stockDealProcessor;
                        break;
                    default:
                        log.error("Process in StockProcessorFactory.generateStockProcessor method, not found processor!");
                        throw new ComponentException(ApplicationErrorEnum.NOT_FOUND_PROCESSOR);
                }
                return processor;
            }
        }
        ```
    *   **`StockDealProcessor.java` (处理器类)**:
        ```java
        @Service
        @Log4j2
        public class StockDealProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
            @GrpcClient("grpc-trade-server")
            private StockTradeDealServiceGrpc.StockTradeDealServiceBlockingStub stockTradeDealServiceStub;
            
            @Override
            public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
                // 处理逻辑
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：`StockDealProcessor` 的请求处理流程**:
    *   讲师首先展示了 `StockDealProcessor` 类的代码。
    *   他解释了该类的主要职责：从 `StockMessage` 中提取订单数据，构建一个 `PlaceOrderRequest` 对象。
    *   接着，他调用 gRPC 服务端的 `placeOrder` 方法来执行下单操作。
    *   最后，他将 gRPC 返回的响应数据封装成一个 `ResponseMessage`，并通过 `channelHandlerContext.writeAndFlush` 方法将结果写回给客户端。

*   **场景二：`StockProcessorFactory` 的工厂模式实现**:
    *   讲师切换到 `StockProcessorFactory` 类。
    *   他演示了如何使用 `@Component` 注解将工厂类注册为 Spring Bean。
    *   他通过 `@Autowired` 注解注入了 `stockDealProcessor`。
    *   他编写了 `generateStockProcessor` 方法，该方法接收一个 `StockHeadProto.RequestType` 类型的参数。
    *   在方法内部，他使用 `switch` 语句判断请求类型。
    *   当请求类型为 `PLACE_ORDER` 时，他将 `stockDealProcessor` 赋值给 `processor` 变量。
    *   在 `default` 分支中，他添加了错误日志并抛出了一个自定义的 `ComponentException`，该异常包含一个错误码 `NOT_FOUND_PROCESSOR`，用于标识未找到处理器的情况。
    *   最后，他添加了 `return processor;` 语句，使方法能够返回处理器实例。

*   **场景三：异常处理与错误码**:
    *   讲师特别强调了 `default` 分支中的异常处理。
    *   他将异常抛出的类型从 `Exception` 改为 `ComponentException(ApplicationErrorEnum.NOT_FOUND_PROCESSOR)`，以提供更精确的错误信息。
    *   这种做法有助于在调用方捕获到特定的错误码，从而进行更精细化的错误处理。

*   **场景四：`StockDealProcessor` 的结构与注解**:
    *   讲师展示了 `StockDealProcessor` 类的结构。
    *   他解释了该类继承自 `AbstractStockProcessor` 并实现了 `IBaseStockProcessor` 接口。
    *   他演示了如何使用 `@GrpcClient` 注解来注入 gRPC 客户端 `stockTradeDealServiceStub`。
    *   他展示了 `processRequest` 方法的签名，该方法接收 `ChannelHandlerContext` 和 `StockMessage` 作为参数，用于处理客户端请求。
