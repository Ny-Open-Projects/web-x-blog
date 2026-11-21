# 26-智能调度服务（实现过程_初始化定时任务_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来看咱们这个智能调度服务

刚才呢我们这个类啊

就是初始化定时任务这个类呢

已经编写好了

那接下来呢

我们就来测试一下

看看什么呢

看看我们这个定时任务

在项目启动的时候

能不能被这个类给我们初始化出来

以及什么呢

初始化好之后呢

能不能按照我们所编写的那个靠岸表达式

对吧

能够正常触发

好

那么这个地方呢

通过这个代码

咱们也能看到

它来创建这些定时任务呢

首先是不是需要先从我们那个表里面

把我们这些定时任务信息把它查上来

也就是咱们这个表

这个schedule job这个表

这里边呢

已经有一些这个测试数据了

但是下边这些呢

你看它这个靠岸表达式

全都是每天下午18点

也就是6点是不是来触发

那么为了方便我们能够

马上就能触发

看到效果呢

我还添加了这么一条测试数据

这0-5

这是不是就是

每隔5秒触发一次

这样呢是

马上我们是不是就能看到效果

对吧

要不然的话

下边这些即使你创建出来

也只能等到下午6点

是不是才能看到结果

它才能触发

所以说呢

我们在这呢

创建了这么一条测试数据

在这呢

我们可以来解释一下

就是这个表里面的这个数据

是从哪来的

对吧

难道是我们手动

往这个表里面插入数据吗

很显然这是不现实的

咱们后边呢

会开发先应的这个服务接口

也就是在我们的页面上呢

我可以

点击某个组织机构

然后呢

右侧呢

就能出现啊

这么一个页面

咱们来看一下

你看

我点击左侧这个机构

对吧

我们专门有这么一个页面

然后右侧呢

就有这么一个表单

对吧

就有这么一个表单

然后呢

我是不是就可以啊

在这个表单里边干什么呢

在这个表单里面

来录入相关的这些信息

录入信息

录入完之后呢

直接点这个修改按钮

那么它就会把我们这个信息呢

把这条记录

对应的

插入到什么呢

插入到我们这个

刚才看到的这张表怎么来了

所以说呢

我们这里面的数据呢

是通过这个页面啊

最终调用我们所提供的服务接口

然后把这个数据

把它插进来的

好

但是现在因为我们还没有开发到

这一块啊

所以我们只能是先手动的

向这个表里面来插入这条测试数据

好

咱们这是先解释了一下

这条数据它是怎么来的

对吧

为了能这让这个效果更明显一点呢

我们呢

咱们可以怎么做呢

在这加一个断点

加一个断点

然后呢

我们来启动一下

看看当项目启动的时候呢

我们这个run方法能不能正常运行

好

然后呢

在这来debug方式来启动

好

大家可以看到

我们现在这个断点已经过来了

对吧

那也就是说

我们在项目启动完成之后啊

那么这个方法就会执行了

好

然后呢

咱们来看一下啊

我们当前这个

scatter的对象是不是也已经给我们这个注入进来了

已经注入进来了

包括这个Mapper呢

在这也已经注入了

它其实是个代理对象

对吧

这个代理对象

好

没问题

然后呢

我们可以往下走一下

看一下啊

往下走一步

走

好

然后接下来呢

通过Mapper是不是来查我们这个

刚才看到的那个数据表

查应该是有很多条数据啊

看一共有多少条

查上来了38条数据

38条数据

这说明什么呢

说明我们这个表里边呢

应该有38条记录对吧

38条记录

好

然后呢

它已经全查上来了

查上来之后呢

把它封装成了什么呢

每一条记录呢

是封装成了这么一个

Scaler Job Entity

这么一个实体类

好

你看

大概看一下啊

它都已经封装好了

对吧

这里边有这个什么呢

Bin Name啊

还有种Parameters啊

包括还有一个Con表达式

对吧

还有这个状态啊

还有EUID啊

等等这些

好

然后接下来呢

我们先来看啊

往下走一步

走

好

便利出来第一个

第一个呢

就是我们这条记录

你看

ID呢是10

对吧

然后呢

这是Bin Name

然后呢

这是Parameter

这是Con

这是我们的Remark

是吧

定时任务测试

好

然后接下来呢

我们调用这个工具类呢

来获得这个什么呢

Con Trigger

其实这个地方呢

它应该是能够获取到的

是因为我以前已经测试过了

所以这个

呃

这个什么呢

触发器对象

你看它不是空

对吧

它不是空

就是因为我们

我以前呢

用过这条测试数据

咱们一会儿呢

可以造一条新的测试数据

啊

前后对比一下

