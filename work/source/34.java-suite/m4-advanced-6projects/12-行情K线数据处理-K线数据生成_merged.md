# 12-行情K线数据处理-K线数据生成 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始学习行情服务K线生成功能的实现

之前咱们已经实现了定时化去持久行情数据

之前咱们实现了定时持久化行情缓存

但是并没有去生成K线数据

在这里咱们就来做一个实现

回到代码当中

打开stock world service implement这个类

在schedule for system cache方法里面

添加一个处理步骤

这个是在最新行情数据保存方法后面去做的处理

这里处理并生成K线数据

进一个process KLAN的方法

传递Quadras的最新行情数据

我们来实现plus KLAN这个方法

这个方法的作用是生成K线行情数据

我们来做个具体实现

首先从缓存里面

获取K线行情数据

shed stock KLAN

这个是查询MAP缓存

我们去定义K线的缓存MAP

采用MAP结构

long 气质为long

存储的是股票ID

然后放入stock KLAN对象

KLAN MAP

然后放入stock KLAN对象

为了保障现场安全

这里是conclude的MAP

它是K线的缓存数据

再回到刚才的K线生成逻辑

生成K线必须要知道当前周期之内有没有K线数据

那么从KLAN MAP里面去查找

根据Quadras里面的股票ID做个唯空判断

如果是没有找到

那么我们叫生成KLAN MAP里面去查找

然后再去查找新的K线

这个情况是可能存在的

比如说咱们重启了服务

或者是新的一天行情

之前的缓存已经清除

那么就要生成新的K线数据

给它一个方法

new KLAN

port传递Quadras对象

new KLAN是生成一个新的K线对象

这个方法其实就是将Quadras的转换为shared stock KLAN对象

实现逻辑比较简单

咱们从讲义当中做个copy

可以看到它将Quadras里面的属性赋予给shared stock KLAN的这个对象

之前咱们讲过K线的生成有四个关键价格

一个是开盘价

一个是收盘价

还有最高价以及最低价

大家可以看到在这里它设置的全部都是最新的行情报价

为什么是最新行情报价呢

因为你是一个新的行情K线

这里接收的是第一口的行情报价

这个是它之前的K线

这个咱们就当做是新生成的K线

它的第一口行情报价

新的K线数据其实就是一根线

所以在这里它不会存在四个价差

他们这四个价格全部都是一致的

也就是最新的行情报价

随着交易时间的变化

比如说之前的价格这里是十块钱

后面变成了十一块钱

那么它的收盘价在这里就会产生一个变化

形成了一个新的K线图

对不对

好

这一点大家要理解清楚

那再回到刚才的处理逻辑

Process K蛋方法里面

生成完新的K线

要将数据放置MAP里面

Word Last

Get Stock ID

K蛋

如果行情K线已经存在

这里是行情K线存在的处理逻辑

如果是存在该怎么处理呢

那么首先要判断

是否达到指定的周期

这里我们的周期是以一分钟为单位

所以要判断时间差

是否超过K线的指定周期

那首先要取到时间差

Word Last

Get Time

这个要减去K蛋当时存储的时间

拿最新的行情报价时间

减去上一个K线的报价时间

就是行情的时间差

那么我们就要判断这个时间差

是不是超过指定的周期

也就是一分钟

如果配置的是五分钟

那么就以五分钟为单位

就以五分钟为单位

那么就以五分钟为单位

那么就以五分钟为单位

就以五分钟作为判断

这里配置的是一分钟

那么就以一分钟作为判断

Verbal Consistency

单位为秒

获符合条件

说明时间差在K线周期范围之内

那就要更新K线行情数据

先更新它的最低价

那么要做一个比较

拿取最新的行情数据

最新的价格

判断K线里面最低的价格

如果是小于就要去更新最低价

K线.set price now

for the last

get last price

将最新价设置进去当做最新的最低价

然后要去处理最高价

