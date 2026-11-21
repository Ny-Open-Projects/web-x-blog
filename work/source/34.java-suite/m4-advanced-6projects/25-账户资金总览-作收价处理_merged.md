# 25-账户资金总览-作收价处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习和讲解

着售价的缓存生成处理

在实现之前大家先思考一下

这里要保存着售价

但我们接受的是当前的行情报价信息

那么我们如何去生成着售价呢

那之前咱们已经实现了

着售价缓存的读取

我们知道着售价的缓存结构

是由售盘价然后再加上日期组成

我们可以每天都生成售盘价

但是会造成一个问题

就是缓存会泛滥

那如果我们去设置超时时间

通过超时时间让缓存自动回收

那超时时间该设置为多久

如果我们设定为24小时

24小时刚好是一整天

但如果咱们是在交易的时间之内

去计算24个小时

这样子的话呢

就会横跨两个交易日

这样也不合适

那如果改成48小时呢

48小时虽然可以解决缓存泛滥的问题

但是如果是系统出现问题之后

咱们要过两三天之后

才能够发现

想要再去修复处理

就会比较麻烦

所以最终的解决方案

我们只维护当天和上一天的售盘价信息

通过两个缓存去做对应的实现

有这两个信息

就能够帮助咱们去实现

对应的业务逻辑

咱们可以画下对应的流程图

从图形上可以便于大家的理解

比如说在这里呢

是昨天的售盘价

在这里我们去给它标识一下

比如说是早上9点半开盘

下面呢是下午3点休市

那么3点钟收到这口行情报价

就代表是售盘价

这个时间呢

也就是1月1号

今天的售盘价呢

我们再放在另外的一个缓存记录里面

这里代表的是1月2号

也就是今天的售盘价信息

那么我们缓存在这里是如何去存储呢

在这里我们给它做一个标识

这里呢

代表的是昨天的售盘价缓存信息

那么它是通过股票产品ID作为key值

value呢

就是售盘价

再加上申购符

然后日期

这里还会记录一个缓存

就是当天的售盘价缓存信息

那么它的存储结构是怎样呢

股票ID

value

这里只需要存储当天的售盘价就可以

不需要加上日期标识

因为呢

它永远是保存当天的售盘价

着售价的记录

在这里追加日期

是为了防止

5分钟的

售盘价缓充时间造成的频繁覆盖

所以咱们要增加一个日期的判断数据

所以咱们要增加一个日期的判断数据

所以咱们要增加一个日期的判断数据

如果这个日期已经写入正确

那么这5分钟的缓存时间

它只需要更新一次就可以了

在这里最主要就是维护两个缓存信息

一个是昨天的售盘价缓存

另外一个就是当天的售盘价缓存

因为在做结算处理的时候

比如要去统计一些报表

这两个售盘价信息的话呢

都是需要使用到的

好

那咱们就回到代码当中来做具体的实现

在行情服务的Stock

在行情服务的Stock

Court Service Employment的这个实现例当中

我们在获取股票产品的行情员数据处理逻辑当中

去增加售盘价的处理

进入发送实时行情的方法

发送模拟数据咱们就暂时不用处理

咱们在这里就添加一个方法

去实现售盘价的更新处理

方法名称我们叫Update

Close

Vice

传递Court Last

最新的行情数据

行情报价信息

然后创建这个方法

Alt加Enter键

添加对应的注释

尝试更新售盘价

然后咱们来做具体的实现

首先判断是否

达到

售盘时间

通过DiscloseTime方法

做对应的判断

Portalist

传递股票市场

然后咱们要去获取当天的

售盘价版权信息

拿到

Cash对象

当前的

售盘价版权

通过CashManager

传递对应的Key字

Stock

Court Close

Vice

Current Key

然后要拿到

昨日的售盘价版权

Cash

Last Vice

Cash

Ladies

CashManager

Get Cash

传递对应的Key字

Court

Close

Vice Last Key

然后我们要去更新

售盘价

首先做一个唯空判断

Null不等于

Last

Vice Cash

传递

股票ID

这个是要获取昨日的

售盘价信息

我们要拿取

对应的售盘价信息

Vice

这个是一个自付例型

要做长转

Last Vice Cash

Quarter Last

传递股票ID

获取款程具体的资格

着售价的存储格式

咱们之前做了讲解

它是由着售价和日期组成

那我们要做一个分割处理

Last Close Vice AR

这是一个数字

Spied

通过转移

加上它的分割符

为了避免5分钟之内

产生的重复更新

