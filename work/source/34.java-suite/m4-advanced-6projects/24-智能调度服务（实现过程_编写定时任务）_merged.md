# 24-智能调度服务（实现过程_编写定时任务） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们这个智能调度服务

刚才我们是把这个基础环境已经搭建好了

这都是我们提前整理好的这些文件

然后我们直接把它导到我们这个项目当中来就可以了

然后下一个小节我们来编写定时任务

因为我们前面也说过

咱们这个智能调度可以通过定时任务这种方式来进行触发

所以说我们需要来开发一个定时任务这么一个类

然后我们这个类名就叫Scheduler Job

但是这个地方我们需要强调一下

我们现在是没有办法一次性的把最终的版本做出来

咱们先开发最简单的这么一个类

然后我们测试一下

看看这个类能不能正常跑起来

然后我们再进行完善

那么我们需要知道的是什么呢

我们这个定时任务它要做的事就是什么呢

它的业务逻辑就是要进行智能调度

具体就是来做

这个定时任务的任务

我们现在是在做的这个定时任务的任务

我们现在是在做的这个定时任务的任务

前面我们在学习Curse这个框架的时候也知道

作为一个定时任务是需要实现这个Job接口

或者是去继承它的这么一个副类

那么咱们这个地方就选择继承了

就继承这个叫做Curse Job Bin

Extends这个Curse Job Bin

我们直接导入一下

那么它为什么会报错呢

就是因为在这里边是不是有一个抽象的方法

是需要我们去做的

就是这个XQ的Internal

咱们先给这个类来加一个注解

这是我们的定时任务类

那么需要进行什么呢

进行我们这个智能调度操作

然后在这里边我们就先

现在先不写那么多

因为这块的代码实在是太复杂了

所以说我们在这儿先简单测试一下

就是什么呢

我这个类写好之后

一会我们来测试一下

看看它能不能正常触发

然后在如果保证它能够正常触发的情况下

我们再去写真正的智能调度相关的这些业务逻辑

然后我们为了方便测试

可以在这个地方输出一下

这个代码我就不再去手敲了

直接把这个代码复制过来

咱们来看一下这是什么东西

来复制一下

拿过来

这个Data先导一下

是U2Data就可以

咱们来看一下

我们是从这个context

这是不是我们这个上下文对象

然后get merge的job datamap

前面我们其实也讲过一个datamap

我们可以获得一个datamap

从datamap当中就可以来获取什么呢

我们当时这个定时任务所设置的一些参数

而这个merge的呢

merge是不是就是合并

因为我们当时在进行这个数据

我们在进行这个数据

也就是说在这个上下文当中来设置数据的时候

具体是怎么设置的呢

我们当时是怎么设置的

可以来看一下

应该是在这块问题思考

这块呢

我们当时提到什么呢

我们在这个提供了相应的方法来创建这个定时任务的时候

可以设置参数

对吧

通过这个上下文

你看咱们是不是通过这个什么job detail get job datamap

然后pull这些数据来设置这个参数呢

然后put对吧

也就是说我们这个job detail可以获得这个datamap

put进去

然后这个trigger呢

其实也可以获得什么呢

这个datamap

然后put进去

也就是说我们可以有多种地方都可以去设置这个

像这个datamap当中来设置相应的这个参数

对不对

而现在呢

我们这个get merge的job datamap指的就是什么呢

获取合并之后的

就是说我在多个地方可能都设置了

我在job detail上

还有这个trigger上都设置了

这个datamap

然后呢

这个我们获得的就是他们合并之后的

合并之后的这个参数

好

然后呢

得到这个datamap

然后再用get的方法

对吧

再用get的方法从这个map当中来获取一个值

获取的这个值呢

根据什么参数来取呢

咱们是定义成了一个常量

是在我们这个工具类

这个工具类呢

就是我们刚才导入的这个工具类

在咱们这个utils里面

你看是不是有个scheduler

utils

在这里边呢

有这么一个常量啊

有这么一个常量啊

所以它这个地方呢

引用的就是这个常量啊

对应的值呢

其实就是这个值

对吧

当然这一定要保证什么呢

一定要保证我们后边在这个

