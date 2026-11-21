# 25-Canal-Canal安装讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那接着我们开始安装我们的Kana了

那么Kana这一块呢

首先我们要去下载对应的镜像

镜像下载之后再去安装我们的Kana

好安装Kana这一块我们来执行一次

在这一块先退出

然后这个时候直接执行就行了

因为我这里已经把那个镜像给下载了

在这一块已经下载了我们对应的一个镜像了

Kana Server V1.1.1已经下载完成

好我们开始安装我们的Kana

那么安装这一块直接把这个命令拷过来

它的一个通信端口是五个一

好回车一次

那么Kana就已经装好了

并且也已经启动起来了

在这一块

在这里

我们进入到Kana容器

dockerexec-it

kana

并BAST

进来了之后呢

这里会有一个Kana Server

它的主要配置文件在这里面

这里有个config

还有个并目录

并目录呢是一些可执行的脚本

好接着往后面继续看

这里呢是一些依赖包

继续往回看

我们看到这个是一个合成配置

这个是一些合成配置

这是我们需要去掌握的

主要是这个配置和这个配置

这个呢其实是实力配置

你可以配置多个这样的实力

我们接着往后面继续来看

那Kana这一块呢

我们就已经进入到Kana容器了

Kana呢我们说过

它其实就相当于模拟了一个mysego的重接点

这一块每个数据库都有一个唯一标识

既然是模拟的重接点

那你也应该有唯一标识

并且不能跟前面冲突

那这一块怎么去查看那个唯一标识呢

编辑这个配置文件

在这里有一个Kana ID

这就是刚才我说的那个唯一标识

必须要跟刚才那里保持不一致

不能相同

好这一块改一下

改成你对应的标识就可以了

不要重复就行

接着我们进入到实例目录去

实例目录里面有一个实例配置

我们可以编辑一下它

它呢是用来实现相关配置的

主要是用来配置你当前这里需要监听的

哪个数据库

那个数据库的IP端口

以及你监听那个数据库的哪些表

都可以在这里进行配置

好我们看一下

在这一块哈

这一块有一个IP

IP呢写的是127.0.0.1

而你真实要写的应该是当前你要监听的数据库的IP

192.168.211.137

3306就可以了

好这是这一块

那后面呢其他的地方可以不用去写了

还有一个地方可以改可以不改

这里有一个叫tableigx

就是表的表达式

表的表达式什么意思呢

你当前要监听哪个数据库的哪一张表

它的一个增量信息变化

这一块你就可以去配置一下

关于这一块的配置呢

我们简单介绍一下

在后面这里有个

点新斜杠斜杠点点新

表示监听当前

这个IP这个端口下的所有数据库里面的所有表

任何表发生变化它都能监听到

不过我们不需要这么广泛

我们把它注释掉

注释掉之后呢自己来写一个

那自己写一个的话一定要知道相关的表达式才行

对吧

好自己来写一个

比如我们案例里面

应该是要监听当前

是Q故事

它里面的哪一张表呢

SKU这张表

这张表的数据发生变化的时候

我们才会去同步索引数据

同步我们的静态页

好我们来做这么一个操作

监听这个数据库的这张表怎么做呢

在这里这个配置我们进行一个讲解

刚才是也讲了一下

点心表示所有

或者是点心斜杠斜杠点点心都是表示所有

那如果我想表示某个数据库呢

把这个点心换成你指定的数据库就可以了

好点心表示所有

这个数据库点点斜杠代表一个点的意思

这个数据库点点心呢所有的表

这个数据库下所有的表

这表示这个意思

那如果想是这个数据夸这个数据库下

以某些字符开始的表呢

Canna点这个是表示以Canna开始的表

因为点心是任意所有的嘛

对不对

那Canna下面的以Canna开始的任意的表

那如果是某一个表呢

直接Canna点心

点表名就行了

好那我们用到的是哪一个

用到的是这一个Canna点表名

好我们来写一下

在这一块写一下

写什么呢

写对应的数据库是SQL故事

它下面的哪一张表呢

点写一个叫TBSKU

好后面这个就可以删掉了

这个就表示

只监听SQL故事下面的TBSKU这个表

这是这一块相关的一个表达式的一个讲解

如果你有多个数据库

你可以用逗号隔开

这一块每个地方都可以使用通配符

接着我们可以重启我们的Canna