咱们在这里加上一个

时间日期的判断

Get Format Today

这格式我们可以看一下

它是年月日

精确到天数

在这里它要和

着售价里面的

日期做判断

第二条数据

这个就是代表日期

根据

时间

判断

如果不一致

代表

首次修改

咱们就可以对着售价

做个分割

然后再来做一个更新处理

避免

重复更新

Long

View Last Price

拿取

当天的收盘价

Get

Quarter Last

Get Stock ID

然后我们就将

将当天的

收盘价

更新为

昨日的

收盘价

物代

时间标记

下一天

收盘时

需要再次更新

Last Price

将它的返存做一个更新

For the Last

传递股票ID

然后将它的值做一个拼接

再加上日期

Date Utils

Get Format Today

将当天的日期

转入进去

咱们可以再打印一个日字

标识是否进入这段模积

做相应的处理

Talk ID

打印一下

Value也打印一下

For the Last

Get Stock ID

For the Last Price Cash

再传递

它的值

Date Utils

Get Format Today

通过日志打印

我们就能够直观的看到

它是否处理成功

那接下来如果是不存在

如果返存中

夺售价

信息不存在

则将

当前的

售盘价

放入返存

Last Price Cash

For the Last

传递股票ID

然后做一个拼接

Date Utils

Get Format Today

最后咱们就要更新

当前的售盘价

Client Last Price Cash

Put

For the Last

Get Stock ID

For the Last

Get Last Price

好这个就是售盘价的整体处理逻辑

那咱们要注意的是

在更新售盘价的时候

要将着售价的缓存

改成当天的售盘价缓存的值

将当天的售盘价缓存

改成当前的售盘价的值

比如说10号

3点半

我们更新的售盘价是20.22

那么它当前的售盘价是20.22

上一次的售盘价是20.12

那么11号

它的售盘价是20.32

这个时候我们要将Last

也就是着售价

改成它的Client的值

然后将Client的值

改成咱们最新的20.32

最后的结果也就是Client是20.32

Last就是20.22

好 售盘价的处理逻辑大家要理解清楚

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“昨收盘价”缓存机制的实现讲解。讲师通过在 IntelliJ IDEA 中逐行演示 `StockQuoteServiceImpl` 类的代码，详细说明了如何在接收到实时行情数据后，判断是否为收盘价，并将该收盘价缓存到 Redis 中。核心设计思路是：仅在当天收盘时更新缓存，避免因系统问题导致的重复更新，从而保证数据的准确性和一致性。整个过程涉及 Redis 缓存、日期时间判断、字符串解析和缓存更新等技术点。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 编辑器中展示课程大纲，定位到“第3章 账户资金总览功能”下的“3.5 昨收盘价生成机制”。
*   **00:00:05 - 00:00:15**: 讲师在 IDE 中打开 `StockQuoteServiceImpl` 类，开始讲解 `sendRealQuote` 方法，说明其作用是处理实时行情数据。
*   **00:00:15 - 00:00:30**: 讲师聚焦于 `updateClosePrice` 方法，解释其功能是更新收盘价缓存。他通过 IDE 的代码补全功能，展示了如何获取 Redis 缓存对象。
*   **00:00:30 - 00:00:45**: 讲师在代码中添加了对 `DateUtils` 工具类的引用，用于处理日期和时间。
*   **00:00:45 - 00:01:00**: 讲师编写了核心逻辑，通过 `DateUtils.getFmtToday()` 判断当前是否为当天，从而决定是否更新缓存。
*   **00:01:00 - 00:01:15**: 讲师演示了如何从缓存中读取昨日收盘价，并将其与当前行情数据进行比较，以避免重复更新。
*   **00:01:15 - 00:01:30**: 讲师编写了将新收盘价存入缓存的代码，并添加了日志输出，用于调试和验证。
*   **00:01:30 - 00:01:45**: 讲师在代码中添加了 `else` 分支，用于处理缓存中不存在收盘价的情况，直接将当前行情数据存入缓存。
*   **00:01:45 - 00:02:00**: 讲师在 Typora 中展示了一个示例，说明了如何将 `cur`（当前价）更新为 `last`（昨收盘价），并解释了缓存的更新策略。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “第3章 账户资金总览功能” -> “3.5 昨收盘价生成机制”。
    *   **核心概念**: “计算当前时间是否在设定的交易时间范围之内”。
    *   **关键设计**: “避免多次调用造成的覆盖，产生数据错误”。
    *   **缓存策略**: “为避免多次调用造成的覆盖，产生数据错误，因为有5分钟的缓冲时间，所以更新昨收盘价的时候，必须带上当天的日期作为标记，如果当天的日期匹配，则不再更新，确保每天只更新一次。”

