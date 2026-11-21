# 12-用户注册-数据库结构 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着换咱们学习数据库结构的一个设计

在这里咱们来看一下

用户注册功能会涉及到哪些表

它们之间是怎么去关联和运作的

我们可以看到交易的核心表

是成交记录订单和常委表

之前也做了讲解和介绍

在这里并非我们的重点

重点咱们是要关注用户为主体的相关表

那么用户为主体可以看到

既然要支持SaaS模式运作

那么就有很多公司可以接入

那么用户会归属于不同公司下面

这个它们的对应关系是

公司和用户是1比N的关系

就是一对多

然后用户表和用户文件表

在这里面的话

它会去上传一些身份证

文件资料等相关信息

那么用户表跟用户文件

是一个一对多的关系

然后下面的话就是用户账户表

用户表跟用户文件

用户账户表是什么关系

是一个1比N的关系

也就是在这里面的话

一个用户可以开设多个交易账号

咱们可以了解到

就是说对于不同券商

我可以在中心证券上面开个户

也可以在国内居安上面开个户

也可以在红元证券

深望红元等等

都可以做这样的一个开户

但是按照咱们现在的交易规定

一个用户他只能在券商里面

开设三个账户

再往下面就是他的一些个账户预警表

在这里面

用户注册功能并不会用到

用户预警设置相关表

所以咱们重点是要关注公司表

用户表

还有用户文件表

用户账户表

红色区域部分是我们所需要新增的一些表

好

咱们来看一下相关的表结构

在这里面增加了用户表的用户文件表

这个是它的具体的表结构

表结构的话

咱们可以看到

这个是跟用户ID进行关联

那么为了可以支撑

不同文件类型的扩展

在这里加上了业务类型

像身份证

然后银行卡

信用卡等等

如果这样的话

你还想上传其他的证明文件

只要在这里扩充不同类型就可以了

表结构都不用再做调整和修改

下面就是File ID文件的唯一标识

咱们后面会采用SIF的分布式文件

进行一个存储

那么存储的时候

就需要生成一个唯一的ID

在下面的话

就是File Name文件的名称

文件类型

文件路径

然后就是它的状态

接着的话就是公司表

这个对应的就是

这个红色区域部分的公司表

因为此下这些表

咱们都做过讲解了

红色区域这部分表是新增的

咱们可以看到

公司表下面它有哪些属性

它有Company Name

然后Instant Type ID

机构类型

联系人

联系信息

这些的话就是一些基本资料

然后下面的话

就是它的管理员账号

States

因为每个公司的话

它必须有一个

管理者对不对

去分配下面的公司的角色

以及公司下面的

不同部门的操作管理人员

好

这个是公司的一些信息

再往下面就是机构表

机构表咱们之前讲过了

整个平台上面有多个角色

多种类型

可以在我们平台上面去使用

比如像集团

还有运营商

还有运营中心

对不对

那么他们在整个平台上面

都称作机构

这样的话

我们就可以了支撑将来更多的身份的揭露

也就变于了统一的一个管理

这个就是机构表

再往下面是系统全局的配置表

那么可以呢

去实现我们整个系统当中的一些配置参数

在这里呢

我们可以看到

这个分类编号呢

是包括不同的配置类型

比如像一些基础性的配置

业务性的配置

还有系统向的配置

那我们在这里注册机开户

属于什么配置啊?

属于业务性的配置

对不对

到时候的话呢

咱们就可以初始化对应的一条配置数据

如果说将来要做调整和修改

只要更改它对应的参数值就可以了

好

再往下面是它的序列表

因为咱们呢

会去实现了全局的序列号生成方案

在这里面的话呢

我们会做一个详细的讲解如何去生成

然后呢

整个的具体实现逻辑是怎样的

在这里呢

是通过

全局序列号生成了用户的唯一电号

好

那咱们呢

再回到刚才

这个呢

就是序列表的一个作用

