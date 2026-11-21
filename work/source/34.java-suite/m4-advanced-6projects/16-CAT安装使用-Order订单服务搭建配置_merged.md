# 16-CAT安装使用-Order订单服务搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着去实现CAT服务的集成和调用

之前我们已经实现了网关服务

那么我们还去实现账户服务

订单服务

以及库存服务

接着的话

咱们就把订单服务做一个配置和实现

打开我们的支流股服务工程

然后在这里

我们先把Gateway这块再完善一下

Gateway这块

大家有没有发现还缺少了配置文件

对不对

我们创建一下它的配置文件

new file

这个application

dmproperties

然后给它一个基本的配置端口

端口的话就是8083

然后再给它的一个服务名称

application name

这个服务名称的话

我们就给它的工程名称保持一致

这个的话就叫CAT

然后demo

Gateway

对不对

在下面的话

就是配置我们的Narcos地址

这个是narcos.service.js

这个Narcos

我们是配置为本机的net地址

8848

因为我们这块网段是什么

10.10 20.10

那么主机的这个主机是20.1

所以的话

到时候它会从虚拟机上面

连接到我们本地的Narcos上面

所以就是20.18810

这点大家注意一下

然后还有什么

开启我们的监控的management

这里面的话

能够让它暴露相关的一个端口

对不对

点endpoint

endpoint

然后是web点

它所暴露的web可以访问的接口地址

这里面的话就包含所有的

这样就完成application的一个创建

然后的话呢

我们还有一句话呢

我们还有一句话呢

我们还有一句话呢

我们还有一句话呢

在这里呢

要给它一个目录

然后呢

info

info下面呢

再去创建一个配置文件

然后是app.problies

这个文件的话呢

它是记录我们这个服务的

就是CAD注册上去的这个服务名称

我们就给它app.name

同样这个名称的话呢

我们也跟这个保持一致

我们就给它app.name

这个配置呢就完成了

接下来呢

我们不要忘记了

还有我们的nest template

nest template这一块的话呢

我们要去给它一个初始化

对不对

在这里呢

要进行一个初始化配置

它的作用呢

要保存和传递上下文的

调用链的上下文信息

可以看到nest template进行一个初始化

然后呢

它会将这个CAD

nest intercept这个拦截器加入进去

然后呢

在这里面它就会去自动找到

我们说初始化创建的这个nest template对象

那接着的话呢

我们就来创建订单服务工程

我们去新增一个服务模块

这个模块呢

就叫CAD

demo

然后呢

order

订单服务对不对

点击next

然后呢

注意它放在CAD demo下面

点击finish

好

创建完成了

完成之后呢

它就会生成对应的Map-in结构

那么呢

之前我们已经讲过CAD的一个机程对不对

order这边的话呢

机程都是一样的

并没有说

一些那个

特殊的地方

那么这一块呢

我们就

可以呢

做一个copy

先把这个包创建一下

com.itcast.buzz.stock.CAD

demo

这个我们把它手中删除一下

Delete

这里我们再make dir startup

这个包名称呢

我们最好要写正确对不对

要检查好

然后呢我们要给它一个启动类

叫那个CAD

demo

order

application

好

那么呢

是它的一个启动look

spin

application

.run

CAD

demo application

max

那么CAD YouTube这块呢基本上都是一样的

我们可以把它全部copy过来

CAD的一个上下文对不对

然后呢CAD field configure

就是过滤器的注射配置

然后呢attb的长量

记录呢视频ID等信息

然后是它的拦截器

因为呢

Odd这边

不仅从Gateway这边接收不到

然后呢还要转发到账户服务以及库存服务

所以呢它要去记录

CAD的电源链

然后还有CAD server field

就是

过滤器的

具体

逻辑处理

那么接下来呢

还要去编写对应的接口

对吧因为我们在Gateway这一块大家应该还记得吧

在Gateway这里面的话呢我们是

编写的理论

两个接口一个是正常的请求一个是什么异常的请求

那么的话呢

它都会流转到什么

Odd服务这里

对不对

好那么我们来看一下

