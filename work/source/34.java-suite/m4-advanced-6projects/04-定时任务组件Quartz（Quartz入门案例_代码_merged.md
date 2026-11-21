# 04-定时任务组件Quartz（Quartz入门案例_代码 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么前面呢 我们是讲解了一下cause它的核心API

那接下来呢 我们来看下一个小节 就是cause的入门案例

咱们通过这个入门案例呢 来学习一下cause它的基本的使用方法

那么我们可以创建一个新的Mainware工程

在这个工程里面我们来讲解一下

咱们在这来create new project

然后直接点next 在这来指定一下cam it黑码

指定一下坐标

然后呢 这个就叫cause test吧

好 接next

好 然后呢 创建好这个工程之后呢

我们第一步呢 先来导入什么呢

它的这个Mainware坐标 直接复制一下

这个坐标我们前面也都提到过了 对吧

那么要使用它的话呢 只需要导入这两个坐标就可以

好 dependency 直接放在这个地方

这是第一步 是吧 好 让它自动导入一下

然后第二步呢 我们需要做什么事呢

第二步的话呢 咱们来看一下我们刚才看到的

这个Mainware工程

这个核心API 对吧

那么需要来创建一个自定义的job

而且呢 这个job的话呢 需要去实现这么一个接口

就是我们这个cause框架所提供的一个job接口

好 那么具体当任务出发的时候执行什么方法呢

执行的方法是不是就需要写在这个自定义的job当中

所以说呢 我们接下来呢 需要来创建这么一个自定义的job

咱们先把这个包呢 给它来创建一下

这是cam it黑码 然后呢 叫做job4吧

所有的自定义的job呢 全都写在这里面

好 那么我们第一个呢 就来叫做hello job 简单一点

然后呢 让它去实现什么呢 咱们这个job接口 注意看

就是这个ord.cause 这个包下边给我们提供了这么一个接口

而在这个接口里边呢 声明了一个方法

就是这个execute 是吧 执行 这么一个方法

好 实现它 先来在这加一个注释啊

这是我们自定义job

然后呢 这个job呢 这个job呢 这个job呢

这个方法叫做执行 而这个方法呢 是什么时候去执行啊

就是当我们这个任务触发时 是不是执行此方法

然后呢 这个方法里边 大家可以看到它传进来了这么一个对象 对吧

job execution context

这个对象呢 其实就是我们这个任务的这个上下文 对吧

任务执行的上下文对象

那么通过这个对象呢 可以获得我们任务执行的相关的信息

比如说什么job detail啊

什么trigger了 在这个通过这个上下文对象都可以获得到

好 这是我们任务执行它的上下文对象

当然我们第一个入门案例呢 咱们简单一点啊

我们先不来不去获得这么多信息 我们就在这来

输出一下 就是能够知道我们当前这个任务啊 它是什么时候执行的

啊 这就是我们自定义job执行 那么执行时间

时间 咱们可以在这儿来说

输出一下 直接在这你有一个data就可以啊 你有一个data

OK 那么这是我们自定义的这个照吧 这个呢 还是非常简单的

然后接下来呢 我们需要来创建一个什么呢 创建一个

另外创建一个类 然后写个main方法 在main方法里边呢 我们就会来调用咱们这个

核心的这些API 对吧 最终呢 把这个任务给它跑起来

那么它是怎么跑呢 它其实就是通过我们这个任务的调度器啊 通过它来进行统一的任务调度

好

那我们需要来创建这么一个类 咱们就在itk码这一层来创建一个啊 就是我们的统一的任务调度 咱们就叫hello

照吧 妹啊 在这里边呢 来进行什么呢 进行我们这个任务统一

调度啊

写个卖方法 通过没方法这种方式啊

然后呢 我们第一步需要来创建一个什么对象呢 就是创建这么一个死该对了 哎 刚才看到了就是任务调度器 对吧 那么它可以统一进行任务的

