# 14-CAT安装使用-GateWay网关服务搭建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来,我们就开始对CAT做集成配置

首先,我们来实现CAT Demo复制工程的创建

以及CAT的依赖的集成配置

我们打开支流股复工程

在这里新建一个模块

Model,这里面选择Maven

就按默认的模板,点击Next

在这里我们给它一个Artifact ID

这里就叫CAT Demo

它会继承复集的Global ID以及Watch

点击Next

在这里我们修改下Model名称,叫CAT Demo

点击Finish

这样CAT Demo就已经创建完成

创建完成之后,我们首先要将它的依赖加入进来

这个Defenses

然后我们将CAT的主要配置

在这里复制进来

这个是让它导入生效,引发的欠据

好,我们看一下有哪些依赖呢

首先是Splendor Boot的依赖

因为这个是一个微服务

我们要通过Splendor Boot做启动

然后还有Narcos服务注册发现依赖

在这里我们是通过Narcos对所有微服务节点做了统一的注册发现管理

Splendor Boot的监控主线依赖

这个是必须要加入进去

否则的话CAT有些信息它是拿不到的

然后CAT的主线依赖,这个也是CAT的核心

在这里面我们可以看到它引入的是什么

CAT的client模块

只要加入CAT client模块就可以了

这些就是整个的CAT的一些依赖

那么我们在这里还要去创建它相关的一些拦截器

这些拦截器在哪装建呢?

这个就要在我们应用服务当中去创建

我们应该还记得上一讲当中讲过的有四个应用服务

有CAT Demo Account,还有CAT Demo Gateway,Order,Stock

那么我们就首先来创建一下Gateway服务网关工程

我们将这个拨币一下

然后在CAT Demo上面右键New Model

点击Next

在这里采用CAT Demo Gateway

然后这个改了,让它名字改一下

注意我们这个目录它在什么?

CAT Demo下面

要注意它的复集工程不是Buzzstock

是CAT Demo

Buzzstock是它的复集的复集

这个是它的一个根基目录

好,点击Finish

这样它就会在上面创建一个模块

然后Import Changes

好,Import Changes

它会去加载相关的一个额外的项目

依赖,Gateway这边

Gateway它不需要加入任何依赖

因为它会去继承CAT Demo上面的所填写的依赖组件

CAT Demo,可以看到,对不对?就是我们刚才所加的

好,那么我们要给它做一个Build

Build下面的话要去添加它的一个构建的插件

这个我们就可以沿用这一块

采用的Spring Boot

Spring Boot帮助我们去做一个构建

好,就这个

那么将它Copy过来

这个是要叫什么?Plugins

然后是一个Plugin

这样它就会按照Spring Boot的方式进行一个打包和配置

它会默认找到对应的一个版本

因为我们的话最复集上面是采用什么?Plugin Management

就会在这里面找到它最优的一个配置

好,这一块就是Gateway的它的一个依赖的

接下来我们还要去创建它的一些栏接器,对不对?

还有CAT相关的一些配置

那么我们先把包创建一下

New Package

然后我们要com.itcast.bossstock

然后在这里面的话它是一个CAT,对不对?

CATdemo.Gateway

好,创建完成之后

首先我们同样要去创建一下它在这里面的Startup

然后我们再创建另外一个包

CATutils,专门去实现CAT的一些配置

那我们直接Open in terminal

cd.make dir

这个就CATutils

好,这个时候我们再看这个包

是不是已经创建完成两个包了,对不对?

那我们的话先来去实现它的启动内

好,那么我们右键创建一个class叫CATdemo

然后呢,Gateway,Application

在这里呢,我们可以看到CATdemo,Application

这个已经创建完成,对不对?

因为刚才选的是一个单例,这个没关系

我们再去编写一下它的一个启动内

启动接口

这个PSVM,然后这里会生成我们的VoidMEM方法

然后要去启动SpringApplication

点,Run

CATdemoApplication.class

然后将参数传递进去

好,接着的话呢,我们还要给它加上注解,对不对?

SpringBootApplication

然后,还要加上什么注解呢?

EnableDiscoverClient,对不对?

