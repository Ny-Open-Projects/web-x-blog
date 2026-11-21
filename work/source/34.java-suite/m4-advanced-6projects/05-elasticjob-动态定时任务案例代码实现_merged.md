# 05-elasticjob-动态定时任务案例代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们在这一块按刚才所分析的几个流程来实现一下我们的动态定时任务案例的一个实现。

好,在这一块添加一个类,这个类呢?

dynamic.dynamicconfigure.dynamicelasticjob.dynamicconfigure。

这一块就是我们的一个动态定时任务案例的配置。

那么这个配置这一块该怎么做呢?

先写个叫configuration。

写了之后,我们在这里按照刚才所说的几点去实现就可以了。

好,第一个是要注册初始化数据,配置初始化数据,配置初始化数据。

第二个是要注册初始化数据,配置初始化数据。

这是第一个,第二个。

那么第三个呢?就是动态添加定时任务案例。

第四个就是制定于任务处理过程,那这个我们可以等会儿单独去实现。

第四个是制定于任务处理过程。

就是这么几个点抓住就行了。

好,我们来开始配置一下。

第一个是初始化配置数据,那在这里写一个bin。

在这里写个public,叫zookeeper。

注意是配置configuration,zkconfiguration。

好,我们来写一下这个配置,newzookeeperconfiguration。

它里面有两个参数,注意一下。

这两个参数呢,我们讲解一下。

第一个参数。

第一个参数是我们当前zookeeper的一个参数。

我们写下一个地址。

第二个参数是什么呢?

第二个参数是,好,我们写下第二个参数。

第二个参数是当前这一块,你必须要向zookeeper注册的一个定时任务命名空间。

必须得有。

好,我们来写一下。

这个我就先随便写个假的就行了。

可以了。

等会儿呢,我们应该是在配置文件里面配置。

再把它给配置。

好,我们来写一下。

我们先把这个字注入进来才对。

好,我们这一块就直接在这里写一下。

这个是动态定时任务案例。

首先我们写个叫zk server。

把后面这个地址给拷过来。

zookeeper我们仍然用同一个zookeeper。

下面呢,写个叫做zk namespace。

随意写哈。

我们就写一个叫zk namespace。

zk namespace.

zk namespace.

zk namespace.

这开 Việt名,илась p得了。

可以了。

把这两个给注入音。

呃,两个给注入进去。

来写到这里。

privacy script。

还有privacy script。

好,这一块,这两个我们交息就喜欢了。

写个叫做Value。

把它给写进来。

那么这一块就搞定了。

把这两个呢

再给放到下面去

这个是ZooKeeper的一个地址

这个是我们当前命名空间

任务的命名空间

这一块就搞定了

接着第二个就是

把它注册到我们ZooKeeper里面去

那么注册进去呢

Public

所以这里有个ZooKeeper

叫Registry Center

Registry Center

我们写过来

留一个ZooKeeper Registry Center

在这一块呢

我们也写一个bin

好

把上面这个对象注册进去

ZK Config

写过来就行了

于是第一步第二步完成了

在这里呢

还要注意一下

它里面有一个方法

这个方法

NIT这个方法

必须要先初始化调用才行

就是你这一块注册之前

你得先调用

这个初始化方法才行

那这个时候怎么办呢

在这里添加一个Method

叫NIT Method

调用它就行了

NIT

可以了

好接着再写

注意

这一点写完了

这一点写完了

这两个是非常简单的

对吧

我们开始写第三个

第三个呢

就这一块略微有点区别

区别点就是之前

这之前这个是在这里用注册写的

现在把这个用注册写的开始写到程序里面去就行了

好

我们来写一下哈

看这一块该怎么做

这块呢

非常的简单

Public

我先写一个Void

叫addDynamicTask

添加动态的定时任务案例

那添加动态的定时任务案例呢

需要哪些参数

大家不用想

绝对是这几个

那么这几个动态任务案例的一个参数添加进来

除了这几个还有什么呢

应该还有下面这个任务

你不把任务告诉我

我哪知道执行什么任务呢

对不对

就是这个好

至于说到底有哪些参数

我们先别管

我们先把程序写出来

