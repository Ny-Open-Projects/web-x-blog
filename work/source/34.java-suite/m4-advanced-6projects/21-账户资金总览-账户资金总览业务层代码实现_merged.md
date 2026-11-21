# 21-账户资金总览-账户资金总览业务层代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现账户资金总览接口

业务层的代码

咱们回到代码当中

上一讲,咱们对业务层的整体实现处理步骤

做了一个讲解和梳理

那接下来咱们就来做具体的实现

第一个步骤,创建资金总览的无忧返回对象

咱们已经做了相关的定义和实现

那么咱们接着去实现第二个步骤

第一,交易记录的集合

去到deal,deal list

去到deal,deal里面去查询对应的数据

传递开始时间

这个是今天的开始时间

然后今天的交易结束时间

get from met,得被end

我们可以看一下

今天的起始时间就是当天的零点开始

时间

这里面全部传递为零

结束时间的话呢

其实就是当前的时间

咱们也可以看一下

这里面传递的是当前的时间点

如果是在交易时间之内进行的查询

那么它就是截止零点到当前的时间点

查询到所有的交易记录

如果是在交易结束之后进行的查询

它的数据信息是不会再产生变化

因为交易结束之后

是不能够再重新进行买卖操作

所以在这里结束时间

咱们只需要传递当前的时间点就可以

接下来就去实现第三个步骤

根据股票产品ID做分组汇总

咱们定义一个map集合

这里面记录的值呢

是一个list

group by deals

deal list

stream方式

做对应的处理

connectors

grouping by

根据股票产品ID

做分组处理

get stock ID

接着我们要去根据交易账户ID

去查询所有的持仓记录

定义一个list

类型是get position

position list

通过数据层接口

拔了数据信息

我们可以去查询

get all

by account ID

传递交易账户ID

接下来做便利处理

get position

position list

那首先呢

要获取最新的行情报价

行情报价信息是从款顺里面获取

port last

get trade

stock port last

传递股票产品ID

get stock ID

这个方法之前呢完美做了讲解

它是传递股票产品ID

然后从缓存当中获取最新的行情报价

好回到刚才的处理逻辑

接着我们做一个唯空判断

if now不等于quad last

那么我们就要去计算它的浮动盈亏

浮动盈亏是采用长者性表示

保留两位小数

它的计算公式是最新价

减去成本价

再乘以持仓数量

定一个long类型

if price

mess utils

点sub减法

拿到行情的最新报价

get last price

再减去position

获取它的成本价

get cost price

计算完差价之后

就可以计算它的浮动盈亏

mess utils

点mult

这个做一个乘法

拿到差价

去乘以持仓数量

position get volume

乘以它的持仓数量

然后计算总的持仓盈亏

position profit

这里就要做一个累加

将单笔的持仓盈亏做一个累加记录

接下来要去计算当日的盈亏

那要计算当日盈亏之前

就要获取所谓的费用

我们先来看一个

昨天的收盘价

定义一个属性做记录

这里面我们通过一个方法

做对应的封装处理

get stock

cord close

这个方法

咱们在下面章节当中

再做一个实现和讲解

还有传递股票产品ID

然后要去计算

单个仓位的

当天

将所有的持仓盈亏

交记录的盈亏信息

也就是获取单笔持仓的当日盈亏

将所有的单笔持仓的当日盈亏

进行一个累加

就是咱们所有持仓的总盈亏

就是咱们的当日持仓盈亏

好

这里也要做一个累加处理

它是要获取所有单笔持仓的当日盈亏

对

profile

那么我们要计算单笔的持仓盈亏

这里面也通过一个方法

做封装处理

deal

office

咱们先定义在这里

下面章节

再做讲解实现

还有传递实时行情

或这一群

仓位记录

以及着手价

最后去记录总的市值

total

market amount

这里也是要记录

这里也是要去做一个累加

将单笔持仓的市值做个计算

最后再累加在一起

就是总的市值

order last

然后在这里传递最新的价格

还有持仓的数量

get volume

最新价乘以持仓数量

