# 13-分布式事务解决方案Seata（应用_启动Seat — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢咱们继续来看我们SITA的应用

刚才呢我们是建立了数据库对吧

把SITA所需要的一些表呢给它创建出来了

那接下来呢我们在这个小节呢就来看一下

如何来启动SITA Server

它其实本身呢是一个服务对不对

它本身是一个服务

那么启动的话呢我们可以啊

有一种最简单的启动方式

就是基于Docker镜像这种方式来启动

那么我们启动一个容器就可以

好这呢我提前已经启动好了

咱们可以来看一下

首先呢我们需要来连接到数据库

连到我们这个服务器上来

然后呢我切换一下用户

获得root权限

然后呢我们可以来看一下Docker PS对吧

把它这样啊看得更清楚一点

好你看现在我们这个SITA服务呢

其实是已经跑起来了对吧

这是一个容器基于Docker来跑起来的

要启动的话呢

我们直接执行这个Docker run命令就可以了

即使你本地没有这个镜像的话也没有关系

因为你启动的时候呢它会检查

如果这个镜像没有

它就会给你去拉取

拉取完之后呢也就起来了

所以我们直接执行这个命令就可以啊

那么我启动呢也是执行的这个命令

这都是已经调整好了

Docker run是吧

杠D后台运行杠杠Name对吧

这是我们这个容器的名称就叫SITA

然后做了一个端口映射

因为这个端口呢是

8091这是它默认的端口

因为我们的SITA呢

它是不是分成很多角色对吧

包括我们的程序当中呢

是相当于是属于SITA的客户端

然后呢这个Server呢就相当于是服务端

它们之间呢是需要进行通信的

然后呢这个服务端呢就需要开放这么一个端口

是8091

所以我们在这呢做一个端口映射

然后呢这是不是就是我们那个镜像

镜像

然后呢现在下的是最新版本

LASTED

所以直接执行这个命令

命令就可以

现在呢我这个服务是已经跑起来了

已经跑起来了

就是这个SITA

那么跑起来之后呢

我们需要做一些配置

需要做一些配置

前面咱们也提到了

你看我们这个SITA呢

最终跑起来之后呢

需要把它注册到我们的服务注册中心

所以说呢我们接下来呢

就需要来做一些配置工作

这个配置工作呢

大家直接把我们这个文件

拷过去

然后呢

稍微修改一下就可以

你看这个是不是叫做

registry.config

这个文件

这个文件呢

其实就是用来配置什么呢

就是用来配置我们这个

服务注册中心的

说白了就是什么呢

就是将我们这个SITA服务

把它注册到我们注册中心里面去

那你要让它注册的话呢

那你得告诉它

我们这个注册中心用的是

NUCOS啊

还是用的是Eureka呀

对吧

那我们这个注册中心在什么位置呢

哎

我们这个注册中心呢

我们是不是需要通过这个文件去描述

需要通过这个文件去描述

好

所以呢

咱们需要在这个地方呢

来创建这么一个文件

其实我这已经创建好了

你看就是这个registry.config

好

咱们可以来看一下

这样看可能不太

不太好

那么我们直接看这边

然后呢

你看内容是一样的

然后呢

你看registry

这是描述我们注册中心

对吧

然后这个注册中心

type等于NUCOS

是不是

指定我们使用的是什么类型的注册中心

对吧

诶注册中心有很多呀

比如有这种NUCOS啊

Eureka呀

Redis啊

包括Zookeeper啊

Cancel啊

就是我们注册中心非常多

咱们当前使用的是NUCOS

对吧

使用的NUCOS

那这样的话呢

我们其实就看这段配置就可以

下面这些呢就不用了

像什么Eureka Redis ZK啊

这些咱们没有用

所以我们只要配这一段就可以

NUCOS

这其实就是描述我们当前服务的注册中心

在什么位置呢

在什么位置

诶

然后呢

注册的时候呢

我们这个Cita服务呢

