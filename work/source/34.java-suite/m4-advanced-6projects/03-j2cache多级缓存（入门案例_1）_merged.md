# 03-j2cache多级缓存（入门案例_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才咱们是对J2Catch做了一个简单的介绍

接下来我们就通过一个入门案例这种形式

来学习一下J2Catch是如何使用的

首先第一步我们可以来创建一个Mainware工程

然后工程名就叫做J2Catch-Demo

跟咱们讲一保持一致

我直接复制一下

然后我们在这来创建一个新的Create New Project

创建一个新的Mainware工程

直接点Next就可以了

然后这个坐标我们可以来指定一下

看我们的IT黑码

然后咱们这个名字叫做J2Catch-Demo

然后Next

这个位置就在这

不用动了

直接点转成

然后创建好之后

我们需要来导一下这个坐标

稍等一下

首先我们这个项目还是基于Spring Boot来开发

这样比较简单一点

所以说我们可以来

记住我们的Mainware工程

我们可以来绘成一下什么呢

Spring Boot Starter Parent

好

咱们把这一段进来复制一下

记住它Spring Boot Starter Parent

然后版本号就是这个2.2.2

这个让它自动导入

然后接下来我们来导一下这个J2Catch相关的Mainware坐标

当然了

我们也需要把这个Web环境导一下

对吧

就是我们这个Spring Boot Starter Web

另外两个就是关于我们这个J2Catch的

前面也已经介绍过了

所以我们整个J2Catch的Mainware工程

我们可以整个把这个Dependency这一块呢

全都复制过来

好

复制一下

直接拿过来就可以了

那这样的话呢

我们这个PoM文件呢

就已经配置好了

对吧

这一步就已经搞定了

然后接下来呢

我们可以来编写一下什么呢

我们这个Spring Boot的配置文件啊

咱们就来创建这个就可以了

叫做application.yml

对吧

这是它默认的配置文件名称

好

在咱们这个Resource下边呢

然后呢

我们再来创建啊

创建这么一个文件

这里面这个配置呢

我就不再去敲了

咱们整个复制过来

复制过来之后呢

大概来读一下

大家可以看到这个配置还挺多

因为大部分的都是关于我们这个J2Catch的一些配置

直接粘贴到这个位置来

咱们来大概读一下

前面这个server.pod

这是我们那个端口号

然后呢

接下来是我们自定义的

这块就是指定我们这个redis啊

他这个服务地址

为什么要配置redis呢

前面我们在做这个J2Catch介绍的时候呢

也提到过了

那么它是一个两级框架

对吧

其中呢

L2级别的

那么这个缓存呢

我们可以集成redis

咱们这儿呢

就不用不使用这个memcatch了

我们使用redis

因为redis目前来说使用是更多的

所以说呢

我们在这儿呢

需要去配置一下这个redis

它的这个IP端口号以及密码等等这些

当然我们讲页上写的是这个本质的设置

这个本地的对吧

实际上呢

我们现在本地没有起这个redis服务

那么我远程的是有的

所以我们把这个地址改一下

咱们来看一下我远程的这个地址

就这个地址啊

68796342

这个地址

这是我提前已经搭建好的一个redis服务

他是在这个地址

所以我们把这个IP呢

来改一下

68.79.63.42

这是这个地址

然后呢

我们来看端口号的话呢

是多少呢

看一下

端口号注意是这个啊

是26379

并不是他默认的那个6379

他是26379

所以这个不要写错了

然后呢

我们这个地方呢

还使用到密码了

这个密码的话是这个

把这个密码配置一下

这个数据库呢

我们就默认使用它的第一个数据库就可以了

零号数据库

好

大家可以看一下呢

现在呢

我们整个这个redis里边呢

现在是没有数据的

对吧

都没有数据都是空的

好

一会儿呢

我们就可以直接基于这个redis呢

来进行测试啊

好

那这块呢

我们就已经配置好了

注意看啊

咱们这这个是品达

是不是自己定义的呀

哎

这说明什么呢

下边呢

他可以引用我们

比如说这块才是真正啊

Spring Redis

对吧

这才是真正的我们这个配置

前面这块呢

其实是咱们自定义的

自定义的啊

你看

他这个host的

对吧

然后呢

他其实引用的就是我们品达redis IP

好

所以以后呢

我们改IP的话呢

你就直接改这儿就可以了

