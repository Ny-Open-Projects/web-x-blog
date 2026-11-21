# 10-Quartz动态定时任务（环境搭建） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看我们COS的动态定时任务

刚才我们是说了一下

要实现动态定时任务

需要有这么一套数据模型支持

那么一共涉及到的是11张表

那么我们直接执行它这个circle脚本

然后把它创建到我们的数据库里面来就可以了

这个地方我提前已经创建好了

然后接下来我们来看下一个小节

就是环境搭建

咱们在这来创建一个新的没用工程

然后来导入什么相关的坐标

那么我们在这来创建一下

把这个先停掉

在这我们重新来new一个project

在这来指定一下com.it黑码

然后这个项目名就叫这个吧

跟咱们这个讲义保持一致

叫做COST test

当然这个T是个大写的

Next,直接完成

它这个地方说是已经存在了

因为它这个项目名是不去

是一份大小写的

那么我们给它改一下

给它加一个横线吧

好

完成

OK

在当前这个工程打开一下就可以了

好

那接下来我们把这个坐标来导一下

整个这一块

整个这一块了

就都复制下来

那么这里边的坐标比较多

因为什么呢

除了我们这个COST相关的坐标之外呢

还有就是关于我们这个Spring Boot一些这个坐标

因为我们这个呢

定位是一个Spring Boot的项目

咱们来看一下

你看我们导入的这些啊

这是COST的对吧

COST的

然后呢

还有LangBook对吧

然后呢

Spring Boot的StarterWeb

还有什么StarterTest测试的对吧

还有这个Swagger文档呢

还有MySQL的

因为要连接数据库对吧

然后呢

就是这个什么呢

MyBattis的

然后还MyBattisPlus等等这一堆

那这块呢

我们就全导进来

就可以了

然后接下来呢

我们就需要来编写一下

咱们这个Spring Boot的配置文件对吧

也就是application.yml这个文件

我直接把这个来复制一下

在这儿来创建出来

在src下边

这个叫application.yml

然后这里面的配置呢

我们就不再手写了

咱们直接把它抄过来

复制一下

直接粘贴在这个位置

这些配置呢

咱们简单看一下就可以了

server.prod指定我们

因为这是一个web项目对吧

那么需要指定一下这个Tomcat它的端口号

然后呢

就是这个什么应用的名称对吧

然后呢

接下来就是这个DataSource来指定一个德鲁伊的数据源

因为要连接数据库啊

然后接下来呢

就是关于我们这个数据库的一些连接参数对吧

像这个什么驱动名啊

还有这个连接参数

然后还有这个用户名密码等等这些

那么这个地方呢

我们就直接指定成什么呢

我们本地的就可以啊

指定成本地的

也是localhost

然后呢

这是咱们这个数据库名数据库名了

刚才我们也看到了

是不是就叫做cos就这个

后边呢

只是跟了一些参数

这个不用改了

然后呢

这是用户名密码

但是我们在这呢

需要来看一下我们这个密码呢

是应该是root

把这个相应的修改一下就可以了

这是咱们这个

这个sprintboot的配置文件

简单改造一下

然后接下来呢

我们需要来编写一个什么呢

配置类对吧

编写一个配置类

在这个配置类里边呢

来创建什么呢

创建我们一些核心的对象啊

比如说什么呢

这个schedule factory bit

也就是说我们前面呢

在咱们这个入门案例里边呢

咱们是写了一个mint方法对吧

在我们mint方法里边

然后呢

把这些对象是不是给创建出来

把这些对象创建出来

那么现在呢

我们就不用这么麻烦了

咱们直接通过一个什么呢

通过一个配置类这种方式

把我们所需要的这个对象给它创建出来

就是通过我们这个啊

叫schedule factory bit

一看这是不是就是一个工厂 bit

它的作用呢

就是创建我们这个统一的任务调度

这个对象schedule

然后直接通过它来创建就可以了

你看我是不是加了一个bin注解嘛

对吧

然后呢

因为它是一个配置类呢

所以必须要加一个configuration

每个注解

然后这里边这些配置

这些写法呢

其实都是

是简单化的

所以呢

我们先把这个代码抄过来

然后呢

大概来看一下

这个配置类呢

应该放在这个config包下边

这个呢

先关掉

然后呢

在下边来创建这个包

好

这就放在这儿

然后呢

我们把这个类呢

直接创建出来

就叫做schedule config

这是一个配置类

然后配置类里边这个代码呢

咱们就不再手敲了

它其实就相当于是配置文件

相当于就是配置文件

然后呢

我们主要就是来看一下

