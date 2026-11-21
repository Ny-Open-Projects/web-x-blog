# 06-文件服务课程-文件服务开发（环境搭建_数据 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来来看咱们课程的第五章

第五章我们要进入的是文件服务的开发

当然了在真正文件服务代码开发之前

我们有一些环境是需要去搭建的

也就是说我们首先来看环境搭建

在环境搭建这儿

我们会通过从这四个方面来进行环境搭建

一个是我们的数据库环境搭建

还有就是我们NUCOS环境搭建

因为我们这个项目它是基于NUCOS

作为我们服务的配置中心

也就是说统一在NUCOS当中来管理我们的配置文件

那么我们需要提前把这个环境把它搭建起来

然后第三个就是我们NGX环境搭建

前面我们也提到过了

如果说我们使用的存储策略是本地存储

那这个时候我们就会通过NGX给我们提供的HTTP功能

然后对外提供下载

对吧

文件的下载

所以说我们也需要把NGX环境搭建起来

最后就是关于我们Maven工厂环境的搭建

那么按照顺序

咱们先来看第一个

就是我们数据库环境的搭建

首先我们可以来创建一个数据库

这个数据库的名字叫做pd-files

咱们可以通过Corey的database

这个circle语句来创建

当然了我们也可以直接通过我们的图形工具

图形界面来创建

这都可以

好

那么我们先来看看

现在我的MySQL服务是已经启动了

然后我们直接连接到本地

那么在开发阶段

咱们尽量就使用本地的环境就可以

然后我们在这new一个database

然后把这个编码

我们可以来指定一下

UTF-8 MB4这种

这个就选第一个就可以

这样的话

我们是不是就创建出来了这么一个数据库

叫做pd-files

然后在这个数据库里面

来创建我们文件服务

相关的表

那么文件服务相关的表

其实只有两张

一个叫做什么

一个叫做pd-attachment

这个其实是我们的附件表

然后还有一个叫做pd-files

这个就是我们文件表

这个地方我们为什么要提供两张表

前面我们其实也提到过了

就是在我们第二个章节

核心功能这儿

我们也提到过了

咱们这个文件服务

它提供的服务

有两种类型

两种类型的服务

一种是面向应用系统的

这种通用的附件服务

这个时候我们附件服务

它把文件上传完成之后

我们需要把文件相关的一些信息

把它记录到我们的数据库里面去

那么具体就会记录到咱们附件表里面

附件表就是pd-attachment

然后第二类服务

就是pd-attachment

面对用户的这种网盘服务

这个时候我们会把上传的文件信息

记录到我们pdfile这个表里面

所以我们回到这边来

这就是我们刚才提到的这两张表

一个叫做pd-attachment

这是附件表

还有一个叫做pdfile

这是我们网盘的数据表

文件表

这两张表其实因为都是用来存储上传的文件信息的

所以说它这里边有很多的文件信息

很多字段其实是重复的

那么我们可以通过下边这个件表语句

把我们这两张表创建出来

这是两个件表语句

然后我们整个复制一下就可以了

咱们直接把这个circle语句复制一下

然后到我们这边

在这个命令窗口里面来

执行一下就可以了

执行之后咱们直接在这儿刷新一下

就能看到我们这两张表了

对吧

然后呢

我们可以先看这个第一个PD

attachment

这个呢是我们的附件这张表

表里面的字段呢

还是比较多的

大家可以看一下ID

这就不用说了

这是主件对吧

然后呢还有个是BIZ ID

这个是业务ID

因为什么呢

我们当前提供的这个附件服务啊

它是一个通用的服务

也就是说啊

可能有很多系统呢

不同的系统都会去调用我们这个服务

暴露出来的接口

来进行文件的上传

下载这些操作对吧

那这个时候呢

我们如何区分

那么这我们记录的这条数据

它到底是哪个业务系统相关的数据呢

所以我们在这个地方呢

会通过一个BIZ ID

就是业务ID来区分

还有呢一个叫做业务类型对吧

业务类型业务ID

这个呢都是跟这个第三方

这个业务系统啊相关的

然后呢还有一个是Data Type

这个就是指定什么呢

我们当前这个

上传的这个文件

它的类型是一个图片呢

还是一个视频呢

还是一个什么样的文件等等

