# 15-第三方行情源-第三方行情源核心逻辑处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现第三方行情员对接的业务层代码

咱们把初始化开盘价信息缓存这一块的逻辑先做一个实现

首先咱们要从缓存当中拿到所有的key值

因为不仅只是记录一只股票的开盘价信息

那么咱们要通过ladies template这个模板接口进行key值的扫描

这个是更为底层的接口

ladies cache manager它没法去扫描获取到所有的key值

扫描的方法

这里是可以支持模糊匹配

做一个围攻判断

接下来就要拿到缓存对象

根据上面扫描的key做便利

咱们通过一个流逝进行处理

根据key进行便利

这里咱们要将扫描的key转换一下

获取了它的stock id

加上一个注释

将key转换

获取了stock id

这样咱们才能通过stock id从缓存当中拿取开盘价

将前对key做一个替换

注意还加上两个报号

替换为空

这样就能拿到stock id

咱们还要拿到缓存对象

开盘价缓存的key值

传入stock id

然后对值做一个围攻判断

将那值做一个强转

转换成为乱形

然后将开盘价缓存信息

放到咱们的map当中

咱们再回到外层行情员的处理逻辑

接下来是要计算股票的涨跌幅比例

它的计算公式

咱们写一下

是最新价

简讯的着收价

注意不是开盘价

是着收价

然后再处理着收价

这样才是它当天的

涨跌幅

也有可能会出现曝数

因为有上涨就会有下跌

对不对

咱们是通过一个

方法进行了封装处理

在这里面传入两个价格

一个是追星价

还有一个就是昨日的收盘价

下面这个就是着收价

咱们来看一下这个方法的处理逻辑

在这里面涨跌幅的计算

它做的三层判断

哪三层

第一个是正值的情况

也就是上涨的情况

第二个就是不涨不跌

就等于零

最后一种就是出现负值的情况

通过这三种情况的处理

才能计算出一个正确的涨跌幅

再回到刚才外层的处理逻辑

接着咱们就要去更新股票报价信息缓存

首先要拿到它的catch对象

从Ladies catch manager当中去获取一个catch对象

传入它的变量

stock

NAS price key

然后呢

将它的最新行情报价存入缓存当中

这样咱们就完成了第三方行情员信息订阅

以及缓存这边计算的处理

咱们计算的开盘价以及它的涨跌幅比例

接下来咱们回到讲义当中

咱们对整个第三方行情员的处理逻辑呢

再做一个回顾

通过第三方行情员对接的实现内

咱们可以获取到最新的行情报价

并且要做唯空判断

在这里面我们可以看到做了一个闹的判断

接下来咱们就去更新了k线的缓存

这个呢是要提供k线加工所必要的信息

所以将它存入缓存当中

k线生成呢

需要涉及到分表的处理方案

后面呢

咱们还会做一个具体的讲解

制定逻辑实现股票的收盘价计算

并且呢

要实现它的一个更新处理流程

开盘价的整个处理流程呢

也给大家做了一个讲解

最主要呢

要把握好这三点流程的处理

在这里如果是制定逻辑实现股票的收盘价计算和更新

咱们需要理解收盘价的处理流程

具体实现呢

后面的章节当中咱们还会做详细的讲解

对于第三方行情员

已经实现收盘价计算的话呢

那么可以不用再去做实现

下面是制定逻辑实现了股票的开盘价计算

以及呢

它的更新处理流程

开盘价的整个处理机制

它的核心主要处理流程呢

咱们在这里做了讲解

最主要呢

要把握好这三点

保障呢

收盘价能够呢

正常计算和处理

第三方聚合平台行情员呢

他已经提供出来的

开盘价

这里做讲解呢

是帮助大家能够更好地掌握开盘价的计算和处理流程

下面呢

是计算股票产品的涨跌幅比例

他需要更新股票产品呢

他的最新报价放入到盘存当中

最后面呢

是要发送行情报价信息给对应的消息队列

因为咱们还没讲到MQ的集成处理

所以这个实现了

咱们的开盘价是最高的开盘价的计算和处理流程

我们放在下面章节

再做一个详细详解

缓存处理以及他的实现呢

在下面的3.5章节当中呢

咱们会做讲解和介绍

在这里呢

咱们就实现了第三方行情员对接业务层的实现

外层呢

咱们还需要实现相应的逻辑

