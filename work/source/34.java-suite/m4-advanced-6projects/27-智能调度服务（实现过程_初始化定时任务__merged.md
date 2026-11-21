# 27-智能调度服务（实现过程_初始化定时任务_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢我们是测试了一下

咱们因为原先这个数据呢

这些定时任务呢都初始化

都已经初始化过了对吧

所以说呢

全都是走的我们这个地方else这个分支

然后呢我们可以造一条新的数据啊

咱们造一条新的数据

然后呢我们就再往后啊

来一个比如说我来个11

然后呢这个bin name呢

还是写这个

还是写这个

然后呢这个呢也是transfer

然后这个表达式呢

我们比如说是每隔三秒让它出发一次

对吧

0-3

这是每隔三秒出发一次

好

然后这个呢是状态

状态是1表示正常

business id啊

这个id的话我们可以随便来一个

比如说我就给个123

然后这creator呢这是创建者对吧

然后随便给个值

OK

那么现在呢

咱们是添加了一个新的数据对吧

就是这个id是11的这条数据啊

然后接下来呢

我们就来重新启动一下咱们这个项目啊

重新启动一下这个项目

同样的还是在这加上这个钻点

这一次呢

当它循环到我们这条数据的时候呢

那么它就会去创建一个新的定时任务

然后任务的id是是多少呢

是不是就是我们这个任务的id就是11

对吧

好

好

那现在我们重新来启动一下

好

这个钻点呢已经过来了对吧

好

过来之后呢

我们可以往下走一下

走

看要查

好

查出来之后呢

看这个记录是39

这因为多了一条记录对吧

多了一条记录

就是这个id是11的这条记录

好

id是11

然后这是它那个表达式

是吧

然后呢

我们接下来看一下啊

往下走

这一次呢

第一个编列出来的

应该还是原先的数据啊

原先的

你看id是10的这个

是10的话呢

那么它应该还是走else这个分支

然后呢

我们可以在这儿加一个钻点啊

要不然你一放行了

它就全跑过去了

好

然后呢

我们直接走

这第二个

第二个是谁呢

来看一下id是

还是这串对吧

这串的话应该是原先的数据

那这样的话呢

它应该走的还是else这个分支

好

那么我们直接放过去

看这个是谁呢

这个也是

好

那么

放过去

这个

这个就是id是11

这是我们刚才手动添加的这条数据

对吧

好

那如果是这个的话呢

我们看走

看现在这个con trigger

它是不是等于空

对吧

因为这是我们刚才手动刚添的一条数据

那么还没有创建过定时任务

所以它是不可能有对应的这个触发器的

所以说呢

这个时候呢

我们就会执行if这个分支

然后这个if分支一执行

其实就是什么呢

就会像我们这个

这个

这个表

咱们来看一下这个什么triggers这个表里边来插入数据

你看现在这个里边一共是有多少条数据呢

是有39条数据对吧

然后呢我们给它放行

走

后边这个就不用看了

全都放过去

然后呢

回过头来看这张表刷新一下注意看

刚才它其实已经更新了对吧

已经更新成40条

那么多出来的是哪一条呢

就是这个就是task-11

因为什么呢

因为我们这个触发器的名字啊

包括这个触发器的名字

它这个命名是有规则的

就是什么呢

这个前缀加上11加上它这个主键

这个是有哪指定的呢

你看啊

我们刚才看到的这个地方是不是来设置咱们这个触发器的时候呢

是不是有一个位置identity对吧

位置identity

这就是它的唯一标识

唯一标识呢

是怎么构成的呢

就是我们把这个主键值是不是传进来

然后呢

前面是不是加上这个常量

而这个常量的话呢

是不是就是这个task下滑线

然后再加上这个主键值

所以你看我们刚才那个主键值是不是11

前面的是task下滑线

所以就构成了我们这个触发器它的名字

所以这条数据是不是就已经插进来了

但是不仅仅是这一张表对吧

那么它所对应的这个触发时间呢

应该是在这个表里面是不是还有一条记录

好你看11的就是这个对吧

这是它那个触发的时间

