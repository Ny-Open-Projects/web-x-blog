# 30-智能调度服务（实现过程_编写智能调度组件 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看我们智能调度服务

刚才呢我们是把这个定时任务这个类呢

已经完善了对吧

然后呢我们接下来下边要写的就是什么呢

我们这个目标类了

你看咱们在这个地方是不是通过我们这个反射对吧

来调用我们目标类的run方法

那么接下来呢

我们就是来编写咱们这个智能调度组件

然后这个类名呢就叫做dispatch task就可以了

放在哪呢

放在task这个包下边

咱们在这个地方呢来创建一个task包

好

应该是一个包啊

package

好

task

然后在这里边呢

我们来创建这么一个类叫做dispatch task

而这个类里边封装的就是我们智能调度的核心逻辑

对吧

然后这里边呢需要提供run方法

在我们前面这个定时任务类当中

咱们通过反射是不是调用这个方法

好

这个代码呢

我们前面

也都看过了

叫做dispatch task

ok

这个呢我们就叫做什么呢

智能调度

智能调度组件

好

然后这个组件的话呢

需要把它交给我们sprint容器来管理

为什么呢

大家来看啊

咱们这个地方是不是通过我们这个

sprint context utils工具类

getbin对吧

这是从我们sprint容器当中来获得这个bin

所以说呢

我们在这个地方呢

必须给它加一个注解

component的对吧

并且呢

我们可以指定这个组件呢

它是什么呢

它的bin的名称

bin的名称啊

注意不能随便写

应该是什么呢

应该是跟我们这个数据库里面这个保持一致

对吧

保持一致

好

叫做dispatch task

直接超过来就可以了

ok

然后呢

我们在这里面是不是需要来提供一个什么呢

提供一个run方法

对吧

提供一个run方法

public void run

然后呢

这个方法的话是不是需要有几个参数呢

四个参数对吧

四个参数

分别是什么呢

分别是我们这个业务id

然后还有parameter

参数

还有就是这个job id

定时任务的id

还有一个就是我们这个日志的id

那么分别对应的是这四个参数

然后呢

我们在这呢

可以直接来

直接来复制一下吧

这块

把它超过来

然后呢

为了方便记录日志呢

我们可以在这来一个sleep for day

在这的话呢

咱们就可以来输出一下这句话

输出一下这句话

你看智能调度正在执行

然后参数

在这呢

我们能够看到

对吧

这就是我们智能调度啊

在这个地方来进行智能调度

智能调度

好

那这个代码

这个类呢

我们就已经写好了

对吧

然后run方法也创建出来了

但是一会呢

我们再去完善什么呢

具体这个方法里边

怎么进行智能调度

咱们现在呢

先把这个类写好

创建出来

然后呢

我们就可以来启动项目呢

来测试一下

对吧

一会我们来测试一下

看看什么呢

看看当我们这个任务啊

触发的时候

它能不能正常的通过反射

调用到我们这个目标对象

对吧

那么如果能够正常调用

它是不是就能调用到

我们这个run方法

对吧

而我们这个run方法

在这个地方呢

是不是有日志输出

通过在控制台呢

观察日志

我们应该就能够看到

对吧

这个任务到底有没有真正执行

好

咱们呢

这是把所需要的这个类呢

先来创建出来

一会儿呢

我们来测试一下

如果整个流程能够跑通

对吧

哎

没有问题

我们再来完善这个run方法

好

所以说呢

我们全都是这种思路

就是什么呢

先把所需要的类对吧

所需要的方法创建出来

然后进行测试

跑通了之后

再回过头来完善真正的核心逻辑

大概是这么一个套路

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在基于 Spring 框架的定时任务系统中，实现一个“智能调度组件”。核心内容是编写一个 `DispatchTask` 类，该类通过反射机制被 `ScheduleJob` 定时任务调用，从而执行具体的智能调度逻辑。视频主要演示了如何定义这个组件、如何通过 Spring 的 `@Component` 注解进行管理，以及如何在 `ScheduleJob` 中通过反射调用其 `run` 方法。整个过程展示了如何将业务逻辑封装成可调度的组件，并通过日志记录任务的执行状态和耗时。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节划分是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程导航与章节定位。画面显示了项目结构和当前章节“3.3.5 编写智能调度组件”，并介绍了本节目标：编写一个 `DispatchTask` 类，作为智能调度的核心逻辑。
*   **00:05 - 00:15**: `DispatchTask` 类的定义。在 IntelliJ IDEA 中创建并编辑 `DispatchTask.java` 文件，定义了类的包名、导入的依赖（`@Component`, `@Slf4j`）和类的注解。
*   **00:15 - 00:25**: `run` 方法的参数与日志。在 `run` 方法中定义了四个参数（`businessId`, `params`, `jobId`, `logId`），并添加了日志语句，用于记录调度任务的执行参数。
*   **00:25 - 00:35**: `ScheduleJob` 中的反射调用逻辑。切换到 `ScheduleJob.java` 文件，演示了如何通过 `SpringContextUtils.getBean()` 获取目标对象，然后通过 `getDeclaredMethod` 获取 `run` 方法，并使用 `method.invoke()` 反射调用该方法。
*   **00:35 - 00:45**: 任务执行日志与状态记录。在 `try-catch` 块中，记录了任务的开始时间、执行耗时，并根据执行结果设置日志实体的状态（成功或失败）。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **代码关键内容**

