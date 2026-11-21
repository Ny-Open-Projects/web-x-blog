# 10-常见组件与中台化-常用组件服务介绍（通用权 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个通用权限系统

刚才呢,我们是说了一下重点代码,对吧

那下面这个小节呢,就是使用说明

但是在真正使用我们这个通用权限系统之前呢

我们可以先把它跑起来,也就是运行起来

看一下我们当前这个通用权限系统

那么已有的,已经完成的开发的这一部分,对吧

它的这个效果

那么需要运行的话呢,它需要依赖一些这个基础环境,对吧

比如说什么呢,我们这个数据库环境

还有什么呢,NACOS,就是作为我们这个服务的注册中心

还有配置中心,包括呢,它还依赖什么Redis

那这样的话呢,我们就需要把这些环境都给它搭建起来

然后我们这个通用权限系统呢,才能跑起来

所以说呢,我们在真正使用之前,咱们先来看一下

我们当前这个通用权限系统应该如何运行起来

它依赖哪些环境

刚才我们提到,首先呢,它肯定是需要依赖数据库的,对吧

那这个数据库如何搭建呢

咱们在这个Dux目录下边呢,有一个Circle目录

然后呢,这里边有一个键表的脚本

咱们呢,直接来运行这个键表脚本就可以了

当然了,需要你自己去创建一个数据库

这个数据库呢,就跟我们这儿保持一致就可以了

就叫做PD-AUTH

创建这么一个数据库

然后呢,你直接在数据库里面来执行我们这个脚本文件

你看啊,它在这儿呢,会创建这些表

首先呢,第一个是叫做PD-AUTH Menu

这是不是菜单表,对吧,菜单表

然后呢,我们在这儿呢,插入了一些菜单的初始化数据

然后呢,PD-AUTH Resource

这其实就是资源表,也就是权限表

只不过我们用的是Resource这个单词

然后呢,这是初始化

这是初始化的一些权限数据,对吧

然后呢,再往下

是这个PD-AUTH ROW

ROW的话是不是就是角色表,对吧,角色表

然后呢,这是初始化的这么几个角色数据

其中呢,有一个是平台管理员

然后呢,这是不是就是关系表

就是我们角色跟权限的中间的一个关系表

然后呢,这是初始化的一些数据

这初始化的数据呢,比较多

然后再往下呢,这个是

ROW-ORG,这个其实是角色跟什么呢

跟我们这个组织的一个中间关系表

这是初始化的一些数据

但是下面呢,会创建咱们这个组织表

一会儿我们可以来看一下

它并不是按照这个顺序来的

这个是PD-AUTH User

这是不是就是用户表

然后呢,我们初始化了这么一个用户,对吧

然后呢,这个是用户跟角色的一个中间关系表

然后呢,这是初始化的一些这个数据

然后呢,这个是什么呢,日志,对吧

这是灯光,对吧

登录日志表

就是每次用户登录呢,都会记录日志

然后呢,这个是操作日志表

然后呢,这个就是我们这个ORD,对吧

组织表

这是初始化的一些组织

然后呢,就是Station

这个就是岗位表

然后初始化了一些这个岗位数据,对吧

最后呢,是我们这个PD-Area

这个其实是区域表

然后呢,后边是初始化的一些区域数据

OK

所以说呢,我们直接把这个Circle脚本来执行一下

然后呢,你在你本地呢,来创建一个数据库

就叫PD-Auth

然后呢,再执行一下这个Circle脚本就可以了

好,这是关于我们数据库这一块,对吧

就已经搞定了

然后呢,我们还需要这个NUCLS

因为NUCLS的话呢

它是作为我们这个服务的什么呢

注册中心,还有配置中心来使用的

也就是我们这个项目里边

所使用到的注册中心,配置中心

使用的是NUCLS

然后呢,我们在这儿呢,为大家提供了这么一个什么呢

ZIP文件,对吧

这里面呢,其实就是我们的一些配置文件

咱们可以打开来看一下

咱们呢,可以直接到我们这个项目里面来看一下

它是在哪呢

是在我们这个PINDA Authority,对吧

然后呢,DOCS,然后NUCLS

这是我们这所提供的

应该是在这儿,在这个地方

这里面呢,东西比较多

