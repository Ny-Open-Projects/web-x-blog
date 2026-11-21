# 17-第三方行情源-行情缓存与持久化处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着咱们开始学习行情缓存与持久化的处理

之前咱们实现了第三方行情的对接

拿到了行情数据将它放入到缓存当中

那么这些缓存数据咱们也将它做一个持久化

记录股票产品的实时行情数据

首先咱们要去集成Ladies配置

将Ladies Configuration拖比到代码当中

放在咱们的Configure目录下面

我们做一个拖比

大家侧重掌握好整个的集成配置流程

在这里要去定义一个Ladies Template的模板

配置它的序列化方式

配置完成之后

要注意在上面加上Enavocation的注解

这个注解的意思就是开启缓存功能

好 咱们回到讲习当中

接着咱们就要去添加POM依赖

这里面只需要添加两个依赖

我们拖比到POM文件里面

这里咱们已经拖比进来了

这两个依赖分别是自动化缓存依赖

以及Ladies缓存依赖

Spring Cache它是一个缓存封装组件

Ladies它只是其中一种实现

还可以支持Memcache、Incache等不同的缓存中间件

如果不采用任何中间件

Cache它默认就会放在本地的JVM内存当中

接下来咱们就对行情持久化做一个业务实现

咱们回到代码当中

在咱们的业务实现类里面做具体实现

咱们把方法定义在最下面

public void

这个是由定时任务去调度实现

咱们先将业务逻辑实现完成

定时任务配置这块在下个章节咱们再做详细讲解

给方法加上注释

这个是定时持久化行情缓存数据

执行频率呢?

一分钟执行一次

接着咱们打印入字

行情持久化

定时任务处理给他一个提示

开始执行

外层的cache补货将异常的打印出来

咱们看一下具体业务实现逻辑是怎样的

第一步呢

通过key来做一个模糊搜索

找到所有的行情缓存信息

set screen

通过latest template模板接口呢

进行模糊比配

concentrate

他的key是stock,water,generate,deline

咱们要加上他的模糊比配的通费符

然后做一个围攻判断

上面的是keys

印钱呢

key不能空

然后咱们要获取缓存管理器

通过latest cache manager

获取对应的缓存对象

然后呢咱们要获取缓存管理器

global consistence

传递了stock,water,deline

第二步呢咱们要针对模糊搜索获取的系信息

做便利处理

仍然采用流逝方式进行便利

这里呢做一个排序

当然如果是不排的话呢也没关系

行情信息呢这个顺序咱们没有业务要求

simply value

把check对象

拿到对应的值

做一个强转

通过cache拿到对应的值

然后又做一个替换

将他的前对呢替换掉

后面呢还要再加两个猫号

slim cache呢

他存储key的时候默认会附带引猫号作为后对

附带进去

所以咱们在这里呢要去除两个猫号

然后做围攻判断

拿到最新行情对象water last

做一个强转

value a check.get对象

第三个步骤呢咱们要根据股票id

以及呢报价时间

去数据库查找有没有对应的数据

避免生成重复的行情数据

那咱们要通过一个数据层接口做一个查询

stop water last

这个呢就叫db

bought last

跟上面这个对象呢做一个区分

get stock water last

然后get distinct

根据股票id以及时间呢

去获取对应的对象

这个呢传递报价时间

咱们可以看一下这个搜狗方法的实现

在这里他是根据股票id和时间说呢获取对应的对象

由jp呢帮咱们自动生成对应的搜狗实现了他的数据查询

咱们做一个围攻判断

如果

db bought last不等于空

bought last呢

咱们加上id做个记录

记录数据库的数据id

第四个步骤

如果

数据存在

那么根据id进行更新

这也是为什么在这里面要设置id的原因

如果不存在

c5方法呢

他就会保存并生成新的数据

咱们就要采用数据层接口

要用c5方法

传递bought last对象

注意

这里面的并非db bought last

