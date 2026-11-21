# 11-账户预警通知-账户预警通知设置接口功能实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们就去实现账户预警通知设置接口的服务层代码

回到咱们的工程代码当中

这里我们就已经将必要的属性以及封装的方法引用进来

那接着我们去测证讲解核心代码的实现

首先咱们来梳理下整体的实现流程

第一步

咱们要根据账号ID

获取

交易账号对象

接着第二步

要去校验通知类型是否合法

第三步

检查用户接收通知设置方式是否能够支持

比如用户设置的是手机的通知方式

那么他就必须要设定手机号

然后

对预警记录类型做检查

这个不能用户随便填

要判断是否系统支持的预警类型

第五个步骤

根据账户ID和股票产品ID

然后查找获取账户的预警设置信息

如果是存在

那么就做更新处理

如果不存在

则新增记录

最后

为了提升预警通知的处理效率

咱们也将预警通知信息

加载至缓存当中

这些就是保存用户设置预警信息的整体处理流程

那接着咱们就来做代码上的实现

首先定义Shared Account

通过Shared Account

DLO数据层接口

调用Get by ID的方法

这里呢

要传递交易账户ID

接下来做一个围攻判断

如果没有找到账号

咱们要抛出一个业务异常

给出错误提示码

这个呢

就是没有找到有效的账号

接下来就要去校验通知类型

是否合法

通过封装的方法

Check Notify Type

咱们传入Notify Type参数

那我们去看一下方法的具体实现

首先他会判断Notify Type

如果是围攻呢

就直接抛出异常

接着的话呢

要对多种通知类型做判断处理

这个参数是可以支持多种预警通知类型的设置

比如说既可以采用APP的方式通知

也可以采用SMS转信的方式进行通知

那么中间呢

以逗号进行分割

那代码就要做相应的处理

分割取到所有通知类型之后

然后去做校验判断

判断是否属于系统支持的类型

咱们可以看到系统里面呢

有三种类型

一种是APP

然后呢

Email

最后呢

就是SMS转信的方式

咱们再回到上层的方法

如果是单一的通知类型

在这里就直接做校验判断

再回到刚才的处理逻辑

接着咱们要去检查用户设置的接收通知方式

Check

Receive

Bin for

传递Request参数对象

然后再传递交易账户

咱们点进去

看这个方法具体实现

这里会根据所设置的通知类型

然后做相应的校验

比如说是短信通知

那么咱们就要去检查

它是否设置了手机号

如果是邮件通知呢

就要去设置是否设定了邮箱

那APP站类性呢

这个就不需要校验

直接通过APP去发送通知就可以

再回到业务处理逻辑

第四步

我们要去对预警记录类型做检查

判断

是否有通知类型

或者是透过系统支持的预警类型

通过Check One Type方法

Request Get One Type

咱们点进去方法

预警通知类型

在咱们系统当中

只支持止盈和止损的类型

这里就根据传递的One Type

做相应的判断处理

好

再回到刚才的处理逻辑

接下来第五步

要根据账户ID和股票产品ID

然后再回到刚才的处理逻辑

然后去查找获取账户的预警设置信息

这样避免产生重复的记录

Account

On

Setting

通过数据层接口

Get By Account and Stock

传递账户ID

再传递股票ID

接下来就要做相应的判断处理

如果是存在

就做更新操作

那如果不存在呢

则新增对应的记录

这里咱们从讲义当中

将代码拖币进来

回到过程当中

三列进去

可以看到在这里会创建当前系统的时间

这里是用于记录数据的操作时间

下面呢

要设置账户预警设置的信息

如果是要做更新处理

在这里只更新相应的字段

Update Time

Notify Type

Warn Type

Stop Late

像交易账户ID

Stock ID

Credit Time

这些信息呢

就不需要重复进行更新

数据保存更新

完成之后

最后咱们要加载预警通知信息到缓存当中

这里呢

调用load account

用setting cage方法

传递交易账户ID

传递预警设置信息

那咱们看一下这个方法具体实现

因为预警通知信息

咱们要去做生成加工的时候

如果去频繁查询数据库

是很耗费性能

所以在这里呢

会将它加载至缓存里面

这里会将账户的预警设置信息

组装为BO对象

那BO对象里面呢

会拢于相应的用户信息

股票产品信息

这样呢

是便于后续业务的加工处理

然后将它放入缓存当中

缓存的key子呢

是Arcana 1 setting stock key

后面呢

再去拼接账户预警设置信息的股票产品ID

那每个交易账户呢

它的预警设置信息都是唯一的

缓存放入的时候呢

会加上交易账户的ID

和账户预警设置信息的ID

做关联

那这一块呢

就是保存用户设置预警信息的

整体代码的实现

那咱们回到讲义当中

用户设定完预警通知之后

但是一天当中

行情是在反复进行变化的

价格呢

会不断的涨跌变化

可能会多次符合预警条件

用户如果是频繁接收

这样呢