缺什么一会儿全部传过来就行了

好

我们开始写程序

在这一块该怎么实现呢

所以这一块有两个步骤

第一个步骤就是添加我们elasticJob

它的一个

Lite的任务作业器

第二个将

所以第二个是将

Lite的任务作业器

添加到Spring的任务启动器中

并初始化即可

就这两个步骤就行了

那么这两个步骤呢

也就是把之前这一块写死的动态传过来就OK了

好

我们来实现一下

首先这一块我们添加这个任务作业器怎么做呢

在这里有一个叫Lite

Job Configuration

LiteJob Configuration.LewBuild

这个LewBuild我们点击进去就OK了

好

我们看一下需要什么参数

叫JobType Configuration

对吧

我们点击一下JobType Configuration

Ctrl Alt加B

你看它就是用来构建Lite的一个作业器的

对不对

好

Ctrl Alt加B

这里有一个JobType Configuration

我们用的其实就是这个对象

这个对象我们看怎么用

来在这里写一下

其他的先关掉

写一下Lew一个它

Lew一个这个对象

对不对

Lew就行了

因为咱们缺的是它就Lew它了

Lew它了之后呢

这个时候还不够

因为它这里没有无参过的函数

Lew了之后

你发现它里面还要去

写对应的代码

怎么写呢

我们看一下这个原文件

Open Class Fill

再来点进来

大家看一下

在这一块

刚才是这个方法

好

我们重新来一次

点进来

再点击Open Class Fill

就这个方法

这个方法呢

第一个是Job Call Configuration

第二个是Job Call Configuration

这两个参数我给写过来

给大家讲解一下

这两个参数分别是个什么东西呢

来我简单说一下

第一个这一块Job Call Configuration

这个就是我们的Job Call

就是我们当前任务的核心配置

这就是Job Call

而另外一个Job Class呢

就是下面这个执行任务的对象的内容

这个全新的名

好

我们来整一下

看这个该怎么做

第一个是Job Configuration

直接用Job Configuration来构建就行了

New Build

最后不要忘了

点Build就OK了

这个构建这一块

就是我们相关的一些参数信息了

而这个呢

就是我们的任务对象的一个全新的名

那这个任务对象的全新的名呢

等会肯定是传过来对不对

行

我们先看这里有哪些数据

我们一点进去你就能发现

你看第一个Job Name

第二个Chrome

第三个分片数量

那因此这一块我们全能搞定了

好把这几个数据给我传过来就行了

实际第一个是Job Name

第二个是我们的什么呢

大家注意一下

好我们点进去吧

把这三个给拷贝过来

拷到这一块

全给拷过来得了

那第一个实讯是我们的任务名字

也就是我们要执行的任务命名空间

第二个是我们当前的一个执行时间的表达式

第三个是分片数量

好我们可以把这三个参数分别写进来

写到这里

好还有一个是我们的任务名字

这个写到这里

可以了

那么还差一个就是Job Class

Job Class其实就是下面这个任务对象

这个任务对象它必须要实现一个接口

Simple Job接口

所以我们这一块可以做这么一个事情

把任务的实例传过来

Simple Job写一个叫Instance

Instance

就OK了

那么现在直接去获取它的一个字兼码

点Get Name

获取它的一个字兼码

然后获取它的一个类的名字就OK了

好这是这一块

那么像这三个参数我就不用去说了

因为说的意义不大对不对

那现在这一块呢

它也只是构建了一个任务的作业器

在这一块还有一个参数

大家也要注意

这几个我们把它给格式一下

格式一下不然看起来很臃肿对吧

好New Build

这里有三个参数

三个参数呢

三个参数我觉得倒可以不用去说它

好到这一块

Build一个参数

这是第二个参数对吧

行这是第二个参数

这里还有一个参数叫做Override

等于Q

这个是什么意思呢

注意一下

在我们这里每次添加这个任务的时候

比如说我现在添加一个任务名称为A

指定的时间是15秒之后进行

那么在这15秒以内

我又添加了一个任务也叫A

那它会把之前那个任务给覆盖掉

这个Override

是这么个意思会覆盖它

