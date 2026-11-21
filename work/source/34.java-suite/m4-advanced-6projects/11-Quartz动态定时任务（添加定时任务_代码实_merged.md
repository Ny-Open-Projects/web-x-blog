# 11-Quartz动态定时任务（添加定时任务_代码实 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们Cross动态定时任务

刚才我们是把环境已经搭建好了

这个环境搭建主要就是从这么几个方面

一个是什么呢

我们需要来创建一个新的Mainframe工厂

并且把坐标是不是来导一下

然后接下来就是我们Spring Boot配置文件

来配置一下

然后再往下就是关于我们Config

就是我们的配置类

然后这个配置类里边主要就是创建这么一个对象

就是Scheduler Factory Bin

通过这个工厂Bin

我们最终其实创建的是这个

叫做Scheduler这个对象

这个前面我们在入门案例里边

是不是也是创建出来的

当然了当时我们是通过什么

是通过这个

咱们来看一下

是通过这个叫做STD Scheduler Factory

然后直接调用这个Get Default Scheduler

然后获得这么一个调度器对象

然后现在我们是通过这种配置类的这种方式来创建

这就是我们一般

在这个项目里面

在入门案例里边跟我们真正项目当中不同的地方

因为在我们Spring Boot项目里面

咱们肯定是通过这种配置类的方式来创建对象

对吧

然后创建的时候

需要指定一些配置参数

最终把这个工厂对象创建出来

然后就是关于我们SWAG文档的这个配置类

这个就不再多说了

然后我们是不是又创建了一个自定义的Job

对吧

还叫HelloJob

然后这个类的话

没有直接去实现那个Job接口

而是继承了这个副类

对吧

其实也是相当于是间接的实现了那个Job接口

然后最后呢

是不是来创建我们这个启动类

还有这个Controller

好

那接下来呢

我们就来看下一个呢

就是实现定时任务

先来看第一个呢

就是什么呢

动态的来添加一个定时任务

那这样的话呢

我们就需要在咱们这个CauseController当中呢

来创建一个Save方法

在这个地方

咱们继续来编写咱们这个Controller

这个它的作用是什么呢

动态来添加一个定时任务

然后Public

返回值的话呢

我们就返回一个死君字符串就可以了

然后呢叫做Save对吧

Save

先来一个retain一个now

这个方法呢

咱们给它加一个叫做post mapping

然后呢通过什么路径能访问到它呢

来看一下

就跟这个保持一致吧

post mapping

它这没有写

那没有写的话呢

那是不是应该就是直接

使用我们上面这个就可以了

然后这块呢就空着

只要是一个post方式请求

这样呢就能请求到我们这个Save方法

对吧

然后呢我们可以给它加一个API operation

但这个呢不是必须的

如果不加这个下面这个註解的话呢

它其实就会默认给我们生成一个

就是使用这个方法名对吧

这个就是动态添加一个定时任务

动态添加定时任务

好

然后这个方法呢

我们给它来一个参数啊

就是这么两个参数

一个是什么的BIZ ID

这肯定是跟我们业务相关的

还有一个就是什么呢

这个coin expression

就是我们动态添加出来的这个任务啊

咱们通过这种coin表达式

这种方式来指定什么呢

它这个新添加的这个任务啊

它的触发的时间

它的触发的时间

好

那这样的话呢我们就需要来看啊

如何做到这个任务呢

用这个动态来添加一个定时任务呢

这个写法的话呢

其实跟咱们前面那个入门案例呢

是非常类似的

就是首先什么呢

我们先创建这个任务对象

也就是我们那个job detail

所以说我们在这呢

使用这个什么呢

job detail

它这里边应该有一个那个什么builder对吧

使用那个构建器啊

叫什么名字来着

叫做job builder

job builder

点什么呢

这里边是不是有个new job

然后在这指定

hello job.class对吧

然后呢接下来我们是不是来给它指定一个什么呢

with identity

是不是设置唯一的一个ID对吧

这个唯一的ID的话呢

