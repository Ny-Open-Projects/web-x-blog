# 16-Seata-分布式事务准备工作 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那么接下来我们将按照这个实现的流程去实现我们TC分布式事物控制

第一个首先我们要在需要做分布式事物的一个数据库里面去添加这个日子表

那么这个日子表呢非常简单

从这一块拷贝一下

然后到我们对应的数据库中去添加就可以了

那刚才我们这里这个分布式事物所涉及到的一个微幅

第一个是我们故事微幅

第二个是当前这个订单微幅

故事微幅呢对应的是商品对应的表

这个对应的是订单相关的表

我们把数据库打开

在这一块这个是订单相关的数据库

我们可以在这里把刚才的一个数据库脚本给执行一次

这个脚本给执行一次

一执行之后就会多这么一个表

这个表叫

这个是对应的一个表的信息

这个我就不去讲解了

接着是我们商品这个数据库

这里也得执行刚才那个脚本

一执行之后也会多一个表

这个表呢也是用来存储回滚的一个信息的

好OK

那么表结构这一块我们就创建了

接着按照这个步骤来的话

要开始去安装我们TC了

TC这一块它是负责全局事务管理的

那么你要拿一个全局锁是需要经过TC的

好我们开始去安装TC

那么安装TC呢

首先我们要知道TC去哪里下载

在这一块提供了一个TC下载的地址

大家可以去这个地址去下载就可以了

那么这一块呢

我已经把TC的下载地址给打开了

大家可以点击下面这一块这个下载

去进行相关的一个操作

我们这一块可以下载CETA1.2.0

或者是CETA1.1.0

或者是CETA1.0

或者是CETA

往后面走

到后面这里

建议最好是下0.6以上的版本

不要下0.6以下的版本

0.6以下的版本呢

它并不是特别的稳定

以前呢也不叫CETA

以前叫Fast Easy Commit and Rollback

这是这个哈

那我们下载的话就下载1.2的版本

或者是1.1.0的版本都可以

或者是1.0的版本

最好不要下载0.8以下的

你要么是下载0.8的版本

要么是下载0.8以上的版本

不要低于0.8

这是这一块哈

当然稳定版本是从0.6开始的

这是这一块

下载之后呢

我们可以把它打开看一下

大概是有这么三个目录

一个目录是B目录

里面都是一些可执行的文件

第二个是Configure配置的一些脚本

好

第三个是什么呢

内部依赖包

我们当前CETA用的是加文语言编写的

那这一块呢

你要想使用它

你可以直接启动ceta.bat

ceta-server.bat

这个是windows下启动

这个是linux下启动的

咱用这个ceta-server.bat

双击就可以了

好

这是这一块哈

行启动之后呢

大概是这么个界面

就这么简单

一个道士界面

我们这里并不打算在windows下去使用它

我们打算在生透时下面去用它

那因此我们这里的要做另外一个事情

在生透之下去安装它

那生透之下去安装它

那生透之下去安装它

那生透之下去安装它

那生透之下怎么安装呢

这一块给你们简单介绍一下

我将采用的是多颗容器去安装

我们就不在生透之下去使用那个

刚才那个安装包了

我们直接用脚本去安装

用容器去安装就可以了

如果是在linux下

我们直接把这一段安装容器的命令给执行一下就可以了

好

这个我给执行一下哈

简单说一下这一块

这里有一个多颗容

刚地就不用说了

后台运行刚刚内

我是当前是他的名字

刚批1881918191

刚一是表示什么呢

这里如果你启动C他他默认的端口是8091

那如果你把这个端口给加上去

这个就是一个属性加上去

就表示启动的端口是8191

换了这个端口啊

为什么不用8091呢

他跟前面的一个applete最大的端口有所冲突

所以这一块是八零九一八一九一好

后面是我们的一个镜像

这就不用说了

那么接着我一回车了

当前c他就已经装好了

在我这一块的装好了啊

多颗ps这里好启动一下多颗

是大的

c他

当servo

启动一次

多颗ps于是这里的c他就启动好了

这里的端口后的是8191

这个8191哈

行

那我们的tc就装好了

tc装好之后呢

接着我们就开始在项目中去实现我们的一个分布式事务控制了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程旨在讲解如何在 Java 项目中集成和使用 **Seata** 分布式事务解决方案，以实现“秒杀”等高并发业务场景下的数据一致性。课程内容围绕 Seata 的核心组件展开，包括：

*   **环境准备**：在数据库中创建 `undo_log` 表，这是 Seata 事务协调的核心日志表。
*   **服务部署**：安装并启动 Seata 的 TC（Transaction Coordinator，事务协调器）服务。
*   **应用配置**：在 Spring Boot 项目中引入 Seata 依赖，并配置数据源代理，使业务方法能够自动参与分布式事务。
*   **代码实现**：在业务代码中使用 `@GlobalTransactional` 注解来声明一个全局事务，从而将多个数据库操作纳入同一个分布式事务中。

