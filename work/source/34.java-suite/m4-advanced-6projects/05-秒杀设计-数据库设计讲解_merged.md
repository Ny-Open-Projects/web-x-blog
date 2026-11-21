# 05-秒杀设计-数据库设计讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那咱们秒杀这一块它的数据库设计呢

我们也来详细讲解一下

像秒杀这一块它的数据库

我们主要设计了跟秒杀相关业务的数据库

首先第一个就是秒杀商品数据库

这个就是直接对外展示的商品信息

还有一个是秒杀订单数据库

这个是用户进行抢单之后去生成的一个数据

还有一个是管理员数据库

管理员要登录之后才能去操作我们的后台

再就是用户数据库

用户数据库这一块呢

是参与抢单的用户信息的一个存储

那主要是讲解第一个和第二个数据库

我们这一块为什么要拆分多个数据库呢

因为整体是一种微幅架构

好我们来看一下每个数据库这一块的一个表设计

先看第一个秒杀商品数据库

那么秒杀商品数据库呢

在这一块

它这里总共有这么多张表

我们来简单分析一下

第一张表是我们的活动表

好我们看一下它详情信息

这个是秒杀活动表

那么活动呢是怎么回事呢

就类似咱们京东上面早晨8点到早晨10点

早晨10点到12点

这个时间段的一个活动信息

那这一块呢就会记录这个信息

第一个是begin time

第二个是end time

这两个就是记录秒杀活动的一个时间信息的

还有一个有个total time

这个是秒杀中间持续的时间

这里还有一个状态

就是秒杀开启了没有

还有一个秒杀的名称

这个是秒杀活动名称

比如说10点抢购

12点抢购

比如说双11抢购

这是这一块

好还有一个是我们的品牌这一块

品牌呢比较简单

我就不去详细介绍了

一个是名字图片

手字母还有排序

下面这个呢是一个分类的表结构

主要是商品分类的表结构

这个呢主要是基于我们后面要去做搜索的一个实现

所以这个也不去详细讲解

分的名称

分类的ID就OK了

好还有一个是秒杀时间段

秒杀时间段呢

比如刚才我说过早晨8点到10点

10点到12点

12点到14点

像这一块是一个时间段

它并没有精确到哪一天

而这一块这个表结构

就是存储这个时间段的

它并不精确到哪一天的

好下面这一块是一个秒杀商品表结构

这个秒杀商品表呢

我们要去好好了解一下

好首先第一个在这一块

它有一个商品的唯一标识ID

这就不用去说了

下面是商品的名称

这个是商品的

这个是商品的价格

而下面这个呢是秒杀商品的价格

这个是当前库存量

好后面还有预警值就不去管它了

图片也不管了

创建时间

修改时间

SPU ID

Category 1

Category 2

Category 3

这是分类ID1

分类ID2

分类ID3

这个呢

像这个分类ID

一般是可以用于做分类过滤搜索的

好还有一个品牌ID

也是可以用来做品牌过滤搜索的

还有一个是我们当前的一个品牌名称

好SPEC这是规格

还有一个销量

还有评论数量

这不管它

后面这里面

这里有一个SKU N的SKU BEGIN

这个是秒杀开始

秒杀结束

因为你当前商品有可能要参与秒杀

那么参与秒杀呢

就会有一个开始时间与结束时间

后面这里有一个状态

注意这个状态呢

我给他做了个描述

就是当前商品参与秒杀的状态

一是普通商品

二是参与秒杀

还有一个是ISLOCK

表示是否锁定

一是未锁定

二是锁定

好另外一个就是SKU NUMBER

就是参与秒杀的一个商品数量信息

我这里有一千件商品

我参与秒杀的可能只有五件

好

这是这个秒杀商品表结构的一个详情介绍

接着我们往后面继续看

这里还有一个叫做SKUACT

其实就是关联第一张表的

秒杀活动商品中间表

它记录了商品ID

记录了活动ID

好这个是一个规格

这个规格了

我们就不去管它了

用于做搜索的时候是有帮助的

最后一个是用来做分布式日志的

分布式事务的

这个我们暂时不讲它

后面用到CETA的时候

我们再来讲解

好

这就是秒杀商品数据库

再来看我们

我们的一个订单数据库

这个订单数据库这一块

只有一个订单表

下面的是用来做分布式事务的

我们看看这个订单表

这一块订单表这一块了

大家注意一下

我们参与秒杀的时候

我们这一块是支持一个秒杀商品

在这里有一个对的订单

并不像我们平时那个购物车一样

一个

订单能有多个秒杀商品

我们不做这个

我们只做一个订单

