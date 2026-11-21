# 13-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看啊

如何使用我们这个通用权益系统

对吧

以它为相当于用它作为我们的脚手架

对吧

在它的基础之上来进行新项目的开发

刚才呢

我们说了是以这个什么呢

商品管理对吧

商品服务为例啊

那么我们开发了是这么一个叫做PD

Goose Entity对吧

咱们这个实体模块

但是这个非常简单

我们就整了一个实体对吧

我们是把这个业务进行了简化

然后呢

我们接下来来看啊

就是这个PD Goose Server

也就是我们这个商品服务

这个Maven模块它的开发

首先呢

我们还是需要把这个什么呢

POM文件是不是给它来配置一下

这里面呢

主要就是把这个Dependency对吧

它所依赖的这些坐标

给它拷过来

你看依赖的坐标其实还是挺多的啊

包括这个Build也一块拷过来

找到我们这个PD Goose Server

它的这个POM文件

然后呢

直接

直接

粘在这个位置

这里边引入了很多这个坐标

对吧

这个地方它是不是报错啊

报错的话是因为它找不到我们这个PD Goose Entity

咱们来看啊

PD Goose Entity

它这个版本号是什么呢

是这个1.0.0

这个地方是不是对不上啊

所以我们这个地方的需要来看一下这个version

对吧

这个version的话

是1.0.0

给它改

改好

好

这样是不是就没问题

那这样的话呢

我们把这个讲义呢

也一块来更新一下

要不然大家拷过来的话呢

可能会

会报这个错误

我们看啊

它在哪呢

这个地方

对吧

好

1.0.0

OK

这是把这个POM文件是不是搞定了

然后呢

我们需要来导入提供的这个配置文件啊

一个是这个什么呢

这个

一个是dozr

还有什么什么Mapper等等这些

好

这块呢

在咱们这个资料当中啊

其实已经提供好了

咱们来看一下

你看在我们这个资料通用权限系统

对吧

商品服务资料

刚才我们创建数据库呢

对吧

创建那个表

然后这有这个键表脚本

然后呢

后端工程对吧

后端工程相应的这个配置文件

对吧

配置文件

这一堆

整个都复制过来

好

复制过来之后呢

咱们大概来看一下这都是什么东西

好

然后呢

直接把它放到我们这个PDGoose Server

它的resource这个目录下面来

OK

然后呢

我们可以打开来看一下

你看这个dozr

这个呢

其实是做什么呢

对象转换呢

就是

以前我们可能做对象转换呢

都是使用什么呢

比如说使用binutils

对吧

将一个对象的这个属性

把它拷贝到另外一个对象里面去

也就是对象转换

咱们使用这个dozr呢

就可以完成

但是这里边呢

它其实都是空的这个文件啊

后期呢

我们如果比方说我从A对象需要转换成B对象

需要相应的进行配置啊

这块呢

我们没有这个转换的要求

所以就再放两个空文件

放这就可以了

然后呢

这是映射文件的吧

这是我们的一个映射文件

然后呢

接下来这是bootstrap

对吧

这是咱们这个文件啊

然后呢

还有这个日志的还有什么SPY的

这个其实是什么呢

相当于是

我们这个在控制台输出circle

使用它

输出circle

同时呢

它会给我们记录什么呢

这个circle它的执行时间

把这些配置文件的直接拿过来使用就可以了

好

这是这一步

然后接下来呢

我们就需要在咱们NUCLS配置中心当中啊

来创建什么呢

来创建一个新的这么一个配置文件

对吧

因为我们刚才创建了新的服务

而这个服务呢

肯定有自己特定的配置文件

那么就需要在我们这个配置中心当中来进行创建

然后这个配置文件的内容呢

我已经整理好了

整理到讲义上了

咱们直接把这个配置文件的内容拷过来

首先呢

我们需要先把这个文件名呢

是不是给它复制一下

来复制一下

然后把它创建到我们这个NUCLS当中来

好

当前呢

我使用的是这个空间

对吧

然后呢

这边

在这个配置里边

这边

然后呢

找到这个空间

然后呢

我们在这呢

来这个添加一个新的

对吧

添加一个新的

对吧

这是Data ID

好

然后这是这种YML

这种形式

对吧

然后具体这个文件的内容是什么呢

咱们就把这一块复制过来就可以了

好

重点看的是什么呢

品达MySQL Database

是不是使用的是PD-GOOSE

对吧

因为这我们要使用这个新的数据库啊

PD-GOOSE