就叫Cita Server

注册的时候叫这个名字

然后呢

这个描述的是什么呢

这是咱们这个NUCOS服务的地址

对吧

6879-6342

然后呢

端口号是8848

现在我这个服务呢

其实是已经跑起来了

这是我们NUCOS

重新登录一下

你看

从这能够看到服务列表

在当前这个地方

好

你看

你看

现在我们这个Cita Server

其实是已经跑起来了

对吧

就是因为它注册了

然后呢

我们也可以来验证一下

什么呢

首先呢

我们先退出来

退出一下

好

刚才有点问题

好

那么这已经退出来了

退出来之后呢

咱们可以怎么做呢

把我们这个Docker Stop Cita

把咱们这个容器呢

暂时暂停一下

好

稍等一下

它暂停的时候呢

稍微有一点点慢

好

已经停完了

停完了之后呢

我们到这边来看一下

重新查询一下这个服务列表

哎

你看是不是就没有了

然后呢

我重新再把它跑起来

通过什么呢

因为我这个容器呢

已经启动过了

所以再启的话呢

就不用Docker Run了

直接通过什么呢

Start对吧

然后Cita

好

这个跑起来了

跑起来之后呢

再来点查询

你看它是不是又注册进来了

好

这就说明啊

我们当前确实使用的是这个配置

对吧

然后

我们这个NUCLS起来之后呢

就会注册到我们这个NUCLS当中去

Cita起来之后呢

就会注册到这个地址

然后呢

它是这个group

是不是叫做Cita group

所以你看这个地方

这个分组名称是不是叫Cita group

然后呢

Namespace对吧

哎

你看这是结尾是什么3D9

这个你看这是不是我们当前这个空间

3D9这个空间

因为我们这个地方呢

是不是有好几个空间

好

咱们呢

在这个地方呢

要注册到这个空间里面来

好

然后下边这些呢

就是我们这个呃

用户名密码

对吧

这NUCLS用户名密码

那么对应的你配置好就可以了

这是服务之所中心

对吧

需要把这个文件给它配置好

配置好之后呢

注意

现在它跟我们的Cita还没有关系了

对不对

所以我们需要干什么呢

把咱们本地的这个文件呀

把它拷到哪去呢

把它拷到我们的这个呃

NUCLS这个容器当中去

一会儿呢

我们再看

怎么拷

咱们继续来看这个文件啊

因为这个文件其实内容还是挺多的

你看这是registry这个文件

下面这段呢

它其实描述的是什么呢

描述的是我们的这个呃

描述的是我们的呃注册中心

对吧

然后接下来还有一个config

这么一个配置

这个呢

就是用来指定我们的配置中心

用来指定我们的配置中心

因为呢

我们这个Cita呢

是有一些配置的

然后呢

我们这个配置的话呢

咱们这个type呢

使用的file这种类型

当然了

你也可以使用其他的啊

像什么这个NUCLS对吧

我们使用NUCLS作为配置中心

因为有些配置文件对吧

然后还有Abru啊

什么zk啊

cancel啊

等等这些

这个地方呢

我们使用的是file这种类型啊

那这个file这种类型

这个file在哪呢

诶

注意看type等于file

所以这些呢

你就不用看了

只看file这一项

name等于file.config

所以一会儿呢

我们需要给它提供这么一个文件

这个文件里边呢

就是关于一些配置信息啊

最终呢

Cita呢

会读取这个

相当于就是Cita服务的配置文件

对吧

它需要读取这些配置文件

好

那么整个这个文件其实非常大

对吧

你看

我们选中的这一块

内容非常多啊

这么多内容

然后呢

这就是我们这个registry.config文件

然后呢

我们可以把这个文件呢

把它复制到容器里面去

怎么复制呢

通过docker cp

然后呢

我们复制

这个文件呢

把它复制到这个服务里面去

对吧

现在呢

我已经复制完了