作为那个NUCLEUS的服务注释发现

然后呢,我们再加上一个注解,CompandScan

就是服务的一个扫描

那么服务扫描这边的话呢,BasePackage

让它扫描我们的一个基础包

这个基础包呢,就叫Comp.itcast

就是我们的一个根基目录的包

它是可以支持多个的

Comp.itcast

好,CompandScan这边的话呢

因为我们是在Startup上面放置了启动内,对不对?

如果是你启动内,在这一个层级下面

它会默认找到它对应的这个层级

以及这个层级下面的这个包

但是我们并不是放在这个Gateway这个层级下面

所以我们还是让它选择这个

去扫描Comp.itcast,对不对?

因为后面的话呢,我们肯定还会添加很多的结包

在实际生产应用当中呢

我们建议大家也是要指定具体的一个包

就是扫描包的一个路径

接着的话呢,我们还要给Gateway定义两个接口

怎么两个,哪两个接口呢?

一个是访问正常的请求

另外一个是模拟访问一个错误的请求

这样的话呢,我们要通过Cat链路监控

就可以查看一下正常跟错误的

到底是怎么去跟踪,怎么去分析,对不对?

那我们呢,要给它呢,去做一个定义

定义的话呢,我们使用ListTemplate做这样一个调用

ListTemplate

ListTemplate我们要将它注入进来

iVT,然后呢,AutoWide

ListTemplate注入完成之后呢

我们呢,再给它

一个地址

这个地址的话呢,就是用于去模拟我们的一个错误的请求

这个地址的话呢,我们就叫String

Service

Service.js

就指向一个服务地址

这个服务地址的话呢,我们可以让它通过那个变量注入进来

比如说这里面的话呢,是Service

Service.js

这个呢,是第一个服务的调用,对不对?

这个是第二个服务的一个调用

我们在这里面呢,给它一个默认值

默认值的话呢,我们就指向Localhost本地,然后呢,8082的一个端口

好

这样呢,Service.js配置完成

配置完成呢,我们就来实现两个接口

这两个接口呢,首先是一个正常的一个请求

我们给它呢,上面要加上ListController

通过SupplyPool进行访问调用

然后呢,定一个接口

这个接口名字呢,PublicString

然后呢,我们给它一个Gateway

访问的是我们的Gateway接口

那么Service将它的异常呢,抛出来

一个Service

这个呢,我们给它一个路径

RequestMapping

这个Mapping的话呢,我们就叫Gateway

好

那这个创建完成之后呢,这个逻辑我们怎么去调呢

我们呢,首先来将线程呢,做一个休眠,对不对

这样我就能看到Gateway这边耗费了多长时间

Sleep,然后这里呢,100毫秒

接着的话呢,我们再去做一个远程的调用

视讯,然后呢,Response

在这里呢,通过ListTemplate

进行远程的访问

Gateway for Object

OBJ1

然后ListTemplate这一块呢,我们怎么去调用呢

大家有没有印象

好,这边的话呢,就要拼接URL的地址

ATTP,然后是采用ATTP的协议,对不对

再加上什么

再加上我们的那个服务的地址

然后我们给它拼接一下Service.js

在这里呢,让它访问什么,订单服务

对不对,然后是String.jpg

class

通过String做这样一个序列化阻力

数据的一个参数的传递

然后呢,我们再返回一个结果

return

Gateway

告诉你呢,这个是Gateway的一个返回输出,对不对

然后呢,再将它的结果输出来,Response

那这个呢,就是Gateway接口的一个请求实现

我们加个注释

模拟呢,正常的请求

这个是由Gateway提供出来的一个接口,对不对

那么我们还要再模拟一个什么

再模拟一个错误的请求

我们再去编写一个接口

这个呢,就给它一个Timeout

比如说有个Timeout的异常,对吧

那这个,我们怎么去写呢

一个Sum

然后在这里面的话呢

我们要去采用那个Cat,对不对

Cat这一块的话呢,就要开始接入进来

我们先给它一个请求路径

RequestMapping

这个呢,就跟方法名一致

叫Timeout

给它一个注释

模拟一个请求异常

这样呢,我们就能够