行这一块一写之后我们就开始做了

我们的任务作业器Build

这个时候就拿到了我们的一个Light

对应的一个任务作业器配置

接着把这个任务作业器呢

添加到我们Spring

它里面对应的一个任务作业器启动器中

怎么做呢

Liu Spring

这里有个Job Schedule

好添加到这里来就行了

那么不要忘了

不要忘了初始化一下

Init初始化一下

至于说这里面有什么参数

我们点一下大家就明白了

第一个ES Job

其实就是当前任务实例

Instance任务实例

第二个呢是当前的一个注册信息

注册对象信息

第三个就是作业器

第四个监听器

监听器你看写了三个点点点表

表示可变参数

可变参数就是可以不写

对不对

好OK

那这一块我们就按照这里的一个要求

把这几个参数给填进来

第一个是执行的任务实例

第二个是当前这一块这个注册对象

注册对象呢

在这一块呢

这有

这是有一个叫做

Zookeeper

好把它写到这里来

Privacy

Privacy

我们写一个叫Zookeeper Center

把它给注入进来

因为你上面是不是创建了对象实例

可以注入进来的呀

对不对

写到这里

还有一个是当前的一个任务作业器

写到这里来

好

于是我们动态添加任务案例

这一块就搞定了

紧接着这个任务执行的一个

业务流程控制

这个就简单了

跟之前是一模一样的

所以这一块比较容易

我们来写一个就OK了

好

右键新建一个叫Dynamic Task

就是我们的动态任务

在这一块呢

它需要实现我们的接口

叫Simple Job

实现这个接口

里面有一个方法

这个方法呢

就是我们来添加的一个任务流程

任务处理的一个流程

好

把它给写到这里来

就可以了

好

那么我们目前这一块动态定时任务案例

就搞定了

这一块是用于实现对应的业务

好

OK

这块搞定了

咱写个Dynamic动态

对吧

好

这块搞定之后呢

我们就可以开始进行一个测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程旨在讲解如何在 Spring Boot 项目中集成并使用 ElasticJob（一个分布式调度框架）来实现动态的定时任务。讲师通过一个名为 `ElasticjobDynamicConfig` 的配置类，演示了从初始化 Zookeeper 配置、注册初始化数据、到动态添加和自定义任务处理过程的完整流程。核心内容包括配置 Zookeeper 地址和命名空间、使用 `ZookeeperRegistryCenter` 进行注册、通过 `LiteJobConfiguration` 构建任务、并最终通过 `SpringJobScheduler` 将任务注册到调度器中。整个过程强调了动态性和可扩展性，允许在运行时添加新的定时任务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 课程开场，展示项目结构，介绍本节将讲解“动态定时任务”的实现。
*   **00:04 - 00:08**: 讲解 `ElasticjobDynamicConfig` 类的结构和核心功能，列出六个主要步骤。
*   **00:09 - 00:14**: 详细讲解第一步：配置初始化的 Zookeeper 地址和命名空间，展示 `ZookeeperConfiguration` 的构造方法。
*   **00:15 - 00:20**: 讲解第二步：注册初始化数据，展示 `ZookeeperRegistryCenter` 的初始化方法。
*   **00:21 - 00:26**: 讲解第三步：动态添加定时任务案例，展示 `addDynamicTask` 方法的框架。
*   **00:27 - 00:32**: 讲解第四步：自定义任务处理过程，展示 `ElasticSimpleJob` 的定义和 `SimpleJobConfiguration` 的使用。
*   **00:33 - 00:38**: 讲解第五步：动态添加定时任务实现，展示如何使用 `LiteJobConfiguration` 构建任务。
*   **00:39 - 00:44**: 讲解第六步：将任务添加到 Spring 的任务调度器中，展示 `SpringJobScheduler` 的初始化方法。
*   **00:45 - 00:50**: 总结并强调动态任务的灵活性和可扩展性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

*   **核心步骤清单**：在屏幕右侧始终显示一个红色边框的文本框，列出了六个关键步骤：
    1.  配置初始化的 Zookeeper 地址。
    2.  配置的定时任务命名空间 (不一定使用)。
    3.  注册初始化数据。
    4.  监听器 -> 任务执行前后监听 (可有可无)。
    5.  动态添加定时任务实现。
    6.  自定义任务处理过程 -> 实现 `SimpleJob`。

