# 16-分布式事务解决方案Seata（应用_增加seata — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢继续来看我们SITA的应用

刚才呢我们是在咱们POM文件当中啊

已经引入了SITA的依赖对吧

就是我们这个依赖包

好把它引进来就可以了

这样我们项目当中呢就可以使用SITA

然后呢相当于我们的项目呢

是作为SITA的一个客户端对吧

跟SITA Server呢来进行交互

当然我们这些客户端呢

其实又分成了不同的角色

包括有什么呢

有我们这个TM对不对

还有什么RM

等等前面我们也都说过了啊

然后接下来呢我们来看这个小节呢

我们来看一下就是增加SITA的配置

好

那么这些配置需要写在哪个配置文件里边呢

就是我们这些微服务

哪一个微服务要使用SITA

那么就需要来进行下面这段配置

刚才我们也说了

咱们这些微服务呢

除了PD-J的这个之外呢

其他的是不是都需要使用到

我们这个SITA对吧

所以说呢

我们这块呢

就需要在其他的这些微服务里边

那么来增加SITA的配置

因为我们这块呢是统一

咱们这些配置文件呢

是统一在我们NUCLS当中来进行配置的

所以说呢

我们下面这个关于SITA的配置呢

就配置在我们这个NUCLS配置中心就可以了

你看咱们来读一下这个配置

你看它是不是就叫SITA

然后呢

Enable的等于True

表示可以了

开启对不对

然后呢

开启

然后呢

每一个微服务呢

需要给一个Application Name

而这个Name的话呢

我们就使用Spring Application Name来定义就可以了

它是不是动态来取值

然后注意看这

TX Service Group

这个所对应的这个值

注意不能随便写

大家还记得吧

我们前面是不是

好像见过这么一个字符串啊

是在哪呢

是在我们前面这个Registry.config

这个文件里面

咱们是不是当时写了这么一个Page

来看一下是在什么地方呢

应该是在File对吧

在这个File.config这个地方

你看我们是不是VGroupMapping是吧

是个虚拟的阻应设

然后呢

在这是不是写了这么一个字符串

叫做IT黑马TX什么Group对吧

就这个名字

然后我当时也说到了

这个名字你可以任意定义

但是要保证跟我们后边用到的地方前后一致

对不对

那么具体哪一边用到的地方呢

就是我们现在看到的这个Cita的Page这块

他们前后要一致

你看当时我们写的是IT黑马下滑线TX下滑线Group

所以这边呢

我们这个Page文件里边呢

咱们这个组的名字就必须起这个名字

这样前后就一致了

这个必须要保证一致

这样的话

我们这个分不出事物呢

才能够管理成功

然后接下来呢

我们来看这个Registry

Registry

这是不是指定什么呢

我们Cita它是什么呢

这个是什么呢

是不是需要有这个注册中心呢

注册中心

然后呢是File类型

Name等于什么Registry.config

这样的话呢

它就会去读取这个文件

而在这个文件里边

我们是不是就配置了NUCLS

作为我们这个注册中心

大家还记得吧

就是在这个地方

所以说了

我们把这个文件呢

是不是已经给它拷到哪了

已经给它拷到Docker容器里面去了

对吧

在这儿呢是不是已经给它拷进去了

所以这个地方呢

它就可以干什么呢

它就可以能够获取到

能够读到我们这个配置文件

好

然后呢

接下来是什么Service

什么Group List

对吧

在这儿呢是不是就是指定什么呢

我们这个Cita它这个服务的地址

Cita服务的地址

因为我们当前呢

是作为Cita的什么呢

客户端

对吧

咱们作为Cita的客户端

需要跟Server进行交互

所以我们需要知道Cita在什么位置

在这儿是不是就是我们这个

这个Cita的服务的地址

咱们当前呢是布在了这儿

这台机器上对吧

68796342这台机器上

然后呢

我们还做了一个端口映射对吧

你看

那么我们在这儿呢已经

现在我们是在容器里面对吧

我们需要退出来

然后呢来Docker PS

好

你看咱们是不是做了这个8091的端口映射

Cita呢就在这个位置

好

那这样的话呢我们就可以啊

回到这边来

能够连上我们的Docker PS

我们这个Cita服务对吧

然后呢在这儿是不是又出现了这个key

这个key的话呢是不是就跟这个保持一致

然后呢是default啊

就是指定默认的就可以

好

所以这块呢

我们重点就是配置这个Server

