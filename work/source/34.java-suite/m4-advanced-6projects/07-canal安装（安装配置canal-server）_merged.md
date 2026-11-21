# 07-canal安装（安装配置canal-server） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们Kander的安装

刚才我们是把MySQL容器已经跑起来了

并且也进行了相应的配置

那接下来我们按照顺序来创建什么呢

Kander Server,这是我们Kander Server

这儿我们还是使用Docker容器这种方式

还是比较简单的,直接执行Docker Run来启动就可以了

那么这个镜像叫做Kander-Server

版本号就是这个版本号

同样还是我们不用自己去拉取镜像

如果本地没有镜像,它会自动来拉取

然后我们可以看到咱们做了一个端口映射

那么Kander Server它默认的端口

启动之后默认的端口就是这个五个一

那么我们映射使用本地也是五个一来映射就可以了

然后启动完之后咱们容器的名称就叫Kander-Server

接下来我们把这个命令复制一下

到这边来

咱们把命令粘贴到这个位置

然后回车

你看它还是按F2,Find Image

然后我们再按F2,Find Image

在我们本地是没有镜像的

所以说它需要去下载镜像

下载完之后再把我们这个容器启动起来

它这个镜像下载是稍微有点慢

那么它现在正在下载

稍等一下

它这个镜像还是比较大的

几百兆

那么启动容器还是非常快的

只要拉取完镜像之后

启动容器瞬间就可以跑起来

那么现在我们这个容器已经起来了

咱们来看一下

咱们刚才那个容器是不是叫做CAN-Server

然后我们做了这个端口映射

这样的话我们这个CAN-Server就已经跑起来了

跑起来之后

咱们需要进入到容器当中来进行一个配置

首先我们先进到这个容器里面去

还是通过Docker EXEC

这个命令

然后进来

现在我们已经进到容器里面来了

注意看这边是不是已经发生了变化

进到容器里面来之后

我们需要来修改这个文件

叫做Docker EXEC

叫做instance.properties

它在哪呢

在我们这个CAN-server

然后什么config下边

咱们来看一下

CAN-server

你看这是不是有个CAN-server

然后是不是有一个叫做config

对吧

好

然后里边是不是有一个叫做什么呢

example

example

example

好

然后这里边是不是有一个叫做instance.properties

对吧

好

那么现在我们要改的就是这个文件

要改的就是这个文件

instance.properties

然后咱们直接通过vi命令来改一下就可以了

vi instance.properties

进来

进来之后

注意看我们改哪些地方

一个是这个canner instance mycircle.slaveid

这个id的话

其实只要是唯一的就可以

只要是唯一的就可以

你看我们这写了个12

对吧

好

这个地方咱们来改一下

来看

叫做canner instance mycircle.slaveid

就是这个

那么输入一个i

进入这个编辑模式

然后把它这个井号

井号是注释对吧

给它去掉

然后这个slaveid咱们就给它改成12

跟我们讲义保持一致

好

然后还要改哪一项呢

是这个position

什么info这个位置

就是下边这个地方

然后这个是指定我们这个mycircle master

对吧

它的这个地址

你看

这是不是master.address

master.address

这个地址的话呢

我们需要来改一下

好

这个地址的话呢

咱们就改成我们的这个公 IP

也就是68

然后79

然后是6342

对吧

端口呢就是3306

这个就不用改了

好

然后还有哪个地方要改呢

就是下边这个

我们刚才是不是创建了一个账号

对吧

叫做canner

好

现在呢就是要改它

在哪呢

在这儿

正好呢

它默认其实就是这个

那我们就不用改了

好

如果不一致呢

你需要给它改一下

大家看我这个都已经标红啊

都标出来了

好

这不是username password吗

对吧

好

这username password

这个地方呢

跟我们刚才设置的是一致的

那这个地方就不用动了

好

那么就只要改这么几个地方就可以啊

其他的都不用动

好

然后ESA

冒号wq

好

保存退出一下

这样的话呢

我们这个配置就已经搞定了

对吧

配置搞定了

搞定之后呢

咱们来重启一下我们这个canner server

好

然后呢

重启完之后呢

重新进来查看它的日志

好

要重启的话呢

我们先来退出一下

退出容器

注意看我们现在又回到了宿主机

对吧

然后呢

我们来执行什么呢

restart

docker restart

那就直接复制了

好

把我们刚才这个容器重启一下

好

重启之后呢

咱们重新进到容器里面去

这要进来了

又重新进来了

进来之后呢

我们干什么呢

来查看一下它的这个日志啊

这个

动态查看对吧

tel-100f

查看最后100行数据就可以了

然后呢

这个日志的话呢

就是在这个canner server logs

这个目录下边

好

那么大家可以看到我们这个地方

其实已经能够看到这个什么

destination目的地对吧

能够能够看到这儿

这就说明我们刚才那个配置的目的地

配置呢是已经生效了

