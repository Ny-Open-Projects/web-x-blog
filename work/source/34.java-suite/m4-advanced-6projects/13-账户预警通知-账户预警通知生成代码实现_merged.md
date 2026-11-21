# 13-账户预警通知-账户预警通知生成代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们接着去实现

征程账户预警通知记录的业务层代码

回到过程当中

之前咱们对整体流程做了一个梳理

那接着我们从代码层面做具体的实现

首先咱们通过股票产品缓存

去遍历所有的有效股票产品

Foreach Stock ID

在这里咱们要获取最新的股票行情信息

Bot Last

传递股票ID

这个方法呢

就是从缓存里面获取最新的行情报价信息

好

接着咱们对获取的行情数据做个围攻判断

如果存在实时的行情

咱们才接下来做下面的业务逻辑

将这些步骤copy过来

那第二步咱们就要根据股票产品ID

获取所有的key值

通过Ladies Template的接口

key方法

咱们要传递它的缓存key

Setting Stock Key

这里要拼接股票ID

然后通过信号进行模糊匹配

这样就能够拿到该股票产品下面的

所有账户缓存的预警设置信息

那接着咱们做个围攻判断

这里要刊登keys

并且keys不围攻

然后我们就要刊登keys

然后我们就要刊登keys

接下来咱们去组装缓存的key

Global Consistence Account

Warn Setting Stock Key

再加上stock ID

然后获取缓存对象

Pitch Manager

Get Key

拿到账户预警模板设置的缓存对象

那接下来咱们就去实现第三个步骤

遍地对应股票产品下面的所有账户设置的预警信息

咱们将步骤copy进去

这里通过keys进行遍地

接下来咱们就去实现第四步的处理

第四步就通过缓存去拿到账户的预警通知设置信息

通过catch的value包装对象

咱们来获取缓存的具体信息

replace all

这里要将缓存的前缀给去除

还要加上两个帽号

因为它是通过两个帽号进行缓存的前缀

进行分割的

接着的话

我们对值对象做一个判断

确保缓存里面的值对象不为空

接着从缓存里面获取账户预警设置对象

这个是一个BO做强转

拿到账户预警设置对象之后

咱们接着就来处理第五步

检查预警通知记录

判断他是否第一次生成

或者是上一次预警通知呢

已经超过十分钟

这里通过一个子方法check account one setting

传递BO对象

那咱们来看一下这个方法的具体时间

在这里他会判断上一次的记录时间

如果是为空的

说明他是第一次处理预警信息

那么就返回为去

接着的话

他会判断当前的时间和上一次预警记录时间的时间差

那么如果是大于十分钟

他的结果呢

也是返回为去

除此之外

结果返回为force

好

那咱们回到刚才的逻辑

符合条件之后

接着就要去生成预警的通知记录信息

通过c1 notify message

传递最新的航行报价

咱们看一下这个方法的具体时间

这里他会判断是否存在多种的通知类型

如果是存在多种通知类型

这里呢

会做一个便利处理

然后呢

调用

读notify message方法

读notify message呢

在这里面

他会去根据预警类型做相应的判断处理

这里是包含两种预警类型

一种呢

是止损

第二种呢

是指引

他们都会去调用record notify message方法

这个方法是做什么事情呢

他会去根据模板

然后生成预警通知信息

比如说是指引的模板

他在这里呢

他会根据传递的预警通知类型

查找对应的模板设置信息

拿到模板设置信息之后

会将模板里面的变量做替换

组装为实际的通知内容

接着会判断接收的类型

如果是短信呢

在这里会将手机号设置进去

如果是邮件会设置email

在内信呢

就设置交易账户ID

下面呢

是组装其他的信息

然后调用数据层接口

进行保存操作

最后他会去更新记录的生成时间

因为咱们缓存了会基于这个最后更新时间做相应的判断处理

好

那咱们回到刚才的业务逻辑

Generator

Want Notify Message

咱们继续处理下面的步骤

生成完预警通知信息之后

咱们还要记录他的通知生成次数

Set Notify Times

将原来的通知信息处理成为通知信息

Send Notify Times

将原来的通知信息处理成为通知信息

他的通知次数累加一

然后我们要去更新缓存的记录

Get Account ID

最后就要判断预警通知记录的通知次数

如果是超过三次

当天呢