同样也要做一个判断

for the last

get last price

K线

判断是否大于它的最低价

如果是大于

同样我们要去更新它的K线最高价格

将最新的行情报价信息

它的价格设置进去

这个是更新最高价

最后就是更新收盘价

Kline.set price close for the last

最新价作为它的收盘价

如果是大于的

我们就要去更新它的收盘价

是超过了行情的指定周期

也就是时间差

超过了咱们指定的K线周期

Global Consistency

Kline period 60

超过了60秒

那就要

进行持久化处理

超过K线周期

需要持久化

并且呢

要生成

新的

K线数据

生成新的K线要记录

上一个周期的K线

它的收盘价格

记录

上一个周期的

收盘价格

上一个K线周期

定义一个变量

long last close price要等于1

给它一个默认值

就为Yellow

然后去持久化行情数据

外围catch一长

记录一长日子

保存的时候要去计算K线

它的成交金额

还有它的成交量

Kline.setamount

bought last

大家注意一下

行情员里面的

金额

它是当日的累计金额

还有它的成交量

是当日

累加的量

累加的总量

那么我们需要计算它的差值

通过总的成交量

减去K线

已经记录的成交金额

那么就是当前周期的

金额差值

也就是当前周期的成交金额

同样

成交量

也是这么去处理

volume

for the last

get volume

然后

去设置

K线的时间

通过一个函数做转换

将时间转换为分钟记录

这是按分钟划分的

行情周期

单位精确到分钟就可以

然后我们要去给

上一个周期的收盘价复值

Kline.get price

close

接着就设计了sharding.jdbc的

分表处理

要去给它设置一个全局的唯一ID

Global

要将全局唯一ID生成器注入进来

将它加入进去

autowide注入进来

全局唯一ID生成器注入进来

全局唯一ID生成器注入进来

全局唯一ID生成器注入进来

全局唯一ID生成器注入进来

全局唯一ID生成器注入进来

全局唯一ID生成器注入进来

再回到刚才的处理逻辑

修改

Global ID generator

获取下一个全局序列ID

如何去保存呢

还是跟咱们之前的接口处理一样的

SharedStore.Kline

要用C5方法

这个数据层的操作是没有任何变化

Sharding.jdbc的分表方案

对业务实现来讲是完全透明

保存完成之后要去生成新的K线

Kline

6.Kline

Ford Last

做一个转换

要去设置

他的上一个周期的收盘价

就是着手价

这里的着手价并非昨天的收盘价

而是指他的上一个周期K线的收盘价格

将它放置Map里面

Ford Last

Guest Talk ID

Kline

再打印一个日志

给出

日志提示

Ford Last

In

方法名称copy过来

进入到这个逻辑

说明时间差是等于当前周期的时间

也就是dif time等于60秒或者是时间差计算错误

这个情况是不需要处理

给出一个错误提示就可以

好

那这里就完成了行情K线的生成处理

我们回到讲义当中

回顾一下整体实现处理流程

这里K线3分钟生成

也就是行情周期的最小力度

具备1分钟的K线

那客户端拿到这个数据

就可以加工生成

不同周期的比如说

10K

日K周K月K等数据

K线呢

它是通过

实时行情数据生成的

先建立Map缓存

如果在Map当中不存在

我们就去初始化一条

行情K线数据

如果K线存在于Map缓存当中

还需要去判断是否达到指定的周期

这里设定的是1分钟

也就是60秒

如果是在行情周期之内

也就在1分钟之内

那么就更新缓存的K线信息

这里要注意成交量和成交金额的计算

它并非当前实时行情的成交量

我们回到代码

并非当前实时行情的成交量

因为这个金额呢

它是当日的累加总量

所以我们要去

计算它的差值

这样才能得到

当前周期的

实际成交量以及它的实际成交金额

如果是超出1分钟

我们就进行持续化

要生成一条新的K线记录

