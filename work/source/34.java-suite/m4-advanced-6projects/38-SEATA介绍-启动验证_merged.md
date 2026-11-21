# 38-SEATA介绍-启动验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着开始实现SETA案例的服务启动与验证。

在启动服务之前,我们先要启动SETA手网,我们可以直接去下载它的运行包。

这个地址的话,不建议采用0.9以下的版本,我们最好就是采用0.9.0的这样一个版本。

我们下载到本地之后,要怎样去配置和运行呢?

我们打开它的服务目录。

在这里,我们进入Config目录。

Config目录下面有两个重要的文件,一个是File.config,一个是Register.config。

这个是不是跟我们工程当中这两个文件一致的,对不对?

一个File,一个是Register。

好,这个作用的话,在之前我们也已经给大家做了一个讲解,

让我们来看一下它具体的一些参数该怎么去修改。

打开File.config文件之后,我们要调整的地方,

其实就两三个地方。

首先的话,我们要去修改它的D4的Group List,也就是说你的IP和端口。

如果说你想对外进行暴露和访问,你最好要将它指向外网的IP,

然后给它分配一个具体的端口,这个是一个修改的地方。

那么如果说你在这里面的话,要采用数据库的方式。

默认的话,我们之前在工程当中,它是采用什么?

它是采用文件的方式,对不对?这个是客户端的一个默认方式。

那如果说你这个时候是采用SATA,建议的话,就要采用DB的这种模式。

因为SATA组件的话,你通过DB它才能够更好地去管理和控制。

这个是DB的一些基础性的配置。

我们可以看到在下面,DB的这个大括号在这里面列出了它所有相关的属性。

最主要我们要配置以下属性,像JRCLASS,就是你连接的是哪个数据源。

在这里,

它对那个MySQL有较好的支持。

其他数据源的话,不建议去采用。

这个就最好是采用MySQL。

然后是它的连接配置信息。

配置信息这一块要输入用户名和密码。

这个是它的数据库。

我们已经将这个数据库创建完成。

那如果说你首次并没有创建这个数据库,该怎么去执行呢?

我们可以打开它的安装包。

在下面的话,找到它的Config目录。

Config目录下面的话,给了你一个什么?

我们可以打开这个文件。

这个文件就初始化了SATA数据库的所有的表结构。

这个表结构具体是怎样的?

可以看到,这里主要有三张表。

一个是Global Table,这个是全局事务的管理表。

一个是Blanche Table,分支事务的管理表。

另外一个是它的一个锁的控制表。

好,主要就是这三个表,非常简单。

那么我们将这个数据库就已经创建完成。

一个是Blanche Table,Global Table。

还有一个是什么?

还有一个是Log Table。

在这里面的话,没有任何数据。

Global Table也没有任何数据。

然后Log Table,这里面都是空的。

这个SATA配置还有数据初始化完成之后,就可以进行运行。

我们将它关闭。

进入SATA的并目录。

然后直接执行BAT脚本。

我们直接打开。

因为我们在这里已经启动了一个。

对不对?

我们先把它关闭,然后再重新启动。

好,启动的时候一定要注意它最后输出。

SERVO START代表是启动成功。

好,这个就已经启动完成。

启动完成之后,接下来我们先不着急。

我们还要做什么事情呢?

我们还要去初始化业务数据库的脚本。

这个就是在我们的SATA案例下面,

ENITDB.CIRCLE。

我们将它COPY过来。

然后打开一个查询窗口,进行一个创建。

在这里它会去查找。

这个表是不是存在?

存在的话它就会删除。

这个我们可以完全重新运行一下。

执行完成。对不对?

这个时候又没有报错。

执行完成之后的话,我们可以看一下这个数据库。

在这里面的话就会有这三张表。

这两张表是我们整个DEMO整个SATA的案例当中所用到的业务数据表。

然后这个UNDO LOG是什么呢?

是SATA。

要做事务控制的一个表。

这个的话一定要给它处置化。

这里的话就是我们的一个提前准备工作。

准备完成之后,我们就可以启动服务做一个测试和验证。

怎么去测试呢?

启动完成之后,我们就要去访问它的接口。

然后去验证这个数据是否能够进行回滚。

同时的话,我们也跟踪一下它的一个异常日志输出。

看一下SATA这块是否能够真正生效。

我们先把服务启动一下。

找到SATA DEMO。

启动入口。

右键LONG运行。

启动完成。

我们可以看到在这里面的话,它已经连入SATA收货。