它会记录在这儿

但是这些表也就是上面这堆表操作

我们不用管

我们不用管

我们要做的就是去调它的这个它的这个API

对不对

我们来创建这个触发器

来创建这个job detail

然后最后来调度

你直接调它这套API就可以

那么这个cause框架呢

它自己会去操作这套表

所以我们只要知道它做了这个事情就可以了

然后呢

我们现在已经给它放行了对吧

那么现在呢

这就说明我们这个定时任务应该是已经触发好了

那现在它是不是有没有正常在调度呢

看一下控制台

你看它其实已经开始调度了对吧

定时任务开始执行

刚才呢我们创建的那个是什么呢

是ID是11的对不对

这能区分出来啊

这个是ID是1的

然后呢还有ID是11的这些

然后呢我们刚才看到是每隔3秒是不是触发一次

你看这是不是42 45 48

对吧

然后呢

这个刷新的比较多啊

比较快啊

那么从这呢

我们就已经测试出来了

是没有问题的

这是关于我们手动往这里面

这个表里面添加一条数据对吧

那么它在初始化的时候呢

也是可以正常的把它创建出来的

好

那么这是关于咱们这个初始化

初始化定时任务这块

我们先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程主要演示了如何在 Spring Boot 项目中，利用 Quartz 定时任务框架，通过代码动态初始化和管理数据库中已定义的定时任务。核心内容包括：
- **环境与数据准备**：通过 Navicat 连接数据库，查看 `schedule_job` 表中已存在的定时任务记录。
- **核心代码逻辑**：在 `DispatchCommandLineRunner` 类中，通过 `ScheduleJobMapper` 查询所有任务，然后遍历每个任务，调用 `ScheduleUtils` 工具类中的 `createScheduleJob` 或 `updateScheduleJob` 方法，根据任务的触发器（CronTrigger）是否存在，来决定是创建新任务还是更新已有任务。
- **工具类实现**：`ScheduleUtils` 类中的 `createScheduleJob` 方法，通过 `JobBuilder` 和 `CronScheduleBuilder` 构建 `JobDetail` 和 `CronTrigger`，并最终调用 `scheduler.scheduleJob(jobDetail, trigger)` 将任务注册到 Quartz 调度器中。
- **运行与验证**：在控制台中运行 `DispatchCommandLineRunner`，观察日志输出，确认任务被成功创建并执行。同时，通过数据库表 `qrtz_triggers` 验证任务状态。

整个过程展示了如何将数据库中的定时任务配置与代码逻辑进行联动，实现“数据驱动”的定时任务管理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序进行的划分：

- **00:00 - 00:05**: **环境与数据准备**。展示 Navicat 数据库管理工具，连接到 `pd_dispatch` 数据库，并查看 `schedule_job` 表，确认存在 39 条记录。
- **00:05 - 00:15**: **核心代码逻辑演示**。在 IntelliJ IDEA 中打开 `DispatchCommandLineRunner.java` 文件，讲解 `run` 方法的逻辑：查询数据库、遍历任务、根据触发器是否存在决定创建或更新。
- **00:15 - 00:25**: **工具类 `ScheduleUtils` 实现**。聚焦于 `createScheduleJob` 方法，展示如何使用 `JobBuilder` 和 `CronScheduleBuilder` 构建任务和触发器。
- **00:25 - 00:35**: **任务创建与执行**。在控制台中运行程序，观察日志输出，确认任务被成功创建并执行。
- **00:35 - 00:45**: **数据验证**。回到 Navicat，查看 `qrtz_triggers` 表，验证任务状态，确认任务已成功注册。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

- **PPT 页面**：展示了一个名为“智能调度操作”的界面截图，说明了定时任务可以通过定时自动触发，也可以由人工立即执行。
- **数据模型图**：展示了 Quartz 的核心数据表结构，包括 `QRTZ_SIMPLE_TRIGGERS`、`QRTZ_CALENDARS`、`QRTZ_LOCKS`、`QRTZ_CRON_TRIGGERS` 和 `QRTZ_SCHEDULER_STATE` 等表，以及它们的字段。

