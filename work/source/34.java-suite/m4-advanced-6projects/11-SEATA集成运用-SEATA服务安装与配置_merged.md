# 11-SEATA集成运用-SEATA服务安装与配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接下来咱们开始去讲解SETA的服务端安装和配置

在前面章节当中,我们讲过分布式事务SETA的使用

它的前身名称是叫FastCard

后面改名叫做SETA

这里我们就讲解具体如何去运用到实际项目当中

SETA之前的版本是存在一些问题的

这里我们建议大家采用0.9.0的版本

不要最新的,也不要太过成就的版本

因为咱们也是测试过好几个版本

发现0.9.0相对会比较稳定一点

那我们就采用0.9.0在项目当中去集成使用

那首先我们要将SETA服务安装和配置好

这里提供了SETA Server 0.9.0版本的下载地址

大家将SETA Server服务端下载到本地之后

我们接着就去修改它的配置

在这里我已经将SETA生网下载并且解压到本地

版本是0.9.0

我们进入Config目录去修改它的配置

我们在这里采用的是File模式

需要去修改File.config文件

将它打开

这里面是SETA的具体配置

我们要修改三个地方

第一个地方将它的模式改成DB

也就是Store里面的Model改成DB模式

因为我们要连接到数据库当中

数据库的事物日日存储相对会比较稳定一点

然后要

去修改DB的连接配置属性

我们可以看到这里面是DB的连接配置信息

我们采用的是MySQL的连接

这里是它的驱动内

然后是Ui的连接字符算信息

下面是账户名和密码信息

最后还去修改Lock的模式

这里面的所有的运用模式也是采用DB方式去做操作

将Mode设置为DB

Db就可以

Ceta配置信息修改完成之后

接下来就要去初始化数据库的脚本

这些脚本是在肯菲格目录下面

可以看到DB Store还有DB Undo Log

DB Store里面是包含Ceta数据库里面的三张表信息

一张是Global Table

然后是Branch Table以及Lock Table

DB Undo Log里面是一张表

我们可以看一下

这个就是Undo Log的日志表记录

将这两个日志表记录放在Db Undo Log里面是一张表我们可以看一下这个就是Undo Log的日志表记录

我们可以看一下这个就是Undo Log的日志表记录

这里要创建一个Ceta的数据库

适用于Ceta Server服务端的连接

将肯菲格目录下面的DB Store的脚本

要初始化到Ceta Server的数据库下面

这里我们已经初始化进去了

就不再重复执行

然后要再应用到Ceta Server的业务数据库里面去初始化Undo Log表

对应的就是DB Undo Log.Circle的脚本文件

大家在对脚本进行初始化的时候要注意一下

如果在使用Ceta Server的时候出现以下错误提示

那么需要将它的脚本里面的字段长度做一个调整

将Global Table表里面的Transaction Name字段调整为2048

Flanche Table里面Log Key的字段也调整为Virtual 2048

这个是因为Ceta Server还在不断的完善

会存在一些bug和小问题

以上配置完成之后

我们就可以切换

我们可以启动Ceta Server

这个是它的运行脚本

这个脚本是在Ceta Server目录下面的B目录下

如果是Windows执行BAT脚本

如果是Linux执行SH脚本

咱们看一下Ceta Server的运行结果

出现以下提示

Sever Started

说明了Ceta Server已经成功启动

好

这一讲咱们就完成了Ceta Server服务端的安装和配置

那这一讲的内容

咱们就先讲到这里

谢谢观看

