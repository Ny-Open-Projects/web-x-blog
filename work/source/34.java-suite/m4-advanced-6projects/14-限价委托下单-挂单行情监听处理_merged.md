# 14-限价委托下单-挂单行情监听处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现委托挂单的处理逻辑

之前咱们梳理了整体的实现步骤流程

这里咱们就来做具体实现

咱们回到service实现类当中

去实现创建保存订单信息的接口

首先咱们定义chadorder对象

new chadorder

接着设置订单的基本信息

买卖方向

request

get direction

再设置股票ID

request get stock ID

然后设置交易账户的ID

接着咱们组装冗余股票信息

首先咱们要查出股票的完整信息

chadstock

通过chadstock.io

获取股票对象

get stock ID

对股票信息做一个唯空判断

如果不唯空

咱们就将信息设置到订单当中

设置股票的编号

chadstock

get code

下面设置股票的名称

set stock name

chadstock

获取股票名称

下面就要去组装冗余账户的编号信息

同样我们要找到账户的完整信息

通过chadstock.io

去获取具体的对象

去获取具体的对象

去获取具体的对象

传递交易账号ID

同样做一个唯空判断

如果不唯空

咱们就将交易账号的ID设置到订单信息当中

get account

get account number

接着咱们去组装订单的完整下单信息

set request price

将价格设置进去

get excuse price

设置执行价

因为在这里只是创建订单信息

还没有进行撮合处理

所以它的默认成交价在这里设为0就可以

然后设置它的成交数量

同样也设为0

接着设置订单的状态

这个时候的订单是处于未成交的状态

等待成交

order stays wait

然后设置订单的类型

再设置它的初始发数量

设置成交时间

在这里咱们就将当前的服务器时间设置进去就可以

保留进来

接着要保存订单至数据库当中

share order do

insert的方法

最后咱们要返回订单ID

通过request VOR对象做传递

将订单ID设置进去

然后咱们再返回订单对象

return order

在request的VOR对象当中去记录订单ID

是便于后面对列撮合匹配处理

咱们再回到GRPC接口的处理逻辑

这里咱们要定义委托挂单的VOR参数对象

new limit

然后咱们通过binutils工具将对象属性做一个复制

copy properties

从request的对象当中

将它复制到VOR的参数对象当中

接着咱们去调用服务层的创建订单接口

这里咱们将刚才创建订单的接口抽取出来

右键

然后我们再去创建订单接口

reflect

for members of

选中刚才创建订单接口

reflect的

好这样就已经抽取完成

咱们再回到GRPC的接口处理逻辑

在这里面调用创建订单的接口

传递VOR value object对象

接下来咱们就要将订单数据放入到缓存对列当中

首先我们定义一个cache key

定义它的简坠

global consistence

stock

因为每个挂单服务有自己的缓存对列

在这里咱们就通过服务的端口作为区分

这个是servo port

咱们将名称改一下

add shift加R给它重命名

servo port

再拿取缓存对象

cache manager

get cache

传递刚才的key值

然后咱们对缓存做个围攻判断

get cache

再通过股票ID去获取对应的缓存信息

在这里缓存是根据股票产品ID进行的分组

咱们来画一下

每个订单服务有自己的缓存对列

比如这里是挂单服务A

这里是挂单服务B

他们会将下单信息存储至ladies缓存当中

那么在这里咱们就根据股票产品ID做对应的分组

也就在这里

我们就把这个缓存信息存储到Ladies缓存当中

根据股票产品ID

比如说是中国平安

这里面是工商银行

那么挂单服务会将接收的订单请求数据

按照不同的股票产品ID进行分组

比如说在这里有不同的请求

每个请求它要交易的股票产品ID是不一样的

那么在这里就会将相同的股票产品下单的请求数据

汇总在一起

然后放置中国平安的购买单

这个对列当中

将工商银行的订单请求信息放置工商银行的对列当中

好

这一块是挂单对列的存放处理逻辑

那咱们回到代码当中

如果是缓存当中

已经存在股票产品的委托下单数据

那就将它们放置相同的对列当中

定义历史的集合去存储这些订单信息

这里做一个强转

转换为集合

然后过去反存对象

这个时候新来的订单

就要对原有的订单数据做一个重新的顺序排列

因为新来的订单要按照请求价格

按照请求时间做重新的排列

这样呢

就形成了新的档位盘口信息

好

那咱们回到代码当中

按照价格优先

时间优先的原则

重新排列下单数据

这里为了防止排序的时候出现空指针异常

咱们去做一个转换处理

将它的成交价格默认了设为零

也就是围空的情况下面

自动会给它默认设为零

这样就可以防止重新排序的时候出现空指针异常