所以我们直接进入到Cita那个容器里面去就可以了

你看就是这个文件

把这个文件呢

复制进去

然后呢

我们就可以通过docker什么呢

exec对吧

然后呢

进到

我们这个

gambash

然后进到Cita里边来

这个地方呢

需要先写Cita

好

Cita

然后呢

gambash

注意看

现在呢

我是不是已经进到了Cita服务里面来了

进来之后呢

我们ls来看一下

这里边是不是有一个叫做resources

因为我们刚才呢

通过docker cp呢

你看是不是考到它这个resources下面去了

所以我们直接进到这个resources目录里边来

然后这里边呢

是不是就有一个叫做registry.config

这个文件怎么来的呢

其实就是我们从外边

这个文件

是不是给它通过docker cp命令

考到容器里面来的

然后呢

我们可以来看一下

直接通过cat来看一下就可以了

你看

这就是我们这个文件的内容

对吧

都是一样的

这是文件内容

所以大家呢

也按照我们讲义上来操作一下

就可以了

具体这里边这些配置项呢

其实不需要去

我们去手动去敲

对吧

这个没有什么意义啊

你只要知道我们这个配置项

它的含义

它是在配置什么样的信息

然后会进行相应的修改

就可以了

好

这是咱们这一步

也就是我们启动服务

同时呢

修改registry

这个config这个文件

但是大家不要忘了

咱们一会儿呢

是不是还需要去创建一个叫做

file.config这个文件

因为这个呢

是Cita服务

它的配置文件

对不对

因为我们当前这个配置中心

使用的就是file这种类型

所以一会儿呢

我们需要创建这个文件

它启动的时候呢

需要读取这个文件

好

那么关于我们这个应用呢

我们先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”第11章“分布式事务解决方案Seata”的教学内容，主要演示了如何在本地环境中搭建和配置Seata分布式事务管理器。视频内容按步骤进行，首先创建了Seata所需的数据库表结构，然后通过Docker启动了Seata服务，并详细讲解了如何修改Seata的配置文件（`registry.conf` 和 `file.conf`），使其能够与Nacos服务注册中心、Redis、Zookeeper、Consul、Apollo等配置中心进行集成。整个过程旨在为后续的分布式事务功能开发提供一个完整的、可运行的本地开发环境。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的播放时间点，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**：开场，展示课程大纲，介绍本章主题“分布式事务解决方案Seata”。
*   **00:05 - 00:15**：**章节一：建立数据库**。演示在MySQL中创建 `global_table` 和 `branch_table` 两个核心表，用于存储全局事务和分支事务信息。
*   **00:15 - 00:25**：**章节二：启动Seata Server**。在终端中使用Docker命令启动Seata服务容器。
*   **00:25 - 00:35**：**章节三：修改registry.conf**。展示如何编辑Seata的配置文件，将注册中心从默认的Eureka改为Nacos，并配置Nacos的地址和命名空间。
*   **00:35 - 00:45**：**章节四：修改file.conf**。展示如何配置Seata的配置中心，包括Nacos、Consul、Apollo和Etcd3，并将配置文件复制到Seata容器内。
*   **00:45 - 00:55**：**章节五：重启服务**。在终端中执行命令，重启Seata服务以使新配置生效。
*   **00:55 - 01:05**：**章节六：验证配置**。在Nacos控制台中查看服务列表，确认Seata服务已成功注册。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程大纲：清晰列出了本章的各个小节，包括“建立数据库”、“修改registry.conf”、“修改file.conf”等。
    *   配置文件结构：详细展示了 `registry.conf` 和 `file.conf` 的配置项，如 `type`, `serverAddr`, `group`, `username`, `password` 等。

