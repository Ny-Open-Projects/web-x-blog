# 37-SEATA介绍-SEATA案例工程搭建和配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习Sita案例的搭建和配置

首先咱们来看一下整个的工程结构

官方Demo实现有些长处

存在一些bug

依赖也比较混乱

因为它集成了double

这里我们重新做了一个调整

去除double

简化它的一个依赖

集成到我们工程当中

便于学习和演示

官方地址我们可以访问一下

这个是官方的Sita sample的一个地址

在这里它采用Slimboot

JPA double

然后德鲁伊的数据源

我们简化了double

在这里通过Slimboot跟Sita的一个集成

便于我们的一个学习和验证

好

这里Sita我们的版本

之前在编写讲义当中

采用的是0.4.0的一个版本

因为它更新比较频繁

所以它也会存在一些bug

我们可以看一下

目前的版本是到哪里

这个是官方的地址

在上面的话

我们可以看到

最新版本已经到1.1.0的一个版本

当然这个并不是一个最终的正式版

最终正式版是GA的版本

就是这个

这个稳定性来讲的话

会比较可靠一些

如果大家要在生产环境当中去运用

最好是采用GA的一个版本

那阿里推出来的话

Sita是一个开源主线

那么推出开源的目的

还是希望大家

可以采用阿里的收费的产品

那么阿里也推出了GTS的这样一个分布式事务解决的组件

这个GTS它相比Sita有什么不一样呢

它在这里呢

如果是大家采用Sita的1.0.0GA以上的一个版本

它可以无缝接入阿里的GTS

那阿里的GTS的话

它还提供了一个特性

就是支持整个分布式事务组件的一个高可用

大家想想

如果说我Sita本身出现问题了

我们这些所有服务节点

它们事务提交

是不是就会产生问题

对不对

好

这个呢

是版本的一个说明

那么我们在这里呢

主要是想学习

对不对

那么我们就采用了0.9.0的一个版本就可以了

这个版本来讲

相对于以下的版本会比较稳定一点

大家不要采用0.8

或者是0.7

0.9以下的一些版本

因为呢

我这边是做过一些实验

他们在这边的话呢

往下一些版本会出现一些不可预知的一些错误

比如像一些假死啊

等等的情况

好

建议大家的话呢

安装0.9.0的一个版本

在后面启动验证当中的话呢

我们还会去教大家如何去启动和配置

Sita Demo这个案例呢

因为是采用官方的Demo做了一个改造

对不对

在这里呢

我们就不带着大家去逐一敲写对应的代码

我们呢

就直接引入到工程当中

Sita Demo

在这里呢

我们已经做了相应的调整和修改

那么我们在这里呢

来看一下

它整个的实现流程

是怎样的

首先的话呢

Sita Demo Application是它的一个启动入口

是通过SplitBoot的方式进行的启动

然后呢

加上它对应的注解

这些呢

都是必要性的

然后呢

它的扫描包

我们做了一个调整

扫描我们common.idcast

这些是一些基础性的配置

那它整个的一个请求流程是怎样的

在这里提供了一个SplitBoot的访问接口

asset r3

通过这个接口呢

它在这里会流转到R3 service

R3 service

是做什么事情呢

我们来看一下

R3 service呢

主要是做了两件事情

第一呢

它要去修改资产的一个状态

然后呢

进行保存

接着的话呢

它要去修改它的一个数量increase

调用了asset service

这个呢

就是模拟一个远程的调用

看到没有

不管说你是在单个节点下面

因为它只是一个模拟

对不对

并没有说按照我们的分布式的这种方式进行测试和验证

但是没有关系

因为的话呢

不管你是单个节点还是多个节点也好

如果说你在这里面的话呢

没有加入事务控制

其中某一个方的出现失败或者异常的话呢

它这数据是会产生不一致的

好

那我们再具体看一下

increase方法里面做什么事情呢

increase方法的话呢

它会打印XID

大家还有没有印象

就是之前呢

我们所讲过的CETA的工作机制

在下面的话呢

它有个什么XID

看到没有

这个呢是TC所分

所分配了一个全局事务的唯一标记

好

那打印了XID

我们就知道了这个分布式失误

它有没有生效

对不对

然后呢

它增加数量

它怎么做的呢

它要去查询对应的数据

拿到这个数据呢

做一个数量上的修改

