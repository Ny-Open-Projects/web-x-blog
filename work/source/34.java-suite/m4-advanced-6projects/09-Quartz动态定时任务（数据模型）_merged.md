# 09-Quartz动态定时任务（数据模型） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们来看一下我们cause的动态定时任务。

前面我们这个入门案例当中啊,我们是通过cause实现了简单的这种定时任务效果,对吧?

但是这种方式啊,它的这个任务信息呢,是保存在内存当中的。

如果服务重启之后呢,这个任务信息呢,就会丢失。

这个任务信息呢,我们指的就是啊,咱们这个地方通过这个什么job,datamap,对吧,来存储的这些值。

那么如果说我们服务重启之后啊,这些状态信息呢,其实就没有了,对吧?

那么我们这个地方呢,可以通过一个断点的方式呢,能够看到这个现象。

也就是说,它这个地方这个任务存储呢,使用的是这个,叫做ramjobstore来实现的。

咱们呢,可以在这儿来加一个断点呢,来简单跟踪一下。

好,加一个断点,然后呢,我们使用debug方式呢,来启动咱们这个项目。

好,稍等一下啊,因为它是,

需要到这些秒数的时候呢,是不是才会出发,对吧?

这是刚才我们写的这个,呃,靠岸表达式。

然后呢,现在我们回到这边来,来看一下什么呢?

看一下我们这个上下文对象。

然后在上下文对象里边呢,你看是不是有一个scheduler,对吧?

然后在scheduler这里边呢,有这么一个。

然后呢,我们直接去找啊,找这个什么呢,resources,资源,对吧?

然后在这里边呢,有一个,来找一下,叫做jobstore,对吧?

那么它的一个存储呢,

使用的就是这个,叫做RAM jobstore。

然后呢,这个类的话呢,咱们前面在核心API这块呢,

在我们前面这个核心API这儿,也简单提到过啊,就是RAM jobstore。

那么这个类呢,实现了一个利用我们这个RAM,就是内存,

作为存储介质的这么一个jobstore。

它的访问速度特别快,对吧?但是数据容易丢失。

所以说呢,我们这个地方呢,默认情况下,使用的就是这种,这种方式,对吧?

使用它来实现我们这个,

任务信息这些存储。

那么,我们如果要想使用这种定时任务的话,要实现这种动态的定时任务的话呢,

我们就需要选择另外一种存储方式,就是什么呢?

使用这个jobstore tx,也就是下边这一种,jobstore tx。

它其实是什么呢?通过GDPC的方式,将我们这个数据呢,把它保存到数据库当中。

这样的话呢,即使我们这个任务呢,重启之后,

那么因为保存的这个数据呢,它是存在数据库,已经持久化了。

所以说呢,这些信息呢,也不会丢失。

这样的话,我们就可以去实现我们动态的定时任务了。

所以说呢,我们这块呢,就需要把它保存在数据库当中,通过这个对象来帮我们保存。

那么同时呢,我们这种方式呢,还支持动态定时任务,对吧?

例如什么动态添加定时任务,什么暂停定时任务,删除定时任务等等。

这个一会儿我们在这块呢,都会使用到。

那这儿的话,我们要把这个,我们这些信息把它保存到数据库。

那就需要有一套数据模型,对不对?

而这套数据模型呢,是由Course官方给我们提供的。

也就是说,它为了保存这些信息呢,它给我们提供了一套数据模型,一共涉及到了是11张表。

那么对于保存定时任务,用来保存这个定时任务相关的信息。

那么因为我们有可能使用的数据库不同,对吧?

所以说呢,

它封装了,它给我们提供了这么多的键标语句,就是针对不同的数据库的,比如说有针对DB2的,对吧?

还有什么呢?

H2的,还有什么My Circle的,Informix的,等等啊,这些。

那么还有Oracle的,对吧?

那么针对不同的数据库呢,它都提供了相应的这个脚本。

大家可以看一下我们这个资料当中,对吧?

这是我们这个Course2.3呢,它这个,我们从它这个官网上下载下来的安装包,然后解压之后就是这么一个效果。

然后,

在这里边呢,