8091的这项端口。

然后放到这个事务组别的话,也是按我们定义好的事务组别进行连接。

服务启动完成之后,咱们接下来就可以做个调用和验证。

打开浏览器。

将我们的地址拷贝上去。

进行访问测试验证。

好,这个时候我们可以看到它抛出一个什么?

LONG TIME EXCESS.

然后这个异常的话,它说做了一个回滚。

将这个资产信息做了一个数据上的还原。

那我们来看一下。

在数据库这一块。

我们首先来看一下数据库它的一个实际情况。

然后TL3的。

大家再回过头来看一下整个代码的实现逻辑。

首先的话,它要去修改ASCEND这个表。

将它的状态改回2。

我们来看一下。

它的状态现在仍然是4。

那么我们对比初始化的数据库。

在这里面,初始化的数据轨大的值是多少呢?

往右边看。

它的初始化值是04。

也就是说,这个数据是进行了一个回滚的处理。

我们再看一下INCREASE。

INCREASE的话,它对ASCEND这个表做了一个数据处理。

它是数量上的、金额上的一个增加。

我们看一下实际情况。

TL3这个表。

金额的话,它仍然是1。

并没有做一个累加。

我们可以检查它的初始化数据。

初始化数据是TL3的这张表。

它的数量是1。

所以我们可以看到,本地事务它没有进行一个回滚操作。

因为的话,我们是通过切币方式,它必须要开启这个transaction的诸简。

如果说本地事务要回滚,必须要配置一个lowbackon这样一个属性。

上面章节当中也给大家做了一个讲解。

那么它怎么去进行回滚呢?

它正是通过Globe Transaction进行了一个全局分布式事务的回滚处理。

好,这样就实现了我们的分布式事务的一个管控。

那么验证的时候,我们再来看一下空置台的一个日子输出情况。

空置台的日子输出情况,我们是不是打印出了XID?

那么XID它具体是什么内容呢?

它其实很简单。

就是你的IP端口以及所分辨的内容。

它给了一个全局唯一的标记ID。

这个就是指向了什么?

CETA Server的端口。

然后给了一个什么?

给了一个全局的唯一标识。

在这里面我们可以看到,对吧?

Assign Service它的一个begin处理,

跟Assign Service begin的处理,它们的这个ID都是一样的。

这样我们就完成了数据上的一个验证以及日子上的一个验证。

从中的话测试出就是CETA Server的一个基层的话是OK,能够正常运转。