然后再保存

最后的话呢

它就抛出一个什么long time一个save行

那long time一个save行的话呢

外层我们是没有什么transaction

然后的话呢

也没有low back

所以这个时候呢

内部的失误

它是不会进行一个回滚的

好

那么我们再看一下它上层的调用

上层调用这一块呢

它加入了transaction了

对不对

但是这里面呢

并没有加入low back

就是low back for

low back on

然后一个save行

点cast

它没有配置这样一个属性

所以呢

即便抛出异常

它这个失误的话呢

是不会补过

本地失误的话呢

是不会进行回滚的

所以的话呢

在这里大家要注意一下

然后的话呢

它怎么进行回滚呢

它就通过global transaction了

全局失误标记进行一个回滚操作

我们来看一下

全局失误的

它的集成和运用是怎么做的呢

它只需要加上global transaction的

这样一个注解就可以了

其实很简单

轻入性来讲非常低

对不对

也符合CETA的设计原则

一定要简单易用

我们在这里的话呢

只要在调用方法路口上面

加上global transaction就可以实现了

这个来讲呢

是非常简单

能够简化我们很多的开发量

对不对

好

global transaction呢

这个呢

是CETA所提供出来的一个注解

在这里面呢

我们还可以配置很多的一些属性

比如说它的超时时间

对不对

然后呢

它的loadback

它要针对哪些异常进行一个触发

那么的话呢

还有它的其他的

不需要loadback的一些等等的配置

都可以很灵活的去使用

好

这样呢

就是CETA

它这个案例的整个的调用处理流程

这里呢

咱们讲起了

如何去使用这个全局分布式事物

对不对

那么全局分布式事物该怎么去配置呢

好

在这个工程当中呢

我们来看一下它的配置目录

配置支援目录下面的话呢

存在两个比较重要的文件

哪两个呢

一个是file.config

还有一个是regist.config

这两个是什么作用呢

这两个的话呢

就是用于CETA的

配置

我们首先看一下regist.config

regist.config的话呢

是CETA将它的配置信息存放在什么

组件当中

我们可以看到它可以支持什么

很多的注册中心

比如像Narcos

Ulika

还有JK或者是Ladies都可以

那么在这里呢

为了简化其间

它默认就采用什么

file的模式

file模式是什么意思呢

就在这里面

它会指向本地的一个文件

然后呢去存储它的配置

那么咱们可以看到

我们这个的话呢

采用file的模式

这里呢指定一个file.config的文件

对不对

好

那么配置的话呢

它的这个是注册对不对

这个的话呢是配置

配置的话呢

跟注册它分为两部分

这样的话呢

你非常管理起来非常灵活

对不对

而且扩展性会比较强

这两个模式呢

它都是采用什么

file.config进行处理

那我们就来看一下file.config具体的配置内容

在这里呢

可以看到是它基本的一些配置

这个呢是transport基于nety的一个配置策略

在这里呢

大家如果是根据一些性能需要

可以做对应的一个调整

比如说修改它的一些现成啊

它的一些工作进程啊等等

然后的话呢

是它的一个store

就是存储的一个设置

比如说你的session的这种size大小

下面的话呢就是service

这一块呢是终点

这个service的话呢

我们要注意

这个是什么

虚拟的一个group啊

对不对

虚拟group的话呢

这里默认就叫mytest-group

然后的话默认值是default

这一块呢

大家不要去改

大家就采用默认值就可以了

如果说你要在实际项目当中去运用

有很多的这种组件

要去做分布式事务的集成处理

那么呢

我们可以给它配置不同的模块名称

好

在下面的话呢

就是我们seta的服务端口和地址

在这里面的话呢

指向本地的8091的一个端口

这个呢就是seta的一个连接配置

然后的话呢

是客户端的一个配置

比如说我的从事的周期

从事的时间

对不对

好

下面的话呢

就是它的一个store存储的方式

那客户端在这里的话呢

也会有一些信息要去做一些记录

比如说你事务的一些日资啊

对吧

那么记录这一块怎么去做的呢

它可以支持db的模式

也可以支持file的模式

默认的话呢

采用file模式

如果说采用db也可以

采用db的话呢

你在下面就要配置它具体的连接信息

好

这个呢就是seta的

它的主要配置信息

那么seta配置文件实现完成之后呢

