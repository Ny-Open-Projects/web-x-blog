# 11-简易下单功能-gRpc自动化配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始实现代理服务的简易下单接口

以及工厂模式的封装使用

代理服务作为GRBC的调用方

在这里也需要添加GRBC的依赖组件

上一讲咱们实现了GRBC的自动化配置

咱们将它的依赖添加进去就可以使用

放置在Proxy下面

依赖咱们添加到最下面

添加完依赖之后

咱们就要去新建对应的处理器

这个处理器的作用是负责处理相应的业务功能

有点类似于接入层Concurer

但它也不完全同于Concurer

它是介于Concurer和Service层之间

在这里咱们可以看到

它会对请求参数做对应的处理

然后去调用业务层的接口

接着就返回对应的包文

处理器不负责具体业务逻辑的

细节方面处理

它是负责整个流程的处理和调用

那咱们再看一下

工厂方法这一块

咱们是如何进行封装的

代理服务呢

它会调用内部多个微服务

有交易或者是业务的数据接口

那客户端发送一个请求进来

该如何去识别

如何去扩展其他的功能接口

在这里咱们又引入了工厂方法

来做相应的实现

首先咱们可以看到

针对于处理器呢

咱们抽象出来的一个公用的处理器

这个呢是处理器的接口

附内当中呢

做了一层封装

封装呢对应的头部信息的处理

因为这些呢是每个处理器呢

所必须涉及到的业务逻辑

所以呢将它们抽象出来

放置附内统一封装去实现

各种处理器定义完成之后

咱们呢再通过一个统一的处理器

在工厂去负责不同接口的调用

通过工厂去获取指定的处理器

当扩充新的功能接口

比如要去实现新的处理器

做对应处理的时候

比如要去实现新的处理器

它不需要去修改调用端

也不需要去修改其他处理器的业务实现逻辑

只需要添加新的处理器

在工厂当中再做一层封装就可以了

这样呢就符合了一个开闭原则

好那咱们呢就从代码上做一个具体实现

回到咱们工程当中

在Proxy工程下面

创建一个新的包

New Package

这个包的话呢专门放置处理器

以及工厂方法的实现

咱们创建新的接口

iBase Stock Processor

这个处理器接口呢

要定义一个公用的方法

处理客户端发送过来的请求

参数呢

是Channel Handle

Context

然后还有咱们在PB里面定义的Stalker Message

这个呢是在Netbook下面

Stalker Message

咱们将它引入进来

需要添加公用的PB数据工程

咱们从交易服务当中copy进来

这个呢是PB数据结构工程

放置PoM文件下面

它导入生效

咱们再回到刚才的接口

这个呢要修改为接口

这样咱们就完成了

Processor的接口定义

添加对应的注释

处理客户端的请求

接着咱们再定义Processor的附类

名称叫AppStack

Stalker Processor

这个是抽箱类

咱们叫它AppStack关键字

这里呢咱们去实现它的公用接口

在这里咱们可以去封装

统一头部的返回数据

还可以去封装

获取用户信息等等

那咱们来做一个实现

Protect Stock Head Portal

返回一个Stock Head对象

PoM名呢就叫Generate Stock Head

Stock Head Portal

创立的参数呢就是Stock Head

还有ScreenStates

将处理的结果状态呢传入进去

咱们先加上对应的注释

它是生成返回的头部信息

因为每个接口呢都必须要返回头部信息

对不对

所以在这里咱们就做一个统一封装

Stock Head

这个呢就叫Head Result

Stock Head.New Builder

Set Request Type

Get Request Type

然后呢设置它的区别号

Sequence ID

直接从Stock Head里面呢

拷贝进去

Get Sequence ID

点Set States

将传递的状态呢设置进去

最后呢要Build构建

构建完成之后呢

将结果作为对象返回出去

抽象内编写完成之后

接着呢咱们就去实现交易服务接口的调用

在这里咱们去创建一个新的处理器

名称就叫StockU Processor

这个处理器呢要去继承咱们定义的抽象处理器

然后呢实现

公用的接口

Base Stock Processor

将接口呢添加进来

处理

客户端发送的请求

要实现GRBC的调用

咱们要将GRBC的客户端呢注入进来

Stock

Chad Deal

Service

GRBC

这里我们采用主设置方式进行调用