调度 而这个对象呢 注意它不是溜出来的 它是通过这么一个工厂对吧 叫做std是该对了

factory这个任务调度工厂 然后呢 可以来创建什么呢 创建我们这个死该对了对象

所以我们第一步啊 先来加一个注释啊 通过什么呢 通过调度器

工厂来创建什么呢 我们这个任务调度器

调度器对象好

然后呢 这个工厂呢 就是这个std什么

死该对了factory对吧 这是一个工厂 然后这个工厂里边呢 有一个方法叫做什么呢 get default

啊 死该对了 就是获得一个默认的啊 这么一个调度器工厂啊 这么一个调度器对象啊

但是他这呢 你看他会抛异常对吧 咱们这呢 就简单一点 直接抛出一下这个异常信息啊 就可以了

这样的话呢 我们第一步就是这个调度器对象是不是就已经创建好了 对吧 来创建任务调度器

创建好它之后呢 接下来我们需要来创建什么呢 需要来创建这么一个啊 就是我们这个

从这能看到叫做job detail

任务对象对吧 而这个任务对象呢 他就会描述什么呢 任务执行的时候具体是执行的是哪一个

我们这个自定义的照吧 是吧 也就是需要去关联这个照吧

而这个job detail这个对象呢 他也不是nil出来的 他是通过什么呢 他是通过我们一个叫做job builder

哎 这么一个任务构成的项目

构建器对象 然后呢 来创建他啊 所以接下来呢 我们在这先来写一下 通过我们这个任务构建器

任务构建器对象来创建什么呢 我们这个任务实力啊 就是这个照吧 第一条啊

叫做照吧 标点照吧 标的刚才看到的就是这个构建器 对吧 下边这个照吧 标的

然后呢 他这里边呢 有一个静态方法叫做什么呢 就叫做new job

然后在这呢 来指定我们自定义的那个任务 对吧 咱们刚才写的是不是就是这个hello job

所以在这呢 来指定他hello job.class

这就是关联上我们自定义任务了 所以出发的时候呢 他就会触发我们这个任务里边的这个execute的方法

然后呢 我们这个任务呢 往往是有一个唯一id的 通过这个叫做with identity identity其实就是标识 对吧

唯一标识

那么我们在这来指定一下

比如说叫做myjobdetail

这个叫什么名字都可以啊 然后呢 调用build的方法 这样呢 就构建出来了这么一个jobdetail对象

好

然后有了他之后呢 下一步我们需要来创建谁呢

还是看咱们这个图 有了job之后呢 下一步是不是需要来创建我们这个触发器对象 对吧 创建触发器对象

而这个触发器呢 就是一个trigger

他是怎么创建的呢 同样 他是通过这个触发器的构建器

来创建啊

所以下一步呢 就是通过

通过我们这个触发器 构建器

来创建什么呢 我们的触发器

对象好

咱们来看一下 就是这个叫做triggerbuilder 对吧

叫做triggerbuilder.new一个trigger

new一个trigger 然后呢 指定他的唯一标识也是with identity 对吧

那比如说我这个就叫mytrigger.new一个trigger

只要是唯一的就可以

然后呢 触发器他主要起的作用是什么呢 是不是就是指定我们这个任务他触发的时间 对吧 任务触发的时间

所以说呢 我们在这个地方呢 就需要来指定啊 叫做with scheduler

在这呢 来指定我们这个任务 他什么时候触发

啊 然后呢 你可以看到他这里边要求传的是一个什么呢 是这么一个对象 叫做schedule builder 对吧 而这个builder对象呢 我们可以通过这个啊 叫做

simple

simple啊 通过他呢点simple scheduler 这样呢 就创建出来了这么一个

啊 搜到了标的对象 然后呢 这里边呢 有一个方法叫做为子internet

啊 interval in seconds 这是啥意思呢 这个指的就是每隔几秒触发一次

