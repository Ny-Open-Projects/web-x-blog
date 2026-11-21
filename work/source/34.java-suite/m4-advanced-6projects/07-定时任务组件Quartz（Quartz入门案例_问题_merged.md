# 07-定时任务组件Quartz（Quartz入门案例_问题 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 接下来呢

咱们继续来看我们问题思考这个小节

刚才呢我们是回答了第一个问题

就是什么呢

当我们这个任务执行的时候呢

它每一次是不是执行定时任务

都会创建一个新的实例

也就是说它其实是一个多利的

这么一个存在

然后接下来呢

我们来看第二个问题啊

第二个问题就是什么呢

如何给定这个任务

给这个定时任务呢

来传递参数对吧

这些参数呢

往往是跟我们这个业务相关的

并且呢在任务执行的时候呢

我们可以动态的

把这些参数给它获取到

这个是如何做到呢

这儿呢我们就会使用到

咱们前面核心API里边

但是我们提到

是不是有这么一个叫做

JobDataMap对吧

JobDataMap吧

那么它就是做这个事的啊

就是可以什么呢

这个任务实例啊

它的一个状态信息

就可以保存在这个Map当中

那么咱们来写一下

看看这个代码怎么写

咱们先把这个进程给它停掉啊

好 停掉了

然后接下来呢

我们先回到这个地方

好

也就是说我们在这个地方

是不是已经创建好了

咱们这个JobDetail对吧

JobDetail实例

然后呢通过这个JobDetail对象

我们就可以来get它一个什么呢

JobDataMap

是不是获得这个DataMap对象

你看这个方法

它的返回值就是一个JobDataMap

也就是我们这个地方看到的

这个JobDataMap

然后呢得到它之后呢

咱们就可以往这里边干什么呢

来put

你看put是不是key value

就是一个普通的这个Map对吧

然后呢

我们在这来指定

比如说我来指定一个key

然后呢这个值呢

我就叫value1

好

这是一个对吧

然后呢我们再来一个JobDetail.getDataMap对吧

JobDetail.put

我再来一个key2

然后呢这边是value2

这个根据我们实际情况来put就可以了

那么我们这儿呢就设置这么两个

这个呢其实就是什么呢

设置啊

或者叫做保存我们这个当前这个Job

它的一些这个状态信息

状态信息

那么一般呢一般是和我们这个业务业务相关的

业务相关的这个信息

好

然后呢我们这个就已经设置进去了对吧

这相当于我们已经完成了这个什么呢

保存这个任务实例一些状态信息

然后呢在它执行的时候

我是不是希望给它取出来啊

就把我放进去之后呢我再去做一些什么呢

我把我放进去的这些对这些key value对吧

给它取出来

那这就是说需要在我们这个execute的方法上来取一下

那么怎么取出来呢

咱们来看一下

这儿呢就需要使用到我们这个什么呢

上下文对象了

上下文对象

前面呢我们也提到了这个上下文对象呢

它是任务执行的上下文对象

通过这个对象呢

可以获得当前执行任务相关的信息

比如说什么呢

JobDetail

还有什么trigger

这些都可以获得到

好

那现在呢我们就可以使用这个

什么job execution context.get什么呢

JobDetail

你看

get job detail

这样呢是不是就获得了我们这个任务实例对象

对吧

任务实例对象

然后呢

从这里边我们来get job datamap

这样呢

你看我是不是就拿到了我们这个job datamap

而这儿获得的这个job datamap呢

其实就是从这个地方跟这儿get出来的是同一个对象

还是同一个对象啊

所以说呢

我们这儿呢

得到它之后呢

我们就可以干什么呢

通过这个job datamap.entryset

调用这个方法

别再put了

put是不是又往里面放值

现在我们是取值对不对

那么它是一个一个的建制对

所以我们直接调用这个entry set

就得到了这么一个set集合

而这个set集合里面装的呢

就是一个一个的entry

而每一个entry呢

其实就是一个key value对不对

就是一个一个的建制对

所以呢

我们可以把这个entries呢

给它来循环一下啊

entries.forEach对吧