已经生效了

到这儿的话呢

我们这个canner server就已经配置好了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析。

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”第6章“数据聚合服务开发”的技术教程，核心内容是**如何在Docker环境中安装、配置并使用Canal Server来实现MySQL数据库的增量数据同步**。讲师通过分步演示，展示了如何拉取Canal镜像、启动容器、修改配置文件（`instance.properties`）、重启服务，并最终通过Navicat客户端验证数据同步功能。整个过程强调了配置文件的修改和容器操作的正确性。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中的具体时间点，以下章节划分是基于画面内容和逻辑顺序进行的：

*   **00:00 - 00:05**: **课程介绍与目标**。画面显示了课程大纲，明确指出本节内容为“1.5 canal安装”。
*   **00:05 - 00:15**: **环境准备与镜像拉取**。讲师在终端中执行 `docker pull canal/canal-server:v1.1.4` 命令，演示了如何从Docker Hub拉取Canal Server的镜像。
*   **00:15 - 00:30**: **启动Canal Server容器**。讲师使用 `docker run -d --name canal-server ...` 命令启动容器，并在终端中查看了镜像拉取和容器启动的输出日志。
*   **00:30 - 00:45**: **配置文件修改**。讲师切换到容器内部，使用 `vi` 编辑器打开配置文件 `conf/example/instance.properties`，并重点修改了 `canal.instance.master.address` 和 `canal.instance.dbUsername`、`canal.instance.dbPassword` 等关键参数。
*   **00:45 - 01:00**: **重启容器并查看日志**。讲师执行 `docker restart canal-server` 命令重启容器，并使用 `tail -100f canal-server/logs/example/example.log` 命令实时查看日志，以确认服务是否正常启动。
*   **01:00 - 01:15**: **创建测试数据库与表**。讲师在Navicat客户端中创建了名为 `student` 的数据库和表，用于后续的数据同步测试。
*   **01:15 - 01:30**: **演示数据同步**。讲师在Navicat中向 `student` 表中插入数据，并通过查看Canal的日志来验证数据是否被成功捕获和同步。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   课程大纲：清晰列出了“1.1 背景”、“1.2 工作原理”、“1.3 架构”、“1.4 HA机制设计”、“1.5 canal安装”、“1.6 简单使用”等章节。
    *   关键步骤说明：如“# 按Ctrl+D退出容器，并重启容器”、“# 重启成功后进入容器”、“# 查看日志”等操作指令。
    *   代码片段：在PPT中展示了 `CREATE TABLE 'student' (...)` 的SQL语句。

*   **代码/配置文件内容**:
    *   **MySQL权限授权**（在PPT中展示）：
        ```sql
        GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal1'@'%';
        FLUSH PRIVILEGES;
        ```
    *   **Docker启动命令**：
        ```bash
        docker run -d --name canal-server -p 11111:11111 canal/canal-server:v1.1.4
        ```
    *   **进入容器并修改配置**：
        ```bash
        docker exec -it canal-server /bin/bash
        vi canal-server/conf/example/instance.properties
        ```
    *   **关键配置项（在 `instance.properties` 文件中）**：
        ```properties
        # position info
        canal.instance.master.address = 127.0.0.1:3306
        # rds oss binlog
        canal.instance.rds.accesskey =
        canal.instance.rds.secretkey =
        # table meta tsdb info
        canal.instance.tsdb.enable=true
        # canal.instance.tsdb.url=jdbc:mysql://127.0.0.1:3306/canal_tsdb
        # canal.instance.tsdb.dbname=canal_tsdb
        # username/password
        canal.instance.dbUsername=canal
        canal.instance.dbPassword=canal
        # enable druid decrypt database password
        canal.instance.enableDruidDecrypt=true
        ```
    *   **重启与查看日志命令**：
        ```bash
        docker restart canal-server
        docker exec -it canal-server /bin/bash
        tail -100f canal-server/logs/example/example.log
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与镜像拉取**。讲师在终端中执行 `docker pull canal/canal-server:v1.1.4`，并展示了镜像拉取成功的日志，确认了环境准备就绪。
*   **场景二：配置文件修改**。讲师在容器内使用 `vi` 编辑器打开 `instance.properties` 文件，重点修改了 `canal.instance.master.address` 为 `127.0.0.1:3306`，并设置了数据库用户名和密码。此操作是配置Canal连接目标MySQL数据库的关键步骤。
*   **场景三：重启服务与日志监控**。讲师执行 `docker restart canal-server` 命令后，立即使用 `tail -100f ...` 命令查看日志，确保Canal Server成功启动并开始监听数据库的Binlog。
*   **场景四：数据同步验证**。讲师在Navicat客户端中创建了 `student` 表，并插入了测试数据。通过查看Canal的日志，确认了数据变更事件已被成功捕获，从而验证了Canal的数据同步功能。

---

以上是根据您提供的视频画面进行的结构化分析。