它这里呢还提供不同的调用方式

比如说回调

还有异步方式的调用

这些的话呢根据咱们的需要去选择不同的调用方式

接着咱们要去定义GRBCCount的客户端信息

咱们给它一个名称叫GRBCChadService

这个注解的作用呢是声明为它是一个GRBC的客户端

那么这里面配置的名称呢

它会从配置文件里面去读取相应的GRBC的客户端配置

增加注释

接下来咱们再对调用做一个具体实现

客户端调用呢

首先咱们要去获取请求的参数信息

Pace Order Leave

从StockMessage里面获取

这个之前咱们已经定义好了

然后呢要去构造请求参数信息

Pace Order Request New Build

设置了它的参数

这个呢是交易的方向

是买或者卖

Get Deleted

咱们呢直接从参数里面传递进去

然后呢设置它的支付价

Audit Date

Get Excuse Price

下面呢设置了股票ID

Audit Date

Get Stock ID

Set Type

将Type也传递进去

最后呢还Use Excuse

Use Queue

Volume

参数设置完成之后呢

最后要做一个Build的构建

然后呢咱们就去调用

GRPC服务端接口

下单的接口

Final

Pace Order Response

通过咱们的GRPC服务端进行完成调用

传递呢Request就下

为了便于调试呢

咱们将信息呢打一下

上面呢加上对应的注册

添加Service

添加日日的注册

Log

Import

Processing

Stop Deal Process

Process Repressed方法

接收到的响应数据

咱们将它们打印出来

最后呢咱们要

封装返回的报文信息

Stock

Add Plot

首先呢要生成包头

这个呢就可以从复类的方法当中

去生成

传递处理结果状态

是处理OK

另一下单的返回包体

Order Response

New Builder

这个是ProBub对象

将交易订单ID呢返回出去

Response

Get New ID

然后要组装一个响应包文

Response Message

New Builder

将咱们刚才生成的

Head信息

以及包体信息全部注入进去

Stock Head

Set Place

Order Response

最后呢

Build所有构件

然后呢通过Channel

Handler Context

将响应消息呢返回给客户端

Mite and Flash

这样呢咱们就完成了

Proxy客户端

对交易服务下单接口的调用实现

那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 **gRPC** 的股票交易代理服务的开发教程，重点讲解了如何使用 **接口工厂模式** 来封装下单接口。讲师通过 IntelliJ IDEA 开发环境，演示了如何在项目中添加 gRPC 依赖、创建抽象处理器基类、编写具体的业务处理器类，并最终实现一个完整的下单请求处理流程。整个过程体现了面向接口编程和代码复用的设计思想。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示本节内容标题：“3.5 代理服务简易下单接口工厂模式封装”，并说明本节目标是封装下单接口。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示项目结构，并开始讲解如何在 `pom.xml` 中添加 gRPC 服务端依赖。
*   **00:15 - 00:25**: 讲师在 `pom.xml` 中粘贴并高亮显示了 `bulks-stock-starter-grpc` 的 Maven 依赖配置。
*   **00:25 - 00:35**: 讲师开始编写具体的处理器类，首先创建了 `StockDealProcessor` 类，并继承自 `AbstractStockProcessor`。
*   **00:35 - 00:45**: 讲师在 `StockDealProcessor` 类中声明了 `@GrpcClient` 注解的 gRPC 客户端 `stockTradeDealServiceBlockingStub`。
*   **00:45 - 00:55**: 讲师开始编写 `processRequest` 方法，首先从 `StockMessage` 中获取请求参数 `PlaceOrderData`。
*   **00:55 - 01:05**: 讲师使用 `PlaceOrderRequest.newBuilder()` 构建请求对象，并设置方向、执行价格、股票ID和类型等字段。
*   **01:05 - 01:15**: 讲师调用 gRPC 服务端的 `placeOrder` 方法，并将返回的 `PlaceOrderResponse` 作为响应。
*   **01:15 - 01:25**: 讲师将响应封装成 `ResponseMessage`，并调用 `channelHandlerContext.writeAndFlush` 发送回客户端。
*   **01:25 - 01:35**: 讲师在 `AbstractStockProcessor` 中定义了 `generateStockHead` 方法，用于生成响应头信息。
*   **01:35 - 01:45**: 讲师在 `StockDealProcessor` 中调用 `generateStockHead` 方法，并将生成的 `StockHead` 设置到 `ResponseMessage` 中。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **标题**: “3.5 代理服务简易下单接口工厂模式封装”
*   **步骤 1**: “POM依赖增加gRpc:”
*   **步骤 2**: “新建处理器”

