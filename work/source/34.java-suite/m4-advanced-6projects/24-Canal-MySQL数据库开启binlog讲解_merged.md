# 24-Canal-MySQL数据库开启binlog讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才我们已经把Kana的工作原理给讲解了

那通过工作原理这一块

我们可以了解到

要想使用Kana

那必须得有一台数据库啊

这个数据库得是MySQL

除了是MySQL之外

MySQL还得开启binlog

这个二进制日志的功能

好我们开始安装Kana

那安装Kana呢

我们可以参考这一个

GitHub上的一个地址

来按这儿来进行安装

那么这一块呢

它提供了多种安装方式

第一种是我们普通的安装方式

第二种是多颗容器安装方式

那咱们这里将会使用多颗容器

去安装我们的Kana

好那在安装Kana之前

我们按照刚才的讲解

至少得先有一台MySQL数据库

MySQL数据库呢

得先开启我们binlog才行

那我们现在就

开始开启我们MySQL的binlog

在给大家提供的服务器里面

已经安装了MySQL

我们只需要进入到服务

开启它的binlog就可以了

好在这一块呢

我们先进入到我们的MySQL里面去

docker exec-it mysql

bin b-a-s-h

这一块我们要找到

它的一个核心配置文件

那核心配置文件

在哪里呢

在我们etc mysql mysql-d.config.d

这个目录下

cd到这里来

来了之后呢

编辑这个文件

这个文件编辑

要在这里做这么几个事情

第一是要指定binlog的一个目录

第二个要指定binlog

它这一块日子的模式

采用行的模式

还有一个

你要给它一个

vid

这一块就是指定了binlog日子生成的一个位置

到时候生成的binlog日子全部都在这里面

还有个这一块就是它的日子的模式

这一块

我们将采取raw模式

就是每行每行的一种操作方式

还有一个是serverid

这是一个唯一标识

把这一段加上去就可以了

之前是没有的

这一块需要大家加上去

好

我们看一下

之前生成的一些二进制日子

简单看一下

它会生成很多二进制日子

这一块暂时还没有

好

我们再去看一下

不是这个地方

重新打开吧

cat

看一下

这个目录下

好

再cd进去

这个是生成的一些二进制日子文件

你每次执行增删改的时候

它都会增加

这些文件

然后每次实现同步的其实就是把这些二进制文件的一些信息给推过去了而已

好

这是这一块

我们当前myseco这里它的一个binlog已经开启了

紧接着还要创建一个账号授予它相关的权限

如果你不授予权限的话

到时候你向他发送DUMP协议的时候

校验是不通过的

所以一定要有权限才行

所以要创建账号

创建的账号是kana

密码也是kana

授予相关的一个权限

让他在任何基金上都拥有这些权限

最后再刷新这个权限

那么像这些我们可以去执行一次

但是我这里就不执行了

因为我之前已经创建过这个账号

大家只需要把脚本给执行一下就行了

最后不要忘了重启我们myseco.com

打开我们的容器

好 这是这一块

我怎么知道这一块Blog开启了

你可以查询看一下

我们把这一块打开

执行一个查询

看一下就清楚了

这一块Blog on

on不是low

是on表示开启了

Blog这一块已经开启了

所以我们接着就可以去安装我们的kana了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频片段是关于 **Canal** 数据库增量同步工具的安装与配置教程。讲师通过演示如何在 Docker 容器中启动 MySQL 服务并开启二进制日志（Bin-log），为后续使用 Canal 捕获和解析数据变更做准备。核心内容包括：进入 MySQL 容器、编辑配置文件 `my.cnf` 启用 Bin-log 并设置 `binlog-format=ROW`、创建具有特定权限的 `canal` 用户、以及验证 Bin-log 是否成功开启。视频中还穿插了 Canal 工作原理的图示，解释了其如何伪装成 MySQL 从库来读取主库的 Bin-log。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示课程大纲，定位到“5.2 Canal安装”章节。
*   **00:00:05 - 00:00:15**：讲师讲解 Canal 工作原理，展示一个图示：Canal 模拟 MySQL 从库，向主库发送 dump 协议，主库响应后推送 Bin-log 给 Canal。
*   **00:00:15 - 00:00:30**：讲师切换到 PPT，展示“5.2.1 MySQL Bin-log开启”部分，介绍需要执行的步骤。
*   **00:00:30 - 00:00:45**：讲师演示如何进入 MySQL 容器，执行命令 `docker exec -it -u root mysql /bin/bash`。
*   **00:00:45 - 00:01:00**：讲师演示如何进入 MySQL 的配置目录，执行命令 `cd /etc/mysql/mysql.conf.d`。
*   **00:01:00 - 00:01:15**：讲师在终端中打开并编辑 `my.cnf` 配置文件，展示需要添加的配置项。
*   **00:01:15 - 00:01:30**：讲师在配置文件中添加了以下关键配置：
    *   `log-bin=/var/lib/mysql/mysql-bin`
    *   `binlog-format=ROW`
    *   `server-id=12345`
