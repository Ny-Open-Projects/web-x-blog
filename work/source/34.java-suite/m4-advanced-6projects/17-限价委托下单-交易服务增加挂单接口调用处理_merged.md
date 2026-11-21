# 17-限价委托下单-交易服务增加挂单接口调用处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们在交易服务当中

要去实现对挂单接口的调用处理

前面咱们在交易服务当中

实现了试价下单的功能

对于试价单和限价单

客户端都是统一采用下单接口

所以在这里呢

咱们只需要去修改交易服务的下单接口的处理逻辑

增加挂单服务接口的调用实现就可以了

好

那打开咱们的工程代码

定位到GRPC Stock Deal Service

这个是在交易服务下面

那我们来完善一下下单接口的处理逻辑

试价下单之前已经做了实现

在这里呢

我们要去增加限价委托单的处理

在做实现之前

大家要思考下

如果当前实时行情的价格

符合限价委托的价格

是否需要去直接匹配撮合处理呢

这个是不需要的

它仍然要通过限价委托接口去做相应的处理

因为如果是存在流通量不足的情况下面

也就是说当前的档位不能够满足请求的数量

它需要跨多个档位进行成交

按市价的逻辑处理只会成交部分

其他部分数据就可能会丢失

所以在这里呢

咱们要通过挂单委托接口进行统一的调用处理

咱们在这里说明一下

请求价格

如果符合当前的行情价格

也要放入挂单对列处理

因为会存在流通量不足的情况

按市价处理

只会成交部分

这点呢

大家要理解清楚

接着我们就要去调用挂单服务的挂单接口

调用挂单服务的挂单接口

挂单处理接口

首先要定义它的请求参数体

place order request builder

order request limit

place order request.new builder

通过binutil工具

咱们将请求参数做一个copy

将原始接收的下单请求参数copy至挂单服务的挂单接口

在挂单的请求参数对象当中

然后要定义它的返回响应对象

order response

limit place order response

stock pending

这里我们要定义GRBC挂单回头接口

stock pending

service

GRBC

walking

spark

加上注解

GRBC client

写入

调用服务端的推辞名称

pending server

还有指向挂单服务

这是挂单

服务的

RPC接口

好接下来我们就要做个调用

调用limit

place order方法

传递request对象

这里要调用builder

接下来我们就要把这个

包装响应消息

response

new builder

set states

将接收的响应参数的

处理状态

设置进去

set order id

这里是response

修正一下

这里要设置

订单的ID

get order id

set new id

这个就取订单的ID

new response

get order id

因为挂单

它只是暂时放在

缓存队列当中

这个时候呢

并不知道是否能够成交

所以是无法获取到

订单成交记录的ID

这里我们放置order id就可以

接下来的话呢

要去设置它的message

将响应的message

传递进去

get message

最后呢要调用build的方法进行构建

好在这里呢就完了

完成了对挂单服务挂单接口的调用处理

接下来咱们还去工程配置文件当中

增加挂单服务的配置

我们要增加

客户端

它的调用配置信息

运营client

在下面呢去增加

挂单

服务的

配置信息

GRPC

pending

servo

运营它的调用地址

mob.js

servo

servo

三个斜杠

指向服务的名称

pending

enable

keepalive

这个servo2

keepalive

without cost

servo2

协议传输类型

plain text

好在这里就完成了挂单服务的调用配置信息

我们可以检查一下

这些属性的话呢都是编解正确

那咱们回到讲习当中

这一讲咱们就完成了

交易服务增加挂单处理接口的调用

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“交易服务”模块的开发教学。核心内容是修改 `GrpcStockDealService` 服务的 `placeOrder` 方法，以支持两种不同类型的订单：市价单（Market Order）和限价单（Limit Order）。视频演示了如何根据订单类型，分别调用不同的业务处理逻辑。对于市价单，直接调用 `stockDealService.processMarketOrder`；对于限价单，则需要先将请求对象转换为限价单请求对象，再调用 `stockPendingServiceBlockingStub.limitPlaceOrder` 方法。整个过程在 IntelliJ IDEA 开发环境中进行，展示了代码编写、类型转换和错误调试的全过程。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 视频开场，展示课程大纲和当前章节“3.3 交易服务增加挂单处理”，并说明需要修改 `GrpcStockDealService` 的 `placeOrder` 方法。
*   **00:05 - 00:15**: 展示 `GrpcStockDealService` 的 `placeOrder` 方法的初始代码框架，其中包含一个 `StreamObserver` 的 `responseObserver` 方法。
*   **00:15 - 00:30**: 开始编写业务逻辑，首先处理市价单。代码中调用 `stockDealService.processMarketOrder` 方法，并将结果封装为 `PlaceOrderResponse`。
*   **00:30 - 00:45**: 开始处理限价单。代码中使用 `LimitPlaceOrderRequest.Builder` 构建请求对象，并调用 `stockPendingServiceBlockingStub.limitPlaceOrder` 方法。
*   **00:45 - 01:00**: 遇到类型不匹配的编译错误。错误提示 `PlaceOrderResponse` 和 `LimitPlaceOrderResponse` 是不同的类型，不能直接赋值。
*   **01:00 - 01:15**: 修正错误。开发者将 `PlaceOrderResponse` 的构建器 `newBuilder()` 方法改为 `LimitPlaceOrderResponse` 的构建器，并正确设置状态和消息。
*   **01:15 - 01:30**: 代码最终完成，成功编译并运行。视频展示了完整的 `placeOrder` 方法，能够根据订单类型分别处理市价单和限价单。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.3 交易服务增加挂单处理”。
    *   **核心目标**: “前面在交易服务实现了市价下单功能，对于市价单和限价单，客户端都是统一下单接口，我们需要修改交易服务的下单接口处理逻辑，增加挂单服务接口的调用：`com.itcast.trade.stock_deal.service.GrpcStockDealService` 实现类”。