K线生成

可以直接放在

实时行情处理之后

但是

要在清除

实时缓存之前

这个是有序惯例的处理步骤

一定要按顺序处理

我们可以看到

Process Klan

这个方法呢

它是放在删除行情缓存之前

这样

在处理K线数据的时候

才能拿到所需要的

行情缓存信息

如果你先将缓存给删除了

那么行情K线数据

就没法进行正常的生成

好这一讲就对行情服务

K线生成功能的实现

那这一讲内容

就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频片段是关于一个股票行情系统中“K线生成功能”的实现讲解。讲师通过在 IntelliJ IDEA 开发环境中，逐步演示如何在 `StockQuoteServiceImpl` 类中编写 `scheduledPersistCache` 定时任务方法，以及其核心的 `processKline` 方法。该方法负责从缓存中获取最新的行情数据，根据时间差判断是否需要生成新的K线，或更新现有K线，并最终将生成或更新后的K线数据持久化到数据库中。整个过程涉及 Spring Boot、Redis、MyBatis-Plus 等技术栈，重点展示了如何处理K线数据的生成、更新和持久化逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示课程大纲，定位到第3.3节“行情服务K线生成功能实现”。
*   **00:00:05 - 00:00:15**: 讲师介绍 `StockQuoteServiceImpl` 类，并展示其成员变量，包括用于操作数据库的 `tradeStockQuoteLastRepository` 和 `tradeStockKlineRepository`，以及用于对接第三方行情数据的 `juheThirdApi` 和 Redis 缓存管理器。
*   **00:00:15 - 00:00:30**: 讲师进入 `scheduledPersistCache` 方法，该方法被 `@Scheduled` 注解标记，用于定时持久化缓存中的K线数据。
*   **00:00:30 - 00:00:45**: 讲师演示如何通过 Redis 的 `keys` 方法获取所有K线缓存的键，并初始化一个 `cache` 变量。
*   **00:00:45 - 00:01:00**: 讲师进入核心方法 `processKline`，该方法用于处理单条行情数据，生成或更新K线。
*   **00:01:00 - 00:01:15**: 讲师演示如何从 `klineMap` 缓存中获取已有的K线对象，如果不存在则创建新的K线对象。
*   **00:01:15 - 00:01:30**: 讲师讲解如何计算时间差 `diffTime`，并判断是否在K线的指定周期内（例如1分钟）。
*   **00:01:30 - 00:01:45**: 讲师演示如何更新K线的最低价、最高价和收盘价。
*   **00:01:45 - 00:02:00**: 讲师演示如何计算K线的成交量和成交金额，并调用 `tradeStockKlineRepository.save` 方法将K线数据持久化到数据库。
*   **00:02:00 - 00:02:15**: 讲师演示如何在K线数据生成后，从缓存中删除对应的键，以避免数据重复。
*   **00:02:15 - 00:02:30**: 讲师总结整个 `processKline` 方法的逻辑，并指出其核心是处理K线数据的生成与更新。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.3 行情服务K线生成功能实现`。
    *   代码注释：`// 定时持久化行情缓存（设定为每隔一分钟执行一次）`。
    *   代码注释：`// 从缓存获取K线行情数据`。
    *   代码注释：`// 生成新的K线数据`。
    *   代码注释：`// 行情线存在的处理逻辑`。
    *   代码注释：`// 计算K线的成交金额与成交量`。
    *   代码注释：`// 记录上一个K线的收盘价`。
    *   代码注释：`// 删除行情生成所用的缓存数据`。

