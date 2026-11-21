# 08-定时任务组件Quartz（Quartz入门案例_问题 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们这个问题思考,第三个问题就是什么呢?咱们现在这个入门案例中,出发器设置的是每隔三秒,每隔三秒是执行一次,那么是否可以使用这种call-on表达式来设置出发的时间呢?咱们来看一下我们这个程序,是在哪呢?是在这个位置,你看我们是不是在这来创建出发器,创建出发器的时候,在这来指定with schedule,

这个其实就是设置一个调度的规则,设置调度规则,咱们把这块给它取出来,整个把这块拿出来,这样会清晰了,Ctrl X我们取出来,然后我们具体是怎么指定的出发的时间呢?

咱们在这使用的是这么一个叫做simple schedule builder,然后它的出发规则是不是就是每隔三秒出发一次,然后是repeat forever,就是永远重复,那么就是这么一个出发的规则,

然后现在我们希望把这个出发的规则给它改一下,改成什么呢?使用我们这种call-on表达式,前面咱们应该都学过,所以我们在这就不再去展开去讲这个表达式了,大概它是不是就是由七位来构成,分别是什么呢?

像什么第一位是秒,然后后边是分,然后是小时,对不对?然后什么日月周年,但是最后那个年那个位置是可以为空的,所以一般我们写前六位就可以了,

然后每位上面又可以使用一些特殊的字符,对吧?这样设置起来就比较灵活了,那我们这个地方就来看一下,咱们就需要把这个simple schedule builder给它改成这么一个,叫做call-on,叫做call-on,c-r-o-n,scal-o-n,你看,它这里边叫做call-on schedule builder,然后它是怎么创建的呢?它自己有一个方法,就叫做call-on schedule,然后在这指定一个表达式,

然后呢,我们是不是就可以把它呢,放在这个位置了,call-on schedule builder,但是这样创建出来的就不是一个simple trigger了,对吧?就是一个普通的trigger,所以把这儿呢,简单改一下,改成trigger,然后呢,我们在这儿呢,重点是不是就要去写这个call-on表达式,对不对?咱们在这儿呢,就简单复制一下,我的讲义上已经整理好了,来看一下,就是这么一个表达式,

这个表达式是什么?

这个含义呢,咱们来超过来看一下,前面啊,这个逗号呢,是不是表示或者的关系,对吧?表示是一个列表,然后第一位呢,刚才提到,它代表的是秒,也就是说秒这个位置呢,当是第一秒,5,11,20,27,35,这些秒的时候呢,是不是会触发,然后后边代表的是星,对不对?那就是说每分钟,每小时,什么每周,每月,是不是都会触发,对吧?然后这个问号呢,表示是不是可以忽略,对吧?

那么可以,这个呢,就不用参考了,然后呢,就是什么呢,每时每刻,只要这个秒是这些秒的时候,那么就会触发,好,这就是我们这个call-on表达式啊,然后呢,接下来我们就来测试一下,看看是不是这些秒数的时候会触发,好,咱们呢,在这儿来执行这个面方法,好,注意看,这个秒呢,是5,10点48分05秒触发,然后呢,这是11秒,

触发,你看,跟我们这儿,你看,5,11,下一次呢,应该是20,对吧?20,然后再下一次呢,应该是27,稍等一下,我们等待几秒钟,你看,27,然后再下一次呢,应该是35,你看,35,然后再下一次呢,肯定就是等10点49分01秒的时候,是不是会触发,好,这个呢,我们就不再去等待它了,然后呢,我们就简单看一下,也就是说我们一开始呢,用的是这种simple scheduler builder,对吧?

哎,简单的,那么

就是每隔多少秒

来执行,而这个coin表达式呢,我们

通过它呢,就可以写出来非常

复杂的这种逻辑关系,对吧?

比如说我是每个月

几号,对吧?或者是每周的

星期几,然后几点来触发

那么通过这个coin表达式呢,是

可以非常灵活的去写出来的

你看这01秒,然后05秒,它又

回来了,11秒

这是我们关于第三个

问题,就是使用这个对象

叫做coin scheduler builder

然后呢,在这里边呢,就可以

设置我们这个coin表达式,通过

这个表达式来指定我们这个触发的