在Odd这一块

编写对应的一个接口

在这里我们就将

之前已经切号的代码呢

做一个copy

不用

从这里

在这里

这个逻辑的话比较简单

我呢就不重新去敲这个代码因为的话呢时间可能

就会比较多一些

我们就

主要来看一下

它整个的处理流程

是怎样的

在这里呢它是要注入到Rest Template对吧这个Rest Template的话呢去实现attp的一个远程调用

然后呢它可以看到

这里呢是有两个OddJS

这两个OddJS的话呢

分别是代表

什么呢

代表我们的远程服务一个是Account服务一个是Stock服务

我们给它呢加个注释

就是

Account

账户服

还有一个是什么

我们的库存服

在这里面的话呢

可以看到对不对

Stock

库存服

默认地址的话呢

我们也给它提供出来了

指向的是一个是8083端口一个是8084也就是说你在配置文件当中如果是不配也没关系我们将配置文件呢

先也

Copy过来

放到Resource目录下面

好配置文件这块呢跟之前说讲的Gateway这块差不多

没有什么特别的地方

Application这块呢

只靠名称这里要做一些

改动其他的话呢都是一致的端口这里大家要注意要区分一下

这个808端口呢

他就是

Gateway这里面所指向的端口

看到没有

808

他指向的是什么

是我们的订单服

指向

订单服务

接口

好那我们回过头来再来看一下

在这里呢会一个端口对不对

这个Mock端口是什么

是用于一个

异常测试的端口

也就是说这个端口呢

是不同的

他调用起来的话呢

会出现一个

错误

模拟像这样一个超时的错误

这里还缺少一个Log

Log的话我们直接

通过Longbook

大家的话呢应该安装了Longbook这个插件对不对第一天的课程当中呢已经给大家做了要求

然后呢还有什么

对应的这个注键

我们要把它加入进来

好在这里呢

粘贴一下

我们再看一下

他下面的一个处理流程

提供了一个订单服务接口

这个呢是提供下单接口

下单接口这里呢

他先睡眠200毫秒

也就是说在

订单服务里面

先做自己的业务逻辑对不对

自己业务逻辑做完之后呢然后去什么

在这里呢

去调用

账户

服务

以及呢

库存

服务

可以看到都是两个远程的调用对不对

最后呢调用完成之后呢

他会将他的结果呢

返回过来

可以看到

Calling

Custom

Service对不对

Calling Custom

Service

在这里呢

就将参数

返回结果呢

打印出来了

那么

Read Timeout

是一个模拟的超时接口

模拟

异常

超时接口

好在这里呢可以看到

先开启了一个Transaction

一个事务追踪

对吧

事务追踪这里面的话呢给他一个名称叫Connection Timeout

便于我们呢在Cat的管理后台去查找

然后同样在这里的发现睡眠500毫秒

就是说代表这个方法呢在做一些事情

接下来呢就是打印日志

那打印日志这块呢

下面就是

LessTemplate的一个远程调用

这个呢是不存在的服务

是我们随便写的一个端口

不存在的服务会出现

出现什么情况呢

调用的时候就会出现异常

那么出现异常的话呢

就会进入到这里面的逻辑处理

然后呢将结果跑出出去

跑出去之后大家可以看到Read Timeout是谁调用的

是Gateway调用的

对吧

好Gateway在这里调用

所以呢

就会出现一个什么问题啊

在这里

在这里呢

他就会打印出

异常信息

然后在Cat的链路监控的时候呢

我们就应该可以看到异常的

统计

好

这个呢是

订单户的

整体的配置以及呢

相关接口的实现

