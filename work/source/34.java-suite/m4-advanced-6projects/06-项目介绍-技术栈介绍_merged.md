# 06-项目介绍-技术栈介绍 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们介绍一下秒杀的项目,那秒杀的项目这一块呢,我会先带大家去了解一下它的一个技术站,然后去介绍一下我们秒杀的一个项目结构。

好,项目结构介绍之后呢,会导入我们已经写好的一个工程,这个工程呢,包含了一些基础功能,像增删改查这些东西我们就不去写了,我们只写项目里面价值较高的部分。

接着我们会去讲解一下我们工程里面的一个品牌案例,品牌案例呢,会带大家去梳理一下从用户请求到数据处理的整个过程。

好。

我们先来介绍一下它的一个技术站这一块。

像我们秒杀这一块它的技术站呢,我们来简单看一下。

首先第一个,我们终端这一块可以是安卓,IOS,PC都可以的。

那这个时候去访问我们系统的时候,我们接入成这一块呢,这一块是KeepAlive的这一块,还有我们的4层负载,7层负载。

那4层负载是LVS,7层负载是Nginx。

那紧急。

接着要进行抢单的话,我们要进行身份识别。

身份识别之后呢,我们还要去判断一下是秒杀的一个热点商品,还是说非热点商品。

那这个时候我们要用脚本去查询我们的缓存的。

所以这一块我们有一个脚本控制。

脚本控制呢,我们将用Lua脚本去控制缓存。

用Lua脚本去操作数据库。

用Lua脚本去操作我们的MQ。

操作缓存呢,缓存我们将用的是分布式缓存Redis。

我们会给它佩戴的一个扫兵策略。

这一块走了之后,紧接着要进入到我们后端微服的话,我们这一块有网关层。

网关层呢,用的是当前比较流行的Gateway。

Gateway这一块紧接着就会路由用户的一个功能,进入到我们的服务层了。

进入到我们的服务层呢,这一块有管理员后台。

热点数据发现、秒杀系统、搜索系统等等。

那这个时候呢,我们数据同步采用的是Kana去实现数据的一个实时同步,实时监听的。

服务字里呢,我们用的是这一块注册与发现用的是Lacos。

限流是Sentinel。

负载金融横是用的Ribbon。

链路追踪是Skywalking。

中间键我们用MQ、RockMQ、卡夫卡都可以。

分布制事务这一块用当前比较流行的Sita。

Sita呢,这一块在微服方面是非常容易使用的哈。

所以这一块用的是Sita。

数据库、数据存储。

非关系型是Redis。

还有个数据存储这一块。

关系型数据库是MySQL。

另外一个海量数据的一个搜索,我们用的是ElectricSearch。

这一块呢就是我们当前秒杀的一块。

这个是一个技术站。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“第一富 秒杀商品维护”项目的第一章“项目介绍”部分。讲师通过演示一个完整的秒杀系统架构，旨在为学员建立项目全局认知。内容主要分为三部分：
- **第一部分 (2.1 技术栈介绍)**：详细讲解了系统的整体技术架构图，包括前端、接入层、缓存层、分布式缓存、网关、服务层、数据同步等模块，并指出了各层所使用的核心技术（如Redis、Nginx、Gateway、Canal等）。
- **第二部分 (2.3 项目导入)**：展示了项目的目录结构，说明了项目采用的模块化设计（如 `seckill-parent` 作为父工程，包含多个子模块），并介绍了开发环境的配置，包括使用 Docker 安装的 MySQL、Elasticsearch 等服务。
- **第三部分 (2.4 工程案例)**：通过一个具体的用户查询品牌信息的案例，演示了从用户请求到后端服务的完整访问流程（用户 -> Nginx -> Gateway -> seckill-service），并给出了对应的 API 路径 `/api/brand`。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下时间点是根据画面内容和常规课程结构推断的：

- **00:00 - 00:30**: 第一章“项目介绍”总览，讲师介绍本章内容。
- **00:30 - 02:00**: **2.1 技术栈介绍**。讲师详细解读系统架构图，从上至下依次讲解前端、接入层、缓存层、网关、服务层、数据同步等模块。
- **02:00 - 03:00**: **2.3 项目导入**。讲师展示项目目录结构，解释各模块的作用，并说明开发环境配置（MySQL、Elasticsearch 等通过 Docker 安装）。
- **03:00 - 04:00**: **2.4 工程案例**。讲师通过一个“查询品牌”案例，演示了请求的访问流程图（用户 -> Nginx -> Gateway -> seckill-service），并给出 API 路径 `/api/brand`。
- **04:00 - 05:00**: **1.3.1 秒杀商品数据库**。讲师切换到数据库设计部分，展示 `tb_activity` 和 `tb_brand` 两张核心表的建表语句。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表