*   **关键代码片段**:

    ```java
    @Override
    @Scheduled(cron = "0 0/1 * * * ?")
    public void scheduledPersistCache() {
        log.info("定时任务[scheduledPersistCache] =====>>> 开始执行");
        try {
            // 1. 通过key做模糊搜索，找到所有的K线缓存信息.
            Set<String> keys = redisTemplate.keys(GlobalConstants.STOCK_QUOTE_GENERATE_KLINE_KEY + "*");
            if (null != keys && !keys.isEmpty()) {
                // 获取缓存管理器
                Cache cache = ...;
                // 遍历所有缓存键
                for (String key : keys) {
                    // 获取缓存中的K线数据
                    TradeStockKline kline = cache.get(key);
                    // 处理K线数据
                    processKline(kline);
                }
            }
        } catch (Exception e) {
            log.error(e.getMessage(), e);
        }
    }
    ```

    ```java
    private void processKline(TradeStockQuoteLast quoteLast) {
        // 从缓存获取K线行情数据
        TradeStockKline kline = klineMap.get(quoteLast.getStockId());
        if (null == kline) {
            // 生成新的K线数据
            kline = newKline(quoteLast, kline);
            klineMap.put(quoteLast.getStockId(), kline);
        } else {
            // 行情线存在的处理逻辑
            long diffTime = quoteLast.getTime() - kline.getTime();
            if (diffTime > 0 && diffTime < GlobalConstants.KLINE_PERIOD_60) {
                // 时间在K线周期范围内，更新K线行情数据
                // 更新最低价
                if (quoteLast.getLastPrice() < kline.getPriceLow()) {
                    kline.setPriceLow(quoteLast.getLastPrice());
                }
                // 更新最高价
                if (quoteLast.getLastPrice() > kline.getPriceHigh()) {
                    kline.setPriceHigh(quoteLast.getLastPrice());
                }
                // 更新收盘价
                kline.setPriceClose(quoteLast.getLastPrice());
                // 计算K线的成交金额与成交量
                kline.setAmount(quoteLast.getAmount());
                kline.setVolume(quoteLast.getVolume());
                // 设置K线的最后更新时间
                kline.setTime(cvtMinuteTime(quoteLast.getTime()));
                // 保存到数据库
                tradeStockKlineRepository.save(kline);
            } else if (diffTime >= GlobalConstants.KLINE_PERIOD_60) {
                // 超过K线周期，需要持久化，并且要生成新的K线数据
                // 记录上一个K线的收盘价
                long lastClosePrice = kline.getPriceClose();
                // 生成新的K线
                kline = newKline(quoteLast, kline);
                klineMap.put(quoteLast.getStockId(), kline);
                // 保存到数据库
                tradeStockKlineRepository.save(kline);
                // 删除缓存中的旧K线数据
                cache.evict(key + quoteLast.getTime());
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：定时任务的创建与执行** (00:00:05 - 00:00:15)
    *   讲师在IDE中打开 `StockQuoteServiceImpl` 类，展示了其成员变量，包括用于操作数据库的 `tradeStockQuoteLastRepository` 和 `tradeStockKlineRepository`，以及用于对接第三方行情数据的 `juheThirdApi` 和 Redis 缓存管理器。
    *   讲师强调了 `@Scheduled` 注解的作用，即定时执行 `scheduledPersistCache` 方法。

*   **场景二：K线数据的生成与更新逻辑** (00:00:45 - 00:01:45)
    *   讲师在 `processKline` 方法中，首先从 `klineMap` 缓存中获取已有的K线对象。
    *   如果没有找到，则创建一个新的K线对象，并将其放入缓存中。
    *   如果找到了，则计算当前行情数据与K线数据的时间差 `diffTime`。
    *   如果时间差在K线周期内（例如1分钟），则更新K线的最低价、最高价和收盘价。
    *   如果时间差超过K线周期，则生成一个新的K线对象，并将其保存到数据库中。

*   **场景三：K线数据的持久化与缓存清理** (00:01:45 - 00:02:30)
    *   讲师演示了如何调用 `tradeStockKlineRepository.save` 方法将K线数据持久化到数据库。
    *   讲师演示了如何在K线数据生成后，从缓存中删除对应的键，以
