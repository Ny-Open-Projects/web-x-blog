# 13-Quartz动态定时任务（暂停定时任务） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢

咱们是完成了我们这个动态的添加定时任务

对吧

并且呢我们进行了一个测试

这个地方呢

我们再来简单说一下

就是什么呢

我们添加的这个定时任务呢

最终呢是调用这个方法

是不是进行了一个关联

那么底层呢

它就会操作数据库

然后呢把我们这个任务信息呢

是不是把它保存在咱们这个表里面去

对吧

前面呢我们也简单看了一下

包括什么呢

我们设置的这些通过这个job datamap

对吧

设置的这些值

它其实也进行了保存

那么具体保存在哪呢

是保存在这个job details

这个表里面去了

你看

它是只不过我们这看起来呢

不太直观

因为什么呢

它用的是这么一个blob字段

对吧

只能显示它这个228 bytes

这么多大小

对吧

那么保存到的就是这个job data

这个字段上

好

所以说呢

我们存储的这些值呢

也都存在

然后呢

我们如果把这个服务重启之后呢

哎

这些状态信息呢

其实都是可以重新获取到的

因为它是持久化到了我们的表里面

对吧

并且前面我们也重点强调了

为什么现在呢

它是把任务信息保存到数据库了呢

就是因为我们是不是在这个配置类里边

是不是在这设置的是什么呢

设置的这个job stop

点class

对吧

就是我们这个job存储的类呢

使用的是gdbc这种方式

也就是最终呢

是把任务信息把它持久化到数据库

这样的话呢

你看我服务重启了这些信息呢

服务重启之后啊

咱们这些定时任务呢

还是能够正常执行

并且呢

我们设置的状态信息

那么都是能够获取到的

哎

你看它现在是不是又开始执行了

对吧

这个bizid呢

是不是就是我们动态获取出来的

啊

但是当时呢

咱们是不是是添加了两个

对吧

哎

添加了两个这个动态的定时任务

好

那接下来呢

我们来看下一个

下一个呢

就是暂停定时任务

就是说我现在这个定时任务呢

我想把它暂停

不再执行了

哎

但是并不是删除

对吧

只是暂停

那这样的话呢

我们只需要调用这个scheduler

它的一个叫做pass job

这么一个方法

好

然后呢

你要暂停的是哪个任务呢

我们需要传进来一个job key

而这个job key的话呢

哎

是通过这个job key

它的一个静态方法来封装出来的

那么关键呢

就是这个

啊

这个bizid对应的是谁呢

其实就是我们当时动态添加定时任务的时候

咱们是不是设置了一个叫做

viz identity

对吧

对吧

其实就是

这个定时任务

它的一个唯一的id

对不对

它的标识

所以说我们停止的时候呢

肯定是要

也要使用这个标识来停止

哎

这就相当于就是我们任务的一个唯一标识

好

那接下来呢

我们先把这个服务呢

给停掉

然后呢

咱们在这个controller当中啊

动态的再来添加这么一个方法

呃

找到我们这个controller

这个有点乱了

咱们把这些呢

都关上

然后重新打开一下

我们这个controller

然后在这个地方呢

咱们添加一个新的方法

呃

从这来复制一下

这个暂停呢

是比较简单的

比这个添加要简单

在这来写一下

暂停定时任务

pass

对吧

然后呢

我们来看一下

这个参数呢

直接给它拿过来吧

通过我们这个pass variable

这个注解来描述

这就意味着我们

这个

变量呢

是通过这个

请求路径

这种方式

是不是给我们提交过来

对吧

对吧

对吧

好

把这呢

改一下

这个就是暂停定时任务

好

然后要暂停的话呢

就非常简单了

咱们是不是直接调用什么呢

刚才看到的叫做scheduler

它得有这么一个方法

对吧

叫做pass job

然后呢

我们这个地方呢

需要传入一个什么呢

叫做job key

对吧

job key

好

而这个job key的话呢

如何来封装呢

就是使用我们传过来的

这个biz id啊

biz id

这样来封装一下就可以

好

这个呢

就是停止什么呢

指定的

暂停

指定

job

它的这个执行

ok

那接下来呢

我们就来测试一下

这个方法

到底能不能

好使

那接下来呢

我们来启动一下

当然了

我们一定要保证

我们传过来的这个什么呢

biz id是存在的

对吧

你不能暂停一个

不存在的这个job

好

稍等一下

好

好

好

好

好

好

好

好

WET OUT

在这输入一个什么呢

比如说我现在啊

我就随便来一个

1001吧

好

1001

也就是说

我只要掉这个方法

是不是就

它就会暂停

对吧

那么它就不再去执行了

现在我们来看

它现在还在执行

对吧

还有执行

我把控制台清理一下

然后呢

我们再执行

好

返回了OK

对吧

返回OK

然后呢

我们来观察控制台

但是这个

需要稍微

等几秒钟的时间啊

因为我们是不是写了一个那个

con表达式对吧

咱们呢可以结合着我们这个数据库

这边来看一下

来刷新一下

然后呢我们来看看

它是什么时间点出发呢

它是不是应该是在我们那个

出发器里边对吧

在咱们这个出发器这个表

con trigger这个表

然后呢我们来看一下

这边刷新一下

你看1001那个是哪个呢

应该是上面这个对吧

150 20什么35 55对吧

这些秒的时候

那么会执行

然后呢我们来观察一下控制台

你看是不是只剩下1002对吧

那么1001的话并没有执行

就是因为什么呢

就是因为我们现在呢

调用了这个暂停的这个方法

那么它已经暂停了

比如说现在呢

我把这个1002也暂停了

我在这呢输入一个1002