有一个Docs,在Docs里边呢,有个叫做DB Tables。

你看这里面的就是针对不同数据库啊,提供了不同的这个脚本。

然后我们如果使用My Circle的话呢,我们就可以使用这个tables-mycircle.circle。

咱们可以打开它来看一下。

你看这里边呢,其实就是什么呢?

就是一些这个Curve Table,键标语句。

你看这个叫做Curses-triggers,也就是我们的出发器呢,会保存在这个表里面。

然后,

还有什么呢?

Codes-simple-triggers,对吧?

简单的出发器。

还有Con-triggers,对吧?

这是不是就是基于我们这个Con表达式,它的出发器。

还有Simple-triggers,然后还有什么呢?

Blog-triggers,这些都是跟这个出发器相关的。

还有Calendars,对吧?

那么一共呢,涉及到的是11张表。

哎,11张表。

那么在这儿呢,我们就直接执行这个键标语句,然后呢,把它创建到我们这个My Circle数据库当中就可以了。

但是这步呢,我都已经创建好了。

咱们直接来看一下就可以了。

那么我们这个呢,是用的本地的数据库啊。

当然你用远程的,什么地方的数据库都无所谓啊。

这个都没有关系。

这个呢,我使用的是本地的My Circle。

然后呢,我创建了一个数据库,就叫做Course。

然后呢,在这里边呢,创建出来了一共是这么11张表,对吧?

这11张表呢,就是执行我们刚才看到的这个脚本。

哎,执行的这个Circle脚本。

然后呢,创建出来的。

好。

这是我们要实现咱们这个动态定时任务,对吧?

哎,那么就需要我们这个这么一套数据模型。

而这一套数据模型呢,是由Course官方给我们提供的。

好,咱们直接把它创建出来就可以了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于 **Quartz 定时任务框架** 的深入讲解，重点在于 **如何实现持久化存储** 以解决任务信息在服务重启后丢失的问题。课程首先通过一个简单的内存任务示例引出问题，然后详细介绍了 Quartz 的 `JobStoreTX` 机制，该机制将任务和触发器的信息存储在数据库中。课程内容包括：展示内存任务的执行（通过 IntelliJ IDEA 的控制台输出），讲解 `JobExecutionContext` 中获取任务数据的方法，展示数据库表结构（通过 SQL 脚本和数据库设计工具），并最终通过图形化工具（如 Navicat Premium）展示 Quartz 在 MySQL 数据库中的完整数据模型。整个课程旨在帮助开发者理解 Quartz 的核心架构，并掌握如何在生产环境中部署持久化定时任务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示 IntelliJ IDEA 中的 `HelloJobMain.java` 代码，演示一个简单的、基于内存的 Quartz 任务。
*   **00:05 - 00:15**: 代码执行演示，控制台输出显示任务成功执行并打印了传入的参数 `key1` 和 `key2`。
*   **00:15 - 00:25**: 聚焦于 `HelloJob` 类中的 `execute` 方法，讲解如何通过 `JobExecutionContext` 获取任务的上下文信息，特别是 `JobDataMap`。
*   **00:25 - 00:35**: 通过调试器查看 `JobExecutionContext` 对象，展示其内部包含的 `trigger`、`jobDetail` 等关键信息。
*   **00:35 - 00:45**: 切换到课程 PPT，介绍 Quartz 的 `JobStoreTX` 机制，说明其将任务信息持久化到数据库中，从而避免服务重启后任务丢失。
*   **00:45 - 00:55**: 展示 Quartz 官方提供的数据库建表脚本文件列表，指出本课程将使用 MySQL 版本。
*   **00:55 - 01:05**: 在 Notepad++ 中打开并查看 `tables_mysql.sql` 文件，展示其中定义的 `QRTZ_SIMPLE_TRIGGERS` 和 `QRTZ_CRON_TRIGGERS` 等核心表结构。
*   **01:05 - 01:15**: 继续查看 `tables_mysql.sql` 文件，展示 `QRTZ_JOB_DETAILS` 和 `QRTZ_TRIGGERS` 等表的定义。
*   **01:15 - 01:25**: 使用 Navicat Premium 数据库设计工具，展示在 MySQL 中创建的 Quartz 数据库表结构图，包括 `QRTZ_JOB_DETAILS`、`QRTZ_TRIGGERS`、`QRTZ_CALENDARS` 等表及其关联关系。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “2. Quartz动态定时任务”。
    *   **核心观点**: “Quartz提供了另外一种方式，即通过JobStoreTX对象将任务相关信息保存在数据库中，这样就可以避免服务重启后任务信息丢失的问题。”
    *   **数据模型**: “Quartz官方提供了一套数据模型(共11张表)用于保存定时任务相关信息，建表脚本：”并列出 `tables_*.sql` 文件。
    *   **数据库表结构图**: 展示了 `QRTZ_JOB_DETAILS`、`QRTZ_TRIGGERS`、`QRTZ_CALENDARS` 等表的实体关系图。