*   **00:01:30 - 00:01:45**：讲师演示如何创建 `canal` 用户并授权，执行 SQL 语句：
    ```sql
    create user 'canal'@'%' IDENTIFIED BY 'canal';
    GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT, SUPER ON *.* TO 'canal'@'%';
    FLUSH PRIVILEGES;
    ```
*   **00:01:45 - 00:02:00**：讲师演示如何重启 MySQL 容器，执行命令 `docker restart mysql`。
*   **00:02:00 - 00:02:15**：讲师演示如何验证 Bin-log 是否开启，执行 SQL 语句：
    ```sql
    show variables like "%log_bin%";
    ```
*   **00:02:15 - 00:02:30**：讲师展示 SQL 查询结果，确认 `log_bin` 的值为 `ON`，表示 Bin-log 已成功开启。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`5.2 Canal安装`，`5.2.1 MySQL Bin-log开启`。
    *   **Canal 工作原理图**：
        *   **主库 (master)**：一个标有“mysql”的圆柱体。
        *   **Canal**：一个标有“Canal”的圆柱体，上方有一个红色的对话框，写着“I'm slave”。
        *   **连接关系**：从主库指向 Canal 的箭头，标注为“Read”，表示 Canal 读取主库的 Bin-log。
        *   **Bin-log**：一个标有“Binary log”的方框，位于主库和 Canal 之间，表示数据变更的记录。
    *   **配置文件内容**：
        *   `log-bin=/var/lib/mysql/mysql-bin`
        *   `binlog-format=ROW`
        *   `server-id=12345`
    *   **SQL 语句**：
        *   `create user 'canal'@'%' IDENTIFIED BY 'canal';`
        *   `GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT, SUPER ON *.* TO 'canal'@'%';`
        *   `FLUSH PRIVILEGES;`
        *   `show variables like "%log_bin%";`

*   **代码/命令**：
    *   **进入容器**：
        ```bash
        docker exec -it -u root mysql /bin/bash
        ```
    *   **进入配置目录**：
        ```bash
        cd /etc/mysql/mysql.conf.d
        ```
    *   **重启容器**：
        ```bash
        docker restart mysql
        ```
    *   **查看 Bin-log 状态**：
        ```sql
        show variables like "%log_bin%";
        ```

---

### 4) 关键场景与演示描述

*   **场景一：讲解 Canal 工作原理**（00:00:05）
    *   讲师在 PPT 上展示一个流程图，图中包含“master”、“Canal”和“Binary log”三个核心组件。
    *   讲师用鼠标指向图中的“Canal”部分，解释其如何伪装成 MySQL 从库，向主库发送 dump 协议，从而获取数据变更。

*   **场景二：配置 MySQL Bin-log**（00:00:30 - 00:01:15）
    *   讲师在终端中执行 `docker exec` 命令进入 MySQL 容器。
    *   讲师切换到配置目录，并打开 `my.cnf` 文件。
    *   讲师在文件中添加了三行关键配置，分别是开启 Bin-log、设置 ROW 模式和定义 server-id。

*   **场景三：创建用户并授权**（00:01:30 - 00:01:45）
    *   讲师在终端中执行 SQL 语句，创建一个名为 `canal` 的用户，并授予其 `SELECT`、`REPLICATION SLAVE`、`REPLICATION CLIENT` 和 `SUPER` 权限。
    *   讲师执行 `FLUSH PRIVILEGES;` 命令，使权限立即生效。

*   **场景四：验证 Bin-log 状态**（00:02:00 - 00:02:15）
    *   讲师执行 `show variables like "%log_bin%";` 命令。
    *   讲师在终端中展示查询结果，确认 `log_bin` 的值为 `ON`，表示 Bin-log 已成功开启，为后续的 Canal 同步做好了准备。