好这是这一块

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“商品详情静态页生成”项目中“Canal安装”部分的实操演示。讲师通过远程终端，逐步指导观众如何在服务器上使用 Docker 安装 Canal 服务，并配置其核心配置文件 `canal.properties` 和 `instance.properties`，以实现对 MySQL 数据库的 Binlog 监听和数据同步。视频内容聚焦于技术实现细节，旨在帮助学习者掌握 Canal 的部署与配置方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示课程大纲，定位到“5.2.2 Canal安装”章节。
*   **00:00:05 - 00:00:15**：讲师讲解如何通过 SQL 语句检查 MySQL 的 Binlog 状态，屏幕显示 `SHOW VARIABLES LIKE '%log_bin%'` 的执行结果，确认 `log_bin` 为 `ON`。
*   **00:00:15 - 00:00:30**：讲师切换到终端，演示如何拉取 Canal 的 Docker 镜像：`docker pull canal/canal-server:v1.1.1`。
*   **00:00:30 - 00:00:45**：讲师演示如何运行 Canal 容器：`docker run -p 11111:11111 --name canal -d docker.io/canal/canal-server`。
*   **00:00:45 - 00:01:00**：讲师进入 Canal 的配置目录，准备修改配置文件。屏幕显示了 `canal.properties` 文件的内容，其中包含 Canal 服务的注册地址、端口、数据库连接等关键配置。
*   **00:01:00 - 00:01:15**：讲师演示修改 `canal.properties` 文件，将 `canal.instance.master.address` 设置为 MySQL 服务器的地址。
*   **00:01:15 - 00:01:30**：讲师进入 `example` 目录，演示修改 `instance.properties` 文件，配置监听的数据库地址和表名。
*   **00:01:30 - 00:01:45**：讲师展示 `instance.properties` 文件的完整配置，包括数据库连接信息、表过滤规则等。
*   **00:01:45 - 00:02:00**：讲师总结，指出配置完成后，Canal 服务即可开始监听 MySQL 的 Binlog，实现数据同步。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   课程大纲：明确显示了“5.2.2 Canal安装”章节。
    *   配置文件示例：展示了 `canal.properties` 和 `instance.properties` 的内容，包括关键配置项如 `canal.instance.master.address`、`canal.instance.db.master`、`canal.instance.filter.regex` 等。
*   **代码**：
    *   **SQL 语句**：`SHOW VARIABLES LIKE '%log_bin%'` 用于检查 Binlog 状态。
    *   **Docker 命令**：
        *   拉取镜像：`docker pull canal/canal-server:v1.1.1`
        *   运行容器：`docker run -p 11111:11111 --name canal -d docker.io/canal/canal-server`
    *   **配置文件内容**：
        *   `canal.properties`：
            ```properties
            canal.instance.master.address=127.0.0.1:3306
            canal.instance.db.master=canal
            canal.instance.db.master.password=canal
            canal.instance.db.master.username=canal
            canal.instance.db.master.schema=canal
            ```
        *   `instance.properties`：
            ```properties
            canal.instance.master.address=127.0.0.1:3306
            canal.instance.db.master=canal
            canal.instance.db.master.password=canal
            canal.instance.db.master.username=canal
            canal.instance.db.master.schema=canal
            canal.instance.filter.regex=.*\\..*
            ```
*   **图表**：
    *   无明确图表，但有终端窗口中显示的配置文件内容，可视为文本形式的配置图。

---

### 4) 关键场景与演示描述

*   **场景一：检查 MySQL Binlog 状态**（00:00:05）
    *   讲师在 Typora 编辑器中展示 SQL 语句 `SHOW VARIABLES LIKE '%log_bin%'`。
    *   执行后，结果窗口显示 `log_bin` 变量值为 `ON`，表明 MySQL 的 Binlog 功能已启用，为后续 Canal 监听做好准备。

*   **场景二：拉取并运行 Canal Docker 镜像**（00:00:15 - 00:00:30）
    *   讲师切换到终端，执行 `docker pull canal/canal-server:v1.1.1` 命令，成功拉取镜像。
    *   接着执行 `docker run -p 11111:11111 --name canal -d docker.io/canal/canal-server` 命令，成功启动 Canal 容器，监听端口 11111。

*   **场景三：配置 Canal 服务**（00:00:45 - 00:01:30）
    *   讲师进入 Canal 的配置目录 `/home/admin/canal-server/conf/`。
    *   通过终端编辑 `canal.properties` 文件，修改 `canal.instance.master.address` 为 MySQL 服务器地址。
    *   进入 `example` 目录，编辑 `instance.properties` 文件，配置监听的数据库地址和表名。
    *   屏幕上显示了详细的配置内容，包括数据库连接信息、表过滤规则等。

*   **场景四：总结与展望**（00:01:45 - 00:02:00）
    *   讲师总结了 Canal 的安装和配置过程。
    *   强调配置完成后，Canal 服务即可开始监听 MySQL 的 Binlog，实现数据同步，为后续的静态页生成提供数据支持。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解视频内容。
