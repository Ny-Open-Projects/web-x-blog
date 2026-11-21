# 03-elasticjob-静态任务案例讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们开始学习ElectricJob

那我们先看一下官方网站这一块

对ElectricJob的一个介绍

这个图我们把网址打开

简单看一下

这个是官网对它的一个介绍

ElectricJob是一个分布式调度解决方案

它有两个相互独立的子项目组成

分别是Lite和Cloud

那ElectricJob这一块

它的Lite是定义为轻量级

无中心化解决方案

使用架包的形式提供分布式任务的协调服务

这是我们Lite这一块对它的一个定义

而Cloud这一块

它会额外提供资源服务治理

应用分发以及进程隔离等功能

相比我们的Lite而言

它的功能要更丰富一些

不过我们的Lite这一块

足以解决我们

所常用的问题

也不仅仅是我们的Lite

也不仅仅是我们Lite

也不仅仅是我们Lite的一些常见的一些任务需求了

所以我们项目里面将采用Lite

好

那我们这就来学习一下

我们Lite对应的一个定时任务案例

那定时任务案例呢

我们会去讲解静态定时任务案例和动态定时任务案例

静态定时任务案例呢

这个比较简单

功能比较单一

比如说

我希望每天早晨六点钟

比如说

我希望闹钟每天十二点叫我睡觉

那么这个一般是把时间给定时了

这个就是静态任务案例

好我们先来实现一下静态任务案例

静态任务案例呢

要想实现的话

我这里总结了这么一个步骤

我们可以按这个步骤来实现

第一步

首先是要引入依赖包

接着我们要配置主Keyboard的一个节点地址

以及我们任务的一个名称命名空间

然后我们就要去实现自己的一个任务了

实现自己的任务呢

他需要实现我们SimpleJob这个接口

好我们开始按照这三点来实现一个静态任务案例

我们以我们当前的商品微服务为例

把商品微服务打开

故事这里

我们在这里去实现我们的静态任务案例

那首先我们要先引入依赖包

在这一块把这个依赖包给拷过来

拷到我们

故事微服

到这来了之后

接着我们就要去配置我们的一个主Keyboard节点地址

以及我们

任务的一个命名空间名称

好我们看一下这个配置

这个配置在这一块

我们把它给拷过来

注意

把它配到

BossJob.yaml里面

就行了

好配置一下

在这里配置

这个是

ElecticJob的一个配置

那这一块我们简单介绍一下

因为我们

ElecticJob

它采用的是主Keyboard

作为我们的注册中心

作为我们的一个

任务发现

那这一块呢

需要指定我们主Keyboard的一个

服务地址

那这里

JK Server

就是我们当前这个服务所对应的一个地址

好下面这里有个LameSpace

这个就是

一会我们要执行的一个

任务所对应的命名空间

这一块弄完了之后

那我们

Lite的ElecticJob

这一块就已经配置完成了

接着我们只需要去

定义我们自己的一个

任务即可

好在这一块我们来写一个对应的任务

右键新建一个

目录叫

Task.

我们写个静态的StaticTask.jp

在这里呢

右键新建一个静态的

任务案例

StaticJob

它需要实现一个接口

叫做

SimpleJob

不要忘了把对象给容器管理

里面有一个方法

我们要去实现一下

这里呢

就是我们

自己要实现的一个

业务处理流程

好

这一块我们就简单输出一段代码就行

代码呢我们就输出一个时间

好这一块怎么输出呢

SimpleDataFormat

LueSimpleDataFormat

我们就输出

分钟就行了

HH

MM

SS

输出分钟和秒就可以了

好我们这个时候

来输出一下当前的时间

LueData

可以了

LueData

一会儿我们看一下这个时间间隔怎么样

行

我们这一块

写完了之后

那这个定时任务现在有效了吗

现在还没有效

因为你还没有告诉我他什么时候执行

对不对

好

怎么做呢

注意在这一块

跟刚才的配置有关系了

刚才这里不是配置了个

LameSpace吗

那么这一块

要写一个

ElectricJob

SimpleJob

在这里面有几个属于

一个属性

第一个属性就是我们的JobLame

这个呢

注意

是需要

和

和我们的

定时任务命名空间

保持一致

就是我这一块JobLame

其实跟他是要相等的

写过来就行了

好那除了这个之外

那什么时候执行呢

Current表达式

这个是

任务执行周期

就是什么时候执行

那我希望

从第1秒钟开始执行

每过5秒钟

执行一次

第1秒执行

每过5秒执行一次

后面写

星

注意啊

秒

分

好这是这一块

大家注意分别是

秒分往后面依此类推去

这是这个执行周期

那除了执行周期

他还有一个

分片的能力

我写个1

分片呢

其实就是多线程执行的意思

好我们写一下这个是

分片

分片我等于1就是

这一块

不开多线程

就一个

程序去执行就行了

OK

那现在我们这一块

基于我们

ElaticaJob的一个静态任务案例

就完成了

好我们来写

我们来启动测试一下

把之前的服务先给停止了

我们现在

直接启动我们当前商品微服务

测试一下

那一块会不会正常执行

右键运行一次

我们看现在的执行效果

好等程序运行

好程序起来了

先Clean一下

我们等待几秒钟

哎31

我们看一下

下一个应该是36

36

接着我们就是

41

好没有问题

这是我们这一块

这个

动态

ElaticaJob

分布式任务调度这一块的一个