是从缓存当中所获取的行情对象

jp方法进行保存的时候呢

会根据id进行判断

如果id已经存在呢

他就做更新处理

如果不存在呢

他就会做影射的

也就是会插入新的数据

好最后一个步骤呢

咱们要去删除行情生成所需的版权数据

catch

invocate

bought last

传递的股票编号

再加上他的分割符

还有他的报价时间

这个和咱们从第三方行情

所保存的缓存数据格式呢

是一致的

可以看到

code加上time

清除完成之后呢

咱们就完成了持久化行情缓存数据

咱们再回到讲义当中

在这里我们是通过定时任务

从缓存当中呢

获取行情数据

再加工

然后持久化到数据库当中

同时呢

我们还做一个事情

将缓存信息进行清除

这里注意整个处理流程呢

要做去重判断

根据股票ID和时间呢

作为依据

在这里面

我们传递了相应的条件进行数据查询

目的的话呢

是为了防止记录重复的行情数据

JPE呢

会通过这个ID进行相应的更新

在这里呢

咱们将他的数据ID

放入到咱们的code last对象里面

好

在这里呢

咱们就实现了行情的缓存

以及持久化的处理

那这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据处理系统的开发教程，重点讲解了如何在 Spring Boot 应用中集成 Redis 缓存，并实现一个定时任务，将缓存中的行情数据持久化到数据库中。视频内容主要围绕 `StockQuoteServiceImpl` 类中的两个核心方法：`initOpenPriceCache()`（初始化缓存）和 `schedulePersistCache()`（定时持久化）。演示了如何使用 Spring Cache 注解、RedisTemplate 进行缓存操作，并通过定时任务将数据写入数据库，同时处理了缓存键的模式匹配、数据转换和去重逻辑。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程导航与章节概览。画面显示了 Markdown 文件的目录结构，当前章节为“3.5 行情缓存与持久化处理”。
*   **00:05 - 00:15**: 缓存配置与依赖。讲解了如何在 `pom.xml` 中添加 Spring Boot 缓存和 Redis 的依赖。
*   **00:15 - 00:30**: 初始化缓存方法 `initOpenPriceCache()`。演示了如何通过 `redisTemplate.keys()` 获取缓存键，并使用 `stream().forEach` 对每个键进行处理。
*   **00:30 - 00:45**: 缓存键的模式匹配与数据转换。展示了如何使用正则表达式 `replaceAll` 将缓存键转换为业务对象 ID。
*   **00:45 - 01:00**: 持久化缓存方法 `schedulePersistCache()`。讲解了如何通过定时任务获取所有缓存键，并将数据持久化到数据库。
*   **01:00 - 01:15**: 数据库持久化与去重。演示了如何使用 JPA Repository 的 `save` 方法将数据写入数据库，并通过 `key` 字段进行去重。
*   **01:15 - 01:30**: 课程总结与下一章节预告。画面切换到“3.6 Spring Boot 整合定时任务”章节，预告了后续内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.5 行情缓存与持久化处理”。
    *   **章节标题**: “3.6 Spring Boot 整合定时任务”。
    *   **关键说明**: “通过定时任务，从缓存获取行情数据，再加持持久化至数据库中，同时将已持久化的数据从缓存清空。”
    *   **关键说明**: “这里要去做重判断，根据股票ID与时间作为依据，防止记录重复的行情数据。”