*   **代码 / SQL**：
    *   **创建数据库表**：
        ```sql
        -- 创建全局事务表
        CREATE TABLE `global_table` (
            xid varchar(128) NOT NULL,
            transaction_id bigint(20) DEFAULT NULL,
            status tinyint(4) NOT NULL,
            application_id varchar(32) DEFAULT NULL,
            transaction_service_group varchar(32) DEFAULT NULL,
            transaction_name varchar(128) DEFAULT NULL,
            timeout int(11) DEFAULT NULL,
            begin_time bigint(20) DEFAULT NULL,
            application_data varchar(2000) DEFAULT NULL,
            gmt_create datetime DEFAULT NULL,
            gmt_modified datetime DEFAULT NULL,
            PRIMARY KEY (`xid`),
            KEY `idx_gmt_modified_status` (`gmt_modified`, `status`),
            KEY `idx_transaction_id` (`transaction_id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

        -- 创建分支事务表
        CREATE TABLE `branch_table` (
            branch_id bigint(20) NOT NULL,
            xid varchar(128) NOT NULL,
            transaction_id bigint(20) NOT NULL,
            resource_group varchar(32) DEFAULT NULL,
            resource_id varchar(256) DEFAULT NULL,
            branch_type varchar(32) DEFAULT NULL,
            status tinyint(4) NOT NULL,
            client_id varchar(64) DEFAULT NULL,
            gmt_create datetime NOT NULL,
            gmt_modified datetime NOT NULL,
            PRIMARY KEY (`branch_id`),
            KEY `idx_xid` (`xid`),
            KEY `idx_status` (`status`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        ```

    *   **Docker 启动命令**：
        ```bash
        docker run -d --name seata -p 8091:8091 seataio/seata-server:latest
        ```

    *   **配置文件 `registry.conf`**：
        ```properties
        registry {
            # file, nacos, eureka, redis, zk, consul, etcd3, sofa
            type = "nacos"
            # 注册中心使用nacos方式
            loadBalance = "RandomLoadBalance"
            loadBalanceVirtualNodes = 10
        }

        nacos {
            application = "seata-server"
            serverAddr = "68.79.63.42:8848"
            group = "SEATA_GROUP"
            cluster = "default"
            username = "nacos"
            password = "itheima123"
        }
        ```

    *   **配置文件 `file.conf`**：
        ```properties
        config {
            # file, nacos, apollo, zk, consul, etcd3
            type = "file"
            # 配置信息采用file方式
        }

        nacos {
            serverAddr = "127.0.0.1:8848"
            namespace = ""
            group = "SEATA_GROUP"
            username = ""
            password = ""
        }

        consul {
            serverAddr = "127.0.0.1:8500"
        }

        apollo {
            appID = "seata-server"
            apolloMeta = "http://192.168.1.204:8801"
            namespace = "application"
            apolloAccessKeySecret = ""
        }

        zk {
            serverAddr = "127.0.0.1:2181"
            sessionTimeout = 6000
            connectTimeout = 2000
            username = ""
            password = ""
        }

        etcd3 {
            serverAddr = "http://localhost:2379"
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库初始化**：讲师在Typora文档中展示并讲解了创建 `global_table` 和 `branch_table` 的SQL语句，强调了这些表在Seata事务管理中的核心作用。
*   **场景二：Docker环境搭建**：在终端中，讲师执行 `docker ps` 命令，查看已运行的容器，确认了Nacos、MySQL、Redis等服务的正常运行，为后续操作提供了环境保障。
*   **场景三：配置文件修改**：讲师在Typora中逐行修改 `registry.conf` 文件，将注册中心类型从Eureka改为Nacos，并配置了Nacos的服务器地址和命名空间。随后，他展示了如何修改 `file.conf` 文件，配置了多种配置中心的地址。
*   **场景四：配置文件复制**：讲师在终端中使用 `docker cp` 命令，将本地修改好的 `registry.conf` 文件复制到正在运行的Seata容器内，确保配置生效。
*   **场景五：服务注册验证**：讲师切换到Nacos控制台，查看服务列表，确认Seata服务已成功注册到Nacos，表明整个配置流程成功完成。

---