对吧

下边呢

全都是使用这种语法来引用

好

然后接下来呢

就是关于我们这个J2Catch相关的一些配置了

你看他这个是叫做J2Catch

然后呢

Clean Mode

这是他的这个清理的模式

对吧

好

然后呢

这个是否允许空值

是允许的

然后呢

这个redis client

哎

那这个呢

那么我们这个J2Catch框架

他底层是对redis进行整合

对吧

那么他要操作我们的redis服务

那么操作redis服务呢

就需要使用我们的Java客户端

对吧

那么Java客户端的话呢

咱们前面应该用的比较多的是Jadis

对吧

是Jadis

其实除了Jadis之外呢

另外还有一个Java客户端就叫这个叫做Lector

所以说呢

我们在这指定的这个redis的Java客户端

那么我们使用这个

当然你使用这个Jadis也是可以的啊

这个都没问题的

有关系

好

然后呢

我们这个L2CatchOpen

这是非常清晰了

对吧

L2级别的缓存

Open就是开启

对吧

然后呢

我们写个true

这就表示开启了我们的二级缓存

好

然后这个呢

就是这个broadcast的

对吧

其实就是我们这个实践通知的模式

实践通知的模式呢

咱们使用的就是这个redis啊

它的这个PubSubPolicy

这种策略

前面其实也简单提了一句啊

就是什么呢

它这个实践通知

对吧

缓存实践的通知

使用的是redis的这个方式

其实除了这种方式之外呢

还有一个叫做JGroups

那么这是两种不同的实践通知方式

咱们这个地方呢

使用的就是这个redis的

给我们提供的这种方式

然后接下来呢

咱们来指定一下我们这个L1

对吧

L1就是一级缓存

一级缓存呢

我们这个service provider

使用的是什么呢

Caffeine

其实除了这个Caffeine

还有什么呢

还有我们这个

E2CatchOpen

还有我们这个E2CatchOpen

刚才也看到了

就是一级缓存既可以使用这个E2Catch

也可以使用Caffeine

然后呢

我们在这使用的是这个

但这个呢

可能大家不太熟悉啊

这个呢

它是底层已经封装了

所以我们直接使用它就可以了

那么直接配置上就可以

然后接下来呢

是描述的是我们L2级别的这个缓存

对吧

L2级别的缓存呢

这个Providers Class

就是服务提供者

对吧

服务的提供者

那么使用的就是这个叫做

SpringRedisProvidersClass

但是这些呢

其实都是一些类

你看它这个是完整的类名

我们直接点进来啊

直接来搜一下

稍等一下

你看

往后拽一下

这个其实是在这个

J2CatchSpringBoot2Starter

对吧

这里边给我们提供的这么一个类

然后呢

它是用来处理什么呢

当我们这个L2级别的缓存

对吧

使用的时候

它要操作Redis

那么会使用这个类来操作

等等这些啊

下面全都是

关于我们这个L2

它的一些配置

然后呢

这块呢

我们一会儿可以测试一下

这个Serialization

这个指的就是我们

这个在进行这个Redis数据保存的时候

它的序列化的方式

对吧

序列化的方式呢

其实一共有这么几种啊

FST

还有什么这个对吧

还有什么Java等等

一会儿呢

我们可以分别来测试一下

它不同的这个序列化方式

其实对我们缓存数据的大小影响

还是非常大的

一会儿呢

我们可以来测试一下

好

所以这块呢

这是描述的我们这个J2Cache

对吧

描述J2Cache

然后接下来呢

是关于我们这个Caffeine

因为我们当前呢

这个L1

这个提供者是不是Caffeine

所以说呢

我们还需要对Caffeine进行一个描述

而它的描述的话呢

我们全都写到了一个配置文件里边

通过Properties

对吧

来指定配置文件的地址

所以说呢

关于Caffeine的配置呢

一会儿我们需要去编写这个配置

那么主要的配置项呢

都在这个文件里边

就在这里

叫Caffeine.properties

这个文件

好

然后这块呢

是关于咱们这个Redis客户端

对吧

Java客户端

Lecture它的描述

你看

刚才我们这儿

这不是已经指定了吗

咱们这个Java的客户端

对吧

是这个

Lecture

所以在这儿呢

又描述了Lecture

它的这一系列的配置

基本上都是一些常规的配置

比较重要的

比较重要的就是这块

