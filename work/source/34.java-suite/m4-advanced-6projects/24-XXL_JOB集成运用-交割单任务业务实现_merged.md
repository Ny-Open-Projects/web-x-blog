# 24-XXL_JOB集成运用-交割单任务业务实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们接着去实现账户交个单任务的业务处理逻辑

如何去处理实现的

首先我们要去获取指定的交易记录数据

因为用户要查询账户交个单

他会指定某一天的日期

比如说是昨天的交个单

或者是上一个月的某一天的交个单

这里的Parameter传递的就是日期

日期格式

比如说2020年5月1号

那么他就传递为2020-05-01

精确到天

后面不需要更具体的时间

那我们就要根据指定的时间

获取相应的成交记录

Trade Deals

通过Gate Trade Deals方法

我们将Parameter传输传递进去

咱们看一下这个方法的具体实现

他会判断这个参数是否为空

如果是为空的话

默认就获取当天的交易记录

那如果不为空呢

他就获取指定日期的交易记录

比如这里传递了一个日期

2020年5月1号

我们看一下他怎么去分割处理呢

他就会转换为两个日期

第一个日期会凭借一个时间

时间是从零点开始

结束日期是晚上的11点59分59秒

也是当天的最后的一个时间点

他会将这两个日期作为数组返回出去

我们可以看到

然后数据层接口根据这个日期范围做数据查询

这里呢

一个是begin time开始时间

另外一个是结束时间去查询对应的交易记录

好

那咱们再回到刚才的处理逻辑

接下来判断成交记录是否为空

如果不为空

我们再接下来处理下面的逻辑记录

首先把一个日志

这里我们将日志插件加入进来

我个pocket2

提示当前获取了多少条记录

这样便于咱们的追溯查询

拿到交易记录之后

要去做便利处理

share deals

通过流逝方式进行便利

这个deal

这里呢就是处理

具体的交易记录

我们去通过一个方法

做对应的实现

processedcredit deal

然后创建相应的方法

这里的交个单是根据每一条交易记录

会生成一条交个单数据

咱们先添加注释

根据

成交记录

生成

交个单数据

首先外围

增加异常的补货处理

输出错误日志

一点get message

为了避免重复生成交个单

这里呢要做一个重复判断

根据

成交记录

ID

来判断

交个单

是否存在

integer

usage

flag

get account settlement deal

deal

get id

这个接口呢会去根据

成交记录ID

查询交个单数据里面呢

是否已经生成了相应的记录

我们可以看一下

他传递了呢是成交记录的ID

返回值为1

如果不为1说明没有找到

再回到刚才的E5逻辑

这里做围攻判断

如果大于0说明他已经是存在

给出一个错误日志

get account

settlement

exist

deal ID

deal.get ID

这里我们将参数做个重复命名

6 便于咱们的使用

然后我们要去

创建

交个单对象

将

成交记录信息

赋予

交个单

创建交个单对象

Settlement

这些属性设置呢我们就不足以编写

从讲义当中做一个copy

回到代码当中

让他粘连进去

这里的错误呢我们要修正一下

要将缓存接口输入进来

一个是账户的缓存

另外一个是股票数据的缓存

添加注释

账户

缓存

这个是股票

缓存

再回到刚才的业务逻辑

再将这个包导入进来

YouTube下面

这一部分是设置交易的行为信息

比如说买的是哪支股票

买卖的方向

币种等相关信息

下面是设置交易的资金信息

这里面是跟金额相关的

比如说佣金税费

成交价格

成交数量等等

然后呢

要保存

交个单数据

CAD

CATCH

SETMENT

INSERT

SETMENT

好那咱们就完成了

交个单

任务接口的业务实现

回到讲义当中

咱们对整个流程再回顾一下

在这里我们先要获取此地的交易记录

然后账户交个单呢

他一般是在每天结算的时间

去处理当天的交易数据

所以

默认情况下面呢

他是加载当天的交易记录

当然这里也可以指定某一个参数日期

他的目的呢

是为了防止某天如果是生成失败的情况下面

第二天

我们仍然可以通过参数去触发

执行上一天的交个数据

修复交个单的生成

去做修复处理

刚才咱们在代码实现过程当中

所提及的

Pyramid这个参数

他不会是一个跨天的日期

这里只会传递具体的某一天日期

