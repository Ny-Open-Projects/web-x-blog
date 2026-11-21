# 14-分布式事务解决方案Seata（应用_配置file.co — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢继续来看Sita的应用

刚才呢我们是通过Docker这种方式呢

把Sita的服务是不是已经跑起来了

并且呢我们提供了这么一个非常重要的文件啊

叫做registry.config

这个文件内容呢就从我们讲义上直接考过去就可以了

当然了你需要进行现行的修改

比如说什么呢

我们Sita呢启动完之后呢

需要注册到Narcos服务注册中心

所以需要在这儿来配置什么呢

Narcos相关的信息对吧

然后呢还有就是什么呢

配置中心

而这个配置中心的话呢

我们在这儿使用的是普通的文件这种类型

当然了你也可以使用Narcos对吧

这样的话呢你告诉他从Narcos在什么地方

他也就去拉取配置文件去了

这个地方呢我们使用的是file

所以这个地方呢我们就需要来给他提供这么一个文件

叫做file.config

这样的话呢他就会相当于就是使用这个文件

作为他的配置文件去读取

那这个文件的内容呢咱们来看一下

首先呢我们需要在

本地也就是在我们这个服务这儿

咱们在这儿呢先来退出一下

注意我们现在是不是在这个容器里边

在Sita Server里边

好退出来

退出来之后呢现在退到我们这个输入机

然后呢我们来看一下

咱们在这儿呢已经提供好了这么一个文件

file.config

这个文件内容呢就是讲以上这个内容

都是一模一样的

然后呢我们需要在这里边呢来进行相关的一些配置工作

你看这是service

对吧

服务

然后呢在这儿呢

注意

V

group mapping

前面这段是固定的

后边这一段是我们自己写的

叫做ithemartxgroup

好

注意这个名字啊

要前后一致

因为后边其他的地方也会用到这个名字

具体这个名字起什么名字

对吧

你写abc也可以写

写什么都可以

但是呢后边用到的地方呢

就需要跟在这儿指定的这个名字是保持一致的

它其实就是说

什么呢

相当于是一个虚拟的组

对不对

虚拟的组名

啊

后边呢我们在程序里边呢还会使用到这个名字

所以保持前后一致就可以

好

然后呢这个地方呢

注意看

Sdow

Sdow是不是代表的是存储

然后呢我们这个mood就是模式

对不对

等于db

db是不是就是数据库

大家还记得吧

我们刚才是不是创建了一个数据库

就是Ceta这个数据库

并且呢我们是不是创建了这么三张表

对不对哎

这些表呢是需要Ceta server来进行操作的

它需要来操作这些表

那我们就需要来告诉它

这些表在什么位置

对吧

所以说呢我们在这个地方呢

就需要来描述这个什么呢

db的信息

你注意看mood等于db

所以这块呢

file这种肯定就不用看了

我们直接看db这个

然后呢你看

DataSource等于Dreed

对吧

德鲁伊数据源

然后呢db type是mycircle

然后呢这是驱动名

然后呢db type是mycircle

然后呢注意最关键的就是这个URL

你看这是不是6879 7.219

端口2 3306

然后Ceta

你看我们当前这个数据库

是不是就在这个6879 7.219

然后呢我们这个数据库名

是不是就是Ceta

端口呢就是默认的3306

所以这样的话

这其实就是我们连接的字符串

对不对连接URL

这样的话呢Ceta server

它就能找到我们这个数据库了

当然了还需要用户名密码

然后下边呢

你看这是指定

我们三个表名

是不是分别是global table

branch table

还有lock table

那么这是关于我们数据库这块描述

这样的话Ceta server

就能够连接上这个数据库

来进行操作了

好

下面redis这个没有用到

所以就不用管它

然后呢

创建完这个文件之后呢

同样我们通需要通过Docker cp命令

把这个什么呢

把这个文件把它复制到我们

这个Ceta server当中去

放在哪呢

就是resources下边

file.config

所以呢你看啊

我们重新进到容器里面去

进来之后呢

ls你看这是不是有个resources

ls进来之后呢

是不是就有一个叫做file.config

哎这个文件呢

就是我们拷进来的

通过Docker cp命令拷进来

好

调整好之后呢

哎需要重启一下Ceta

其实就是什么呢

因为我们这是刚刚拷进来的这个文件

对吧

哎所以你最好重启一下

我这个呢

因为我提前

早就已经准备好了

我就不用重新启动了

好

所以重启完之后呢

我们可以到这个呃Nex当中去看一下Ceta服务是否注册成功

刚才也都看过了

对吧

他这都已经注册好了

这个就没问题了

那么到这儿的话呢

我们整个Ceta它的服务端哎

就是Ceta server这一段其实就已经完成了

剩下的就是什么呢

哎在我们的程序当中

我们就需要来引入什么呢

Ceta的依赖对不对

哎然后呢进行相关的配置

然后还有它的一些过滤器啊

拦截器需要去编写

好到这儿的话