forEach

然后呢

这里边呢

我们来一个entry

entry

entry怎么写来着

tr这样

然后呢

写这么一个表达式对吧

这是一个这个啊

然后在这里边呢

我们是不是就可以通过这个什么呢

entry来获得什么呢

注意这一个entry呢

它既包括了key也包括了value对吧

它其实就是一个建制对

所以我们在这儿呢就可以通过entry来获得这个scripts

然后呢

还可以通过entry点什么呢

get value

这是获得我们的value

然后我们在这儿呢

是不是来输出一下就可以了

key

然后呢

加上一个等号

然后呢

再加上这个value

这样呢

就是动态的把我们这个key value给它取出来

这就是我们通过辨认的这个scripts

我们可以用这个辨认的这个scripts

来办理这种方式

把这里面存的所有的值对吧

我们放的所有的值都给它取出来

这个地方呢

它报错

这是因为什么呢

你看啊

其实是这个jtk的一个问题啊

我们在这儿呢

给它来调整一下

设置一下这个to level 8

好

反应有点慢

然后接下来呢

我们来执行一下

就来看一下什么呢

我们在这个地方呢

是不是通过这个job detail get map

然后put进来的这个值

在任务来执行的时候呢

能不能给它取出来

好

这个呢其实就是获取什么呢

获取我们这个

这个存放的存放的这个存放的任务

状态

状态信息

好

然后呢我们再来执行一下

看一注意看啊

现在我们控制台输出呢

就会多一些东西了

出来就是这条输出语句

key value这条

哎你注意看

第一次

它是不是执行了

然后key等于

key1等于value1

key2等于value2

但是后边的话呢

咱们因为放的都是这个对象啊

所以说呢

它取出来的都是一样的

哎那么从这也能看到啊

那么每一次任务执行的时候呢

它都可以从我们这个什么job detail

对吧

调用它的一个get什么job detail map

啊

而这个map呢

就是用来存放我们这些任务的状态信息的

好

所以说呢

我们第二个问题呢

是不是也解决了

就是通过这一段啊

就是诶

我看我们的这个jaw歌

诶

有没有诶

我好像也没有诶

我去诶

我去诶

对

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

诶

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于 **Quartz 定时任务框架** 的入门教程，主要讲解如何通过代码动态创建任务（Job）和触发器（Trigger），并传递参数。课程通过一个名为 `HelloJob` 的自定义任务类和 `HelloJobMain` 的主程序进行演示。核心内容包括：
- **任务与触发器的概念**：通过 `Job` 和 `Trigger` 两个核心组件实现任务调度。
- **动态创建任务**：使用 `JobBuilder` 构建 `JobDetail` 对象。
- **传递参数**：通过 `JobDataMap` 在任务执行时传递和获取参数。
- **任务执行上下文**：在 `execute` 方法中通过 `JobExecutionContext` 获取任务信息和参数。
- **代码演示**：在 IntelliJ IDEA 中逐步编写、调试并运行代码，展示控制台输出结果。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取时间戳，以下章节按画面内容和逻辑顺序排列：

- **00:00 - 00:15**：课程介绍与问题思考。屏幕显示 PPT 页面，提出三个核心问题：自定义任务是否每次执行都创建新实例？如何传递参数？是否能用 cron 表达式设置触发时间？
- **00:15 - 00:30**：解答第一个问题。演示如何在 `HelloJob` 类中添加无参构造方法，以确保每次任务执行时创建新实例。
- **00:30 - 00:45**：演示任务调度主程序。展示 `HelloJobMain` 类的代码，包括创建调度器、构建任务和触发器、并启动调度。
- **00:45 - 01:00**：讲解 `JobDataMap`。在 `HelloJobMain` 中向 `JobDetail` 的 `JobDataMap` 中添加键值对 `key1=value1` 和 `key2=value2`。
- **01:00 - 01:15**：在 `HelloJob` 的 `execute` 方法中，通过 `JobExecutionContext` 获取 `JobDetail`，并从中取出 `JobDataMap`。
- **01:15 - 01:30**：遍历 `JobDataMap`。使用 `entrySet().forEach()` 方法遍历键值对，并打印输出。
- **01:30 - 01:45**：代码优化与完善。将 `forEach` 中的逻辑改为使用 `entry.getKey()` 和 `entry.getValue()` 显式获取键值，并打印。
- **01:45 - 02:00**：最终代码与输出。展示最终的 `execute` 方法代码，并在控制台查看输出结果，确认参数传递成功。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

