# 16-SEATA集成运用-挂单服务委托挂单接口改造 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着呢,去改造挂单服务的委托限价的接口,让它能够支持分布式事务。

那我们回到工程代码当中,定义到Stalker-Chad-Pending-Service。

咱们要去修改它的委托挂单,Process-Market Order。

首先,增加分布式事务的注解,Global-Transactional,设置一个超时时间。

超时时间设为5秒。

接下来再通过日志打印出全局分布式事务的ID,XID,通过Root-Context,Get-XID。

接下来我们要去模拟抛出一个异常。

这个异常的出发就放在保存成交记录之后。

if-chew-slu-new-compend-exception,随便给它一个异常错误码。

这里就给它。

Akana-not-match。

接下来我们去修改额度调整接口的调用。

进入Generate-Qt-Dio。

在这里增加XID的传递。

Root-Context,Get-XID。

好,那挂单服务的调整就已经修改完成。

接着的话呢,我们去检查一下它的外围调用。

因为挂单服务呢,它有很多个订单对电。

如果其中某一个订单出现了异常,其他对电呢,它不应该阻塞。

我们查看它外层是否有异常的补货。

在这里我们可以看到,便利的时候呢,增加了异常的补货处理。

某个挂单如果出现问题,并不会阻塞后面挂单的运行。

好,那咱们回到讲义当中。

这一讲咱们就对挂单服务的委托挂加单的接口做了调整和修改。

让它能够支持CETA分布式事务的使用。

那这一讲的内容咱们就先讲到这里。

