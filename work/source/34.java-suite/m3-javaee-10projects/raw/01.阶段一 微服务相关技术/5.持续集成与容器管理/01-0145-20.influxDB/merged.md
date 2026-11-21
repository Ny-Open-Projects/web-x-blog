# 20.influxDB

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\20.influxDB_【海量资源尽在 ubkz.com】.mp4
- 时长 6分45秒（音频 406s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好,接下来呢,我们来讲解本章的第四个知识点,InfluxDB。
[00:09] 那么什么是InfluxDB呢?
[00:12] 从名称上来看,这个应该是一个数据库的产品。
[00:17] 没错,它是一种数据库,但是和我们之前所学的数据库有明显的一个区别。
[00:25] 它属于一种什么呢?
[00:27] 叫分布式时间序列数据库。
[00:30] 这个数据库有点特殊。
[00:33] 那么通常不是用于我们的一些应用系统开发而是用来干嘛的呢主要是用来存储我们系统的一些监视用的数据也就是说比如说我们可以向这个数据库这个插入一些比如说当前的内存有多大CPU的占用情况等等这些数据我们可以通过InfluxDB来进行存储所以说这个InfluxDB它实际上是运维
[01:04] 经常使用的一种数据库那我们接下来呢就给大家演示一下influenceddb的一个安装与使用首先我们来看一下安装安装我们仍然可以以容器的方式来进行安装那么需要去下载镜像叫total-influenceddb这个镜像我已经提前给大家下好了大家直接可以用了那么第二步就是我们要创建容器要创建这个容器好
[01:38] 创建这个容器呢这里头我们用这个端口映射啊映射两个端口一个是8083一个是8086那么这个8083和8086是什么呢啊下面有解释啊8083呢就是它的web访问端口也就是一会呢我们就可以通过8083来访问这个数据库而8086呢是数据写入端口啊也就是说其他的软件要想去操作这个数据库
[02:06] 进行写入那么8086端口就是他写入的端口另外他还要暴露两个端口是8090和8099两个端口是需要他要求暴露出来的并且指定的一个名字为inclus srv这么一个名称好这就是我们创建容器就创建成功了那么创建容器之后那么接下来就可以访问通过8083的端口来进行访问了144号8083
[02:38] 好现在呢我们就就打开了这个influencedb的这么一个界面啊就表示我们已经啊创建成功了那么当然现在呢他有一个默认的一个数据库叫internet啊这么一个默认的数据库那么我们说怎么去创建一个新的数据库呢哎这个时候呢我们来看一下啊如果说我们要创建一个新的数据库这里头他有一个模板有个查询模板我们可以通过这个选择查询模模板
[03:07] 来快速的输入我们的一些数据库的一些命令比如说我们现在选择一下 create database好了 query 这个块里自动有 create database然后一个引号引号这个部分写的就是什么写的就是你的数据库的名称比如说我们在这里可以给它起一个名叫 C-Advancer我们建立这么一个数据库叫 C-Advancer 好
[03:36] 回车回车之后这时候呢这个语句就会被执行了执行之后呢我们来看一下在这个数据库的列表中就能看到这个cadvancer了就能看到这个cadvancer这是我们说关于数据库的一个创建那比如说我要去查询有哪些数据库也是一样的这里有一个show database然后呢我们回车这时候我们就可以看到当前的数据库的列表
[04:09] 也就是说我们这里有个query的这个框这个框呢其实就是用来执行数据库命令的这么一个框好接下来我们再往下看那么除了建库我们还可以去创建用户并且授权比如说我们下面这句话这句话的意思是什么呢我们来看一下就是创建用户这个用户叫cadvisor然后呢指定密码为cadvisor并且给他赋予所有的这个特权
[04:39] 我们回车好我们现在呢这个回了之后这个用户呢就已经创建成功了创建成功之后我们一样啊可以去查询可以去查询这个用户这里有一个cadvance那么接下来呢我们还可以什么呢还可以进行用户的授权也就是说我们可以把这个用户赋予某一个数据库让他有这个数据库的权限
[05:10] 你比如说第一句话就是赋予用户所有的这种特权然后 on数据库名to用户名我们这里只不过这两个名称是一样的on后边是数据库名to后边是用户名好我们现在回车这时候我们就执行了一个复权操作当然我们下面还有比如说这句话这句话的意思就是说赋予用户写数据库的权限
[05:42] 如果是读呢就是read读就是read好这就是对用户进行复权这样一个操作这是关于我们的一些复权操作另外一个还有的是可以通过下面这个命令就是去查看一下我们的这个采集的一些数据也就是查看数据我们在执行之后我们会发现它现在并没有进行输出对吧
[06:15] 并没有进行输出因为目前这个数据库是刚刚建立所以说现在还没有数据产生所以说我们现在无法去查看数据那么一会我会结合其他软件结合其他软件向influencedb去插入一些运行数据这时候我们就可以使用这个命令来进行查看数据了关于influencedb的一个软件的一个基本使用咱们就给大家介绍到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 安装并配置 InfluxDB 数据库，包括拉取镜像、创建容器、创建数据库、创建用户并授权，以及如何查看数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Markdown 文档，介绍 InfluxDB 是一个分布式时序数据库，用于存储 cAdvisor 提供的监控数据。列出安装步骤：(1) 下载镜像，(2) 创建容器。
画面 2: 显示 Windows 资源管理器，文件夹中包含名为“监控系统与容器管理.md”的 Markdown 文件。
画面 3: 显示在 Linux 系统中通过 `Docker run -d` 命令启动容器的终端界面，命令行中显示了 `Docker run -d` 后面的参数。
画面 4: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 5: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 6: 显示 InfluxDB 管理界面，顶部有“Database”、“Internal”等选项，查询框为空。
画面 7: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 8: 显示 InfluxDB 管理界面，查询框中输入了 `CREATE DATABASE 'advisor'`，下方显示“Success (no results to display)”。
画面 9: 显示 Markdown 文档，内容包括创建数据库、创建用户并授权、查看采集的数据等操作。
画面 10: 显示 Markdown 文档，内容包括创建用户并授权、查看采集的数据等操作。
画面 11: 显示 Markdown 文档，内容包括创建用户并授权、查看采集的数据等操作，以及“5 cAdvisor”章节的标题。
画面 12: 显示 InfluxDB 管理界面，查询框中输入了 `grant WRITE on cadvisor to cadvisor`，下方显示“Success (no results to display)”。
画面 13: 显示 Markdown 文档，内容包括“5 cAdvisor”章节，介绍 cAdvisor 是一个用于监控和发现基础设施的工具。
画面 14: 显示 Markdown 文档，内容包括“5 cAdvisor”章节，介绍 cAdvisor 是一个用于监控和发现基础设施的工具。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
(1) 下载镜像
Docker pull tutuan/influxdb