这个在下面章节当中再做讲解和介绍

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段来自一个关于股票行情数据处理的Java后端技术课程。讲师正在演示如何在 `StockQuoteServiceImpl` 服务类中，通过 Spring Boot 和 Redis 缓存技术，实现股票实时行情数据的获取、处理和缓存更新。核心内容包括：
- **初始化开盘价缓存**：从 Redis 中加载历史开盘价数据，并将其存入一个本地的 `ConcurrentHashMap` 中。
- **计算涨跌幅**：根据最新价和开盘价，计算股票的涨跌比例。
- **更新缓存**：将处理后的最新价和涨跌幅信息更新到 Redis 缓存中。
- **代码演示**：讲师通过 IntelliJ IDEA 编辑器，逐行讲解并演示了 `initOpenPriceCache`、`calcPriceRate` 和 `updateOpenPrice` 等关键方法的实现逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示 `StockQuoteServiceImpl` 类中的 `initOpenPriceCache` 方法，讲师准备初始化开盘价缓存。
*   **00:00:05 - 00:00:15**：讲师在 `initOpenPriceCache` 方法中，使用 `redisTemplate.keys` 方法，根据一个模式（`STOCK_QUOTE_OPEN_PRICE_CUR_KEY`）从 Redis 中获取所有相关股票的开盘价键。
*   **00:00:15 - 00:00:25**：讲师使用 `redisCacheManager.getCache` 方法，根据键获取对应的缓存对象，并遍历所有键。
*   **00:00:25 - 00:00:35**：讲师演示如何从缓存中取出 `ValueWrapper`，并将其转换为 `Long` 类型的股票代码和开盘价，存入本地的 `stockOpenCache` 映射中。
*   **00:00:35 - 00:00:45**：讲师切换到 `fetchQuote` 方法，演示如何通过第三方行情接口（`juheThirdApi`）获取实时行情数据。
*   **00:00:45 - 00:00:55**：讲师演示如何计算涨跌幅，使用 `MathUtils.divDouble` 方法进行除法运算，并根据差值的正负判断涨跌。
*   **00:00:55 - 00:01:05**：讲师演示如何将计算好的最新价和涨跌幅信息更新到 Redis 缓存中，使用 `lastPriceCache.put` 方法。
*   **00:01:05 - 00:01:15**：讲师切换到课程的 Markdown 文档，总结本节内容，包括缓存初始化、涨跌幅计算和缓存更新等核心逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **代码关键内容**

*   **`initOpenPriceCache` 方法**：
    ```java
    @PostConstruct
    @Override
    public void initOpenPriceCache() {
        Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY + "*");
        if (keys != null && !keys.isEmpty()) {
            Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
            for (String key : keys) {
                Cache.ValueWrapper valueWrapper = cache.get(key);
                Long stockId = valueWrapper.get();
                stockOpenCache.put(stockId, valueWrapper.get());
            }
        }
    }
    ```

*   **`calcPriceRate` 方法**：
    ```java
    private double calcPriceRate(Long lastPrice, Long openPrice) {
        double priceRate = 0;
        if (null != openPrice) {
            long diffPrice = MathUtils.subPrice(lastPrice, openPrice);
            if (diffPrice > 0) {
                priceRate = MathUtils.divDouble(diffPrice, openPrice) * 100;
            } else if (diffPrice == 0) {
                priceRate = 0;
            } else {
                priceRate = -MathUtils.divDouble(diffPrice, openPrice) * 100;
            }
        }
        return priceRate;
    }
    ```

*   **`updateOpenPrice` 方法**：
    ```java
    if (closeDiffMins > 0 && closeDiffMins < 5) {
        // 更新开盘价
        updateOpenPrice(quoteLast);
    }
    ```

#### **公式关键内容**

*   **涨跌幅计算公式**：
    $$
    \text{涨跌幅} = \begin{cases}
    \frac{\text{最新价} - \text{开盘价}}{\text{开盘价}} \times 100\% & \text{如果 } (\text{最新价} - \text{开盘价}) > 0 \\
    0 & \text{如果 } (\text{最新价} - \text{开盘价}) = 0 \\
    -\frac{\text{开盘价} - \text{最新价}}{\text{开盘价}} \times 100\% & \text{如果 } (\text{最新价} - \text{开盘价}) < 0
    \end{cases}
    $$

---

### 4) 关键场景与演示描述

*   **场景一：初始化开盘价缓存**
    讲师在 `initOpenPriceCache` 方法中，首先使用 `redisTemplate.keys` 方法，根据一个通配符模式从 Redis 中获取所有股票的开盘价键。然后，他通过 `redisCacheManager.getCache` 获取对应的缓存对象，并遍历所有键，将缓存中的值（股票代码和开盘价）取出，存入本地的 `stockOpenCache` 映射中。

*   **场景二：计算涨跌幅**
    讲师在 `calcPriceRate` 方法中，首先判断开盘价是否为空。然后，他计算最新价与开盘价的差值。根据差值的正负，他分别计算涨跌幅，并乘以 100% 得到百分比。最后，他将计算好的涨跌幅返回。

*   **场景三：更新缓存**
    讲师在 `updateOpenPrice` 方法中，首先判断当前时间与开盘时间的差值是否在 0 到 5 分钟之间。如果满足条件，他调用 `updateOpenPrice` 方法，将计算好的最新价和涨跌幅信息更新到 Redis 缓存中。

*   **场景四：课程总结**
    讲师切换到课程的 Markdown 文档，总结本节内容，包括缓存初始化、涨跌幅计算和缓存更新等核心逻辑。他强调，这些逻辑是后续 K 线生成和行情处理的基础。