我们就可以使用什么呢

这个bizid

bizid

这就是我们传过来的这么一个参数对吧

通过调用端

给我们传过来这个参数bizid

所以我们一定要保证这个bizid呢

应该是一个唯一的

然后接下来呢

我们是不是调用这个build的方法

这样的话呢

咱们就创建出来了一个job detail对象

这是我们的任务实力对吧

创建我们的任务实力对象

好

创建好它之后呢

接下来我们要创建谁啊

是不是要创建我们那个触发器

大家还有印象吧

要创建触发器对象

而这个触发器的话呢

我们使用的是什么呢

叫做trigger builder对吧

trigger builder

使用它来创建一个触发器

new一个trigger

然后呢

需要来指定什么呢

指定with schedule

是不是来指定我们这个任务

它的这个调度策略对吧

调度规则

好

咱们一会儿再去完善它

然后呢

我们是不是调用这个build的方法

这样的话呢

就可以把触发器对象

是不是给创建好

好

这个呢

是创建我们这个

创建触发器对象

好

创建好了之后啊

咱们是不是直接啊

让这个触发器

还有我们这个触发器

创建我们这个触发器对象

然后呢

我们这个job detail

就任务实例进行一个关联就可以了

进行关联

怎么关联呢

是不是就是使用这个scheduler

所以我们在这呢

直接调用它的什么呢

schedule job这个方法

然后把这个job detail

还有trigger

传进去

就可以了

这个是关联什么呢

关联我们这个任务实例和什么呢

触发器对吧

触发器对象

好

它这个地方呢

需要抛异常对吧

咱们就来看看

我们这呢

就简单来throw一下

往外抛一下

就可以了

最后呢

我们是不是来返回一下

直接返回一个ok就可以了

返回一个ok

ok

但是这呢

你看它是不是还抱着错呢

因为我们这个地方呢

是不是需要来指定一个什么呢

指定一个

它的这个叫做scheduler builder

scheduler builder对象

然后这个地方呢

我们使用的是这种con表达式的

传过来的是con表达式

所以说呢

我们在这呢

需要使用一个叫做con scheduler builder

好

点什么呢

来设置这个

把它传过来这个参数

传进去对吧

这样的话呢

我们就得到了一个con scheduler builder对象

然后呢

把它放在这

就可以了

那么这个地方呢

就是我们使用的传过来的

比如说我们页面上对吧

我提供一个页面

然后呢

来输入这么一个con表达式

最终呢调用到我们save方法

这样的话呢

我就动态的来添加了这么一个

动态的来添加了一个

定时任务

并且呢

我们为了能够区分出来

不同的定时任务

咱们在这呢

需要干什么呢

给它来设置一些参数

就是每一个定时任务

都让它是唯一的

都让它是唯一的

那这个怎么做呢

大家还记得吧

我们前面是不是讲过

有一个那个什么呢

job datamap对吧

所以说我在这就可以

直接使用这个job detail.get

job datamap.put

我给它放进去

然后呢

这个key的话呢

就叫做biz

biz.put

biz.put

biz.id

而这个value的话呢

就是我传过来的这个bizid

来看一下咱们这个讲义啊

讲义上我是不是就是这么写的

对吧

然后呢

这个key的话叫做bizid

然后具体的值

每一个job是不是都是唯一的

这就要求我们页面呢

是不是需要做一定的控制

对吧

也就是说前面需要做一个校验

保证我们传过来的bizid呢

是一个唯一的值

好

那么到这儿的话呢

咱们这个代码呢

其实就已经写完了

这是我们动态的来添加的

一个定时任务

其实你会发现

整体这个代码呢

跟我们前面那个入门案例呢

其实没有什么区别

对吧

没有什么区别

无非就是这块这个scatter了呢

它其实是通过autoware的这种方式注入的

并且呢

在我们这个config这个地方

还指定了是什么呢

咱们是不是指定了这个任务存储

使用的是这个gdbc这种方式

也就是把它持续化到数据库了