*   **关键代码片段**:

    ```java
    @Override
    @Transactional(rollbackFor = Exception.class)
    public void placeOrder(PlaceOrderRequest request, StreamObserver<PlaceOrderResponse> responseObserver) {
        log.info("Process in GrpcStockDealService.placeOrder, request: " + request);
        
        // 市价单处理
        if (request.getType() == GlobalConstants.ORDER_TYPE_MARKET) {
            TradeStockQuoteLast quoteLast = (TradeStockQuoteLast) quoteLastWrapper.get();
            TradeOrder tradeOrder = stockDealService.processMarketOrder(request, quoteLast);
            response = PlaceOrderResponse.newBuilder().setStatus(GlobalConstants.STATUS_OK).setDealId(tradeOrder.getDealId()).build();
        }
        // 限价单处理
        else if (request.getType() == GlobalConstants.ORDER_TYPE_LIMIT) {
            LimitPlaceOrderRequest.Builder orderRequest = LimitPlaceOrderRequest.newBuilder();
            BeanUtils.copyProperties(request, orderRequest);
            LimitPlaceOrderResponse limitPlaceOrderResponse = stockPendingServiceBlockingStub.limitPlaceOrder(orderRequest);
            response = PlaceOrderResponse.newBuilder().setStatus(limitPlaceOrderResponse.getStatus()).setOrderId(limitPlaceOrderResponse.getOrderId()).setMessage(limitPlaceOrderResponse.getMessage()).build();
        }
        
        // 业务异常返回
        catch (ComponentException e) {
            response = PlaceOrderResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).setCode(e.getErrorCode()).setMessage(e.getMessage()).build();
        }
    }
    ```

*   **关键公式 / 图表**:
    *   无公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：代码框架展示 (00:05 - 00:15)**
    *   **描述**: 视频首先展示了 `GrpcStockDealService` 类的 `placeOrder` 方法的代码框架。该方法接收一个 `PlaceOrderRequest` 和一个 `StreamObserver<PlaceOrderResponse>`，并在 `responseObserver` 中处理业务逻辑。这为后续的代码编写提供了上下文。

*   **场景二：市价单逻辑实现 (00:15 - 00:30)**
    *   **描述**: 开发者在 `if` 条件中处理市价单。代码首先获取最新的行情数据 `quoteLast`，然后调用 `stockDealService.processMarketOrder` 方法处理订单，并将返回的 `TradeOrder` 对象的 `dealId` 设置到 `response` 中。这展示了如何处理市价单的业务逻辑。

*   **场景三：限价单逻辑实现 (00:30 - 00:45)**
    *   **描述**: 开发者在 `else if` 条件中处理限价单。代码首先创建一个 `LimitPlaceOrderRequest.Builder`，然后使用 `BeanUtils.copyProperties` 方法将 `PlaceOrderRequest` 中的属性复制到 `LimitPlaceOrderRequest` 中。接着，调用 `stockPendingServiceBlockingStub.limitPlaceOrder` 方法处理限价单，并将返回的 `LimitPlaceOrderResponse` 对象中的状态、订单ID和消息设置到 `response` 中。这展示了如何处理限价单的业务逻辑。

*   **场景四：类型错误与修复 (00:45 - 01:00)**
    *   **描述**: 在尝试将 `LimitPlaceOrderResponse` 赋值给 `PlaceOrderResponse` 时，IDE 报错“不兼容的类型”。开发者意识到 `PlaceOrderResponse` 和 `LimitPlaceOrderResponse` 是不同的类型，不能直接赋值。这揭示了在处理不同类型的订单时，需要使用不同的响应对象。

*   **场景五：错误修复与最终代码 (01:00 - 01:15)**
    *   **描述**: 开发者修正了错误。他将 `PlaceOrderResponse.newBuilder()` 改为 `LimitPlaceOrderResponse.newBuilder()`，并正确设置了状态、订单ID和消息。这展示了如何解决类型不匹配的问题，并确保代码的正确性。

*   **场景六：代码完成与运行 (01:15 - 01:30)**
    *   **描述**: 代码成功编译并运行。视频展示了最终的 `placeOrder` 方法，该方法能够根据订单类型分别处理市价单和限价单。这标志着本节教学内容的完成。