好

在这里呢

用户注册和开户呢

是两个功能

对不对

只不过呢

我们是实现了用户注册机开户的功能

会生成一个交易账号

通过的开关做了一个全局配置

应涉及到开关配置

公筒参数以及将来的系统参数配置的处理呢

我们在这里就会加入全局的配置表

帮助我们呢

去实现整体的控制

这块呢

就对数据库结构的一个讲解

那这一讲啊

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程为“第2章 用户注册功能”的第3.2节“数据库结构”，主要讲解了在用户注册系统中，如何设计和创建数据库表结构。讲师通过在数据库设计工具（如 Typora）中展示实体关系图（ERD），并配合编写 SQL 脚本，详细演示了创建“用户文件表”、“公司表”和“系统全局配置表”等核心数据表的过程。同时，课程也介绍了如何为这些表创建索引，并规划了全局序列号的生成方案，为后续的实体类和数据访问层（DAO）开发做准备。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引入，展示当前章节“3.2 数据库结构”在大纲中的位置。
*   **00:15 - 00:45**: 展示数据库实体关系图，重点讲解“用户文件表”、“用户表”、“用户账户表”等核心表的字段构成和关联关系。
*   **00:45 - 01:15**: 演示创建“用户文件表”的 SQL 语句，包括字段定义、注释和主键设置。
*   **01:15 - 01:45**: 演示为“用户文件表”创建索引 `idx_userId`。
*   **01:45 - 02:15**: 演示创建“公司表”的 SQL 语句，包含公司名称、机构类型、联系人等字段。
*   **02:15 - 02:45**: 演示创建“系统全局配置表”的 SQL 语句，用于存储系统参数。
*   **02:45 - 03:15**: 演示为“系统全局配置表”创建索引 `idx_key`。
*   **03:15 - 03:45**: 演示向“系统全局配置表”中插入初始数据。
*   **03:45 - 04:15**: 演示创建“全局序列表” `t_seq` 用于管理全局ID。
*   **04:15 - 04:45**: 转入下一节“3.3 创建实体”，展示在项目中创建对应的 Java 实体类。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **实体关系图 (ERD)**: 展示了多个核心数据表，包括“系统全局配置表”、“序列表”、“股票交易表”、“用户表”、“用户账户表”、“用户文件表”、“公司表”等。图中用箭头标明了表与表之间的外键关系。
    *   **目录大纲**: 左侧显示了课程的完整目录结构，清晰地列出了“第1章 Sentinel集成使用”和“第2章 用户注册功能”下的各个子章节。

