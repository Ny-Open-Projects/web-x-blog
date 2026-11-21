# 12-账户预警通知-账户预警通知生成流程梳理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们开始学习和讲解调度服务

去实现生成账户的预警通知记录

那么预警通知呢

它是需要较高的实时性

但也能容许一定的延迟

因为它不像交易服务

下了单呢必须要尽快去处理

预警通知从条件的触发

再到信息的下发是会有一定的延迟

当然这个时间差呢是越小越好

那么如何去保障实时性

同时呢又要去兼顾性能

我们不能去采用监听每口行情的报价

来触发账户的预警通知

因为一个交易平台有几十万

上百万上千万的用户

而且股票交易市场有几千只股票

每秒行情呢它又可以接收数口报价

即便咱们是采用集群方式去做处理

压力呢也是非常巨大的

这些数据是成倍增长

非常消耗服务器的资源开销

那咱们采用什么方式去做处理呢

这里就采用调度任务来做处理

我们每分钟或者是数秒检测一次

比如说三十秒十秒

这样相比监听每口行情报价来触发

能够呢去极大的减少信息处理量

同时咱们再批量处理

然后结合缓存

这样就能够有较好的性能

以及数据通知的实时性

那咱们先来看一下账户预警通知记录表的属性结构

这里会有用户信息

用户ID账户ID

然后呢接收者的地址信息

如果是手机呢

在这里就是手机号

如果是email的通知方式

在这里呢就是邮箱

那这个是notify type通知的具体方式

下面呢是one type预警类型

预警类型呢包括止损和止盈

然后呢是content通知内容

下面呢是发生状态

然后是从事次数

接着呢是备注信息

如果是失败

在这里会记录异常的提示信息

最后就是更新时间

下面就是实体的对象结构

这个呢和表结构的属性定义都是一致的

然后咱们先去创建对应的调度任务

generate one notify message job

咱们将这段代码copy一下

回到工程当中

好

找到咱们的task交易调度服务

在交易调度服务下面

咱们在job的包下面创建一个纸包

纸包名称呢就叫warning

专门去处理预警通知相关的调度任务

接着咱们去创建预警通知的job

名称叫generate one notify message job

咱们将job的代码后备进去

检查对应的文件

为了解释一下这个技能的错误

导入日之查鉴

咱们添加注释描述下

这个是生成站户预警通知记录信息

每分钟执行一次

它的clone表达式呢就是0

这个是代表分钟

然后后面采用信号

接下来咱们去创建它的服务层接口

这个是账户预警通知信息号码

接下来咱们去创建它的服务层接口

预警通知的服务层接口

将名称 copy

在 service 下面

先创建对应的接口

类型为 interface

将名称 copy 进去

接下来咱们再去创建它的实现类

new-java-class

这个名称呢我们叫 account

one-setting-service-implement

它去实现

i account

one-setting-service 这个接口

接下来咱们就要去实现服务层逻辑的处理

咱们首先将必要的属性和辅助方法引用进来

回到工程当中

单列进去

对代码做一个检查和修正

这里我们需要加上 log4j 的插件

添加 service

添加 log4j2 的插件

接下来咱们再检查一下

这个是预警通知的发生功能

咱们

在下面的章节在做讲解

这里可以先暂时去除

data 日期包找不进来

在叫 youtube 下面

好那接下来咱们就去实现预警通知生成的业务层代码

update void

generate

or

notify message

这里面不需要传递参数

添加注释

这个是生成

预警通知记录的接口实现

因为预警通知记录的生成处理数据量会比较多

所以咱们要在这里加入失误控制

采用批量方式去处理提交数据信息

lowback4

exception.cast

首先咱们对整体实现流程做一个梳理

第一步要遍地

所有的有效股票产品

如果不是有效的产品就不能进行交易

也就不会产生预警通知记录信息

接着第二步要根据股票产品ID去获取所有的汽值

然后第三步

遍地

对应股票产品下面的所有账户设置的预警信息

第四个步骤

根据股票产品ID获取账户的预警通知设置信息

第五个步骤

咱们要做相应的交易判断

要去检查预警通知记录

是否第一次生成或者是放一次预警通知超过10分钟