创建一个定时任务的时候呢

需要去进行相应的设置

对吧

你只有设置进去了

它是不是才能获取出来

就跟我们前面这个地方似的

你必须得先put进去

然后呢

put进来一个k1

然后你在get k1的时候

是不是才能获取到

好

这个呢

相当于是我们前后一定要一致

好

所以一会儿呢

我们在这个创建定时任务的时候呢

需要设置这个参数

然后这个地方呢

就可以取到了

取到之后呢

咱们在这呢

来输出一下

先输出一下日期

然后呢

说定时任务开始执行

然后定时任务的ID是什么呢

咱们是不是从这来get出来之后呢

其实是这么一个实体类

这个实体类呢

也是我们刚才导入的

对吧

那么它所对应的

它所对应的呢

就是我们这个表

scheduler job

这就是我们定时任务那张表

对吧

然后呢

我们把它的ID

直接通过它

点get ID

就可以了

这是我们这个定时任务实体

然后通过它get ID

这样就取到了

所以我们当前这个类呢

只是一个半成品

对吧

只是一个半成品

一会儿呢

我们需要把这些定时任务

把它一个一个初始化出来

然后我们来测试一下

看看能不能正常执行

能不能正常取到

对吧

通过观察控制台这个输出

我们就能知道

它能不能正常执行了

如果我们经过

测试啊

发现这个定时任务

都没有办

都没有问题

对吧

都可以正常触发

然后我们再来回过头来

完善这个方法

在这里边呢

来编写什么呢

真正的智能调度

相关的这些业务逻辑

好

所以这是咱们先把

所需要的

非常重要的

这个定时任务

这个类

把它传进出来

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”中“智能调度服务”模块的开发教程，核心内容是使用 Quartz 定时任务框架来实现动态定时任务。视频首先回顾了 Quartz 的基础概念和入门案例，然后重点讲解了如何编写一个可复用的定时任务类 `ScheduleJob`，并演示了如何通过 `ScheduleUtils` 工具类将任务参数（如任务ID）传递给任务执行器。整个过程结合了 PPT 讲解和 IntelliJ IDEA 中的代码编写与调试演示，旨在帮助开发者掌握在实际项目中配置和运行动态定时任务的方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示 PPT 页面，标题为“3.3.2 编写定时任务”，并说明本节将编写一个定时任务类 `ScheduleJob`。
*   **00:05 - 00:15**: 展示 PPT 页面，内容为“3.3.1 基础环境”，讲解需要导入的项目资源，如配置文件、Entity、DTO、Mapper 等。
*   **00:15 - 00:25**: 展示 IntelliJ IDEA 项目结构，定位到 `pd-dispatch` 模块。
*   **00:25 - 00:35**: 在 IDEA 中创建新文件 `ScheduleJob.java`，并开始编写代码。
*   **00:35 - 00:45**: 编写 `ScheduleJob` 类的包声明和继承 `QuartzJobBean`。
*   **00:45 - 00:55**: 在 `executeInternal` 方法中，通过 `context.get(MergedJobDataMap)` 获取 `ScheduleJobEntity` 实例，并调用 `ScheduleUtils.JOB_PARAM_KEY` 获取参数。
*   **00:55 - 01:05**: 展示 `ScheduleUtils` 工具类的代码，用于获取触发器键和任务键。
*   **01:05 - 01:15**: 回顾 PPT 中的“1.3.2 问题思考”部分，讨论如何在 Quartz 中传递参数。
*   **01:15 - 01:25**: 展示 `HelloJobMain` 的代码，演示如何使用 `JobBuilder` 和 `TriggerBuilder` 创建定时任务。
*   **01:25 - 01:35**: 展示控制台输出，验证任务执行情况。
*   **01:35 - 01:45**: 回到 `ScheduleJob` 的代码，强调 `get(ScheduleUtils.JOB_PARAM_KEY)` 的作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “3.3.2 编写定时任务”、“3.3.1 基础环境”、“1.3.2 问题思考”。
    *   **问题思考**: 针对 Quartz 任务，提出了三个问题：1) 任务是单例还是每次执行都创建新实例？2) 如何传递参数？3) 是否可以使用 cron 表达式？
    *   **解答**: 针对第一个问题，建议为 `HelloJob` 类添加无参构造方法。
    *   **代码示例**: 在“问题思考”部分，展示了 `HelloJob` 的无参构造方法 `public HelloJob() { System.out.println("创建HelloJob实例"); }`。