就是我们这个商品数据库

然后这块呢

其实是我们这个SWAG文档

对吧

它要扫描这个包

一会儿呢

我们是不是就需要来

我们的control了

要创建在这种包下边

还有一个就是这个端口号

好

然后呢

我们直接在这点发布就可以了

确定

这样的话呢

就已经发布完成了

这是关于我们这个配置中心

接下来呢

我们是不是来编写咱们这个服务的什么

启动类

对吧

服务的启动类

这个启动类的话呢

我们就把它放在这个包

com

ITK码

品达这个包下边

对吧

然后呢

我们先把这个包呢

来创建一下

然后在这下边来创建我们这个包的内容

然后呢

我们先把这个包呢

我们这个启动类

叫做

Goose Server Application

好

直接抄过来

然后具体这里边的代码呢

同样我也不再去写了

直接把这个代码抄过来

好

把启动类

把它粘贴在这个位置

对吧

这里边都是一些常规的配置

你看

Spring Boot Application

然后呢

什么Discovery Client

是作为我们这个发现客户端

对吧

因为它要到我们Nakas

这个注册中心

来查找服务

还有什么呢

这是不是服务的

熔断

对吧

还有这个什么呢

Enable Faint Clients

它可能需要进行

接口的远程调用

对吧

Faint接口远程调用

然后呢

还有什么事务

对吧

然后呢

就是这个日志

包括这个

这个呢

其实是我们自定义的一个注解

就是开启什么呢

校验

对我们数据进行校验

然后这边是不是正常启动

就可以了

好

这是关于我们这个启动类

就已经搞定了

然后接下来呢

还有几个配置类

对吧

这个配置类呢

咱们也是直接抄过来

就可以了

我们也不再去敲了

这个配置类放在哪呢

放在Goose Config

这个包下边

也就是说我们在

PinDar这个下边呢

来创建

叫做Goose

Goose

好

然后Config

对吧

在这个包下边来

创建我们这些配置类

而这些配置类的话呢

在咱们这个

后端工程

然后配置类

这提前已经整理好了

那么我们直接把它

怎么弄啊

复制一下

然后呢

放在这个下边来

OK

粘贴一下

这些配置呢

都是一些常规的配置

像我们这个什么Exception Configuration

是不是全局的一常处理

还有这个什么呢

数据库的配置

对吧

数据库的配置

这里边主要就是

把我们这个数据源对象

对吧

包括我们这个什么模板对象

这些给它创建出来

好

然后呢

这是关于我们这个MyBitPlus

对吧

它需要使用到我们这个拦截器

然后呢

还有这个什么呢

Web的一些配置

但是这个地方呢

你看它全都是继承的

继承的这个Base Config从哪来呢

其实它是来自于我们这个PD Tools里边的一些模块

比如说这个Base Config

它其实是在哪呢

是在我们这个PD Tools Common里边

一些基础的配置

所以这些配置呢

都是可以附用的

我们在这直接继承它就可以了

好

这是关于我们这个配置类就已经搞定了

然后接下来

咱们是不是来创建这个MyPool接口

好

因为我们要针对这个商品的配置类

我们要针对这个商品的配置类

然后接下来

咱们是不是来创建这个MyPool接口

我们要针对这个商品信息这个表

是不是进行增伤改查

所以我们在这呢

需要来创建这个接口

好

这些代码呢

我都直接抄了就

先把这个包是不是来创建一下

在哪呢

我们这个PD Goose Server

然后呢

这里边

把这个包结构创建好

DAO

对吧

然后呢

我们

这个叫做

Goose Info

MyPool

这个

注意它应该是接口对吧

Interface

好

然后呢

这个接口其实就非常简单了

因为我们使用的是MyBasePlus

所以直接继承它这个什么呢

BaseMapper这个附类就可以了

然后把这个实体是不是传进去

好

这个呢

我们就不再过多的解释了

然后呢

还有就是Service对吧

接口包括它的实现类

Service接口呢

咱们是不是需要来创建一个Service包

在这一层目录

然后来创建一个Service包

然后在Service包里面呢

我们来创建这个什么

Goose InfoService接口

然后这个接口呢

同样也需要继承一个附接口

而这个附接口呢

其实也是由这个什么呢

MyBasePlus给我们提供的

这个iService对吧

同样这是不是也要传进来这个实体的类型

然后呢

再来一个实体类

实体类呢

我们就创建在这个实现包里面

也就是impl

按照规范

对吧

把这个包结构呢

给它清晰的划分出来