你就能看到区别了

现在这个呢

你看它盖得出来之后呢

它不是空

说明什么呢

说明在我们前面

这个

靠

这里边

有它相应的这个定时任务

有触发器

相关的信息

因为我已经创建过了

对吧

所以说呢

这个地方它盖得出来之后呢

获取出来之后呢

不是空

不是空的话呢

它就会执行什么else这个分支

对吧

执行else这个分支

好

然后呢

我们可以在这儿加一个断点

别给它放走

然后看下一个

走

好

你看是不是又过来一个

这个呢

是不是便利第二次了

便利第二次呢

这应该就是下一条数据了

下一条数据

你看

这个ID呢

就是这一串

对吧

然后这是它那个coin expression

但是这些呢

因为我们前面呢

都已经这个创建过了

所以你看

这个

它全都是进的else这个分支

好

全都是进的else这个分支

走

你看又过来一个

这是第三个

好

然后呢

再来放行

好

这是第四个

一共呢

是一共是有多少个呢

38个对吧

刚才看到了38条记录

好

然后呢

我们直接啊

把这个断点去掉啊

咱们直接走

让它放过去

放过去之后呢

我们相当于这些

这个定时任务呢

就已经动态创建了

对吧

就已经动态创建了

然后呢

我们看一下控制台

注意看控制台

这块呢

应该是由于数据的问题啊

可能是我这个删除数据

原先的数据有问题

咱们不用管它

然后呢

你看这边

定时任务是不是已经开始执行了

任务的ID是10

这说明是哪条数据呢

就是我们刚才

这个

ID是10的

这是我们手动添加的这条数据

OK

然后呢

它是每个什么呢

5秒钟触发一次

你看每隔5秒触发一次

稍等一下

你看它是不是又触发

然后呢

你看上一次这个触发呢

你看这是20

然后25

就是每隔5秒触发一次

就是30

这个呢

这是咱们测试了一下什么呢

因为这些数据呢

它都已经这个创建过了

对吧

已经创建过了

所以说呢

它全都是走的else

这个分支

一会儿呢

我们可以再来添加一条新的数据

让它走eve这个分支

这个呢

就是我们测试了一下

当我们这个项目在启动的时候呢

这个类呢

确实是能够执行到的

对吧

执行这个run方法

然后它所执行的这个逻辑就是什么呢

就是从我们刚才看到的

这个定时任务这个表里边

把所有的数据都查出来

然后呢

根据这个什么呢

触发器对象是否为空

来确定什么呢

当前那个定时任务

是否已经创建过来的呢

对吧

如果等于空

说明那个定时任务还没有动态创建

这个时候呢

它就调用这个方法

然后在这个方法里边呢

这些代码

这就是我们动态创建一个定时任务

对吧

那么这个代码

咱们前面都讲过了

那么如果说

如果说它走的是else这个分支

这就说明我们这个定时任务已经存在了

这个时候呢

我们就更新它就可以了

这是咱们测试了一下

是没有问题的

然后一会儿呢

我们可以来测试

添加一条新的数据

咱们再来测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的技术课程，具体讲解了如何在 Spring Boot 项目中使用 Quartz 定时任务框架来初始化和管理定时任务。核心内容是演示 `DispatchCommandLineRunner` 类的 `run` 方法，该方法负责从数据库中查询所有定时任务配置，并根据每个任务的触发器（CronTrigger）是否存在，来决定是创建新任务还是更新现有任务。视频通过在 IntelliJ IDEA 中逐步调试和运行代码，展示了从数据查询、触发器获取到任务创建/更新的完整流程，并在控制台中观察了任务调度器的启动日志。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下时间点是根据画面内容和逻辑顺序进行的合理推断：

*   **00:00 - 00:05**: 开场，展示项目结构和当前讲解的章节“3.3.3 初始化定时任务”。
*   **00:05 - 00:15**: 展示 `executeInternal` 方法的代码，用于在定时任务执行时打印日志。
*   **00:15 - 00:30**: 展示 `DispatchCommandLineRunner` 类的完整代码结构和注释，说明其作用是项目启动时初始化定时任务。
*   **00:30 - 00:45**: 进入 `run` 方法的代码，开始讲解核心逻辑。
*   **00:45 - 01:00**: 代码执行，查询数据库中的 `schedule_job` 表，获取所有任务实体。
*   **01:00 - 01:15**: 遍历任务列表，获取每个任务的触发器对象。
*   **01:15 - 01:30**: 判断触发器是否为空，如果为空则调用 `createScheduleJob` 方法创建新任务。
*   **01:30 - 01:45**: 如果触发器不为空，则调用 `updateScheduleJob` 方法更新现有任务。
*   **01:45 - 02:00**: 运行程序，观察控制台日志，确认任务调度器已成功启动并处理了所有任务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **章节导航**: 展示了项目结构和当前章节“3.3.3 初始化定时任务”。
    *   **数据模型图**: 展示了 Quartz 的核心数据表结构，包括 `QRTZ_SIMPLE_TRIGGERS`, `QRTZ_CALENDARS`, `QRTZ_LOCKS` 等，用于说明定时任务的存储方式。
    *   **系统界面截图**: 展示了“智能调度服务”的后台管理界面，说明了定时任务可以通过定时触发或人工干预执行。