什么格式的对吧

然后呢这个叫做数据类型

然后这个Submitted File Name

这个是什么呢

这个从字面来看的话

这是不是就是提交的文件名

其实就是我们上传的那个文件

它的原始文件名

原始文件名

然后呢包括这个Group啊

这个Path呢

这个呢是我们这个平常的这个

通常情况下是没有用的

只是在我们Fast DFS

如果我们选择的是这种存储方式的情况下

才会使用到它

Group还有Path

然后呢还有这个什么相对路径对吧

相对路径

还有这个是完整的一个URL

因为我们要去下载一个文件

我们必须知道它的这个完整的URL

还有这个File MD5

这个呢我们可以把这个文件整个进行MD5

进行这个哈希

然后呢来得到一个MD5值

然后呢这个呢这个呢我们可以把这个文件整个进行MD5进行这个哈希

这个呢是我们这个上传的文件

它的类型对吧

Context Type

然后还有File Name

注意这个File Name呢

这不是原始的文件名了

这个就是我们经过这个

一般是随机给它生成一个文件名

比如我们使用UID对吧

防止我们这个文件名重复

所以说呢我们可以给它来生成

这个随机的一个文件名

然后呢EXT

这个就是我们上传的文件

它的后缀

然后呢这个是Size对吧

这个就是文件的大小

再往下呢

ORG ID

这个就是组织ID

当然这些呢是一些扩展的字段啊

比如说我们这个当前上传的这个文件

它属于哪个组织下边

这些字段呢都是可选的

那么根据我们的情况来填就可以了

那么如果需要的话呢

你就把这个参数给我们传过来

然后就可以

还有呢这个对应的就是一个图标

一个图标

下边这些呢其实都是什么

创建的月份

创建的这个日期对吧

创建的日期

创建的时间

创建人

创建的时间

更新时间

更新人等等这些

这是咱们这个复建这张表

然后呢我们再来看

另外一张就是PDFile这张表

这张表里面的字段呢也是比较多的

也是比较多的

然后呢我们来看一下ID

这不用说了

Data Type跟前面已经说过了

就是我们上传的文件

它的类型对吧

是一个什么样的类型

是图片还是视频

还是文件夹等等啊

然后呢还有Submitted File Name对吧

这个是原始文件名

还有Tripath

因为呢我们这里边有文件夹的概念

对吧

所以说呢它就会有这种目录层次

所以这个是描述这个目录层次的

Grid呢这个

这个其实也是目录层次

表示的是什么呢

它是第几级目录

它是第几级

因为我们目录层次很深

所以说通过它呢可以去描述

然后Ease Delete

这其实就是一个逻辑字段对吧

标识是否删除了

还有Fold ID

这是文件夹的ID

还有这是文件的这个URL

地址啊

完整的路径

这是文件的大小

然后Folder Name

这是文件夹的名称

包括Group还有Path

前面已经提到过了

只有我们Fast DFS啊

这种存储方式的时候呢

才会用到它

然后呢这是文件的它的相对路径

这个呢还是File MD5对吧

对整个文件进行MD5计算

然后呢还有Contact Path

这是文件的类型

File Name对吧

这个也是随机生成的文件名

这个呢也是File MD5

包括这个ext后缀还有图标

然后后边这块呢都是一样的了

跟上一张表

最后呢有个source

就是这个文件它的来源

但是这个呢也是根据需要

我们可以选

根据我们这个业务系统的需要

然后呢提交过来这个参数就可以了

好

这个呢这是我们这个PD File这张表

那么刚才呢我们是通过这个键表语句呢

已经把我们数据库里面

所涉及到的这两张表呢

已经这个

这个创建好了

当然了我们在这个今天的资料里边呢

也已经提供好了这个键表语句

大家呢也可以直接去执行咱们这个

Circle脚本也可以

然后呢在我们这个数据库资料数据库这

是不是有一个PD File.circle这个文件

然后呢我们直接

这里面呢也是相应的这个键表语句

当然这个呢是编码的问题啊

我们把这个编码呢给它修改一下就可以了

其实是一样的

跟咱们讲义上是一样的

也就是说我们也可以通过这个Circle脚本来创建我们的表

然后刚才也提到了

