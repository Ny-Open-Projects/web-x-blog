# 14-账户预警通知-开盘价与涨跌幅的计算处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们开始学习和讲解

行情服务去实现开盘价和涨跌幅的计算处理

对于没有提供着售价的行情员

咱们在前面的章节当中讲解了如何去计算实现收盘价

这里咱们就开始讲解如何去实现开盘价的计算

开盘价是当天开盘的第一口报价

据我们目前使用的数据员

在开之后拉取到的第一口报价就相当于是开盘价

实现的时候我们要考虑下

当天我们只能记录一次开盘价

不能被覆盖

这点要注意

如果被覆盖了

那这开盘价信息就是不准确的

隔天又要重新去更新开盘价信息

这个流程咱们来画一下

比如在一天当中

开盘呢

我们是从九点半开始

收盘呢

是从下午三点

我们在这里会将开盘价存储至两个地方

一个是JVM的MAP里面

另外一个是Ladies缓存里面

如果当天九点半开盘

所接收到的第一口行情报价

它会写入至MAP缓存里面

但是当天的交易时间范围之内

行情会源源不断的进行推送

如何去确保开盘价不会被重复更新呢

这个时候就会针对于MAP的缓存数据

做唯空判断

如果接收到的行情数据

它发现MAP里面没有数据信息

那么就会将行情写入到MAP里面

作为开盘价

这里面存放的就是开盘价信息

如果MAP里面已经写入了开盘价

后面的行情它要做校园判断

就不会再往上冲了

MAP里面重复写入行情信息

MAP在更新开盘价的时候

它同时会对Ladies缓存数据

将这里面的开盘价信息也做一个更新

可以看到存在两份开盘价信息

为什么要这么去做呢

咱们写一份开盘价的信息不就可以了吗

因为这个会涉及到效率问题

咱们知道在这里呢

它会根据每一口行情报价

做唯空判断处理

即便是通过Ladies的

操作

这个也需要进行远程的调用

效率来讲并没有自身MAP的判断处理

来得更快一些

这样呢就可以节省一定的开销

那大家可能又会存在疑问

将开盘价信息放置MAP缓存里面

不就可以了吗

为什么还要去放置Ladies里面呢

大家可以想一下

如果服务出现了当机

那这个MAP数据是不是就会产生丢失

这个时候该怎么去恢复开盘价呢

就可以从咱们之前写录的Ladies当中

将开盘价信息重新加载至MAP里面

这也就是为什么要去双写开盘价信息的原因

既要保障性能

又要保证它的稳定性

那还有一个处理

就是要在凌晨的时候

咱们要去更新开盘价信息

交易时间之外

要将MAP里面开盘价信息置为空

这样就能够保障

每个人的时间都能够更新到开盘价

好

那咱们回到讲义当中

看一下代码的具体实现

开盘价的计算处理是在stock world service下面做到实现

那咱们可以回到工程当中

定位到对应的实现类

在第五个步骤更新开盘价

这里会调用update open price的方法

这方法咱们可以看到

它首先会去拿取开盘价的缓存信息

这个stock open cash

它是一个MAP对象

我们可以看到

conclude hashMap

它是现成安全的hashMap

首先会对MAP里面的值做围空判断

如果是围空

说明之前并没有接收到开盘价信息

这里就需要将开盘价信息写入到缓存当中

接下来他就对Ladies的数据做了更新

同时的话

更新了自身的MAP缓存信息

然后咱们还要通过定时调度任务

去重置开盘价缓存信息

这里是安排在每天凌晨一点的时候执行

会保留一个小时的缓存时间

在一点和两点的时间段之内

每十分钟会去运行一次

确保缓存能够真正清除

这样第二天的开盘价就能够正常接收和更新

通过这些处理

还不能保证开盘价的数据正确性

如果是行情服务出现了故障

那么MAP里面的数据就会造成丢失

这个时候我们还需要增加一个处理

在服务启动的时候去加载开盘价的缓存

通过EditOpenPriceCache方法

可以看到这个方法的主要作用

就是从Ladies里面去加载开盘价的信息

他会拿到所有的开盘价缓存的key

然后进行便利

MAP的存储结构是根据stockid

去存储开盘价

有多少个股票产品在这里面

就会有多少条开盘价缓存记录

通过stockid拿到开盘价缓存信息之后

然后将它放置MAP里面

这样就完成了开盘价缓存信息的加载

好

这个就是行情服务里面开盘价的实现处理流程

