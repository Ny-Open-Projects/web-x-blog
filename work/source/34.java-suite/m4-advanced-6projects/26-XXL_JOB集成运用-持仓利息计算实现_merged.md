# 26-XXL_JOB集成运用-持仓利息计算实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,这一讲,咱们就去对账户的仓位利息做具体的实现

我们根据梳理的流程来做具体的实现

这里第一个map

law

然后list的对象

chad position

group by position

chad position

stream

collect

collectors

grouping by

这里根据股票ID

做分组汇总

get stock ID

下面呢,就开始做便利

group

by position

for each

stock ID

还有position记录

咱们将处理步骤

简洁进去

首先做一个围攻判断

确定具备持仓数据

接下来我们要获取股票的最新行情报价

get stock

for the last

等于

get

stock for the last

通过这个方法

获取最新的股票行情

接下来

我们对最新行情报价

做个围攻判断

必须要存在最新的行情报价信息

否则无法计算下面的仓位市值

也就没法去计算对应的利息

然后要去便利

仓位的数据

for each

定义或这群对象

将处理步骤

简洁进去

接下来计算股票的利息

接下来计算股票的利息

接下来计算股票的利息

接下来计算股票的利息

接下来计算股票的利息

接下来计算仓位的市值

long

total

market value

通过mass utils工具

做对应的计算

multi

position

get volume

传递最新的行情报价

nice price

接下来我们要去计算

仓位利息

long

position

interest

通过mass utils

dy to long

这里的利息数据

利息率是采用万分比作为计算

所以外层要通过divide to long

做相应的处法

将总市值

再乘以利息

万分比是为长度

这里说明一下

为什么要除以1万呢

我们可以看一下它的利息率

这里呢

是万分比为单位

设置为二

代表的就是万分之二

所以在这里呢

要将市值和利息率相乘的结果再除以1万

接着

我们要去累加持仓利息

post

position

set

interest

做一个now

转换为0的处理

position

get interest

加入已经计算的利息

做这个处理呢

是为了防止空置人异常

接下来就要写入持仓利息的更新时间

position

set

interest time

这个呢

就是当天的时间

然后呢

我们将数据持续化到数据库当中

set position

do update interest

传递持仓对象

好

这样呢

我们就完成了账户持仓利息的调度任务处理

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中“账户持仓利息计算”服务的实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `AccountPositionInterestServiceImpl` 类中，利用 Java 8 的 Stream API 对数据库查询出的持仓数据进行分组、遍历、计算和更新。核心逻辑包括：根据日期获取所有有效持仓，按股票ID分组以减少数据库查询次数，获取最新的行情报价，计算每个持仓的市值和利息，并将计算结果更新回数据库。过程中，讲师还演示了如何使用 `MathUtils` 工具类进行精确的数值计算，并处理了空值（`null`）的情况。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示项目结构，定位到 `AccountPositionInterestServiceImpl.java` 文件。
*   **00:00:05 - 00:00:15**: 介绍方法 `generateAccountPositionInterest` 的功能和注释，说明其目的是“生成账户的持仓利息”。
*   **00:00:15 - 00:00:30**: 从数据库查询当天所有有效的持仓数据，代码为 `List<TradePosition> tradePositions = tradePositionDao.findAllValidPositionsByInterestTime(...)`。
*   **00:00:30 - 00:00:45**: 使用 Stream API 对 `tradePositions` 进行分组，按 `getStockId()` 分组，代码为 `Map<Long, List<TradePosition>> groupByPositions = tradePositions.stream().collect(Collectors.groupingBy(TradePosition::getStockId));`。
*   **00:00:45 - 00:01:00**: 遍历分组后的数据，对每个股票ID下的持仓列表进行处理。
*   **00:01:00 - 00:01:15**: 获取每个股票的最新行情报价 `TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(stockId);`。
*   **00:01:15 - 00:01:30**: 计算每个持仓的市值 `totalMarketValue = MathUtils.mul(pos.getVolume(), quoteLast.getLastClosePrice());`。
*   **00:01:30 - 00:01:45**: 计算每个持仓的利息 `posInterest = MathUtils.divLong(MathUtils.mul(totalMarketValue, interest), per: 10000);`。
*   **00:01:45 - 00:02:00**: 将计算出的利息更新到持仓对象中，并设置更新时间 `pos.setInterest(...); pos.setInterestTime(fmtDay);`。
*   **00:02:00 - 00:02:15**: 代码编写完成，展示最终的 `forEach` 循环结构。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    ```java
    @Override
    @Transactional(rollbackFor = Exception.class)
    public void generateAccountPositionInterest(String param) {
        log.info("Process in AccountPositionInterestServiceImpl.generateAccountPositionInterest method.");
        String fmtDay = DateUtils.getFmtDay();

        List<TradePosition> tradePositions = tradePositionDao.findAllValidPositionsByInterestTime(...);

        Map<Long, List<TradePosition>> groupByPositions = tradePositions.stream()
            .collect(Collectors.groupingBy(TradePosition::getStockId));

        groupByPositions.forEach((stockId, positions) -> {
            if (null != positions && positions.size() > 0) {
                TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(stockId);
                if (null != quoteLast) {
                    positions.forEach(pos -> {
                        Long totalMarketValue = MathUtils.mul(pos.getVolume(), quoteLast.getLastClosePrice());
                        Long posInterest = MathUtils.divLong(MathUtils.mul(totalMarketValue, interest), per: 10000);
                        pos.setInterest(isNullToZero(pos.getInterest()) + posInterest);
                        pos.setInterestTime(fmtDay);
                    });
                }
            }
        });
    }
    ```