然后呢

然后在这里边呢

来创建我们这个实现类

Goose InfoServiceimpl

这是按照流程正常来创建就行了

其实就是我们这个什么

Mipro呀

什么Service啊

Controller呀

对吧

把它三层啊

给它都创建出来

好

这是Service创建好

然后接下来我们是不是来创建一个Controller

先把这个包来创建一下

Controller包

然后这里边呢

来创建一个什么呢

叫做Goose InfoController

这么一个

控制器这么一个类

对吧

但是这里边呢

它肯定会直接调我们的Service

来完成一些增长改查的操作

对吧

整个代码呢

我就都复制过来了

其实就是一些增长改查

你看代码量比较多

对吧

然后呢

Ctrl C

整个把这个代码拷过来

是不是删除啊

什么更新啊

对吧

Save

这个新增啊

等等这些

这些代码呢

我不作为重点啊

重点还是再来强调一遍

就是什么呢

为大家演示一下

如何基于我们这个脚手架

对吧

在它的基础之上

来开发我们新的项目

所以我们这块呢

其实这个

所谓的这个商品服务

其实是做了

很大的简化对吧

主要就是展示一下

我们如何去开发

这个开发的流程

是什么样子

那么到这儿的话呢

咱们这个后端

业务功能了

就算是已经开发完了

对吧

就已经开发完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频课程为一个关于“常见组件与中台化”的技术教程，主要聚焦于一个名为 `pd-goods-server` 的后端服务的开发与集成。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何配置 Maven 项目、集成 Spring Cloud 生态（如 Nacos、Sentinel、Gateway）、实现数据持久化（MyBatis-Plus）、定义业务接口（Service、Mapper）以及通过 Swagger 提供 API 文档。整个过程强调了在微服务架构下，如何通过配置中心（Nacos）和网关（Gateway）来管理服务的路由和配置，体现了“中台化”开发的实践方法。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1: 项目初始化与依赖配置 (00:00 - 00:45)**
    *   展示了 `pd-goods-server` 项目的结构。
    *   在 `pom.xml` 文件中添加了 Spring Cloud、MyBatis-Plus、Spring Boot Configuration Processor 等核心依赖。
    *   配置了 `spring-boot-configuration-processor` 为 `optional=true`，以避免编译时冲突。

*   **章节 2: 数据库与配置中心集成 (00:45 - 01:15)**
    *   在 IDEA 中打开 `GoodInfoMapper.xml` 文件，准备编写 MyBatis 映射文件。
    *   切换到 Nacos 配置中心，演示如何创建新的配置文件，为后续的配置管理做准备。

*   **章节 3: 服务启动与核心配置 (01:15 - 01:45)**
    *   展示了 `GoodsServerApplication.java` 的主类代码，其中包含了 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableCircuitBreaker` 等注解，用于启用服务发现和熔断降级。
    *   在 `main` 方法中，通过 `Environment` 获取并打印了应用的端口和 Swagger 文档地址，用于验证服务是否启动成功。

*   **章节 4: 数据库连接与数据访问层 (01:45 - 02:15)**
    *   展示了 `GoodDatabaseAutoConfiguration.java` 文件，其中定义了 `SqlSessionTemplate` 和 `DataSource` 的 Bean，用于配置 MyBatis 和数据库连接。
    *   定义了 `GoodsInfoMapper` 接口，继承自 `BaseMapper<GoodsInfo>`，用于操作商品数据。

*   **章节 5: 业务服务与控制器 (02:15 - 02:45)**
    *   展示了 `GoodsInfoService` 接口，定义了业务方法。
    *   展示了 `GoodsInfoController` 控制器类，其中包含了 `@GetMapping` 和 `@DeleteMapping` 等注解，用于处理商品信息的查询和删除请求。

*   **章节 6: 网关路由配置 (02:45 - 03:00)**
    *   在 Nacos 配置中心中，演示了如何为 `pd-gateway` 服务添加新的路由配置。
    *   展示了 `zuul` 路由规则的配置内容，包括 `servable-path` 和 `retryable` 等参数。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容:**
    *   **大纲**: 展示了课程的结构，包括“中台概述”、“常用组件服务介绍”、“分布式ID”等章节。
    *   **章节标题**: 如“2.1.4.1 新项目开发”、“2.1.4.1.2 后端业务功能开发”、“2.1.4.1.3 配置网关路由规则”等。

*   **代码关键内容:**

    *   **Maven 依赖配置 (`pom.xml`)**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix
