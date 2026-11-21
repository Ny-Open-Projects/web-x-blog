# 06-elasticjob-动态任务案例测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那我们接着来测试一下这个动态定时任务案例

那既然要测试

咱们这里写一个控制器来测试一下

右键新建一个TaskControl

好写个RestControl

RequestMapping

这里呢我们就写一个简单的测试就行了

这个是定时任务案例测试

Public

写个Result

写个叫做Task

GuideMapping

我就直接写个Task就行了

New Result

好这是这一块

那么这一块写了之后呢

我们一会儿就要调它

所以我们要把它给注入进来

一会儿要调当前这一个定时任务对象

就是我们这一块的一个

ElectricJobDynamicConfigure

要调它

调它里面的这个

方法

所以我们要把它给注入进来

就是ElectricJobDynamicConfigure

把它给注入进来

注入进来

我们添加一个动态定时任务案例

第一个我们看一下

JobLame

给我传过来

第二个呢我们看一下

是Chrome

Chrome呢我们就写一下

写一下Chrome

等于1-5

好我们写成这个样子

好我们写成这个样子

但是这样子写了其实也定时了

我希望在外面把时间给我传过来

String Time

这个5呢我就不写死了

我用外面传过来的5Time

这个就写个Intel型

好了

我们这一块Chrome就给它

看另外一个参数是分片1

还有一个是你要执行的一个任务案例6

我们就写了这个

我们就写了这个任务案例6

我们刚才创建了一个Dynamic Task

就可以了

行我们来测试一下

看行与不行

好把之前为了看到这个案例执行更清晰一点

把之前的一个打印给注释掉

这是之前的一个任务

好我们现在来测试一次

看效果如何

Task

JobLame

Time

等它启动

好启动没有报错

我们请求这个地址

Localhost

1808

18081

我们看一下

是18081

Task

加上一个JobLame

等于随便写

咱写个叫ABC

加上一个Time

等于10秒钟执行一次

大家看10秒钟

回车

这里显示OK

我们看这里

这里没有执行

等10秒

41

那一会儿再过10秒

大家看

应该可以了

应该是51

正确

对吧

我们再添加一个任务案例

注意如果我是ABC的话

它会把ABC这一块给改变的

大家看我把它换成2秒钟

回车

2秒之行

动态定时任务案例就搞定了

好我们再做这么一个事情

大家看一下

这个动态定时任务案例

我们写的还不够完美

把它写的更完美一点

比如说

我希望你传给我一个参数行不行呢

我希望我这里传一个参数过去

传一个ID.9的

我传个ID.9行不行呢

好这个也是可以的

如果你想接收参数的话

这个时候你可以把参数传过来

String ID

这个ID怎么传过去呢

注意在这一块要想传过去

我们仍然是在这一块

往里面添加就行了

往这里面添加就行了

大家看

这是在这里

好我们看一下

它还可以继续添加

这是前面添加了这几个参数对不对

好我们看

添加别的参数

点有个job

Permit

直接把这个参数给它就行了

哪个参数

ID给它

这个是

传递的参数

额外的参数

额外的参数

是可以传过来的

那么传过来之后

我这边执行任务能不能获取呢

可以获取

好我们获取一下这个参数

String ID.9

怎么获取大家看啊

点有个get job permit

就可以获取这个

ID参数的值了

好我们把这个ID参数的值

给加过来

可以了

除了这个ID

包括我们任务的名称

大家看啊

get job name

都是可以获取的

都是可以获取

我们执行一次大家看一下效果

看现在的效果如何

把刚才这个

重新启动一次

我们同时执行多个任务

看多个任务能不能够同时执行

这里

参数没传

咱这一块参数也得获取一下

String ID

把ID给它

好我们看ID应该不在这里

在前面这里

好了我们再来重新启动一次

大家看看现在这个任务

能不能多个任务同时执行呢

好等它启动