*   **代码关键内容**:

    **1. 初始化缓存方法 `initOpenPriceCache()`**

    ```java
    @PostConstruct
    public void initOpenPriceCache() {
        Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
        if (null != keys && keys.isEmpty()) {
            // 获取缓存对象，对每个key进行处理
            Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
            keys.stream().forEach(key -> {
                // key转换，获取stockId
                Long stockId = Long.valueOf(key).replaceAll(regexp: GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY, "");
                Cache.ValueWrapper valueWrapper = cache.get(key);
                if (null != valueWrapper) {
                    // 将缓存数据写入数据库
                    stockOpenCache.put(Long.valueOf(stockId), value);
                }
            });
        }
    }
    ```

    **2. 定时持久化方法 `schedulePersistCache()`**

    ```java
    public void schedulePersistCache() {
        // 通过key做模糊搜索，找到所有的行情缓存信息
        Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.STOCK_QUOTE_GENERATE_KLINE_KEY + "*");
        if (null != keys && keys.isEmpty()) {
            // 获取缓存管理器
            Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_KLINE_KEY);
            // 针对模糊搜索获取的key进行处理，做去重
            keys.stream().sorted().forEach(key -> {
                SimpleValueWrapper valueWrapper = (SimpleValueWrapper) cache.get(key);
                if (null != valueWrapper) {
                    // 获取股票对象
                    TradeStockQuoteLast tradeStockQuoteLast = new TradeStockQuoteLast();
                    // 设置股票对象的属性
                    tradeStockQuoteLast.setStockId(valueWrapper.getStockId());
                    tradeStockQuoteLast.setPrice(valueWrapper.getPrice());
                    tradeStockQuoteLast.setVolume(valueWrapper.getVolume());
                    // 保存到数据库
                    tradeStockQuoteLastRepository.save(tradeStockQuoteLast);
                    // 从缓存中删除
                    cache.evict(key);
                }
            });
        }
    }
    ```

    **3. 依赖配置 (pom.xml)**

    ```xml
    <!-- 自动化缓存依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-cache</artifactId>
        <version>${spring-cloud-starter.version}</version>
    </dependency>

    <!-- 缓存依赖 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-redis</artifactId>
        <version>${spring-cloud-starter.version}</version>
    </dependency>
    ```

---

### 4) 关键场景与演示描述

*   **场景一：缓存配置与依赖检查 (00:05 - 00:15)**
    *   **描述**: 讲师在 IDE 中打开 `pom.xml` 文件，高亮显示了两个必需的依赖项：`spring-boot-starter-cache` 和 `spring-boot-starter-data-redis`。强调了 `@EnableCaching` 注解的必要性。

*   **场景二：初始化缓存方法演示 (00:15 - 00:30)**
    *   **描述**: 讲师在 `StockQuoteServiceImpl` 类中定位到 `initOpenPriceCache()` 方法。通过 `redisTemplate.keys()` 方法获取符合模式的缓存键，并使用 `stream().forEach` 遍历处理。演示了如何将缓存键转换为股票 ID，并将数据写入 `stockOpenCache`。

*   **场景三：缓存键模式匹配与数据转换 (00:30 - 00:45)**
    *   **描述**: 讲师在代码中使用 `replaceAll` 方法，将缓存键中的特定模式（如 `STOCK_QUOTE_OPEN_PRICE_CUR_KEY`）替换为空字符串，从而提取出股票 ID。演示了如何将缓存中的值包装成 `SimpleValueWrapper` 对象。

*   **场景四：定时持久化方法演示 (00:45 - 01:00)**
    *   **描述**: 讲师在 `schedulePersistCache()` 方法中，使用 `redisTemplate.keys()` 获取所有符合 `STOCK_QUOTE_GENERATE_KLINE_KEY` 模式的缓存键。通过 `stream().sorted().forEach` 对键进行排序和处理。

*   **场景五：数据库持久化与去重 (01:00 - 01:15)**
    *   **描述**: 讲师在 `schedulePersistCache()` 方法中，使用 `TradeStockQuoteLastRepository.save()` 方法将数据保存到数据库。演示了如何通过 `key` 字段进行去重，防止重复记录。

*   **场景六：课程总结与下一章节预告 (01:15 - 01:30)**
    *   **描述**: 讲师切换到 Markdown 文档的“3.6 Spring Boot 整合定时任务”章节，总结了本节内容，并预告了下一节将讲解如何整合 Spring Boot 的定时任务功能。
