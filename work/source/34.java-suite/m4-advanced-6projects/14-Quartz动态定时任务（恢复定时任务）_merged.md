# 14-Quartz动态定时任务（恢复定时任务） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才呢我们是实现了暂停定时任务

那么我们调用的方法呢比较简单

就是调用Scheduler对象的一个叫做PathJob

这么一个方法对吧

然后呢通过这个BICID

封装成这么一个JobKey对象

然后传进去

这就是暂停指定的定时任务

好,然后呢我们需要知道什么呢

我们一调这句话的话

其实那么框架呢

就是Cars框架会去帮我们修改数据库

然后呢它改的是哪张表呢

它其实改的是这个

叫做Cars-Triggers这张表

咱们来看一下

你看这个表里面有两条记录

从这能看出来分别对应的是这两个对吧

定时任务1001 1002

然后呢我们调用的那个PathJob

它其实改的就是这个字段的值

就是这个字段叫做TriggerState

这是不是Trigger的状态对吧

触发器的状态

现在呢都改成了这叫做Path的

这个翻译过来就是暂停的意思

暂停

好

所以

所以说呢我们调用这个方法

那么底层呢

其实就是去修改这张表的这个字段

把它这个状态改成这个值

这就表示这个任务呢暂停了

然后接下来呢

我们来看下一个就是恢复定时任务

恢复定时任务呢

跟暂停定时任务是不是恰好是相反的

对吧

恢复执行

然后呢

我们这个调用的就是这个叫做ResumeJob

这个方法

同样的还是传进来一个JobKey

对吧

而这个JobKey呢

还是通过BIZID这样来得到的

好

然后呢

我们在这呢

可以来复制一下这个方法

稍微改造一下就可以

这是比较简单的方法

然后呢

把这改成什么呢

叫做ResumeJob

好

然后呢

这个方法名改一下

对吧

这个路径也改一下

这个呢

改成什么呢

恢复

叫做恢复定时任务

OK

然后呢

咱们现在呢

来启动一下啊

我们这个项目

好

现在呢

我们这两个定时任务呢

都是这种什么呢

暂停的状态

对吧

PASS的

然后呢

我们可以来调用一下

刚才咱们这个恢复定时任务

这个接口

对吧

然后呢

来恢复他们的执行

稍等一下

把控制台呢

先清理一下

好

现在呢

应该是已经跑起来了

然后呢

我们可以观察控制台

控制台呢

现在是没有输出的

就是我们定时任务是没有输出的

就是因为他们都处于暂停的状态

对吧

然后呢

现在呢

我们把这个控制台

把这边的刷新一下

咱们来调用一下什么呢

来调用一下这个恢复定时任务

这个接口

比如说我现在呢

来恢复1001

他的这个执行

对吧

先来观察一下控制台啊

这些都不是

这是框架

他的日之输出

不用管他

然后呢

我们来执行一下

注意看

走好

调用完了

调用完之后呢

咱们看控制台

你看他是不是已经开始恢复执行了

对吧

然后再观察一下什么呢

观察一下我们这个表里面的变化

你看

现在呢

这个1001所对应的这一条

是不是这个状态就已经发生了变化

叫做acquired

这是啥意思呢

这叫做获得

也就是获得执行的权利了

已经

好

那么这是我们测试了一下

咱们调用这个resume job

这个方法

对吧

就可以将已经暂停的这个任务呢

给他恢复执行

好

那么这个呢

我们简单测试一下就可以了

都是比较简单的方法

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 项目中集成 Quartz 定时任务框架，重点演示如何通过 HTTP 接口实现对定时任务的“暂停”和“恢复”操作。讲师通过 IntelliJ IDEA 编辑器展示控制器代码，通过 Navicat Premium 查看数据库中的触发器状态，并通过 Swagger UI 进行接口测试，完整地呈现了从代码实现到功能验证的开发流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，定位到“2.3.2 暂停定时任务”章节。
*   **00:00:05 - 00:00:15**：在 IntelliJ IDEA 中展示 `QuartzController.java` 文件，重点讲解 `@PutMapping("/pause/{bizId}")` 方法的代码逻辑。
*   **00:00:15 - 00:00:25**：切换到 Navicat Premium，展示 `qrtz_triggers` 数据库表，其中包含 `pdScheduler` 任务的触发器信息，用于后续验证。
*   **00:00:25 - 00:00:35**：回到 IDEA，展示 `QuartzController.java` 中 `pause` 方法的完整代码，包括 `JobKey` 的创建和 `scheduler.pauseJob` 的调用。
*   **00:00:35 - 00:00:45**：在 IDEA 的终端中运行 `QuartzApplication`，查看 Spring Boot 启动日志。
*   **00:00:45 - 00:00:55**：在 IDEA 中展示 `resume` 方法的代码，用于恢复定时任务。
*   **00:00:55 - 00:01:05**：在 IDEA 终端中再次运行应用，观察 Quartz Scheduler 启动日志。
*   **00:01:05 - 00:01:15**：在浏览器中打开 Swagger UI，展示 `/quartz/pause/{bizId}` 和 `/quartz/resume/{bizId}` 两个接口。
*   **00:01:15 - 00:01:25**：在 Swagger UI 中，为 `/quartz/resume/{bizId}` 接口输入 `bizId=1001`，并点击“Execute”按钮进行测试。
*   **00:01:25 - 00:01:35**：在 IDEA 中展示 `resume` 方法的代码，再次确认其逻辑。
*   **00:01:35 - 00:01:45**：在 IDEA 中展示课程大纲，定位到“2.3.3 恢复定时任务”和“2.3.4 删除定时任务”章节，为后续内容做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程大纲：清晰地列出了“第8章 智能调度服务(pd-dispatch)”下的各个子章节，包括“2.3 实现定时任务”及其子项“2.3.2 暂停定时任务”、“2.3.3 恢复定时任务”等。
    *   代码注释：在控制器方法中，有清晰的中文注释，如 `/* 暂停定时任务 */` 和 `/* 恢复定时任务 */`，以及方法的描述 `@ApiOperation("暂停定时任务")` 和 `@ApiOperation("恢复定时任务")`。