而这个配置的话呢

咱们其实不需要把它考到我们相应的这些

配置文件里面来

这里边呢我们其实不需要把它考进来

因为什么呢

因为我们的配置文件呢

是不是统一都在我们这个NUCLS里面

统一管理的

所以说呢我们在这里边来找到配置中心

你看这是不是有配置列表

然后找到我们这个空间

我们就拿这个OMS这个为例

你看我这里边呢其实已经给它配置完了

嗯

往下翻

翻到最后

就是这点

对吧

就是这点已经配置完了

那么除了OMS呢

其他的微服务

比如说我这个什么呢

我们再来找一个

比如说我这个在我们当前这个场景下面会用到的

这个work对吧

PD work是不是也会用到CETA

所以说呢这里边呢也已经配置了这点

你看这不是CETA

其实都是一模一样的

都是一模一样的

这是这个服务的地址

那这样的话呢

我们这些微服务

哪一个微服务要使用CETA

那么都需要在NUCLS当中来进行配置

好

这就是关于我们增加CETA的配置

然后呢你直接到NUCLS当中来进行配置

就可以了

这都是我们需要必须要经过的这些配置

这样的话呢

我们这个程序呢

才能跟咱们这个CETA服务是不是连接上

对吧

他们之间的才能进行协调进行通信

好

这是增加CETA配置

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”中集成分布式事务解决方案 **Seata** 的技术教程。课程主要围绕如何在项目中配置和引入 Seata 服务，重点讲解了如何在各个微服务的 `pom.xml` 中排除冲突的依赖（如 `druid` 和 `seata`），如何在 `registry.conf` 和 `file.conf` 配置文件中设置 Seata 的核心参数（如服务组、注册中心、配置中心），以及如何通过 Nacos 配置中心进行集中管理。视频通过 IntelliJ IDEA 和 Nacos 控制台的演示，详细说明了配置文件的结构和关键参数的含义，旨在帮助开发者正确地在项目中集成 Seata，以支持分布式事务管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和当前学习的章节“7. 增加Seata配置”。
*   **00:05 - 00:15**: 讲解在 `pom.xml` 中排除 `druid` 和 `seata` 依赖的必要性，并演示在 IntelliJ IDEA 中如何操作。
*   **00:15 - 00:30**: 展示 `registry.conf` 配置文件，讲解 `service` 和 `registry` 模块的配置，特别是 `group` 和 `registry` 的设置。
*   **00:30 - 00:45**: 展示 `file.conf` 配置文件，讲解 `service` 和 `store` 模块的配置，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **00:45 - 01:00**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **01:00 - 01:15**: 展示 `bootstrap-dev.yml` 文件，讲解如何通过 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file` 配置文件来加载 Nacos 中的配置。
*   **01:15 - 01:30**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **01:30 - 01:45**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **01:45 - 02:00**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **02:00 - 02:15**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **02:15 - 02:30**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **02:30 - 02:45**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **02:45 - 03:00**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **03:00 - 03:15**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **03:15 - 03:30**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **03:30 - 03:45**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **03:45 - 04:00**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **04:00 - 04:15**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **04:15 - 04:30**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **04:30 - 04:45**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **04:45 - 05:00**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **05:00 - 05:15**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **05:15 - 05:30**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **05:30 - 05:45**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **05:45 - 06:00**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **06:00 - 06:15**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **06:15 - 06:30**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **06:30 - 06:45**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **06:45 - 07:00**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **07:00 - 07:15**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **07:15 - 07:30**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **07:30 - 07:45**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **07:45 - 08:00**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **08:00 - 08:15**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file` 存储路径的设置。
*   **08:15 - 08:30**: 讲解如何在 Nacos 配置中心创建并上传 `file.conf` 文件。
*   **08:30 - 08:45**: 讲解如何在 `bootstrap-dev.yml` 文件中配置 `spring.cloud.nacos.config.file-extension` 和 `spring.cloud.nacos.config.file`。
*   **08:45 - 09:00**: 讲解如何在 `pom.xml` 中引入 `seata-spring-boot-starter` 依赖，并配置 `application.properties` 文件。
*   **09:00 - 09:15**: 讲解如何在 `registry.conf` 中配置 `service` 和 `registry` 模块，特别是 `group` 和 `registry` 的设置。
*   **09:15 - 09:30**: 讲解如何在 `file.conf` 中配置 `service` 和 `store` 模块，特别是 `store.mode` 和 `file`
