# 32-智能调度服务（实现过程_订单分类_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢咱们继续来看我们智能调度服务

刚才呢我们是测试了一下

就是我们编写完了这个dispatch task这个类对吧

这个类呢咱们已经写完了

并且在这里边提供了一个run方法

然后这个方法呢是在哪调用的呢

是不是在我们这个定时任务这个类这个地方对吧

通过反射这种方式来调用的这个run方法

好然后呢我们也测试通过了

也就是说我们整个流程是可以跑通的

没有问题

好那接下来呢我们就需要来看一下

我们当前这个run方法

前面我们也说了

这个方法呢主要就是做智能调度对吧

做智能调度

然后真正在写代码之前呢

我们需要再来回顾一下

前面章节当中啊

我们已经提到了智能调度呢

需要处理的流程是这个样子的

首先是订单分类对吧

然后是路线规划

归好路线之后呢来创建运输任务

然后呢规划车次车辆对吧

最后呢来创建司机的作业

对吧

运输作业

好整个流程是这个样子的

那么由于整个这个处理流程呢

非常复杂

那么代码量呢也是比较多的啊

这都是几千行的代码

所以说呢需要按照什么呢

处理流程进行功能的抽取

还有封装

所以我们订单分类啊

什么路线规划等等这些环节

那么就不可能把所有的代码

全都写到一个run方法当中

如果全都写到这一个方法当中

那么我们这个方法就太复杂了

那怎么办呢

我们会根据这个流程处理的流程

这些关键的阶段呢

封装成一个一个的service

然后每一个service呢

来处理其中的某一个阶段

大家可以来看一下

我们具体这个类和接口的设计是这样的

首先呢定义这么一个接口

iTaskOrderClassifiedService

这是订单分类的service接口

好

然后在这个接口下边呢

有一个实现类对吧

你看在它的基础上

mpl

那么这就是订单分类的实现类

这个实现类里边主要处理的

就是订单分类的核心逻辑

然后呢

接下来有这么一个service接口

对吧

这个就是路线规划的

然后对应的肯定也有实现类

实现什么呢

路线规划相关的

然后还有什么呢

运输任务的

对吧

还有这个什么规划车次车量的

这些

所以说呢

我们这个地方呢

还是由于代码

它的复杂程度比较高

对吧

所以说呢

还是需要进行类的设计

所以我们会抽取出来这么多的接口

包括实现类

对吧

那首先呢

我们先来看第一个阶段呢

就是我们这个订单分类

好

那么订单分类的话呢

咱们是不是需要来创建这么一个接口

叫做iTaskOtherServiceClassified

对吧

OtherClassifiedService

好

你看这个地方呢

我们也说了订单分类

对吧

好

咱们呢

在service这个包下边来创建这个service接口

好

把这些呢

全都关上

然后呢

在我们service这个包下边来创建一个接口

这个是interface

对吧

这个呢

主要处理的就是什么呢

处理的就是我们这个

处理我们这个订单分类

service接口

好

然后这个接口里边呢

只需要声明一个方法就可以了

这个方法名呢

我们统一的都叫什么呢

都叫execute的方法

啊

就叫execute的方法

就是执行

对吧

好

然后呢

我们把这个方法呢

直接考过来

这个方法呢

咱们来看一下

它传进来的这个参数

传进来的参数是这个

agency id

这个指的就是什么呢

就是我们这个机构的id

这个是机构id

在这来写一下

那这个机构具体是哪个机构呢

大家还记得吧

我们前面也一直在强调

那么针对每一个网点

或者是网点的网点呢

或者是转运中心

是不是都会有自己对应的一个

这个定时任务

对吧

所以说呢

这块呢

传的就是我们当前

自己的这个网点的这个id

那这样的话呢

它在进行这个订单分类的时候呢

只是针对自己网点的这些订单

来进行分类

对吧

所以啊

这个传进来的是机构id

指的就是我们的这个网点

或者是什么呢

转运中心

对吧

转运中心

对吧

中心的中心的id

然后第二个呢

是job id

对吧

job id呢

这就是我们这个定时任务的id

定时任务id

这个呢

是不是就是我们这个日志啊

日志的id

而这些的话呢

我们其实都是可以获取到的