接下来是涨跌服务的计算

咱们在做预警条件判断的时候

需要获取到当前股票行情的涨跌服务

涨跌服的计算它是依赖于着售价

我们可以看到它的具体计算公式

涨跌服是等于当前的最新报价减去着售价

然后再除以着售价

也就是以着售价为基准去计算它的涨跌服

最新价是做到缓存处理

涨跌服和最新价是一起放入了缓存当中

这样可以便于咱们后续业务功能的处理

股票行情的涨跌服

它是放在jetstock

whatlast里面增加了一个属性

这个属性增加了一个非持续化的注解

这个是动态变化的数据

并不会存储到数据库里面

那么咱们来看一下

涨跌服的计算处理逻辑是怎样的

咱们回到工程当中定位到对应的方法

可以看到在这里传递了两个弹数

一个是最新的行情报价

一个是着售价

首先会去计算它们的差值

也就是拿最新的行情报价减去着售价

接着的话会对价差做判断

如果是正数

这里返回的就是一个正值

那如果是等于0就直接返回为0

下面是负值

涨跌服的计算是存在这三种情况

大家不要忽略了负值的处理

在这里它会根据每一口行情报价

做对应的计算处理

咱们可以看到它的调用步骤

它是在订阅获取

产品行情的实时数据里面

做了处理

这是一个动态变化的值

通过涨跌服的计算处理

可以变于后续关联功能的业务处理

这一讲就是对行情服务

开盘价的处理流程

以及涨跌服的计算处理流程做了讲解

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情服务系统开发的教程，重点讲解了如何实现“开盘价”和“涨跌幅”的计算与缓存。讲师通过在 IntelliJ IDEA 中演示 `StockQuoteServiceImpl` 类的代码，详细说明了：

*   **开盘价计算**：如何使用一个 `ConcurrentHashMap` (`stockOpenCache`) 来缓存每个股票的开盘价，并在收到新的行情数据时，如果该股票的开盘价尚未设置，则将其设置为当前的最新价。
*   **涨跌幅计算**：如何通过 `calcPriceRate` 方法，根据最新的价格 (`lastPrice`) 和上一个收盘价 (`lastClosePrice`) 计算出涨跌幅比例。
*   **数据缓存与初始化**：如何利用 Redis 作为缓存层，通过 `@PostConstruct` 注解在服务启动时初始化开盘价缓存，并通过 `@Scheduled` 注解定时重置缓存，确保每天的开盘价能被正确记录。

整个过程体现了在分布式系统中，如何通过缓存、定时任务和数据校验来保证核心业务数据（如开盘价和涨跌幅）的准确性和时效性。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供具体的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：介绍本节目标，即实现开盘价与涨跌幅的计算。
*   **00:30 - 01:00**：讲解开盘价的定义和实现思路，展示 `stockOpenCache` 的声明。
*   **01:00 - 01:30**：演示 `updateOpenPrice` 方法，展示如何从行情数据中获取开盘价并写入缓存。
*   **01:30 - 02:00**：讲解如何通过定时任务 `scheduleResetOpenPriceCache` 来重置缓存，确保每天的开盘价能被正确记录。
*   **02:00 - 02:30**：讲解涨跌幅的计算逻辑，展示 `calcPriceRate` 方法的实现。
*   **02:30 - 03:00**：演示 `sendRealQuote` 方法，展示如何从第三方行情接口获取数据，并调用 `updateClosePrice` 方法更新收盘价，为涨跌幅计算做准备。
*   **03:00 - 03:30**：总结本节内容，强调缓存和定时任务在保证数据准确性中的作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**：`3.4 行情服务实现开盘价与涨跌幅的计算`
*   **核心概念**：
    *   开盘价是当天开盘的第一口报价。
    *   涨跌幅 = (最新价 - 收盘价) / 收盘价 * 100%。
    *   涨跌幅比例的单位是%，例如 `2.28` 代表 `0.228`。
*   **代码结构**：
    *   `StockQuoteServiceImpl` 类是核心实现类。
    *   `stockOpenCache` 是一个 `Map<Long, Long>`，用于缓存股票ID到开盘价的映射。
    *   `calcPriceRate` 方法用于计算涨跌幅。

#### 代码关键内容