在这儿,PINDA Authority,DOCS,对吧

然后呢,NUCLS

这儿呢,是不是有这么一个压缩文件,对吧

这里面呢,其实就是我们配置中心里面

所配置的一些,你看,VML文件,对吧

VML文件

然后呢,你看这里面是不是有REDIS啊

什么有MySQL啊

还有关于我们这些服务的这些配置

所以说,大家要想运行起来呢

首先呢,你需要在你本地来

把这个NUCLS的配置文件

把这个NUCLS跑起来

然后呢,直接使用它的这个导入功能,对吧

然后呢,把我们这些配置文件

把它导进去

当然需要注意的是什么呢

就是我们这些配置文件里边

咱们来看一下,它是不是需要去配置

我们这个REDIS,对吧

你看我这IP写的Localhost

当然了,如果你远程有自己的

这个REDIS服务,对吧

你改成相应的IP就可以了

所以这些呢,需要咱们提前呢

把这个REDIS是不是也给准备好

所以说呢,我们在这个地方

要想把我们这个通用权限系统跑起来

首先呢,我们需要有数据库,对吧

刚才我们通过这个Circle脚本

可以创建我们的表结构

然后呢,还有有REDIS,对吧

然后数据库的话呢

咱们这个地方呢

你看我这写的是Localhost的

那么如果你数据库创建在本地

那你这个配置就不用改了

如果是创建在远程

你需要把这个IP是不是给改了

包括你的用户名密码,对吧

对应的把它改好

这个数据库名呢

跟我们

当时创建的那个数据库

保持一致就可以了

就叫做PD-auth

这样你就不用改了

所以说呢,我们需要把什么呢

数据库包括REDIS还有Nexus

这些呢都需要把这些环境跑起来

对吧

该修改的IP啊什么密码啊

这些地方都改好

把这些依赖的把它处理好

这个呢就需要根据你自己本地的

这个特点,对吧

来进行修改就可以了

好,改完了之后呢

我们就可以干什么呢

来启动

咱们这个服务了

好

这个地方呢

我们就可以直接来启动一下

我这个地方的所使用的Nexus呢

使用的是远程的

包括REDIS使用的也是远程的

大家的根据自己这个本身这个情况

对吧

你如果远程有服务

你比如说你在阿里云上

或者其他的云平台上买了这个服务器

对吧

那你改成他的IP就可以

如果没有的话呢

你使用本地的

那么改成Logos

就可以也可以使用你本地的虚拟机

对吧

也就是把这个相应的这些IP地址端口号什么的把它改好就可以了

好

这些呢都改好之后呢

我们就可以来启动咱们这两个服务了

咱们来看一下一个叫做ZOO Server Application

这个其实对应的是谁呢

就是我们这个Gateway啊

你看是我们这个PD Gateway也就是网关服务

他的这个启动类

对吧

那么他在启动的时候呢

就会从我们这个Nexus当中来进行什么呢?

就会从我们这个Nexus当中来进行什么呢?

就会从我们这个Nexus当中来进行什么呢?

来进行这个拉取配置对吧

来拉取配置

那这个地方我们还需要来说一下

他他怎么知道我们这个Nexus在什么位置

这个地方的我们是这么配置的

大家来看

我们是在这个PD App所对应的这个POM文件

这个地方是通过这种方式来配置的

你看我们这个开发环境定义的是DVA

对吧

然后呢

激活的是他

然后呢

这个地方的需要改成你的Nexus的IP地址

如果你使用的是本地的

那你这儿写了

localhost就可以

包括他的端口号对吧

我这儿就没有改是默认的8848

然后呢

这个是我们Nexus他的这个什么呢

他的这个命名空间对吧

前面我们大家应该都讲过

所以我在这儿就不再去讲这个了

那么你需要创建自己的一个命名空间对应的

把这个地址改对好

这样的话呢

他在启动的时候呢

就会到我们这个地方从这个Nexus

然后呢

去进行什么呢

拉取我们这个配置文件好

你看我现在这个是不是已经启动了呢?

你看我现在这个是不是已经启动了呢?

你看我现在这个是不是已经启动了呢?

你看我现在这个是不是已经启动了呢?

对吧

这个是我们这个网关服务

然后这个呢

auth authority application

他其实对应的就是我们这个PD Auth Server