只去抢购一件商品就可以了

好

我们看一下这一块对应的列

第一个ID列就不说了

第二个是total number

这个是当前这个商品

你买几件

还有一个支付类型

创建时间

修改时间

支付付款时间

发货时间

完成交易时间

关闭交易时间

收货人

收货人手机

收货人地址

交易留守号

这个我都不去详细讲解了

还有一个叫做订单状态

那一下单肯定是未完成

好

还有一个支付状态

还有一个发货状态

是否删除

这个我就不去讲解了

后面这三个呢

这四个呢

我就讲解一下

第一个是什么呢

是商品ID

第一个是商品ID

第二个呢

是商品名称

第三个呢

三个是商品的价格

第四个是当前这个订单是属于哪个用户的

好

那这一块我们默认商品只能抢购一件

所以这块这个价格呢

最默认是单个商品价格

如果以后你这里开放多个商品的话

那这个时候就是商品乘以商品单价乘以抢购的个数

这一块就是一个总金额的概念

好

这是我们秒杀订单表哈

还有两个辅助数据库

一个是管理员数据库

一个是用户数据库

这两个呢

是辅助的管理员呢

主要是记录管理员的一些信息

用来实现登录操作的

再就是用户这一块

只是记录用户相关的信息

也是用来实现登录

能有用户去抢单的好

这是我们这个秒杀的数据库的一个设计

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“黑马程序员”技术课程《第1章 秒杀商品维护》中“1.3 数据库设计”部分的讲解。讲师通过 MySQL 数据库管理工具（如 Navicat Premium）和配套的 PPT 讲义，系统性地介绍了为实现高并发秒杀系统而设计的数据库架构。核心内容包括创建并定义多个关键数据表，如秒杀活动表 (`tb_activity`)、商品品牌表 (`tb_brand`)、商品规格表 (`tb_sku`)、订单表 (`tb_order`)、管理员表 (`tb_admin`) 和用户表 (`tb_user`)。讲解重点在于表结构的设计，包括字段名、数据类型、默认值、注释（COMMENT）以及主键和索引等约束条件，旨在为后续的高并发业务逻辑提供数据支撑。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和课程逻辑推断的，按讲解顺序排列：

*   **00:00 - 00:30**: **1.3 数据库设计** (PPT标题页)
    *   介绍本节内容：设计支撑秒杀业务的数据库。
*   **00:30 - 01:00**: **1.3.1 秒杀商品数据库**
    *   介绍数据库名称 `seckill_goods`。
    *   展示并讲解 `tb_activity` (秒杀活动表) 的结构。
    *   展示并讲解 `tb_brand` (商品品牌表) 的结构。
*   **01:00 - 01:30**: **1.3.2 秒杀订单数据库**
    *   展示并讲解 `tb_sku` (商品规格表) 的结构。
    *   展示并讲解 `tb_sku_act` (秒杀活动与商品关联表) 的结构。
    *   展示并讲解 `undo_log` (用于分布式事务的回滚日志表) 的结构。
*   **01:30 - 02:00**: **1.3.3 管理员数据库**
    *   展示并讲解 `tb_admin` (管理员表) 的结构。
*   **02:00 - 02:30**: **1.3.4 用户数据库**
    *   展示并讲解 `tb_user` (用户表) 的结构。
*   **02:30 - 03:00**: **1.3.5 订单数据库 (续)**
    *   展示并讲解 `tb_order` (订单表) 的结构。
*   **03:00 - 03:30**: **1.2 秒杀架构 (PPT回顾)**
    *   快速回顾系统架构，强调数据库设计是支撑高并发的核心。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **章节标题**：
    *   `1.3 数据库设计`
    *   `1.3.1 秒杀商品数据库`
    *   `1.3.2 秒杀订单数据库`
    *   `1.3.3 管理员数据库`
    *   `1.3.4 用户数据库`
    *   `1.2 秒杀架构`
*   **架构图**：
    *   一张展示“秒杀系统架构”的流程图，包含“用户”、“秒杀服务”、“订单服务”、“库存服务”、“支付服务”等模块，说明了系统各部分的交互关系。

#### 代码 (SQL)

以下是视频中展示的关键 SQL `CREATE TABLE` 语句：

*   **秒杀活动表 (`tb_activity`)**

    ```sql
    CREATE TABLE `tb_activity` (
      `id` varchar(60) NOT NULL,
      `name` varchar(100) NOT NULL COMMENT '活动名称',
      `status` int(2) NOT NULL DEFAULT '1' COMMENT '状态：1开启，2未开启',
      `start_time` datetime DEFAULT NULL COMMENT '开始时间，单位：时分秒',
      `end_time` datetime DEFAULT NULL COMMENT '结束时间，单位：时分秒',
      `total_time` float DEFAULT NULL COMMENT '总时长，单位：分',
      `is_del` int(1) DEFAULT '1' COMMENT '删除：1未删除，2已删除',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```