它在创建这个工厂对象的时候啊

它这里边需要指定的一些参数

这个呢

我们需要来重点看一下

好

你看我们这个地方呢

是不是就是来创建了这么一个schedule factory bin

通过这个工厂bin呢

来创建我们这个schedule对象

然后呢

我们来看一下一般这种工厂bin呢

它这里边呢

都会有一个方法叫做什么呢

叫做getobject的方法

咱们来看一下

一般呢都会有这么一个方法

而这个方法呢

就是我们这个工厂bin

那么它最终创建出来的实例

你看这是this.schedule

这个schedule是谁呢

我们可以点上来来看

你看是不是就是一个schedule对象

所以说呢

它是通过先创建这个工厂bin

然后呢

再调用getobject的方法

就可以返回我们真正想创建的这个schedule

就是统一任务调度的这个对象

然后呢

这里边呢

需要来注入一个数据源对象的对象

对吧

那这个数据源呢

我们其实不用管

因为呢

在这儿呢

咱们是不是已经配置了这个数据源

并且呢

在我们这个pum文件当中

已经导入了咱们这个坐标

对吧

刚才也看到了

在哪呢

刚才我们导入的这个

德鲁伊的数据源

在这儿了

对吧

好

这个是

它是做成了一个starter

对吧

做成了一个starter

这样的话呢

这个starter呢

就会自动的把这个数据源对象

给我们实例化好

然后这个地方呢

它是通过这么一种方式呢

通过类型

这种方式直接类型注入

就注给了我们这个方法

对吧

这样的话呢

就可以啊

把我们这个工厂bin给创建出来了

而这个工厂bin呢

怎么创建呢

注意看

首先先new一下它

然后呢

set data source

先把数据源设置上

因为什么呢

它是不是要访问我们

这11张表

对不对

所以说呢

我们需要通过这个数据源对象

来访问

这个数据库里面的资源

先把这个data source

set好

然后接下来

指定什么呢

指定我们这个scheduler

它的一些这个参数

而这个参数的话呢

我们是封装到了一个properties

这么一个对象里面

你看

全都是通过properties这个对象

来put各种各样的配置

参数

最后呢

把它设置给我们这个

这个factor对象

对吧

set cause properties

然后呢

把这个property对象

给我们注入一下

给我们set进来

就可以了

好

然后呢

我们来看啊

它这个配置的是什么呢

这instance name

这其实就是给我们scheduler

起了一个

一个实例名

对不对

但这个名字呢

只要是唯一的就可以

还包括有个id

对不对

然后呢

还有这个什么呢

这是连接池的一些配置

然后接下来呢

关键我们看的是这个

关键看的是这个

这个就是什么呢

我们这个job.class

也就是说我们进行这个任务

存储

对吧

任务存储这块

使用的就是这个类

叫做job.tx

大家还记得这个类吧

这个类呢

我们前面在这个核心API这块

是不是也

提到过了

就是它

它是通过gdbc这种方式呢

将所有数据保存到数据库中

具体呢

就是保存在咱们这个数据库的相应的

这11张表当中

所以说呢

我们这个地方呢

就是指定啊

指定咱们这个job.stop

它的配置

使用的就是这种方式

而它默认使用的呢

默认使用的

如果我们不配置

默认使用的是上面这种

也就是将我们这个任务信息呢

保存在内存当中

但是这种方式呢

就是什么呢

前面也提到了

如果我们服务

重启对吧

或者程序关闭啊

那么这些信息呢

就都没有了

好

也就是它是没有持久化的

然后接下来呢

是关于我们集群的一些配置

对吧

然后还有这个

这个就是table prefix

大家来看一下

这个什么cause横线

这是啥呢

这其实就是指定我们这个

我们要操作的那些表

它的前缀

你看咱们创建的这些表

是不是全都是cause下划线

对吧

那么开始了

相当于是它这些表的一个

一个

前缀啊

也就是说它这创建出来的

全都是按照这个命名规则

来命名这些表的

但是我们这个地方是大写的

因为表明真正在数据库里面呢

它是不区分大小写的

所以这个人没有关系

然后呢

这个什么select with lock circle

这是它指定的一个circle

用来锁定的

用来锁定的

然后呢

你看select from

这个地方是一个logs

对吧

然后或者unlock

where lock name

等于什么呢

这个它其实就是操作

我们这里边有一张什么呢

有一张这个

logs这边一张表

logs就是这张表

用来锁定的

然后呢

这些呢

就是基本上都是固定的套路

然后给它配置好就可以了

然后呢

再设置我们工厂

它的这个什么scheduler name