还要做什么配置呢

还要去修改它的一个seta的configuration

seta configuration呢

在这里面我们可以看到

它通过这个注解

会去扫描它的一个seta的配置

那么seta配置呢

其实也很简单

主要的话呢

去创建一个global transaction scanner

这样的一个扫描器

让它呢加入到实用性容积当中

那么的话呢

我们可以看到

它在这里会去初始化

global transaction scanner

这样一个对象

对不对

那么有没有注意到

在这里面application id

就是我们的服务名称

还有一个什么

其他service group

这个呢是事务的分组

这个分组呢不要搞错了

一定要跟这里呢是保持统一

如果说你在这里修改了

大家注意这个配置当中呢

也要做张映的修改和调整

好

这里呢就是seta的一个集成配置

还有seta的一个配置文件

好

最后呢咱们再看一下seta demo的

它的工程配置application

在这里面的话呢

是它的工程的基本信息

然后它的访问前缀路径demo

下面的话呢是它的服务模块名称

注意这个是数据员的连接配置

数据员连接配置的话呢

我们指向的是我们本地虚拟机的seta数据库

然后的话呢

我们还将init db

它的一个表结构呢

初始化到这个数据库当中

这个数据库呢

我们就沿用了seta组件的数据库

好

至于seta这一块的

运行和配置呢

下个章节呢

我们还会做详细讲解

那么我们将这个表结构

还有它连接信息

配置好之后

这个工程案例呢

就是配置完成

然后下面的话呢

就是jpa的一些配置

double这块

因为我们没有运用到

所以这一块的话呢

配不配置都没有关系

好

这个呢

就是seta demo案例的一个搭建和配置

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于分布式事务解决方案 **Seata** 的技术课程，具体讲解了如何将官方的 Spring Boot 示例集成到自研项目中。讲师首先介绍了 Seata 的服务设计（3.6节），通过一个“修改状态”和“增加数量”两个接口的示例，演示了如何模拟异常并验证事务的回滚机制。随后，讲师深入到工程结构（3.7节），展示了项目目录，并重点讲解了如何配置 Seata 的事务组（`@GlobalTransactional`）和数据源（`application.yml`），以确保分布式事务能够正确生效。整个过程结合了 PPT 讲解、代码演示和配置文件修改，旨在帮助学习者理解 Seata 的核心原理和实际应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: **3.6 服务设计**。讲师在 PPT 上展示了一个流程图，说明了客户端通过 HTTP 调用“修改状态”和“增加数量”两个接口，后者会模拟抛出异常，用于验证事务回滚。
*   **00:16 - 00:30**: **3.7 工程结构**。讲师切换到 IntelliJ IDEA，展示了一个名为 `trade-stock` 的项目结构，并重点介绍了 `seata-demo` 模块，说明了其目录结构和依赖关系。
*   **00:31 - 00:45**: **代码演示 - `SeataDemoApplication`**。讲师在 `SeataDemoApplication` 类中，展示了如何通过 `@RequestMapping` 注解定义一个 `/asset/assign` 接口，并在 `assetAssign()` 方法中调用 `assignService.increaseAmount()`。
*   **00:46 - 00:55**: **代码演示 - `AssignServiceImpl`**。讲师在 `AssignServiceImpl` 类中，展示了 `increase()` 方法的实现，该方法会查询数据库，修改资产状态，然后抛出一个 `RuntimeException` 来模拟异常。
*   **00:56 - 01:05**: **代码演示 - `@GlobalTransactional`**。讲师在 `increaseAmount()` 方法上添加了 `@GlobalTransactional` 注解，并在 IDE 中查看了其可用的异常类型，如 `Exception`、`RuntimeException` 等。
*   **01:06 - 01:15**: **代码演示 - `@Transactional`**。讲师在 `increaseAmount()` 方法上添加了 `@Transactional` 注解，用于定义本地事务。
*   **01:16 - 01:25**: **配置文件 - `registry.conf`**。讲师在 `registry.conf` 文件中，配置了 Seata 的服务组（`vgroup_mapping.my_test_tx_group = "default"`）和注册中心地址（`default.groupList = "127.0.0.1:8091"`）。
*   **01:26 - 01:35**: **配置文件 - `application.yml`**。讲师在 `application.yml` 文件中，配置了数据库连接信息（`url`, `username`, `password`）和 Seata 的服务端口（`server.port: 9999`）。
*   **01:36 - 01:45**: **配置文件 - `SeataConfiguration`**。讲师在 `SeataConfiguration` 类中，通过 `@Bean` 注解配置了 `GlobalTransactionScanner`，并传入了事务组名称 `my_test_tx_group`。
*   **01:46 - 01:55**: **代码演示 - `assignService.increase()`**。讲师在 `AssignServiceImpl` 类中，展示了 `increaseAmount()` 方法的完整实现，包括查询、修改、调用远程服务和保存数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **3.6 服务设计**: 展示了一个流程图，包含“客户端”、“接口地址”、“业务接口”和“抛出异常”等模块。
    *   **3.7 工程结构**: 展示了项目目录结构，包括 `trade-stock`、`cat-demo`、`grpc-demo`、`hateoas-demo` 和 `seata-demo` 等模块。
