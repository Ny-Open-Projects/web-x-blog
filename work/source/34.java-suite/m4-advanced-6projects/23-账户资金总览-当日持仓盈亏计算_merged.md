# 23-账户资金总览-当日持仓盈亏计算 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们接着去实现账户资金总览

当天浮动盈亏的计算实现

首先咱们创建对应的方法

add加under键

create method

添加对应的注释

这是根据成交记录

计算当日的浮动盈亏

浮动盈亏

当日浮动盈亏的计算公式

咱们之前是做了讲解

我们可以再回顾一下

在这里是当日浮动盈亏的计算公式

我们将它修正一下

它是由原持仓数量

再乘以最新价格减去昨日的收盘价

也就是最新的价差

这样就得出原持仓的盈亏情况

然后将原持仓的盈亏

做一个汇总求和

就得出了

原有的持仓总盈亏数据

接着的话

再去计算求和当日卖出的盈亏信息

再加上当日买入的盈亏信息

实际上就是这三部分数据

组成了当日的持仓盈亏

大家注意一下

在各个交易平台里面

他们提供的当日持仓盈亏

都会给出一个提示

也就是说不能保证100%的精确程度

为什么呢

因为这个最新价格

是会不断的产生变化

所以原持仓的盈亏

是一个不固定的值

好

这一点大家要明白清楚

那咱们就来做具体的实现

回到代码当中

首先咱们要去获取

成交记录信息

从

成交

记录汇总数据里面

根据股票

ID

获取对应的成交记录信息

这个呢是一个集合

叫做Deals

从Globe by Deals里面获取

传递股票的ID

Gestalk ID

接下来要定义

买入收益属性

By Profit

Money为0

By Volume

Money为0

然后是卖出收益的

属性记录

Sell

Office

Volumes

然后我们要根据成交信息

做便利计算处理

首先判断成交记录是否为空

确保数据存在

然后我们做一个便利处理

Shared Deals

Shared Deals

拿到成交记录之后

我们要判断它的买卖方向

Shared Deals

Bet Direction

如果是等于买入的方向

Odd Directed By

那么它的计算是最新价格

减去成交价格

再乘以买入数量

定义价差

Diff Price

通过Mass Utils工具做对应处理

要做减法

拿到最新价格

Get Last Price

再减去成交记录里面的成交价格

这样计算出来的价差

那么我们就可以计算出它的买入的收益

Mass Utils

做一个乘法

通过Diff Price

再乘以成交数量

Get Exqueue Volume

然后我们还记录它买入的数量

Shared Deals

Get Exqueue Volume

接下来就是卖出方向的判断处理

卖出方向

卖出方向的它的计算公式

是成交价格减去着收价格

再乘以买入数量

Long Diff Price

Mass Utils

做一个减法

Shared Deals

Get Exqueue Price

再传递它的着收价

然后我们可以看到

要计算卖出的收益情况

做点加处理

Mass Utils

将价差相乘

传递成交数量

Exqueue Volume

然后记录它的卖出数量

Shared Deals

Get Exqueue Volume

接着咱们就可以去计算

它当前的仓位总数

给它定义一个变量

Edit Position

Value Position

Get Value

将当前的持仓数量

加上卖出数量

再减去买入的数量

这个就是原持仓的数量

这里我们要修改一下

原持仓总数量

这个是单比仓位

接下来我们就要去计算

原持仓的当日收益

这个都是单比仓位

这个计算公式

这个计算公式

我们将它拷贝进来

这里是单比仓位

不需要做求和处理

我们就可以简化一下

原持仓数量

他们已经计算出来了

在这里就拿到原持仓数量

去乘以最新价格

减去昨日收盘价

这个得出来的结果

就是原持仓的当日收益

Long

Separate

Mass Utils

Martin

S없yo

C segments

Supplier

Sperance

Supply

Supply

Supplier

后在紧迷的给我这是个

让我们看一下

我们之前说的

里面面跟内点

aproximadamente

我们现在来看一下

重点就是

Zio

宽美宽绝

您现在可以看到

我在这个码jazer做 fifa

现在可以看到

这个前复 cheese

悬起来

Cover plays

西 dictard

接下来要去计算当日时时持仓盈亏

这个呢就等于软此仓

当日收益

再加上

卖出数量

也就是卖出的收益

然后再加上买入的收益

这个收益有可能为正值也有可能为负值

对

forbis

会过一个累加

再加上

