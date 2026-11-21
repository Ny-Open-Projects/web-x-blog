# 18-Quartz动态定时任务（更新定时任务_测试） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才咱们这个更新定时任务

我们代码都已经写完了

那接下来我们来测试一下

看看能不能生效

好 直接把我们这个服务重新启动一下

咱们现在更新的话

就可以来更新一下什么呢

更新一下咱们这个

刚才我们创建的这个1003

这个任务

好 那么这个服务已经跑起来了

可以来看一下

我们现在这个1003

它的这个触发是什么时候触发的呢

从这儿看不出来

需要看另外一张表

就是这个什么

con triggers

它在这个表里面记录着了

1003所对应的这个表达式

你看是不是就是这个表达式

1 多少时 对吧

也就是说秒数是1跟10的时候会触发

好 现在应该还没有到

还没有到 现在到了

你看这是101

然后现在我们直接来测试一下

咱们把这边刷新一下

好 然后找到我们

这个什么呢

更新定时任务

就是这个 对吧

现在呢 我就改这个1003这个

所以这个bizid呢

就是我们设置的1003这个

然后这个表达式呢

咱们稍微给它改一下

能看出区别来就可以了

原先这不是写的是

10吗 对吧

然后呢 我把它抄过来

我改成

10 120

能看出区别来就可以了

然后呢 我们来

先来观察一下控制台

它是不是已经出出了

是不是1 然后10

下一次执行了

肯定就是10点33分01秒的时候

是不是会触发

现在呢 我们把它清理掉

然后呢 执行一下

注意看啊 走 执行

那就意味着什么呢

那就意味着

它是不是应该是11秒20秒的时候会触发

现在时间还没有到

咱们直接来看一下数据库里边

看看这个地方有没有变过来

刷新一下

你看这是不是已经更新过来了

就是11 20

然后呢 再观察一下它这个触发的时间

你看 哎 这是不是是33分11秒

如果没有改成功的话呢

原先它是不是01秒 对吧

现在呢 改成11秒

然后是20

好 所以说呢

我们这样来验证一下就可以了

其实呢 我们直接看这个表更加清楚

对吧

从这能看出来

它这个表达是已经更新过来了

包括什么呢

包括它这个trigger name

你看是不是这个地方也更新过来了

对吧

1003

然后呢 在刚才这个表里面呢

也有一个trigger name

你看这个它是不是也是1003

那么这样的话呢

我们更加能够通从表里面呢

更加能直观看到啊

具体是哪个触发器改变了

好 这是关于咱们这个动态的更新定时任务

我们测试了一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频演示了如何在 Spring Boot 项目中，通过 REST API 动态更新 Quartz 定时任务的执行频率（Cron 表达式）。核心操作是调用 `PUT /quartz` 接口，传入任务 ID (`bizId`) 和新的 Cron 表达式。后端代码通过 Quartz API 获取现有触发器，根据新表达式重建触发器，并调用 `scheduler.rescheduleJob()` 方法重新调度任务。整个过程通过 Swagger UI 进行调用，并在控制台和数据库中验证了任务配置的更新。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示项目结构，定位到 `QuartzController.java` 文件。
*   **00:00:05 - 00:00:15**: 代码高亮显示 `@PutMapping` 注解的 `update` 方法，该方法用于更新定时任务。
*   **00:00:15 - 00:00:25**: 代码逻辑解析：获取触发器的唯一标识 `TriggerKey`，然后通过 `scheduler.getTrigger()` 获取对应的 `CronTrigger`。
*   **00:00:25 - 00:00:35**: 代码逻辑解析：使用 `CronScheduleBuilder` 根据传入的 `cronExpression` 构建新的调度规则。
*   **00:00:35 - 00:00:45**: 代码逻辑解析：调用 `trigger.getTriggerBuilder().withIdentity(...).withSchedule(...).build()` 重新构建触发器对象。
*   **00:00:45 - 00:00:55**: 代码逻辑解析：调用 `scheduler.rescheduleJob(triggerKey, trigger)` 方法，将新触发器应用到任务上。
*   **00:00:55 - 00:01:05**: 展示 Swagger UI 界面，定位到 `PUT /quartz` 接口。
*   **00:01:05 - 00:01:15**: 在 Swagger UI 中填写参数：`bizId` 为 `1003`，`cronExpression` 为 `11,20 * * * ?`。
*   **00:01:15 - 00:01:25**: 执行更新操作，观察控制台日志，确认 `MisfireHandler` 处理了错过触发的事件。
*   **00:01:25 - 00:01:35**: 查看 Navicat 数据库，确认 `qrtz_cron_triggers` 表中的 `CronExpression` 字段已更新。
*   **00:01:35 - 00:01:45**: 观察控制台日志，确认任务已按新的调度规则执行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 (Java)**:
    ```java
    @PutMapping("更新定时任务")
    @ApiOperation("更新定时任务")
    public String update(String bizId, String cronExpression) throws Exception {
        TriggerKey triggerKey = TriggerKey.triggerKey(bizId);
        CronTrigger trigger = (CronTrigger) scheduler.getTrigger(triggerKey);
        CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression).withMisfireHandlingInstructionDoNothing();
        trigger = trigger.getTriggerBuilder().withIdentity(triggerKey).withSchedule(cronScheduleBuilder).build();
        scheduler.rescheduleJob(triggerKey, trigger);
        return "OK";
    }
    ```
    *   **关键点**:
        *   `@PutMapping`: HTTP PUT 请求映射。
        *   `TriggerKey.triggerKey(bizId)`: 通过业务 ID 获取触发器的唯一标识。
        *   `scheduler.getTrigger(triggerKey)`: 获取指定触发器。
        *   `CronScheduleBuilder.cronSchedule(cronExpression)`: 根据 Cron 表达式构建调度规则。
        *   `trigger.getTriggerBuilder().withIdentity(...).withSchedule(...).build()`: 重新构建触发器。
        *   `scheduler.rescheduleJob(triggerKey, trigger)`: 重新调度任务。