Host

对吧

Password

数据库等等这些

因为它要操作

我们的

我们的这个Redis

好

那么整个啊

这个大概来读一下就可以了

因为都是一些常规的配置

对于这些配置项呢

那么我们只要能大概看懂

然后呢

会修改就可以

大家其实可以看一下

基本上我们要改的

也就是它这个IP

还有这个密码

对吧

IP端口号

还有这个密码等等这些

好

其他的地方呢

基本上都是固定的配置

好

这是关于咱们这个配置文件呢

大概来

浏览一下

然后下一步呢

我们是不是需要来提供这个文件呢

刚才提到了对吧

我们还差这么一个文件

所以接下来呢

我们就需要来提供啊

回到这边来

下一步呢

来提供这个文件啊

就叫做cafini.properties

我们把这个文件名的复制一下

不要写错了

放在哪呢

放在我们这个resource下边啊

因为你看它这个杠

这个杠呢

代表的就是根对吧

指的就是我们这个resource

所以我们在这呢

来创建这个文件啊

然后这里边配置的是什么呢

其实配置的还是比较简单的

一个是这个default

default指的就是什么呢

我们这个默认的策略对吧

因为我们在进行缓存的时候呢

是需要指定区域的

就是你将你的这个缓存数据

放在哪个区域

它有这么一个region

区域的概念

如果没有指定的话呢

它就会使用我们这个default

使用默认的

当然了我们你看我这是不是定义

这个叫做Rx的区域啊

所以我在缓存数据的时候呢

可以显示的指定

我这个数据放在这个Rx区域

如果不指定呢

它就会使用这个default

而这个default呢

默认指定的是什么呢

可以存放2000个对象

2000个数据

然后呢

存放的这个过期时间

注意看啊

第一个是数量对吧

是size

这上面这不也有描述啊

这是size

后边呢指定的是什么呢

指定的是缓存的时间

它的这个有效期对吧

2a是代表

就是两个小时

当然了除了这个h呢

你还可以写s对吧

s就是秒

m呢就是分钟

h呢是小时对吧

d呢指的就是什么呢

day就是天

所以说呢

我们可以用不同的单位啊

来描述

2h呢代表的就是两个小时

除了这个默认的呢

我们也可以自己去定义对吧

比方说我这有一个区域叫做Rx

那么我在缓存数据的时候呢

我就可以显示的来指定

我的数据呢缓存在这个Rx区域

然后呢

这个区域最多可以缓存50个数据

然后呢缓存的时长呢也是两个小时

所以呢我们把这块呢直接复制过来

一会呢我们也来测试一下

这样的话呢

我们这个文件呢就已经写好了啊

这是我们cafony它的一个配置文件

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于 **Spring Boot 项目集成 `j2cache` 缓存框架** 的技术教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何从零开始创建一个 Maven 项目，并配置 `pom.xml` 文件引入必要的依赖（包括 `spring-boot-starter-parent` 和 `j2cache`）。随后，讲师重点讲解了如何在 `application.yml` 配置文件中设置 Redis 连接参数，并配置 `j2cache` 以使用 Caffeine 和 Redis 作为一、二级缓存。视频中还展示了如何创建 `caffeine.properties` 配置文件，并在配置中指定缓存的模式、存储、命名空间等参数。整个过程旨在为开发者提供一个完整的 `j2cache` 入门配置案例。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，定位到“1.2 j2cache入门案例”章节。
*   **00:00:05 - 00:00:15**: 讲师切换到 IntelliJ IDEA，开始创建名为 `jcache_demo` 的 Maven 项目，并在 `pom.xml` 中配置了 `spring-boot-starter-parent` 作为父工程。
*   **00:00:15 - 00:00:30**: 讲师在 `pom.xml` 中添加 `j2cache` 的依赖，并通过 `<exclusions>` 排除 `slf4j-simple` 和 `slf4j-api`，以避免冲突。
*   **00:00:30 - 00:00:45**: 讲师切换到 `application.yml` 文件，开始配置 Redis 连接信息，包括 `ip`、`port`、`password` 和 `database`。
*   **00:00:45 - 00:01:00**: 讲师在 `application.yml` 中配置 `j2cache` 的核心参数，如 `cache-clean-mode`、`allow-null-values`、`redis-client` 和 `l2-cache-open`。
*   **00:01:00 - 00:01:15**: 讲师在 `application.yml` 中配置 `j2cache` 的 `provider_class`，分别指定一级缓存为 `caffeine`，二级缓存为 `SpringRedisProvider`。
*   **00:01:15 - 00:01:30**: 讲师在 `application.yml` 中配置 `caffeine` 和 `lettuce` 的详细参数，如 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。
*   **00:01:30 - 00:01:45**: 讲师在项目中创建 `caffeine.properties` 文件，并在 `application.yml` 中引用它。
*   **00:01:45 - 00:02:00**: 讲师在 `caffeine.properties` 文件中配置 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`1.2 j2cache入门案例`。
    *   配置说明：`j2cache-clean-mode: passive`，`allow-null-values: true`，`redis-client: lettuce`，`l2-cache-open: true`。
    *   依赖配置：`<dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-web</artifactId> </dependency>`。
    *   配置文件路径：`application.yml`，`caffeine.properties`。