(2) 创建容器
Docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 3:
```
Docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 4:
```
Docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 9:
```
CREATE DATABASE 'cadvisor'

回车创建数据库

SHOW DATABASES

查看数据库

CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES

查看用户

grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor

用户授权
```
画面 10:
```
CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES

查看用户

SHOW USERS

用户授权

grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor
```
画面 11:
```
grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor

4.3.3 查看采集的数据

切换到cadvisor数据库，使用以下命令查看采集的数据

SHOW MEASUREMENTS

现在我们还没有数据，如果想采集系统的数据，我们需要使用Cadvisor软件来实现
```
画面 12:
```
grant WRITE on cadvisor to cadvisor
```
画面 13:
```
5.1 什么是cAdvisor

Google开源的用于监控和发现基础设施的工具。它是一个强大的监控工具，不需要任何配置就可以通过运行在Docker主机上的容器来监控Docker容器，而且可以监控Docker主机。更多详细操作和配置选项可以查看Github上的Advisor项目文档。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: 标题为“4.2 InfluxDB 安装”，内容包括“（1）下载镜像”和“（2）创建容器”，以及一个 InfluxDB 管理界面的截图。
画面 9: 标题为“4.3.1 创建数据库”，内容包括“CREATE DATABASE 'cadvisor'”、“回车创建数据库”、“SHOW DATABASES”、“查看数据库”。
画面 10: 标题为“4.3.2 创建用户并授权”，内容包括“CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES”、“查看用户”、“用户授权”。
画面 11: 标题为“4.3.3 查看采集的数据”，内容包括“SHOW MEASUREMENTS”。
画面 13: 标题为“5.1 什么是cAdvisor”，内容包括对 cAdvisor 的介绍。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

