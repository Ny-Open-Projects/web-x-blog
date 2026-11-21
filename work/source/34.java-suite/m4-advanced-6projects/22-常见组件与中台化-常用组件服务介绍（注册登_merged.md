# 22-常见组件与中台化-常用组件服务介绍（注册登 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么接下来呢

咱们继续来看我们这个注册登录服务

刚才呢 我们是说了一下这个图 对吧

这个呢 它其实就是展示的

我们注册登录服务里边

这两个 对吧

一个是Auth 一个是Gateway

这两个微服务

那么它们所起的作用

再来强调一遍

这个Gateway呢 网关呢

它主要做的事是什么呢

就是针对我们这个JWT领牌

进行这个校验

而这个Auth呢

主要就是做什么呢

注册 还有登录等等

当然如果用户呢

登录成功之后啊

它会通过JWT这种方式

给我们这个客户端页面

来签发一个什么呢

Token 来签发一个Token

然后这个页面再次请求的时候呢

请求我这些业务微服务的时候呢

就需要通过请求头这种方式

把这个JWT领牌给带过来

因为什么呢

它在我们这个Gateway网关

这个地方呢

需要进行校验

如果校验通过之后

我们这个网关呢

就会把你这次请求

路由到具体的某个微服务

对吧

然后在这个微服务这个地方呢

你也可以从请求头里面

把这个什么呢

Auth ID给取出来

Auth ID它其实代表的是什么呢

代表的就是一个用户的认证ID

通过这个ID呢

你就可以去查询我们这个数据库

对吧

最终呢

把用户的详细信息都可以获取到

好

这是咱们这个

整个它的一个执行流程

然后呢

我们需要再来说明一下什么呢

就是要运行我们这个注册登录服务

它需要依赖一些环境

但是这个环境依赖的呢

不是很多

就这么三个

一个是MySQL

因为呢

我们注册啊

登录啊

等等这些

那么它其实是有一套这个数据库表结构的

所以说它需要依赖MySQL

而这个MySQL呢

需要我们来创建哪几张表呢

在MySQL数据库里边

你看在我这个Docs目录里边

已经整理好了一个Circle脚本

大家呢

直接来创建

直接来这个执行这个Circle脚本就可以了

你看

你可以在你自己本地呢

来创建这么一个叫做Customer-auth

这么一个数据库

然后在这个数据库里边呢

来执行这个脚本

来创建这些表

你看一个叫做TB-auth

对吧

然后呢

还有什么呢

TB-login record

这其实是登录记录

然后还有什么呢

TB-QQ

如果你使用的是QQ这种登录

方式对吧

那么它会把你的QQ信息

给存到这里面

然后还有什么微博

还有什么微信等等

那么这么几张表

这是依赖我们这个MySQL数据库

然后呢

所需要的表结构

你直接从这儿来执行这个Circle脚本

就可以把它创建出来了

然后呢

还需要Redis

因为我们这个地方呢

为了这个提高这个程序

它的这个性能

对吧

执行效果

会使用到Redis来缓存你的什么登录信息

然后还有Nex

它是作为我们服务的注册中心

还有配置中心

然后呢

Nex里边的配置文件呢

我这儿也已经提前整理好了

就是在这个Nex目录下边

所以说你直接把这个什么呢

把这个ZIP

这是一个压缩文件

对吧

这里边呢

就已经整理了几个

我们整个这个项目要运行的配置文件

你直接把这个脚

把这个ZIP文件呢

导入到哪呢

导入到你的Nex当中

这样的话

配置文件也就有了

启动的时候呢

它就会从这个配置中心来拉取配置

这是我们说了一下

要运行咱们这个项目

对吧