这样的话呢

即使我们服务重启

我们设置的这些任务信息呢

都是存在的

好

那接下来呢

我们就可以啊

一会儿呢

可以这是代码写完了

一会儿呢

我们可以来测试一下

这块的报错呢

是因为什么呢

它是

它说there is more than one bit of scatter type

这块呢

可以先不用管它

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于在 Spring Boot 项目中集成 Quartz 定时任务框架的实战教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建 Maven 项目、引入 Quartz 依赖、编写自定义任务类（`HelloJob`）、配置 Quartz 调度器（`SchedulerFactoryBean`），并最终在控制器（`QuartzController`）中实现一个通过 HTTP 请求动态添加定时任务的功能。核心代码展示了如何使用 `JobBuilder` 构建任务、`CronScheduleBuilder` 构建触发器，并通过 `Scheduler.schedule(jobDetail, trigger)` 方法将两者关联并注册到调度器中。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 0: 项目初始化与依赖引入 (00:00 - 00:05)**
    *   展示了创建 Maven 工程并添加 Quartz 核心库（`quartz`）和 Job 库（`quartz-jobs`）的依赖配置。

*   **章节 1: 自定义任务类 (00:05 - 00:10)**
    *   创建 `HelloJob` 类，实现 Quartz 的 `Job` 接口，用于定义具体的定时任务逻辑。

*   **章节 2: 配置调度器 (00:10 - 00:15)**
    *   通过 `SchedulerFactoryBean` 配置 Quartz 调度器，设置线程池、JobStore、集群等核心参数。

*   **章节 3: 创建控制器 (00:15 - 00:20)**
    *   创建 `QuartzController` 控制器类，使用 `@RestController` 和 `@RequestMapping` 注解。

*   **章节 4: 实现动态添加任务功能 (00:20 - 00:30)**
    *   在 `QuartzController` 中编写 `@PostMapping` 方法，接收 `bizId` 和 `cronExpression` 参数。
    *   使用 `JobBuilder` 构建 `JobDetail` 对象。
    *   使用 `CronScheduleBuilder` 构建 `CronSchedule`。
    *   使用 `TriggerBuilder` 构建 `Trigger` 对象。
    *   调用 `scheduler.schedule(jobDetail, trigger)` 方法将任务注册到调度器。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档结构

*   **左侧导航栏**：清晰地展示了课程大纲，当前章节为“第8章 智能调度服务 -> 2.3 实现定时任务 -> 2.3.1 添加定时任务”，表明这是一个系列教程的特定部分。

#### 代码关键内容

*   **Maven 依赖 (POM.xml)**：
    ```xml
    <dependency>
        <groupId>org.quartz-scheduler</groupId>
        <artifactId>quartz</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>org.quartz-scheduler</groupId>
        <artifactId>quartz-jobs</artifactId>
        <version>2.3.0</version>
    </dependency>
    ```

*   **自定义任务类 `HelloJob.java`**：
    ```java
    package cn.ictast.jobs;
    import org.quartz.Job;
    import org.quartz.JobExecutionContext;
    import org.quartz.JobExecutionException;
    import java.time.LocalDateTime;
    import java.time.format.DateTimeFormatter;
    public class HelloJob implements Job {
        @Override
        public void execute(JobExecutionContext context) throws JobExecutionException {
            // 任务执行逻辑
            System.out.println("Hello Job executed at: " + LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
        }
    }
    ```

