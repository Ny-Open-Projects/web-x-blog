# 13-限价委托下单-挂单Grpc接口重排功能自测 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们开始实现行情监听功能的处理

挂单服务是订阅了行情数据

每接收到一口行情数据报价

都要检测挂单对立

然后咱们去撮合

是否有匹配成交条件的订单

这个在之前讲解挂单处理流程当中

也做了介绍

行情监听结构

要去根据实时行情

检测挂单对立当中

是否有匹配成交的订单

好

接着咱们就从代码层面

来做一个具体实现

回到工程当中

打开Pending for the Consume

这个实现内

首先咱们梳理一下

整体的处理流程

第一步

要增加锁的控制处理

根据股票产品ID

进行加锁控制

同时我们要减少锁的控制地度

提升锁的控制地度

提升处理性能

也要保障并发现成锁

他们锁定的对象是一致的

如果你锁的是一个值

这个并不能真正生效

只有锁定对象

传递的是对象的引用地址

这个锁才能真正控制生效

接下来第二步

要获取挂单的反存兑电信息

第三步

根据

股票ID

获取对应的挂单兑电数据

第四步

我们要定义一个变量

标识挂单兑电

是否发生了变化和修改

这个是用于控制反存的更新

如果变化

需要更新反存

第五个步骤

要去便利挂单

反存兑电

根据

实时行情

要去拖和匹配

需成交的定单

最后

就是反存的

判断

更新处理

这个是挂单反存数据

这个是整体的处理流程

那咱们就来做具体实现

首先打印日志信息

log.info

process

copy 掌权内名

ECU info的方法

message

将参数打印出来

port last message

接着咱们通过现成词去执行

整个业务逻辑

execute

提供ronnable接口

将内部逻辑copy进来

我们在内层做个实现

为了提升处理速度

加入

现成词处理

但同时呢

也要

保障

现成安全

在操作修改缓存的时候特别要注意

因为外层咱们加了锁的控制

所以在内部的话

咱们是可以去直接修改缓存的

作为一步现成处理

咱们要注意

外围异常的补货

h

exception

将异常补货打印

将处理步骤copy进去

首先咱们实现第一步

根据股票产品ID

进行加锁的控制

外围通过signalize的关键字

定义一个getlog的方法

传递

股票产品ID

让咱们来实现getlog方法

edit加enter

修改它的返回值

static

log

为什么会采用static

因为在这里咱们用到的锁

它是一个静态存储对象

静态对象

会常住在内存当中

这样锁的话呢

就不是锁它的值

而是锁它的对象

那首先咱们做一个唯空判断

lock keys

传递stock ID

如果这个锁不存在

咱们要加入进去

stock ID

就将股票ID传递进去作为对象锁

然后返回

lock keys

getstock ID

添加对应的注释

根据

不同股票产品

获取

对象锁

好再回到刚才的处理逻辑

将处理步骤copy进去

接下来去获取挂断的

返存堆叠信息

定义ghp

globalconsistence

加上售后port

服务端口

获取返存对象

通过ghmanage

传递ghkey

做一个唯空判断

接下来要获取挂单堆叠的返存

stock kh

gh

get

传递股票ID

然后做一个唯空判断

stock kh

将下面的步骤copy进来

在这里要拿到

挂单的返存堆叠

做一个强转

接下来再去定义一个

标识变量

然后我们要去便利挂单的返存堆叠

通过迭代器做对应的便利处理

itil later

limit

base order request view

itil等于

base

做迭代处理

下面就是挂单的

撮合比配的处理逻辑

外围加上check cache异常补货

将异常打印出来

这里check cache的目的是

某个挂单

如果是出现问题

不能阻塞

后面的

挂单运行

那咱们看一下如何去便利处理呢

首先在这里要去获取

挂单数据

limit

request view

order

id.next

接着

判断

挂单数据是否

符合当前的

行情价格

calling

match price

stock

shared

pending service

通过service层去判断处理

咱们先定一个方法

match price

传递

订单的买卖方向

再传递它的请求执行价格

接着就要传递实时行情数据

这个方法咱们在下面再做具体讲解

然后做一个判断

这里就是

符合当前价格

那么就要去生成

订单

成交信息

这里咱们也要用

service的方法做对应的处理

这和之前在交易服务里面实现的4加单

成交处理逻辑就基本上是一致的

因为在这里它已经符合当前价格

所以可以直接去匹配

生成订单成交信息

marked

order

传递订单信息

传递实时行情数据

处理完成之后咱们还去判断

它内部的成交数量

如果成交数量等于0

说明了这个订单已经是完全成交

订单

完全成交

我们要从缓存当中

清除

挂单数据

将迭代的数据删除

将挂单对列的修改标记标识维修

最后咱们还要去更新挂单缓存的对列数据

例如

list list change

我的last message

传递铺配ID

将list的对列重新设置进去

因为这个list的对列已经将之前完全成交的缓存给清除了

所以在这里放入缓存的就是最新的挂单对列数据

好这一块就是行情监听挂单对列的处理逻辑

那么内部的挂单数据价格的匹配判断

以及订单成交信息生成的处理逻辑

这些是放在业务层去做实现

在下面章节咱们再做具体讲解