*   **代码关键内容**：
    *   **暂停任务方法 (`pause`)**：
        ```java
        @PutMapping("/pause/{bizId}")
        @ApiOperation("暂停定时任务")
        public String pause(@PathVariable String bizId) throws Exception {
            JobKey jobKey = JobKey.jobKey(bizId);
            scheduler.pauseJob(jobKey);
            return "OK";
        }
        ```
    *   **恢复任务方法 (`resume`)**：
        ```java
        @PutMapping("/resume/{bizId}")
        @ApiOperation("恢复定时任务")
        public String resume(@PathVariable String bizId) throws Exception {
            JobKey jobKey = JobKey.jobKey(bizId);
            scheduler.resumeJob(jobKey);
            return "OK";
        }
        ```
    *   **数据库表结构**：
        *   表名：`qrtz_triggers`
        *   关键字段：`SCHED_NAME` (调度器名称), `TRIGGER_NAME` (触发器名称), `JOB_NAME` (任务名称), `NEXT_FIRE_TIME` (下次执行时间), `PREV_FIRE_TIME` (上次执行时间)。

*   **图表 / 界面**：
    *   **Swagger UI 接口文档**：
        *   展示了 `/quartz/pause/{bizId}` 和 `/quartz/resume/{bizId}` 两个 PUT 接口。
        *   接口参数：`bizId` (string, required)。
        *   接口响应：`"OK"`。
    *   **Navicat Premium 数据库界面**：
        *   展示了 `qrtz_triggers` 表的数据，用于验证任务状态。

---

### 4) 关键场景与演示描述

*   **场景一：暂停任务功能实现与验证**
    *   **演示过程**：讲师首先在 IDEA 中编写了 `pause` 方法，该方法通过 `JobKey.jobKey(bizId)` 获取任务键，然后调用 `scheduler.pauseJob(jobKey)` 来暂停指定任务。接着，讲师在 Navicat 中查看了数据库中的触发器状态，确认了任务的暂停状态。
    *   **技术要点**：展示了如何通过 Quartz API 暂停一个已存在的定时任务，并通过数据库验证其状态。

*   **场景二：恢复任务功能实现与验证**
    *   **演示过程**：讲师在 IDEA 中编写了 `resume` 方法，该方法通过 `JobKey.jobKey(bizId)` 获取任务键，然后调用 `scheduler.resumeJob(jobKey)` 来恢复指定任务。讲师随后在 Swagger UI 中调用 `/quartz/resume/1001` 接口，成功恢复了任务。
    *   **技术要点**：展示了如何通过 Quartz API 恢复一个已暂停的定时任务，并通过 Swagger UI 进行了接口测试。

*   **场景三：系统启动与日志监控**
    *   **演示过程**：讲师在 IDEA 中运行 `QuartzApplication`，并观察终端中的启动日志。日志显示了 Spring Boot 的启动过程以及 Quartz Scheduler 的初始化信息，如 `Starting Quartz Scheduler now...`。
    *   **技术要点**：展示了 Quartz 定时任务框架在 Spring Boot 项目中的集成方式，以及如何通过日志监控其启动状态。

*   **场景四：接口测试与文档展示**
    *   **演示过程**：讲师在浏览器中打开 Swagger UI，展示了 `/quartz/pause/{bizId}` 和 `/quartz/resume/{bizId}` 两个接口的详细信息，包括请求方法、参数和响应。讲师随后在 Swagger UI 中输入 `bizId=1001` 并点击“Execute”按钮，成功调用了恢复接口。
    *   **技术要点**：展示了如何使用 Swagger UI 为 RESTful API 生成文档，并通过其界面进行便捷的接口测试。