谢谢大家的观看。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个分布式交易系统中“挂单服务”功能的修改与实现。核心内容是修改 `StockTradePendingServiceImpl` 类中的 `processMarketOrder` 方法，使其在处理市场订单时，能够与“资金服务”进行 gRPC 通信以更新账户余额，并在交易失败时抛出特定的业务异常。整个过程体现了分布式事务（通过 `@GlobalTransactional` 注解）和微服务间调用（gRPC）的结合。视频通过代码编辑器（IntelliJ IDEA）逐步展示代码修改、异常处理和业务逻辑的实现。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，定位到当前章节“3.6 挂单服务撮合功能修改”。
*   **00:00:05 - 00:00:15**: 展示 `StockTradePendingServiceImpl` 类的接口定义，包括方法签名 `processMarketOrder` 及其参数和返回值。
*   **00:00:15 - 00:00:30**: 代码编辑器中，展示 `@Transactional` 和 `@GlobalTransactional` 注解的配置，用于管理事务边界。
*   **00:00:30 - 00:00:45**: 代码编辑器中，展示 `@GrpcClient` 注解用于注入 gRPC 客户端 `stockFinanceServiceBlockingStub`。
*   **00:00:45 - 00:01:00**: 代码编辑器中，展示 `processMarketOrder` 方法的实现逻辑，包括获取交易账户、生成交易记录、保存订单等步骤。
*   **00:01:00 - 00:01:15**: 代码编辑器中，展示在 `processMarketOrder` 方法中添加了模拟异常的代码 `throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_NOT_MATCH);`。
*   **00:01:15 - 00:01:30**: 代码编辑器中，展示 `generateTradeDeal` 方法的实现，用于根据报价单和订单请求生成交易对象。
*   **00:01:30 - 00:01:45**: 代码编辑器中，展示 `generateTradeOrder` 方法的实现，用于生成订单记录。
*   **00:01:45 - 00:02:00**: 代码编辑器中，展示 `generatePosition` 方法的实现，用于生成持仓记录。
*   **00:02:00 - 00:02:15**: 代码编辑器中，展示 `updateBalance` 方法的实现，用于调用资金服务更新账户余额。
*   **00:02:15 - 00:02:30**: 代码编辑器中，展示 `processMarketOrder` 方法的最终实现，包括异常处理和返回值。
*   **00:02:30 - 00:02:45**: 展示 `PendingQuoteConsumer` 类中的 `processMarketOrder` 方法，用于处理撮合后的订单。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.6 挂单服务撮合功能修改`。
    *   代码文件路径：`com.ictast.trade.stock.pending.service.trade.impl.StockTradePendingServiceImpl`。
    *   方法签名：`public LimitPlaceOrderRequestVo processMarketOrder(LimitPlaceOrderRequestVo request, TradeStockQuoteLast quoteLast)`。
    *   异常类型：`ComponentException`。
    *   业务异常枚举：`ApplicationErrorCodeEnum.ACCOUNT_NOT_MATCH`。
    *   事务注解：`@Transactional(rollbackFor = Exception.class)` 和 `@GlobalTransactional(timeoutMills = 5000)`。
    *   gRPC 客户端注解：`@GrpcClient("grpc-finance-server")`。

*   **代码关键内容**:

    **1. `processMarketOrder` 方法核心逻辑**:
    ```java
    @Override
    @Transactional(rollbackFor = Exception.class)
    @GlobalTransactional(timeoutMills = 5000)
    public LimitPlaceOrderRequestVo processMarketOrder(LimitPlaceOrderRequestVo request, TradeStockQuoteLast quoteLast) {
        // 1. 获取交易账户信息
        TradeAccount tradeAccount = tradeAccountDao.getById(request.getAccountId());
        // 2. 获取股票产品信息
        TradeStock tradeStock = tradeStockDao.getById(request.getStockId());
        // 3. 生成成交记录
        TradeDeal tradeDeal = generateTradeDeal(quoteLast, request, tradeAccount, tradeStock);
        // 4. 生成持仓信息
        TradePosition tradePosition = generatePosition(tradeDeal, request, tradeAccount, tradeStock);
        // 5. 生成订单记录
        TradeOrder tradeOrder = generateTradeOrder(tradeDeal, request, tradeAccount, tradeStock);
        // 6. 执行订单记录保存操作
        saveOrder(tradeOrder);
        // 7. 执行持仓记录保存操作
        savePosition(tradePosition);
        // 8. 保存持仓记录
        tradeDeal.setOrderId(tradeOrder.getId());
        tradeDeal.setPositionId(tradePosition.getId());
        tradeDealDao.insert(tradeDeal);
        // 9. 模拟异常
        if(true) {
            throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_NOT_MATCH);
        }
        // 10. 更新账户余额
        UpdateBalanceRequest updateBalanceRequest = UpdateBalanceRequest.newBuilder()
            .setAdjustBalance(request.getDirection(), amount: deal.getAmount())
            .setAccountId(request.getAccountId())
            .setTradeId(tradeDeal.getId())
            .build();
        UpdateBalanceResponse updateBalanceResponse = stockFinanceServiceBlockingStub.updateAccountBalance(updateBalanceRequest);
        if (GlobalConstants.STATUS_OK.equals(updateBalanceResponse.getStatus())) {
            Log.warn("update account balance error => code: {}, msg: {}", updateBalanceResponse.getStatusCode(), updateBalanceResponse.getMessage());
            throw new ComponentException(ApplicationErrorCodeEnum.parseByCode(updateBalanceResponse.getStatusCode()));
        }
        return deal;
    }
    ```

    **2. `generateTradeDeal` 方法**:
    ```java
    private TradeDeal generateTradeDeal(TradeStockQuoteLast quoteLast, LimitPlaceOrderRequestVo request, TradeAccount tradeAccount, TradeStock tradeStock) {
        // 转换为报价深度
        Map<Long, Long> deepOffers = _cvtDeepOffer(quoteLast, request.getDirection());
        // 计算公式：均价 = (报价n价格 * 挂单n数量 + 挂单n数量) / (挂单n数量 + 挂单n数量)
        // (此处为示意，实际代码可能更复杂)
        return new TradeDeal();
    }
    ```

    **3. `updateBalance` 方法**:
    ```java
    // 调用资金服务更新账户余额
    UpdateBalanceRequest updateBalanceRequest = UpdateBalanceRequest.newBuilder()
        .setAdjustBalance(request.getDirection(), amount: deal.getAmount())
        .setAccountId(request.getAccountId())
        .setTradeId(tradeDeal.getId())
        .build();
    UpdateBalanceResponse updateBalanceResponse = stockFinanceServiceBlockingStub.updateAccountBalance(updateBalanceRequest);
    ```

---

### 4) 关键场景与演示描述

*   **场景一：接口定义与事务配置** (00:00:05 - 00:00:30)
    *   **描述**: 视频首先展示了 `StockTradePendingServiceImpl` 类的接口定义，强调了 `processMarketOrder` 方法的参数和返回值。随后，演示了如何使用 `@Transactional` 和 `@GlobalTransactional` 注解来管理方法的事务边界，确保在分布式环境下的一致性。

*   **场景二：gRPC 服务集成** (00:00:30 - 00:00:45)
    *   **描述**: 通过 `@GrpcClient` 注解，演示了如何在服务类中注入 gRPC 客户端 `stockFinanceServiceBlockingStub`，以便在方法内部调用远程的资金服务。

*   **场景三：核心业务逻辑实现** (00:00:45 - 00:01:15)
    *   **描述**: 逐步演示了 `processMarketOrder` 方法的实现。首先获取交易账户和股票产品信息，然后调用 `generateTradeDeal`、`generateTradeOrder` 和 `generatePosition` 等辅助方法生成交易、订单和持仓记录。接着，调用 `saveOrder` 和 `savePosition` 方法将记录保存到数据库。

*   **场景四：异常处理与资金更新** (00:01:15 - 00:02:30)
    *   **描述**: 在核心逻辑中，演示了如何模拟异常（`throw new ComponentException(ApplicationErrorCodeEnum.ACC