然后这个是in hours 这就是每个几小时触发一次 然后这个是命令赛克次 这是不是就是每隔几毫秒触发一次

然后这个就是每隔几分钟

好 咱们在这呢 为了方便测试啊 我们在这呢 就使用这个s seconds

然后我这写个三 那代表的就是什么呢 每隔三秒触发一次

好 那他每隔三秒触发一次 那什么时候这个任务结束了 哎 在这呢 我指定一下什么呢 叫做repeat forever

这是不是就是永远重复 对吧 哎 repeat forever 那也就是说 我们如果不手动去停止这个进程 那么我们当前这个任务呢就一直调度啊

没有停止的时候

ok 这就是指定啊 然后呢 别忘了 我们现在是创建触发器对象 所以调用这个build的方法

这样呢 我就来创建出来了一个叫做trigger 对吧 trigger触发器对象

好 是通过我们这个trigger builder来new一个trigger 然后呢 指定它的唯一标识 然后呢 再指定什么呢 这个任务触发的频率 对吧 with schedule触发的频率

好 只不过这个方法呢 套的比较深啊 套的比较深啊 然后这部触发器创建好之后呢 还没完 我们选择这个触发器

需要干什么呢 是不是需要使用我们这个schedule 将我们的这个job啊 就是job detail对象 还有这个trigger对吧 触发器对象进行关联

好 所以说呢 我们需要来关联啊 下一步

关联什么呢 我们这个任务实力和这个什么呢 触发器对吧好对象

怎么关联呢 就是使用这个schedule 前面第一步创建出来的 对吧 调用它的一个叫做schedule job方法 你看这个方法呢 是不是就接受两个参数 第一个呢 就是job detail

第二个就是trigger job detail 我们也创建了

job detail创建了 然后还有一个是trigger 也创建

这个就关联了 关联上之后呢 咱们就需要来调用我们这个schedule它的一个start方法 这就表示什么呢 启动我们这个任务调度器

就是开始进行任务调度 对吧 启动任务调度器

然后呢 开始任务调度

好 那么我们直接调用schedule它的一个什么start方法 这就开始了

ok 那么你看我们这块写的这个代码呢 整体来说其实比较繁琐 对吧 那么使用的呢 全都是

这个

提供的就是我们这个cause所提供的这些核心API 但是下面还有这几个还没有使用到 一会呢 我们会使用到他们

所以说呢 它这个整个这个过程呢 其实也属于一些模板化的代码

创建这个调度器对象什么条件

创建job detail对吧 还有出发器 然后关联 最后启动都是一些这种模板化的代码

好 那么一会呢 我们再来测试一下 看看我们这个入门案例呢 能不能正常执行

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频是关于 Java 定时任务框架 Quartz 的入门教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个简单的 Quartz 任务调度程序。主要内容包括：创建 Maven 项目、导入 Quartz 核心依赖、理解 Quartz 的核心 API（Scheduler, Job, Trigger），以及编写代码实现一个任务的创建、触发和启动。视频通过代码演示和架构图，清晰地展示了 Quartz 的工作原理和基本使用方法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **00:00 - 00:05**：开场，展示 IntelliJ IDEA 的欢迎界面，讲师准备创建新项目。
*   **00:05 - 00:15**：创建名为 `quartztest` 的 Maven 项目，并展示 `pom.xml` 文件，其中已配置了 Quartz 的依赖。
*   **00:15 - 00:30**：讲解 Quartz 的核心架构图，介绍 `Scheduler`、`Job` 和 `Trigger` 三个核心组件及其关系。
*   **00:30 - 00:45**：详细讲解核心 API，包括 `StdSchedulerFactory`、`JobBuilder`、`TriggerBuilder` 等类的作用。
*   **00:45 - 01:10**：在 `HelloJobMain.java` 文件中编写代码，首先通过 `StdSchedulerFactory.getDefaultScheduler()` 创建 `Scheduler` 对象。
*   **01:10 - 01:25**：使用 `JobBuilder` 构建 `JobDetail` 对象，指定任务类为 `HelloJob`。
*   **01:25 - 01:40**：使用 `TriggerBuilder` 构建 `SimpleTrigger` 对象，设置触发器名称为 `mytrigger`，并配置触发间隔为 3 秒。
*   **01:40 - 01:55**：调用 `scheduler.scheduleJob(jobDetail, trigger)` 方法将任务和触发器关联。
*   **01:55 - 02:05**：调用 `scheduler.start()` 方法启动调度器，完成整个任务的创建和启动。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   **核心架构图**：展示了 `Scheduler`、`Job` 和 `Trigger` 三者之间的关系。`Scheduler` 负责管理 `Job` 和 `Trigger`。
    *   **API 说明图**：以列表形式详细说明了 Quartz 的核心类及其功能，包括 `Scheduler`、`StdSchedulerFactory`、`JobDetail`、`JobBuilder`、`Trigger`、`TriggerBuilder`、`JobExecutionContext`、`JobDataMap`、`RAMJobStore` 和 `JobStoreTX`。