*   **代码关键内容**:
    *   **`ScheduleJob.java`**:
        ```java
        package com.itheima.pinda.execute;
        import org.springframework.scheduling.quartz.QuartzJobBean;
        public class ScheduleJob extends QuartzJobBean {
            @Override
            protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
                ScheduleJobEntity scheduleJob = (ScheduleJobEntity) context.get(MergedJobDataMap()).get(ScheduleUtils.JOB_PARAM_KEY);
                System.out.println(new Date() + "定时任务开始执行....定时任务id：" + scheduleJob.getId());
            }
        }
        ```
    *   **`ScheduleUtils.java`**:
        ```java
        public class ScheduleUtils {
            private final static String JOB_NAME = "TASK";
            public static final String JOB_PARAM_KEY = "JOB_PARAM_KEY";
            public static TriggerKey getTriggerKey(String jobId) { return TriggerKey.triggerKey(JOB_NAME + jobId); }
            public static JobKey getJobKey(String jobId) { return JobKey.jobKey(JOB_NAME + jobId); }
        }
        ```
    *   **`HelloJobMain.java`**:
        ```java
        public class HelloJobMain {
            public static void main(String[] args) {
                try {
                    //1:创建调度器
                    Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
                    //2:创建任务实例
                    JobDetail jobDetail = JobBuilder.newJob(HelloJob.class)
                            .withIdentity("jobDetail_1")
                            .build();
                    //设置参数
                    jobDetail.getJobDataMap().put("key1", "value1");
                    jobDetail.getJobDataMap().put("key2", "value2");
                    //3:创建触发器
                    Trigger trigger = TriggerBuilder.newTrigger()
                            .withIdentity("Trigger_1")
                            .withSchedule(SimpleScheduleBuilder.simpleSchedule().withIntervalInSeconds(5).repeatForever())
                            .build();
                    //4:触发器和任务关联
                    scheduler.scheduleJob(jobDetail, trigger);
                    //5:启动任务调度器
                    scheduler.start();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建定时任务类**
    *   **描述**: 讲师在 IntelliJ IDEA 中创建了一个名为 `ScheduleJob.java` 的新文件。他首先定义了包名 `com.itheima.pinda.execute`，然后声明了类 `ScheduleJob` 并使其继承自 `QuartzJobBean`。这表明该类是一个标准的 Quartz 任务。
*   **场景二：编写任务执行方法**
    *   **描述**: 讲师在 `executeInternal` 方法中，通过 `context.get(MergedJobDataMap())` 获取一个合并后的数据映射。他将这个映射中的 `ScheduleUtils.JOB_PARAM_KEY` 对应的值强制转换为 `ScheduleJobEntity` 类型，并打印出任务的 ID 和执行时间。这演示了如何从外部传递参数并获取。
*   **场景三：演示参数传递**
    *   **描述**: 讲师在 `ScheduleUtils` 工具类中定义了 `JOB_PARAM_KEY` 常量，并在 `ScheduleJob` 中使用它。这表明任务的参数是通过 `JobDataMap` 传递的，`ScheduleUtils` 作为工具类，用于统一管理任务和触发器的键名。
*   **场景四：回顾 Quartz 入门案例**
    *   **描述**: 讲师切换到 PPT 页面，回顾了 Quartz 的入门案例 `HelloJobMain`。他展示了如何使用 `StdSchedulerFactory` 创建调度器，`JobBuilder` 创建任务，`TriggerBuilder` 创建触发器，并将它们关联起来。最后调用 `scheduler.start()` 启动调度器。
*   **场景五：控制台输出验证**
    *   **描述**: 讲师在控制台中展示了 `HelloJob` 的输出日志，显示了“创建HelloJob实例”和“HelloJob开始执行”的信息。这验证了任务的创建和执行流程，为后续的动态任务开发提供了基础。