对吧

然后呢

这又设置了一个什么呢

start delay 3

这是啥意思呢

这个表示延时启动

你看我们前面在那个入门案例里边呢

咱们是直接调用了

我们scheduler对象的start方法

表示立即启动

对不对

而它这个呢

是一个延时启动

就是三秒钟之后

再来启动我们整体的任务调路

然后呢

这个是设置什么呢

设置一个contact key

这个都是套路性的

那么直接来设置就可以了

最终呢

把这个工厂对象来返回一下

这就是咱们一个配置类

直接把它这个超过来就可以了

大概读一下

好

配置类写好之后呢

我们下一步要做的是什么呢

就是关于我们这个

SWAG

的配置啊

来看一下

下一个就是关于SWAG的配置

咱们来配置一个叫configuration support

对吧

在这里面来开启我们这个SWAG

这种方式呢

就是便于我们来进行接口测试啊

这个咱们应该看的就比较多了

咱们直接把这个类呢

创建出来

也是放在这个config包下边

好把这个类创建一下

然后呢

这里面这个代码呢

整个都考过来了

好

Ctrl C直接复制到这边来

好

一会儿呢

我们是不是需要来创建一个controller

对吧

咱们在controller里边呢

去编写什么呢

我们动态的这些什么动态添加定时任务啊

暂停定时任务等等这些全都写在controller当中

好

那么一会儿呢

我们就需要按照这个包来创建

这样的话呢

他就可以扫描到这个包

把我们这些接口的都给暴露出去

对吧

然后呢

我们就可以使用SWAG这种方式来进行接口测试了

这个呢

直接超过来就可以了

不再过多解释了

这一步搞定

然后接下来呢

我们就需要来编写一个自定义任务

对吧

哎

就是还是我们那个hello job

然后呢

这回这个hello job呢

跟咱们前面那个入门案例不太一样

哎

我们前面这个入门案例呢

是不是让他去实现的是一个job接口

对吧

而现在呢

我们让他继承的是一个叫做causejobB

当然了

他其实最终的也会去实现那个接口

只不过呢

我们是间接实现的

因为什么呢

我们只要继承了他

而他的话呢

已经实现了那个job接口

好

所以说直接继承这个就可以了

而这个causejobB呢

咱们可以来看一下

他其实是什么呢

是这个sprint整合cause的时候给我们提供的这么一个

好

所以接下来呢

我们来创建一下

先把这个jobs这个包呢

来创建一下

在itk码这一层对吧

来创建一个jobs

然后呢

咱们这个自定义job的名字呢

还叫做hello job

然后这里面这个代码呢

我就不再写了

直接把它抄过来

好

CtrlC复制过来

整个替换一下

然后呢

我们可以来看一下咱们是不是继承了他

而他的话是不是实现了这个job

对吧

这就相当于我们间接的实现了他

间接的实现他

然后呢

为什么要继承他呢

就是因为在这个附类里边呢

他是不是已经去帮我们实现了一下这个execute的方法

对吧

那么我们需要做什么呢

哎

我们需要去实现这个方法

去重写这个方法叫executeintel

对吧 去重写这个方法叫executeintel

哎

你看他这儿

也就是说前面这块呢

是一些这个参数的准备

对吧

那么他都已经提供好了

最后呢

他需要调用这个executeintel这个方法

而这个方法的话呢

你看他在附类里边是一个什么呢

abstract的

是一个抽象的

那么这就需要我们的子类是不是去覆盖这个方法

去真正实现这个方法

所以说呢

在咱们这个hello job里边呢

只要去实现这块叫executeintel

然后呢

我们可以看到

他是不是同样把这个context对象

给我传过来了

哎

因为呢

他在上面这儿调用的时候

是不是就把这个context已经传进来了

好

所以我们在这儿直接使用就可以

当然咱们这一块呢

还是比较简单的

我们直接还是把这个什么呢

把这个时间是不是给他输出一下就可以了

然后呢

再把这个job的这个通过这个context的对象

获得job detail

然后呢

再获得这个job datamap

这个前面我们已经讲过了

对吧

通过这个datamap呢

可以动态的传一些参数进来

比如说我传一个什么呢

biz id进来

这样的话呢

我就可以直接get他来获得他

然后在这儿来输出一下

好

在这儿来输出一下biz id

好

这是我们自定义的这个job呢

也是比较简单的

因为我们这块呢

重点还是在演示什么呢

我们这个框架它是怎么用的

哎

所以说呢

重点呢

就没有放在这个方法

具体它实现的业务逻辑

我们在这儿只是简单输出一下