我们这个课程当中呢提供两种类型的服务对吧

那么通用的附件服务呢

我们最终呢就会把它保存到我们这个PD Attachment

这个叫做附件表里面

然后呢其他的比如说我们这个网盘服务对吧

所上传的这个这些文件信息呢

就会保存到PD File这个表里面去

这是关于我们这个数据库环境的搭建

那我们就先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频是关于“文件服务开发”系列课程的第5部分，具体为“5.1 环境搭建”中的“5.1.1 数据库环境搭建”章节。讲师通过演示在 MySQL 数据库中创建名为 `pd_files` 的数据库和两个核心数据表 `pd_attachment` 与 `pd_file` 的过程，为后续的文件服务开发奠定数据存储基础。视频内容主要围绕数据库设计、表结构定义和字段注释展开，强调了文件服务的核心功能（上传下载）和非功能性要求（可用性、配置性、扩展性），并介绍了将使用本地存储作为第一种存储策略。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开场，展示课程大纲，当前位于“文件服务开发”下的“5.1 环境搭建”。
*   **00:00:05 - 00:00:15**：讲师介绍文件服务的核心功能和非功能性要求，并概述课程将实现两种服务类型。
*   **00:00:15 - 00:00:30**：讲师进入“5.1.1 数据库环境搭建”子章节，展示数据库设计文档和表结构。
*   **00:00:30 - 00:00:45**：讲师在 MySQL Workbench 中演示创建名为 `pd_files` 的数据库，并设置字符集为 `utf8mb4`。
*   **00:00:45 - 00:01:00**：讲师在 Typora 编辑器中展示 `pd_attachment` 表的完整 SQL 创建语句，包括字段定义和注释。
*   **00:01:00 - 00:01:15**：讲师在 MySQL Workbench 中展示 `pd_attachment` 表的字段设计界面，逐个解释字段含义。
*   **00:01:15 - 00:01:30**：讲师展示 `pd_file` 表的字段设计界面，重点解释 `tree_path` 和 `grade` 字段。
*   **00:01:30 - 00:01:45**：讲师在 Typora 编辑器中展示 `pd_file` 表的完整 SQL 创建语句。
*   **00:01:45 - 00:02:00**：讲师总结数据库环境搭建完成，并预告下一节将讲解 Nacos 环境搭建。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **课程大纲**：清晰列出了“文件服务”的主要模块，包括“需求背景”、“核心功能”、“存储策略”、“技术设计”和“文件服务开发”。
    *   **文件服务核心功能**：明确指出核心功能是“上传和下载”，并列出了非功能性要求：可用性、配置性、扩展性。
    *   **存储策略**：介绍了两种服务类型：1) 面向应用系统的通用附件服务；2) 面向用户的网盘服务。
    *   **表结构说明**：详细说明了 `pd_attachment` 表用于存储文件元数据，`pd_file` 表用于存储文件的树形结构和层级关系。