*   **数据库表 (Navicat)**:
    *   `qrtz_triggers`: 存储触发器信息，包含 `TRIGGER_NAME`, `JOB_NAME`, `CronExpression` 等字段。
    *   `qrtz_cron_triggers`: 存储 Cron 表达式信息，包含 `TRIGGER_NAME`, `CronExpression` 等字段。
*   **Swagger UI**:
    *   提供了 `POST /quartz` (添加任务), `PUT /quartz` (更新任务), `DELETE /quartz` (删除任务), `PUT /quartz/pause/{bizId}` (暂停任务), `PUT /quartz/resume/{bizId}` (恢复任务) 等接口。
*   **日志 (控制台)**:
    *   `自定义Job.bizId = 1003 执行时间2020-09-15 10:32:08.332` (旧执行时间)。
    *   `自定义Job.bizId = 1003 执行时间2020-09-15 10:33:20` (新执行时间)。
    *   `[MisfireHandler] ... Handling 1 trigger(s) that missed` (处理错过触发的事件)。

---

### 4) 关键场景与演示描述

1.  **场景一：代码逻辑演示**
    *   **描述**: 视频首先展示了 `QuartzController.java` 中的 `update` 方法。讲师通过逐行代码高亮，解释了如何获取触发器、构建新调度规则、重新构建触发器并最终调用 `rescheduleJob` 方法来更新任务。
    *   **技术要点**: 重点讲解了 Quartz API 的使用，特别是 `CronTrigger` 和 `CronScheduleBuilder` 的作用。

2.  **场景二：Swagger UI 调用演示**
    *   **描述**: 讲师切换到 Swagger UI 界面，定位到 `PUT /quartz` 接口。他填写了 `bizId` 为 `1003` 和 `cronExpression` 为 `11,20 * * * ?`，然后点击“Execute”按钮。
    *   **技术要点**: 展示了如何通过 REST API 调用后端服务，验证了接口的可用性。

3.  **场景三：日志与数据库验证**
    *   **描述**: 在执行更新后，讲师查看了控制台日志，确认了任务的执行时间从旧的时间点更新到了新的时间点，并且日志中出现了 `MisfireHandler` 的信息，表明系统处理了因更新导致的错过触发事件。同时，他打开了 Navicat 数据库工具，查询了 `qrtz_cron_triggers` 表，确认了 `CronExpression` 字段已成功更新。
    *   **技术要点**: 通过日志和数据库双重验证，证明了代码逻辑的正确性和数据的一致性。

4.  **场景四：任务执行验证**
    *   **描述**: 在更新完成后，讲师再次查看控制台日志，确认了任务在新的调度规则下成功执行。
    *   **技术要点**: 通过观察任务的执行日志，验证了更新操作的实际效果。

---

以上是根据视频画面进行的结构化分析，涵盖了视频的主要内容和技术要点。