会不太友好

所以我们在这里

设定是12天

10分钟之内不重复接收

相同的预警信息

如果一天之内有多次条件的触发

我们最多呢

只发送三次

这样用户的体验就会相对好一些

那该如何去实现呢

这里我们是通过一个BIO对象做了封装处理

在Accounted One Setting BIO里面呢

我们增加了一个时间的记录

也就是上次预警记录的时间

同时再加上预警通知的次数

通过这两个属性记录呢

就能够实现这里面的要求

做到不重复去发送预警

一天之内

如果是多次触发

最多呢

就发送三次

但是到第二天的时候呢

用户又能够接收预警信息

所以咱们在这里需要再添加一个定时的调度任务

服务如果重启

或者是每天凌晨三点

开盘之前

休市之后

不要放在交易时间之内

将服务的时间和时间都放在交易时间之内

我们把我们数据库的数据重新放入缓存当中

然后做缓存的刷新处理

比如说用户达到一天预警的三次上线之后

缓存呢

就会做清除

第二天呢

就需要重新加载预警的设置信息

这样就相当于将用户预警设置的缓存记录做了一个重置

那咱们就将相应的代码做一个实现

将代码copy

放置trade user service implement的下面

咱们将接口抽取下右键refact

formal bus app

将该方法抽取出来refact

接下来咱们再加上一个日子插件log4j2

再回到刚才的方法

好

那咱们来看一下它的实现逻辑

首先呢

他会去查找所有的账户预警设置信息

拿到数据信息之后

会做一个便利处理

接着他去查找对应的交易账户信息

然后调用load account one setting cache方法

将数据加载至缓存里面

咱们可以进去看一下

这个方法咱们刚才做了讲解

注意在缓存更新的时候呢

我们可以看到他会将缓存内容做覆盖更新

因为account one setting bior是一个新建的对象

所以这里面的上次预警记录时间以及预警通知次数都默认为零

好

那这样呢就实现了这个方法了

实现了账户预警缓存信息的重置处理

就能够保障用户每天都可以接收到预警的通知消息

这一讲

那咱们就实现了账户预警通知设置接口的具体功能

这讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“用户预警通知”功能的实现讲解。讲师通过 IntelliJ IDEA 开发环境，逐步演示了 `TradeUserServiceImpl` 类中 `saveAccountWarnSetting` 方法的完整逻辑。该方法负责处理用户提交的预警设置请求，包括：校验用户接收通知的合法性（如短信或邮件）、校验预警类型（止盈或止损）、根据账户ID和产品ID查询或创建预警记录、并将最终的预警信息持久化到数据库。此外，视频还展示了如何将预警设置信息加载到缓存中，以及如何通过定时任务（`@Scheduled`）定期刷新缓存，以保证系统在高并发下的性能和实时性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：开场，展示项目结构和 `TradeUserServiceImpl` 类中的 `saveAccountWarnSetting` 方法。
*   **00:00:15 - 00:00:30**：讲解方法的注释和基本结构，列出六个主要步骤。
*   **00:00:30 - 00:00:45**：演示第一步，根据账户ID获取 `TradeAccount` 对象。
*   **00:00:45 - 00:01:00**：演示第二步，检查通知类型是否合法。
*   **00:01:00 - 00:01:15**：演示第三步，检查用户接收通知的方式是否支持。
*   **00:01:15 - 00:01:30**：演示第四步，校验预警记录类型。
*   **00:01:30 - 00:01:45**：演示第五步，根据账户ID和产品ID查找或创建预警记录。
*   **00:01:45 - 00:02:00**：演示第六步，将预警信息保存到数据库。
*   **00:02:00 - 00:02:15**：讲解如何将预警信息加载到缓存中。
*   **00:02:15 - 00:02:30**：演示如何通过 `@Scheduled` 注解实现定时任务，定期刷新缓存。
*   **00:02:30 - 00:02:45**：总结，强调缓存和定时任务在高并发场景下的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：第2章 用户预警通知的设置与生成。
    *   **子章节**：3.1 实现预警通知模板设置接口；3.2 实现账户预警通知设置接口；3.3 调度服务实现生成账户预警通知记录；3.4 行情服务实现开盘价与涨跌幅的计算；3.5 功能验证。
    *   **关键说明**：在“3.3 调度服务实现生成账户预警通知记录”部分，PPT中提到“预警通知需要较高的实时性，但也能容许一定延迟...采用调度任务来处理...结合缓存，就能有较好的性能与实时性。”