#### 代码

*   **`ElasticjobDynamicConfig.java`** (核心配置类)
    *   **`@Configuration`**: 标注该类为 Spring 配置类。
    *   **`@Bean` `ZookeeperConfiguration zkConfig()`**: 创建并返回一个 `ZookeeperConfiguration` 实例，用于配置 Zookeeper 地址和命名空间。
    *   **`@Bean(initMethod = "init")` `ZookeeperRegistryCenter registryCenter(...)`**: 创建并返回一个 `ZookeeperRegistryCenter` 实例，用于注册初始化数据。
    *   **`public void addDynamicTask(...)`**: 动态添加定时任务的核心方法。
        *   **`LiteJobConfiguration.newBuilder(...)`**: 创建 `LiteJobConfiguration` 的构建器。
        *   **`JobCoreConfiguration.newBuilder(...)`**: 创建 `JobCoreConfiguration` 的构建器，用于配置任务的核心属性。
        *   **`.overwrite(true).build()`**: 设置任务覆盖策略并构建配置。
        *   **`new SpringJobScheduler(...).init()`**: 将任务注册到 Spring 的任务调度器中。

*   **`ElasticSimpleJob`** (自定义任务类)
    *   **`jobName = "updatetask"`**: 任务名称。
    *   **`cron = "1/5 * * * * ?"`**: 任务的执行时间表达式，表示每5分钟执行一次。
    *   **`shardingTotalCount = 1`**: 任务的分片总数，表示该任务不进行分片。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置类定位 (00:00-00:04)**
    *   讲师首先展示了项目的整体结构，包括 `seckill-module`、`seckill-service` 等模块。
    *   他将焦点定位到 `ElasticjobDynamicConfig.java` 文件，这是本节的核心代码文件。

*   **场景二：配置 Zookeeper (00:09-00:14)**
    *   讲师在代码中定位到 `ZookeeperConfiguration` 的构造方法。
    *   他通过 `@Value("${zkserver}")` 和 `@Value("${zknamespace}")` 注解，从配置文件中注入 Zookeeper 的地址和命名空间。
    *   他解释了 `ZookeeperConfiguration` 的作用是为后续的注册操作提供基础配置。

*   **场景三：注册初始化数据 (00:15-00:20)**
    *   讲师展示了 `ZookeeperRegistryCenter` 的初始化方法。
    *   他解释了 `ZookeeperRegistryCenter` 是用于在 Zookeeper 中注册初始化数据的组件。
    *   他强调了 `@Bean(initMethod = "init")` 注解的作用，即在 Spring 容器启动时自动调用 `init` 方法进行初始化。

*   **场景四：动态添加任务 (00:21-00:32)**
    *   讲师开始编写 `addDynamicTask` 方法。
    *   他首先创建了一个 `LiteJobConfiguration` 的构建器。
    *   他使用 `JobCoreConfiguration.newBuilder(...)` 来配置任务的核心属性，包括 `jobName`、`cron` 和 `shardingTotalCount`。
    *   他展示了如何通过 `.overwrite(true).build()` 来构建任务配置。

*   **场景五：注册到调度器 (00:33-00:44)**
    *   讲师展示了如何将构建好的任务配置注册到 Spring 的任务调度器中。
    *   他使用 `new SpringJobScheduler(instance, zookeeperRegistryCenter, liteJobConfiguration).init();` 来完成注册。
    *   他解释了 `SpringJobScheduler` 的作用是将任务添加到调度器中，以便在指定时间执行。

*   **场景六：自定义任务处理 (00:45-00:50)**
    *   讲师展示了 `ElasticSimpleJob` 类的定义。
    *   他解释了 `SimpleJob` 是 ElasticJob 框架中定义的接口，自定义的任务类需要实现该接口。
    *   他强调了 `jobName`、`cron` 和 `shardingTotalCount` 是任务的核心配置参数。
    *   他总结了整个动态任务的实现流程，强调了其灵活性和可扩展性。