整个过程是典型的“从零开始”部署和使用 Seata 的教程，目标是让开发者能够快速上手并理解其工作原理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：课程开场，展示项目代码 `OrderService`，并引出“秒杀”场景下需要解决的分布式事务问题。屏幕上弹出的注释框列出了本课程的五个核心步骤。
*   **00:30 - 01:00**：讲解数据库层面的准备工作，展示在 `seckill_goods` 数据库中创建 `undo_log` 表的 SQL 语句。
*   **01:00 - 01:30**：讲解如何安装和启动 Seata 的 TC 服务，展示在 GitHub 上下载 Seata 服务的页面，并演示如何通过命令行或 Docker 部署 TC。
*   **01:30 - 02:00**：讲解如何在 Spring Boot 项目中配置 Seata，展示 `pom.xml` 中的依赖配置和 `DataSourcesProxyConfig` 配置类。
*   **02:00 - 02:30**：讲解如何在业务代码中使用 `@GlobalTransactional` 注解来声明全局事务，展示 `OrderService` 中的 `doSku` 方法。
*   **02:30 - 03:00**：演示整个流程，从用户下单、插入订单、写入 Redis 限流，到最终的事务提交或回滚。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **核心步骤列表**：视频中反复出现一个注释框，列出了 Seata 部署的五个关键步骤：
        1.  在每个需要控制分布式事务的数据库中添加日志表 `undo_log`。
        2.  安装 TC。
        3.  配置数据源-代理数据源。
        4.  配置微服务与 Seata 的 TC 交互信息以及注册地址。
        5.  使用全局分布式事务的方法上添加注解 `@GlobalTransactional`。
    *   **Seata 模式介绍**：PPT 中提到了 Seata 的三种模式：AT 模式、TCC 模式和 Saga 模式。
    *   **Seata 服务版本**：展示了 Seata 的 GitHub 仓库，包括 `v1.1.0` 和 `v0.5.1` 等版本的更新日志，其中包含了功能、Bug 修复和性能优化的详细信息。

*   **代码关键内容**：
    *   **数据库表结构**：
        ```sql
        CREATE TABLE undo_log (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            branch_id bigint(20) NOT NULL,
            xid varchar(100) NOT NULL,
            context varchar(128) NOT NULL,
            rollback_info longblob NOT NULL,
            log_status int(1) NOT NULL,
            log_created datetime NOT NULL,
            log_modified datetime NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY ux_undo_log (xid, branch_id)
        ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
        ```
    *   **Java 业务代码**：
        ```java
        Result<Sku> count = skuFeign.count(order, order.getSkuId(), order.getTotalNum());
        if (count.isSuccess()) {
            // 记录当前用户抢购的时间点，24小时内不能抢购该商品
            redisTemplate.boundValueOps(userKey).set("*");
            redisTemplate.boundValueOps(userKey).expire(timeout, TimeUnit.MINUTES);
            orderMapper.insertSelective(order);
            return StatusCode.ORDER_OK;
        } else {
            // 405库存不足
            if (count.getCode() == StatusCode.DECOUNT_NUM) {
                return StatusCode.DECOUNT_NUM;
            } else if (count.getCode() == StatusCode.DECOUNT_HOT) {
                return StatusCode.DECOUNT_HOT;
            }
        }
        ```
    *   **依赖配置**：
        ```xml
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库表创建**（画面：数据库管理工具）
    *   **描述**：讲师在数据库管理工具中，为 `seckill_goods` 数据库执行 SQL 脚本，创建 `undo_log` 表。这是 Seata 事务协调的基础，用于记录事务的回滚信息。

*   **场景二：TC 服务部署**（画面：GitHub 页面、命令行）
    *   **描述**：讲师首先在 GitHub 上下载 Seata 服务的 `seata-server-1.2.0.tar.gz` 文件，然后通过命令行解压并启动服务。演示了如何通过 `docker run` 命令快速部署 TC 服务，展示了服务启动后的日志输出。

*   **场景三：应用配置**（画面：IDE、PPT）
    *   **描述**：讲师在 Spring Boot 项目的 `pom.xml` 中添加了 Seata 的依赖，并在 `src/main/java` 目录下创建了 `DataSourcesProxyConfig` 配置类，用于配置数据源代理。PPT 上展示了 Seata 的三种模式，帮助理解不同场景下的选择。

*   **场景四：代码注解**（画面：IDE 代码）
    *   **描述**：讲师在 `OrderService` 的 `doSku` 方法上添加了 `@GlobalTransactional` 注解。通过高亮显示代码，强调了该注解的作用是将整个方法纳入一个全局事务中，从而保证数据一致性。

*   **场景五：事务演示**（画面：IDE 代码、Redis、数据库）
    *   **描述**：讲师模拟了一个“秒杀”场景，用户下单后，系统会先检查库存，然后插入订单，并在 Redis 中设置一个“已抢购”的标记。整个过程通过 `@GlobalTransactional` 注解保证了数据库和 Redis 的操作要么全部成功，要么全部失败，从而实现了分布式事务的一致性。
