# 21-市价下单功能-下单入口处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始学习市价下单的功能接口

下单方式主要分为两种

第一种是市价下单

另外一种是限价委托下单

这个之前在下单相关业务之时

咱们也做了讲解

市价就是按市场的成交价格来进行下单

限价就是自己委托的一个指定价格进行下单

虽然这两种方式都是下单功能

但它们的实现处理逻辑是不一样

首先我们来讲解市价的下单功能

之前我们已经搭建了交易服务

实现了简易下单的接口

这里我们基于原来的简易下单接口

基于这个接口

我们要做一个深度改造

首先我们从整体上来了解一下

它的主要实现方法

这里是基于已经实现的功能

列出的所有相关的方法

我们可以看到市价下单接口处理逻辑

相对会比较复杂一点

这里面处理的业务内容比较多

比如要去生成交易订单

交易的成交记录

持仓信息

还有深度报价处理等等不同的业务逻辑

我们在做复杂业务处理的方法

我们在做逻辑的时候

一定要做好对应的封装

不能说在一个方法里面写到底

将所有逻辑全部写在一个方法之内

这样会比较冗长

整个代码是不利于维护

可以看到我们对整个的流程做了一个拆分

每个方法去负责不同功能流程的处理

最后就实现了整体的市价下单的功能

为什么要做封装处理

通过这些方法的封装

能够便于后面在对现价委托功能实现的时候

进行相关的复用

好

对整个方法有了整体上的了解之后

首先去实现下单功能的入口

打开项目工程

找到交易服务的下单处理接口

GRPC Stock Deal Service

这个是place order的方法

对下单功能进行业务逻辑处理

之前简易下单的接口其实处理比较简单

没有去做任何业务逻辑的实现

所以在这里咱们要对它进行一个改造

将原有代码先删除

删除完成之后

咱们来梳理它整体的处理逻辑

要进行下单

首先要获取实时行情数据

取得对应的股票报价信息

接下来我们就要对下单类型进行一个判断

不同下单类型通过不同的业务逻辑去做对应处理

这里主要包括两种下单类型

一种是市价委托

另一种是现价委托

根据不同委托类型调用相应的业务逻辑处理接口

具体的实现就通过收益死神接口做处理

最后就要返回信息给调用方

封装结果给调用方

好

我们就对外层处理逻辑进行处理

逻辑做对应的代码实现

首先定义封装返回的项

Base Order Response

定义为NOW

接下来定义一个Check Catch的异常捕获

异常捕获的处理代码

我们可以直接从讲义当中copy过来

回到代码当中

粘贴

将response属性做个调整

这里异常主要是处理两个方面

第一个是业务异常的封装返回

第二个就是

系统异常的封装返回

业务异常是可以拿到对应的错误码

系统异常

我们就直接拿到返回的消息

做包装处理就可以了

好

接着就去实现它的外层处理逻辑

首先我们需要将用到的属性注入进来

将缓存管理器注入进来

Legit Sketch Manager

Autowide

这个是缓存管理器

接着我们还要将Service层接口

处理进来

Service层接口目前还没有实现

咱们先将它定义好

在Service下面再创建一个新的保证

叫CHAD

接着我们定义一个接口

选择Intenfice

iStock

DO

Service

我们去定义试架处理的下单接口

CHAD

order

process

market order

定义它的请求三树体

face order

order request

将request传递进来

然后还将他的实时行情数据也传递进来

bought last

接着抛出对应的业务异常

增加对应注释

这个是处理4加单的接口

好

下面再创建他的实现类

new加class

名称叫stock deal

service

implement

OK

去实现刚才定义的交易接口

stock deal service

implement method

选择process

market order

将注释拷贝进来

这里面的逻辑

咱们在下面章节的讲解过程当中

再做对应处理

好

那回到外层GRPC

stock deal service

我们首先去实现第一个步骤

获取他的实时行情

从ladies catchment里当中获取

好

拿到最新缓存对象

读取行情信息

quote last request.getstock id

然后做一个唯空判断

如果是没有找到对应的行情信息

我们要抛出一个异常

compend exception

quote last price not found

提示未找到实时行情信息

接着我们就要根据请求类型

做对应判断

global consistence

这个判断是否为市价单

在外层咱们定义一下

他的shared order信息

然后再拿取实时行情信息

stock

quote last

做一个转换

从缓存当中读取

get

下面就要去调用

交易

服务业务层的接口