- **核心概念图**：
  - 一个简单的流程图，显示 `Job` 和 `Trigger` 通过 `Scheduler` 进行关联。
  - 文字说明：
    - `Scheduler`：任务调度器，使任务和触发器关联，统一进行任务的调度。
    - `StdSchedulerFactory`：任务调度器工厂，可以创建 `Scheduler` 对象。
    - `JobDataMap`：保存任务实例的状态信息。
    - `RAMJobStore`：此类实现了一个利用 RAM 作为其存储设备的 `JobStore`，访问速度极快，但是数据却易失。
    - `JobStoreTX`：通过 JDBC 将所有数据保存在数据库中。

#### 代码

- **`HelloJobMain.java` 主程序**：
  ```java
  import com.itheima.jobs.HelloJob;
  import org.quartz.*;
  import org.quartz.impl.StdSchedulerFactory;

  public class HelloJobMain {
      public static void main(String[] args) throws Exception {
          // 通过调度器工厂创建任务调度器对象
          Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
          // 通过任务构建器对象创建任务实例
          JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity("myjobdetail").build();
          // 通过触发器构建器创建触发器对象
          SimpleTrigger trigger = TriggerBuilder.newTrigger().withIdentity("mytrigger").withSchedule(SimpleScheduleBuilder.simpleSchedule().withIntervalInSeconds(5).repeatForever()).build();
          // 关联任务实例和触发器对象
          scheduler.scheduleJob(jobDetail, trigger);
          // 启动任务调度器，开始任务调度
          scheduler.start();
      }
  }
  ```

- **`HelloJob.java` 任务类**：
  ```java
  import org.quartz.Job;
  import org.quartz.JobExecutionContext;
  import org.quartz.JobExecutionException;

  public class HelloJob implements Job {
      public HelloJob() {
          System.out.println("HelloJob被创建了...");
      }

      @Override
      public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {
          System.out.println("自定义Job执行，执行时间为：" + new Date());
          JobDataMap jobDataMap = jobExecutionContext.getJobDetail().getJobDataMap();
          Set<Map.Entry<String, Object>> entries = jobDataMap.entrySet();
          entries.forEach(entry -> {
              String key = entry.getKey();
              Object value = entry.getValue();
              System.out.println(key + "=" + value);
          });
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：任务实例创建与控制台输出**
  - **描述**：在 `HelloJob` 类中，演示了无参构造方法的作用。在 `HelloJobMain` 中运行程序后，控制台输出显示“创建HelloJob实例”，并记录了每次任务执行的时间戳，证明了每次触发都会创建新的任务实例。

- **场景二：使用 JobDataMap 传递参数**
  - **描述**：在 `HelloJobMain` 中，通过 `jobDetail.getJobDataMap().put("key1", "value1");` 和 `jobDetail.getJobDataMap().put("key2", "value2");` 向任务传递了两个参数。在 `HelloJob` 的 `execute` 方法中，通过 `JobExecutionContext.getJobDetail().getJobDataMap()` 获取并遍历这些参数，最终在控制台打印出 `key1=value1` 和 `key2=value2`。

- **场景三：代码调试与优化**
  - **描述**：在 `HelloJob` 的 `execute` 方法中，演示了如何使用 `entrySet().forEach()` 遍历 `JobDataMap`。随后，演示了如何将 `forEach` 中的逻辑改为使用 `entry.getKey()` 和 `entry.getValue()` 显式获取键值，使代码更清晰易懂。

- **场景四：最终效果验证**
  - **描述**：在控制台中，最终输出显示了任务执行的时间和传递的参数，验证了整个动态创建任务、传递参数和获取参数的流程成功执行。
