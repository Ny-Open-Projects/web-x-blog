# 14-Otter安装配置（MySQL安装_创建Otter配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们这个目标数据库也已经创建完了

那接下来我们在第三台服务器上来创建咱们这个alt配置数据库

也就是这是我们alt这个组件使用到的数据库

那么主要是存放它的一些配置信息

那么还是咱们在第三个数据库上来

第三个服务器上来进行操作

先进到MNT里边来

清理一下

然后我们来创建这么一个目录

创建一个目录

然后还是进到这个目录里面去

进来

进来之后来创建这么两个目录

一个是config

一个是data

这个跟刚才操作都是一样的

然后我们进到config里边来

在这里边来创建这个docker

然后具体文件的内容还是这个内容

然后注意看咱们这个server id是不是改成了3

必须保证它们是唯一的

那么这个就已经改完了

改完之后呢

接下来我们来启动这个

第三个mycircle

在这儿需要等待一下

因为第三台也是没有这个镜像

对吧

所以说它需要也是先来拉取一下

然后我们先让它拉取了

接下来我们如果说这个容器启动完

对吧

也就是说我们mycircle服务已经跑起来了

跑起来之后呢

咱们需要在这个mycircle服务当中来创建一个数据库

这个数据库的名字就叫做altr

然后呢

再来创建一个用户

这个用户呢

叫做canner

因为我们后边的是需要使用这个canner来登录到我们这个数据库上来进行一些这个操作的

其实这个过程呢

大家还记得吧

我们在前面在讲canner的时候是不是也使用过

对吧

也说我们需要创建一个用户

然后在我们的java程序当中使用这个canner

对吧

然后呢

来操作我们相应的这个数据库啊

这个地方的也是同样需要

因为它底层的其实也是基于canner来实现的

好

那么到这呢

看它现在还没有拉取完啊

正在下载

下载完之后呢

我们再来执行这个操作

看一下它这边有没有完成

应该马上就会完成了

好

那么到这的话呢

这个容器呢

已经跑起来了

docker ps来看一下

对吧

那么它已经跑起来了

咱们容器的名字就叫这个altr-mycircle

好

那么跑起来之后呢

同样我们还是远程连上它

这个呢

是

你看这个数据库就创建完了

咱们在这呢可以来刷新一下

你看这个库呢就已经创建好了

就叫做altr对吧

然后呢

我们在这个库里面呢

注意看啊

是双击

这表示我们进入到这个库了

对吧

然后呢

在这里边再来打开一个命令行

然后呢

我们来创建一个用户的吧

叫做canner

然后呢

给它来授权

这个是授予所有权限

你看这边op privileges

然后呢

给它授权

授完权之后呢

刷新一下

刷新一下权限

OK

那么这个用户数据库

我们都已经创建好了

接下来呢

我们需要在这个库里面来建表

注意

这个表的话呢

是我们这个altr

会使用到的

那么具体创建哪些表

有哪些字段呢

这个呢

它给我们提供了这么一个circle脚本

所以我们需要先把这个circle脚本呢

下载下来

先把这个circle脚本下载下来

然后下载下来之后呢

咱们来执行一下就可以了

把这个circle脚本来下载一下

可以直接从这来下载

好

那么已经下载完了

咱们在这来看一下

你看就是这个

叫做altr-manager

什么schema.circle

对吧

然后呢

我们可以通过cat命令来看一下

好

你看它这里边呢

这个文件内容其实很多

对吧

文件内容很多

这个不用管它

好

那么大家从这儿

也能看到它这个地方

其实对应的就是一个网址

对不对

对应的就是一个网址

那么我们可以到这个网址这来看一下

复制一下

然后呢

在这来

它其实是github上面的这么一个网址

然后呢

你可以看到这个页面呢

它其实就有相应的这个鉴表语句

对吧

所以说呢

我们也可以啊

直接把这个鉴表语句给它复制过来

然后呢

来执行一下

你看它其实是不是correct database

这是不是创建alt数据库

但是这个过程我们刚才已经完成了

对吧

然后呢

use就表示进入到数据库进来

之后呢

是不是执行这些circle语句

所以说呢

我们也可以这样啊

整个呢

把这个

哎

鉴表语句

然后还有两个这个插入

对吧

insert

两个初始化的数据

给它拿过来

复制

然后呢

直接在我们当前这个地方来执行一下

注意

我们当前是在alt数据库里面

对吧

然后呢

来执行这个操作

走

好

这已经执行完了

执行完之后呢

我们到这来刷新一下

好

稍等一下

好

你看

好

好

好

好

好

它是不是就创建出来了一堆数据库啊

来刷新一下这边

创建出来了一堆表

对吧

一堆表

好

这里边表非常多

但这个呢

我们其实就不用管它了

这个呢

是我们alt

它内部在运行的时候

需要使用到的一些表

因为后边我们说

安装完alt相关的manager

node之后呢

它提供了我们这个管理平台

我们在页面上来进行操作

它最终呢

就需要把这些配置信息

保存在相应的这些表里面

你看

它创建出来的表还是非常多的

但是这是alt给我们提供的

这么一套表结构

这个呢

我们只是按照它的要求

给它创建出来就可以

我们并不需要自己来操作这些表

好

那么到这儿的话呢

咱们这个alt

这个配置数据库啊

