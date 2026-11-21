# 15-SEATA集成运用-交易服务市价单接口改造 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们去修改交易服务的下单接口

让它能够支持分布式事物的使用

这里要去修改stock deal service

整个代码基本上与原来的是一致

不需要去调整它的业务逻辑处理

因为CETA的集成使用并不会侵入原有的代码

这里我们就来着重讲解下有关分布式事物的具体运用

好那回到代码当中

定位到stock deal service implement

我们要去修改试价单的接口

首先我们增加transaction的事物注解

这个是在split-fling-work下面

no-back-for

针对于所有异常都进行回滚

大家注意

这个事物的注解和分布式事物是没有关系的

该事物注解的作用呢

主要是保证方法内部数据库接口操作的一致性

因为这里会具生成成交记录

时尝信息

订单信息等等

所以需要开启事物统一提交

好

接下来我们就去实现CETA售我的全局分布式事物

加上global

transactional

这里面不需要做过多的配置

咱们加上一个超时时间的配置就可以了

这里面呢

给它设置为5秒

一般接口处理时间超过5秒呢

就可能是出现问题了

这根据实际业务功能的复杂度

做相应的配置

一般设置为3到5秒

CETA的集成运用呢

非常简单

只需要加上这个注解就可以了

不需要加上任何的代码

也不需要调整原来的业务处理逻辑

这就是CETA接入的一个优势

使用和实现起来非常简便

为了便于跟踪

我们在这里呢

打印个日志

log.info

钥匙呢

已经开启了全局分布式事物了

global transaction

并且打印全局分布式唯一ID

这怎么获取呢

通过root context上下文

这个是由CETA提供出来

然后get xid

只要全局分布式事物生效

那么就能够正常接收到xid

并且将它打印出来

那么怎么知道

全局分布式事物有没有生效呢

我们在这里要模拟抛出一个异常

就在保存订单之后

保存持商记录之后

我们将异常的模拟抛出来

if true,sluh,new,compandException

这里面呢

就随便给它一个异常错误

比如说code last,price not found

只要抛出异常就可以

那接下来还去修改额度调整接口的调用处理

因为之前咱们讲过

CETA呢

它可以支持double或者是gattb的调用处理

这些都是正式的调用

GRPC,CETA 0.09版本目前还不支持

所以我们要做一个调整

手动将xid传递给调用的资金服务

好,那咱们就去修改一下

进入general,channel 2方法

找到更新账户资金的调用

这里很简单

我们只需要增加xid的注入

通过root,context,get xid

xid之前咱们在PP文件当中呢

已经提前定义好了

它的作用呢

就是用于全局分布式事务的控制

好,那资金服务的施加单接口就已经调整完成

咱们回到讲义当中

为了验证分布式事务的可用性

咱们在代码当中

模拟抛出了一个业务异常

整个调用顺序呢

就是组装完交易记录

调用资金服务

然后组装持仓记录,组装订单记录,保存订单记录

在保存持仓记录之前

模拟抛出了一个异常

那这样呢,之前的所有操作都会进行回滚,对不对

如果分布式事务验证是成功的

那么已经发出去的资金调整的接口

在这里已经将资金调整接口做了调用

那么数据呢,就应该进行回滚

具体结果是怎样

咱们在下面功能验证的时候呢

再做测试

好,这一讲就是对交易服务

施加下单接口做的改造