好那这一讲内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“挂单服务”的技术实现讲解。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `PendingQuoteConsumer` 类中处理实时行情数据，以匹配并撮合用户的挂单。核心内容包括：使用 `@StreamListener` 监听行情消息、通过 `ConcurrentHashMap` 实现股票ID的分布式锁、利用 Redis 缓存存储挂单数据、遍历缓存队列进行匹配，并在匹配成功后调用服务处理成交。整个过程强调了高并发下的线程安全和性能优化。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：开场，展示课程大纲，定位到“3.2 挂单服务限价委托接口”章节。
*   **00:00:05 - 00:00:15**：讲师讲解挂单服务的核心逻辑，即“按价格最优优先，其次时间优先”的撮合原则，并强调单元测试的重要性。
*   **00:00:15 - 00:00:30**：进入“3. 行情监听处理”章节，展示 `PendingQuoteConsumer` 类的代码结构。
*   **00:00:30 - 00:00:45**：讲解 `@StreamListener` 注解用于监听行情数据，并介绍 `taskExecutor.execute()` 用于异步处理以提升性能。
*   **00:00:45 - 00:01:00**：演示如何为 `ConcurrentHashMap` 添加锁，以实现股票ID的分布式锁控制。
*   **00:01:00 - 00:01:15**：展示如何根据股票ID获取缓存键，并从 Redis 中获取对应的挂单队列数据。
*   **00:01:15 - 00:01:30**：演示遍历挂单队列，对每个挂单进行价格匹配。
*   **00:01:30 - 00:01:45**：讲解匹配成功后的处理逻辑，包括调用 `processMarketOrder` 方法和从缓存中移除订单。
*   **00:01:45 - 00:02:00**：总结整个处理流程，强调线程安全和性能优化。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **代码关键内容**

*   **类定义与注解**：
    ```java
    @Autowired
    private IStockTradePendingService stockTradePendingService;
    ```

*   **行情监听方法**：
    ```java
    @StreamListener("quote")
    public void receiveInput(@Payload TradeStockQuoteLast quoteLastMsg) {
        Log info("Process in PendingQuoteConsumer.receiveInput method, quoteLastMsg: " + quoteLastMsg);
        taskExecutor.execute(() -> {
            // 处理逻辑
        });
    }
    ```

*   **分布式锁实现**：
    ```java
    private static Long getLock(Long stockId) {
        if (null == lockKeys.get(stockId)) {
            lockKeys.put(stockId, stockId);
        }
        return lockKeys.get(stockId);
    }
    ```

*   **Redis 缓存与数据处理**：
    ```java
    String cacheKey = GlobalConstants.STOCK_PENDING_LIMIT_ORDER + "_" + serverPort;
    ValueWrapper stockCache = cache.get(cacheKey);
    List<LimitPlaceOrderRequestVo> placeOrderRequestVoList = (List<LimitPlaceOrderRequestVo>) stockCache.get();
    ```

*   **订单匹配与处理**：
    ```java
    for (Iterator<LimitPlaceOrderRequestVo> itr = placeOrderRequestVoList.iterator(); itr.hasNext(); ) {
        LimitPlaceOrderRequestVo placeOrder = itr.next();
        boolean matchPrice = stockTradePendingService.checkMatchPrice(placeOrder, quoteLastMsg);
        if (matchPrice) {
            stockTradePendingService.processMarketOrder(placeOrder, quoteLastMsg);
            if (placeOrder.getExecVolume() == 0) {
                itr.remove();
            }
        }
    }
    ```

#### **图表/公式**

*   **无公式或图表**：视频中未出现任何数学公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：代码结构展示**（00:00:00-00:00:15）
    *   讲师首先展示了课程大纲，定位到“3.2 挂单服务限价委托接口”。
    *   他解释了挂单服务的核心逻辑是“按价格最优优先，其次时间优先”，并强调了单元测试的重要性。

*   **场景二：行情监听与异步处理**（00:00:15-00:00:45）
    *   讲师在 `PendingQuoteConsumer` 类中，展示了 `@StreamListener("quote")` 注解用于监听行情数据。
    *   他演示了如何使用 `taskExecutor.execute()` 将处理逻辑放入线程池，以提升处理性能并保证线程安全。

*   **场景三：分布式锁实现**（00:00:45-00:01:00）
    *   讲师在代码中添加了 `ConcurrentHashMap` 用于存储股票ID和锁。
    *   他演示了 `getLock` 方法，通过 `putIfAbsent` 方法实现分布式锁，确保同一股票ID的处理是串行的。

*   **场景四：Redis 缓存与数据处理**（00:01:00-00:01:30）
    *   讲师展示了如何根据股票ID生成缓存键，并从 Redis 中获取对应的挂单队列数据。
    *   他演示了如何将缓存数据转换为 `List<LimitPlaceOrderRequestVo>`，以便后续遍历处理。

*   **场景五：订单匹配与成交处理**（00:01:30-00:02:00）
    *   讲师演示了如何遍历挂单队列，对每个挂单进行价格匹配。
    *   他展示了匹配成功后的处理逻辑，包括调用 `processMarketOrder` 方法和从缓存中移除订单。
    *   最后，他总结了整个处理流程，强调了线程安全和性能优化的重要性。

---

以上是根据视频画面内容整理的结构化分析。