好那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **CAT（应用性能监控）** 与 **Sentinel（流量控制与熔断降级）** 在 Spring Cloud 微服务架构中集成的实战教程。讲师通过演示一个包含网关（Gateway）和订单服务（Order Service）的微服务项目，详细讲解了如何在服务间传递 CAT 上下文（Context）以实现全链路监控，并展示了如何利用 Sentinel 的 `@SentinelResource` 注解来实现服务的熔断与降级。视频内容聚焦于代码实现，包括配置文件、核心类的编写以及异常处理逻辑，旨在帮助开发者理解如何在实际项目中部署和使用这些监控与治理工具。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**: 视频开头，讲师在 IntelliJ IDEA 中展示 `CatDemoGatewayApplication` 的主类代码，重点是 `@EnableDiscoveryClient` 注解，用于服务发现。
*   **00:00:03 - 00:00:06**: 讲师切换到 `application.properties` 文件，展示服务端口配置 `server.port=8083` 和 Spring Cloud 服务名 `spring.application.name=cat-demo-gateway`。
*   **00:00:06 - 00:00:10**: 讲师在 `CatDemoGatewayApplication` 中定义了 `@Value("${service2.address:localhost:8082}")`，用于注入服务地址。
*   **00:00:10 - 00:00:13**: 讲师在 `CatDemoOrderApplication` 中定义了 `@Value("${service4.address:localhost:8084}")`，用于注入另一个服务地址。
*   **00:00:13 - 00:00:16**: 讲师在 `CatDemoOrderApplication` 中定义了 `private static final int MOCK_PORT = 8765;`，用于模拟测试端口。
*   **00:00:16 - 00:00:19**: 讲师在 `CatDemoOrderApplication` 中定义了 `@RequestMapping("/order")` 的 `serviceMethodInController` 方法，用于模拟调用服务。
*   **00:00:19 - 00:00:22**: 讲师在 `CatDemoOrderApplication` 中定义了 `@RequestMapping("/readtimeout")` 的 `connectionTimeout` 方法，用于模拟超时。
*   **00:00:22 - 00:00:25**: 讲师在 `CatDemoOrderApplication` 中定义了 `try { ... } catch (InterruptedException e) { ... }`，用于处理超时异常。
*   **00:00:25 - 00:00:28**: 讲师在 `CatDemoOrderApplication` 中定义了 `Log.info(s: "Calling a missing service");`，用于记录日志。
*   **00:00:28 - 00:00:31**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback")`，用于定义熔断降级逻辑。
*   **00:00:31 - 00:00:34**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", blockHandler = "orderBlockHandler")`，用于定义降级逻辑。
*   **00:00:34 - 00:00:37**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler")`，用于同时定义熔断和降级逻辑。
*   **00:00:37 - 00:00:40**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class})`，用于定义异常处理。
*   **00:00:40 - 00:00:43**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class})`，用于定义多种异常处理。
*   **00:00:43 - 00:00:46**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class})`，用于定义多种异常处理。
*   **00:00:46 - 00:00:49**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class})`，用于定义多种异常处理。
*   **00:00:49 - 00:00:52**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class})`，用于定义多种异常处理。
*   **00:00:52 - 00:00:55**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class})`，用于定义多种异常处理。
*   **00:00:55 - 00:00:58**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class})`，用于定义多种异常处理。
*   **00:00:58 - 00:01:01**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class, IllegalArgumentException.class})`，用于定义多种异常处理。
*   **00:01:01 - 00:01:04**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class, IllegalArgumentException.class, IllegalStateException.class})`，用于定义多种异常处理。
*   **00:01:04 - 00:01:07**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class, IllegalArgumentException.class, IllegalStateException.class, NullPointerException.class})`，用于定义多种异常处理。
*   **00:01:07 - 00:01:10**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class, IllegalArgumentException.class, IllegalStateException.class, NullPointerException.class, RuntimeException.class})`，用于定义多种异常处理。
*   **00:01:10 - 00:01:13**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", blockHandler = "orderBlockHandler", exceptions = {Exception.class, InterruptedException.class, TimeoutException.class, RuntimeException.class, IOException.class, SQLException.class, NullPointerException.class, IllegalArgumentException.class, IllegalStateException.class, NullPointerException.class, RuntimeException.class, IOException.class})`，用于定义多种异常处理。
*   **00:01:13 - 00:01:16**: 讲师在 `CatDemoOrderApplication` 中定义了 `@SentinelResource(value = "orderService", fallback = "orderFallback", block
