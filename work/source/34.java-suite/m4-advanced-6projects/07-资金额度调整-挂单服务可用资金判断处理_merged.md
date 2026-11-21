# 07-资金额度调整-挂单服务可用资金判断处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们对本章内容做一个回顾和总结

首先咱们回顾本章的学习目标

这里我们要实现额度调整功能

完善交易服务下单功能

对额度调整接口的调整处理

接着的话要去完善挂单服务

撮合交易也就是委托挂单

对额度调整接口的调整处理

最后就是要完善挂单服务

对可用资金的判断和教验

接下来我们再回顾本章所讲解的具体内容

首先我们定义了接口的数据结构

在资金服务里面实现了额度调整接口功能

资金对用户来讲是比较重要的信息

一定要谨慎操作

在生产环境当中

这个是一定要加上分布式所的工资

要防止现成并发导致的数据安全问题

接着的话我们在交易服务里面

增加了额度调整的调用

完善了交易服务的市价下单处理功能

然后我们在挂单服务里面

也增加了对应的调用

同时在挂单服务里增加了可用资金的判断和教验

最后咱们从不同的测试场景

对整体功能做了测试和验证

在测试的过程当中

大家要注意一下

如果设计的资金比较大

在做计算比对的时候

会产生一些误差

因为咱们的成交记录里面

并没有实际的成交总金额

如果是在生产应用当中

我们最好要增加一个额外的字段

去记录实际的成交总金额

这样在对账和统计的时候

就不会出现误差的情况

好

最后咱们再来总结一下

额度调整设计的业务功能比较多

有下单挂单

还有业务方面的输入金和相关功能

我们在这里是测试交易

将相关的额度调整

功能做了改造和验证

大家在自行验证的时候

可以充分考虑

模拟各种场景

对功能进行充分的校验和完善

额度调整功能虽然已经实现了

但这还不足以保障生产环境的使用

为什么呢

因为上面也提到了

我们还没有实现分布之所

没有处理现成安全的问题

下面上节

我们就会利用分布之所

以及分布之事物

去保证了

保障数据的一致性以及安全性

好

这一讲就是对本章功能的回顾与总结

那这一讲的内容

咱们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是“交易平台”系列的第17天，主要讲解**额度调整功能**的实现与验证，并引出后续的**分布式事务**主题。课程内容围绕如何在交易系统中实现对用户账户资金的调整（如增加或减少），并确保在下单和挂单等核心业务场景中，资金操作的正确性与一致性。讲师通过修改 gRPC 接口、数据结构、DAO 层代码以及进行数据库验证，逐步完成了功能开发。最后，课程指出当前实现仅满足功能层面，尚不能保障生产环境的数据一致性，为下一章的分布式事务控制埋下伏笔。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：开场，展示课程大纲，介绍本章主题“额度调整功能”。
*   **00:05 - 00:15**：讲解“第1章 额度调整功能”的目标，包括实现额度调整、完善下单和挂单对额度调整接口的调用、以及完善资金判断校验。
*   **00:15 - 00:30**：进入“3. 实现”部分，首先讲解“3.1 定义接口数据结构”，说明额度调整仅用于内部服务调用，需定义 gRPC 接口。
*   **00:30 - 00:45**：讲解“3.2 资金服务额度调整接口实现”，展示如何修改 `GrpcStockFinanceService` 类，实现 `updateAccountBalance` 方法。
*   **00:45 - 01:00**：在 `updateAccountBalance` 方法中，展示核心逻辑：根据账户 ID 获取账户信息、检查可用资金、调整资金余额、并检查余额是否不足。
*   **01:00 - 01:15**：讲解“3.3 交易服务增加额度调整实现”，展示如何在 DAO 层修改 `TradeAccountDao`，添加 `updateBalanceById` 方法。
*   **01:15 - 01:30**：讲解“3.4 挂单服务增加额度调整实现”，展示如何在 `StockTradePendingServiceImpl` 类中调用资金服务的 gRPC 接口。
*   **01:30 - 01:45**：讲解“3.5 挂单服务增加可用资金判断校验”，说明在挂单时需要增加资金校验，并定义新的 gRPC 请求结构 `GetBalanceRequest`。
*   **01:45 - 02:00**：进入“4. 调用验证”部分，展示如何启动服务并查询数据库，验证订单和账户表的数据。
*   **02:00 - 02:15**：展示验证结果，包括订单表和账户表的数据，确认资金调整成功。
*   **02:15 - 02:30**：展示一个失败的验证场景，挂单时因资金不足而失败，系统返回错误信息 `SYS_500005`，验证成功。
*   **02:30 - 02:45**：进入“4. 总结”部分，回顾本章内容，并引出下一章“第2章 分布式事务集成运用”的目标：实现资金额度调整的分布式事务控制。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **第1章 额度调整功能**：目标、步骤、实现。
    *   **第2章 分布式事务集成运用**：目标（实现资金额度调整分布式事务控制，改造交易、挂单和资金服务）。
    *   **总结**：额度调整涉及下单、挂单、出入金等功能，已实现但不足以保障生产环境一致性，需用分布式事务。