*   **商品品牌表 (`tb_brand`)**

    ```sql
    CREATE TABLE `tb_brand` (
      `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '品牌Id',
      `name` varchar(100) NOT NULL COMMENT '品牌名称',
      `image` varchar(200) DEFAULT NULL COMMENT '品牌图片地址',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
    ```

*   **商品规格表 (`tb_sku`)**

    ```sql
    CREATE TABLE `tb_sku` (
      `id` varchar(60) NOT NULL COMMENT '商品id',
      `name` varchar(200) NOT NULL COMMENT 'SKU名称',
      `price` int(20) NOT NULL DEFAULT '1' COMMENT '价格（分）',
      `seckill_price` int(20) NOT NULL DEFAULT '1' COMMENT '秒杀价（分）',
      `num` int(11) DEFAULT '100' COMMENT '库存数量',
      `alert_num` int(11) DEFAULT '0' COMMENT '库存预警数量',
      `image` varchar(200) DEFAULT NULL COMMENT '商品图片',
      `images` varchar(2000) DEFAULT NULL COMMENT '商品图片列表',
      `create_time` datetime DEFAULT NULL COMMENT '创建时间',
      `update_time` datetime DEFAULT NULL COMMENT '更新时间',
      `spu_id` varchar(60) DEFAULT NULL COMMENT 'SPU ID',
      `category1_id` int(10) DEFAULT NULL,
      `category2_id` int(10) DEFAULT NULL,
      `category3_id` int(10) DEFAULT NULL,
      `category1_name` varchar(20) DEFAULT NULL COMMENT '类目名称',
      `category2_name` varchar(20) DEFAULT NULL COMMENT '类目名称',
      `category3_name` varchar(20) DEFAULT NULL COMMENT '类目名称',
      `brand_name` varchar(100) DEFAULT NULL COMMENT '品牌名称',
      `spec` varchar(200) DEFAULT NULL COMMENT '规格',
      `sale_num` int(11) NOT NULL DEFAULT '0' COMMENT '销量',
      `comment_num` int(11) NOT NULL DEFAULT '0' COMMENT '评论数',
      `seckill_end` timestamp NULL DEFAULT NULL COMMENT '秒杀结束时间',
      `seckill_begin` timestamp NULL DEFAULT NULL COMMENT '秒杀开始时间',
      `status` int(1) NOT NULL DEFAULT '0' COMMENT '是否普通商品：1普通商品，2参与秒杀',
      `is_lock` int(1) NOT NULL DEFAULT '0' COMMENT '秒杀数量',
      PRIMARY KEY (`id`),
      KEY `cid` (`category1_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```

*   **秒杀活动与商品关联表 (`tb_sku_act`)**

    ```sql
    CREATE TABLE `tb_sku_act` (
      `sku_id` varchar(60) NOT NULL,
      `activity_id` varchar(60) NOT NULL,
      `is_del` int(2) DEFAULT '1' COMMENT '删除状态：1未删除，2已删除',
      PRIMARY KEY (`sku_id`, `activity_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```

*   **回滚日志表 (`undo_log`)**

    ```sql
    CREATE TABLE `undo_log` (
      `id` bigint(20) NOT NULL AUTO_INCREMENT,
      `branch_id` bigint(20) NOT NULL,
      `xid` varchar(100) NOT NULL,
      `context` varchar(128) NOT NULL,
      `rollback_info` longblob NOT NULL,
      `log_status` int(1) NOT NULL,
      `log_created` datetime NOT NULL,
      `log_modified` datetime NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `ux_undo_log` (`xid`, `branch_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```

*   **订单表 (`tb_order`)**

    ```sql
    CREATE TABLE `tb_order` (
      `id` varchar(60) COLLATE utf8_bin NOT NULL COMMENT '订单id',
      `total_num` int(1) DEFAULT NULL COMMENT '数量合计',
      `pay_type` varchar(1) COLLATE utf8_bin DEFAULT NULL COMMENT '支付类型，1、在线支付',
      `create_time` datetime DEFAULT NULL COMMENT '订单创建时间',
      `update_time` datetime DEFAULT NULL COMMENT '更新时间',
      `pay_time` datetime DEFAULT NULL COMMENT '付款时间',
      `consign_time` datetime DEFAULT NULL COMMENT