这里面就是单笔持仓的最新市值

通过外乘循环便利

就能计算出

咱们仓位的总市值

接着我们还将计算的结果

存放到vr的返回对象当中

account of will

set day profit

account of will

set position profit

set total market amount

最后就要去计算总的资产

这里我们也通过一个方法

做封装处理

access

account of id

account of will

然后呢

我们将account of will

will对象

作为结果返回出去

计算总资产这个方法

咱们来做一个实现

edit

加enter

创建对应的方法

添加注释

这个是计算总资产

这里要抛出一场

sluice

compound exception

首先获取交易账户的信息

因为交易账户里面呢

记录了它的可用资金

接着account of do

get by id

传递交易账户id

然后做一个唯空判断

如果account的唯空

在这里咱们要抛出对应的一场

sluicecompound exception

给它一个抽物码

account not found

allow balance

获取它的账户可用资金

account get balance

判断是否唯空

不唯空呢

就取出它的实际可用资金

然后将信息设置到account of do当中

加上balance可用资金

然后去设置它的可用资金

get balance

好这个呢就是总资产的计算实现

这里呢我们还抛出一场

sluicecompound exception

在接口层

也要追加一场的抛出

好这一讲就是对计算账户总览信息

业务层代码的实现

下面章节咱们再对关联的逻辑

做实现和讲解

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“账户资金总览功能”的实现教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `StockFinanceServiceImpl` 服务类中编写 `calcAccountSummary` 方法。该方法的核心是计算一个账户在指定日期的当日盈亏、总市值和总资产。实现过程涉及 Spring 的 `@Autowired` 注解注入数据访问层（DAO），使用 Java 8 的 Stream API 对交易记录进行分组聚合，以及通过循环遍历持仓信息来计算各项财务指标。视频重点展示了代码的逻辑结构、关键公式和数据处理流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 中展示课程大纲，明确本节内容为“第3章 账户资金总览功能”下的“3.1 资金服务的搭建与配置”。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，展示 `StockFinanceServiceImpl` 类的代码结构，重点是 `@Service` 注解和 `@Autowired` 注解用于注入 `ITradePositionDao` 和 `IStockQuoteDao`。
*   **00:00:15 - 00:00:30**: 讲师开始编写 `calcAccountSummary` 方法，首先创建 `AccountOverviewVo` 对象，并初始化 `dayProfits`、`totalMarketAmount` 和 `totalAssets` 等变量。
*   **00:00:30 - 00:00:45**: 讲师调用 `tradeDealDao.getTradeDealByAccountAndTime` 方法，根据账户ID和日期范围获取当天的所有交易记录 `dealList`。
*   **00:00:45 - 00:01:00**: 讲师使用 `Stream` API 对 `dealList` 按照产品ID进行分组，以减少后续的 SQL 查询次数。
*   **00:01:00 - 00:01:15**: 讲师调用 `tradePositionDao.getAllByAccountId` 方法，根据账户ID获取该账户的所有持仓信息 `positionList`。
*   **00:01:15 - 00:01:30**: 讲师开始一个 `for` 循环，遍历 `positionList` 中的每一个持仓对象 `position`。
*   **00:01:30 - 00:01:45**: 在循环体内，讲师获取最新的行情报价 `quoteLast`，并计算单个持仓的浮动盈亏 `diffPrice` 和 `profit`。
*   **00:01:45 - 00:02:00**: 讲师继续计算 `dayProfits`（当日盈亏）和 `totalMarketAmount`（总市值）。
*   **00:02:00 - 00:02:15**: 讲师将计算结果设置到 `accountView` 对象中。
*   **00:02:15 - 00:02:30**: 讲师调用 `calcTotalAssets` 方法来计算总资产。
*   **00:02:30 - 00:02:45**: 讲师展示 `calcTotalAssets` 方法的实现，该方法会调用 `accountView` 的 `setTotalMarketAmount` 方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`第3章 账户资金总览功能`，包含子章节如 `3.1 资金服务的搭建与配置`、`3.2 账户资金总览功能计算公式介绍`、`3.3 定义接口数据结构`、`3.4 资金服务账户资金总览接口实现` 等。
*   **代码关键内容**:
    *   **服务层类定义**:
        ```java
        @Service
        public class StockFinanceServiceImpl implements IStockFinanceService {
            @Autowired
            private ITradePositionDao tradePositionDao;
            @Autowired
            private IStockQuoteDao stockQuoteDao;
        }
        ```
    *   **核心方法 `calcAccountSummary`**:
        ```java
        @Override
        public AccountOverviewVo calcAccountSummary(long accountId) throws ComponentException {
            AccountOverviewVo accountView = new AccountOverviewVo();
            long positionProfits = 0;
            long dayProfits = 0;
            long totalMarketAmount = 0;
            long totalAssets = 0;

            // 获取交易记录
            List<TradeDeal> dealList = tradeDealDao.getTradeDealByAccountAndTime(accountId, DateUtils.getPartTodayStart(), DateUtils.getPartTodayEnd());

            // 按产品ID分组
            Map<Long, List<TradeDeal>> groupByDeals = dealList.stream().collect(Collectors.groupingBy(TradeDeal::getProductId));

            // 获取持仓信息
            List<TradePosition> positionList = tradePositionDao.getAllByAccountId(accountId);

            // 遍历持仓计算
            for (TradePosition position : positionList) {
                TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(position.getStockId());
                if (null == quoteLast) {
                    continue;
                }
                long diffPrice = MathUtils.sub(quoteLast.getLastPrice(), position.getCostPrice());
                long profit = MathUtils.mul(diffPrice, position.getVolume());
                positionProfits += profit;

                long lastClosePrice = getStockQuoteClose(position.getStockId());
                dayProfits += calcTodayTradeDealProfits(groupByDeals, quoteLast, position, lastClosePrice);
                totalMarketAmount += MathUtils.mul(quoteLast.getLastPrice(), position.getVolume());
            }

            // 设置结果
            accountView.setDayProfit(dayProfits);
            accountView.setPositionProfit(positionProfits);
            accountView.setTotalMarketAmount(totalMarketAmount);

            // 计算总资产
            calcTotalAssets(accountId, accountView);

            return accountView;
        }
        ```
    *   **公式说明**:
        *   **当日持仓当日收益**：$\sum (\text{持仓数量} \times (\text{最新价格} - \text{成本价格}))$
        *   **总市值**：$\sum (\text{最新价格} \times \text{持仓数量})$
        *   **总资产**：总市值 + 可用资金