*   **代码**:
    *   **`executeInternal` 方法**:
        ```java
        protected void executeInternal(JobExecutionContext context) {
            ScheduleJobEntity scheduleJob = (ScheduleJobEntity) context.getMergedJobDataMap().get(ScheduleUtils.JOB_PARAM_KEY);
            System.out.println(new Date() + " 定时任务开始执行...定时任务id：" + scheduleJob.getId());
        }
        ```
    *   **`DispatchCommandLineRunner` 类**:
        ```java
        package com.itehima.pinda.init;
        import com.itehima.pinda.entity.ScheduleJobEntity;
        import com.itehima.pinda.mapper.ScheduleJobMapper;
        import com.itehima.pinda.utils.ScheduleUtils;
        import lombok.extern.slf4j.Slf4j;
        import org.quartz.CronTrigger;
        import org.quartz.Scheduler;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.boot.CommandLineRunner;
        import org.springframework.stereotype.Component;
        import java.util.List;
        @Slf4j
        @Component
        public class DispatchCommandLineRunner implements CommandLineRunner {
            @Autowired
            private Scheduler scheduler;
            @Autowired
            private ScheduleJobMapper scheduleJobMapper;
            @Override
            public void run(String... args) throws Exception {
                log.info("开始进行定时任务初始化...");
                //查询定时任务表schedule_job中所有的数据
                List<ScheduleJobEntity> list = scheduleJobMapper.selectList(queryWrapper(null));
                for (ScheduleJobEntity scheduleJobEntity : list) {
                    //获得触发器对象
                    CronTrigger cronTrigger = ScheduleUtils.getCronTrigger(scheduler, scheduleJobEntity.getId());
                    if(cronTrigger == null) {
                        //触发器对象为空，说明对应的定时任务还没有创建
                        ScheduleUtils.createScheduleJob(scheduler, scheduleJobEntity);
                    }else{
                        //触发器对象不为空，说明对应的定时任务已经存在了，此时只需要更新
                        ScheduleUtils.updateScheduleJob(scheduler, scheduleJobEntity);
                    }
                }
            }
        }
        ```
    *   **`ScheduleUtils` 工具类**:
        *   `getCronTrigger(Scheduler scheduler, Long jobId)`: 获取指定任务的触发器。
        *   `createScheduleJob(Scheduler scheduler, ScheduleJobEntity job)`: 创建新的定时任务。
        *   `updateScheduleJob(Scheduler scheduler, ScheduleJobEntity job)`: 更新已有的定时任务。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与章节定位**
    *   **描述**: 视频开头展示了项目的整体结构和当前讲解的章节“3.3.3 初始化定时任务”，帮助观众定位学习内容。

*   **场景二：`executeInternal` 方法演示**
    *   **描述**: 展示了 `executeInternal` 方法的代码，用于在定时任务执行时打印日志，说明了定时任务的执行机制。

*   **场景三：`DispatchCommandLineRunner` 类核心逻辑演示**
    *   **描述**: 重点演示了 `run` 方法的核心逻辑。首先，通过 `scheduleJobMapper.selectList` 查询数据库中的所有定时任务配置。然后，遍历任务列表，调用 `ScheduleUtils.getCronTrigger` 获取每个任务的触发器对象。根据触发器对象是否为空，决定是调用 `createScheduleJob` 创建新任务，还是调用 `updateScheduleJob` 更新现有任务。

*   **场景四：程序运行与日志观察**
    *   **描述**: 在 IntelliJ IDEA 中运行程序，观察控制台日志。日志显示了任务调度器成功启动，并处理了所有任务，验证了代码的正确性。

*   **场景五：异常处理演示（可选）**
    *   **描述**: 在某个特定条件下（如触发器不存在），程序会抛出 `JobPersistenceException` 异常，日志中会显示具体的错误信息，如“Couldn't retrieve trigger: No record found for selection of Trigger with key: 'DEFAULT_TASK_10'”。这展示了在实际开发中可能遇到的问题和异常处理的重要性。

---