*   **代码**：
    *   **Maven 依赖**：在 `pom.xml` 中配置了 Quartz 的核心依赖。
    *   **HelloJobMain.java**：
        ```java
        package com.itehima;
        import com.itehima.jobs.HelloJob;
        import org.quartz.JobBuilder;
        import org.quartz.Scheduler;
        import org.quartz.impl.StdSchedulerFactory;

        public class HelloJobMain {
            public static void main(String[] args) throws Exception {
                // 通过调度器工厂创建任务调度器对象
                Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
                // 通过任务构建器对象创建任务实例
                JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity("myjobdetail").build();
                // 通过触发器构建器对象创建触发器对象
                SimpleTrigger trigger = TriggerBuilder.newTrigger().withIdentity("mytrigger").withSchedule(SimpleScheduleBuilder.simpleSchedule().withIntervalInSeconds(3).repeatForever()).build();
                // 关联任务实例和触发器对象
                scheduler.scheduleJob(jobDetail, trigger);
                // 启动任务调度器，开始任务调度
                scheduler.start();
            }
        }
        ```
    *   **HelloJob.java**：一个简单的任务类，用于执行具体的业务逻辑。

---

### 4) 关键场景与演示描述

*   **场景一：项目创建与依赖配置**：
    讲师在 IntelliJ IDEA 中创建了一个名为 `quartztest` 的 Maven 项目，并在 `pom.xml` 中添加了 Quartz 的依赖。这为后续的开发奠定了基础。

*   **场景二：核心架构讲解**：
    讲师通过一张架构图，清晰地解释了 Quartz 的核心组件：`Scheduler`（调度器）、`Job`（任务）和 `Trigger`（触发器）。他强调了 `Scheduler` 的作用是将 `Job` 和 `Trigger` 关联起来，统一进行任务调度。

*   **场景三：代码编写与调试**：
    讲师在 `HelloJobMain.java` 中逐步编写代码：
    1.  首先，通过 `StdSchedulerFactory.getDefaultScheduler()` 创建 `Scheduler` 对象。
    2.  然后，使用 `JobBuilder` 构建 `JobDetail` 对象，指定任务类为 `HelloJob`。
    3.  接着，使用 `TriggerBuilder` 构建 `SimpleTrigger` 对象，设置触发器名称和触发间隔。
    4.  最后，调用 `scheduler.scheduleJob(jobDetail, trigger)` 将任务和触发器关联，并调用 `scheduler.start()` 启动调度器。

*   **场景四：API 详解**：
    讲师在代码中通过鼠标悬停或使用 IDE 的自动补全功能，展示了 `JobBuilder`、`TriggerBuilder` 和 `Scheduler` 等类的常用方法，帮助观众理解如何使用这些 API。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解这段技术课程的内容。