那具体怎么获取到呢

咱们可以顺着这个代码呢

来梳理一下这个过程

那么你看

我们的定时任务呢

那个类呢

是在这儿呢

定时任务类是不是在这儿

当它触发的时候呢

是不是就会执行我们这个execute internal

这个方法

对吧

并且呢

我们是不是通过这个context

上下文对象

可以获得什么呢

可以获得我们当时在创建这个定时任务的时候

是不是放进来的一个对象

这个对象呢

就是我们这么一个实体

schedule job entity

对吧

而这个实体里边

这些属性呢

对应的就是我们这个

这个表里面的字段

而这里边是不是就有id

对吧

这个id具体的值呢

其实就来自于什么呢

就来自于咱们这个表

不是这边啊

应该是我们dispatch

应该是这个对吧

这个表的主件值

所以说呢

他们是有这个对应关系

那这样的话呢

我们是不是就把这个entity对象给获得到了

获得了之后呢

我就可以通过它getid

是不是获得主件值

对吧

然后呢

我们刚才看到除了它之外呢

是不是还有什么呢

还有一个agency id

而这个agency id

注意不是随便来的

它对应的是谁呢

它对应的就是我们所设置的那个business id

所以你看我们这边

这个地方是不是就可以调了

这个是获得business id

这个叫做业务id

对吧

业务id呢

传的就是什么呢

机构id

你看我们这个表里边

是不是有一个business id

注意看

我们现在是自己造的这两条数据

对吧

是为了方便测试啊

随便写了个123

实际上呢

到时候我们真实的数据呢

应该这个这个id不是随便来的

它对应的是谁呢

它对应的就是我们组织机构的id

而这个id的话

而这个id的话是从哪来的呢

它其实是来自于我们这个pdbase

对吧

来自于pdbase这个数据库里边

那个组织机构

你看我们这里边是不是有个

应该不是pdbase

应该是pdaus

这边

因为我们这边分的这个库呢

比较多啊

分的库比较多

组织机构是在这儿呢

它对应的其实是什么呢

是这个表里面的某个逐渐值

是这样的

你看这是我们组织机构

在这边

你看是不是有各种网点啦

什么转运中心呢等等

那么存储的是它的这个id的值

是这么一个对应关系啊

也就是说我们这个business id呢

也是可以获取到的

对吧

也是可以获取到的

就是通过这个实体get business id

对吧

然后还有一个是什么呢

还有一个就是我们这个log id

对吧

这个日志id呢

那就更简单了

是不是对应的

就是我们创建出来的这个

这不是一个log实体吗

对吧

在这儿我们是不是已经生成它这个id了

所以说我们把这个log id给它传进去

把这个log id

在哪儿呢

这儿对吧

log id传进去

所以说这些参数呢

都已经传到哪儿了

还调用到我们这个

run方法

而这个run方法呢

对应的就是咱们

task

这个dispatch task

这边是不是已经传过来了

对吧

已经传过来了

所以说呢

这些参数呢

我们是都能够获取到的

都能够获取到

好

那这样的话

在我们run方法这个地方呢

我是不是就可以干什么呢

把咱们这个service给注入一下

把service注入一下

然后呢

调用这个execute的方法

对吧

而这些参数刚才我们也分析了

都是能够获取到的

但是一会儿呢

我们再去写实现类啊

咱们先怎么做呢

先把我们这个service把它注入一下

private

这个接口呢

叫做什么呢

叫做itask

task order classify service

对吧

然后呢

在这儿直接通过autoware的

就可以注入了

因为我们当前这个类呢

也是交给sprint容器管理的

所以说直接这样呢

就可以注入进来了

注进来之后呢

我们是不是就可以去调什么呢

就可以去调这个方法

直接调用它这个什么呢

execute的方法

对吧

然后呢

这个机构ID的话

对应的是谁呢

是不是就是我们的

businessID

然后第二个呢

是不是就是这个jobID

而这个jobID呢

就是我们上面jobID

然后还有一个是logID

这个也都是对应的

logID

OK

你看

然后呢

它这是有返回值的啊

有返回值

这个返回值呢

比较特殊

这个返回值

我们来看一下

现在来看一下

我们是怎么做的

你看这个execute的方法