*   **代码关键内容**：

    *   **`saveAccountWarnSetting` 方法核心逻辑**：
        ```java
        @Override
        public void saveAccountWarnSetting(AccountWarnSettingRequest request) throws ComponentException {
            // 1. 根据账号ID获取交易账号对象
            TradeAccount tradeAccount = ...;

            // 2. 要去校验通知类型是否合法
            checkNotifyType(request.getNotifyType());

            // 3. 检查用户接收通知设置方式是否能够支持
            checkReceiverInfo(request, tradeAccount);

            // 4. 预警记录类型检查
            checkWarnType(request.getWarnType());

            // 5. 根据账号ID和股票产品ID，查找获取账户的预警设置信息
            AccountWarnSetting accountWarnSetting = ...;

            // 6. 加载预警通知信息至缓存
            loadAccountWarnSettingCache(tradeAccount, accountWarnSetting);
        }
        ```

    *   **`checkWarnType` 方法**：
        ```java
        private void checkWarnType(Integer warnType) throws ComponentException {
            boolean isMatch = false;
            if (GlobalConstants.ACCOUNT_WARN_TYPE_STOP_PROFIT == warnType) {
                isMatch = true;
            } else if (GlobalConstants.ACCOUNT_WARN_TYPE_STOP_LOSS == warnType) {
                isMatch = true;
            }
            if (!isMatch) {
                throw new ComponentException(ApplicationErrorCodeEnum.WARN_TYPE_ERROR);
            }
        }
        ```

    *   **`loadAccountWarnSettingCache` 方法**：
        ```java
        private void loadAccountWarnSettingCache(TradeAccount tradeAccount, AccountWarnSetting accountWarnSetting) {
            AccountWarnSettingBo accountWarnSettingBo = new AccountWarnSettingBo();
            BeanUtils.copyProperties(accountWarnSetting, accountWarnSettingBo);
            // 设置用户信息、股票信息等
            accountWarnSettingBo.setStockCode(stock.getCode());
            accountWarnSettingBo.setStockName(stock.getName());
            accountWarnSettingBo.setUserId(tradeUser.getId());
            accountWarnSettingBo.setUserName(tradeUser.getName());
            accountWarnSettingBo.setEmail(tradeUser.getEmail());
            accountWarnSettingBo.setPhone(tradeUser.getPhone());

            // 加载到缓存
            Cache cache = cacheManager.getCache(name: GlobalConstants.ACCOUNT_WARN_SETTING_STOCK);
            cache.put(accountWarnSettingBo);
        }
        ```

    *   **`@Scheduled` 定时任务**：
        ```java
        @PostConstruct
        @Override
        @Scheduled(cron = "0 0 3 ? * *")
        public void scheduledAccountWarnSettingCache() {
            log.info("refresh account warn setting cache...");
            List<AccountWarnSetting> warnSettingList = accountWarnSettingDao.getAll();
            if (null != warnSettingList && !warnSettingList.isEmpty()) {
                // 加载到缓存
            }
        }
        ```

    *   **常量定义**：
        ```java
        public static final String ACCOUNT_WARN_NOTIFY_TYPE_APP = "APP";
        public static final String ACCOUNT_WARN_NOTIFY_TYPE_EMAIL = "EMAIL";
        public static final String ACCOUNT_WARN_NOTIFY_TYPE_SMS = "SMS";
        ```

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与步骤规划 (00:00:00-00:00:30)**
    *   讲师首先在 IDE 中定位到 `TradeUserServiceImpl` 类的 `saveAccountWarnSetting` 方法。
    *   他通过注释清晰地列出了该方法的六个主要步骤，为后续的代码演示提供了清晰的框架。

*   **场景二：校验预警类型 (00:00:45-00:01:15)**
    *   讲师展示了 `checkWarnType` 方法的实现。
    *   他通过代码演示了如何使用 `GlobalConstants` 中定义的常量（如 `ACCOUNT_WARN_TYPE_STOP_LOSS`）来校验用户输入的预警类型。
    *   如果类型不合法，会抛出 `ComponentException` 异常。

*   **场景三：加载缓存 (00:01:45-00:02:00)**
    *   讲师演示了如何将数据库中的预警设置信息转换为 `AccountWarnSettingBo` 对象。
    *   他使用了 `BeanUtils.copyProperties` 方法进行属性拷贝，并填充了用户和股票相关的详细信息。
    *   最后，他通过 `cacheManager.getCache` 获取缓存实例，并调用 `put` 方法将对象存入缓存。

*   **场景四：定时任务 (00:02:15-00:02:30)**
    *   讲师在 `TradeUserServiceImpl` 类中添加了一个 `@Scheduled` 注解的方法。
    *   他设置了 `cron = "0 0 3 ? * *"`，表示每天凌晨3点执行一次。
    *   该方法会从数据库中查询所有预警设置，并调用 `loadAccountWarnSettingCache` 方法将它们加载到缓存中，以保证系统在高并发下的性能。

*   **场景五：PPT 与代码结合讲解 (00:02:30-00:02:45)**
    *   讲师切换到 PPT，强调了“调度任务”和“缓存”在系统设计中的重要性。
    *   他解释了为什么不能采用“监听行情报价去触发预警”的方式，因为这会导致巨大的压力。
    *   他总结道，通过“调度任务 + 缓存”的组合，可以在保证实时性的同时，有效分担系统压力，提升整体性能。