但是大家应该能够想象出来

在我们真实的项目当中啊

其实重点应该就是写这个方法

就是当我们某个

实

这个任务触发的时候

具体要做什么事

而那块的话

是不是跟我们的业务相关的

对吧

跟我们业务相关的

所以我们真正啊

在项目当中啊

肯定重点就是编写这个业务方法

好

然后再往下呢

我们就编写一个启动类啊

来启动咱们这个项目就可以了

好

咱们就编写一个叫做

cause application

这么一个启动类

但是这块呢

大家要注意

我们现在呢

都属于这个环境准备啊

都属于环境准备

因为这块呢

跟我们动态的定时任务

其实还没有关系

只是把这个

整个开发环境

是不是把它搭建起来

把需要的这些啊

这些类啊

这些包啊

整体来提供一下

好

这个启动类就不用解释了

然后接下来呢

我们可以来编写一个controller

来简单测一下

对吧

来简单测一下

咱们先来把这个包啊

controller包

来创建一下

好

com itk 嘛

controller

然后呢

在这个controller里边呢

在这个包里边呢

来创建这么一个类

好

这个叫做cause

controller

然后呢

这里边的代码呢

整个复制过来

但是现在呢

我们只是相当于

只是注入了这么一个

schedule对象

对吧

然后呢

还没有任何方法

那么到这儿的话呢

我们就已经把这个什么呢

环境搭建这块搞定了

一会儿呢

我们就需要来实现什么呢

动态的这个定时任务

比如说我要

动态添加一个定时任务

我要暂停一个定时任务

那么就需要在咱们

controller当中啊

也就是在我们现在

这个controller中

一个一个添加方法

然后每一个方法呢

就是来实现一个任务的操作

就可以了

好

这是关于我们这个环境搭建

先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频为一个关于“智能调度服务”技术课程的片段，核心内容是使用 **Quartz** 框架在 **Spring Boot** 项目中实现动态定时任务。讲师通过演示如何创建 Maven 工程、配置依赖、编写核心调度配置类、定义任务类以及创建控制器来完成一个完整的定时任务示例。视频中还展示了如何集成 Swagger 用于 API 文档，并对 Quartz 的核心概念（如 Scheduler、Job、Trigger）进行了简要介绍。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节按画面内容和逻辑顺序排列：

*   **00:00 - 00:05**: 课程导航与项目结构概览。讲师展示了 Typora 中的课程大纲，当前章节为“2.2 环境搭建”，并介绍了项目整体结构。
*   **00:05 - 00:15**: 创建 Maven 工程并配置 `pom.xml`。讲师在 IntelliJ IDEA 中创建了名为 `quartzTest` 的 Spring Boot 项目，并展示了 `pom.xml` 文件中引入的依赖，包括 Spring Boot、Spring Cloud Alibaba、Swagger、Quartz 等。
*   **00:15 - 00:25**: 配置 Quartz 核心依赖。讲师在 `pom.xml` 中添加了 `quartz-scheduler` 依赖，并配置了 `spring-boot-starter-parent` 的版本管理。
*   **00:25 - 00:35**: 配置数据库连接和 JobStore。讲师在 `application.yml` 中配置了数据源（Druid）和 Quartz 的 JobStore，使用 `JobStoreTX` 以确保数据持久化。
*   **00:35 - 00:45**: 编写核心调度配置类 `ScheduleConfig.java`。讲师展示了如何通过 `SchedulerFactoryBean` 配置 Scheduler，设置线程池、JobStore 等参数。
*   **00:45 - 00:55**: 定义自定义任务类 `HelloJob`。讲师创建了一个继承自 `QuartzJobBean` 的类，并重写了 `executeInternal` 方法，用于打印任务执行信息。
*   **00:55 - 01:05**: 创建控制器 `QuartzController`。讲师在控制器中注入 `Scheduler` 对象，并编写了用于添加定时任务的 `save` 方法。
*   **01:05 - 01:15**: 集成 Swagger。讲师展示了如何通过 `@EnableSwagger2` 注解和 `Docket` 配置类来启用 Swagger 文档，方便 API 调试。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: 显示了“第8章 智能调度服务”的详细目录，包括“2.1 数据模型”、“2.2 环境搭建”、“2.3 实现定时任务”等子章节。
    *   **Quartz 核心概念**: 在 PPT 中列出了 Quartz 的核心组件，如 `Scheduler`、`JobDetail`、`Trigger`、`JobBuilder`、`TriggerBuilder`、`JobExecutionContext`、`JobDataMap`、`RAMJobStore` 和 `JobStoreTX`。