通过对比,更加呢

方便的,直观的,帮助我们去分析整个链路

跟踪调用的情况

那在这里呢,我们首先要

开启一个事物

Transaction

在这里面的话呢

它的作用是要Cat的一个追踪使用的

然后在这里呢,是Cat.newInstance

NewTransaction

创建一个Transaction

好,创建完Transaction之后呢

给它一个参数,叫Cat.consistence

然后呢,type UL

再给它一个名称,叫Timeout

好,接着的话呢

我们就要去做一个check catch

我们就要把这个参数的异常的捕获

在这里面的话呢

捕获Exception

然后呢,将它的异常

我们要把它放到Cat里面

GetProbably

Producer

然后呢,要给它一个日之的记录

然后呢,将Exception传递进去

接着的话呢,我们还要给它一个标记

TsetStates

同样,也将这个Exception传入进去

然后呢,我们再将它异常包出去

最后呢,别忘记了

我们要去完成整个事物的处理

对吧

要去做相关的一些动作的示范

我们可以看一下

在那个Cat里面

对不对,如果是你结束之后

它要做一些状态的标记

然后呢,还做一些事物结束的处理

好,那么在这里具体逻辑该怎么去调呢

我们同样先让它

Sled.Sleep

先让它呢,睡眠100毫秒

然后呢,String.LessPounds

做一个调用

通过LessTemplate的方式

GetForObject

然后呢,是HTTP的协议

再加上你的请求地址

Service.Adjust

然后呢,我们再加上一个Timeout

这里呢,参数传递String.Cast

好

接着的话呢

我们再返回它的一个LessPounds对象

即使呢

它应该不会走到这里

因为它这里呢

就会调用报错

会进入到一个Supply

这个呢

我们没关系

给它一个方法的结束处理

对不对

好,这个就是Timeout

也就是我们的GetAway

这边实现的两个接口

好

再往下面呢

我们还在应用服务当中

去对这些接口呢

还做一个提供

做具体实现

那这一讲呢

咱们先讲完

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的微服务架构项目中，`CAT`（一个分布式应用性能监控系统）集成的实践演示。讲师通过 IntelliJ IDEA 开发环境，逐步展示了如何在网关服务 `cat-demo-gateway` 中集成 CAT 的核心功能，包括：

*   **依赖管理**：在父级工程 `cat-demo` 的 `pom.xml` 中引入 CAT 客户端依赖。
*   **服务结构**：展示网关服务的 `pom.xml` 和 `CatDemoGatewayApplication.java` 主类。
*   **核心功能演示**：演示如何使用 `RestTemplate` 发起 HTTP 请求，并在请求中集成 CAT 的事务（Transaction）和异常（Exception）监控功能。
*   **代码实现**：通过注解 `@EnableDiscoveryClient` 启用服务发现，通过 `@TransactionalWriter` 注解来标记事务，并通过 `Cat.getProducer().log()` 方法记录日志。

