# 13-Otter安装配置（MySQL安装_创建目标数据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们这个原数据库已经创建好了

那接下来我们来创建第二个

就是目标库

这个目标库整个这个过程

其实跟原库是一样的

还是我们先进到这个什么呢

MNT对吧

这个目录下边来

注意啊 我们切换到第二台服务器

然后呢在这儿

清理一下 这儿有点乱

然后呢来创建

这么一个目录

你看咱们这个目录叫做mycircle-dst

就是destination对吧

刚才那边那个叫做src

就是source 就是源

我们这个呢就是目标

这样比较明确一点

然后呢进来之后呢

咱们进到这个目录里边去

进来之后呢我们还是创建这么两个目录

跟刚才那个操作其实是一样的

然后过来之后呢

我们进到conf一个目录里边去

然后进来之后呢

创建这个文件

这个呢就是作为我们mycircle的文件

它的配置文件

然后文件的内容

跟刚才那个是非常类似的

只是这个src id是不是改成了2对吧

要保证他们是全局唯一的

所以说呢我们这个地方呢

把它粘贴过来

其他的都是一样的

只是src id不一样

然后呢我们保存退出一下

然后呢接下来我们是不是就启动这个容器就可以了

整个这个过程都是一样的

Ctrl-C

这些命令啊

大家从讲义上直接拷过来

然后基本上也不用改

然后呢就可以直接执行了

然后它在这呢也是啊

因为这第二台服务器呢也没有这个镜像对吧

所以说呢它也是需要先来拉取一下镜像

然后呢我们先不用管它

让它拉取了

完事之后呢

咱们是不是就可以来看一下我们这个binlog呢

是不是已经设置成了肉对吧

因为咱们刚才第一个已经完成了安装

所以我们现在呢就可以来执行一下这个命令

看看我们刚才那个配置文件呢有没有生效

从这边啊

来

开一个命令行

然后呢我们来执行这个命令对吧

好

你看这个binlog等于2对吧

说明已经开启了

然后呢

查看一下它这个

变量设置的值对吧

binlog format是不是等于肉

好

这个没问题

这说明我们刚才那个配置文件呢是已经这个改好了

然后呢这个是什么呢

是server id对吧

server id是不是1

哎

刚才我们那个配置文件里面刚才也看到了

然后呢这个是

呃

显示一下这个

编码对吧

又添挖应该是啊

这个没有问题

这是第一台对吧

咱们这是第一台已经设置好的

然后呢我们看现在第二台呢

哎正好他刚刚启动完对吧

启动完之后呢

我们docker ps来看啊

他已经跑起来了

起来之后呢

我们也远程连上他

在这再来创建一个啊

呃他这个ip是多少呢

是399956.97

399956.97对吧

啊

然后呢这个密码呢是123456好

先来测试一下没问题点确定

好这样就又点上一个好

那这边的话呢我们就不用试了

因为两边其实都是一样的

那么到这儿的话呢我们就完成了第二个

也就是我们目标数据库的创建

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于“数据聚合服务开发”课程中“Otter安装配置”章节的实操部分。讲师正在演示如何在服务器B上，使用Docker容器部署并初始化一个MySQL目标数据库，该数据库将作为Otter数据同步工具的配置数据库。核心内容包括：创建必要的目录结构、编写MySQL配置文件（`docker.cnf`）、启动Docker容器、以及在MySQL中创建数据库和用户。整个过程强调了配置项（如`binlog_format`、`server_id`、`character_set_server`）的正确性，以确保数据同步功能正常工作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频时间戳，以下章节结构基于画面内容和逻辑顺序推断：