- **系统架构图 (2.1 技术栈介绍)**：
  - **前端层**：支持 Android、iOS、PC。
  - **接入层**：Vip、Kapalined、七层负载均衡（Nginx、Haproxy）。
  - **缓存层**：Redis、Memcached、本地缓存。
  - **分布式缓存**：Redis+Sentinel。
  - **网关层**：Gateway（服务网关）。
  - **服务层**：
    - **管理服务**：秒杀订单服务、秒杀商品服务。
    - **热点商品服务**：热点商品服务、热点商品服务。
    - **秒杀分组**：秒杀商品服务、秒杀商品服务。
  - **数据同步层**：Canal。
  - **中间件**：RocketMQ、Seata、SkyWalking。
  - **CDB**：Cache、Cache、Cache。

- **访问流程图 (2.4 工程案例)**：
  - 用户 -> Nginx -> Gateway -> seckill-service。

#### 代码

- **秒杀活动表 `tb_activity` 建表语句**：
  ```sql
  CREATE TABLE `tb_activity` (
    `id` varchar(60) NOT NULL,
    `name` varchar(100) NOT NULL,
    `status` int(2) NOT NULL DEFAULT '1' COMMENT '状态：1开启，2未开启',
    `start_time` datetime DEFAULT NULL COMMENT '开始时间，单位：时分秒',
    `end_time` datetime DEFAULT NULL COMMENT '结束时间，单位：时分秒',
    `total_time` float DEFAULT NULL,
    `is_del` int(1) DEFAULT '1' COMMENT '删除：1未删除，2已删除',
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  ```

- **商品品牌表 `tb_brand` 建表语句**：
  ```sql
  CREATE TABLE `tb_brand` (
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '品牌id',
    `name` varchar(100) NOT NULL COMMENT '品牌名',
    `image` varchar(100) DEFAULT NULL COMMENT '品牌图片地址',
    `status` int(1) DEFAULT NULL COMMENT '状态',
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  ```

- **用户表 `tb_user` 建表语句**：
  ```sql
  CREATE TABLE `tb_user` (
    `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
    `username` varchar(50) NOT NULL COMMENT '用户名',
    `password` varchar(50) NOT NULL COMMENT '密码',
    `phone` varchar(20) DEFAULT NULL COMMENT '手机号',
    `email` varchar(50) DEFAULT NULL COMMENT '邮箱',
    `status` int(1) DEFAULT '1' COMMENT '状态：1正常，2禁用',
    `create_time` datetime DEFAULT NULL COMMENT '创建时间',
    `update_time` datetime DEFAULT NULL COMMENT '更新时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  ```

---

### 4) 关键场景与演示描述

- **场景一：系统架构图讲解 (2.1 技术栈介绍)**
  - 讲师在屏幕上逐层展示架构图，从最上层的“前端”开始，向下讲解“接入层”、“缓存层”、“网关”、“服务层”、“数据同步层”和“中间件”。
  - 讲师特别强调了“缓存层”中使用了 Redis 和 Memcached，并指出“分布式缓存”使用了 Redis+Sentinel。
  - 讲师还指出“服务层”中包含了“管理服务”、“热点商品服务”和“秒杀分组”，并解释了它们各自的功能。

- **场景二：项目导入与环境配置 (2.3 项目导入)**
  - 讲师展示了项目的目录结构，指出 `seckill-parent` 是父工程，包含 `seckill-goods-api`、`seckill-order-api` 等多个子模块。
  - 讲师解释了开发环境的配置，说明由于注册中心使用 Nacos、数据库使用 MySQL、搜索使用 Elasticsearch，因此采用了 Docker 安装方式。
  - 讲师在屏幕上展示了虚拟机的 IP 地址、MySQL 的端口和账号密码。

- **场景三：工程案例演示 (2.4 工程案例)**
  - 讲师通过一个“查询品牌”案例，演示了请求的访问流程。
  - 讲师在屏幕上展示了访问流程图：用户 -> Nginx -> Gateway -> seckill-service。
  - 讲师给出了请求路径 `/api/brand`，并解释了该路径的作用。

- **场景四：数据库设计展示 (1.3.1 秒杀商品数据库)**
  - 讲师切换到数据库设计部分，展示了 `tb_activity` 和 `tb_brand` 两张表的建表语句。
  - 讲师详细解释了 `tb_activity` 表中的字段含义，如 `status` 表示秒杀活动状态（1开启，2未开启），`start_time` 和 `end_time` 表示活动开始和结束时间。
  - 讲师还解释了 `tb_brand` 表中的字段含义，如 `name` 表示品牌名，`image` 表示品牌图片地址。

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解课程内容。