---

### 4) 关键场景与演示描述

*   **场景一：服务层初始化** (00:00:05-00:00:15)
    *   讲师在 IDEA 中打开 `StockFinanceServiceImpl` 类，展示了其 `@Service` 注解和 `@Autowired` 注解的使用，说明了服务层如何通过依赖注入获取数据访问层的实例。
*   **场景二：方法实现与公式展示** (00:00:30-00:01:00)
    *   讲师在 `calcAccountSummary` 方法中，通过注释清晰地展示了计算公式，并逐步编写代码，包括初始化变量、获取交易记录和持仓信息。
*   **场景三：Stream API 分组聚合** (00:00:45-00:01:00)
    *   讲师使用 `Stream` API 对交易记录进行分组，以减少后续的 SQL 查询次数，这是一个重要的性能优化点。
*   **场景四：循环遍历与计算** (00:01:15-00:02:00)
    *   讲师通过 `for` 循环遍历持仓列表，对每个持仓对象进行处理，计算其浮动盈亏、当日盈亏和总市值，并将结果累加到相应的变量中。
*   **场景五：结果设置与返回** (00:02:15-00:02:30)
    *   讲师将计算出的当日盈亏、持仓盈亏和总市值设置到 `AccountOverviewVo` 对象中，并调用 `calcTotalAssets` 方法计算总资产，最后返回 `accountView` 对象。

整个演示过程逻辑清晰，代码结构良好，充分体现了面向对象编程和函数式编程在实际项目中的应用。