#### 代码

- **`DispatchCommandLineRunner.java`** 中的 `run` 方法：
  ```java
  @Override
  public void run(String... args) throws Exception {
      log.info("开始进行定时任务初始化...");
      List<ScheduleJobEntity> list = scheduleJobMapper.selectList(queryWrapper: null);
      for (ScheduleJobEntity scheduleJobEntity : list) {
          CronTrigger cronTrigger = ScheduleUtils.getCronTrigger(scheduler, scheduleJobEntity.getId());
          if (cronTrigger == null) {
              // 触发器对象为空，说明对应的定时任务还没有创建
              ScheduleUtils.createScheduleJob(scheduler, scheduleJobEntity);
          } else {
              // 触发器对象不为空，说明对应的定时任务已经存在了，此时只需要更新
              ScheduleUtils.updateScheduleJob(scheduler, scheduleJobEntity);
          }
      }
  }
  ```

- **`ScheduleUtils.java`** 中的 `createScheduleJob` 方法：
  ```java
  public static void createScheduleJob(Scheduler scheduler, ScheduleJobEntity scheduleJob) {
      try {
          // 构建 job 信息
          JobDetail jobDetail = JobBuilder.newJob(ScheduleJob.class)
                  .withIdentity(getJobKey(scheduleJob.getId()))
                  .build();

          // 表达式调度构建器
          CronScheduleBuilder scheduleBuilder = CronScheduleBuilder.cronSchedule(scheduleJob.getCronExpression())
                  .withMisfireHandlingInstructionDoNothing();

          // 按新的 cronExpression 表达式构建一个新的 trigger
          CronTrigger trigger = TriggerBuilder.newTrigger()
                  .withIdentity(getTriggerKey(scheduleJob.getId()))
                  .withSchedule(scheduleBuilder)
                  .build();

          // 放入参数，运行时的方法可以获取
          jobDetail.getJobDataMap().put(JOB_PARAM_KEY, scheduleJob);

          // 调度器注册任务
          scheduler.scheduleJob(jobDetail, trigger);

          // 暂停任务
          if (scheduleJob.getStatus() == ScheduleStatus.PAUSE.getValue()) {
              pauseJob(scheduler, scheduleJob.getId());
          }
      } catch (SchedulerException e) {
          throw new PdException("CREATE ERROR", e);
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：数据库初始化**。讲师首先在 Navicat 中打开 `schedule_job` 表，展示其中包含 39 条记录，每条记录代表一个待初始化的定时任务。这为后续的代码操作提供了数据基础。

- **场景二：代码逻辑演示**。讲师在 IntelliJ IDEA 中打开 `DispatchCommandLineRunner.java`，逐行讲解 `run` 方法。重点演示了如何通过 `scheduleJobMapper.selectList` 查询所有任务，然后遍历 `for` 循环，调用 `ScheduleUtils.getCronTrigger` 获取触发器对象。通过 `if (cronTrigger == null)` 判断，决定是调用 `createScheduleJob` 还是 `updateScheduleJob`。

- **场景三：工具类实现**。讲师切换到 `ScheduleUtils.java`，重点讲解 `createScheduleJob` 方法。演示了如何使用 `JobBuilder` 构建 `JobDetail`，使用 `CronScheduleBuilder` 构建 `CronTrigger`，并最终调用 `scheduler.scheduleJob(jobDetail, trigger)` 将任务注册到调度器中。

- **场景四：运行与验证**。讲师在控制台中运行 `DispatchCommandLineRunner`，观察日志输出。日志显示“2020定时任务开始执行”，并记录了任务 ID 和执行时间，证明任务已成功创建并执行。同时，讲师也展示了如何通过 `pauseJob` 方法暂停任务。

- **场景五：数据验证**。讲师回到 Navicat，查看 `qrtz_triggers` 表，确认任务状态，验证了代码逻辑的正确性。

整个演示过程逻辑清晰，从数据准备到代码实现再到运行验证，完整地展示了如何在 Spring Boot 项目中实现 Quartz 定时任务的动态初始化。