时间,好,这是第三个问题

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于 **Quartz 定时任务框架** 的入门实践教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个简单的定时任务（HelloJob），并逐步讲解了任务的核心组件：**Job（任务）**、**Trigger（触发器）** 和 **Scheduler（调度器）**。课程重点在于通过代码实例，演示如何设置任务的执行频率（如每3秒一次或使用 Cron 表达式），以及如何在任务执行时获取上下文参数。视频中还通过控制台输出，直观地展示了任务的执行日志和调度效果，帮助学习者理解 Quartz 的工作原理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 课程开场，展示项目结构和 `HelloJob` 任务类的代码，说明 `execute` 方法是任务的核心执行逻辑。
*   **00:11 - 00:25**: 讲解 `HelloJobMain` 主类，演示如何创建 `Scheduler`、`JobDetail` 和 `SimpleTrigger`，并调用 `scheduleJob` 和 `start` 方法启动调度。
*   **00:26 - 00:35**: 展示控制台输出，验证任务已成功执行，并说明 `JobDataMap` 用于存储任务参数。
*   **00:36 - 00:45**: 讲解 `JobExecutionContext`，并演示如何在 `execute` 方法中获取 `JobDataMap` 中的参数。
*   **00:46 - 00:55**: 引入并演示 `CronScheduleBuilder`，讲解如何使用 Cron 表达式来设置更复杂的触发时间。
*   **00:56 - 01:05**: 展示修改后的代码，将触发器从 `SimpleTrigger` 改为 `CronTrigger`，并演示其执行效果。
*   **01:06 - 01:15**: 讲解 `CronScheduleBuilder` 的常用方法，如 `cronSchedule`，并展示其在代码中的应用。
*   **01:16 - 01:25**: 总结课程内容，强调 Quartz 的核心概念和使用方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲：`第5章 智能调度服务(pd-dispatch)` -> `1. 定时任务组件Quartz` -> `1.3 入门案例` -> `1.3.2 问题思考`。
    *   问题思考：
        1.  自定义任务 `HelloJob` 是单例的还是每次执行定时任务都创建一个实例？
        2.  如何给定时任务传递参数并且在执行任务时可以获取到相应参数？
        3.  入口案例中触发器设置的是每隔5秒执行一次，是否可以使用 Cron 表达式设置触发时间？
    *   解答：
        1.  通过添加无参构造方法来解决。
        2.  使用 `JobDataMap` 和 `JobExecutionContext`。
        3.  使用 `CronScheduleBuilder`。

*   **关键代码**:
    *   **Job 类 (`HelloJob.java`)**:
        ```java
        public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {
            System.out.println("自定义Job执行，执行时间为：" + new Date());
            // 获取有效的任务状态信息
            JobDataMap jobDataMap = jobExecutionContext.getJobDetail().getJobDataMap();
            final Set<Map.Entry<String, Object>> entries = jobDataMap.entrySet();
            entries.forEach(entry -> {
                String key = entry.getKey();
                Object value = entry.getValue();
                System.out.println(key + "=" + value);
            });
        }
        ```
    *   **主类 (`HelloJobMain.java`)**:
        ```java
        public class HelloJobMain {
            public static void main(String[] args) {
                Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
                JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity("myjobdetail").build();
                jobDetail.getJobDataMap().put("key1", "value1");
                jobDetail.getJobDataMap().put("key2", "value2");
                SimpleScheduleBuilder simpleScheduleBuilder = SimpleScheduleBuilder.simpleSchedule().withIntervalInSeconds(3).repeatForever();
                SimpleTrigger trigger = TriggerBuilder.newTrigger().withIdentity("mytrigger").withSchedule(simpleScheduleBuilder).build();
                scheduler.scheduleJob(jobDetail, trigger);
                scheduler.start();
            }
        }
        ```
    *   **使用 Cron 表达式的代码**:
        ```java
        CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule("1,5,11,20,27,35 * * * * ?");
        Trigger trigger = TriggerBuilder.newTrigger().withIdentity("mytrigger").withSchedule(cronScheduleBuilder).build();
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建并执行简单定时任务**
    *   **描述**: 讲师在 IntelliJ IDEA 中展示 `HelloJobMain` 类的代码，其中创建了一个 `Scheduler`，并配置了一个 `JobDetail` 和 `SimpleTrigger`。通过 `scheduler.start()` 启动调度器。
    *   **演示**: 运行程序后，控制台输出显示任务每3秒执行一次，打印“自定义Job执行，执行时间为：”和当前时间。

*   **场景二：使用 JobDataMap 传递参数**
    *   **描述**: 讲师在 `HelloJob` 类的 `execute` 方法中，通过 `JobExecutionContext.getJobDetail().getJobDataMap()` 获取任务参数。
    *   **演示**: 运行程序后，控制台输出显示 `key1=value1` 和 `key2=value2`，证明参数成功传递并被获取。

*   **场景三：使用 Cron 表达式设置触发时间**
    *   **描述**: 讲师将触发器从 `SimpleTrigger` 改为 `CronTrigger`，并使用 `CronScheduleBuilder.cronSchedule("1,5,11,20,27,35 * * * * ?")` 设置触发时间。
    *   **演示**: 运行程序后，控制台输出显示任务在指定的秒数（1, 5, 11, 20, 27, 35）触发执行，验证了 Cron 表达式的有效性。

*   **场景四：解决任务单例问题**
    *   **描述**: 讲师在 `HelloJob` 类中添加了无参构造方法 `public HelloJob() {}`。
    *   **演示**: 运行程序后，控制台输出显示“创建HelloJob实例”，证明每次执行定时任务都会创建一个新的 `HelloJob` 实例。

*   **场景五：解决参数传递问题**
    *   **描述**: 讲师在 `HelloJobMain` 类中，通过 `jobDetail.getJobDataMap().put("key1", "value1");` 设置参数，并在 `HelloJob` 的 `execute` 方法中通过 `JobExecutionContext` 获取。
    *   **演示**: 运行程序后，控制台输出显示 `key1=value1` 和 `key2=value2`，证明参数成功传递并被获取。

*   **场景六：使用 Cron 表达式设置触发时间**
    *   **描述**: 讲师在 `HelloJobMain` 类中，使用 `CronScheduleBuilder.cronSchedule("1,5,11,20,27,35 * * * * ?")` 设置触发时间。
    *   **演示**: 运行程序后，控制台输出显示任务在指定的秒数（1, 5, 11, 20, 27, 35）触发执行，验证了 Cron 表达式的有效性。