*   **代码关键内容**:
    *   **`SeataDemoApplication.java`**:
        ```java
        @RequestMapping(value = "/asset/assign")
        @ResponseBody
        public String assetAssign() {
            String result = AssetAssign assetAssign = assignService.increaseAmount(ASSET_ID);
            return result;
        }
        ```
    *   **`AssignServiceImpl.java`**:
        ```java
        @Override
        public AssetAssign increaseAmount(String id) {
            AssetAssign assetAssign = assignRepository.findById(id).get();
            assetAssign.setStatus("2");
            assignRepository.save(assetAssign);
            // remote call asset service
            assetService.increase();
            return assetAssign;
        }
        ```
    *   **`application.yml`**:
        ```yaml
        server:
          port: 9999
          servlet:
            context-path: /demo
        spring:
          application:
            name: seata-springboot-app
          datasource:
            driverClassName: com.mysql.jdbc.Driver
            url: jdbc:mysql://192.168.19.150:3306/seata?useSSL=false&serverTimezone=UTC
            username: root
            password: 654321
            poolPingConnectionsNotUsedFor: 60000
            connectionProperties: true
            validationQuery: SELECT 1 FROM DUAL
        ```
    *   **`registry.conf`**:
        ```properties
        service {
          vgroup_mapping.my_test_tx_group = "default"
          default.groupList = "127.0.0.1:8091"
        }
        ```
    *   **`SeataConfiguration.java`**:
        ```java
        @Bean
        public GlobalTransactionScanner globalTransactionScanner() {
            GlobalTransactionScanner globalTransactionScanner = new GlobalTransactionScanner("my_test_tx_group");
            return globalTransactionScanner;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务设计演示** (00:00-00:15)
    *   讲师在 PPT 上展示了一个流程图，说明了客户端通过 HTTP 调用“修改状态”和“增加数量”两个接口。
    *   讲师强调，增加数量接口会模拟抛出异常，目的是为了验证修改状态接口的数据是否会回滚。
*   **场景二：工程结构与代码演示** (00:16-00:45)
    *   讲师在 IntelliJ IDEA 中展示了 `trade-stock` 项目的结构，并重点讲解了 `seata-demo` 模块。
    *   讲师在 `SeataDemoApplication` 类中，演示了如何定义一个 HTTP 接口，并调用 `assignService.increaseAmount()` 方法。
*   **场景三：事务处理与异常模拟** (00:46-01:05)
    *   讲师在 `AssignServiceImpl` 类中，演示了 `increase()` 方法的实现，该方法会查询数据库，修改资产状态，然后抛出一个 `RuntimeException`。
    *   讲师在 `increaseAmount()` 方法上添加了 `@GlobalTransactional` 注解，用于定义全局事务。
*   **场景四：配置文件设置** (01:06-01:35)
    *   讲师在 `registry.conf` 文件中，配置了 Seata 的服务组和注册中心地址。
    *   讲师在 `application.yml` 文件中，配置了数据库连接信息和 Seata 的服务端口。
*   **场景五：事务组配置与代码集成** (01:36-01:55)
    *   讲师在 `SeataConfiguration` 类中，通过 `@Bean` 注解配置了 `GlobalTransactionScanner`，并传入了事务组名称。
    *   讲师在 `AssignServiceImpl` 类中，演示了 `increaseAmount()` 方法的完整实现，包括查询、修改、调用远程服务和保存数据。