启动成功了

我们先来第一个任务A任务

给的值是1

好

它是两秒钟执行一次

把它换成

五秒钟执行一次

回车

可以了

再

B任务

它是几秒执行一次呢

是

两秒执行一次

ID给个2

回车

也成功了

大家看这个时间

好重新来看

重新来看

这是

B任务

两秒钟执行的

39

41

对吧

好我们看A任务是5秒钟

41

A任务我们再看A任务

46

5秒钟执行

正确吧

好这个就是我们

当前这一块

我们Electic Job的一个

动态任务案例的一个

测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频演示了如何在 Spring Boot 项目中，使用 ElasticJob-Lite 框架实现一个**动态的、可配置的分布式定时任务**。核心内容包括：
- **环境搭建**：使用 IntelliJ IDEA 开发环境，项目结构包含 `TaskController`、`DynamicTask`、`ElasticJobDynamicConfig` 等核心类。
- **核心逻辑**：通过 HTTP 接口（`/task`）接收任务参数（任务名、Cron 表达式、分片总数），并动态创建一个 `SimpleJob` 实例。
- **技术栈**：Spring Boot + ElasticJob-Lite + ZooKeeper（用于分布式协调）。
- **关键步骤**：
  1.  在 `TaskController` 中定义 REST 接口。
  2.  在 `ElasticJobDynamicConfig` 中配置 `ZookeeperRegistryCenter`。
  3.  在 `DynamicTask` 中实现 `SimpleJob` 接口，定义具体的业务逻辑。
  4.  通过 `addDynamicTask` 方法将新任务注册到 ElasticJob-Lite 的调度器中。
- **演示流程**：通过浏览器访问 `/task` 接口，传入参数，触发任务创建和执行，并在控制台输出日志。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **00:00 - 00:05**: **项目环境与核心类概览**。展示项目结构，重点介绍 `TaskController`、`DynamicTask` 和 `ElasticJobDynamicConfig` 三个核心文件。
*   **00:06 - 00:15**: **定义 REST 接口**。在 `TaskController` 中使用 `@RestController` 和 `@GetMapping` 注解定义 `/task` 接口，用于接收动态任务参数。
*   **00:16 - 00:25**: **配置 ElasticJob-Lite 核心类**。在 `ElasticJobDynamicConfig` 中，通过 `@Configuration` 和 `@Bean` 注解配置 `LiteJobConfiguration` 和 `SpringJobScheduler`，并注入 `ZookeeperRegistryCenter`。
*   **00:26 - 00:35**: **实现动态任务逻辑**。在 `DynamicTask` 类中，实现 `SimpleJob` 接口的 `execute` 方法，定义具体的业务逻辑（如打印当前时间）。
*   **00:36 - 00:45**: **整合与调用**。在 `TaskController` 的 `task` 方法中，调用 `ElasticJobDynamicConfig` 的 `addDynamicTask` 方法，传入任务名、Cron 表达式、分片总数和自定义的 `DynamicTask` 实例。
*   **00:46 - 00:55**: **演示与测试**。通过浏览器访问 `/task` 接口，传入参数，触发任务创建和执行，并在控制台查看输出日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   **右侧浮动框**：贯穿整个视频，是一个关键的演示辅助工具，内容为：
        1.  配置初始化的 ZooKeeper 地址
        2.  配置定时任务命名空间（不一定会用）
        3.  注册初始化数据
        4.  监听器 -> 任务执行前后监听（可有可无）
        5.  动态添加定时任务实现
        6.  自定义任务处理过程 - 实现 `SimpleJob`
    *   **代码示例框**：在右侧浮动框中，展示了一个 `ElasticSimpleJob` 的示例配置，用于说明任务的基本结构：
        ```java
        @ElasticSimpleJob(
            jobName = "updatetask",
            cron = "1/5 * * * * ?",
            shardingTotalCount = 1
        )
        ```