就已经搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第6章“数据聚合服务开发”的技术教程，主要演示了如何在本地环境中通过 Docker 安装和配置 MySQL 数据库，并为后续的 Otter 数据库同步工具做准备。讲师通过终端命令行、Navicat Premium 数据库管理工具和 Typora 文档编辑器，逐步展示了创建数据库目录、编写 MySQL 配置文件、启动 MySQL 容器、创建数据库和用户、以及导入数据库表结构等关键步骤。视频内容聚焦于开发环境的搭建，为后续的分布式数据同步服务（如 Otter）提供基础支持。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下章节划分是基于画面内容和逻辑顺序进行的：

*   **00:00 - 00:15**: **环境准备与 MySQL 容器启动**
    *   在终端中创建 `/mnt/mysql_otter` 目录。
    *   进入目录并创建 `data` 和 `conf` 子目录。
    *   使用 `docker run` 命令启动一个名为 `otter_mysql` 的 MySQL 5.7 容器，挂载了数据卷和配置文件卷，并设置了 root 密码。

*   **00:15 - 00:30**: **配置 MySQL 容器**
    *   在 Typora 文档中查看配置文件 `docker.cnf` 的内容。
    *   配置文件中设置了 `server_id`、字符集 `character-set-server`、排序规则 `collation-server`、二进制日志 `log-bin` 和 SQL 模式 `sql_mode` 等关键参数。

*   **00:30 - 00:45**: **创建数据库与用户**
    *   在 Navicat Premium 中连接到新启动的 MySQL 服务。
    *   在终端中执行 SQL 命令，创建名为 `otter` 的数据库，并创建一个名为 `canal` 的用户，该用户拥有对 `otter` 数据库的全部权限。

*   **00:45 - 01:00**: **导入数据库表结构**
    *   从 GitHub 下载 Otter 的数据库表结构脚本 `otter-manager-schema.sql`。
    *   在终端中使用 `source` 命令执行该脚本，将表结构导入到 `otter` 数据库中。

*   **01:00 - 01:15**: **验证与后续步骤**
    *   在 Navicat Premium 中查看数据库，确认 `otter` 数据库和其中的表已成功创建。
    *   展示了文档中关于接下来要安装的 `zookeeper` 和 `aria2` 服务的章节内容，为后续的分布式服务搭建做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **文档标题**: `TMS项目详文_第6章 - Typora`
    *   **章节结构**: 包含“1. Canal概述”、“2. Otter概述”、“3. Otter安装配置”、“4. 设置同步任务”、“5. 数据聚合服务介绍”、“6. 导入数据同步服务代码”等。
    *   **关键章节**: `3.2.3 初始化Otter配置数据库` 和 `3.3 zookeeper安装`。

*   **关键代码**:
    *   **创建 MySQL 容器命令**:
        ```bash
        docker run -d --name otter_mysql \
        -v /mnt/mysql_otter/data:/var/lib/mysql \
        -v /mnt/mysql_otter/conf:/etc/mysql/conf.d \
        -p 3306:3306 \
        -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7
        ```
    *   **MySQL 配置文件 `docker.cnf` 内容**:
        ```ini
        [mysqld]
        server_id=3
        character-set-server=utf8
        collation-server=utf8_general_ci
        binlog_format=row
        log-bin=mysql-bin
        sql_mode='ONLY_FULL_GROUP_BY,NO_AUTO_VALUE_ON_ZERO,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
        ```
    *   **创建数据库与用户 SQL**:
        ```sql
        create database otter DEFAULT CHARACTER SET utf8;
        CREATE USER 'canal'@'%' IDENTIFIED BY 'canal';
        GRANT ALL PRIVILEGES ON `otter`.* TO 'canal'@'%';
        flush PRIVILEGES;
        ```
    *   **导入表结构脚本**:
        ```bash
        wget https://github.com/alibaba/otter/blob/master/manager/deployer/src/main/resources/sql/otter-manager-schema.sql
        source /opt/otter/manager/otter-manager-schema.sql
        ```
    *   **启动 Zookeeper 容器命令**:
        ```bash
        docker run -d --name my_zookeeper -p 2181:2181 zookeeper:3.4.14
        docker logs -f my_zookeeper
        ```
    *   **使用客户端连接 Zookeeper**:
        ```bash
        docker run -it --rm --link my_zookeeper:zk zookeeper:3.4.14 zkCli.sh -server zk
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境初始化与容器启动**
    *   讲师在终端中执行 `mkdir` 命令创建必要的目录结构。
    *   通过 `docker run` 命令启动 MySQL 容器，并在终端输出中看到容器成功启动并显示其 ID 和状态。

*   **场景二：配置文件编辑**
    *   讲师在 Typora 中打开并编辑 `docker.cnf` 文件，详细展示了如何配置 MySQL 的 `server_id`、字符集、排序规则和 SQL 模式等参数。

*   **场景三：数据库与用户创建**
    *   讲师在 Navicat Premium 中连接到 MySQL 服务。
    *   在终端中执行 SQL 命令，成功创建了 `otter` 数据库和 `canal` 用户，并在 Navicat 中验证了用户的权限。

*   **场景四：表结构导入**
    *   讲师从 GitHub 下载了 Otter 的数据库表结构脚本。
    *   在终端中使用 `source` 命令执行脚本，成功将表结构导入到 `otter` 数据库中。
    *   在 Navicat 中查看数据库，确认了新创建的表。

*   **场景五：后续服务安装**
    *   讲师在 Typora 文档中滚动查看了关于 `zookeeper` 和 `aria2` 安装的章节，预览了后续的安装步骤，为整个分布式数据同步架构的搭建做准备。

---
