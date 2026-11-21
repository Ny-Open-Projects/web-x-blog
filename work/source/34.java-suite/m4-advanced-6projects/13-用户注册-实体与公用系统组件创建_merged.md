# 13-用户注册-实体与公用系统组件创建 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们开始去创建用户注册所需要用到的实体

以及呢

我们公用的系统层组件的封装处理

好

那我们看一下

在这里呢

会涉及到哪些实体呢

其实呢

这个呢

就是我们数据库结构当中所讲到的

这几个主要的实体信息

像GitHub account

GitHub globe configure

GitHub user file

GitHub company

GitHub instig

那在这里呢

我们可以通过MyBedis generator工程呢

帮助我们快速去生成了实体和数据层代码

我们看一下怎么去配置和生成呢

找到咱们的MyBedis generator工程

然后呢

找到它的配置文件

在这里呢

其实只要按照这个table的格式去进行了一个copy

然后呢

将这个table name修改一下

那我们可以看到

我们可以把这些GitHub account

GitHub globe configure

这些表呢

加入进去

那加入进去之后呢

然后呢

去生成对应的代码

咱们先把这些代码清空一下

这里呢

去delete

然后找到咱们的启动内

右键run运行

运行完成之后呢

咱们关台下autoboot这个目录

好

那么在autoboot目录下面呢

就生成了对应的实体以及数据层

对不对

当然这个生成的实体呢

并非就可以照搬过去使用

咱们呢

还做一些调整

对不对

因为按照MyBedis generator呢

它在这里呢

会按它默认的模板生成对应的代码

像这种的话呢

就没必要

两个字母都搭起来

对不对

那么我们怎么办呢

可以呢

将这些内容copy过去

因为这些属性呢

都帮我们生成和备制好了

然后的话呢

就要将class做一个修改就可以了

那我们在n体下面

在这里呢

我已经将它全部创建完成

那个instage

还有company

缺的counter

大家呢

也要按照这个方法

去生成对应的实体

把这些必要的实体信息呢

先创建好

创建完成之后呢

数据层这块

咱们先不着急去实现

创建数据层

生成数据层代码的作用呢

比如说我们要去查询

对应的数据

要做映射

对不对

那么就可以将这个Lizardo map呢

直接copy过去

当然了

大家如果是有时间和精力呢

可以做一个个性化的定制

这些的话呢

比如说

你可以去修改它的一些

收口的一些语句

这些呢都可以

然后去生成呢

你想要的一些语句呢

可以去创建一些常用的接口类型

但是呢

一般复杂一点的项目的话呢

它都会有自定义的收口

对不对

所以呢

咱们在这里

不能去完全套用它

所生成的默认的这种查询收口

还有它的一些操作收口

那么呢

我们只需要呢

让借助于它的一些基础信息

帮助我们呢

快速的去实现收口的编写

就可以了

这个呢

就是咱们使用代码生成器的一个目的

好

那接着的话呢

咱们就要去创建

公用的系统层组件

那么系统层组件在这里呢

我们先去实现

T-Chad Global Config

就是全局的配置数据层接口

这个呢

是便于各微幅模块的一个附用

咱们想一下

因为这个是全局的配置

对不对

就没必要呢

把这个放在具体的某一个微幅节点下面

去做实现

应该把它抽离出来

这样呢

就便于它的附用

那么怎么去实现呢

我们可以看到

在T-Chad

巴斯特

托尔控门下面

咱们打开System

在下面呢

有两个包

一个包呢

是service

一个是DEO数据层的实现

那这里呢

是针对于T-Chad Global Config

做了一个数据层接口的一个编写

那么数据层接口的话呢

包括它的新增

对不对

get by

就是根据具体的一个编号去查询

它整个的配置对象

然后呢

根据编号

获取了它的序列ID

这个呢

是数据层的接口

在这里呢

咱们先把这些基本的接口提供好就可以了

那在这里可以看到有很多的社会具对不对

对一些个性化的

比如说自身业务相关的

咱们可以去自己自己去编写

