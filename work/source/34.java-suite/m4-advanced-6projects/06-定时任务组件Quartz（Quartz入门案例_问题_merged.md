# 06-定时任务组件Quartz（Quartz入门案例_问题 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 前面咱们这个入门案例代码已经写完了

并且我们在这也测试了一下

你看现在这个程序它还没有结束

所以你可以看到它每隔三秒就会触发一次

你看 如果说我们不点击这个红点

强制结束它的话

它就会一直这样调度下去

你看

好 这个我们直接给它强制结束这个进程就可以了

好 这样就停止了

对吧

那接下来我们来看下一个小节了

就是什么呢

我们这个问题思考

这个问题思考呢

就是针对咱们这个入门案例呢

有这么三个问题

那么随着我们通过这三个问题呢

再来深入的研究一下咱们这个cause

首先第一个问题是什么呢

就是我们自定义的这个招吧

Hello招吧

对吧

这是咱们自定义的这个类啊

那么它是什么呢

是不是它是单立存在的

还是说我们每一次任务触发的时候呢

都会创建

一个新的实例

这是第一个问题

对吧

这是第一个问题

那么它是单立的

还是说是多立的

也就是每次执行的时候都创建一个新的实例呢

这是第一个问题

然后第二个问题就是什么呢

我们如何给这个定时任务来传递参数

并且在执行任务的时候呢

来获得相应的参数

这个呢其实是比较有价值的

就是说我们通过某种方式啊

能不能给它传递参数进去

好

那么这些参数呢

往往是跟我们的业务相关的一些参数

好

这是第二个问题

然后第三个问题就是什么呢

咱们这个入门案例当中啊

设置的是每隔几秒执行一次

对吧

当然我们设置的是每隔三秒执行一次

好

讲义上写的是五秒

这个都无所谓啊

那么是否可以使用更加复杂的

比如说我们这个con表达式这种方式

来设置触发的时间呢

那么我们接下来呢

就带着这三个问题呢来看一下

首先呢来看第一个问题

第一个问题就是什么呢

它到底是个单立的

还是每一次任务执行的时候

都创建一个新的实例呢

这个呢其实比较好解答

就是什么呢

我们是不是可以给它添加一个

无参的构造方法对吧

然后呢在构造方法里面来一个输出语句

然后呢我们来观察控制台输出

如果说控制台呢

只能看到这么一次创建对吧

那就说明它肯定是单立的

如果说每一次任务执行的时候

都能看到这句输出

那是不是说明

每一次任务执行的时候

它都创建了一个新的实例对吧

所以说呢我们这个呢

是比较好验证的啊

这是第一个

咱们给这个HelloJob呢

给它来加一个什么呢

无参的构造方法

无参的构造方法

因为要创建它的时候呢

是不是就会调用这个无参构造方法

这样的话我们在这儿

加一个输出语句

就能看到它是什么时候创建的

它创建了多少次对吧

那么这个就是我们这个HelloJob

被创建了

然后呢我们再来执行

咱们这个程序

来看一下

我们的这个

它这个构造方法里面

这个输出语句啊

是输出一次还是输出多次

这样的话呢

我们第一个问题呢

就能解答了

你看HelloJob被创建了

这第一次对吧

然后呢你看

它是不是又被创建了

然后创建完之后

是不是紧接着执行

所以说呢

通过控制台这个输出呢

我们应该就能知道了

它其实就是什么

每一次任务出发的时候呢

都会创建一个新的HelloJob

这个实例对吧

这是自定义Job

是多次被创建

好

这是我们第一个问题思考

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于 Java 定时任务框架 Quartz 的入门教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个简单的定时任务。核心内容包括：
- **环境搭建**：展示了一个名为 `quartztest` 的项目结构，包含 `HelloJob`（任务类）和 `HelloJobMain`（调度器主类）。
- **任务实现**：定义了一个 `HelloJob` 类，它实现了 Quartz 的 `Job` 接口，并在 `execute` 方法中打印当前时间。
- **调度配置**：在 `HelloJobMain` 类中，使用 `StdSchedulerFactory` 创建调度器，通过 `JobBuilder` 和 `TriggerBuilder` 定义任务和触发器，最后启动调度器。
- **运行演示**：运行程序后，控制台输出显示任务按设定的时间间隔（每5秒）成功执行，验证了 Quartz 的基本功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **章节 0:00 - 0:05**: 课程开场，展示项目结构和 `HelloJobMain` 类的代码，强调“任务统一调度”的主题。
- **章节 0:06 - 0:15**: 展示 `HelloJob` 类的代码，讲解其 `execute` 方法的作用，即在任务触发时打印执行时间。
- **章节 0:16 - 0:25**: 展示 `HelloJobMain` 类的代码，讲解如何通过 `StdSchedulerFactory` 创建调度器，以及如何使用 `JobBuilder` 和 `TriggerBuilder` 构建任务和触发器。
- **章节 0:26 - 0:35**: 运行程序，演示控制台输出，验证任务每5秒执行一次。
- **章节 0:36 - 0:45**: 讲解并演示如何为 `HelloJob` 添加无参构造方法，以解决潜在的实例化问题。
- **章节 0:46 - 0:55**: 展示运行结果，强调任务执行的规律性，并指出这是 Quartz 的基本用法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**: `第5章 智能调度服务 (pd-dispatch)`
- **子章节**: `1.3.2 问题思考`
- **问题列表**:
  1. 自定义任务 `HelloJob` 是单例的还是每次执行定时任务都创建新实例？
  2. 如何给定时任务传递参数，并且在执行任务时可以获取到相应参数？
  3. 入口案例中触发器设置的是每隔5秒执行一次，是否可以使用 cron 表达式设置触发时间？