同样成交时间要做围空判断总换

get excuse time

将时间设为当前时间

excuse time system.clientTimeMails

这个呢是毫秒

接着咱们就将新的订单放置集合当中

接下来咱们还去判断

如果它不存在于缓存当中

我们就要将当前请求数据放入缓存

创建一个list的集合

limit

request viewer

place

定义list的对象

是一个alien list

将订单请求放入至集合当中

page

put

传递stock id

按照股票产品的设定

将厂品做分组

在这里咱们也要去更新缓存

它在更新之前先要做一个排序整理

也就根据价格优先

时间优先的处理规则

重新做一个排序

sort

base order

再用这个方法做对应的处理

传递集合对象

最后就是更新缓存

page

put

这个stock id

将list的对象传入集合当中

这里面排序处理的方法

咱们稍后再做讲解

最后要返回来

response对象给客户端

这里面states要调整一下

global

consistence

states ok

message的话呢

就是挂单处理成功

最后咱们还去返回订单的id

给调用房

place

order request viewer

get order id

回车

好在这里呢

就是GRPC挂单接口的处理方法

最后呢

还将数据输出给调用房

on next

返回response

最后调用on complete的方法

完成整个接口的处理

好

这一讲就是对GRPC挂单接口的逻辑实现

那这一讲内容

咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“限价下单”功能的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `GrpcStockPendingService` 服务中处理一个 gRPC 接口请求。核心流程包括：接收客户端请求、获取实时行情、将 gRPC 参数复制到内部 VO 对象、调用持久化服务创建订单、将订单信息存入缓存队列（用于后续处理），并最终返回响应。代码中大量使用了 Spring Boot 的注解、DAO 层操作、以及自定义的常量和缓存机制。讲师还展示了如何通过 `@Value` 注解注入配置，并使用 `Stream` API 对订单列表进行排序。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示 `GrpcStockPendingService` 类中的 `limitPlaceOrder` 方法，这是整个功能的入口。
*   **00:00:05 - 00:00:15**：讲师解释方法签名，指出这是一个 gRPC 服务方法，接收 `LimitPlaceOrderRequest` 并返回 `StreamObserver<LimitPlaceOrderResponse>`。
*   **00:00:15 - 00:00:30**：讲师开始讲解方法内部逻辑，首先根据股票 ID 获取实时行情。
*   **00:00:30 - 00:00:45**：讲师展示如何将 gRPC 接口的参数值复制到内部的 `LimitPlaceOrderRequestVo` 对象中，使用了 `BeanUtils.copyProperties` 方法。
*   **00:00:45 - 00:01:00**：讲师调用 `stockTradePendingService.createTradeOrder` 方法来创建订单。
*   **00:01:00 - 00:01:15**：讲师进入 `createTradeOrder` 方法，展示如何创建 `TradeOrder` 对象并设置其属性，包括方向、股票 ID、账户 ID、股票信息和账户信息。
*   **00:01:15 - 00:01:30**：讲师展示如何通过 DAO 层获取股票和账户的详细信息，并设置到订单对象中。
*   **00:01:30 - 00:01:45**：讲师设置订单的执行价格和状态，状态为 `ORDER_STATUS_WAIT`。
*   **00:01:45 - 00:02:00**：讲师调用 `tradeOrderDao.createTradeOrder` 方法将订单持久化到数据库。
*   **00:02:00 - 00:02:15**：讲师返回一个 `TradeOrder` 对象，表示订单创建成功。
*   **00:02:15 - 00:02:30**：讲师回到 `limitPlaceOrder` 方法，展示如何将订单信息放入缓存队列。
*   **00:02:30 - 00:02:45**：讲师展示如何根据股票 ID 从缓存中获取订单列表，并进行排序。
*   **00:02:45 - 00:03:00**：讲师展示如何将排序后的订单列表存入缓存，并返回成功响应。
*   **00:03:00 - 00:03:15**：讲师展示如何处理异常情况，包括业务异常和系统异常，并返回相应的错误响应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：
    *   **gRPC 服务方法**：
        ```java
        @Override
        public void limitPlaceOrder(LimitPlaceOrderRequest request, StreamObserver<LimitPlaceOrderResponse> responseObserver) {
            // 1. 根据股票ID，获取实时行情报价信息
            TradeStockQuoteLast stockQuoteLast = stockTradePendingService.getTradeStockQuoteLast(request.getStockId());
            // 2. 创建委托单的请求VO参数对象
            LimitPlaceOrderRequestVo placeOrderRequestVo = new LimitPlaceOrderRequestVo();
            // 3. 将gRPC接口的参数值复制到VO对象中
            BeanUtils.copyProperties(request, placeOrderRequestVo);
            // 4. 调用挂单服务接口，创建保存订单信息
            stockTradePendingService.createTradeOrder(placeOrderRequestVo);
            // 5. 放入缓存队列，等待订单的撮合处理
            String cacheKey = GlobalConstants.STOCK_PENDING_LIMIT_ORDER + "_" + serverPort;
            Cache cache = cacheManager.getCache(cacheKey);
            List<LimitPlaceOrderRequestVo> placeOrderRequestVoList = (List<LimitPlaceOrderRequestVo>) cache.get(request.getStockId());
            if (null == placeOrderRequestVoList) {
                placeOrderRequestVoList = new ArrayList<>();
                cache.put(request.getStockId(), placeOrderRequestVoList);
            }
            placeOrderRequestVoList.add(placeOrderRequestVo);
            // 6. 返回成功响应
            responseObserver.onNext(LimitPlaceOrderResponse.newBuilder().setOrderId(placeOrderRequestVo.getOrderId()).build());
            responseObserver.onCompleted();
        }
        ```
    *   **创建订单方法**：
        ```java
        public TradeOrder createTradeOrder(LimitPlaceOrderRequestVo requestVo) throws ComponentException {
            TradeOrder order = new TradeOrder();
            order.setDirection(requestVo.getDirection());
            order.setStockId(requestVo.getStockId());
            order.setAccountId(requestVo.getAccountId());
            // 2. 组装元素股票信息
            TradeStock tradeStock = tradeStockDao.getById(requestVo.getStockId());
            if (null != tradeStock) {
                order.setStockCode(tradeStock.getCode());
                order.setStockName(tradeStock.getName());
            }
            // 3. 组装元素账户编号信息
            TradeAccount tradeAccount = tradeAccountDao.getById(requestVo.getAccountId());
            if (null != tradeAccount) {
                order.setAccountNo(tradeAccount.getAccountNo());
            }
            // 4. 组装订单的下单信息
            order.setRequestPrice(requestVo.getExecPrice());
            order.setExecVolume(0);
            order.setStatus(GlobalConstants.ORDER_STATUS_WAIT);
            // 5. 保存订单至数据库中
            tradeOrderDao.createTradeOrder(order);
            // 6. 返回新生成的订单ID
            return order;
        }
        ```
    *   **缓存排序逻辑**：
        ```java
        private static List<LimitPlaceOrderRequestVo> sortPlaceOrderRequestVoList(List<LimitPlaceOrderRequestVo> placeOrderRequestVoList) {
            return placeOrderRequestVoList.stream().sorted(Comparator.comparing(LimitPlaceOrderRequestVo::getExecTime).reversed()).collect(Collectors.toList());
        }
        ```