就不再生成预警通知

要将账户的缓存记录做清楚处理

在这里咱们做一个判断

If Account Onsetting Bureau Get Notify Times

如果是大于等于三次

将缓存信息执行清除

传递交易账户ID

好

这样咱们就完成了核心业务逻辑的处理

这里咱们再做一个日志完善

便于日志的追踪处理

这个是没有找到账户的预警设置信息

提示股票产品ID

这里也打印个日志

提示没有获取最新的行情报价信息

打印出

股票ID

Stock ID

好

那在这里

咱们就完成了调度服务

去生成账户的预警通知记录

将业务层的核心代码做了具体实现

预警通知记录的生成实现要符合咱们设定的规则

每天只发送三次

十分钟之内的重复预警信息

就不再进行通知

不要产生大量的预警通知信息给用户造成干扰

好

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“账户预警通知”功能的实现讲解。核心内容是演示如何在 `AccountWarnSettingServiceImpl` 服务类中，通过遍历所有有效股票产品，获取其对应的账户预警设置，并根据股票最新报价生成预警通知消息。整个过程涉及 Redis 缓存、Spring Cache、模板引擎（如 `AccountWarnTemplate`）以及多渠道（短信、邮件、APP）通知的逻辑。视频重点展示了代码的逐行实现、关键的缓存操作、以及如何根据预警类型（如 SMS、EMAIL、APP）动态设置通知接收方。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**: 视频开头，展示 `AccountWarnSettingServiceImpl` 类的 `generateWarnNotifyMessage` 方法的入口。
*   **00:00:03 - 00:00:08**: 开始实现方法体，首先遍历所有有效股票产品，通过 `stocksCache.getKeys()` 获取股票ID列表。
*   **00:00:08 - 00:00:14**: 对每个股票ID，调用 `getTradeStockQuoteLast(stockId)` 获取最新报价。如果返回 `null`，则跳过该股票。
*   **00:00:14 - 00:00:21**: 使用 Redis 的 `keys` 命令，根据股票ID和预设的键前缀 `ACCOUNT_WARN_SETTING_STOCK_KEY`，获取该股票下所有账户的预警设置键。
*   **00:00:21 - 00:00:28**: 通过 `cacheManager` 获取缓存对象，遍历上一步获取的键集合，对每个账户的预警设置进行处理。
*   **00:00:28 - 00:00:35**: 从缓存中获取账户预警设置对象 `AccountWarnSettingBo`，并调用 `checkAccountWarnSetting` 方法检查该账户是否在10分钟内已生成过预警。
*   **00:00:35 - 00:00:42**: 如果未在10分钟内生成过预警，则继续处理。调用 `AccountWarnTemplate` 模板，根据 `AccountWarnSettingBo` 中的参数（如股票代码、价格、涨跌幅）生成通知内容。
*   **00:00:42 - 00:00:49**: 根据预警类型（SMS、EMAIL、APP）设置通知接收方。例如，如果是 SMS 类型，则设置 `notifyMessage.setReceiver(accountWarnSettingBo.getPhone())`。
*   **00:00:49 - 00:00:56**: 将生成的通知对象 `notifyMessage` 保存到数据库，并更新该账户的预警通知次数。同时，将通知对象存入缓存，以便后续处理。
*   **00:00:56 - 00:01:03**: 代码逻辑结束，展示最终的 `doNotifyMessage` 方法的调用，该方法负责根据预警类型执行具体的发送逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “第2章 用户预警通知的设置与生成”。
    *   **子章节**: “3.1 实现预警通知模板设置接口”、“3.2 实现账户预警通知设置接口”、“3.3 调度服务实现生成账户预警通知记录”。
    *   **核心逻辑描述**: “每种预警方式，可能会做不同的逻辑处理，再做了一层封装，这里的止盈和止损用的是同一个模板，生成逻辑是一样的：”。
    *   **方法签名**: `private void doNotifyMessage(AccountWarnSettingBo accountWarnSettingBo, String type, TradeStockQuoteLast quoteLast);`