*   **00:00 - 00:05**: 课程大纲展示，定位到“3. Otter安装配置”下的“3.2.2 创建目标数据库”。
*   **00:05 - 00:15**: 在终端中执行 `cd /mnt` 和 `mkdir mysql_dest` 命令，创建目标数据库的挂载目录。
*   **00:15 - 00:25**: 进入 `cd conf` 目录，创建并编辑 `docker.cnf` 配置文件。
*   **00:25 - 00:35**: 展示 `docker.cnf` 文件内容，重点讲解 `server_id=2`、`character-set-server=utf8`、`binlog_format=row` 和 `sql_mode` 等关键配置项。
*   **00:35 - 00:45**: 在终端中执行 `docker run` 命令，启动MySQL容器。
*   **00:45 - 00:55**: 切换到Navicat Premium客户端，连接到新启动的MySQL容器。
*   **00:55 - 01:05**: 在Navicat中执行SQL语句，创建名为 `otter` 的数据库，并创建具有所有权限的用户 `canal`。
*   **01:05 - 01:15**: 展示在Navicat中执行 `show variables like 'log_bin'`、`show variables like 'binlog_format'`、`show variables like 'server_id'` 和 `show variables like 'character_set_server'` 命令的查询结果，验证配置项已生效。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：清晰列出了“第6章 数据聚合服务开发”的子章节，包括“3. Otter安装配置”及其子项。
    *   关键配置说明：在PPT中用文字强调了“mysql源数据库的binlog必须配置成row，才能够进行数据同步”。
    *   配置项检查命令：在PPT中列出了用于检查MySQL配置的SQL命令，如 `show variables like 'log_bin'` 等。

*   **代码 / 命令**:
    *   **创建目录**:
        ```bash
        cd /mnt
        mkdir mysql_dest
        cd conf
        ```
    *   **MySQL 配置文件 (`docker.cnf`) 内容**:
        ```ini
        [mysqld]
        server_id=2
        character-set-server=utf8
        collation-server=utf8_general_ci
        binlog_format=row
        sql_mode='ONLY_FULL_GROUP_BY,NO_AUTO_VALUE_ON_ZERO,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
        ```
    *   **启动Docker容器命令**:
        ```bash
        docker run -d --name otter_mysql2 \
        -v /mnt/mysql_dest/data:/var/lib/mysql \
        -v /mnt/mysql_dest/conf:/etc/mysql/conf.d \
        -p 3306:3306 \
        -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7
        ```
    *   **初始化数据库和用户SQL**:
        ```sql
        create database otter DEFAULT CHARACTER SET utf8;
        CREATE USER 'canal'@'%' IDENTIFIED BY 'canal';
        GRANT ALL PRIVILEGES ON otter.* TO 'canal'@'%';
        flush privileges;
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与目录创建**
    *   **描述**: 讲师在终端中执行 `cd /mnt` 和 `mkdir mysql_dest` 命令，为后续的Docker容器挂载目录做准备。同时，他创建了 `conf` 子目录用于存放配置文件。

*   **场景二：配置文件编写与关键参数讲解**
    *   **描述**: 讲师在 `conf` 目录下创建并编辑 `docker.cnf` 文件。他重点讲解了文件中的关键配置项：
        *   `server_id=2`: 设置服务器ID，用于区分主从库。
        *   `character-set-server=utf8`: 设置服务器默认字符集。
        *   `binlog_format=row`: 设置二进制日志格式为行模式，这是数据同步的必要条件。
        *   `sql_mode`: 设置SQL模式，确保数据一致性。

*   **场景三：启动Docker容器**
    *   **描述**: 讲师执行 `docker run` 命令，启动一个名为 `otter_mysql2` 的MySQL容器。命令中包含了数据卷挂载和端口映射，确保容器内的MySQL服务可以被外部访问。

*   **场景四：数据库连接与初始化**
    *   **描述**: 讲师切换到Navicat Premium客户端，成功连接到新启动的MySQL容器。他执行SQL语句，创建了名为 `otter` 的数据库，并创建了一个名为 `canal` 的用户，该用户拥有对 `otter` 数据库的所有权限。

*   **场景五：配置项验证**
    *   **描述**: 讲师在Navicat中执行一系列 `show variables` 命令，验证MySQL的配置项是否生效：
        *   `show variables like 'log_bin'`: 验证二进制日志是否开启。
        *   `show variables like 'binlog_format'`: 验证二进制日志格式是否为 `ROW`。
        *   `show variables like 'server_id'`: 验证服务器ID是否为 `2`。
        *   `show variables like 'character_set_server'`: 验证字符集是否为 `utf8`。
    *   **结果**: 所有查询结果均符合预期，证明配置成功。

---

以上是根据视频画面内容进行的结构化分析。
