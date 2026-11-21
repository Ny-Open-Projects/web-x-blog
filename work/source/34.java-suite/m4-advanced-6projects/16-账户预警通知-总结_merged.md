# 16-账户预警通知-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来 接着咱们对本章内容做一个回顾和总结

首先咱们回顾下本章的主要学习目标

在这里咱们要去实现指引止损的通知模板设置功能

然后咱们要去实现账户预警通知的设置功能

接下来要去生成账户的预警通知记录

最后就是掌握开盘价和涨跌幅的计算处理流程

好 接着咱们回顾下本章所讲解的具体内容

首先咱们讲解了实现预警通知模板的设置接口

预警通知模板要支持内线变量

这样是可以灵活去修改和维护

接下来咱们实现了账户预警通知的设置接口

这个接口是由客户端进行调用

每个用户他可以设置自己的预警条件

账户的预警通知设置完成之后

由于行情是在反复进行变化

可能会多次符合预警条件

这个时候用户如果是频繁接收到通知

体验性就不太友好

所以在做处理的时候要做相应的判断

这里我们是设定在10分钟之内

不会去重复接收到相同的预警消息

如果一天之内是有多次触发

那么最多也就发送三次

这个大家也可以根据自身的业务需要

做相应的调整

这种推送通知信息

最好是不要太密集

或者是太频繁

那接着咱们在调度服务里面

实现了账户预警通知记录的生成

接下来咱们讲解了调度服务

去实现和生成账户的预警通知记录

预警通知呢

需要较高的实时性

但是它也能容许一定的延迟

咱们在实现的时候

要保障实时性的同时

又要兼顾它的处理性能

咱们在这里是采用了调度任务的方式

我们在这里是采用了调度任务的方式

做处理

结合缓存的运用

保障这块逻辑的处理

能够有较好的性能和实时性

在往下面

咱们还讲解了行情服务里面

如何去实现开盘价和涨跌幅的计算

涨跌幅是要用于预警通知记录的生成处理

掌握好开盘价和涨跌幅的计算处理流程

能够拓展咱们业务层面的知识

最后咱们就对整体的功能做了一个测试

和验证

通过三种场景做了相应的测试

验证的整体结果是能够正常处理

最后咱们再来总结一下

本章是以止盈止损为例

讲解了账户预警通知功能的设置

以及数据的生成

任何一个项目的预警通知

它都有可能是一个高频行为

所以我们要去充分考虑它的性能

以及整体服务的负载

这里我们有很多地方都加入了缓存的处理

大家在咱们的讲解过程当中也应该可以知道

目的是为了保障服务的处理性能

为什么咱们要在这里去生成预警通知记录

而不是直接发送呢

因为这样做的目的

一是可以做到数据的可追溯性

便于后续的统计

如果咱们不做生成存储

那么数据发送之后就没有了

第二点是可以保障服务的可靠性

确保每条数据呢

都能够发送到

正确处理

即便是服务当机或者发送的过程当中出现问题

也不会造成数据的丢失

第三呢就是结偶式的设计

为什么要采用结偶式设计呢

因为生成通知记录之后

还要再做发送处理

通过分离之后

即便某个环节出现了错误

它也不会影响整个流程

能够提升整体的稳定性

而且如果是某个环节出现了瓶颈

那么咱们可以针对性的去做相应的过程

不会影响其他环节的业务处理

同时也能够便于一步堆叠的揭露

预警通知记录生成完成之后

就可以呢将消息发布到堆叠当中

那么堆叠的订阅者接收到消息之后

就可以进行消息的推送

从而能够提升整体的预警通知记录的吞吐量

可以支撑海量数据的处理场景

好

这一讲就是对本章内容的回顾与总结

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为一个技术实现教程，主要讲解如何在金融交易系统中实现“账户预警通知”功能。课程以“止盈止损”为具体业务场景，详细阐述了从用户设置预警条件、系统生成预警记录，到最终将通知推送给用户的完整技术实现流程。核心内容包括：定义接口、实现数据库表结构、编写服务代码、引入缓存机制以提升性能和可靠性，并通过数据库查询验证最终结果。课程强调了系统设计中对高并发、数据一致性、可扩展性的考量。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，明确本章主题为“第2章 用户预警通知的设置与生成”。
*   **00:00:05 - 00:00:15**：介绍本章目标，包括实现预警模板设置、账户预警设置、生成预警记录以及开盘价与涨跌幅的计算。
*   **00:00:15 - 00:00:30**：讲解实现步骤，包括实现预警模板和账户设置接口、调度服务生成记录、行情服务计算以及功能验证。
*   **00:00:30 - 00:00:45**：进入“实现”部分，首先讲解“实现账户预警通知设置接口”，展示数据库表 `t_account_warn_setting` 的结构。
*   **00:00:45 - 00:01:00**：展示 gRPC 接口定义，修改 `StockUserService.proto` 文件，增加 `accountWarnSetting` 方法。
*   **00:01:00 - 00:01:15**：展示服务端代码实现，包括检查用户接收通知方式、查询预警设置、新增或更新设置。
*   **00:01:15 - 00:01:30**：讲解缓存机制，展示 `loadAccountWarnSettingCache` 方法，将预警设置加载到缓存中。
*   **00:01:30 - 00:01:45**：讲解定时任务，展示 `scheduledAccountWarnSettingCache` 方法，用于定时刷新缓存。
*   **00:01:45 - 00:02:00**：讲解行情服务改造，展示 `StockQuoteServiceImpl` 中的 `updateOpenPrice` 方法，用于计算并缓存开盘价。
*   **00:02:00 - 00:02:15**：进入“功能验证”部分，展示最终生成的预警通知记录表 `t_account_warn_notify_message`。
*   **00:02:15 - 00:02:30**：总结本章内容，强调预警通知的三个核心设计原则：数据可追溯性、服务可靠性、流程解耦。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：第2章 用户预警通知的设置与生成。
    *   **目标列表**：实现止盈止损模板设置功能、实现账户预警通知设置功能、生成账户预警通知记录、开盘价与涨跌幅的计算处理。
    *   **步骤列表**：实现预警通知模板设置接口、实现账户预警通知设置接口、实现生成账户预警通知记录、行情服务改造、功能验证。
    *   **总结要点**：
        1.  预警通知生成数据记录，一是做到数据的可追溯性，便于统计；二是保障服务的可靠性，确保每条数据都能正确处理，即便出现问题，也不会丢失数据；三是解耦，生成通知记录之后，还要再做发送处理，分离之后，某个环节出错，不会影响整个流程，提升稳定性。而且，如果某个环节出现瓶颈，可以针对性做扩展处理，也能便于异步队列的接入，支撑海量数据的处理。