它的返回值

首先是个list集合

对吧

list集合

然后集合里边封装的是这种实体

这是一个DTO

你看这是一个DTO

然后呢

在这里边什么有ID

这是主件不用说了

还有key

然后这个key的话呢

我们后边会重点分析一下

这个key其实代表的就是什么呢

就是由我们这几个维度构成的

就是由这几个维度构成的

分别是什么呢

分别是我们这个start agency ID

是不是起始机构

终止机构

还有当前机构

但是都是取的ID对吧

然后给它拼到一块

然后我们再来看一下

这个key

然后呢

我们这个地方需要注意

咱们是不是要进行订单分类

对吧

进行订单分类

所以这块呢

你看我们是按照什么分呢

start还有end

对吧

存储的这些参数

最终你分成了多少类呢

那么每一类

其实对应的就是这么一个对象

每一类对应的就是这么一个对象

而你这一类里边

具体包含了哪些

这个具体的订单呢

你看

在这是不是有个others

这就是原始的订单集合

这就说明这些订单被分为了一类

而这些订单为什么被分为一类呢

就是因为他们这些start还有end

这两个包括这个拼一块

他们是一个什么呢

是相同的

说明他们这个起始机构

目的机构对吧

那么都是相同的

所以这些订单会被分成一类

这就是我们当前这个DTO

它的一个封装

这是咱们的订单

把这个返回结果呢

来简单说一下

好

那么这是咱们当前这个订单分类啊

所需要的这个service接口

就已经写完了

一会儿呢

我们再来编写它的实现类

看看具体这个实现类啊

是如何实现订单分类

它的逻辑的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程主要讲解了一个基于 Spring Boot 的“智能调度”系统的核心实现。该系统通过一个名为 `DispatchTask` 的调度任务类，利用 Java 反射机制动态调用业务服务（如订单分类服务 `ITaskOrderClassifyService`），从而实现任务的解耦与灵活执行。课程内容涵盖了从任务定义、服务接口设计、反射调用实现到数据库表结构的分析，重点展示了如何通过代码层面的动态调用，将调度逻辑与具体业务逻辑分离，提升了系统的可维护性和扩展性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和 `DispatchTask` 类的初始代码。
*   **00:05 - 00:15**: 讲解 `DispatchTask` 类的注解 `@Component("dispatchTask")` 和 `@Slf4j`，并展示其 `run` 方法的参数和日志输出。
*   **00:15 - 00:25**: 切换到 `ITaskOrderClassifyService` 接口，介绍其作为业务服务的定义。
*   **00:25 - 00:40**: 展示 `ScheduleJob` 类中的核心逻辑，重点讲解通过反射调用目标对象的 `run` 方法。
*   **00:40 - 00:50**: 切换到 Navicat 数据库工具，展示 `pd_dispatch` 数据库中的相关表结构，如 `schedule_job`、`pd_order_classify` 等。
*   **00:50 - 01:00**: 在 Navicat 中查看 `pd_auth` 数据库表，展示组织机构（`pd_core_org`）的数据。
*   **01:00 - 01:15**: 回到 IntelliJ IDEA，展示 `DispatchTask` 类中通过 `@Autowired` 注入 `ITaskOrderClassifyService` 服务。
*   **01:15 - 01:25**: 展示 `DispatchTask` 类中调用 `taskOrderClassifyService.execute(...)` 方法的代码。
*   **01:25 - 01:35**: 展示 `ITaskOrderClassifyService` 接口的详细定义，包括其方法签名和参数。
*   **01:35 - 01:45**: 展示 `DispatchTask` 类中用于判断是否为新订单的 `isNew` 方法。
*   **01:45 - 01:55**: 展示 `OrderClassifyGroupDTO` 数据传输对象（DTO）的定义。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1: `DispatchTask.java` - 任务执行方法**
    ```java
    public void run(String businessId, String params, String jobId, String logId) {
        Log.info("智能调度正在执行，参数为：{},{},{},{}", businessId, params, jobId, logId);
    }
    ```
    *   该方法是调度任务的核心执行入口，接收四个参数并记录日志。