*   **调度器配置 `SchedulerFactoryBean`**：
    ```java
    @Bean
    public SchedulerFactoryBean schedulerFactoryBean(DataSource dataSource) {
        SchedulerFactoryBean factory = new SchedulerFactoryBean();
        factory.setDataSource(dataSource);
        // 配置 Quartz 参数
        Properties prop = new Properties();
        prop.put("org.quartz.scheduler.instanceName", "witlinkedScheduler");
        prop.put("org.quartz.scheduler.instanceId", "AUTO");
        prop.put("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
        prop.put("org.quartz.threadPool.threadCount", "20");
        prop.put("org.quartz.threadPool.threadPriority", "5");
        // JobStore 配置
        prop.put("org.quartz.jobStore.class", "org.quartz.impl.jdbcjobstore.JobStoreTX");
        prop.put("org.quartz.jobStore.isClustered", "true");
        prop.put("org.quartz.jobStore.clusterCheckinInterval", "15000");
        prop.put("org.quartz.jobStore.misfireThreshold", "12000");
        prop.put("org.quartz.jobStore.tablePrefix", "QRTZ_");
        prop.put("org.quartz.jobStore.selectWithLockSQL", "SELECT ... FROM {0}LOCKS UPLOCK WHERE LOCK_NAME = ?");
        factory.setQuartzProperties(prop);
        factory.setSchedulerName("pdScheduler");
        return factory;
    }
    ```

*   **控制器 `QuartzController.java`**：
    ```java
    @RestController
    @RequestMapping("/quartz")
    public class QuartzController {
        @Autowired
        private Scheduler scheduler;
        
        @PostMapping("/add")
        @ApiOperation("添加定时任务")
        public String save(String bizId, String cronExpression) throws Exception {
            // 创建任务实例对象
            JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity(bizId).build();
            jobDetail.getJobDataMap().put("bizId", bizId);
            
            // 创建触发器对象
            CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression);
            Trigger trigger = TriggerBuilder.newTrigger().withSchedule(cronScheduleBuilder).build();
            
            // 关联任务实例和触发器对象
            scheduler.schedule(jobDetail, trigger);
            
            return "OK";
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 项目结构与依赖配置**
    *   讲师首先在 IDEA 中展示了一个名为 `quartz-test` 的 Spring Boot 项目结构。
    *   他切换到 `pom.xml` 文件，高亮显示了添加 Quartz 依赖的代码块，强调了项目启动前必须引入的库。

*   **场景 2: 创建自定义任务类**
    *   讲师在 `src/main/java` 目录下创建了一个 `cn.ictast.jobs` 包。
    *   他新建了一个 `HelloJob.java` 文件，并编写了实现 `Job` 接口的 `execute` 方法，用于定义任务的具体执行逻辑。

*   **场景 3: 配置调度器**
    *   讲师在配置类中创建了 `SchedulerFactoryBean` 的 `@Bean` 方法。
    *   他通过 `Properties` 对象配置了 Quartz 的核心参数，如线程池大小、JobStore 类型、集群模式等，并将配置设置给 `SchedulerFactoryBean`。

*   **场景 4: 编写控制器并实现动态添加任务**
    *   讲师在 `controller` 包下创建了 `QuartzController.java`。
    *   他使用 `@RestController` 和 `@RequestMapping("/quartz")` 注解定义了控制器。
    *   通过 `@Autowired` 注入 `Scheduler` 对象。
    *   他编写了 `@PostMapping("/add")` 方法，接收 `bizId` 和 `cronExpression` 参数。
    *   在方法中，他使用 `JobBuilder` 构建 `JobDetail`，并使用 `CronScheduleBuilder` 构建 `CronSchedule`，再用 `TriggerBuilder` 构建 `Trigger`。
    *   最后，他调用 `scheduler.schedule(jobDetail, trigger)` 方法将任务注册到调度器，并返回 "OK" 表示成功。

*   **场景 5: 代码调试与运行**
    *   讲师在 `QuartzController` 中的 `save` 方法中添加了 `return "OK";` 语句。
    *   他通过 IDEA 的代码提示功能，成功导入了 `org.quartz` 包下的 `JobBuilder`、`TriggerBuilder` 等类。
    *   他逐步编写了构建 `JobDetail`、`CronScheduleBuilder` 和 `Trigger` 的代码，并最终完成 `scheduler.schedule(jobDetail, trigger)` 的调用。

---

以上是根据视频画面内容进行的结构化分析，旨在帮助理解该技术教程的核心内容和实现步骤。