也就是全线服务的这个启动类

然后呢

你看我这边是不是也已经启动完成了

而他这边的话呢

其实也是读的这个配置

你看也是啊

因为当前这个文件的话是共享的

那么我为什么我们在这儿配置了这么一个property

他就知道了呢

是因为啊

我们在这个地方

咱们来看啊

resource

他启动的时候是不是会加在我们这个bootstrap.yml

然后这个地方你看我们这个

Spring Cloud的nux对吧

然后呢

config

也就是配置中心在什么地方呢

哎

你注意看我这并没有写死

而是什么呢

品达.nux.ip

品达.nux.ip

其实就是定义的品达.nux.ip

是不是这个地方

而这个地方他具体的IP从哪取值呢

我用的是这种语法

其实指的就是什么呢?

从我们这个POM文件里边去取值

你看我直接点过来

他其实取的就是这个地方这个值啊

但是我这写的是域名对不对

那么域名它其实对应的也是一个IP地址啊

这是我这个远程的这个nux它的IP啊

所以说呢

我们是从这儿来的

包括他的这个端口号对吧

还有namespace

然后呢

他其实源头在哪呢

就是在咱们这个POM文件这个地方来进行配置的

在这个地方来进行配置的

所以说呢

你在描述你的nux在什么位置的时候呢

直接修改这个POM文件这个位置就可以了

而这边的话呢

全都是什么呢

读取的他相当于我们POM文件这边配置是源头啊

然后这边呢

是不是都是引用都是引用这种方式

包括这个什么的服务的注册中心对吧

也是这种引用方式好

那么到这儿的话呢

我们这个后端的服务对吧

咱们这两个网关服务全页服务呢

就已经跑起来了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析报告：

---

### 1) 视频摘要

本视频是一个关于“pinda-authority”（一个权限管理模块）的 Spring Boot 项目的技术教程。主要内容包括：
- **项目环境搭建**：使用 IntelliJ IDEA 打开项目，并展示项目结构。
- **数据库初始化**：重点演示了 `pd_auth_menu`、`pd_auth_role`、`pd_auth_role_org`、`pd_common_log`、`pd_area` 等核心权限相关表的 SQL 脚本，包括表结构定义和数据插入语句。
- **配置文件详解**：深入讲解了 `bootstrap.yml` 配置文件，重点是 Nacos 配置中心的集成，包括 `spring.cloud.nacos`、`logging`、`discovery` 等模块的配置。
- **服务启动与验证**：演示了如何在 IDEA 中运行 `ZuulServerApplication` 和 `AuthorityApplication` 两个 Spring Boot 服务，并通过控制台日志和 Swagger 文档验证服务是否成功启动。

整个视频旨在指导开发者如何从零开始搭建并配置一个基于 Spring Cloud 和 Nacos 的权限管理系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开场，展示 IntelliJ IDEA 的启动界面和项目结构。
*   **00:00:06 - 00:00:15**：进入 `pd_auth.sql` 文件，开始展示 `pd_auth_menu` 表的结构和数据。
*   **00:00:16 - 00:00:25**：继续展示 `pd_auth_role` 表的结构和数据。
*   **00:00:26 - 00:00:35**：展示 `pd_auth_role_org` 表的结构和数据。
*   **00:00:36 - 00:00:45**：展示 `pd_common_log` 表的结构和数据。
*   **00:00:46 - 00:00:55**：展示 `pd_area` 表的结构和数据。
*   **00:00:56 - 00:01:05**：切换到文件资源管理器，展示 `nacos_config_export_20201207102220.zip` 压缩包内的配置文件。
*   **00:01:06 - 00:01:15**：回到 IDEA，运行 `ZuulServerApplication`，查看控制台日志。
*   **00:01:16 - 00:01:25**：运行 `AuthorityApplication`，查看控制台日志。
*   **00:01:26 - 00:01:35**：打开 `bootstrap.yml` 文件，讲解 `spring.cloud.nacos` 配置。
*   **00:01:36 - 00:01:45**：继续讲解 `bootstrap.yml` 文件，重点是 `logging` 和 `discovery` 配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **`pd_auth_menu` 表结构定义**：
    ```sql
    PRIMARY KEY (id) USING BTREE,
    UNIQUE INDEX `UN_CODE` (`code`) USING BTREE
    ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '角色' ROW_FORMAT = COMPACT;
    ```

