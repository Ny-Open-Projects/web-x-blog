# 28-代码生成器-工程配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢上面就开始创建MyBetis Generate的代码生成工程

打开我们的支流股服工程

在下面的话呢新建一个模块

new

然后呢model

这里呢也用model模板点击next

给它呢一个名称

这工程名称呢我们就叫MyBetis Generate

1

D-N-E-R-A-T-O-R

然后点击next

将名称呢调整一下

点击finish

这时候呢它就会生成MyBetis Generate的服工程

好

工程创建完成之后呢

咱们先不着急去做具体实现

先把它对应的依赖加入进展

这个依赖呢

我们从讲义当中呢拋笔进去

放到呢POM下面

大家注意一下

这里呢我们的依赖

是加入了对应的数据库驱动包

那在这里呢是买社口的数据驱动包

我们采用的是MailDB数据库

买社口的话呢

它都是可以兼容连接的

那么PG社口这一块呢

采用的是PG的专用的驱动包

这里呢是它的一个版本号

如果说我们后面要从PG社口当中

映射实体生成代码的话呢

我们就要用PG社口来做这个设定

这个驱动包要把它加入进来

在这里呢咱们呢就讲解

针对于买社口数据库

也就是我们的业务数据员

看一下呢如何去生成对应代码

那么PG社口这一块呢

可以先把它去掉

下面的话呢是

MyBatis Generator的

代码生成器的组件

这个呢是核心依赖

必须呢要把它加入进来

然后呢是MyBatis

因为我们呢是基于MyBatis的映射

如果说你采用GPA

或者是MATIS的映射

或者是Hypernet的框架的话呢

那么就不适用这套代码生成器

但是呢它也可以帮助我们呢

生成实体

如果说DAO或者说社口的话呢

那么GPA的话呢就不能呢

采用这个代码生成器

去做对应的生成和实现

好

这个呢是MyBatis Generator的

它的一个依赖的导入

那么依赖导入完成之后呢

咱们接下来呢还去创建它的配置文件

对不对

那这个配置文件的话呢

我们把它放在Resource目录下面

那么我们就来看

去new

然后呢

新建一个文件

好

这里呢我们将它

禁止忽略

找到我们的MyBatis Generator

并没有出现在这里面

对不对

那么呢我们把它重新刷新一下

Mave Reimport

好重新刷新之后

这个时候是不是可以看到啊

它是灰色的

我们要把它呢禁止忽略

好

那这样呢

它就会纳入我们整个工程了

就会放在这个管理当中

接下来咱们看一下

如何去配置MyBatis Generator

我们将Generator Config呢

这个配置文件

copy进来

那我们呢带着大家来逐一看一下

它具体是如何配置的

首先呢在这里是它的一个context上下文

这个呢我们给它一个唯一标识就可以了

那么Plugin呢

它在这里呢给它一个插件

就这个插件的话呢

是一个序列化的插件

比如说我们实体要实现

这个searchlizable这样一个接口

要通过这个插件

帮助我们做对应实现

然后下面的话是通过type

指定了自定义的注释生成器

因为mybetsgenerator

它默认生成的代码注释比较浓于

然后经常会出现很多的英文字符

不便于我们的理解以及维护

所以我们要通过自定义的注释生成器

去生成指定的注释

下面是jdbc

connect

它的数据库连接配置信息

咱们就指向虚拟器的数据库

再往下面是java-type-resolve

就是java的一个类型解析

就像那个big-d-sim

如果是我们的数字类型

想采用big-d-sim

那么在这里可以改为to

下面是java-model-generator

它的意思是配置对应的一个实体生成信息

比如说我们的实体的报名

实体所要生成存储的路径

在这里是它的一些属性配置

是不是要开启指保信息

这个我们要把它开启

在这里按照这个配置就可以了

在往下面是它的一个dao的配置

dao的话是我们的数据操作层的接口

在这里我们同样要配置它的一个报名

还有它生成的路径

再往下面就是插名

我们先用map

这个就是我们所熟知的mybattist的map文件

里面主要是社口文件信息

那么同样它会指定对应的pocket

就是我们的报名以及我们的生成目录

对不对

好

再往下面就是我们所要去映射和生成的表信息

在这里采用了两张表

一张是T-shirt user表

另外一张是T-shirt account表

一个是用户信息表

另外一个是交易账号信息表

在这里面有很多的一些属性

对不对

咱们来看一下它具体是什么意思呢

这个scam是它的数据户

table name就是我们的表名

那么enable count这个

就是说你要不要开启它的一个总数的circle的生成

如果说我们不需要

就将它改成force

我们比如说slack的count

就是获取一些分页总数信息

对不对

然后这里要不要enable upfile

就是要不要开启更新的这种语句