静态任务案例

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于 **Elastic-Job** 分布式任务调度框架的入门教程，主要演示如何在 Spring Boot 项目中实现一个**静态定时任务**。讲师通过一个名为 `seckill-goods` 的电商项目为例，详细讲解了三个核心步骤：
1.  **引入依赖**：在 `pom.xml` 中添加 `elastic-job-lite-spring-boot-starter` 依赖。
2.  **配置 Zookeeper**：在 `bootstrap.yml` 中配置 Zookeeper 服务器地址和任务命名空间。
3.  **实现自定义任务**：编写一个实现 `SimpleJob` 接口的 Java 类 `StaticJob`，并在其中编写具体的业务逻辑（如打印当前时间）。

整个过程旨在帮助学习者快速上手 Elastic-Job，理解其基本架构和配置方式。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示课程大纲，介绍本节将学习 Elastic-Job 的静态任务案例。
*   **00:05 - 00:15**: 讲解 Elastic-Job 的概念，包括其由 `Elastic-Job-Lite` 和 `Elastic-Job-Cloud` 两个子项目组成，并简要介绍其架构。
*   **00:15 - 00:30**: 进入“1.2.1 静态任务案例”章节，明确本节目标是实现一个静态定时任务。
*   **00:30 - 00:45**: 展示实现步骤，包括引入依赖、配置 Zookeeper、实现自定义任务。
*   **00:45 - 01:00**: 在 IDE 中打开 `seckill-goods` 项目，并在 `pom.xml` 中添加 Elastic-Job 依赖。
*   **01:00 - 01:15**: 在 `bootstrap.yml` 文件中配置 `elasticjob` 的 `server-lists` 和 `namespace`。
*   **01:15 - 01:30**: 创建 `StaticJob` 类，实现 `SimpleJob` 接口，并编写 `execute` 方法。
*   **01:30 - 01:45**: 在 `StaticJob` 类中编写具体的业务逻辑，使用 `SimpleDateFormat` 格式化并打印当前时间。
*   **01:45 - 02:00**: 启动 Spring Boot 应用，验证任务是否成功注册并执行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `1.2.1 静态任务案例` 和 `1.2.2 动态任务案例`。
    *   **实现步骤**:
        1.  引入依赖包。
        2.  配置 Zookeeper 节点以及任务名称命名空间。
        3.  实现自定义任务，需要实现 `SimpleJob` 接口。
    *   **动态任务案例描述**: 动态任务案例主要用于程序运行时动态添加定时任务，应用场景非常广泛。

*   **代码关键内容**:
    *   **Maven 依赖 (pom.xml)**:
        ```xml
        <dependency>
            <groupId>com.github.kuhnhh</groupId>
            <artifactId>elastic-job-lite-spring-boot-starter</artifactId>
            <version>2.1.5</version>
        </dependency>
        ```
    *   **配置文件 (bootstrap.yml)**:
        ```yaml
        elasticjob:
          zookeeper:
            server-lists: zk-server:3181
            namespace: updatetask
        ```
    *   **自定义任务类 (StaticJob.java)**:
        ```java
        package com.seckill.goods.task.statictask;
        import org.springframework.stereotype.Component;
        import org.apache.shardingsphere.elasticjob.lite.api.ShardingContext;
        import org.apache.shardingsphere.elasticjob.lite.api.SimpleJob;
        @Component
        public class StaticJob implements SimpleJob {
            @Override
            public void execute(ShardingContext shardingContext) {
                SimpleDateFormat simpleDateFormat = new SimpleDateFormat("mm:ss");
                System.out.println("时间：" + simpleDateFormat.format(new Date()));
            }
        }
        ```
    *   **主启动类 (GoodsApplication.java)**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @MapperScan(basePackages = "com.seckill.goods.dao")
        public class GoodsApplication {
            public static void main(String[] args) {
                SpringApplication.run(GoodsApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**
    *   讲师在 IDE 中打开 `seckill-goods` 项目，展示其目录结构。
    *   在 `pom.xml` 文件中，讲师定位到 `<dependencies>` 标签，并添加了 Elastic-Job 的 Maven 依赖，强调了版本号 `2.1.5`。

*   **场景二：配置文件设置**
    *   讲师切换到 `bootstrap.yml` 文件，定位到 `elasticjob` 配置块。
    *   讲师演示如何配置 `zookeeper` 的 `server-lists`（`zk-server:3181`）和 `namespace`（`updatetask`），并解释了这些配置的作用。

*   **场景三：编写自定义任务**
    *   讲师在 `src/main/java/com/seckill/goods/task/statictask/` 目录下创建 `StaticJob.java` 文件。
    *   讲师编写了 `@Component` 注解，表明这是一个 Spring Bean。
    *   讲师实现了 `SimpleJob` 接口，并重写了 `execute` 方法。
    *   在 `execute` 方法中，讲师使用 `SimpleDateFormat` 格式化当前时间，并通过 `System.out.println` 打印出来。

*   **场景四：启动应用与验证**
    *   讲师在 IDE 中右键点击 `GoodsApplication.java` 的 `main` 方法，选择“Run 'GoodsApplication'”。
    *   应用启动后，讲师在控制台（Console）中观察到日志输出，确认任务已成功注册并执行。
    *   控制台输出示例：`时间：01:23`（具体时间根据实际运行情况而定）。

通过以上步骤，讲师成功地演示了如何使用 Elastic-Job 在 Spring Boot 项目中创建并执行一个静态定时任务。