这个是由维护人员在XZLJob管理后台

去操作控制

通过这个参数

咱们就能够更加灵活的

去生成交个单数据

即便某一天失败了

咱们再次去调用相应的任务

传递指定的参数日期就可以

咱们再回到讲义当中

通过交易记录生成交个数据

我们先要做重复的判断检查

根据成交记录ID

做相应的判断

目的是要防止

去生成重复的数据

交易记录大部分数据都做了冗余

这里我们不用去做过多额外的计算

在代码当中可以看到

直接将成交记录的相关信息

设置进去就可以了

内部的话我们是通过遍地方式处理

存在大量的数据库的写入操作

这里我们需要加入事物

来提升整体的处理效率

咱们还需要将事物添加进去

在方法的最上面

添加consectional

这个是splint framework下面的

loadback for

指定

出现任何异常时候

都触发回滚

然后transaction manage

这里因为采用了双数据源

所以默认双数据源里面配置的是交易数据源

咱们可以看到

这里有Blimbo里的注写

如果是不指定consectional manage的情况下面

默认了他就会去操作交易的数据源

但是

咱们的

报表数据

统一

是放在业务数据下面

所以在这里我们要去指定业务数据源的事务管理器

Biz

System

Consectional

Manage

这点大家要注意一下

再回到讲习当中

咱们在内部做便利的时候

并没有采用并行流

因为并行流

它会异步执行

事务是不能真正生效的

由于调度服务是采用的双数据源

在这里呢我们也是用双数据源的

再次通过consectional manage

去指定了

业务数据库的

事务管理器的名称

防止出现错乱

因为咱们的报表数据呢是统一放在业务数据源下面

最后

交购单冗余了用户ID

股票产品代码等相关信息

这里呢是通过缓存去获取

目的是为了保障处理效率

不用每条数据都去查询数据库

缓存的实现处理呢

咱们之前也做了讲解

好

在这里

咱们就完成了

账户股票交购单调度任务的实现

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“账户交割单生成”功能的实现讲解。讲师通过 IntelliJ IDEA 开发环境，逐步演示了 `AccountSettlementServiceImpl` 服务类中 `generateAccountSettlement` 方法的编写过程。核心内容包括：
- **数据获取**：通过 `tradeDealDao` 获取指定日期范围的交易记录。
- **数据处理**：遍历交易记录，调用 `processTradeDeal` 方法进行处理。
- **数据持久化**：将处理后的交割单数据通过 `tradeAccountSettlementDao` 插入数据库。
- **事务管理**：使用 `@Transactional` 注解对整个操作进行事务控制，并通过 `transactionManager` 属性指定事务管理器。
- **缓存优化**：引入 `AccountsCache` 和 `StocksCache` 缓存组件，用于获取用户ID和股票代码，避免重复查询数据库，提升性能。
- **异常处理**：在关键步骤中添加日志记录和异常捕获，确保程序健壮性。

整个过程体现了在分布式系统中，如何通过分层架构、缓存、事务管理等手段，实现一个高效、可靠的数据处理任务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开始，讲师展示项目结构，定位到 `AccountSettlementServiceImpl` 类。
*   **00:05 - 00:20**: 讲解 `generateAccountSettlement` 方法的入口，参数为日期字符串（如 `2020-05-01`），并展示如何获取交易记录。
*   **00:20 - 00:40**: 详细演示 `getTradeDeals` 方法，展示如何根据日期范围查询数据库。
*   **00:40 - 01:00**: 讲解如何遍历交易记录，并调用 `processTradeDeal` 方法进行处理。
*   **01:00 - 01:20**: 进入 `processTradeDeal` 方法，展示如何获取交易数据、设置交割单信息。
*   **01:20 - 01:40**: 展示如何将交割单数据插入数据库。
*   **01:40 - 02:00**: 讲解事务管理，使用 `@Transactional` 注解，并通过 `transactionManager` 属性指定事务管理器。
*   **02:00 - 02:20**: 讲解缓存优化，引入 `AccountsCache` 和 `StocksCache`，避免重复查询数据库。
*   **02:20 - 02:40**: 总结整个实现过程，强调缓存和事务管理的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **第3章 分布式任务调度框架运用**：包含目标、步骤、实现等部分。
    *   **3.4 实现账户股票交割单调度任务**：详细说明了本节要实现的功能。
    *   **账户缓存实现**：展示了 `@Component` 和 `@Log4j2` 注解的使用。