*   **代码关键内容**:
    *   **`HelloJobMain.java`**:
        ```java
        // 创建触发器
        Trigger trigger = TriggerBuilder.newTrigger()
            .withIdentity("mytrigger")
            .withSchedule(CronScheduleBuilder.cronSchedule("1,5,11,20,27,31 1,5,11,20,27,31 ? * * * * *"))
            .build();
        // 创建任务
        JobDetail jobDetail = JobBuilder.newJob(HelloJob.class)
            .withIdentity("myjob")
            .usingJobData("key1", "value1")
            .usingJobData("key2", "value2")
            .build();
        // 调度任务
        scheduler.scheduleJob(jobDetail, trigger);
        // 启动调度器
        scheduler.start();
        ```
    *   **`HelloJob.java`**:
        ```java
        public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {
            // 获取任务数据
            JobDataMap jobDataMap = jobExecutionContext.getJobDetail().getJobDataMap();
            // 打印任务数据
            System.out.println("自定义Job执行，执行时间为：" + new Date());
            for (Map.Entry<String, Object> entry : jobDataMap.entrySet()) {
                String key = entry.getKey();
                Object value = entry.getValue();
                System.out.println(key + " = " + value);
            }
        }
        ```

*   **图表关键内容**:
    *   **数据库表结构图**: 在 Navicat Premium 中展示的实体关系图，清晰地显示了 `QRTZ_JOB_DETAILS`、`QRTZ_TRIGGERS`、`QRTZ_CALENDARS` 等表及其外键关联。

---

### 4) 关键场景与演示描述

*   **场景一：内存任务执行演示**
    *   **描述**: 在 IntelliJ IDEA 中，开发者运行 `HelloJobMain` 类。控制台输出显示任务成功执行，并打印了 `key1 = value1` 和 `key2 = value2`。这演示了 Quartz 基础的、非持久化的任务调度能力。

*   **场景二：调试器查看任务上下文**
    *   **描述**: 开发者在 `HelloJob` 类的 `execute` 方法中设置断点并启动调试。当任务执行时，调试器会显示 `JobExecutionContext` 对象的详细信息，包括 `trigger`、`jobDetail`、`jobDataMap` 等，帮助开发者理解任务的运行时上下文。

*   **场景三：数据库建表脚本分析**
    *   **描述**: 开发者在 Notepad++ 中打开 `tables_mysql.sql` 文件，逐行查看 SQL 语句。通过高亮和滚动，展示了 `QRTZ_SIMPLE_TRIGGERS`、`QRTZ_CRON_TRIGGERS`、`QRTZ_JOB_DETAILS` 等表的 `CREATE TABLE` 语句，了解了 Quartz 数据库表的结构。

*   **场景四：数据库实体关系图展示**
    *   **描述**: 开发者使用 Navicat Premium 连接到 MySQL 数据库，打开 Quartz 数据库的 `ER Diagram`。屏幕上清晰地展示了 `QRTZ_JOB_DETAILS` 表与 `QRTZ_TRIGGERS` 表之间的 `1:N` 关系，以及 `QRTZ_TRIGGERS` 表与 `QRTZ_CALENDARS` 表等其他表的关联，直观地呈现了 Quartz 的数据模型。

---