卖出的收益

再加上买入的收益

最后咱们就返回当日的收益结果

好在这里

就是对

当日

浮动盈亏的计算处理

那咱们回到讲义当中

咱们再对

整体的实现流程

做一个回顾

首先

咱们是初始化的一个vivo对象

在这里会去记录

资金总打的概要信息包括持仓盈亏

当日持仓盈亏

总资产

费用资金等等

接着话呢

我们去

获取

账户当天的所有交易记录

这里要注意一下他的时间

传递参数

PG Circle

他的时间是要转换为Time Step

才能进行正常的查询

买Circle咱们之前做查询的时候

通过Datalation就能够直接查询

对不对

但是PG Circle是有些不一样

这里咱们要注意一下

也就在数据查询的时候咱们是通过一个

日期工具

做的转换处理

可以看到

这里面是他的起始时间范围

我们点进去看一下

他返回的对象就是Time Step的时间错类型

好那咱们继续回到讲义当中

接下来呢我们就获取了用户的所有持仓信息

每个用户

每个股票产品

他只会存在

一条记录

由用户

和股票产品

组成的唯一性

这也就是为什么咱们是根据产品ID进行的分组汇总

接着我们是便利了用户的

仓位记录

从缓存当中

获取了最新的

行情报价

来直接计算

持仓的盈亏

当日的持仓盈亏计算起来

在整个的账户资金总览

信息计算当中

是属于比较复杂的

我们先要获取昨日的收盘价

由GetStoreCodeClose这个方法

去做具体的实现

这里咱们只是做

收盘价的获取处理

收盘价如何去生成

咱们在下面章节会做具体的讲解

然后咱们是对

当日的

持仓盈亏信息

做了计算处理

大家按照这个公式

做实现就可以

因为当日持仓盈亏是一个动态的

数据信息

所以不同的交易平台

他都无法去保障这个数据信息是100%的准确

而且每个交易平台他们的计算公式可能略微会有些差异

但是要保障最终的结果差别不大

如果只是几块钱的价差这个问题都不大

因为我们可以看到

组成信息当中

这里面都运用到了最新价格的

计算

如果你的持仓总市值越大那么这个价格的波动也就比较大

当日盈亏的计算咱们是先要去计算出

买入的收益

然后计算卖出的收益

最后咱们再来统计当日的

实时持仓盈亏

按照咱们的业务逻辑有序处理

好那这一讲咱们就完成了

账户

资金总打接口的

逻辑实现

下面章节

咱们再去对所涉及到的

着手价

如何去生成

做具体的讲解