*   **代码关键内容**:
    *   **`generateAccountSettlement` 方法**：
        ```java
        @Override
        public void generateAccountSettlement(String param) {
            // 获取交易记录
            List<TradeDeal> tradeDeals = getTradeDeals(param);
            if (null != tradeDeals && !tradeDeals.isEmpty()) {
                log.info("get trade deal size: " + tradeDeals.size());
                // 遍历交易记录
                tradeDeals.stream().forEach(tradeDeal -> {
                    // 处理交易记录
                    processTradeDeal(tradeDeal);
                });
            }
        }
        ```
    *   **`processTradeDeal` 方法**：
        ```java
        private void processTradeDeal(TradeDeal tradeDeal) {
            // 设置交割单信息
            TradeAccountSettlement settlement = new TradeAccountSettlement();
            settlement.setDealId(tradeDeal.getId());
            settlement.setStockId(tradeDeal.getStockId());
            settlement.setUserId(accountsCache.getUserId(tradeDeal.getAccountId()));
            settlement.setCurrency("CNY");
            settlement.setDirection(tradeDeal.getDirection());
            settlement.setStatus(0);
            settlement.setCreateTime(new Date());
            settlement.setStockCode(stocksCache.getCode(tradeDeal.getStockId()));
            // 设置交易资金信息
            settlement.setCommission(tradeDeal.getCommission());
            settlement.setTaxes(tradeDeal.getTaxes());
            settlement.setTradePrice(tradeDeal.getExecPrice());
            settlement.setTradeVolume(Long.valueOf(tradeDeal.getExecVolume()));
            settlement.setTradeTime(tradeDeal.getExecTime());
            settlement.setTradeAmount(MathUtils.mul(tradeDeal.getExecPrice(), tradeDeal.getExecVolume()));
            // 保存交割单数据
            tradeAccountSettlementDao.insert(settlement);
        }
        ```
    *   **事务管理注解**：
        ```java
        @Transactional(rollbackFor = Exception.class, transactionManager = "bizSystemTransactionManager")
        public void generateAccountSettlement(String param) {
            // ... 业务逻辑 ...
        }
        ```
    *   **缓存类定义**：
        ```java
        @Component
        @Log4j2
        public class AccountsCache {
            // ... 缓存逻辑 ...
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与数据获取**
    *   讲师在 `AccountSettlementServiceImpl` 类中定位到 `generateAccountSettlement` 方法。
    *   通过 `getTradeDeals` 方法获取指定日期范围的交易记录，并在控制台打印记录数量。

*   **场景二：数据处理与持久化**
    *   讲师使用 `stream().forEach` 遍历交易记录。
    *   调用 `processTradeDeal` 方法，将每条交易记录转换为 `TradeAccountSettlement` 对象。
    *   在 `processTradeDeal` 中，讲师展示了如何设置交割单的各个属性（如交易ID、用户ID、股票代码、交易金额等）。
    *   最后，调用 `tradeAccountSettlementDao.insert(settlement)` 将交割单数据保存到数据库。

*   **场景三：事务管理**
    *   讲师在 `generateAccountSettlement` 方法上添加 `@Transactional` 注解。
    *   通过 `transactionManager` 属性指定事务管理器为 `bizSystemTransactionManager`，以确保在双数据源环境下事务能正确生效。

*   **场景四：缓存优化**
    *   讲师在 `AccountSettlementServiceImpl` 中添加 `AccountsCache` 和 `StocksCache` 成员变量。
    *   在 `processTradeDeal` 方法中，通过 `accountsCache.getUserId(...)` 和 `stocksCache.getCode(...)` 获取用户ID和股票代码，避免了直接查询数据库。

*   **场景五：异常处理**
    *   在 `processTradeDeal` 方法中，讲师添加了 `try-catch` 块，用于捕获异常并记录日志。
    *   在 `generateAccountSettlement` 方法中，也添加了 `catch(Exception e)` 块，用于捕获整个流程中的异常。

通过以上演示，讲师清晰地展示了如何在实际项目中实现一个复杂的业务功能，并通过多种技术手段（如缓存、事务、异常处理）来优化性能和保证系统的稳定性。