*   **代码关键内容**:

    **`pom.xml` 依赖配置**:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```

    **`application.yml` 配置**:
    ```yaml
    server:
      port: 9000
    pinda:
      redis:
        ip: 127.0.0.1
        port: 6379
        password: 0
        database: 0
    spring:
      redis:
        host: ${pinda.redis.ip}
        password: ${pinda.redis.password}
        port: ${pinda.redis.port}
        database: ${pinda.redis.database}
    j2cache:
      cache-clean-mode: passive
      allow-null-values: true
      redis-client: lettuce #指定redis客户端使用lettuce，也可以使用Jedis
      l2-cache-open: true #开启二级缓存
      broadcast: net.oschina.j2cache.cache.support.redis.SpringRedisPubSubPolicy
      # broadcast: jgroups
      L1: #指定一级缓存提供者为caffeine
        provider_class: caffeine
      L2: #指定二级缓存提供者为redis
        provider_class: net.oschina.j2cache.cache.support.redis.SpringRedisProvider
        config_section: lettuce
        sync_ttl_to_redis: true
        default_cache_null_object: false
        serialization: fst #序列化方式：fst、kyro、Java
    caffeine:
      properties: /caffeine.properties #这个配置文件需要放在项目中
    lettuce:
      mode: single
      namespace: j2cache
      storage: generic
      channel: j2cache
      hosts: ${pinda.redis.ip}:${pinda.redis.port}
      password: ${pinda.redis.password}
      database: ${pinda.redis.database}
      sentinelMasterId:
      maxTotal: 100
      minIdle: 10
      timeout: 10000
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建 Maven 项目** (00:00:05 - 00:00:15)
    *   讲师在 IntelliJ IDEA 中右键点击项目根目录，选择 `New` -> `Module`，创建名为 `jcache_demo` 的 Maven 项目。
    *   讲师在 `pom.xml` 中添加了 `spring-boot-starter-parent` 作为父工程，并配置了 `j2cache` 的依赖。

*   **场景二：配置 Redis 连接** (00:00:30 - 00:00:45)
    *   讲师在 `application.yml` 中配置了 Redis 的连接参数，包括 `ip`、`port`、`password` 和 `database`。
    *   讲师在 `application.yml` 中配置了 `j2cache` 的核心参数，如 `cache-clean-mode`、`allow-null-values`、`redis-client` 和 `l2-cache-open`。

*   **场景三：配置缓存提供者** (00:01:00 - 00:01:15)
    *   讲师在 `application.yml` 中配置了 `j2cache` 的 `provider_class`，分别指定一级缓存为 `caffeine`，二级缓存为 `SpringRedisProvider`。
    *   讲师在 `application.yml` 中配置了 `caffeine` 和 `lettuce` 的详细参数，如 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。

*   **场景四：创建配置文件** (00:01:30 - 00:01:45)
    *   讲师在项目中创建 `caffeine.properties` 文件，并在 `application.yml` 中引用它。
    *   讲师在 `caffeine.properties` 文件中配置 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。

*   **场景五：配置文件错误提示** (00:01:45 - 00:02:00)
    *   讲师在 `application.yml` 中配置了 `caffeine` 和 `lettuce` 的详细参数，如 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。
    *   讲师在 `caffeine.properties` 文件中配置 `mode`、`namespace`、`storage`、`channel`、`hosts`、`password`、`database`、`maxTotal`、`minIdle` 和 `timeout`。

---