和实现

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“账户资金总览”功能的实现细节讲解。讲师通过在 IntelliJ IDEA 中逐行演示 `StockFinanceServiceImpl` 类中的 `calcTodayTradeDealProfits` 方法，详细说明了如何根据交易记录（`TradeDeal`）计算单个持仓的当日盈亏。核心逻辑是：遍历分组后的交易记录，根据买卖方向分别计算买入和卖出收益，最后将总收益与持仓数量结合，得出当日总收益。整个过程体现了面向对象设计、数据分组处理和业务逻辑计算的结合。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**: 展示 `StockFinanceServiceImpl` 类中 `calcTodayTradeDealProfits` 方法的入口，以及调用该方法的上下文。
*   **00:00:16 - 00:00:30**: 讲解方法的参数：`groupByDeals`（按股票ID分组的交易记录）、`quoteLast`（最新行情报价）、`position`（持仓信息）和 `lastClosePrice`（昨日收盘价）。
*   **00:00:31 - 00:00:45**: 初始化买入和卖出收益变量 `buyProfits`、`sellProfits`、`buyVolumes`、`sellVolumes`。
*   **00:00:46 - 00:01:00**: 遍历 `tradeDeals` 列表，根据 `getDirection()` 判断交易方向。
*   **00:01:01 - 00:01:15**: 计算买入收益：`diffPrice = quoteLast.getLastPrice() - tradeDeal.getExecPrice()`，然后 `buyProfits += MathUtils.mul(diffPrice, tradeDeal.getExecVolume())`。
*   **00:01:16 - 00:01:30**: 计算卖出收益：`diffPrice = tradeDeal.getExecPrice() - lastClosePrice`，然后 `sellProfits += MathUtils.mul(diffPrice, tradeDeal.getExecVolume())`。
*   **00:01:31 - 00:01:45**: 计算初始持仓数量 `initPositionVolume = position.getVolume() + sellVolumes - buyVolumes`。
*   **00:01:46 - 00:02:00**: 计算当日总收益：`dayProfits = MathUtils.mul(initPositionVolume, MathUtils.sub(quoteLast.getLastPrice(), lastClosePrice))`，并加上 `sellProfits + buyProfits`。
*   **00:02:01 - 00:02:15**: 返回最终计算结果 `dayProfits`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    ```java
    private long calcTodayTradeDealProfits(Map<Long, List<TradeDeal>> groupByDeals, TradeStockQuoteLast quoteLast, TradePosition position, long lastClosePrice) {
        // 初始化变量
        long buyProfits = 0;
        long buyVolumes = 0;
        long sellProfits = 0;
        long sellVolumes = 0;

        // 遍历交易记录
        if (null != tradeDeals) {
            for (TradeDeal tradeDeal : tradeDeals) {
                if (tradeDeal.getDirection() == GlobalConstants.ORDER_DIRECTION_BUY) {
                    // 买入收益计算
                    long diffPrice = MathUtils.sub(quoteLast.getLastPrice(), tradeDeal.getExecPrice());
                    buyProfits += MathUtils.mul(diffPrice, tradeDeal.getExecVolume());
                    buyVolumes += tradeDeal.getExecVolume();
                } else {
                    // 卖出收益计算
                    long diffPrice = MathUtils.sub(tradeDeal.getExecPrice(), lastClosePrice);
                    sellProfits += MathUtils.mul(diffPrice, tradeDeal.getExecVolume());
                    sellVolumes += tradeDeal.getExecVolume();
                }
            }
        }

        // 计算初始持仓数量
        long initPositionVolume = position.getVolume() + sellVolumes - buyVolumes;

        // 计算当日总收益
        long dayProfits = MathUtils.mul(initPositionVolume, MathUtils.sub(quoteLast.getLastPrice(), lastClosePrice));
        dayProfits += sellProfits + buyProfits;

        return dayProfits;
    }
    ```

*   **关键公式**:
    *   **买入收益**：`买入收益 = Σ (最新价格 - 成交价格) * 买入数量`
    *   **卖出收益**：`卖出收益 = Σ (成交价格 - 昨日收盘价) * 卖出数量`
    *   **当日总收益**：`当日总收益 = 原持仓数量 * (最新价格 - 昨日收盘价) + 卖出收益 + 买入收益`
    *   **初始持仓数量**：`初始持仓数量 = 原持仓数量 + 卖出数量 - 买入数量`

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与参数说明** (00:00:00-00:00:30)
    讲师首先在 IDE 中定位到 `StockFinanceServiceImpl` 类中的 `calcTodayTradeDealProfits` 方法。他通过注释和代码行号，向观众解释了该方法的职责是计算单个持仓的当日盈亏，并介绍了四个关键参数：`groupByDeals`（按股票ID分组的交易记录）、`quoteLast`（最新行情）、`position`（持仓信息）和 `lastClosePrice`（昨日收盘价）。

*   **场景二：变量初始化与循环遍历** (00:00:31-00:01:00)
    讲师在代码中初始化了四个 `long` 类型的变量用于记录买入和卖出的收益与数量。随后，他通过 `for` 循环遍历 `tradeDeals` 列表，为每个交易记录准备计算。

*   **场景三：买卖方向判断与收益计算** (00:01:01-00:01:30)
    讲师使用 `if-else` 结构判断交易方向。在 `BUY` 分支中，他演示了如何计算 `diffPrice`（最新价减成交价），并将其乘以交易数量累加到 `buyProfits`。在 `SELL` 分支中，他演示了如何计算 `diffPrice`（成交价减昨日收盘价），并将其乘以交易数量累加到 `sellProfits`。

*   **场景四：持仓数量与总收益计算** (00:01:31-00:02:00)
    讲师展示了如何计算初始持仓数量 `initPositionVolume`，其公式为 `原持仓数量 + 卖出数量 - 买入数量`。接着，他演示了如何计算当日总收益，即 `初始持仓数量 * (最新价格 - 昨日收盘价)`，并加上 `sellProfits + buyProfits`。

*   **场景五：返回结果** (00:02:01-00:02:15)
    讲师在完成所有计算后，将最终的 `dayProfits` 返回，标志着该方法的执行结束。整个过程清晰地展示了如何将业务逻辑分解为可管理的步骤，并通过代码实现。