*   **关键常量**：
    *   `GlobalConstants.STOCK_PENDING_LIMIT_ORDER`：缓存的前缀。
    *   `GlobalConstants.ORDER_STATUS_WAIT`：订单的等待状态。
    *   `GlobalConstants.ORDER_STATUS_OK`：订单处理成功的状态。
    *   `GlobalConstants.ORDER_STATUS_ERROR`：订单处理失败的状态。
*   **关键注解**：
    *   `@Value("${server.port}")`：从配置文件中注入服务器端口。
    *   `@Component`：将类标记为 Spring 组件。
    *   `@Transactional`：用于数据库事务管理（在 `createTradeOrder` 方法中）。
*   **关键类和接口**：
    *   `TradeOrder`：订单实体类。
    *   `TradeStock`：股票实体类。
    *   `TradeAccount`：账户实体类。
    *   `TradeStockDao`、`TradeAccountDao`、`TradeOrderDao`：数据访问对象。
    *   `CacheManager`：缓存管理器。
    *   `LimitPlaceOrderRequest`、`LimitPlaceOrderRequestVo`、`LimitPlaceOrderResponse`：gRPC 请求/响应对象和内部 VO 对象。

---

### 4) 关键场景与演示描述

*   **场景一：gRPC 服务入口** (00:00:00-00:00:15)
    *   讲师在 IDE 中打开 `GrpcStockPendingService` 类，聚焦于 `limitPlaceOrder` 方法。
    *   讲师解释该方法是处理客户端限价下单请求的入口，它接收一个请求对象和一个响应观察者。
*   **场景二：获取行情与参数复制** (00:00:15-00:00:45)
    *   讲师调用 `stockTradePendingService.getTradeStockQuoteLast` 方法获取实时行情。
    *   讲师创建一个 `LimitPlaceOrderRequestVo` 对象，并使用 `BeanUtils.copyProperties` 方法将 gRPC 请求中的参数复制到 VO 中，以便后续处理。
*   **场景三：创建并持久化订单** (00:00:45-00:01:30)