*   **SQL 代码**：
    *   **创建数据库**：
        ```sql
        CREATE DATABASE `pd_files` CHARACTER SET utf8mb4;
        ```
    *   **创建 `pd_attachment` 表**：
        ```sql
        CREATE TABLE `pd_attachment` (
          `id` bigint(20) NOT NULL COMMENT '主键',
          `biz_id` varchar(64) DEFAULT NULL COMMENT '业务ID',
          `biz_type` varchar(255) DEFAULT NULL COMMENT '业务类型\n#AttachmentType',
          `data_type` varchar(255) DEFAULT NULL COMMENT '数据类型\n#DataType:DIR:目录;IMAGE:图片;VIDEO:视频;AUDIO:音频;DOC:文档;OTHER:其他',
          `submitted_file_name` varchar(255) DEFAULT '' COMMENT '原始文件名',
          `path` varchar(255) DEFAULT '' COMMENT 'FastDFS的远程文件名\n用于FastDFS',
          `relative_path` varchar(255) DEFAULT '' COMMENT '文件相对路径',
          `url` varchar(255) DEFAULT '' COMMENT '文件访问链接\n需要通过nginx配置路由，才能访问',
          `file_md5` varchar(255) DEFAULT NULL COMMENT '文件md5值',
          `context_type` varchar(255) DEFAULT '' COMMENT '文件上传类型\n用于上传文件的值',
          `ext` varchar(64) DEFAULT '' COMMENT '后缀\n(没有.)',
          `size` bigint(20) DEFAULT '0' COMMENT '大小',
          `org_id` bigint(20) DEFAULT NULL COMMENT '组织ID\n#core_org',
          `icon` varchar(64) DEFAULT '' COMMENT '图标',
          `create_month` varchar(10) DEFAULT NULL COMMENT '创建年月\n格式，yyyy-MM 用于统计',
          `create_week` varchar(10) DEFAULT NULL COMMENT '创建处于当年的第几周\nyyyy-WW 用于统计',
          `create_day` varchar(12) DEFAULT NULL COMMENT '创建年月日\n格式， yyyy-MM-dd 用于统计',
          `create_time` datetime DEFAULT NULL COMMENT '创建时间',
          `update_time` datetime DEFAULT NULL COMMENT '最后修改时间',
          `create_user` bigint(20) DEFAULT NULL COMMENT '创建人',
          `update_user` bigint(20) DEFAULT NULL COMMENT '最后修改人',
          `source` varchar(10) DEFAULT 'inner' COMMENT '文件来源：inner, outer',
          `is_delete` bit(1) DEFAULT '0' COMMENT '是否删除\n#NonLoanStatus(TRUE:1,只删不删)',
          PRIMARY KEY (`id`) USING BTREE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT COMMENT='附件';
        ```
    *   **创建 `pd_file` 表**：
        ```sql
        CREATE TABLE `pd_file` (
          `id` bigint(20) NOT NULL COMMENT '主键',
          `biz_id` varchar(64) DEFAULT NULL COMMENT '业务ID',
          `biz_type` varchar(255) DEFAULT NULL COMMENT '业务类型\n#AttachmentType',
          `data_type` varchar(255) DEFAULT NULL COMMENT '数据类型\n#DataType:DIR:目录;IMAGE:图片;VIDEO:视频;AUDIO:音频;DOC:文档;OTHER:其他',
          `submitted_file_name` varchar(255) DEFAULT '' COMMENT '原始文件名',
          `path` varchar(255) DEFAULT '' COMMENT 'FastDFS的远程文件名\n用于FastDFS',
          `relative_path` varchar(255) DEFAULT '' COMMENT '文件相对路径',
          `url` varchar(255) DEFAULT '' COMMENT '文件访问链接\n需要通过nginx配置路由，才能访问',
          `file_md5` varchar(255) DEFAULT NULL COMMENT '文件md5值',
          `context_type` varchar(255) DEFAULT '' COMMENT '文件上传类型\n用于上传文件的值',
          `ext` varchar(64) DEFAULT '' COMMENT '后缀\n(没有.)',
          `size` bigint(20) DEFAULT '0' COMMENT '大小',
          `org_id` bigint(20) DEFAULT NULL COMMENT '组织ID\n#core_org',
          `icon` varchar(64) DEFAULT '' COMMENT '图标',
          `create_month` varchar(10) DEFAULT NULL COMMENT '创建年月\n格式，yyyy-MM 用于统计',
          `create_week` varchar(10) DEFAULT NULL COMMENT '创建处于当年的第几周\nyyyy-WW 用于统计',
          `create_day` varchar(12) DEFAULT NULL COMMENT '创建年月日\n格式， yyyy-MM-dd 用于统计',
          `create_time` datetime DEFAULT NULL COMMENT '创建时间',
          `update_time` datetime DEFAULT NULL COMMENT '最后修改时间',
          `create_user` bigint(20) DEFAULT NULL COMMENT '创建人',
          `update_user` bigint(20) DEFAULT NULL COMMENT '最后修改人',
          `source` varchar(10) DEFAULT 'inner' COMMENT '文件来源：inner, outer',
          `is_delete` bit(1) DEFAULT '0' COMMENT '是否删除\n#NonLoanStatus(TRUE:1,只删不删)',
          PRIMARY KEY (`id`) USING BTREE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT COMMENT='文件表';
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库创建** (00:00:30)
    *   **描述**：讲师在 MySQL Workbench 中，点击“File” -> “New” -> “Create New Database”，在弹出的对话框中输入数据库名 `pd_files`，并选择字符集 `utf8mb