让它支持了CETA分布式事务的使用

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个分布式交易系统（`bulls-stock-deal`）的开发教程，重点讲解了如何在服务层（`StockDealServiceImpl`）中使用分布式事务框架（Seata）来保证一系列数据库操作的原子性。讲师通过修改代码，演示了如何使用 `@Transactional` 注解来管理事务，并通过模拟异常来验证事务的回滚机制。视频内容主要集中在“交易服务下单接口”的修改和“挂单服务撮合功能”的调整上，旨在说明分布式事务在实际业务场景中的应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Markdown 文档中定位到“3.5 交易服务下单接口修改”章节，介绍本节目标是调整市价单接口。
*   **00:05 - 00:15**: 讲师在 IDE 中打开 `StockDealServiceImpl.java` 文件，展示 `processMarketOrder` 方法的代码结构，并指出该方法包含多个数据库操作步骤。
*   **00:15 - 00:25**: 讲师将光标移动到方法的开始处，准备添加事务注解。他首先尝试添加 `@Transactional` 注解，并在注解中指定 `rollbackFor = Exception.class`，以确保任何异常都会导致事务回滚。
*   **00:25 - 00:35**: 讲师在方法上添加了 `@GlobalTransactional` 注解，并设置超时时间为 5000 毫秒，以模拟一个全局事务。
*   **00:35 - 00:45**: 讲师在方法内部添加日志语句，用于记录事务的开始，并打印当前事务的 ID（`XID`）。
*   **00:45 - 00:55**: 讲师在代码中添加了模拟异常的逻辑，通过一个 `if(true)` 语句来抛出 `ComponentException`，以测试事务回滚功能。
*   **00:55 - 01:05**: 讲师切换到 `StockDealServiceImpl` 的另一个方法，展示如何在 `updateBalance` 方法中处理账户余额更新，并在失败时抛出异常。
*   **01:05 - 01:15**: 讲师切换回 Markdown 文档，定位到“3.6 挂单服务撮合功能修改”章节，介绍接下来要修改的功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.5 交易服务下单接口修改` 和 `3.6 挂单服务撮合功能修改`。
    *   **关键说明**: 在“3.5”章节中，提到“调整市价下单接口”，并指出“整个代码基本与原来的一致，这里着重讲解下有关分布式事务使用的地方”。在“3.6”章节中，提到“为了验证分布式事务的可用性，在代码中模拟抛出 `QUOTE_LAST_PRICE_NOT_FOUND` 异常”，并描述了调用顺序和预期结果。

*   **代码关键内容**:
    *   **事务注解**:
        ```java
        @Transactional(rollbackFor = Exception.class)
        @GlobalTransactional(timeoutMills = 5000)
        ```
        这两个注解用于管理事务。`@Transactional` 是 Spring 的本地事务注解，`@GlobalTransactional` 是 Seata 的分布式事务注解。
    *   **日志语句**:
        ```java
        log.info("Start Global Transaction, XID = {}", RootContext.getXID());
        ```
        用于记录事务开始和事务 ID。
    *   **模拟异常**:
        ```java
        if(true) {
            throw new ComponentException();
        }
        ```
        用于在特定位置抛出异常，以触发事务回滚。
    *   **业务逻辑**:
        ```java
        TradeAccount tradeAccount = tradeAccountDao.getById(request.getAccountID());
        TradeStock tradeStock = tradeStockDao.getById(request.getStockId());
        TradeDeal tradeDeal = generateTradeDeal(...);
        TradePosition tradePosition = generatePosition(...);
        TradeOrder tradeOrder = saveTradeOrder(...);
        savePosition(tradePosition);
        ```
        这是处理市价单的核心业务逻辑，包含获取账户、股票、生成交易记录、生成持仓记录、保存订单和保存持仓等步骤。
    *   **余额更新异常处理**:
        ```java
        UpdateBalanceResponse updateBalanceResponse = stockFinanceServiceBlockingStub.updateAccount(...);
        if (GlobalConstants.STATUS_OK != updateBalanceResponse.getStatus()) {
            log.warn("update account balance error => code: {}, msg: {}", updateBalanceResponse.getStatus(), updateBalanceResponse.getMessage());
            throw new ComponentException(ApplicationErrorCodeEnum.parseByCode(updateBalanceResponse.getStatus()));
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：添加分布式事务注解**
    *   **描述**: 讲师在 `StockDealServiceImpl.java` 文件中，将光标定位到 `processMarketOrder` 方法的上方。他首先添加了 `@Transactional(rollbackFor = Exception.class)` 注解，然后添加了 `@GlobalTransactional(timeoutMills = 5000)` 注解。这表明他正在为该方法配置分布式事务，确保在任何异常发生时，所有相关的数据库操作都能被回滚。
    *   **技术要点**: `@Transactional` 用于管理本地事务，`@GlobalTransactional` 用于管理分布式事务，`rollbackFor` 指定哪些异常会导致事务回滚。

*   **场景二：模拟异常以验证事务回滚**
    *   **描述**: 讲师在方法内部添加了一段代码，通过 `if(true)` 语句来抛出 `ComponentException`。他解释说，当抛出这个异常时，由于之前配置了 `@Transactional` 注解，所有在该方法中执行的数据库操作都应该被回滚，从而保证数据的一致性。
    *   **技术要点**: 通过模拟异常来验证分布式事务框架的回滚功能，这是测试分布式事务是否生效的关键步骤。

*   **场景三：处理账户余额更新失败**
    *   **描述**: 讲师切换到 `updateBalance` 方法，展示如何处理账户余额更新失败的情况。他通过调用 `stockFinanceServiceBlockingStub.updateAccount` 方法来更新余额，并检查返回的状态码。如果状态码不是成功（`STATUS_OK`），则记录错误日志并抛出 `ComponentException`。
    *   **技术要点**: 在分布式系统中，任何操作都可能失败，因此需要在业务逻辑中处理失败情况，并通过抛出异常来触发事务回滚，确保数据一致性。

*   **场景四：切换到挂单服务撮合功能修改**
    *   **描述**: 讲师在视频末尾切换到 Markdown 文档，定位到“3.6 挂单服务撮合功能修改”章节。他简要介绍了接下来要修改的功能，并提到会模拟抛出异常来验证分布式事务的可用性。
    *   **技术要点**: 这表明视频内容是分阶段进行的，讲师在完成一个功能的修改后，会继续讲解下一个功能的修改，以展示分布式事务在不同业务场景中的应用。