*   **代码关键内容**:

    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz</artifactId>
            <version>${quartz.version}</version>
        </dependency>

        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${swagger.version}</version>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>${druid.version}</version>
        </dependency>
        ```

    *   **`application.yml` 配置**:
        ```yaml
        spring:
          datasource:
            type: com.alibaba.druid.pool.DruidDataSource
            druid:
              driver-class-name: com.mysql.cj.jdbc.Driver
              url: jdbc:mysql://localhost:3306/quartz?useUnicode=true&characterEncoding=utf-8&useSSL=false&serverTimezone=Asia/Shanghai
              username: root
              password: 123456
        ```

    *   **`ScheduleConfig.java` 核心配置**:
        ```java
        @Configuration
        public class ScheduleConfig {
            @Bean
            public SchedulerFactoryBean schedulerFactoryBean(DataSource dataSource) {
                SchedulerFactoryBean factory = new SchedulerFactoryBean();
                factory.setDataSource(dataSource);
                Properties prop = new Properties();
                prop.put("org.quartz.scheduler.instanceName", "WitlinkedScheduler");
                prop.put("org.quartz.scheduler.instanceId", "AUTO");
                prop.put("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
                prop.put("org.quartz.threadPool.threadCount", "20");
                prop.put("org.quartz.jobStore.class", "org.quartz.impl.jdbcjobstore.JobStoreTX");
                prop.put("org.quartz.jobStore.isClustered", "true");
                prop.put("org.quartz.jobStore.tablePrefix", "QRTZ_");
                prop.put("org.quartz.jobStore.misfireThreshold", "120000");
                prop.put("org.quartz.jobStore.selectWithLockSQL", "SELECT * FROM (SELECT LOCKS FROM QRTZ_LOCKS WHERE LOCK_NAME = ?) LOCKS");
                factory.setQuartzProperties(prop);
                return factory;
            }
        }
        ```

    *   **`HelloJob.java` 任务类**:
        ```java
        public class HelloJob extends QuartzJobBean {
            @Override
            protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
                LocalDateTime now = LocalDateTime.now();
                DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
                String time = dateTimeFormatter.format(now);
                Object bizId = context.getJobDetail().getJobDataMap().get("bizId");
                System.out.println("自定义Job...bizId = " + bizId + " 执行时间 " + time);
            }
        }
        ```

    *   **`QuartzController.java` 控制器**:
        ```java
        @RestController
        @RequestMapping("/quartz")
        public class QuartzController {
            @Autowired
            private Scheduler scheduler;
            
            @PostMapping("/add")
            public String addJob(@RequestBody JobDataMap jobDataMap) {
                // 业务逻辑：创建 JobDetail、Trigger，然后调用 scheduler.scheduleJob()
                return "任务添加成功";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**
    *   **描述**: 讲师在 IntelliJ IDEA 中创建了一个名为 `quartzTest` 的 Spring Boot 项目，并在 `pom.xml` 中配置了 `spring-boot-starter-parent` 作为父工程。随后，他逐步添加了 `quartz`、`springfox-swagger2`、`druid-spring-boot-starter` 等依赖，并通过右键菜单“删除代码块”功能来管理依赖版本。

*   **场景二：配置 Quartz 核心参数**
    *   **描述**: 讲师在 `application.yml` 中配置了数据库连接信息，并在 `ScheduleConfig.java` 中通过 `SchedulerFactoryBean` 配置了 Quartz 的核心参数，包括线程池大小、JobStore 类型（`JobStoreTX`）、集群模式等。

*   **场景三：定义自定义任务**
    *   **描述**: 讲师创建了一个 `HelloJob` 类，该类继承自 `QuartzJobBean`。在 `executeInternal` 方法中，他获取了任务的 `bizId` 和当前执行时间，并打印到控制台，用于演示任务的执行逻辑。

*   **场景四：创建控制器并集成 Swagger**
    *   **描述**: 讲师创建了 `QuartzController`，并在其中注入了 `Scheduler` 对象。他通过 `@PostMapping("/add")` 注解定义了一个用于添加定时任务的接口。同时，他通过 `@EnableSwagger2` 和 `Docket` 配置类启用了 Swagger，方便前端或测试人员查看和调用 API。

*   **场景五：核心概念讲解**
    *   **描述**: 在 PPT 页面上，讲师用列表形式清晰地介绍了 Quartz 的核心组件，如 `Scheduler`（任务调度器）、`JobDetail`（任务对象）、`Trigger`（触发器）、`JobBuilder`（任务构建器）等，帮助学生理解框架的底层结构。

---