*   **开盘价缓存初始化**：
    ```java
    // 标记股票是否需要写入开盘价
    public Map<Long, Long> stockOpenCache = new ConcurrentHashMap<>();

    // 更新开盘价
    private void updateOpenPrice(TradeStockQuoteLast quoteList) {
        Long openPrice = stockOpenCache.get(quoteList.getStockId());
        if(openPrice == null) {
            // 待写入开盘价
            Cache curOpenPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR);
            curOpenPriceCache.put(quoteList.getStockId(), quoteList.getLastPrice());
            stockOpenCache.put(quoteList.getStockId(), quoteList.getLastPrice());
        }
    }
    ```

*   **定时重置开盘价缓存**：
    ```java
    @Override
    @Scheduled(cron = "0 0/10 1 ? * *")
    public void scheduleResetOpenPriceCache() {
        stockOpenCache.keySet().forEach(stockId -> {
            stockOpenCache.put(stockId, null);
        });
    }
    ```

*   **涨跌幅计算方法**：
    ```java
    private double calcPriceRate(Long lastPrice, Long lastClosePrice) {
        double priceRate = 0;
        if(null != lastClosePrice) {
            long diffPrice = MathUtils.sub(lastPrice, lastClosePrice);
            if(diffPrice > 0) {
                priceRate = MathUtils.divDouble(diffPrice, lastClosePrice) * 100;
            } else if(diffPrice == 0) {
                priceRate = 0;
            } else {
                priceRate = -MathUtils.divDouble(diffPrice, lastClosePrice) * 100;
            }
        }
        return priceRate;
    }
    ```

*   **初始化缓存**：
    ```java
    @PostConstruct
    public void initOpenPriceCache() {
        Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY + "*");
        if(null != keys && !keys.isEmpty()) {
            Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
            keys.stream().forEach(key -> {
                // Key转换，获取stockId
                Long stockId = Long.valueOf(key.replaceAll(regex: GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY + ".*", ""));
                ValueWrapper valueWrapper = cache.get(stockId);
                if(null != valueWrapper) {
                    Long value = (Long)valueWrapper.get();
                    stockOpenCache.put(Long.valueOf(stockId), value);
                }
            });
        }
    }
    ```

---

### 4) 关键场景与演示描述

1.  **场景一：开盘价缓存初始化与更新**
    *   **描述**：讲师首先在 `StockQuoteServiceImpl` 类中声明了一个 `ConcurrentHashMap` 用于缓存开盘价。然后，通过 `updateOpenPrice` 方法，当收到新的行情数据时，如果该股票的开盘价尚未设置，则将其设置为当前的最新价，并同时更新 Redis 缓存。
    *   **技术点**：展示了如何使用 `ConcurrentHashMap` 进行线程安全的缓存操作，以及如何结合 Redis 进行分布式缓存。

2.  **场景二：定时重置开盘价缓存**
    *   **描述**：讲师演示了如何使用 `@Scheduled` 注解来定时重置开盘价缓存。通过设置 `cron = "0 0/10 1 ? * *"`，系统会在每天凌晨1点执行，每10分钟重置一次缓存，确保当天的开盘价能被正确记录。
    *   **技术点**：展示了 Spring Boot 中定时任务的实现方式，以及如何通过重置缓存来保证数据的准确性。

3.  **场景三：涨跌幅计算逻辑**
    *   **描述**：讲师讲解了如何计算涨跌幅比例。通过 `calcPriceRate` 方法，根据最新的价格和上一个收盘价，计算出涨跌幅比例。如果最新价大于收盘价，则为正数；如果相等，则为0；如果小于，则为负数。
    *   **技术点**：展示了如何通过简单的数学运算来计算涨跌幅，并通过 `MathUtils` 工具类进行数值处理。

4.  **场景四：数据初始化与缓存同步**
    *   **描述**：讲师演示了如何在服务启动时，通过 `@PostConstruct` 注解初始化开盘价缓存。通过 Redis 获取所有股票的开盘价，并将其同步到本地的 `stockOpenCache` 中。
    *   **技术点**：展示了如何在服务启动时进行数据初始化，以及如何通过 Redis 进行数据同步。

5.  **场景五：行情数据处理与收盘价更新**
    *   **描述**：讲师演示了 `sendRealQuote` 方法，该方法用于从第三方行情接口获取实时行情数据。在获取到数据后，会调用 `updateClosePrice` 方法更新收盘价，为后续的涨跌幅计算做准备。
    *   **技术点**：展示了如何通过第三方接口获取数据，并通过缓存机制进行数据处理。

---

以上是根据视频画面进行的结构化技术分析。