好,那这一讲咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于分布式事务解决方案 **Seata** 的实操教学课程，主要演示了如何在本地环境搭建 Seata Server、配置 Seata 客户端、执行数据库初始化脚本，并通过一个简单的“资产分配”业务场景来验证 Seata 的分布式事务回滚能力。课程的核心目标是让学习者理解 Seata 的工作原理，并掌握其在实际项目中的配置与使用方法。视频通过展示代码、配置文件、数据库操作和日志输出，完整地呈现了从环境搭建到功能验证的全过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：课程介绍与目标。讲师在文档中指出本节内容为“3.8 启动验证”，并说明本章目标是掌握 Seata 的工作原理和配置方法。
*   **00:00:15 - 00:00:30**：启动 Seata Server。讲师在文档中提示需要先启动 Seata-Server，并提供了下载链接。
*   **00:00:30 - 00:00:45**：数据库初始化。讲师展示了 `init_db.sql` 和 `db_store.sql` 文件，并在 Navicat 中验证了数据库表结构是否创建成功。
*   **00:00:45 - 00:01:00**：配置 Seata 客户端。讲师在 IntelliJ IDEA 中打开了项目，修改了 `application.yml` 文件，将事务模式设置为 `file`。
*   **00:01:00 - 00:01:15**：执行业务逻辑。讲师在代码中编写了 `increaseAmount` 方法，并在控制台中执行了该方法。
*   **00:01:15 - 00:01:30**：验证回滚结果。讲师在数据库中查询了 `asset_assign` 表，确认了事务回滚成功，`status` 字段值为 `04`。
*   **00:01:30 - 00:01:45**：课程总结。讲师在文档中总结了本章内容，强调了 Seata 的侵入性低、配置简单，并建议在实际应用中多查看服务日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3.8 启动验证`，`4. 总结`。
    *   **总结要点**：
        1.  重点掌握分布式事务解决方案，知道 Seata 的工作处理机制，如何解决分布式事务问题。
        2.  从服务设计中，通过多个服务的不同接口操作，来验证分布式事务的一致性，掌握 Seata 的整合配置，支持多种方式配置，根据实际情况结合应用场景。
        3.  Seata 侵入性低，接入使用比较简单，在实际应用中，如果出现问题，也要多查看 Seata Server 的服务运行日志。

*   **代码关键内容**：
    *   **Seata Server 配置文件 (`file.conf`)**：
        ```properties
        # transaction log store
        store {
          # store mode: file, db
          mode = "file"
          # file store
          file {
            dir = "sessionStore"
            # branch session size, if exceeded first try compress lockkey, still exceeded throws exceptions
            max-branch-session-size = 16384
            # globe session size, if exceeded throws exceptions
            max-global-session-size = 512
            # file buffer size, if exceeded allocate new buffer
            file-write-buffer-cache-size = 16384
            # when recover batch read size
            session-reload-read-size = 100
            # async, sync
            flush-disk-mode = async
          }
          # database store
          db {
            # the implement of java.sql.DataSource, such as DruidDataSource(druid)/BasicDataSource(dbcp) etc.
            datasource = "dbcp"
            # mysql/oracle/h2/oceanbase etc.
            db-type = "mysql"
            driver-class-name = "com.mysql.jdbc.Driver"
            jdbc-url = "jdbc:mysql://192.168.19.150:3306/seata"
            user = "root"
            password = "554321"
          }
        }
        ```
    *   **数据库初始化脚本 (`init_db.sql`)**：
        ```sql
        -- Table structure for undo_log
        DROP TABLE IF EXISTS `undo_log`;
        CREATE TABLE `undo_log` (
          `id` bigint(20) NOT NULL AUTO_INCREMENT,
          `branch_id` bigint(20) NOT NULL,
          `xid` varchar(100) NOT NULL,
          `rollback_info` longblob NOT NULL,
          `log_status` int(11) NOT NULL,
          `log_created` datetime NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        ```
    *   **业务代码 (`AssignServiceImpl.java`)**：
        ```java
        @Override
        @Transactional
        @GlobalTransactional
        public AssetAssign increaseAmount(String id) {
            LOGGER.info("Assign Service Begin ... xid: " + RootContext.getXID() + ", id: " + id);
            AssetAssign assetAssign = assignRepository.findByID(id).get(0);
            assetAssign.setStatus("2");
            assignRepository.save(assetAssign);
            // remote call asset service
            assetService.increase();
            return assetAssign;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境搭建与配置**
    *   **描述**：讲师首先在文档中强调了启动 Seata Server 的必要性，并展示了 `file.conf` 配置文件，其中详细说明了事务日志存储模式（`file`）和数据库连接信息（`mysql://192.168.19.150:3306/seata`）。
    *   **操作**：讲师在 IntelliJ IDEA 中打开项目，修改 `application.yml` 文件，将 `store.mode` 设置为 `file`，并配置了数据库连接信息。

*   **场景二：数据库初始化**
    *   **描述**：讲师在文件资源管理器中展示了 `init_db.sql` 和 `db_store.sql` 文件，并在 Navicat 数据库管理工具中执行了 SQL 脚本，成功创建了 `branch_table`、`global_table`、`lock_table`、`undo_log` 等核心表。
    *   **操作**：讲师在 Navicat 中连接到数据库 `seata`，并执行了 `init_db.sql` 脚本，验证了表结构。

*   **场景三：业务逻辑执行与回滚验证**
    *   **描述**：讲师在 IntelliJ IDEA 中编写了 `increaseAmount` 方法，该方法在事务中修改了 `asset_assign` 表的状态，并调用了远程服务 `assetService.increase()`。
    *   **操作**：讲师在控制台中执行了 `increaseAmount` 方法，触发了分布式事务。在日志中可以看到 `rollback status:Rollbacked`，表明事务回滚成功。
    *   **验证**：讲师在 Navicat 中查询了 `asset_assign` 表，确认了 `status` 字段的值为 `04`，证明事务回滚成功，资产数量未被修改。

*   **场景四：课程总结**
    *   **描述**：讲师在文档中总结了本章内容，强调了 Seata 的核心优势：侵入性低、配置简单、支持多种模式（文件、数据库）。
    *   **操作**：讲师在文档中列出了学习要点，包括掌握 Seata 的工作原理、通过服务接口验证事务一致性、以及在实际应用中多查看服务日志。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解本节课程内容。
