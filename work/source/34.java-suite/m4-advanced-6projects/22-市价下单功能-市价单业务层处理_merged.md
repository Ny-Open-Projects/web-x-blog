# 22-市价下单功能-市价单业务层处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始去实现处理试价单的实现逻辑

咱们回到代码,打开StockDeal Service Implement

首先咱们梳理一下整体实现处理流程

第一步,首先要获取交易账户信息

接着咱们再拿到股票产品信息

然后就可以去生成成交记录

接着就要去生成持仓信息

成交记录和持仓信息处理完成之后

接下来就是去保存订单信息

第六步,保存持仓记录

注意它们的实现顺序

这些记录是存在关联关系

成交记录和持仓和订单

这些都有关联关系

所以是要先生成成交记录,然后就是持仓

接着就是保存订单信息

保存完持仓记录之后

最后就是保存成交记录

这里的成交记录生成并非去保存成交记录

而是将成交记录信息

组装完成

最后才是去保存成交记录

因为在这里呢

我们要去记录订单的ID和持仓

仓位的ID信息

所以先要保存订单

然后保存持仓

最后才是保存成交记录

为了节省大家时间

咱们将必要的属性以及周边的辅助功能方法先copy进来

copy完成之后

咱们再去侧重主逻辑的讲解

理解计划

你实现

放置上面啊

咱们看一下他主要的一些属性接口

这里注入的属性主要是数据层接口

还有咱们的缓存管理器

注意神借口包括交易相关一些对象的数据接口

比如时长记录交易记录交易订单

下面的提供了一些辅助方法

这里是深度报价的转换处理

然后是订单状态

的计算

这个log插件了

咱们加入进去

log project2

这里面是订单状态的计算和转换

这些方法在咱们去完成主逻辑实现的时候还会做讲解介绍

好

那咱们回到处理试价单的主逻辑

首先咱们要去获取交易账号

share account

get by id

这个是get by id

根据交易账号id获取交易账号id

获取交易账号对象信息

我们可以看下这个数据层接口的实现

在这里它增加了缓存功能的处理

为了提升账号信息的获取速度

好

再回到咱们刚才的处理逻辑

接下来就要去实现获取股票产品信息

get stock

通过dao

根据id获取

传递股票产品id

然后是生成成交记录

生成完成

要去将成交记录返回出来

要定义一个方法做对应的处理实现

传递对应的参数信息

port last

request 参数信息

share account 交易账户

以及股票产品

咱们先将方法定义在这里

下面再做具体实现

注意这里面的处理逻辑

只是生成share deal的对象信息

方法是这样的

方法是这样的

方法是这样的

方法是这样的

方法内部是不会去保存成交记录的

成交记录是在下面会做保存处理

接下来咱们去生成持商信息

share position

制定一个新的方法做对应的实现

get data position

传递成交记录

请求参数

share account 交易账户

以及股票产品

这个方法咱们先定义在这里

接下来我们就去保存订单信息

我们先去保存订单信息

credit order

generate

credit order

在这个方法里面去实现订单信息的保存

为了便于大家的理解

我们在这里就不采用generate

直接采用save

因为方法内部的话

是要去实现订单信息的保存

这两个方法只是生成相应的对象

保存订单的方法要传递对应参数

credit deal

request

credit counter

股票产品

最后就是保存持仓记录

c5 position

share position

将持仓信息传递进来

因为这里已经生成了持仓对象

所以我们只要在这里

直接调用保存方法去做对应处理就可以

最后就是要保存成交记录信息

share deal

我们要去设置它的订单ID

share order get id

share deal

share position id

将持仓记录ID也设置进去

最后要用share deal数据层接口

将成交记录进行保存

然后我们就返回share order订单信息

好这个就是市价单service层整体的处理逻辑

这样封装梳理之后

整个实现步骤就会比较清晰

下面章节我们再对具体逻辑的设定进行设定

和逻辑做相应的实现