*   **代码关键内容**：
    *   **数据库表结构** (`t_account_warn_setting`)：
        | 属性 | 名称 | 数据类型 | 是否为空 | 注释 |
        | :--- | :--- | :--- | :--- | :--- |
        | id | 主键标识 | bigint(20) | NO | 主键标识 |
        | accountId | 账户ID | bigint(20) | YES | 账户ID |
    *   **gRPC 接口定义**：
        ```protobuf
        service StockUserService {
          // 用户登陆
          rpc userLogin (LoginRequest) returns (LoginResponse) {}

          // 账户预警设置
          rpc accountWarnSetting(AccountWarnSettingRequest) returns (AccountWarnSettingResponse) {}
        }
        ```
    *   **服务端代码片段**：
        ```java
        // 检查用户接收通知设置是否支持
        checkReceiverInfo(request, tradeAccount);

        // 预警记录类型检查
        checkWarnType(request.getWarnType());

        // 根据账户ID和股票产品ID，查找获取账户预警设置
        AccountWarnSetting accountWarnSetting = accountWarnSettingDao.getByAccountAndStock(request.getAccountId(), request.getStockId());
        Date curDate = new Date();
        if(null == accountWarnSetting) {
            // 新增
            accountWarnSetting = new AccountWarnSetting();
            accountWarnSetting.setAccountId(request.getAccountId());
            accountWarnSetting.setStockId(request.getStockId());
            accountWarnSetting.setCreateTime(curDate);
            accountWarnSetting.setUpdateTime(curDate);
        }
        ```
    *   **缓存加载方法**：
        ```java
        private void loadAccountWarnSettingCache(TradeAccount tradeAccount, AccountWarnSetting accountWarnSetting) {
            // 设置预警通知所需信息
            AccountWarnSettingBo accountWarnSettingBo = new AccountWarnSettingBo();
            // ... (省略具体设置代码)
        }
        ```
    *   **定时任务方法**：
        ```java
        @PostConstruct
        @Override
        @Scheduled(cron = "0 0 3 ? * *") // 每天凌晨3点执行
        public void scheduledAccountWarnSettingCache() {
            log.info("刷新 accountWarnSetting 缓存...");
            List<AccountWarnSetting> warnSettingList = accountWarnSettingDao.getAll();
            if(null != warnSettingList && !warnSettingList.isEmpty()) {
                warnSettingList.stream().forEach(setting -> {
                    // ... (省略具体处理代码)
                });
            }
        }
        ```
    *   **行情服务代码片段**：
        ```java
        public Map<Long, Long> stockOpenCache = new ConcurrentHashMap<>();

        private void updateOpenPrice(TradeStockQuoteLast quotelist) {
            Long openPrice = stockOpenCache.get(quotelist.getStockId());
            if(openPrice == null) {
                // 待写入开盘价
                Cache curOpenPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
                // ... (省略具体缓存写入代码)
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：功能设计与目标设定 (00:00:00-00:00:15)**
    *   **描述**：讲师首先在文档中展示了本章的标题和目标。他明确指出，本章将实现“用户预警通知”的设置与生成功能，具体包括模板设置、账户设置、记录生成和涨跌幅计算。这为后续的代码实现提供了清晰的指导方向。

*   **场景二：接口定义与数据库设计 (00:00:30-00:00:45)**
    *   **描述**：讲师切换到代码编辑器，展示了如何定义 gRPC 接口。他修改了 `StockUserService.proto` 文件，添加了 `accountWarnSetting` 方法，用于接收用户设置的预警参数。同时，他展示了数据库表 `t_account_warn_setting` 的结构，说明了账户ID和主键ID等关键字段。

*   **场景三：服务端逻辑实现 (00:01:00-00:01:15)**
    *   **描述**：讲师演示了服务端的实现代码。他展示了如何根据用户请求，检查接收通知的方式（APP、邮件、短信），然后查询或创建预警设置对象。代码中包含了对数据库的查询和对象的初始化逻辑。

*   **场景四：缓存机制与性能优化 (00:01:15-00:01:30)**
    *   **描述**：讲师重点讲解了缓存的重要性。他展示了 `loadAccountWarnSettingCache` 方法，该方法将查询到的预警设置加载到内存缓存中，避免了后续频繁的数据库查询，从而提升了系统的响应速度和性能。

*   **场景五：定时任务与数据刷新 (00:01:30-00:01:45)**
    *   **描述**：讲师演示了如何使用 Spring 的 `@Scheduled` 注解来创建一个定时任务。该任务会在每天凌晨3点执行，