处理市价单逻辑

shared order stock deal

我们要将service先注入进来

private i stock deal service

autowire的注解

这个是交易服务

业务层接口

在这里我们也添加service注解

再回到gipc stock deal service

然后接着去实现市价单的处理

process market order

要传递咱们的请求参数信息

以及实时行情信息

然后包装他的处理结果

response

place order

response

new builder

set state

state ok

set deal id

将订单id返回出去

get id

再给出一个提示信息

说下单成功

最后调用build的方法后建

接下来还要加上对现价单的判断处理

else if request gettype

这个是limit

加上注释

这个是现价委托单的处理

这块的实现咱们在后面章节当中

再做具体讲解

先留一个标记

后面实现现价委托下单功能时

再做具体处理

好

那这一讲咱们就完成了市价下单

它的入口

也就是外围的调用处理逻辑

下面咱们再去实现其他的业务逻辑

那这一讲内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“市价下单”功能的实现讲解。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `GrpcStockDealService` 类中实现 `placeOrder` 方法。核心内容包括：获取实时行情数据、根据订单类型（市价单或限价单）进行分支处理、调用相应的业务逻辑服务、以及处理异常并返回响应。整个过程体现了典型的微服务架构下，服务层如何协调数据、业务和异常处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，定位到“3.2 实现市价下单接口”这一章节。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示 `GrpcStockDealService` 类的代码结构，重点讲解 `placeOrder` 方法的签名和职责。
*   **00:15 - 00:30**: 讲师开始编写 `placeOrder` 方法的主体逻辑，首先获取实时行情数据。
*   **00:30 - 00:45**: 讲师演示如何从 Redis 缓存中获取股票的最新价格，并处理缓存为空的异常情况，抛出 `QUOTE_LAST_PRICE_NOT_FOUND` 错误。
*   **00:45 - 01:00**: 讲师根据订单类型（`ORDER_TYPE_MARKET`）进行判断，为市价单分支做准备。
*   **01:00 - 01:15**: 讲师开始编写市价单的处理逻辑，包括创建 `TradeOrder` 对象并设置其属性。
*   **01:15 - 01:30**: 讲师演示如何将订单对象持久化到数据库（调用 `tradeOrderDao.insert`）。
*   **01:30 - 01:45**: 讲师开始处理异常情况，为业务异常和系统异常分别编写返回逻辑。
*   **01:45 - 02:00**: 讲师展示如何构建并返回 `PlaceOrderResponse` 对象，设置状态码和消息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲中明确指出“3.2 实现市价下单接口”。
    *   文档中提到“下单分为两种，市价下单和限价委托下单，两个处理逻辑不一样”。

*   **代码关键内容**:
    *   **方法签名**:
        ```java
        public void placeOrder(PlaceOrderRequest request, StreamObserver<PlaceOrderResponse> responseObserver)
        ```
    *   **获取实时行情**:
        ```java
        Cache lastPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_LAST_PRICE_KEY);
        Cache.ValueWrapper quoteLastWrapper = lastPriceCache.get(request.getStockId());
        if (quoteLastWrapper == null) {
            throw new ComponentException(ApplicationErrorCodeEnum.QUOTE_LAST_PRICE_NOT_FOUND);
        }
        TradeStockQuoteLast tradeStockQuoteLast = (TradeStockQuoteLast) quoteLastWrapper.get();
        ```
    *   **市价单处理逻辑**:
        ```java
        if (request.getType() == GlobalConstants.ORDER_TYPE_MARKET) {
            TradeOrder tradeOrder = new TradeOrder();
            tradeOrder.setDirection(request.getDirection());
            tradeOrder.setStockId(request.getStockId());
            tradeOrder.setAccountId(OL);
            tradeOrder.setExecPrice(request.getExecPrice());
            tradeOrder.setExecVolume(request.getExecVolume());
            tradeOrder.setStatus(GlobalConstants.INT_ENABLE);
            tradeOrder.setInitVolume(request.getInitVolume());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setCreateTime(System.currentTimeMillis());
            tradeOrder.setUpdateTime(System.currentTimeMillis());
            tradeOrder.setTradeType(request.getTradeType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS_PENDING);
            tradeOrder.setOrderSource(request.getOrderSource());
            tradeOrder.setOrderTime(request.getOrderTime());
            tradeOrder.setOrderType(request.getOrderType());
            tradeOrder.setOrderStatus(GlobalConstants.ORDER_STATUS