它是会根据by example的这种方式去生成circle信息

然后delete

在这里咱们都不需要

因为这些信息的话也用不到

我们的业务处理来讲的话

并不会是大量的单纯的增上改差

因为往往也会涉及很多的一些业务处理

再往下面的话是propt

是它的一个属性

这个是什么意思呢

就是说要不要根据

它实际的circle列名来映射对应的属性

咱们在这里就改成to

如果说咱们不根据

它会将circle当中的下滑线会自动做对应的一个转换

那我们在数据库里面设计的时候

我们可以看一下

它在这里面就已经采用了头红命名

对不对

所以在这里

它的意思就是保持一致就可以了

再往下面是它的generate key

也是ID的一个生成策略

这个我们采用支撑档为标识

那么chrome是它的一个列的一个属性配置

在这里面的话呢

比如说我们要针对是它的这个data这样一个属性值呢

采用一个data的字段

那么inlogicchrome要忽略了这种列名

我们呢

也可以在这里面做对应的配置

那在这里面的话呢

还有一些列名的一些其他配置

比如说我们要去配置一些long virtual field

在这里面的话呢

会让它指定一个jdbc的type

这个jdbc的type

可以采用什么

vhre

就是说对应的一个属性配置

这样呢

就更加灵活

可以根据我们自己的要求去设定不同的配置信息

那同样的

chrome的话呢

也是基本上是一样的配置

这里呢

就是mybetsgenerate

它配置文件的一个说明

怎么去配置

里面的话呢

有哪些配置项

它们具体的一个作用

以及它们对应的参数说明

好

这样呢

咱们先讲到这里

下一讲呢

咱们再来去实现对应的一个代码

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程为“第5章 MyBatis Generator代码生成器”的教学内容，主要讲解如何使用 MyBatis Generator 工具自动生成 Java 项目中的实体类、Mapper 接口及 XML 配置文件。讲师通过 IntelliJ IDEA 开发环境，演示了从创建 Maven 项目、配置 `pom.xml` 文件添加依赖，到编写 `generatorConfig.xml` 配置文件，最终实现对数据库表的代码自动生成。课程重点在于展示如何自定义注释生成器（`CustomCommentGenerator`）并配置生成规则，以满足特定项目需求。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 开场，展示课程大纲，定位到“第5章 MyBatis Generator代码生成器”。
*   **00:03 - 00:06**: 讲解“3.1 说明”，介绍 MyBatis Generator 是一个自动代码生成工具，可生成实体、Mapper 接口和 XML 文件，并支持自定义扩展。
*   **00:06 - 00:10**: 讲解“3.2 创建工程”，展示项目结构，包括 `src/main/java` 和 `src/main/resources` 目录。
*   **00:10 - 00:15**: 在 `pom.xml` 文件中添加数据库驱动依赖（MySQL 和 PostgreSQL）。
*   **00:15 - 00:20**: 在 `pom.xml` 文件中添加 MyBatis Generator 核心依赖和 MyBatis 依赖。
*   **00:20 - 00:25**: 讲解 `generatorConfig.xml` 配置文件的结构和作用。
*   **00:25 - 00:30**: 在 `generatorConfig.xml` 中配置 `commentGenerator`，使用自定义注释生成器 `CustomCommentGenerator`。
*   **00:30 - 00:35**: 配置 `jdbcConnection`，设置数据库连接信息（URL、用户名、密码）。
*   **00:35 - 00:40**: 配置 `javaModelGenerator`，设置生成的实体类包名和输出目录。
*   **00:40 - 00:45**: 配置 `sqlMapGenerator`，设置生成的 Mapper 接口包名和输出目录。
*   **00:45 - 00:50**: 配置 `javaClientGenerator`，设置生成的 Mapper XML 文件包名和输出目录。
*   **00:50 - 00:55**: 配置 `table` 节点，为具体的数据库表（如 `t_trade_user` 和 `t_trade_account`）设置生成规则，包括字段映射、主键生成策略等。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：第5章 MyBatis Generator代码生成器，包含“目标”、“步骤”、“实现”、“使用说明”等子章节。
    *   项目结构图：展示 `mybatis-generator` 项目下的 `src/main/java` 和 `src/main/resources` 目录结构。
    *   `generatorConfig.xml` 文件结构：包含 `<context>`、`<commentGenerator>`、`<jdbcConnection>`、`<javaModelGenerator>`、`<sqlMapGenerator>`、`<javaClientGenerator>` 和 `<table>` 等核心配置节点。