那么对于这种的话

通用性的就直接copy过来就行了

没必要呢

去把时间花在一些重复性的简单的工作方面

好

那么service层这一块呢

可以看到我们呢

是对DEO的项目呢

做了一套封装

那么呢

它提供了些什么接口呢

提供了一个根据编号去获取了全局系统配置信息的接口

因为呢

在用户服务当中要去做调用

去生成对应的用户编号

好

在这里呢

就是对公用系统人组建的一个封装

以及呢

实体的创建

那这一讲呢

我们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的 Java 项目中“用户注册功能”开发过程的演示。核心内容是使用 MyBatis Generator 工具自动生成与数据库表 `t_trade_account`、`t_trade_global_config`、`t_trade_user_file`、`t_company`、`t_institution` 对应的 Java 实体类（Entity）和数据访问对象（DAO/Mapper）层代码。演示者通过修改 MyBatis Generator 的配置文件，然后执行生成操作，最终在项目中创建了相应的 Java 文件和 XML 映射文件。视频还展示了如何为这些生成的实体类和 DAO 接口编写业务逻辑，例如通过 `TradeGlobalConfigService` 服务类根据配置代码查询系统配置信息。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示项目文档（Typora）中“3.3 创建实体”章节，说明本节目标是通过 MyBatis Generator 生成实体与数据层代码。
*   **00:00:05 - 00:00:15**: 展示 MyBatis Generator 配置文件 `generatorConfig.xml` 的内容，其中定义了需要生成的数据库表名，如 `t_trade_account` 和 `t_trade_global_config`。
*   **00:00:15 - 00:00:25**: 演示者在 IntelliJ IDEA 中右键点击 `mybatis-generator` 模块，选择“Run 'StockUserApplication'”或“Generate”来执行代码生成。
*   **00:00:25 - 00:00:40**: 展示生成后的 Java 文件，如 `TTradeAccount.java` 和 `TTradeGlobalConfig.java`，以及对应的 Mapper XML 文件 `TTradeAccountMapper.xml`。
*   **00:00:40 - 00:00:55**: 展示生成的 Mapper XML 文件内容，其中包含了 `insert` 和 `selectKey` 等 SQL 语句，用于处理数据库的插入和主键回填。
*   **00:00:55 - 00:01:10**: 展示 `TradeGlobalConfigMapper.xml` 文件，其中定义了查询 `t_trade_global_config` 表的 SQL 语句。
*   **00:01:10 - 00:01:25**: 展示 `TradeGlobalConfigService` 服务类的代码，其中定义了根据配置代码查询系统配置信息的方法 `getTradeGlobalConfigByCode`。
*   **00:01:25 - 00:01:40**: 视频结束，回到项目文档，显示“3.4 创建公用系统层组件”章节，预示下一节内容。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**:
    *   **章节标题**: “3.3 创建实体”
    *   **关键步骤**:
        1.  修改 MyBatis Generator 配置文件，生成 `t_trade_account`, `t_trade_global_config`, `t_trade_user_file`, `t_company`, `t_institution` 实体与数据层代码。
        2.  创建 `TradeAccount` 与 `TradeUserFile`。
    *   **项目结构图**: 展示了 `bulls-stock-entity` 模块下的 `src/main/java/com.icast.bulls.stock.entity` 包结构，其中包含 `TradeGlobalConfig`, `Company`, `Institution`, `TradeAccount`, `TradeUser` 等实体类。

