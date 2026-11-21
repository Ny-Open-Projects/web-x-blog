# 11-限价委托下单-挂单Grpc接口实现流程梳理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们开始实现GRPC限价委托挂单接口

首先咱们将功能实现所需要用到的属性

以及辅助方法做一个copy

回到工程当中

在pending的工程下面

咱们去创建一个GRPC接口的实现

new delcast grpc stock pending service

它要去继承GRPC的限价委托挂单接口

service grpc implement base

adalt insert重写限价委托接口

咱们将讲义当中的代码copy进来

上面增加GRPC的注解

GRPC service增加日志查检注解

修正相关的错误

导入对应的包

在split framework下面

这里面用到了VO对象

这个VO对象里面

主要是定义下单相关的请求参数信息

咱们就直接从已经实现的原码当中copy过来

放在VO的包下面

回到刚才的GRPC的service

再导入complete接口

在util包下面

好

必要的属性以及辅助方法

copy进来之后

咱们就来侧重核心逻辑的讲解实现

添加对应注释

这里是限价下单接口的处理

那咱们来看一下整体逻辑是该如何去实现的

首先咱们定义接口的返回对象

这个是限价下单的返回对象

case order response

接下来我们去定义外围异常的补货

开catch

catch异常的处理

在这里咱们就不足以去敲选

从讲义当中直接copy进来

接下来我们就来定义外围异常的补货

这里主要是包括两部分异常

一个是业务异常的处理

另外就是系统异常的工庄返回

好

再回到咱们的主逻辑

第一步咱们要根据股票ID

获取实时行情的报价信息

定义trader quote last

实时行情对象

通过stock trader pending service

业务层接口去获取对应信息

那咱们定义一个业务层接口方法

我们来定义一个业务层接口方法

stock quote last

传递股票ID

get stock ID

对这个方法做个实现

edit enter回车键

create method

添加对应的注释

这个是获取股票产品的最新报价信息

在这里要抛出对应的业务异常

compound exception

接着我们在实现类当中做具体的实现

edit enter

将注释添加过来

这里我们先要去定义款存的管理器

ladies

ladies catch manager

将它注入进来

autowide

这个是ladies款存管理器

接下来我们就做具体的实现

从款存当中

获取对应数据

catch

last price

catch

ladies catch manager

get catch

global constituents

传递key值

stock quote last price key

然后获取缓存存储的对象

quote

last

rep

从last price catch里面获取

传递stock ID

然后做一个唯空判断

如果缓存对象唯空

没有获取到

最新的报价信息

我们就要抛出业务异常

这里给它一个异常错误码

quote last price not found

没有找到

接下来就返回款存对象信息

quote last

做一个强转

将结果返回

好

再回到跨单GRBC接口的主逻辑

咱们再梳理一下

下面的处理实现流程

第二步呢

就要去创建

委托挂单的

请求参数对象

这个呢

是一个vr的参数对象

接下来

我们要将GRBC

接口的参数信息

复制到vr对象当中

接着话呢

我们就要去调用挂单的服务接口

调用挂单服务接口

去创建

保存订单信息

然后呢

这里的目的

是要做持久化

记录订单的信息

第五步呢

咱们要将数据放入款存对象当中

等待订单的撮合处理

好

这些呢

就是限价下单接口的

整体处理流程

这个接口主要是做两件事情

第一是要持久化保存订单信息

第二就是将下单请

第二就是将下单请求信息

放入款存对列当中

接着咱们再去实现service层的必要接口

就是创建保存订单的方法

咱们定一个新的接口

public

trader order

grade

trader order

传递下单请求参数信息

request vr

将vr对象传送进来

抛出可能出现的业务异常

添加注释

这个是创建交易项目的方法

我们再去看看这个交易订单记录

那咱们再将必要的数据层接口注入进来

咱们要去查询股票信息

要注入股票的数据层接口

hsstock.io

添加注释

这个是股票产品的数据层接口

接下来咱们再去添加交易账号的数据层接口

添加注解普通外的

加上注释

这个是交易账户的数据层接口

最后要添加订单的数据层接口

卖位的iChat

我的DLO注入进来

这个是交易订单的数据层接口

好再回到刚才的创建订单的接口

我们来整理下具体实现步骤

第一步是要创建订单对象

第二步

咱们要组装

并拢于股票信息

第三步要组装

冗余账户编号信息

第四步要组装订单的下单信息

接下来就要保存

订单数据

至数据库当中

最后我们要返回新生成的订单ID

返回

新生成的

订单ID

这个就是创建交易订单的整体实现步骤

好在这里呢咱们对GRBC

限价下单接口的流程

做了一个梳理

同时也整理了

订单保存接口的处理步骤

下一讲咱们再做具体的实现

那这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“挂单服务”的开发与实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何构建一个基于 gRPC 的服务，该服务负责处理用户的挂单请求。核心内容包括：
- **服务定义**：创建并实现一个 gRPC 服务接口 `IStockTradePendingService`。
- **数据结构**：使用 Protocol Buffers (protobuf) 定义请求和响应的数据结构。
- **服务实现**：在 `StockTradePendingServiceImpl` 类中，实现具体的业务逻辑，包括获取股票最新报价、创建订单对象、调用订单服务等。
- **技术栈**：主要使用 Java、Spring Boot、gRPC、Redis（用于缓存）和 MyBatis（用于数据访问）。
- **异常处理**：对业务异常和系统异常进行区分处理，并返回相应的错误码。