*   **代码关键内容**：

    **1. `TaskController.java` (REST 接口)**

    ```java
    @RestController
    @RequestMapping(value = "/task")
    @CrossOrigin
    public class TaskController {
        @Autowired
        private ElasticJobDynamicConfig elasticJobDynamicConfig;

        @GetMapping("/task")
        public Result task(String jobName, Integer time, String id) {
            String cron = "1/5 * * * * ?";
            elasticJobDynamicConfig.addDynamicTask(jobName, cron, shardingTotalCount, id, new DynamicTask());
            return new Result(flag: true, StatusCode.OK, message: "执行成功！");
        }
    }
    ```

    **2. `DynamicTask.java` (自定义任务)**

    ```java
    public class DynamicTask implements SimpleJob {
        @Override
        public void execute(ShardingContext shardingContext) {
            String id = shardingContext.getJobParameter();
            String jobName = shardingContext.getJobName();
            System.out.println("DynamicTask 执行中，任务名：" + jobName + "，参数：" + id);
        }
    }
    ```

    **3. `ElasticJobDynamicConfig.java` (核心配置类)**

    ```java
    @Configuration
    public class ElasticJobDynamicConfig {
        @Autowired
        private ZookeeperRegistryCenter zookeeperRegistryCenter;

        @Bean
        public LiteJobConfiguration liteJobConfiguration() {
            // 配置 LiteJob
            return new LiteJobConfiguration(
                new JobCoreConfiguration("jobName", "1/5 * * * * ?", 1),
                new JobSchedulerConfiguration(zookeeperRegistryCenter)
            );
        }

        @Bean
        public SpringJobScheduler springJobScheduler() {
            // 创建并初始化调度器
            return new SpringJobScheduler(
                liteJobConfiguration(),
                zookeeperRegistryCenter
            );
        }

        public void addDynamicTask(String jobName, String cron, int shardingTotalCount, SimpleJob instance) {
            // 动态添加任务到调度器
            springJobScheduler().addJob(jobName, cron, shardingTotalCount, instance);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与核心类定位 (00:00-00:05)**
    *   **描述**：讲师首先展示了项目的整体结构，重点指向 `TaskController`、`DynamicTask` 和 `ElasticJobDynamicConfig` 三个文件，说明它们是实现动态任务的核心组件。

*   **场景二：定义 REST 接口 (00:06-00:15)**
    *   **描述**：讲师在 `TaskController` 中编写了 `@GetMapping("/task")` 方法，用于接收前端传来的任务参数。他强调了 `@RestController` 和 `@CrossOrigin` 注解的作用。

*   **场景三：配置 ElasticJob-Lite (00:16-00:25)**
    *   **描述**：讲师在 `ElasticJobDynamicConfig` 中配置了 `ZookeeperRegistryCenter`，并创建了 `LiteJobConfiguration` 和 `SpringJobScheduler` 两个 Bean。他解释了 `ZookeeperRegistryCenter` 是用于分布式协调的关键组件。

*   **场景四：实现动态任务逻辑 (00:26-00:35)**
    *   **描述**：讲师在 `DynamicTask` 类中实现了 `SimpleJob` 接口的 `execute` 方法。他演示了如何通过 `ShardingContext` 获取任务名和参数，并在控制台打印日志。

*   **场景五：整合与调用 (00:36-00:45)**
    *   **描述**：讲师在 `TaskController` 的 `task` 方法中，调用 `elasticJobDynamicConfig.addDynamicTask` 方法，将 `DynamicTask` 实例注册到调度器中。他强调了参数的传递和方法的调用。

*   **场景六：演示与测试 (00:46-00:55)**
    *   **描述**：讲师通过浏览器访问 `/task` 接口，传入任务名、Cron 表达式和参数。在控制台中，可以看到 `DynamicTask` 被成功创建并执行，打印出日志信息，证明了动态任务功能的实现。
