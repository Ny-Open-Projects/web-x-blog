# 17-Quartz动态定时任务（更新定时任务_代码实 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 接下来呢

咱们继续来看我们COS的动态定时任务

下面这个呢是更新定时任务

这个更新定时任务啊

我们主要更新的是什么呢

主要更新的就是这个定时任务

它的触发时间

比如说呢

我原先的这个触发的时间呢

是什么呢

每天上午10点钟触发

现在呢

我希望给它改成每天下午5点钟来触发

这个时候呢

我就可以通过更新定时任务

来修改它的这个触发的时间

好

那么要修改的话呢

咱们来看一下

我们需要传过来这么两个参数

一个呢是BIZID

这个呢是用来找到原先的那个触发器

对吧

比如说每天上午10点触发

那么我们当时肯定是写了一个触发的规则

对吧

通过那个coin表达式

然后呢通过BIZID呢

就可以找到原先的那个触发器

然后呢

新的这个触发规则呢

通过传过来的这个coin expression

对吧

重新来表达

比如说我这个触发器呢

描述的就是什么呢

每天下午5点来执行

好

那这就需要什么呢

我们当时啊

在新添加一个定时任务的时候

是不是需要来创建啊

你看这是我们save方法

需要来创建这个触发器

对吧

来创建触发器的时候呢

需要指定这个触发器

它的唯一标识

这个地方呢

我们当时好像是没有去指定

对吧

那么没有指定的话呢

这个curls框架呢

它会给我们去随机生成一个唯一标识

好

咱们可以来看一下

就在这个curls框triggers这个表里面

你看

这里面是不是有我们的这个job name

对吧

这个job name呢

对应的就是我们传过来的这个biz id

当时我们是不是传过来1002 1001

然后呢

在这调用with identity

是不是设置它的唯一标识

对吧

这样的话呢

那么它在这记录的就是我们这个job name

而它这个trigger呢

也有name

而它这个name呢

我是不是没有去调用那个with identity

那个方法

所以框架呢

就随机给我们生成了一个这么长

对吧

它为了保证不重复啊

就类似于uuid的

那么非常长的这么一个字符串

但是呢

这样的话

我们如果是框架帮我们生成

我们并不知道它给我生成的这个字符串

到底是什么

对吧

所以说呢

我们这个地方呢

可以稍微改一下

就是什么呢

我们在创建这个出发器的时候呢

不用它给我们随机生成了

我们自己来指定一下

咱们在这呢

来通过调用with identity

在这呢

我也使用这个bizid

对吧

其实就是我们的uid

好

然后呢

这样我就自己来指定了

咱们呢

可以先来测试一下这个方法

就是确认一下什么呢

我们这个地方

这个trigger name呢

使用咱们自己指定的这个bizid

而不再是让框架给我们去生成了

先把这块呢

解决一下

然后呢

我们再翻回头来

来说这个什么呢

更新定时任务

因为一会儿呢

我们需要干什么呢

把原形呢

先这个出发器对象呢

给它获取出来

而获取的时候呢

会使用到这个唯一标识

对吧

现在呢

我们可以重新来测试一下

这个save方法

好

服务呢

已经跑起来了

没啥问题

然后呢

我们重新把这边来刷新一下

找到咱们这个什么呢

save

就是这个

添加定时任务

对吧

然后呢

try it out

比如说我在这来个1003

对吧

然后这个con表达式呢

我就随便写一个

啊

啊

,然后呢

我们回过头来来看

咱们现在呢

是不是要修改一下

我们这个出发的规则

对吧

那么我们需要来整一个update的方法

咱们呢

就把这个动态添加的这个方法呢

复制一下

然后到这边来

给它修改一下

修改的话呢

这个就不应该是post mapping了

应该是什么呢

应该是put mapping

对吧

好put mapping

这是动态修改

好

或者叫做更新吧

更新定时任务

更新定时任务

这个方法名呢

改成什么呢

update

然后这个参数的话呢

咱们还是使用这两个参数

对吧

这个参数就不用改了

好

先把这个服务停掉啊

然后呢

把这里边的代码都给删掉

我们重新来写一下

也就是说呢

我们现在需要来获得原先的那个触发器

原先的触发器

好

现在已经停掉了

原先的这个触发器呢

刚才也看到了

它的这个触发器的name是不是叫做1003

对吧

好

所以我们在这呢

需要获得原先的触发器

怎么获得呢

我们使用这个什么呢

使用这个scheduler.gettrigger

gettrigger

你看

是不是就可以获得我们原先的这个触发器

然后呢

它传进来的是一个什么呢