*   **代码关键内容**:

    *   **`pom.xml` 依赖配置**:
        ```xml
        <!-- MySQL 数据库驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.14</version>
        </dependency>

        <!-- PostgreSQL 数据库驱动 -->
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>${postgresql.version}</version>
        </dependency>

        <!-- MyBatis Generator 核心 -->
        <dependency>
            <groupId>org.mybatis.generator</groupId>
            <artifactId>mybatis-generator-core</artifactId>
            <version>1.3.7</version>
        </dependency>

        <!-- MyBatis -->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.4.6</version>
        </dependency>
        ```

    *   **`generatorConfig.xml` 配置**:
        ```xml
        <!DOCTYPE generatorConfiguration
            PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
            "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">

        <generatorConfiguration>
            <!-- 注释生成器 -->
            <commentGenerator type="org.mybatis.generator.plugins.SerializablePlugin">
                <!-- 自定义注释生成器 -->
                <commentGenerator type="com.mybatis.generator.custom.CustomCommentGenerator">
                </commentGenerator>

            <!-- 数据库连接 -->
            <jdbcConnection driverClass="com.mysql.jdbc.Driver"
                            connectionURL="jdbc:mysql://192.168.19.150:3306/trade_stock?characterEncoding=UTF-8"
                            userId="root"
                            password="654321">
            </jdbcConnection>

            <!-- 实体类生成配置 -->
            <javaModelGenerator targetPackage="com.icitast.trade.stock.entity"
                                targetProject="mybatis-generator/output">
                <property name="enableSubPackages" value="true"/>
                <property name="trimStrings" value="true"/>
            </javaModelGenerator>

            <!-- Mapper 接口生成配置 -->
            <sqlMapGenerator targetPackage="com.icitast.trade.stock.dao"
                             targetProject="mybatis-generator/output">
                <property name="enableSubPackages" value="true"/>
            </sqlMapGenerator>

            <!-- Mapper XML 文件生成配置 -->
            <javaClientGenerator type="XMLMAPPER"
                                targetPackage="com.icitast.trade.stock.dao"
                                targetProject="mybatis-generator/output">
                <property name="enableSubPackages" value="true"/>
            </javaClientGenerator>

            <!-- 表生成配置 -->
            <table schema="trade_stock" tableName="t_trade_user"
                   enableCountByExample="false"
                   enableUpdateByExample="false"
                   enableDeleteByExample="false"
                   enableSelectByExample="false"
                   selectByExampleQueryId="false">
                <property name="useActualColumnNames" value="true"/>
                <generatedKey column="ID" sqlStatement="MySql" identity="true"/>
                <columnOverride column="DATE_FIELD" property="startDate"/>
                <ignoreColumn column="LONG_VARCHAR_FIELD" jdbcType="VARCHAR"/>
            </table>

            <table schema="trade_stock" tableName="t_trade_account"
                   enableCountByExample="false"
                   enableUpdateByExample="false"
                   enableDeleteByExample="false"
                   enableSelectByExample="false"
                   selectByExampleQueryId="false">
                <property name="useActualColumnNames" value="true"/>
                <generatedKey column="ID" sqlStatement="MySql" identity="true"/>
                <columnOverride column="DATE_FIELD" property="startDate"/>
                <ignoreColumn column="LONG_VARCHAR_FIELD" jdbcType="VARCHAR"/>
            </table>
        </generatorConfiguration>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**
    *   **描述**: 讲师在 IntelliJ IDEA 中创建了一个名为 `mybatis-generator` 的 Maven 项目。他通过鼠标滚轮和点击操作，依次在 `pom.xml` 文件中添加了 MySQL、PostgreSQL 数据库驱动依赖、MyBatis Generator 核心依赖和 MyBatis 依赖。演示了如何通过编辑器的高亮和自动补全功能来快速添加和配置依赖。

*   **场景二：配置文件编写与自定义注释**
    *   **描述**: 讲师切换到 `generatorConfig.xml` 文件。他首先配置了 `commentGenerator`，并将其类型设置为自定义的 `CustomCommentGenerator` 类。接着，他配置了 `jdbcConnection`，输入了数据库的连接 URL、用户名和密码。他强调了配置文件的结构和各节点的作用。

*   **场景三：生成规则配置**
    *   **描述**: 讲师依次配置了 `javaModelGenerator`、`sqlMapGenerator` 和 `javaClientGenerator`，分别指定了生成的实体类、Mapper 接口和 XML 文件的包名和输出目录。他展示了如何通过 `property` 节点来设置生成规则，如 `enableSubPackages` 和 `trimStrings`。

*   **场景四：表级配置与字段映射**
    *   **描述**: 讲师在 `generatorConfig.xml` 中添加了两个 `<table>` 节点，分别对应数据库中的 `t_trade_user` 和 `t_trade_account` 表。他详细演示了如何为每个表配置生成规则，包括禁用某些查询方法（如 `enableCountByExample`）、设置主键生成策略（`generated
