# 22-XXL_JOB集成运用-交易调度服务搭建与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,这一讲咱们去完成交易调度服务的创建

以及基本必要组件的集成配置

回到工程当中

我们去创建一个新的模块

右键New Model

点击Next

名称我们叫Bus

Stock Task

点击Next

Finish

让它导入生效

接下来我们将必要的依赖加入进去

从讲义当中做一个copy

粘连进去

让它导入生效

我们看一下它所加入的有哪些依赖

在这里有Spring Boot的依赖

然后Marcus服务注册发现

这里是公用的数据层主线

服务层主线

工具主线

还有实体依赖

接着是缓存依赖

GRBC主线的依赖

最后就是XLJob的核心依赖

依赖加入完成之后

我们接着去创建工程的配置文件

New File

Boot Strap

首先创建基准的配置文件

这里要配置是读取哪一个环境的配置文件

读取相应的变量

Package Invaluable

接着我们再去创建一个开发环境的配置文件

Boot Strap

DV

也是采用Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

Yaml可用的配置文件

也是采用Yaml可用的配置文件

我们从讲习当中将配置信息拷贝进来

拷贝完成之后

我们大概来看一下它有哪些属性配置

这个是服务的基本配置

然后是LockitMQ

服务端的消息配置

它的主编是stocktask-1

每个服务的主编名称要保持为一

下面是双数据的配置

这些都是所用到的

主件的配置信息

最后就是分布式调度任务的配置

咱们来看一下这一块具体是如何配置的

首先它要去配置插在了Job

管理后台的地址

管理后台的地址

如果是有多个节点该如何配置呢

这里它给了一个说明

如果是存在多个节点

那么将所有的地址信息全部加入进去

中间是采用逗号进行分隔

在这里咱们就不演示了

我们先来看看两次集群的操作

我们侧重是学习插在了Job和项目的集成运用

我们指向插在了Job单个后台管理节点就可以

下面是插在了Job执行器的配置地址

插在了Job其实是一个分离式设计

它包含两大部分

第一部分是admin调度管理后台

另外一部分就是任务的具体执行者

也就是discute执行器

执行器里面是配置些什么信息呢?

这个是App的名称

也就是咱们服务的名称

然后是IP

IP可以不用配置

它会默认读取本机的IP

然后是port的端口

这个是执行器的先听端口

下面是log pass

它的log日志的记录

然后是log的保留时间

这里-1

那么日志是不会清除的

下面是access token

如果说

咱们要通过插在Job做权限控制的

那么access token在这里呢

就要去做相应的配置

好工程配置实现完成之后

接下来我们还要去实现插在Job的配置内

那首先我们创建相应的包

右键new package

创建基准目录

com idcast bus

stock task

然后在下面我们创建相应的纸包

右键open in terminal

make dir

pitch

config

do

然后是Job具体的调度任务

service业务实现

启动包

那接下来我们去创建插在Job的配置内

右键new

jocast

名称叫插在Job

config

这个配置内呢

它主要就是将工程当中配置的插在Job信息

配置的插在Job的属性录取进来

然后去创建初始化插插Job的执行器

首先我们加上注解configuration

然后要去定义一个插在Job的执行器

Job

spin is cuter

声明bin

给它一个初始化的调用方法

start

也就是说这个bin在初始化的时候呢

会去调用is cuter的start方法

结束的时候呢

它会去调用destroy的方法

因为咱们知道执行器呢

它会通过异步现成去实现任务的处理

所以在服务关闭的时候呢

它要去关闭任务

释放相应的资源

这里呢

要去定义插在Job is cuter

创建插在Job is cuter

下面就是设置咱们刚才在工程配置文件里面

所定义的属性

这里属性量比较多

咱们就不再主意去敲写

从讲义当中做一个copy

将属性copy进来

导入value的val

这个是在smin framework下面

这个日子咱们换种方式实现

采用Longboard的日子插件

导入合截图

咱们再去copy

属性的设置代码

将这一段copy进去就可以了

这里就是将工程配置的属性设置进去

然后返回

插在了Job

Spin is cuter