这就是暂停

这个任务的执行

然后执行一下

好

现在已经暂停了

暂停之后呢

我们把控制台清理一下

正常的情况下呢

如果暂停成功的话呢

应该是控制台是没有输出的

因为这两个任务呢都暂停了

好

你看

到这边你看

那我们就不再多等了啊

从这呢就能看出来

我们调用这个方法对吧

就是暂停指定的任务的执行

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析报告。

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 项目中集成 Quartz 定时任务框架的教学内容，具体聚焦于“暂停定时任务”功能的实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 `QuartzController` 中编写一个 `@PutMapping` 接口，该接口接收一个业务ID (`bizId`)，并调用 Quartz 的 `scheduler.pauseJob(JobKey, JobKey)` 方法来暂停指定的定时任务。视频同时展示了如何通过 Swagger UI 调用此接口，并在控制台日志中验证任务暂停的效果。整个过程旨在说明如何动态管理 Quartz 定时任务的生命周期。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中定位到当前章节“2.3.2 暂停定时任务”，并展示其在目录结构中的位置。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，展示 `QuartzController.java` 文件，重点讲解 `pause` 方法的代码逻辑。
*   **00:00:15 - 00:00:30**: 讲师在代码中高亮显示 `scheduler.pauseJob(JobKey, JobKey(bizId));` 这一行，解释其作用是暂停指定ID的任务。
*   **00:00:30 - 00:00:45**: 讲师切换到终端窗口，展示 `QuartzApplication` 启动后的日志，确认 Quartz 服务已成功初始化。
*   **00:00:45 - 00:01:00**: 讲师在终端中执行了 `pause` 接口的调用，日志显示任务暂停成功。
*   **00:01:00 - 00:01:15**: 讲师切换到浏览器，打开 Swagger UI，展示 `PUT /quartz/pause/{bizId}` 接口的文档。
*   **00:01:15 - 00:01:30**: 讲师在 Swagger UI 中输入 `bizId=1001`，并点击“Execute”按钮，演示如何通过 HTTP 请求暂停任务。
*   **00:01:30 - 00:01:45**: 讲师返回 IDEA，查看终端日志，确认任务暂停后，后续的执行被阻止。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `2.3.2 暂停定时任务`
    *   **目录结构**: `品达物流TMS项目 > 第8章 智能调度服务(pd-dispatch) > 2. Quartz动态定时任务 > 2.3 实现定时任务 > 2.3.2 暂停定时任务`
    *   **接口注解**: `@PutMapping("/pause/{bizId}")` 和 `@ApiOperation("暂停定时任务")`

*   **代码关键内容**:
    *   **暂停任务方法**:
        ```java
        @PutMapping("/pause/{bizId}")
        @ApiOperation("暂停定时任务")
        public String pause(@PathVariable String bizId) throws Exception {
            JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity(bizId).build();
            JobKey jobKey = JobKey.jobKey(bizId);
            scheduler.pauseJob(jobKey);
            return "OK";
        }
        ```
    *   **添加任务方法 (用于对比)**:
        ```java
        @PostMapping("/quartz")
        @ApiOperation("添加定时任务")
        public String save(@PathVariable String bizId, String cronExpression) throws Exception {
            JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity(bizId).build();
            jobDetail.getJobDataMap().put("bizId", bizId);

            CronScheduleBuilder scheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression).withMisfireHandlingInstructionDoNothing();
            CronTrigger trigger = TriggerBuilder.newTrigger().withSchedule(scheduleBuilder).build();

            scheduler.scheduleJob(jobDetail, trigger);
            return "OK";
        }
        ```
    *   **配置文件内容**:
        ```properties
        org.quartz.scheduler.instanceName=WitlinkedScheduler
        org.quartz.scheduler.instanceId=AUTO
        org.quartz.threadPool.class=org.quartz.simpl.SimpleThreadPool
        org.quartz.threadPool.threadCount=20
        org.quartz.jobStore.class=org.quartz.impl.jdbcjobstore.LocalDataSourceJobStore
        ```

*   **图表/日志**:
    *   **终端日志**: 展示了 Quartz 服务启动、任务调度、以及任务暂停后的日志信息，例如：
        ```
        自定义Job.bizId = 1001 执行时间2020-09-15 09:19:55
        自定义Job.bizId = 1002 执行时间2020-09-15 09:19:57
        ```
        在暂停后，日志中不再出现 `bizId = 1001` 的执行记录。

---

### 4) 关键场景与演示描述

*   **场景一：代码编写与讲解**
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `QuartzController.java` 文件，逐行讲解 `pause` 方法。他重点解释了 `JobKey.jobKey(bizId)` 如何根据业务ID获取任务键，并调用 `scheduler.pauseJob(jobKey)` 来暂停任务。
    *   **演示**: 讲师在代码中高亮显示关键语句，并在终端中执行 `pause` 接口，观察日志变化。

*   **场景二：Swagger UI 调用演示**
    *   **描述**: 讲师切换到浏览器，打开 Swagger UI 页面，找到 `PUT /quartz/pause/{bizId}` 接口。
    *   **演示**: 讲师在参数框中输入 `bizId=1001`，点击“Execute”按钮，成功调用接口。随后，他返回 IDEA 查看终端日志，确认任务暂停成功。

*   **场景三：任务暂停效果验证**
    *   **描述**: 讲师在终端日志中观察到，`bizId=1001` 的任务在暂停后，其后续的执行被阻止，日志中不再出现该任务的执行记录。
    *   **演示**: 讲师通过对比暂停前后的日志，直观地验证了 `pause` 方法的有效性。

---

以上是根据视频画面进行的结构化分析。