*   **代码关键内容**:

    ```java
    // 1. 调用第三方行情源，去获取最新的行情报价
    TradeStockQuoteLast quoteLast = juheThirdApi.getStockReal(stock);

    // 2. 判断实时行情价是否获取成功
    if (null != quoteLast) {
        // 3. 获取线程加工的行情数据放入缓存
        Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_GENERATE_KLINE_KEY);
        cache.put(stock.getCode() + "_" + quoteLast.getTm(), quoteLast);

        // 4. 更新处理收盘价（改变后5分钟内更新）
        if (closeDiffMins >= 0 && closeDiffMins < 5) {
            updateClosePrice(quoteLast);
        }
    }

    // 5. 更新收盘价
    private void updateClosePrice(TradeStockQuoteLast quoteLast) {
        // 判断是否到达收盘时间
        if (isCloseTime(quoteLast.getMarketNo())) {
            // 当天收盘价
            Cache curlLastPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
            // 昨日收盘价
            Cache lastPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_CLOSE_PRICE_LAST_KEY);

            // 更新收盘价
            if (null != lastPriceCache.get(quoteLast.getStockId())) {
                String lastClosePriceStr = (String) lastPriceCache.get(quoteLast.getStockId()).get();
                String[] lastClosePriceArr = lastClosePriceStr.split(regex: "\\|");
                if (DateUtils.getFmtToday().equals(lastClosePriceArr[1])) {
                    Long curlLastPrice = (Long) curlLastPriceCache.get(quoteLast.getStockId()).get();
                    lastPriceCache.put(quoteLast.getStockId(), curlLastPrice + "|" + DateUtils.getFmtToday());
                    Log.info("update lastprice cache, stockId: {}, value: {}, quoteLast: {}", quoteLast.getStockId(), curlLastPrice, quoteLast);
                } else {
                    // 如果缓存中，作收盘价不存在，则将当前的收盘价放入缓存
                    lastPriceCache.put(quoteLast.getStockId(), quoteLast.getLastPrice() + "|" + DateUtils.getFmtToday());
                }
            } else {
                // 更新当前的收盘价
                curlLastPriceCache.put(quoteLast.getStockId(), quoteLast.getLastPrice());
            }
        }
    }
    ```

*   **公式/图表**: 无。

---

### 4) 关键场景与演示描述

*   **场景一：代码环境与结构展示 (00:00:00-00:00:15)**:
    *   讲师首先在 Typora 中展示课程大纲，明确当前讲解的章节是“3.5 昨收盘价生成机制”。
    *   接着，他切换到 IntelliJ IDEA，打开项目 `bulls-stock-quote`，并定位到 `StockQuoteServiceImpl` 类，为后续代码演示做准备。

*   **场景二：核心逻辑实现 (00:00:15-00:01:30)**:
    *   讲师在 `sendRealQuote` 方法中，通过 `if (closeDiffMins >= 0 && closeDiffMins < 5)` 判断是否需要更新收盘价。
    *   他进入 `updateClosePrice` 方法，首先通过 `isCloseTime` 方法判断是否为收盘时间。
    *   他使用 `redisCacheManager.getCache(...)` 获取两个 Redis 缓存对象：`curlLastPriceCache`（用于存储当前价）和 `lastPriceCache`（用于存储昨收盘价）。
    *   他编写了核心的 `if (null != lastPriceCache.get(...))` 逻辑，用于判断缓存中是否存在昨收盘价。
    *   他使用 `DateUtils.getFmtToday()` 方法获取当前日期字符串，并与缓存中的日期进行比较，以决定是否更新。

*   **场景三：缓存更新与日志 (00:01:30-00:02:00)**:
    *   讲师在 `if` 分支中，将新收盘价（`curlLastPrice`）和当前日期（`DateUtils.getFmtToday()`）拼接后存入 `lastPriceCache`，并添加了日志输出。
    *   在 `else` 分支中，他处理了缓存中不存在昨收盘价的情况，直接将当前行情数据存入缓存。
    *   最后，他在 Typora 中展示了一个示例，说明了如何将 `cur` 更新为 `last`，并强调了缓存的更新策略：每天只更新一次，避免数据错误。

---

以上是根据视频画面进行的结构化技术分析，希望能帮助您更好地理解该技术课程的内容。