是一个trigger key对不对

其实就是用来标识我们每一个触发器的

好

trigger key.trigger key

然后这个name是不是就是我们这个bizid

传过来的bizid

这样的话呢我们就获得了一个trigger key

这个你可以认为这是什么呢

这就是我们触发器

触发器的这个唯一标识对吧

唯一标识

然后呢通过这个唯一标识

咱们就可以来获得原先的触发器

你看

原先的我们这个触发器是一个con trigger对吧

这个con的

就是基于con表达式的这种

所以呢我们在这儿呢给它强转一下

强转成这种con trigger

把这个去掉

来

强转一下con trigger

我们可以看一下

你看这个con trigger它是不是继承了咱们这个trigger

对吧

向下转型一下转成这个con trigger

这是获得我们原先的这个触发器对吧

然后呢我们现在呢

需要来修改一下原先的这个触发器

因为触发规则变了

主要就是这个什么呢表达式是不是发现了呢

主要就是这个什么呢表达式是不是发现了呢

所以说我们在这儿呢就需要通过咱们原先的

这是原来的触发器啊

这是获得

原来的

这个触发器

现在呢需要给它来改变一下触发规则

重新设置一个触发规则对吧

怎么设置呢

通过它呢get一个什么呢trigger builder

重新构建一个触发器

重新构建一个触发器

好

然后点什么呢

with identity

咱们这个标识呢还是使用原先的这个标识

然后接下来呢with

什么呢schedule

在这是不是来指定什么呢

指定我们新的触发规则对吧

那么使用这个with schedule

好

最后呢调用这个build方法对吧

调用build方法

来创建一个新的触发器出来

但是这儿呢我们还附给它自己也可以

就不用生命一个新的变量了啊

就不用生命一个新的变量了

好

还附给它自己

然后呢这个地方呢还报的错呢

它是不是要求我们传一个什么呢

这个

传一个builder进来对吧

schedule

所以我们在这呢就需要重新来构造啊

构造新的这个触发规则

构造

新的

触发规则

怎么构造呢

使用这个contriggerbuilder

点什么呢

前面我们都写过了

cont

schedule

然后在这是不是要把我们这个表达式传进去

然后呢再来指定一下什么呢

这还是这个什么do nothing对吧

就是

如果错过了那个触发时间它就什么都不做

好

这样的话呢我们是不是就获得了这么一个新的触发规则呢

这个触发规则

然后呢把这个触发规则构建器

把它放进来

就可以了

好

那这样的话呢我们这个新的

触发器是不是相当于就已经构造好了

然后呢使用这个新的这个触发规则

然后呢这个

触发器构造好之后呢需要使用我们这个schedule重新来

叫做ray

schedule

来看一下应该叫做

ray schedule job

就是重新进行调度

重新进行调度

按照新的规则进行调度

然后呢在这呢传进来这么两个参数一个是trigger key

还有一个是新的trigger

一个是trigger key

还有一个是新的这个trigger对象

这是重新

重新

按照什么呢

按照新的规则进行调度

需要调用一下这个方法

按照新的规则进行调度

那这样的话呢我们

一调用这个update的方法

在不重启服务的情况下呢

其实我们这个触发规则就已经发生变化了

一会儿呢我们可以来测试一下

这个呢这就是

调用咱们这个ray schedule job方法

然后呢更新我们定时任务

主要更新的就是我们触发的这个时间

一会儿呢我们来测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 项目中集成 Quartz 定时任务框架，实现对动态定时任务的“更新”功能。讲师通过 IntelliJ IDEA 编辑器演示了如何在 `QuartzController` 中编写一个 `update` 方法，该方法允许用户通过 HTTP PUT 请求，传入任务 ID (`bizId`) 和新的 Cron 表达式 (`cronExpression`)，来修改已存在的定时任务的执行频率。核心操作是：先根据旧的 `TriggerKey` 获取当前的触发器 (`CronTrigger`)，然后使用新的 Cron 表达式构建一个新的触发器，最后调用 `scheduler.rescheduleJob()` 方法，将旧任务的触发器替换为新触发器，从而实现任务的动态更新。视频中也展示了如何通过 Swagger UI 调用接口，并在控制台中查看任务执行日志。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，定位到“2.3.6 更新定时任务”章节。
*   **00:00:05 - 00:00:15**: 展示 `QuartzController` 中 `update` 方法的初始代码框架，准备编写更新逻辑。
*   **00:00:15 - 00:00:30**: 讲师在 `update` 方法中，通过 `scheduler.getTrigger(triggerKey)` 获取当前任务的触发器对象。
*   **00:00:30 - 00:00:45**: 讲师使用 `trigger.getTriggerBuilder()` 方法，结合新的 Cron 表达式，构建一个新的触发器。
*   **00:00:45 - 00:01:00**: 讲师调用 `scheduler.rescheduleJob(triggerKey, trigger)` 方法，将旧的触发器替换为新的触发器，完成任务更新。
*   **00:01:00 - 00:01:15**: 展示 `QuartzController` 中 `save` 方法的代码，用于创建新任务，作为对比和上下文。
*   **00:01:15 - 00:01:30**: 展示 Swagger UI 界面，演示如何通过 HTTP PUT 请求调用 `update` 接口。
*   **00:01:30 - 00:01:45**: 展示控制台日志，显示任务成功更新后的执行信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`第8章 智能调度服务(pd-dispatch)` -> `2.3 实现定时任务` -> `2.3.6 更新定时任务`。
    *   代码注释：`//表达式调度构建器`、`//获取触发器对象`、`//关联任务实例和触发器对象`、`//重新按新的规则进行调度`。