Ceta server哎就完全搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”中第11章“分布式事务解决方案Seata”的教学内容，具体聚焦于**如何配置和启动Seata服务**。讲师通过演示在本地编辑配置文件、将配置文件复制到Docker容器内、重启服务以及引入Seata依赖等步骤，指导观众完成Seata服务的本地部署和集成。视频内容主要围绕Seata的配置文件（`registry.conf` 和 `file.conf`）进行讲解，涉及注册中心（Nacos、Consul、Eureka、Zookeeper、Etcd3）和事务日志存储（文件、数据库、Redis）的配置，并演示了如何在Spring Boot项目中引入Seata的依赖。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: **开场与课程概览**。讲师在Typora编辑器中展示课程大纲，明确本节内容为“4. 修改file.conf”。
*   **00:05 - 00:15**: **修改 `registry.conf` 文件**。讲师在Typora中展示 `registry.conf` 的配置内容，重点讲解了 `service`、`zk`、`consul`、`etcd3`、`sofa` 等模块的配置项，如 `serverAddr`、`cluster`、`timeout` 等。
*   **00:15 - 00:25**: **修改 `file.conf` 文件**。讲师切换到 `file.conf` 文件，讲解了 `service` 模块下的 `vgroupMapping` 和 `disableGlobalTransaction` 配置，以及 `store` 模块下的 `mode` 配置（默认为 `db`）。
*   **00:25 - 00:35**: **配置文件的存储模式**。讲师详细讲解了 `store` 模块下的 `mode` 配置，说明了 `file`、`db`、`redis` 三种模式的区别，并重点讲解了 `file` 模式下的 `file` 子模块配置，如 `dir`、`maxBranchSessionSize`、`maxGlobalSessionSize` 等。
*   **00:35 - 00:45**: **配置文件的存储模式（续）**。讲师继续讲解 `file` 模式下的配置，包括 `fileWriteBufferCacheSize`、`sessionReloadReadSize`、`flushDiskMode` 等。
*   **00:45 - 00:55**: **配置文件的存储模式（续）**。讲师讲解了 `db` 模式下的配置，包括 `db` 子模块下的 `host`、`port`、`database`、`password`、`maxConn`、`maxTotal` 等。
*   **00:55 - 01:05**: **将配置文件复制到容器中**。讲师在终端中执行 `docker cp file.conf seata:seata-server/resources/file.conf` 命令，将本地修改的配置文件复制到Docker容器内。
*   **01:05 - 01:15**: **重启Seata服务**。讲师在终端中执行 `docker restart seata` 命令，重启Seata服务。
*   **01:15 - 01:25**: **验证服务注册**。讲师在终端中执行 `curl http://127.0.0.1:8080/nacos/v1/ns/instance` 命令，验证Seata服务是否成功注册到Nacos。
*   **01:25 - 01:35**: **引入Seata依赖**。讲师在Typora中展示如何在 `pinda-tms-java/pom.xml` 和 `pd-common/pom.xml` 中添加Seata的依赖坐标，如 `io.seata:seata-spring-boot-starter:1.2.0`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **课程大纲**：在Typora中展示的课程大纲，包含“第11章 TMS司机端、快递员端开发”、“分布式事务解决方案Seata”、“4. 修改file.conf”等章节。
    *   **配置文件内容**：
        *   `registry.conf`：包含 `service`、`zk`、`consul`、`etcd3`、`sofa` 等模块的配置。
        *   `file.conf`：包含 `service`、`store`（`file` 和 `db`）模块的配置。
    *   **代码片段**：
        *   `registry.conf` 中的 `service` 模块配置：
            ```yaml
            service {
                vgroupMapping.ithema_tx_group = "default"
                # 当前值也需要在应用中添加 具体见 “7、增加seata配置” ithema_tx_group可修改
                disableGlobalTransaction = false
            }
            ```
        *   `file.conf` 中的 `store` 模块配置：
            ```yaml
            store {
                # store mode: file, db, redis
                mode = "db" # 使用数据库方式，需要修改db模块下的配置信息
            }
            ```
        *   `file.conf` 中的 `file` 子模块配置：
            ```yaml
            file {
                # store location dir
                dir = "sessionStore"
                # branch session size, if exceeded first try compress Lockkey, still exceeded throws exceptions
                maxBranchSessionSize = 16384
                # globe session size, if exceeded throws exceptions
                maxGlobalSessionSize = 512
                # file buffer size, if exceeded allocate new buffer
                fileWriteBufferCacheSize = 16384
                # when recover batch read size
                sessionReloadReadSize = 100
                # async, sync
                flushDiskMode = async
            }
            ```
        *   `file.conf` 中的 `db` 子模块配置：
            ```yaml
            db {
                # database store property
                host = "127.0.0.1"
                port = "6379"
                password = ""
                database = "0"
                minConn = 1
                maxConn = 10
                maxTotal = 100
                queryLimit = 100
            }
            ```
        *   **终端命令**：
            ```bash
            docker cp file.conf seata:seata-server/resources/file.conf
            docker restart seata
            ```

---

### 4) 关键场景与演示描述

*   **场景一：配置文件编辑与复制**。
    *   讲师在Typora中编辑 `file.conf` 文件，修改 `store` 模块的 `mode` 为 `db`。
    *   讲师在终端中执行 `docker cp file.conf seata:seata-server/resources/file.conf` 命令，将本地修改的配置文件复制到Docker容器内。
*   **场景二：服务重启与验证**。
    *   讲师在终端中执行 `docker restart seata` 命令，重启Seata服务。
    *   讲师在终端中执行 `curl http://127.0.0.1:8080/nacos/v1/ns/instance` 命令，验证Seata服务是否成功注册到Nacos。
*   **场景三：引入依赖**。
    *   讲师在Typora中展示如何在 `pinda-tms-java/pom.xml` 中添加Seata的依赖坐标。
    *   讲师在Typora中展示如何在 `pd-common/pom.xml` 中添加Seata的依赖坐标。

---

以上是根据您提供的视频画面进行的结构化技术分析。