*   **代码关键内容**：
    *   **`GrpcStockFinanceService` 类**：
        ```java
        @Override
        public void updateAccountBalance(UpdateBalanceRequest request, StreamObserver<UpdateBalanceResponse> responseObserver) {
            log.info("Process in updateAccountBalance method, xid: " + request.getxid());
            // 1. 根据账户ID，获取账号信息
            TradeAccount tradeAccount = tradeAccountDao.getByAccountId(request.getAccountId());
            if (null == tradeAccount) {
                throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_NOT_FOUND);
            }
            // 2. 检查账户的可用资金
            long balance = tradeAccount.getBalance() == null ? 0 : tradeAccount.getBalance();
            // 3. 调整可用资金
            balance += adjustBalance;
            // 4. 如果可用资金不足，给出错误提示信息
            if (balance < 0) {
                // 可用资金不足
                throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_BALANCE_NOT_ENOUGH);
            }
            // 5. 最后根据账户ID更新资金信息
            tradeAccountDao.updateBalanceById(request.getAccountId(), balance);
            responseObserver.onNext(UpdateBalanceResponse.newBuilder().setBalance(balance).build());
            responseObserver.onCompleted();
        }
        ```
    *   **`TradeAccountDao` 接口**：
        ```java
        /**
         * 更新账户资金信息
         * @param accountId
         * @param balance
         * @return
         */
        int updateBalanceById(@Param("id")Long id, @Param("balance")Long balance);
        ```
    *   **`StockTradePendingServiceImpl` 类**：
        ```java
        @GrpcClient("grpc-finance-server")
        private StockFinanceServiceGrpc.StockFinanceServiceBlockingStub stockFinanceseviceBlockingstub;
        // 在生成成交记录时调用
        stockFinanceseviceBlockingstub.updateAccountBalance(UpdateBalanceRequest.newBuilder().setAccountId(accountId).setAdjustBalance(adjustBalance).build());
        ```
    *   **`GetBalanceRequest` 消息定义**：
        ```protobuf
        message GetBalanceRequest {
            int64 accountId = 1;
        }
        ```

*   **图表/演示**：
    *   **数据库查询结果**：
        *   订单表 (`t_trade_order`)：查询 `id=53` 的记录，显示成交金额为 `1000 * 539 = 539000`，佣金为 `539000 * 0.012 = 6468`。
        *   账户表 (`t_trade_account`)：查询 `userId=1` 的记录，显示账户余额为 `399682`。
    *   **错误信息**：
        ```json
        {
            "status": "SYS_500005",
            "message": "挂单资金余额不足：请重新检查！",
            "data": "receiver server msg: ***** complete *****"
        }
        ```

---

### 4) 关键场景与演示描述

1.  **场景一：功能实现与代码演示**
    *   讲师首先在 PPT 上展示“第1章 额度调整功能”的目标和步骤。
    *   接着，他通过修改 `StockFinanceService.proto` 文件，定义了 `UpdateBalanceRequest` 数据结构。
    *   他演示了如何在 `GrpcStockFinanceService` 类中实现 `updateAccountBalance` 方法，详细讲解了获取账户、检查余额、调整余额、并更新数据库的完整流程。
    *   他展示了如何在 `TradeAccountDao` 中定义 `updateBalanceById` 方法，并在 `TradeAccountMapper.xml` 中编写对应的 SQL 更新语句。

2.  **场景二：服务集成与调用**
    *   讲师讲解了如何在“挂单服务”中集成资金服务。
    *   他展示了如何在 `StockTradePendingServiceImpl` 类中注入 `StockFinanceServiceGrpc` 客户端，并在生成成交记录时调用 `updateAccountBalance` 方法。

3.  **场景三：资金校验与验证**
    *   讲师讲解了在挂单时需要增加资金校验，以防止资金不足的情况。
    *   他演示了如何定义新的 gRPC 请求结构 `GetBalanceRequest`。
    *   他通过启动服务并查询数据库，验证了订单表和账户表的数据，确认资金调整成功。

4.  **场景四：失败场景验证**
    *   讲师演示了一个失败的挂单场景，即当账户资金不足时。
    *   他展示了系统返回的错误信息 `SYS_500005`，并确认该错误符合预期，验证了资金校验功能的有效性。

5.  **场景五：课程总结与展望**
    *   讲师在 PPT 上总结了本章内容，强调额度调整功能已实现，但尚不能保障生产环境的数据一致性。
    *   他引出了下一章“第2章 分布式事务集成运用”的目标，即通过分布式事务来保障数据的一致性。