*   **代码关键内容**:

    *   **MyBatis Generator 配置文件 (`generatorConfig.xml`)**:
        ```xml
        <table schema="trade_stock" tableName="t_trade_account" enableCountByExample="false" enableUpdateByExample="false" enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false">
            <property name="useActualColumnNames" value="true"/>
            <generatedKey column="ID" sqlStatement="MySql" identity="true"/>
            <columnOverride column="DATE_FIELD" property="startDate"/>
            <ignoreColumn column="LONG_VARCHAR_FIELD" jdbcType="VARCHAR"/>
        </table>
        ```

    *   **生成的 Java 实体类 (`TTradeAccount.java`)**:
        ```java
        public class TTradeAccount implements Serializable {
            private Long id;
            // ... 其他属性
        }
        ```

    *   **生成的 Mapper XML 文件 (`TTradeAccountMapper.xml`)**:
        ```xml
        <resultMap id="BaseResultMap" type="com.icast.bulls.stock.entity.TTradeAccount">
            <id column="id" jdbcType="BIGINT" property="id"/>
            <result column="user_id" jdbcType="BIGINT" property="userId"/>
            <result column="account_no" jdbcType="VARCHAR" property="accountNo"/>
            <result column="balance" jdbcType="BIGINT" property="balance"/>
            <result column="trade_group_id" jdbcType="BIGINT" property="tradeGroupId"/>
            <result column="status" jdbcType="TINYINT" property="status"/>
            <result column="institution_id" jdbcType="BIGINT" property="institutionId"/>
            <result column="company_id" jdbcType="BIGINT" property="companyId"/>
            <result column="user_name" jdbcType="VARCHAR" property="userName"/>
            <result column="trade_group_name" jdbcType="VARCHAR" property="tradeGroupName"/>
        </resultMap>

        <insert id="insert" parameterType="com.icast.bulls.stock.entity.TTradeAccount">
            <selectKey keyProperty="id" order="AFTER" resultType="java.lang.Long">
                SELECT LAST_INSERT_ID()
            </selectKey>
            insert into t_trade_account (user_id, account_no, balance, trade_group_id, status, institution_id, company_id, user_name, trade_group_name)
            values
            (#userId,jdbcType=VARCHAR), (#accountNo,jdbcType=VARCHAR), (#balance,jdbcType=VARCHAR), (#tradeGroupId,jdbcType=VARCHAR), (#status,jdbcType=VARCHAR), (#institutionId,jdbcType=VARCHAR), (#companyId,jdbcType=VARCHAR), (#userName,jdbcType=VARCHAR), (#tradeGroupName,jdbcType=VARCHAR)
        </insert>
        ```

    *   **生成的 Service 代码 (`TradeGlobalConfigServiceImpl.java`)**:
        ```java
        @Service
        public class TradeGlobalConfigServiceImpl implements ITradeGlobalConfigService {
            @Autowired
            private ITradeGlobalConfigDao tradeGlobalConfigDao;

            @Override
            public TradeGlobalConfig getTradeGlobalConfigByCode(String code) {
                return tradeGlobalConfigDao.getByCode(code);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：配置文件修改与生成**
    *   **描述**: 演示者首先在 Typora 文档中确认了本节目标。随后切换到 IntelliJ IDEA，打开 `mybatis-generator` 模块下的 `generatorConfig.xml` 文件，展示其中配置的数据库表名。接着，右键点击项目，选择“Run 'StockUserApplication'”来执行生成操作。

*   **场景二：生成结果展示**
    *   **描述**: 生成完成后，演示者在项目结构中导航到 `bulls-stock-entity` 模块，展示生成的 Java 文件（如 `TTradeAccount.java`）和 XML 映射文件（如 `TTradeAccountMapper.xml`）。同时，通过打开 `TTradeAccountMapper.xml` 文件，详细讲解了其中的 `resultMap` 和 `insert` 标签的含义和作用。

*   **场景三：服务层开发**
    *   **描述**: 演示者切换到 `bulls-stock-common-system` 模块，打开 `TradeGlobalConfigMapper.xml` 文件，展示查询 `t_trade_global_config` 表的 SQL 语句。然后，打开 `TradeGlobalConfigServiceImpl.java` 文件，讲解如何通过 `@Autowired` 注入 DAO 接口，并实现 `getTradeGlobalConfigByCode` 方法来查询系统配置信息。

*   **场景四：项目结构回顾**
    *   **描述**: 视频最后回到 Typora 文档，展示“3.4 创建公用系统层组件”章节，预示接下来将介绍如何创建和使用这些生成的组件。