- **解答**:
  - 针对第一个问题，建议为 `HelloJob` 添加无参构造方法。

#### 代码关键内容

- **`HelloJob.java`** (任务类)
  ```java
  import org.quartz.JobExecutionException;
  import java.util.Date;

  /**
   * 自定义Job
   */
  public class HelloJob implements Job {

      /**
       * 当任务触发时执行此方法
       * @param jobExecutionContext 任务执行的上下文对象
       * @throws JobExecutionException
       */
      public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {
          System.out.println("自定义Job执行，执行时间为：" + new Date());
      }
  }
  ```

- **`HelloJobMain.java`** (调度器主类)
  ```java
  import org.quartz.Scheduler;
  import org.quartz.SchedulerException;
  import org.quartz.SchedulerFactory;
  import org.quartz.impl.StdSchedulerFactory;
  import org.quartz.JobBuilder;
  import org.quartz.JobDetail;
  import org.quartz.Trigger;
  import org.quartz.TriggerBuilder;
  import org.quartz.SimpleTrigger;

  public class HelloJobMain {
      public static void main(String[] args) throws Exception {
          // 通过调度工厂创建任务调度对象
          Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
          // 通过任务构建器对象创建任务对象
          JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity("myjobdetail").build();
          // 通过触发器构建器创建触发器对象
          SimpleTrigger trigger = TriggerBuilder.newTrigger().withIdentity("mytrigger").withSchedule(
                  SimpleScheduleBuilder.simpleSchedule().withIntervalInSeconds(5).repeatForever()).build();
          // 关联任务调度器和触发器对象
          scheduler.scheduleJob(jobDetail, trigger);
          // 启动任务调度器，开始任务调度
          scheduler.start();
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景 1: 项目结构展示 (0:00-0:05)**
  - 讲师在 IntelliJ IDEA 中打开 `quartztest` 项目，展示 `src/main/java/com/itheima/jobs` 目录下的 `HelloJob.java` 和 `HelloJobMain.java` 文件。
  - 强调 `HelloJobMain` 是调度器的入口类，负责启动和管理任务。

- **场景 2: 任务类代码演示 (0:06-0:15)**
  - 讲师聚焦于 `HelloJob.java`，解释 `execute` 方法是任务的核心逻辑，它接收 `JobExecutionContext` 参数并打印当前时间。
  - 通过高亮和滚动，展示代码的执行流程。

- **场景 3: 调度器配置演示 (0:16-0:25)**
  - 讲师在 `HelloJobMain.java` 中展示如何创建 `Scheduler` 对象。
  - 详细讲解 `JobBuilder` 和 `TriggerBuilder` 的使用，特别是 `SimpleTrigger` 的 `withIntervalInSeconds(5)` 方法，用于设置任务每5秒执行一次。
  - 展示 `scheduler.scheduleJob(jobDetail, trigger);` 和 `scheduler.start();` 语句，说明任务的注册和启动。

- **场景 4: 运行与结果演示 (0:26-0:35)**
  - 讲师点击运行按钮，控制台输出开始滚动。
  - 展示控制台输出，每5秒打印一次“自定义Job执行，执行时间为：Mon Sep 14 10:15:XX CST 2020”，证明任务按预期执行。
  - 讲师强调这是 Quartz 的基本用法，任务执行时间精确到秒。

- **场景 5: 问题思考与解答 (0:36-0:45)**
  - 讲师切换到 PPT，展示“1.3.2 问题思考”部分，提出关于任务实例化的问题。
  - 讲师回到代码，演示如何为 `HelloJob` 添加无参构造方法 `public HelloJob() {}`，以解决潜在的实例化问题。
  - 讲师强调，虽然当前代码可以运行，但添加构造方法是更规范的做法。

- **场景 6: 最终验证 (0:46-0:55)**
  - 讲师再次运行程序，控制台输出继续滚动，确认任务持续稳定执行。
  - 讲师总结，通过本节学习，学员掌握了 Quartz 的基本使用方法，包括任务定义、调度配置和运行验证。