*   **关键代码片段**:

    **1. `save` 方法 (用于创建任务)**

    ```java
    @PostMapping("/quartz/添加定时任务")
    @ApiOperation("添加定时任务")
    public String save(String bizId, String cronExpression) throws Exception {
        JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity(bizId).build();
        jobDetail.getJobDataMap().put("bizId", bizId);
        CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression).withMisfireHandlingInstructionDoNothing();
        Trigger trigger = TriggerBuilder.newTrigger().withIdentity(bizId).withSchedule(cronScheduleBuilder).build();
        scheduler.scheduleJob(jobDetail, trigger);
        return "OK";
    }
    ```

    **2. `update` 方法 (用于更新任务)**

    ```java
    @PutMapping("/quartz/更新定时任务")
    @ApiOperation("更新定时任务")
    public String update(String bizId, String cronExpression) throws Exception {
        // 获取触发器的唯一标识
        TriggerKey triggerKey = TriggerKey.triggerKey(bizId);

        // 获得原有的触发器
        CronTrigger trigger = (CronTrigger) scheduler.getTrigger(triggerKey);

        // 构造新的触发规则
        CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression).withMisfireHandlingInstructionDoNothing();

        // 重新构建触发器
        trigger = trigger.getTriggerBuilder().withIdentity(bizId).withSchedule(cronScheduleBuilder).build();

        // 重新按新的规则进行调度
        scheduler.rescheduleJob(triggerKey, trigger);

        return "OK";
    }
    ```

*   **关键公式 / 图表**:
    *   **无**。视频中未出现数学公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：创建任务 (save 方法)**

    讲师首先在 `QuartzController` 中展示了 `save` 方法。该方法接收 `bizId` 和 `cronExpression` 参数，使用 `JobBuilder` 创建一个 `JobDetail`，并将其与一个 `CronTrigger` 关联，最后通过 `scheduler.scheduleJob()` 将任务注册到 Quartz 调度器中。讲师通过 Swagger UI 发送一个 POST 请求来测试此功能，并在控制台中看到任务成功创建并执行的日志。

*   **场景二：更新任务 (update 方法)**

    讲师随后开始编写 `update` 方法。他首先通过 `TriggerKey.triggerKey(bizId)` 获取任务的唯一标识，然后调用 `scheduler.getTrigger(triggerKey)` 获取当前的 `CronTrigger` 对象。接着，他使用 `CronScheduleBuilder.cronSchedule(cronExpression)` 构建一个新的调度规则，并调用 `trigger.getTriggerBuilder().withIdentity(bizId).withSchedule(...).build()` 重新构建触发器。最后，他调用 `scheduler.rescheduleJob(triggerKey, trigger)` 方法，将旧的触发器替换为新的触发器，从而实现了任务的动态更新。讲师在代码中添加了注释，清晰地说明了每一步操作。

*   **场景三：错误处理与调试**

    在演示过程中，讲师也展示了如何处理错误。例如，当传入一个非法的 Cron 表达式时，控制台会抛出 `java.text.ParseException: Unexpected character` 异常，这有助于开发者理解输入参数的约束条件。

*   **场景四：Swagger UI 调用**

    讲师在 Swagger UI 界面中演示了如何通过 HTTP PUT 请求调用 `update` 接口。他输入了任务 ID 和新的 Cron 表达式，然后点击“执行”，系统返回 `OK`，表明任务更新成功。

---

通过以上分析，我们可以清晰地理解视频中演示的 Quartz 动态更新定时任务的核心逻辑和实现步骤。