整个过程旨在说明如何在 Spring Cloud 微服务架构中，将 CAT 监控能力无缝集成到网关服务中，以实现对服务调用链路的监控和异常追踪。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示课程大纲，定位到“3.5 CAT集成事项”章节。
*   **00:05 - 00:15**: 展示父级工程 `cat-demo` 的 `pom.xml` 文件，重点是引入 `cat-client` 依赖。
*   **00:15 - 00:25**: 切换到网关服务 `cat-demo-gateway` 的 `pom.xml`，展示其模块定义和版本管理。
*   **00:25 - 00:35**: 展示 `cat-demo-gateway` 的 `pom.xml` 中的 `build` 配置，包括 `spring-boot-maven-plugin`。
*   **00:35 - 00:45**: 展示 `CatDemoGatewayApplication.java` 的主类，包含 `@SpringBootApplication` 和 `@EnableDiscoveryClient` 注解。
*   **00:45 - 00:55**: 在主类中添加 `@ComponentScan` 注解，并定义 `RestTemplate` 和 `serviceAddress` 字段。
*   **00:55 - 01:05**: 编写 `@RequestMapping("/timeout")` 方法，用于模拟一个请求异常。
*   **01:05 - 01:15**: 在 `timeout` 方法中，使用 `Cat.getProducer().log()` 记录日志，并通过 `@TransactionalWriter` 注解标记事务。
*   **01:15 - 01:25**: 在 `timeout` 方法中，使用 `Thread.sleep(millis)` 模拟请求耗时，并通过 `Cat.getProducer().log()` 记录日志。
*   **01:25 - 01:35**: 编写 `@RequestMapping("/gateway")` 方法，用于模拟一个正常的请求。
*   **01:35 - 01:45**: 在 `gateway` 方法中，使用 `RestTemplate` 发起 HTTP 请求，并通过 `Cat.getProducer().log()` 记录日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.5 CAT集成事项`
    *   **关键说明**: `cat-demo父级工程的POM依赖：引用最新版本cat组件`
    *   **依赖配置**:
        ```xml
        <dependency>
            <groupId>com.dianping.cat</groupId>
            <artifactId>cat-client</artifactId>
            <version>3.0.0</version>
        </dependency>
        ```

*   **代码关键内容**:
    *   **网关服务 `pom.xml`**:
        ```xml
        <modules>
            <module>bulls-stock-gateway</module>
            <module>bulls-stock-user</module>
            <module>cat-demo</module>
        </modules>
        ```
    *   **主类 `CatDemoGatewayApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = {"com.ictast"})
        public class CatDemoGatewayApplication {
            @Autowired
            private RestTemplate restTemplate;
            private String serviceAddress;
            public static void main(String[] args) {
                SpringApplication.run(CatDemoGatewayApplication.class, args);
            }
        }
        ```
    *   **异常处理方法 `timeout`**:
        ```java
        @RequestMapping("/timeout")
        public String timeout() throws Exception {
            Transaction t = Cat.newTransaction(CatConstants.TYPE_URL, "timeout");
            try {
                Thread.sleep(millis);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            t.log();
            t.end();
            return "timeout";
        }
        ```
    *   **正常请求方法 `gateway`**:
        ```java
        @RequestMapping("/gateway")
        public String gateway() throws Exception {
            String response = restTemplate.getForObject(url + serviceAddress, String.class);
            return "gateway response --> " + response;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖引入 (00:05 - 00:15)**
    *   讲师首先展示了父级工程 `cat-demo` 的 `pom.xml` 文件，重点是 `<dependencies>` 部分，其中包含了 `cat-client` 依赖。
    *   通过鼠标点击和高亮，强调了 `cat-client` 的 `groupId`、`artifactId` 和 `version`。

*   **场景二：网关服务配置 (00:15 - 00:35)**
    *   讲师切换到 `cat-demo-gateway` 的 `pom.xml`，展示了其 `modules` 配置，表明它是一个模块化的项目。
    *   展示了 `build` 配置，包括 `spring-boot-maven-plugin`，用于打包和运行 Spring Boot 应用。

*   **场景三：主类与注解配置 (00:35 - 00:55)**
    *   讲师展示了 `CatDemoGatewayApplication.java` 的主类，高亮了 `@SpringBootApplication` 和 `@EnableDiscoveryClient` 注解。
    *   通过 `@ComponentScan` 注解，指定了组件扫描的包路径。

*   **场景四：异常处理与CAT集成 (00:55 - 01:15)**
    *   讲师编写了 `@RequestMapping("/timeout")` 方法，用于模拟一个请求异常。
    *   在方法中，使用 `Cat.getProducer().log()` 记录日志，并通过 `@TransactionalWriter` 注解标记事务。
    *   通过 `Thread.sleep(millis)` 模拟请求耗时。

*   **场景五：正常请求与CAT集成 (01:15 - 01:35)**
    *   讲师编写了 `@RequestMapping("/gateway")` 方法，用于模拟一个正常的请求。
    *   在方法中，使用 `RestTemplate` 发起 HTTP 请求，并通过 `Cat.getProducer().log()` 记录日志。
    *   通过 `Cat.getProducer().log()` 记录日志，实现对正常请求的监控。

---

以上是根据视频画面进行的结构化分析报告，旨在帮助理解视频中展示的技术内容和实现过程。