那这一讲的内容我们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“市价单”处理逻辑的代码实现教学。讲师通过在 IntelliJ IDEA 开发环境中，逐步演示了 `StockDealServiceImpl` 类中的 `processMarketOrder` 方法的完整流程。该方法负责处理用户提交的市价单，其核心步骤包括：获取交易账户信息、获取股票产品信息、生成成交记录、生成持仓信息、保存订单信息、保存持仓记录，以及最后将订单ID关联到成交记录和持仓记录中。整个过程展示了如何在服务层协调多个DAO（数据访问对象）来完成一个完整的业务操作，并强调了代码的可读性和模块化设计。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 中展示课程大纲，定位到“3.2 实现市价下单接口”下的“3. 处理市价单”章节。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，展示 `StockDealServiceImpl` 类的代码，定位到 `processMarketOrder` 方法的定义。
*   **00:00:15 - 00:00:30**: 讲师开始逐行讲解代码，首先展示获取交易账户信息的代码：`TradeAccount tradeAccount = tradeAccountDao.getById(request.getAccountId());`。
*   **00:00:30 - 00:00:45**: 讲师继续讲解，获取股票产品信息：`TradeStock tradeStock = tradeStockDao.getById(request.getStockId());`。
*   **00:00:45 - 00:01:00**: 讲师演示生成成交记录，代码为 `TradeDeal tradeDeal = generateTradeDeal(quoteLast, request, tradeAccount, tradeStock);`。
*   **00:01:00 - 00:01:15**: 讲师演示生成持仓信息，代码为 `TradePosition tradePosition = generatePosition(tradeDeal, request, tradeAccount, tradeStock);`。
*   **00:01:15 - 00:01:30**: 讲师演示保存订单信息，代码为 `TradeOrder tradeOrder = saveTradeOrder(tradeDeal, request, tradeAccount, tradeStock);`。
*   **00:01:30 - 00:01:45**: 讲师演示保存持仓记录，代码为 `savePosition(tradePosition);`。
*   **00:01:45 - 00:02:00**: 讲师演示将订单ID关联到成交记录和持仓记录，代码为 `tradeDeal.setTradeOrderId(tradeOrder.getId());` 和 `tradePosition.setTradeOrderId(tradeOrder.getId());`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.2 实现市价下单接口` -> `3. 处理市价单`。
    *   代码注释：`// 1. 获取交易账户信息`，`// 2. 获取股票产品信息`，`// 3. 生成成交记录`，`// 4. 生成持仓信息`，`// 5. 保存订单信息`，`// 6. 保存持仓记录`，`// 7. 保存成交记录，记录订单ID和持仓位的ID信息`。
*   **代码关键内容**:
    *   **方法签名**:
        ```java
        private TradeOrder processMarketOrder(PlaceOrderRequest request, TradeStockQuoteLast quoteLast) throws ComponentException
        ```
    *   **核心业务逻辑**:
        ```java
        // 1. 获取交易账户信息
        TradeAccount tradeAccount = tradeAccountDao.getById(request.getAccountId());

        // 2. 获取股票产品信息
        TradeStock tradeStock = tradeStockDao.getById(request.getStockId());

        // 3. 生成成交记录
        TradeDeal tradeDeal = generateTradeDeal(quoteLast, request, tradeAccount, tradeStock);

        // 4. 生成持仓信息
        TradePosition tradePosition = generatePosition(tradeDeal, request, tradeAccount, tradeStock);

        // 5. 保存订单信息
        TradeOrder tradeOrder = saveTradeOrder(tradeDeal, request, tradeAccount, tradeStock);

        // 6. 保存持仓记录
        savePosition(tradePosition);

        // 7. 保存成交记录，记录订单ID和持仓位的ID信息
        tradeDeal.setTradeOrderId(tradeOrder.getId());
        tradePosition.setTradeOrderId(tradeOrder.getId());
        ```
*   **公式 / 图表**: 视频中未出现任何公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：方法定义与注释** (00:00:05 - 00:00:15)
    *   **描述**: 讲师在 IntelliJ IDEA 中定位到 `StockDealServiceImpl` 类的 `processMarketOrder` 方法。他首先展示了方法的完整签名，包括参数 `PlaceOrderRequest request` 和 `TradeStockQuoteLast quoteLast`，以及返回值 `TradeOrder` 和异常 `ComponentException`。他强调了方法的职责是处理市价单。
*   **场景二：获取账户与产品信息** (00:00:15 - 00:00:45)
    *   **描述**: 讲师逐行讲解代码。他首先演示了如何通过 `tradeAccountDao.getById(request.getAccountId())` 获取交易账户信息，并在IDE中展示了 `tradeAccountDao` 的类型。接着，他演示了如何通过 `tradeStockDao.getById(request.getStockId())` 获取股票产品信息，并在IDE中展示了 `tradeStockDao` 的类型。
*   **场景三：生成成交与持仓记录** (00:00:45 - 00:01:30)
    *   **描述**: 讲师演示了如何调用 `generateTradeDeal` 方法来生成成交记录，并在IDE中展示了 `generateTradeDeal` 方法的参数。接着，他演示了如何调用 `generatePosition` 方法来生成持仓信息，并在IDE中展示了 `generatePosition` 方法的参数。他强调了这两个方法是业务逻辑的封装，由其他类实现。
*   **场景四：保存订单与持仓记录** (00:01:30 - 00:01:45)
    *   **描述**: 讲师演示了如何调用 `saveTradeOrder` 方法来保存订单信息，并在IDE中展示了 `saveTradeOrder` 方法的参数。接着，他演示了如何调用 `savePosition` 方法来保存持仓记录，并在IDE中展示了 `savePosition` 方法的参数。
*   **场景五：关联订单ID** (00:01:45 - 00:02:00)
    *   **描述**: 讲师演示了如何将订单ID关联到成交记录和持仓记录。他调用 `tradeDeal.setTradeOrderId(tradeOrder.getId())` 和 `tradePosition.setTradeOrderId(tradeOrder.getId())`。他强调了这是为了保证数据的一致性，即一个订单对应一个成交记录和一个持仓记录。