*   **关键公式**:
    *   **持仓市值计算**: `总市值 = 持仓数量 × 股票最新价`
    *   **持仓利息计算**: `利息 = (总市值 × 利率) / 10000`
    *   **利率单位**: `interest` 是一个 `Integer` 类型的变量，表示“持仓利息率（四位），万分比为单位”，即 `2` 代表 `0.02%`。

*   **关键工具类**:
    *   `MathUtils`: 用于进行精确的数值计算，避免浮点数精度问题。
    *   `DateUtils`: 用于获取格式化的日期字符串 `fmtDay`。
    *   `TradeStockQuoteLast`: 用于获取股票的最新行情报价。

*   **关键设计模式**:
    *   **分组处理**: 使用 `Collectors.groupingBy` 按股票ID分组，以减少数据库查询次数。
    *   **事务管理**: 方法上使用 `@Transactional` 注解，确保数据操作的原子性。
    *   **空值处理**: 使用 `if (null != ...)` 判断，避免 `NullPointerException`。

---

### 4) 关键场景与演示描述

*   **场景一：分组处理** (00:00:30 - 00:00:45)
    讲师在代码中使用 `Stream` API 的 `collect(Collectors.groupingBy(...))` 方法，将 `List<TradePosition>` 按 `getStockId()` 进行分组。这一步是为了避免对每个持仓都去查询一次行情数据，而是先按股票分组，然后对每个股票组只查询一次行情。

*   **场景二：空值判断** (00:01:00 - 00:01:15)
    讲师在获取行情数据后，使用 `if (null != quoteLast)` 判断行情数据是否为空。这是为了防止在行情数据不存在时，后续的计算和更新操作抛出异常。

*   **场景三：数值计算** (00:01:15 - 00:01:30)
    讲师演示了如何使用 `MathUtils.mul` 和 `MathUtils.divLong` 进行精确的数值计算。`mul` 用于乘法，`divLong` 用于除法，并且 `divLong` 的第二个参数是 `per: 10000`，这表示利息是按万分比计算的。

*   **场景四：更新数据库** (00:01:45 - 00:02:00)
    讲师演示了如何将计算出的利息和更新时间写入持仓对象中。`pos.setInterest(...)` 用于设置利息，`pos.setInterestTime(fmtDay)` 用于设置更新时间。这一步是为了将计算结果持久化到数据库中。

*   **场景五：代码结构化** (00:02:00 - 00:02:15)
    讲师最终展示了完整的 `forEach` 循环结构，该结构将所有持仓数据处理完毕，实现了“生成账户的持仓利息”的核心功能。