*   **SQL 代码**:
    *   **创建用户文件表**:
        ```sql
        drop table if exists t_trade_user_file;
        /*
        Table: t_trade_user_file
        */
        create table t_trade_user_file (
            id bigint not null auto_increment comment '主键标识',
            userId bigint(16) not null comment '用户ID',
            fileType tinyint(3) not null comment '业务类型 (0, 身份证, 1, 银行卡, 2, 信用卡)',
            filename varchar(64) comment '文件名称',
            fileTyp varchar(32) comment '文件类型',
            filePath varchar(255) comment '文件路径',
            status tinyint(3) not null comment '状态(0:有效, 1, 无效)',
            createTime datetime comment '创建时间',
            updateTime datetime not null default CURRENT_TIMESTAMP comment '更新时间',
            primary key (id)
        );
        ```
    *   **创建公司表**:
        ```sql
        drop table if exists t_company;
        CREATE TABLE 't_company' (
            'id' bigint(19) NOT NULL AUTO_INCREMENT COMMENT '主键标识',
            'companyName' varchar(32) DEFAULT NULL COMMENT '公司名称',
            'institutionType' varchar(32) CHARACTER SET utf8 DEFAULT NULL COMMENT '机构类型',
            'contactUser' varchar(32) NOT NULL DEFAULT NULL COMMENT '联系人',
            'contactPhone' varchar(32) DEFAULT NULL COMMENT '联系电话',
            'adminUser' varchar(32) DEFAULT NULL COMMENT '管理账号',
            'status' tinyint(3) NOT NULL COMMENT '状态(0:有效, 2, 禁用)',
            'creator' varchar(32) CHARACTER SET utf8 DEFAULT NULL COMMENT '创建人名称',
            'createTime' datetime DEFAULT NULL COMMENT '创建时间',
            'lastupdateUser' varchar(32) CHARACTER SET utf8 DEFAULT NULL COMMENT '最后更新人名称',
            'lastupdateTime' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
            PRIMARY KEY ('id'),
            KEY 'idx_accountNo' ('contactUser')
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='机构表';
        ```
    *   **创建系统全局配置表**:
        ```sql
        drop table if exists t_trade_global_config;
        /*
        Table: t_trade_global_config
        */
        create table t_trade_global_config (
            id bigint not null auto_increment comment '主键标识',
            code varchar(32) comment '配置项编号',
            category varchar(32) comment '分类编号(BASIC:基础配置, BUSINESS:业务配置, SYSTEM:系统配置)',
            value varchar(128) comment '配置项的值',
            status tinyint(2) not null comment '状态(0:启用, 1, 禁用)',
            primary key (id)
        );
        ```
    *   **创建全局序列表**:
        ```sql
        drop table if exists t_seq;
        /*
        Table: t_seq
        */
        create table t_seq (
            id bigint not null auto_increment comment '主键标识',
            code varchar(32) comment '配置项编号',
            value bigint(21) comment '序列值',
            primary key (id)
        );
        ```
    *   **创建索引**:
        ```sql
        create index idx_userId on t_trade_user_file (userId);
        create index idx_key on t_trade_global_config (code);
        ```
    *   **插入初始数据**:
        ```sql
        INSERT INTO 'trade_stock'.t_trade_global_config ('id', 'code', 'category', 'value', 'status') VALUES (1, 'REG_OPEN_ACCOUNT', 'SYSTEM', 'N', 0);
        ```

*   **Java 代码**:
    *   **全局序列ID接口**:
        ```java
        /**
         * 根据编号获取序列ID
         * @param code
         * @return
         */
        int getNextId(TradeSeq record);
        ```
    *   **Mapper 更新语句**:
        ```xml
        <update id="getNextId" keyColumn="nextId" keyProperty="nextId">
            parameterType="com.ictast.trade.stock.entity.system.TradeSeq">
            update t_seq set nextId = last_insert_id(nextId + 1) where code = #{code};
        </update>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库结构概览**
    *   讲师首先在 Typora 中展示了一个完整的数据库实体关系图，图中包含了“用户表”、“用户账户表”、“用户文件表”、“公司表”等多个核心表。
    *   通过鼠标点击和高亮，讲师重点介绍了“用户文件表”和“公司表”的字段结构，强调了 `userId`、`companyId`、`status` 等关键字段的作用。

*   **场景二：创建“用户文件表”**
    *   讲师切换到 SQL 代码编辑界面，演示了如何使用 `CREATE TABLE` 语句创建 `t_trade_user_file` 表。
    *   代码中包含了详细的字段定义，如 `id`（主键，自增）、`userId`（用户ID）、`fileType`（文件类型）、`status`（状态）等，并为每个字段添加了中文注释。
    *   讲师特别强调了 `status` 字段的取值含义（0:有效，1:无效）。

*   **场景三：创建“公司表”**
    *   讲师演示了创建 `t_company` 表的 SQL 语句。
    *   代码中定义了 `companyName`、`institutionType`、`contactUser`、`status` 等字段，并为 `status` 字段添加了注释“状态(0:有效, 2, 禁用)”。
    *   讲师还展示了如何为 `contactUser` 字段创建索引 `idx_accountNo`。

*   **场景四：创建“系统全局配置