#### 代码关键内容

*   **Maven 依赖 (POM)**:
    ```xml
    <!-- gRPC服务端的依赖组件 -->
    <dependency>
        <groupId>com.itcast.trade</groupId>
        <artifactId>bulks-stock-starter-grpc</artifactId>
        <version>${project.stock.version}</version>
    </dependency>
    ```

*   **抽象处理器基类 `AbstractStockProcessor`**:
    *   包含 `protected String generateStockHead(StockHead stockHead)` 方法。
    *   包含 `protected void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage)` 方法。

*   **具体处理器类 `StockDealProcessor`**:
    *   **类定义**:
        ```java
        public class StockDealProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
        ```
    *   **gRPC 客户端注入**:
        ```java
        @GrpcClient("grpc-trade-server")
        private StockTradeDealServiceGrpc.StockTradeDealServiceBlockingStub stockTradeDealServiceBlockingStub;
        ```
    *   **处理请求方法 `processRequest`**:
        ```java
        @Override
        public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
            // 1. 获取请求的参数信息
            PlaceOrderData orderData = stockMessage.getPlaceOrderData();
            
            // 2. 构造请求参数
            PlaceOrderRequest request = PlaceOrderRequest.newBuilder()
                .setDirection(orderData.getDirection())
                .setExecPrice(orderData.getExecPrice())
                .setStockId(orderData.getStockId())
                .setType(orderData.getType())
                .setExecVolume(orderData.getExecVolume())
                .build();
            
            // 3. 调用gRPC服务端的接口
            final PlaceOrderResponse response = stockTradeDealServiceBlockingStub.placeOrder(request);
            log.info("Process in StockDealProcessor.processRequest method. receive: " + response);
            
            // 4. 封装返回的报文信息
            StockHeadProto.StockHead stockHead = generateStockHead(stockMessage.getStockHead(), GlobalConstants.STATUS_OK);
            PlaceOrderResp orderResp = PlaceOrderResp.newBuilder().setDealId(response.getDealId()).build();
            ResponseMessage responseMessage = ResponseMessage.newBuilder()
                .setStockHead(stockHead)
                .setPlaceOrderResp(orderResp)
                .build();
            channelHandlerContext.writeAndFlush(responseMessage);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：添加 gRPC 依赖**
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `pom.xml` 文件，通过鼠标点击和键盘输入，将 `bulks-stock-starter-grpc` 的 Maven 依赖添加到项目中。此步骤是后续开发的基础。

*   **场景二：创建抽象处理器**
    *   **描述**: 讲师在 `com.itcast.bulls.stock.proxy.processor` 包下创建了一个名为 `AbstractStockProcessor` 的 Java 类。该类定义了所有处理器需要实现的通用方法，如 `generateStockHead` 和 `processRequest`，体现了工厂模式中“抽象”的概念。

*   **场景三：实现具体处理器**
    *   **描述**: 讲师创建了 `StockDealProcessor` 类，并使其继承自 `AbstractStockProcessor`。在该类中，讲师使用 `@GrpcClient` 注解注入了 gRPC 客户端，并重写了 `processRequest` 方法。该方法完整地演示了从接收请求、构建请求、调用服务、封装响应到发送响应的整个流程。

*   **场景四：调用 gRPC 服务**
    *   **描述**: 在 `processRequest` 方法中，讲师通过 `stockTradeDealServiceBlockingStub.placeOrder(request)` 调用 gRPC 服务端的下单接口。此调用是整个业务逻辑的核心，讲师通过日志打印了返回的响应信息，以便于调试和验证。

*   **场景五：封装响应信息**
    *   **描述**: 讲师在调用 gRPC 服务后，通过 `generateStockHead` 方法生成响应头，并将响应头和业务响应体封装到 `ResponseMessage` 中。最后，通过 `channelHandlerContext.writeAndFlush(responseMessage)` 将响应发送给客户端，完成了整个请求-响应周期。