整个过程展示了从接口定义、服务实现到核心业务逻辑的完整开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程目标与步骤介绍。讲师在大纲中展示了本节的主要内容，包括定义接口数据结构、提供 gRPC 挂单接口、行情监听处理、挂单撮合交易处理、挂单队列并发锁验证、交易服务增加挂单处理以及功能验证。

*   **00:16 - 00:30**：定义 gRPC 服务接口。讲师在 `IStockTradePendingService` 接口中定义了 `getTradeStockQuoteLast` 方法，用于获取股票的最新报价。

*   **00:31 - 00:45**：实现服务接口。讲师创建了 `StockTradePendingServiceImpl` 类，并实现了 `getTradeStockQuoteLast` 方法。

*   **00:46 - 01:00**：实现获取股票报价逻辑。讲师在 `getTradeStockQuoteLast` 方法中，通过 `redisCacheManager` 从缓存中获取股票的最新报价。

*   **01:01 - 01:15**：实现创建订单对象。讲师在 `createTradeOrder` 方法中，将请求参数转换为 gRPC 的订单对象。

*   **01:16 - 01:30**：实现调用订单服务。讲师在 `limitPlaceOrder` 方法中，调用 `stockTradePendingService` 的 `getTradeStockQuoteLast` 方法获取报价，并创建订单对象。

*   **01:31 - 01:45**：实现异常处理。讲师在 `limitPlaceOrder` 方法中，对业务异常和系统异常进行区分处理，并返回相应的错误码。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 大纲**：
    *   **目标**：定义接口数据结构、提供 gRPC 挂单接口、行情监听处理、挂单撮合交易处理、挂单队列并发锁验证、交易服务增加挂单处理、功能验证。
    *   **步骤**：定义接口数据结构、提供 gRPC 挂单接口、行情监听处理、挂单撮合交易处理、挂单队列并发锁验证、交易服务增加挂单处理、功能验证。

*   **代码**：
    *   **gRPC 服务接口**：
        ```java
        public interface IStockTradePendingService {
            TradeStockQuoteLast getTradeStockQuoteLast(long stockId) throws ComponentException;
        }
        ```
    *   **服务实现类**：
        ```java
        public class StockTradePendingServiceImpl implements IStockTradePendingService {
            @Autowired
            private RedisCacheManager redisCacheManager;
            
            @Override
            public TradeStockQuoteLast getTradeStockQuoteLast(long stockId) throws ComponentException {
                Cache lastPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_LAST_PRICE_KEY);
                if (null == quoteLastWrapper) {
                    throw new ComponentException(ApplicationErrorCodeEnum.QUOTE_LAST_PRICE_NOT_FOUND);
                }
                TradeStockQuoteLast quoteLast = (TradeStockQuoteLast) quoteLastWrapper.get();
                return null;
            }
        }
        ```
    *   **挂单处理方法**：
        ```java
        @Override
        public void limitPlaceOrder(LimitPlaceOrderRequest request, StreamObserver<LimitPlaceOrderResponse> responseObserver) {
            TradeStockQuoteLast stockQuoteLast = stockTradePendingService.getTradeStockQuoteLast(request.getStockId());
            LimitPlaceOrderResponse response = null;
            try {
                // 1. 根据股票ID，获取实时行情的最新报价信息
                // 2. 创建挂单接口的请求VO参数对象
                // 3. 调用挂单服务接口，创建保存订单信息
                // 4. 放入缓存队列，等待订单的撮合处理
            } catch (ComponentException e) {
                log.error(e.getMessage(), e);
                response = LimitPlaceOrderResponse.newBuilder().setStatusCode(GlobalConstants.STATUS_ERROR).build();
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                response = LimitPlaceOrderResponse.newBuilder().setStatusCode(GlobalConstants.STATUS_ERROR).build();
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：定义 gRPC 服务接口**（00:16 - 00:30）
    *   讲师在 IDE 中创建了 `IStockTradePendingService` 接口，并定义了 `getTradeStockQuoteLast` 方法，用于获取股票的最新报价。

*   **场景二：实现服务接口**（00:31 - 00:45）
    *   讲师创建了 `StockTradePendingServiceImpl` 类，并实现了 `getTradeStockQuoteLast` 方法。

*   **场景三：实现获取股票报价逻辑**（00:46 - 01:00）
    *   讲师在 `getTradeStockQuoteLast` 方法中，通过 `redisCacheManager` 从缓存中获取股票的最新报价。

*   **场景四：实现创建订单对象**（01:01 - 01:15）
    *   讲师在 `createTradeOrder` 方法中，将请求参数转换为 gRPC 的订单对象。

*   **场景五：实现调用订单服务**（01:16 - 01:30）
    *   讲师在 `limitPlaceOrder` 方法中，调用 `stockTradePendingService` 的 `getTradeStockQuoteLast` 方法获取报价，并创建订单对象。

*   **场景六：实现异常处理**（01:31 - 01:45）
    *   讲师在 `limitPlaceOrder` 方法中，对业务异常和系统异常进行区分处理，并返回相应的错误码。