下期再见

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于分布式事务解决方案 **Seata**（前身为 Fescar）的入门教程，具体聚焦于 **Seata 服务端的安装与配置**。讲师通过演示如何将 Seata 服务端从文件模式（file）切换为数据库模式（db），并配合数据库脚本初始化所需表结构，来完成服务端的部署。视频中也提及了 Seata 当前版本存在的已知问题，并展示了服务启动后的日志输出，旨在为后续的分布式事务集成打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: **课程引入与目标**。讲师在 Markdown 文档中指出，本节将讲解如何在实际项目中集成 Seata 服务端，并明确采用 `v0.9.0` 版本。
*   **00:05 - 00:15**: **服务端安装配置**。讲师开始讲解 `3.1 SEATA服务端安装配置` 章节，首先介绍如何下载 `Seata Server 0.9.0`。
*   **00:15 - 00:25**: **修改配置文件**。讲师指出默认配置为文件模式，需要修改 `conf` 目录下的 `file.conf` 文件，将其改为数据库模式。
*   **00:25 - 00:35**: **配置文件修改演示**。讲师在代码编辑器中展示如何将 `store` 配置块中的 `mode` 从 `file` 改为 `db`。
*   **00:35 - 00:45**: **数据库初始化**。讲师讲解了需要创建 `seata` 数据库，并导入 `conf` 目录下的 `db_store.sql` 脚本以生成 `branch_table`, `global_table`, `lock_table` 三张核心表。
*   **00:45 - 00:55**: **处理潜在错误**。讲师提示在使用 `db_store.sql` 脚本时，可能需要调整 `branch_table` 的 `lock_key` 字段长度，以避免因数据过长导致的 `TransactionException`。
*   **00:55 - 01:05**: **启动服务**。讲师演示了如何通过双击 `seata-server.bat` 文件来启动服务，并在控制台中查看服务启动日志。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.1 SEATA服务端安装配置`
    *   **关键步骤**:
        1.  下载 Seata Server 0.9.0。
        2.  修改配置：将 `store.mode` 从 `file` 改为 `db`。
        3.  初始化数据库：导入 `db_store.sql` 脚本。
        4.  启动服务。
    *   **注意事项**: 提及 Seata 仍处于完善阶段，存在小问题，并提示了 `db_store.sql` 脚本中可能需要调整的字段长度。

*   **代码 / 配置文件内容**:
    *   **`file.conf` 文件片段**:
        ```properties
        # transaction log store
        store {
            # store mode: file, db
            mode = "db"
            ...
        }
        ```
    *   **`db_store.sql` 脚本**:
        *   用于创建 `seata` 数据库。
        *   用于生成 `branch_table`, `global_table`, `lock_table` 三张表。
    *   **`db_undo_log.sql` 脚本**:
        *   用于在需要纳入分布式事务的数据库中初始化 `undo_log` 表。

---

### 4) 关键场景与演示描述

*   **场景一：配置文件修改**
    *   **描述**: 讲师在 `Sublime Text` 编辑器中打开 `seata-server-0.9.0/conf/file.conf` 文件。
    *   **操作**: 使用鼠标选中并修改 `mode` 的值，将 `mode = "file"` 改为 `mode = "db"`。
    *   **目的**: 将 Seata 服务端的事务日志存储模式从文件模式切换为数据库模式。

*   **场景二：数据库初始化**
    *   **描述**: 讲师在 `Navicat Premium` 数据库管理工具中，连接到本地 MySQL 数据库。
    *   **操作**: 在 `seata` 数据库中执行 `db_store.sql` 脚本。
    *   **结果**: 成功创建了 `branch_table`, `global_table`, `lock_table` 三张表，如图所示。
    *   **后续操作**: 讲师提示，如果需要在其他数据库中使用 Seata，还需执行 `db_undo_log.sql` 脚本以创建 `undo_log` 表。

*   **场景三：服务启动与日志**
    *   **描述**: 讲师在桌面双击 `seata-server.bat` 文件。
    *   **操作**: 启动服务。
    *   **结果**: 在弹出的黑色控制台窗口中，可以看到 Seata 服务启动的日志信息，包括配置加载、数据源初始化等过程，表明服务已成功启动。

*   **场景四：错误处理提示**
    *   **描述**: 讲师在 PPT 中展示了一个可能的错误信息。
    *   **内容**: `io.seata.core.exception.TransactionException: RuntimeException [Data truncation: Data too long for column 'transaction_name' at row 1]`
    *   **解决方案**: 讲师提示，如果出现此错误，需要将 `db_store.sql` 脚本中 `branch_table` 的 `lock_key` 字段长度从默认值改为 `varchar(2048)`。

---

以上是根据视频画面整理出的结构化技术课程分析。