*   **代码片段 2: `ScheduleJob.java` - 反射调用核心逻辑**
    ```java
    try {
        // 通过反射调用目标对象，在目标对象中封装智能调度核心逻辑
        Object target = SpringContextUtils.getBean(scheduleJob.getBeanName());
        Method method = target.getClass().getDeclaredMethod("run", String.class, String.class, String.class, String.class);
        method.invoke(target, scheduleJob.getBusinessId(), scheduleJob.getParams(), scheduleJob.getJobId(), scheduleJob.getLogId());
    } catch (Exception ex) {
        // 处理异常
    }
    ```
    *   该代码通过 Spring 的 `getBean` 方法获取目标对象，然后通过 `getDeclaredMethod` 获取 `run` 方法，并使用 `invoke` 方法动态调用，实现了任务的解耦。

*   **代码片段 3: `DispatchTask.java` - 服务注入与调用**
    ```java
    @Autowired
    private ITaskOrderClassifyService taskOrderClassifyService;

    public void run(String businessId, String params, String jobId, String logId) {
        taskOrderClassifyService.execute(businessId, jobId, logId);
    }
    ```
    *   通过 `@Autowired` 注解将业务服务注入到调度任务中，然后在 `run` 方法中调用其 `execute` 方法。

*   **代码片段 4: `ITaskOrderClassifyService.java` - 服务接口定义**
    ```java
    public interface ITaskOrderClassifyService {
        List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId);
    }
    ```
    *   定义了业务服务的接口，其 `execute` 方法接收机构ID、任务ID和日志ID作为参数，并返回一个订单分组的列表。

*   **代码片段 5: `DispatchTask.java` - 判断新订单**
    ```java
    public boolean isNew() {
        return this.startAgencyId.equals(this.currentAgencyId);
    }
    ```
    *   该方法用于判断当前订单是否为新订单，逻辑是判断起始机构ID与当前机构ID是否相等。

*   **数据库表结构 (Navicat)**:
    *   `schedule_job`: 存储调度任务的配置信息，如任务ID、业务ID、参数、日志ID等。
    *   `pd_order_classify`: 存储订单分类的详细信息。
    *   `pd_core_org`: 存储组织机构信息，如机构ID、名称、省份ID、城市ID等。

---

### 4) 关键场景与演示描述

*   **场景 1: 任务定义与执行**
    *   **描述**: 教师首先在 IntelliJ IDEA 中打开 `DispatchTask.java` 文件，展示了一个简单的 `run` 方法。该方法接收四个参数（业务ID、参数、任务ID、日志ID），并输出日志信息。这表明该任务是一个通用的调度执行器。

*   **场景 2: 反射调用机制演示**
    *   **描述**: 教师切换到 `ScheduleJob.java` 文件，展示其核心逻辑。通过 `SpringContextUtils.getBean` 获取目标对象，然后通过 `getDeclaredMethod` 获取 `run` 方法，并使用 `invoke` 方法动态调用。这演示了如何通过反射机制动态执行不同的任务，实现了任务与业务逻辑的解耦。

*   **场景 3: 服务注入与调用**
    *   **描述**: 教师在 `DispatchTask.java` 中展示了 `@Autowired` 注解的使用，将 `ITaskOrderClassifyService` 服务注入到调度任务中。然后在 `run` 方法中调用 `taskOrderClassifyService.execute(...)` 方法。这演示了 Spring 的依赖注入机制如何将业务逻辑与调度逻辑结合。

*   **场景 4: 数据库表结构分析**
    *   **描述**: 教师切换到 Navicat 数据库工具，展示 `pd_dispatch` 数据库中的表结构。重点查看了 `schedule_job` 表，该表用于存储调度任务的配置信息。同时，也查看了 `pd_core_org` 表，用于存储组织机构信息，这为订单分类提供了数据支持。

*   **场景 5: 业务逻辑接口定义**
    *   **描述**: 教师展示了 `ITaskOrderClassifyService.java` 接口的定义，其中 `execute` 方法的签名是 `List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId)`。这表明业务服务需要接收机构ID、任务ID和日志ID，并返回一个订单分组的列表，为调度任务提供了具体的业务逻辑。

通过以上场景，课程完整地演示了从任务定义、反射调用、服务注入、数据库支持到业务接口定义的整个智能调度系统的实现过程。