你需要把这些依赖环境来搞定

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于“常见组件与中台化”技术课程的一部分，主要聚焦于“注册登录服务”的“应用场景”。讲师通过演示一个典型的用户认证系统架构图，并结合 IntelliJ IDEA 开发环境，展示了一个用于创建用户认证相关数据库表的 SQL 脚本。内容涵盖了系统架构、依赖组件（如 MySQL、Redis、Nacos）以及具体的数据库表结构设计，旨在说明如何为一个支持多种登录方式（用户名密码、手机验证码、邮箱、微信、微博等）的系统建立数据模型。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **课程引入与架构概览**。画面显示了 Typora 文档的“大纲”，当前章节为“2.2.2 应用场景”，并展示了系统架构图，包括用户、网关（auth-gateway）、认证服务（auth）和多个业务服务。
*   **00:05 - 00:15**: **系统架构细节**。讲师在架构图上添加了服务端口信息，说明 `auth-gateway` 服务端口为 8782，`auth` 服务端口为 8783。
*   **00:15 - 00:30**: **数据库设计演示**。讲师切换到 IntelliJ IDEA，打开名为 `customer_auth.sql` 的 SQL 文件，开始演示创建数据库表的脚本。
*   **00:30 - 00:45**: **创建用户表 `tb_auth`**。讲师逐步展示并解释了 `tb_auth` 表的结构，包括 `id`、`user_name`、`password`、`status`、`mobile`、`email`、`qq`、`weixin`、`weibo` 等字段，并说明了其用途和约束。
*   **00:45 - 00:55**: **创建微博表 `tb_weibo`**。讲师继续演示，展示了 `tb_weibo` 表的结构，用于存储用户微博认证信息。
*   **00:55 - 01:05**: **创建微信表 `tb_weixin`**。讲师展示了 `tb_weixin` 表的结构，用于存储用户微信认证信息。
*   **01:05 - 01:15**: **总结与过渡**。讲师完成数据库表结构的演示，画面回到 Typora 文档，准备进入下一个章节。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **系统架构图**：一个清晰的流程图，展示了用户通过前端页面访问 `auth-gateway` 网关，网关将请求转发给 `auth` 服务，`auth` 服务再与后端的 `Server A`, `Server B` 等业务服务交互。
    *   **服务端口信息**：在架构图上标注了 `auth-gateway` (8782) 和 `auth` (8783) 服务的端口号。
    *   **项目依赖环境**：列出了项目所依赖的技术栈，包括 `mysql`、`redis` 和 `nacos`。
    *   **应用场景**：列出了针对互联网用户的多种登录/注册方式，包括用户名密码、手机验证码、邮箱、微信、微博等。

*   **代码**:
    *   **SQL 脚本 `customer_auth.sql`**：
        *   **连接配置**：`Source Host: localhost:3306`, `Source Schema: customer_auth`。
        *   **字符集设置**：`SET NAMES utf8mb4;`。
        *   **表结构定义**：
            *   `tb_auth` 表：
                ```sql
                CREATE TABLE `tb_auth` (
                  `id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
                  `user_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名',
                  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户密码',
                  `status` tinyint(4) NULL DEFAULT NULL COMMENT '账户状态，1正常账号，0测试账号，-1禁用账号',
                  `mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '手机号',
                  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱',
                  `qq` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'QQ唯一标识',
                  `weixin` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '微信唯一标识',
                  `weibo` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '新浪微博唯一标识',
                  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
                  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
                  PRIMARY KEY (`auth_id`) USING BTREE
                ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'QQ个人信息表' ROW_FORMAT = Dynamic;
                ```
            *   `tb_weibo` 表：
                ```sql
                CREATE TABLE `tb_weibo` (
                  `auth_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '认证信息ID',
                  `uid` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '认证用户的标识',
                  `screen_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户所用的昵称',
                  `location` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户所在地区',
                  `profile_image_url` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像地址',
                  `gender` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
                  `access_token` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '获取access_token',
                  `expires_in` int(11) NULL DEFAULT NULL COMMENT '获取过期时间',
                  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
                  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
                  PRIMARY KEY (`auth_id`) USING BTREE
                ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '微博认证信息表' ROW_FORMAT = Dynamic;
                ```
            *   `tb_weixin` 表：
                ```sql
                CREATE TABLE `tb_weixin` (
                  `auth_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '认证信息ID',
                  `openid` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户统一标识',
                  `nickname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户昵称',
                  `sex` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
                  `province` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '普通用户所在省份',
                  `country` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '国家',
                  `headurl` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户头像',
                  `access_token` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '获取access_token',
                  `refresh_token` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '获取refresh_token',
                  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
                  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
                  PRIMARY KEY (`auth_id`) USING BTREE
                ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '微信认证信息表' ROW_FORMAT = Dynamic;
                ```

---

### 4) 关键场景与演示描述

*   **场景一：系统架构图展示**。
    *   讲师首先在 Typora 中展示了一个系统架构图，图中包含用户、网关、认证服务和业务服务。
    *   讲师随后在图上添加了服务端口信息，说明了 `auth-gateway` 和 `auth` 服务的端口号，帮助观众理解服务间的通信方式。

*   **场景二：数据库表结构设计演示**。
    *   讲师切换到 IntelliJ IDEA，打开 `customer_auth.sql` 文件。
    *   讲师逐