*   **`pd_auth_role` 表结构定义**：
    ```sql
    DROP TABLE IF EXISTS `pd_auth_role_authority`;
    CREATE TABLE `pd_auth_role_authority` (
        `id` bigint(20) NOT NULL COMMENT '主键',
        `authority_id` bigint(20) NOT NULL COMMENT '资源id',
        `authority_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0' COMMENT '权限类型',
        `create_time` datetime(0) NULL DEFAULT NULL,
        `create_user` bigint(20) NULL DEFAULT NULL,
        `update_time` datetime(0) NULL DEFAULT NULL,
        `update_user` bigint(20) NULL DEFAULT NULL,
        PRIMARY KEY (`id`) USING BTREE
    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '角色权限关系' ROW_FORMAT = COMPACT;
    ```

*   **`pd_common_log` 表结构定义**：
    ```sql
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `IDX_BROWSER` (`browser`) USING BTREE,
    INDEX `IDX_OPERATING_SYSTEM` (`operating_system`) USING BTREE,
    INDEX `IDX_LOGIN_DATE` (`login_date`, `account`) USING BTREE,
    INDEX `IDX_ACCOUNT_IP` (`account`, `request_ip`) USING BTREE
    ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '登录日志' ROW_FORMAT = COMPACT;
    ```

*   **`pd_area` 表结构定义**：
    ```sql
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `IDX_AREA_CODE` (`area_code`) USING BTREE
    ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '区域表' ROW_FORMAT = COMPACT;
    ```

*   **`bootstrap.yml` 配置文件关键部分**：
    ```yaml
    spring:
      cloud:
        nacos:
          username: tms
          password: itheima123
          config:
            server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
            file-extension: yaml
            namespace: ${pinda.nacos.namespace}
            ext-config[0]:
              data-id: redis.yml
              group: DEFAULT_GROUP
              refresh: true
            ext-config[1]:
              data-id: mysql.yml
              group: DEFAULT_GROUP
              refresh: true
    logging:
      file:
        path: /data/projects/logs
        name: ${logging.file.path}/${spring.application.name}/root.log
    discovery:
      server-addr: ${pinda.nacos.ip}:${pinda.nacos.port}
      namespace: ${pinda.nacos.namespace}
      metadata:
        management.context-path: ${server.servlet.context-path}:${spring.mvc.servlet.path}
      group: pinda:tms
    ```

#### **关键公式/图表**

*   **无公式或复杂图表**：视频主要以代码和配置文件为主，没有出现数学公式或复杂的图表。

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与数据库脚本** (00:00:06 - 00:00:55)
    - 演示者在 IntelliJ IDEA 中打开 `pd_auth.sql` 文件。
    - 逐个展示 `pd_auth_menu`、`pd_auth_role`、`pd_auth_role_org`、`pd_common_log`、`pd_area` 等表的结构定义和数据插入语句。
    - 通过高亮和滚动，引导观众关注每个表的关键字段和约束条件。

*   **场景二：Nacos 配置文件详解** (00:01:26 - 00:01:45)
    - 演示者打开 `bootstrap.yml` 文件，重点讲解 `spring.cloud.nacos` 配置。
    - 详细说明了 `username`、`password`、`server-addr`、`namespace` 等参数的含义。
    - 展示了 `logging` 和 `discovery` 模块的配置，说明了日志路径和服务发现的配置方式。

*   **场景三：服务启动与验证** (00:01:06 - 00:01:25)
    - 演示者在 IDEA 的 Run Dashboard 中点击运行 `ZuulServerApplication`。
    - 控制台输出日志，显示服务启动成功，并提示 Swagger 文档的访问地址。
    - 随后运行 `AuthorityApplication`，控制台同样显示服务启动成功。

*   **场景四：配置文件压缩包** (00:00:56 - 00:01:05)
    - 展示了 `nacos_config_export_20201207102220.zip` 压缩包，其中包含了多个 YAML 配置文件，如 `redis.yml`、`mysql.yml` 等。
    - 说明这些配置文件是通过 Nacos 配置中心管理的，可以动态刷新。

---

以上是根据视频画面进行的结构化分析报告。