为了知道有没有正常执行

在这里要加上一个日子的打印

上塞落Job

很费感

一粒的

插在了Job的集成配置就已经实现完成

接下来我们还要去实现

必要组件的集成配置

比如说双数据源

内地式仿存

异步现成词等等

这些组件的集成咱们之前都做过讲解

在这里咱们就快速实现

引用之前咱们已经实现的代码

将config下面的这些配置内

咱们引入进来

把它放在config目录下面

这里是集成了双数据源的配置

这里面的双数据源是基于mybattist实现的

然后是Ladies的配置

下面是现任词的配置实现

为了测试后面业务逻辑的讲解

咱们再将DAO的数据层接口引入进来

b字和chad

放入DAO包下面

咱们检查一下

进入到map文件

好实体跟数据层接口

这些指向都是正确了

这些都没有问题

最后再去创建系统内

new telcast stock task application

创建启动方法

psvm stream application.run

指向当前内ax

然后增加必要的数据源

enable discovery command

enable transaction management

然后开启sprint任务调度处理

comment second

基础的包扫描

指向com.idcast

好,启动内就已经配置好

那这一讲

咱们就完成了交易调度服务的创建

以及基本必要组件的集成配置

这里大家侧重要掌握

xxljob的集成配置

好,这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“分布式任务调度框架”的实战教学，具体聚焦于如何在 Spring Cloud 微服务架构中集成并使用 **XXL-JOB** 分布式任务调度系统。讲师通过一个名为 `bulls-stock-task` 的微服务工程，演示了从项目依赖配置、核心配置文件编写、执行器初始化到具体业务任务实现的完整流程。课程内容包括：添加 XXL-JOB 依赖、配置 `bootstrap-dev.yml` 文件、编写 `XxlJobConfig` 配置类初始化执行器、以及实现一个具体的“账户股票交割单调度任务”。整个过程旨在帮助开发者掌握在微服务项目中集成 XXL-JOB 的标准方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程开场，讲师介绍本章目标是学习如何在微服务中集成 XXL-JOB。
*   **00:16 - 00:30**: 在 `pom.xml` 文件中添加 XXL-JOB 的依赖，版本号为 `2.1.0`。
*   **00:31 - 00:45**: 在 `bootstrap-dev.yml` 配置文件中配置 XXL-JOB 的管理端地址、执行器 IP、端口、日志路径等核心参数。
*   **00:46 - 01:00**: 创建 `XxlJobConfig` 配置类，使用 `@Configuration` 注解，并通过 `@Bean` 方法初始化 `XxlJobSpringExecutor`。
*   **01:01 - 01:15**: 在 `XxlJobConfig` 类中，通过 `setAdminAddresses`、`setAppName`、`setIp`、`setPort`、`setAccessToken`、`setLogPath`、`setLogRetentionDays` 等方法，将配置文件中的属性值注入到执行器中。
*   **01:16 - 01:30**: 讲师讲解 `@Value` 注解用于从配置文件中读取属性值，并将其注入到 `XxlJobConfig` 类的私有属性中。
*   **01:31 - 01:45**: 讲师在 `StockTaskApplication` 启动类中添加 `@EnableXxlJob` 注解，以启用 XXL-JOB 功能。
*   **01:46 - 02:00**: 讲师开始实现具体的业务任务，即“账户股票交割单调度任务”，并讲解了交割单的概念和数据结构。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.8 功能验证”、“3.8.1 交易服务下单验证”、“3.8.2 挂单服务功能验证”、“3.9 总结”、“3.1 XXL-JOB介绍”、“3.2 XXL-JOB管理端配置使用”、“3.3 创建配置交易调度服务工程”、“3.4 实现账户股票交割单调度任务”、“3.5 实现账户持仓利息调度任务”、“3.6 交割单调度任务接入管理端”。
    *   **关键说明**: “这里的依赖可以借用其他工程配置，需要加入xxl-job组件依赖，版本为2.1.0，目前的最新版本。”、“这里初始化xxl-job的执行器信息，读取注入上面配置文件中的属性值。”、“交割单是用来记录交割的具体交易情况的单据。交割的概念来源于期货，分为：实物交割和现金交割。交割单查询数据以电子表格的形式输出比较容易看清。交割单表格内容包含交割日期、证券代码、成交价格等19项内容。”