*   **代码关键内容**:

    *   **方法签名**:
        ```java
        @Transactional(rollbackFor = Exception.class)
        public void generateWarnNotifyMessage() {
        ```

    *   **遍历股票产品**:
        ```java
        stocksCache.getKeys().forEach(stockId -> {
            TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(stockId);
            if (null == quoteLast) {
                return;
            }
        ```

    *   **获取 Redis 键**:
        ```java
        Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.ACCOUNT_WARN_SETTING_STOCK_KEY + stockId);
        ```

    *   **缓存处理**:
        ```java
        Cache cache = cacheManager.getCache(prefixKey);
        keys.forEach(key -> {
            Cache.ValueWrapper valueWrapper = cache.get(key);
            if (null != valueWrapper && valueWrapper.get() != null) {
                Account accountWarnSettingBo = (AccountWarnSettingBo) valueWrapper.get();
                // ... 处理账户预警设置 ...
            }
        });
        ```

    *   **检查预警频率**:
        ```java
        private boolean checkAccountWarnSetting(AccountWarnSettingBo accountWarnSettingBo) {
            if (accountWarnSettingBo.getLastWarnRecordTime() == null) {
                return true; // 第一次预警
            }
            long diffTime = System.currentTimeMillis() - accountWarnSettingBo.getLastWarnRecordTime();
            if (diffTime > 60000) { // 60秒
                return true;
            } else {
                log.warn("check account warn setting, time in period, not generate data.");
                return false;
            }
        }
        ```

    *   **生成通知内容**:
        ```java
        AccountWarnNotifyMessage notifyMessage = new AccountWarnNotifyMessage();
        notifyMessage.setNotifyContent(content);
        notifyMessage.setAccountId(accountWarnSettingBo.getAccountId());
        notifyMessage.setUserId(accountWarnSettingBo.getUserId());
        if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_SMS.equals(type)) {
            notifyMessage.setReceiver(accountWarnSettingBo.getPhone());
        } else if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_EMAIL.equals(type)) {
            notifyMessage.setReceiver(accountWarnSettingBo.getEmail());
        } else if (GlobalConstants.ACCOUNT_WARN_NOTIFY_TYPE_APP.equals(type)) {
            notifyMessage.setReceiver(accountWarnSettingBo.getApp());
        }
        ```

    *   **保存通知记录**:
        ```java
        saveAccountWarnNotifyMessage(accountWarnSettingBo, quoteLast);
        cache.put(accountWarnSettingBo.getNotifyId(), accountWarnSettingBo);
        ```

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与循环结构** (00:00:00 - 00:00:08)
    *   讲师在 IDE 中定位到 `generateWarnNotifyMessage` 方法。
    *   通过 `stocksCache.getKeys()` 获取所有股票ID的集合，并使用 `forEach` 循环遍历。
    *   演示了如何通过 `getTradeStockQuoteLast(stockId)` 获取股票的最新报价，并在 `null` 时直接 `return` 跳过。

*   **场景二：Redis 缓存键获取与处理** (00:00:14 - 00:00:28)
    *   讲师演示了如何使用 `redisTemplate.keys()` 方法，结合 `ACCOUNT_WARN_SETTING_STOCK_KEY` 前缀和当前股票ID，获取该股票下所有账户的预警设置键。
    *   通过 `cacheManager.getCache(prefixKey)` 获取缓存对象，并使用 `forEach` 遍历所有键，对每个账户的预警设置进行处理。

*   **场景三：预警频率检查** (00:00:28 - 00:00:35)
    *   讲师调用 `checkAccountWarnSetting` 方法，检查账户是否在10分钟内已生成过预警。
    *   通过 `System.currentTimeMillis()` 计算时间差，如果超过60秒（10分钟），则允许生成新预警。

*   **场景四：模板引擎与通知内容生成** (00:00:35 - 00:00:42)
    *   讲师从缓存中取出 `AccountWarnSettingBo` 对象。
    *   调用 `AccountWarnTemplate` 模板，使用 `replace` 方法将模板中的占位符（如 `$stockCode`、`$stockPrice`）替换为实际值，生成最终的通知内容。

*   **场景五：多渠道通知接收方设置** (00:00:42 - 00:00:49)
    *   讲师根据 `type` 参数（如 SMS、EMAIL、APP）设置通知接收方。
    *   通过 `setReceiver` 方法，将接收方设置为 `AccountWarnSettingBo` 中对应的属性值（如 `getPhone()`、`getEmail()`、`getApp()`）。

*   **场景六：保存通知记录与缓存** (00:00:49 - 00:00:56