*   **`DispatchTask.java` 文件内容：**

    ```java
    package com.iteima.pinda.task;

    import lombok.extern.slf4j.Slf4j;
    import org.springframework.stereotype.Component;

    /**
     * 智能调度组件
     */
    @Slf4j
    @Component("dispatchTask")
    public class DispatchTask {

        /**
         * 智能调度
         * @param businessId
         * @param params
         * @param jobId
         * @param logId
         */
        public void run(String businessId, String params, String jobId, String logId) {
            log.info("智能调度正在执行，参数为：{},{},{},{}", businessId, params, jobId, logId);
        }
    }
    ```

*   **`ScheduleJob.java` 文件中关键代码段：**

    ```java
    // 记录定时任务相关的日志对象
    ScheduleJobLogEntity logEntity = new ScheduleJobLogEntity();
    logEntity.setId(IdUtils.get());
    logEntity.setJobId(scheduleJob.getJobId());
    logEntity.setBeanName(scheduleJob.getBeanName());
    logEntity.setParams(scheduleJob.getParams());
    logEntity.setCreateDate(new Date());

    long startTime = System.currentTimeMillis();

    try {
        // 通过反射调用目标对象，在目标对象中封装智能调度核心逻辑
        Object target = SpringContextUtils.getBean(scheduleJob.getBeanName());
        Method method = target.getClass().getDeclaredMethod("run", String.class, String.class, String.class, String.class);
        method.invoke(target, scheduleJob.getBusinessId(), scheduleJob.getParams(), scheduleJob.getJobId(), scheduleJob.getLogId());

        // 任务执行时长
        long times = System.currentTimeMillis() - startTime;
        logEntity.setTimes(times);
        logEntity.setStatus(1); // 成功
        logger.info("任务执行完毕，任务ID：{}，总耗时：{}毫秒", scheduleJob.getJobId(), times);
    } catch (Exception ex) {
        logEntity.setStatus(0); // 失败
        logEntity.setError(ExceptionUtils.getStackTrace(ex));
    }
    ```

#### **技术概念**

*   **反射机制 (Reflection)**：用于在运行时动态获取类的信息并调用其方法，是实现“智能调度”与“定时任务”解耦的关键。
*   **Spring 注解 (`@Component`, `@Slf4j`)**：`@Component` 用于将 `DispatchTask` 注册为 Spring 容器中的 Bean，`@Slf4j` 用于自动生成日志对象。
*   **`ScheduleJob` 类**：一个定时任务的执行器，负责通过反射调用 `DispatchTask` 的 `run` 方法。
*   **日志记录**：通过 `ScheduleJobLogEntity` 记录任务的执行状态、耗时和异常信息。

---

### 4) 关键场景与演示描述

1.  **场景一：项目结构与组件定位**
    *   **描述**：视频开始时，画面展示了 IntelliJ IDEA 的项目结构，清晰地定位到“第8章 智能调度服务”下的“3.3.5 编写智能调度组件”章节。这为观众提供了当前学习内容的上下文。
    *   **技术点**：强调了组件在项目中的位置和作用。

2.  **场景二：创建并编写 `DispatchTask` 类**
    *   **描述**：在 `DispatchTask.java` 文件中，讲师逐步编写代码。首先定义了类的包名和导入的依赖，然后使用 `@Component("dispatchTask")` 注解将其注册为 Spring Bean。接着，定义了 `run` 方法及其参数，并添加了日志语句。
    *   **技术点**：演示了如何创建一个可被 Spring 管理的业务组件，并定义其核心执行方法。

3.  **场景三：`ScheduleJob` 中的反射调用**
    *   **描述**：讲师切换到 `ScheduleJob.java` 文件，演示了如何通过 `SpringContextUtils.getBean()` 获取 `DispatchTask` 实例，然后通过 `getDeclaredMethod` 获取 `run` 方法，并使用 `method.invoke()` 调用它。同时，演示了如何记录任务的开始时间、执行耗时和最终状态。
    *   **技术点**：核心演示了如何通过反射机制将定时任务与具体的业务逻辑解耦，实现了“智能调度”的动态调用。

4.  **场景四：日志与状态管理**
    *   **描述**：在 `try-catch` 块中，讲师演示了如何记录任务的执行时长，并根据执行结果设置 `logEntity` 的状态（成功或失败）。这确保了任务执行的可追溯性和可观测性。
    *   **技术点**：强调了任务执行过程中的监控和异常处理机制。

---

以上是根据视频画面提供的技术分析。视频内容清晰地展示了如何在 Spring 框架中实现一个可被定时任务调用的智能调度组件，其核心是反射机制和日志记录。