*   **代码关键内容**:
    *   **Maven 依赖 (pom.xml)**:
        ```xml
        <dependency>
            <groupId>com.xuxueli</groupId>
            <artifactId>xxl-job-core</artifactId>
            <version>${xxl.job.version}</version>
        </dependency>
        ```
    *   **配置文件 (bootstrap-dev.yml)**:
        ```yaml
        xxl:
          job:
            admin:
              addresses: http://127.0.0.1:8081/xxl-job-admin
            executor:
              appname: ${spring.application.name}
              ip: ${xxl.job.executor.ip}
              port: ${xxl.job.executor.port}
              logpath: /data/aplogs/xxl-job/jobhandler
              logretentiondays: -1
              access_token: ${xxl.job.executor.accessToken}
        ```
    *   **配置类 (XxlJobConfig.java)**:
        ```java
        @Configuration
        public class XxlJobConfig {
            @Bean(initMethod = "start", destroyMethod = "destroy")
            public XxlJobSpringExecutor xxlJobExecutor() {
                XxlJobSpringExecutor xxlJobSpringExecutor = new XxlJobSpringExecutor();
                xxlJobSpringExecutor.setAdminAddresses(adminAddresses);
                xxlJobSpringExecutor.setAppName(appName);
                xxlJobSpringExecutor.setIp(ip);
                xxlJobSpringExecutor.setPort(port);
                xxlJobSpringExecutor.setAccessToken(accessToken);
                xxlJobSpringExecutor.setLogPath(logPath);
                xxlJobSpringExecutor.setLogRetentionDays(logRetentionDays);
                return xxlJobSpringExecutor;
            }
        }
        ```
    *   **启动类 (StockTaskApplication.java)**:
        ```java
        @SpringBootApplication
        @EnableXxlJob
        public class StockTaskApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockTaskApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：添加 XXL-JOB 依赖** (00:16-00:30)
    *   讲师在 `pom.xml` 文件中，通过鼠标点击和键盘输入，添加了 `com.xuxueli:xxl-job-core` 依赖，并将其版本号设置为 `${xxl.job.version}`，以便与项目版本号保持一致。

*   **场景二：配置 XXL-JOB 执行器** (00:31-00:45)
    *   讲师在 `bootstrap-dev.yml` 文件中，配置了 XXL-JOB 的管理端地址、执行器的 IP、端口、日志路径等关键参数。他特别强调了 `admin` 和 `executor` 两个配置块的重要性。

*   **场景三：初始化 XXL-JOB 执行器** (00:46-01:15)
    *   讲师创建了一个名为 `XxlJobConfig` 的配置类，并使用 `@Configuration` 注解将其标记为 Spring 配置类。
    *   在类中，他通过 `@Bean` 注解定义了一个方法，该方法返回一个 `XxlJobSpringExecutor` 实例。
    *   在方法体内，他通过 `setAdminAddresses`、`setAppName`、`setIp`、`setPort`、`setAccessToken`、`setLogPath`、`setLogRetentionDays` 等方法，将配置文件中的属性值注入到执行器中。

*   **场景四：启用 XXL-JOB 功能** (01:31-01:45)
    *   讲师在 `StockTaskApplication` 启动类中，添加了 `@EnableXxlJob` 注解。这个注解是启用 XXL-JOB 功能的关键，它会自动扫描并注册所有带有 `@XxlJob` 注解的任务。

*   **场景五：实现业务任务** (01:46-02:00)
    *   讲师开始编写具体的业务任务代码，即“账户股票交割单调度任务”。
    *   他首先在 `XxlJobConfig` 类中，通过 `@Value` 注解读取了配置文件中的属性值，并将其注入到类的私有属性中。
    *   他讲解了交割单的概念，指出交割单是记录交易情况的单据，包含日期、证券代码、成交价格等信息。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解课程内容。