也就是说在生成预警通知记录的时候呢

咱们会去做相应的判断

如果是第一次服务条件

那这个是需要生成预警通知记录

接着在10分钟之内

仍然触发了预警通知的条件

那么就不会再去生成预警通知记录

直到他超过10分钟之后

并且每个账户的预警通知记录

每天呢他最多通知发送三次

所以在生成预警通知记录的时候

咱们还会根据次数做判断

如果是他超过了三次

那么是不会再去生成预警通知记录

好咱们回到代码当中

第六步

咱们就去生成预警通知记录

记录信息

最后一步

要判断预警通知记录的通知次数

如果超过三次

当天不再处理生成预警通知

将账户的返存记录移除

好这个呢

就是生成预警通知记录接口的

整体处理实现流程

下一讲咱们再做代码的具体实现

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“账户预警通知”功能的实现教程。核心内容是设计并实现一个定时调度任务，用于批量生成账户预警通知记录。该任务需要处理高并发、低延迟的预警需求，因此采用了“调度任务 + 缓存 + 批量处理”的架构。视频详细展示了从数据库表结构设计、定时任务类编写、服务层逻辑实现到最终的数据库持久化操作的全过程，重点讲解了如何通过 Spring Boot 的 `@Scheduled` 和 `@Transactional` 注解来管理任务和事务，以及如何通过缓存机制来优化性能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：开场，展示课程大纲，定位到“3.3 调度服务实现生成账户预警通知记录”章节。
*   **00:00:15 - 00:00:30**：讲解预警通知的业务需求，强调需要高实时性、高并发处理能力，并引出采用“调度任务 + 缓存 + 批量处理”的解决方案。
*   **00:00:30 - 00:00:45**：展示并讲解数据库表 `t_account_warn_notify_message` 的结构，包括 `warnType`（预警类型）、`notifyContent`（通知内容）、`sendStatus`（发送状态）、`retryTimes`（重试次数）等关键字段。
*   **00:00:45 - 00:01:00**：讲解如何创建定时调度任务类 `GenerateWarnNotifyMessageJob`，并展示其 `@JobHandler` 和 `@Service` 注解。
*   **00:01:00 - 00:01:15**：在 `TradeUserServiceImpl` 中配置定时任务，使用 `@Scheduled` 注解设置 cron 表达式 `0 0 3 * * ?`，表示每天凌晨3点执行。
*   **00:01:15 - 00:01:30**：讲解服务层 `IAccountWarnSettingService` 的接口定义和实现类 `AccountWarnSettingServiceImpl` 的结构。
*   **00:01:30 - 00:01:45**：在 `AccountWarnSettingServiceImpl` 中实现核心方法 `generateWarnNotifyMessage()`，并添加 `@Transactional` 注解以保证数据一致性。
*   **00:01:45 - 00:02:00**：在 `generateWarnNotifyMessage()` 方法中，展示伪代码逻辑：遍历所有有效股票产品，根据产品ID获取所有账户的预警设置，检查并生成预警通知记录。
*   **00:02:00 - 00:02:15**：讲解如何在 `saveAccountWarnNotifyMessage` 方法中根据 `warnType` 字段的值（如“短信”、“邮件”、“站内信”）来设置不同的接收者，并调用 `doNotifyMessage` 方法进行通知。
*   **00:02:15 - 00:02:30**：展示如何将生成的预警通知记录保存到数据库表 `t_account_warn_notify_message` 中，并更新预警设置的最后生成时间。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3.3 调度服务实现生成账户预警通知记录`
    *   **核心思想**：采用“调度任务 + 缓存 + 批量处理”来保证性能与实时性。
    *   **表结构**：`t_account_warn_notify_message` 表，包含字段：`warnType`, `notifyContent`, `sendStatus`, `retryTimes`, `memo` 等。

*   **代码关键内容**：

    *   **定时任务类 `GenerateWarnNotifyMessageJob`**：
        ```java
        @JobHandler(value="generateWarnNotifyMessageJob")
        @Service
        @Log4j2
        class GenerateWarnNotifyMessageJob extends IJobHandler {
            @Autowired
            private IAccountWarnSettingService accountWarnSettingService;
            
            @Override
            public ReturnT<String> execute(String param) throws Exception {
                log.info("Process in GenerateWarnNotifyMessageJob.execute method, param: " + param);
                try {
                    // 生成预警通知记录
                    accountWarnSettingService.generateWarnNotifyMessage();
                    return ReturnT.SUCCESS;
                } catch (Exception e) {
                    log.error("GenerateWarnNotifyMessageJob execute error", e);
                    return ReturnT.FAIL;
                }
            }
        }
        ```

    *   **服务层接口 `IAccountWarnSettingService`**：
        ```java
        public interface IAccountWarnSettingService {
            void generateWarnNotifyMessage();
        }
        ```

    *   **服务层实现类 `AccountWarnSettingServiceImpl`**：
        ```java
        @Service
        @Log4j2
        public class AccountWarnSettingServiceImpl implements IAccountWarnSettingService {
            @Autowired
            private CacheManager cacheManager;
            @Autowired
            private TaskExecutor taskExecutor;
            @Autowired
            private StocksCache stocksCache;
            
            @Transactional
            public void generateWarnNotifyMessage() {
                // 伪代码逻辑
                // 1. 遍历所有的有效股票产品
                // 2. 根据股票产品ID获取所有的预警设置
                // 3. 根据预警设置，生成预警通知记录
                // 4. 判断通知记录的次数，如果超过3次，当天不再生成预警通知
            }
        }
        ```

    *   **数据库表结构**：
        | 属性 | 名称 | 数据类型 | 是否为 | 注释 |
        | :--- | :--- | :--- | :--- | :--- |
        | warnType | 预警类型 | int(11) | NO | 预警类型 (0: 止损, 1: 止盈) |
        | notifyContent | 通知内容 | varchar(2000) | YES | 通知内容 |
        | sendStatus | 发送状态 | varchar(128) | YES | 发送状态 (成功为200, 失败为错误码) |
        | retryTimes | 重试次数 | int(11) | YES | 重试次数，默认重发3次 |
        | memo | 备注 | varchar(500) | YES | 备注，如果失败，记录失败原因 |

---

### 4) 关键场景与演示描述

*   **场景一：需求分析与架构设计**（00:00:00-00:00:30）
    *   **演示**：讲师在文档中定位到“3.3 调度服务实现生成账户预警通知记录”章节，并解释了预警通知的高并发、低延迟需求。
    *   **关键动作**：讲师在屏幕上高亮显示了“调度任务 + 缓存 + 批量处理”的解决方案。

*   **场景二：数据库表设计**（00:00:30-00:00:45）
    *   **演示**：讲师在文档中展示了 `t_account_warn_notify_message` 表的结构，并逐行讲解了 `warnType`、`notifyContent`、`sendStatus`、`retryTimes` 等字段的含义和数据类型。
    *   **关键动作**：讲师在屏幕上高亮并解释了 `retryTimes` 字段的默认值为3次。

*   **场景三：定时任务创建**（00:00:45-00:01:00）
    *   **演示**：讲师在 IntelliJ IDEA 中创建了一个名为 `GenerateWarnNotifyMessageJob` 的新类，并为其添加了 `@JobHandler` 和 `@Service` 注解。
    *   **关键动作**：讲师在代码编辑器中高亮并解释了 `@JobHandler` 注解的 `value` 属性。

*   **场景四：定时任务配置**（00:01:00-00:01:15）
    *   **演示**：讲师在 `TradeUserServiceImpl` 类中添加了 `@Scheduled` 注解，并设置了 cron 表达式 `0 0 3 * * ?`。
    *   **关键动作**：讲师在屏幕上高亮并解释了 cron 表达式的含义（每天凌晨3点执行）。

*   **场景五：服务层实现**（00:01:15-00:02:30）
    *   **演示**：讲师在 `AccountWarnSettingServiceImpl` 类中实现了 `generateWarnNotifyMessage()` 方法，并添加了 `@Transactional` 注解。
    *   **关键动作**：讲师在屏幕上高亮并解释了 `@Transactional` 注解的作用。
    *   **演示**：讲师在 `saveAccountWarnNotifyMessage` 方法中展示了如何根据 `warnType` 字段的值来
