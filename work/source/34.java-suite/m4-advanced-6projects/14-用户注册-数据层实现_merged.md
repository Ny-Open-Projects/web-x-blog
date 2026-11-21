# 14-用户注册-数据层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话咱们就来对数据层做一个实现

我们看一下找到BuzzTalk User服务工程

然后我们在DOU下面去创建对应的接口

咱们看一下数据层要实现哪些接口呢

在这里要提供两个操作接口

第一个是交易账号的数据层接口

第二个是用户文件的数据层接口

咱们来实现一下

在这里咱们去创建Interface

这个名称的话咱们先来创建交易账号的数据层接口

Account.DOU

先加上对应的注解

微博C2里标注为数据层接口

然后咱们给它提供两个方法

第一个是新增

因为咱们是要注册及开户

要创建交易账号

那么给它创建一个新增的接口

加上对应的注释

新增交易账号信息

再往下面咱们再加另外一个接口

这个接口是根据交易账户编号来获取交易账户的对象信息

Add Account

Add By Account Number

给它传递一个参数

Add Account Number

Add Account Number

用户的交易账户编号

这个Padme呢

注意是在MyBetis下面的

选中iBetis下面的这个包

加上对应的注释

根据账户编号

获取交易用户对象

接着的话呢

咱们还要去实现它的MAP文件

在这里呢

咱们就可以去copy刚才所生成的

MAP文件

那个代码文件

在output下面

找到呢

Shared Account的这个MAP文件

在这里就可以直接copy过来

这也就是说为什么会通过代码生成器它的一个作用

那生成完成之后呢

咱们要改下名称

重新名

AddShift再加R

然后在这里呢

我们把名字改一下

Shared Account Map

好

更改完名称之后呢

这些不必要的注释

咱们把它去除掉

那像这个Insert的话呢

可以保留

像其他的这些介绍的话呢

就不需要了

对不对

好了

都把它删除掉

可以看到能用的信息的其实并不是特别多

所以呢

我们就将代码生成的时候呢

一些不必要的接口

我们就没有拿它去生成

在这里的首先要注意了

把它的那个路径做一个替换

然后这个是实体

对不对

实体

咱们要找到它对应的路径

copy reference

Ctrl加Q

回到上一次编辑的地方

然后呢

将它替换下

好

在这一块呢

路径就没有问题了

那么影射的这一块呢

同样也要在这里了

做个修改

因为咱们在这里会有一个影射的接口

对吧

那我们还差一个接口

一个接口呢

就是Get by Account Number

这里呢

我们做个实现

采用Stack标签ID的话呢

我们可以copy过来

好

我们来看看这个绿灶的Map

这个话呢

就采用上面的Base绿灶的Map

Stack的语句呢

我们也可以节省点时间

在这里面好

直接copy下Stack

然后呢

将这些属性的copy过来

这个是ID

这里说进一下

Chad group name

这里并没有s

下面的话呢

就是flom

flom什么表呢

TChadColon

这个呢

我们终于就改成Dash

它的条件呢

就是Rail

然后呢

AccountNumber

那等于我们传递过来的AccountNumber

这个值

这个呢

就是根据账户编号去获取交易对象

用户交易对象

这个交易账户的数据对象呢

我们就已经创建完成

接着的话呢

咱们要创建用户的文件的数据层接口

对不对

那咱们来创建一下

右键new

Java class选择interface

这里让我们i开头了

Chad user file do

加上它的注解

以后set里

然后新增两个接口

一个呢是影射的接口

Chad user file

给它加上注释

新增交易账户的文件对象

再往下进一步

下面呢

咱们再创建一个接口

这个接口的话

根据用户ID去获取所有的文件信息

文件对象要传递User ID

同样加上注释根据用户ID获取所有文件信息

好

然后呢

我们还创建它的web文件

对不对

我们将这个copy一下

名称做个修改

这些不必要的注释呢

去掉

然后影射的在这里也把它

那个不必要的注释去掉了

下面这些收口的话呢

不需要把它删除掉

我们呢

来实现刚才所新增的接口

get by user ID

result map

要等于base

result map

这里面的话呢

我们也copy一下

改成大写

让它所有属性呢

都查出来

ID保持文件格式

flown

这个呢是T-Chad user file

这个呢是T-Chad user file

这个表

然后加上它的条件

user ID

要等于我们所传递过来的user ID

好

这个数据层呢

我们就已经实现完成

那咱们呢

再回到讲习当中

我们呢已经将这两个数据层接口呢

做到实现

那接着的话呢

咱们还会涉及到用户注册逻辑的

调整对不对

所以呢

我们还在用户的接口上面呢

去增加对应的方法

像在这里呢

使到个user db的选项呢

要增加呢

check regist

我们呢

来看一下

增加一个方法

这个方法的话呢

是根据

咱们先把这个

导入进来

它是根据呢

用户编号

然后呢

email

还有呢

手机号

去检查呢

是否已经被注册

也就说

这三者呢

如果其中有一个

存在于我们系统当中

那咱们呢就认为呢

它已经是

在我们系统当中

进行了注册

因为这三个信息的话呢

都是

唯一的

标识

那map文件呢咱们去copy一下

我们

找到

stock user map

在下面的话呢

增加对应的实现

我们看一下这个

circle是怎么去写呢

在这里呢是传递了这三个条件对不对

而这三个条件的关系的话呢是货的关系

并非

与的关系这一点呢

大家要了解清楚

不要写错了

那么呢

因为

正是因为采用这种

货的关系对不对

这样的话呢

有可能会产生多条记录

那怎么办呢

咱们只需要呢

limit 1就可以了

当然如果是你在实际

测试过程当中比较严谨

不会产生这样脏数据或者垃圾数据的话呢

不写这个也没问题

但是呢

为了避免

咱们现场当中

或者是些不可预知的bug所造成的一些数据问题

咱们呢

还是可以

现已呢

把这个limit

这个语句呢

加上去对不对

这样程序来讲啊就不会出现一些未知的异常

这个是checkregister的

方法处理

接着的话呢我们还看一下

他要去获取公司的信息接口

这个话是根据什么获取呢

根据公司的ID去获取公司对象

咱们呢也把这个呢

做个实现

放在

stock user do下面

这个是company view

comany view呢

咱们

并没有对不对

要将它定义一下

我们在这里有个view的宝

然后呢

将comany view先copy过来

new

cast

这里做个copy替换

通过longbook的

入解呢

它会自动把我们生成get和set的方法

再导入一下

它已经自动导入完成

这个呢是

根据ID来获取了

公司的信息

因为呢

整个逻辑的时候呢

还要去

做

公司信息的一个反显

那同样的话呢

咱们也将map文件做一个实现

呃是在stock user map下面

那同样的

在这里呢

它的实现来讲也可能会产生多条

也就是说为了避免呢

产生一些张数据问题

咱们

建议呢最好还是要把limit1这个加上

那它的查询来讲呢

是去join

机构信息表

对不对

join机构信息表的他们的跨年关系

是

机构信息表的

表里面

咱们可以看到它的别名是t对不对

有一个什么

详细的

数据ID

也就是详细的机构ID

那么这个详细的机构ID的话呢

跟company的ID是进行关联的

company的别名是u

好

那在这里呢

它进行了一个表连接

表连接完成之后呢

管理的条件就是公司的ID

这样呢

就会找到对应的一条公司数据

对不对

正常情况下来讲的话呢

它只会找到一条

对吧

但是呢

如果说你在这里面

产生了一个垃圾数据

可能呢

会出现多条

所以呢

还是要把这个limit

加上以防万一

好

然后在这里呢

查询到对应的数据之后

对吧

这样的company呢

它就是

有一个机构

信息的

可以看到

对机构的

这个类型呢做了一些

冗余

那么呢

在

用户注册的整个逻辑上来讲呢

就能够呢

实现一些信息的反显

将来要去查询用户对象资料的时候呢

就不需要再去反查这些表

减少了它的一些

查询品质

好

那这一块呢

就是数据层的一个

接口实现

就在这里呢

数据层所用到的一些接口呢

咱们呢

都将它

实现好了

接着的话呢咱们就能呢

去

实现了服务层的代码

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统（`bulls-stock-user`）的“用户注册功能”模块开发教程，重点讲解了数据层（DAO层）的构建。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建和配置 MyBatis 的 Mapper 文件、DAO 接口以及对应的实体类。内容涵盖了数据库表结构映射、增删改查（CRUD）操作的接口定义、以及如何使用 MyBatis 的 `@SelectKey` 注解来处理自增主键。整个过程旨在为后续的业务逻辑层（Service）和控制层（Controller）提供数据访问支持。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节划分是基于画面内容和逻辑顺序进行的推断：

*   **00:00 - 00:05**：课程引入，展示项目结构。讲师在 IDE 中打开 `bulls-stock-user` 项目，定位到 `src/main/java/com.icitcast.trade.stock.user/dao` 包，并高亮显示了 `TradeAccountDao` 和 `ITradeUserFileDao` 等接口文件，说明本节将创建数据层组件。
*   **00:05 - 00:15**：创建 DAO 接口。讲师在 `ITradeAccountDao` 接口中定义了 `insert` 和 `getByAccountNo` 方法，用于新增交易账户和根据账号查询用户。
*   **00:15 - 00:25**：创建 Mapper XML 文件。讲师打开 `StockUserMapper.xml` 文件，定义了 `resultMap` 和 `insert` SQL 语句，用于映射 `TradeAccount` 实体类并插入数据。
*   **00:25 - 00:35**：创建实体类。讲师展示 `TradeAccount` 实体类，其中包含 `id`、`userId` 等字段，并说明其继承自 `BaseEntity`。
*   **00:35 - 00:45**：创建文件映射接口。讲师在 `ITradeUserFileDao` 接口中定义了 `insert` 方法，用于新增用户文件记录。
*   **00:45 - 00:55**：创建文件映射 XML。讲师打开 `TradeUserFileMapper.xml` 文件，定义了 `resultMap` 和 `insert` SQL 语句，用于映射 `TradeUserFile` 实体类。
*   **00:55 - 01:05**：创建校验接口。讲师在 `IStockUserDao` 接口中定义了 `checkRegister` 方法，用于校验用户是否已注册。
*   **01:05 - 01:15**：创建校验 XML。讲师在 `StockUserMapper.xml` 文件中定义了 `checkRegister` 查询语句，用于根据用户编号、邮箱或手机号查询用户。
*   **01:15 - 01:25**：创建公司信息接口。讲师在 `IStockUserDao` 接口中定义了 `getCompanyVoById` 方法，用于根据公司 ID 获取公司对象。
*   **01:25 - 01:35**：创建公司信息实体。讲师展示 `CompanyVo` 实体类，包含 `id`、`companyName` 和 `bizType` 等字段。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.5 数据层`。
    *   **目标**：创建 DAO 与 MAPPER 文件。
    *   **关键接口定义**：
        *   `ITradeAccountDao` 接口：
            ```java
            int insert(TradeAccount record);
            TradeAccount getByAccountNo(Long accountNo);
            ```
        *   `ITradeUserFileDao` 接口：
            ```java
            int insert(TradeUserFile record);
            List<TradeUserFile> selectList();
            ```
        *   `IStockUserDao` 接口：
            ```java
            Integer checkRegister(@Param("userNo") String userNo, @Param("email") String email, @Param("phone") String phone);
            CompanyVo getCompanyVoById(@Param("id") Long id);
            ```
    *   **关键 Mapper XML 语句**：
        *   `resultMap` 定义：
            ```xml
            <resultMap id="BaseResultMap" type="com.icitcast.bulls.stock.entity.TradeUser">
                <id column="id" property="id" jdbcType="BIGINT" />
                <result column="userNo" jdbcType="VARCHAR" property="userNo" />
                <!-- ... 其他字段映射 ... -->
                <result column="createTime" jdbcType="TIMESTAMP" property="createTime" />
            </resultMap>
            ```
        *   `insert` 语句：
            ```xml
            <insert id="insert" parameterType="com.icitcast.bulls.stock.entity.TradeAccount">
                insert into t_trade_account (id, accountNo, status, companyId, userName, tradeGroupId, activeTime, institutionTypeId, institutionName, createBy, createTime, updateBy, updateTime)
                values (#id, #accountNo, #status, #companyId, #userName, #tradeGroupId, #activeTime, #institutionTypeId, #institutionName, #createBy, #createTime, #updateBy, #updateTime)
            </insert>
            ```
        *   `checkRegister` 查询语句：
            ```xml
            <select id="checkRegister" resultType="java.lang.Integer">
                select 1
                from t_trade_user
                where userNo = #{userNo} or email = #{email} or phone = #{phone}
                limit 1
            </select>
            ```
        *   `getCompanyVoById` 查询语句：
            ```xml
            <select id="getCompanyVoById" resultType="com.icitcast.bulls.stock.entity.CompanyVo">
                select id, companyName, bizType
                from t_company
                where id = #{id}
            </select>
            ```

*   **代码关键内容**：
    *   **实体类 `TradeAccount`**：
        ```java
        public class TradeAccount extends BaseEntity {
            private Long id;
            private Long userId;
            // ... 其他字段 ...
        }
        ```
    *   **实体类 `TradeUserFile`**：
        ```java
        public class TradeUserFile extends BaseEntity {
            private Long id;
            private Long userId;
            private String filename;
            private String filePath;
            private Integer status;
            private Long createTime;
            private Long updateTime;
        }
        ```
    *   **实体类 `CompanyVo`**：
        ```java
        @Data
        public class CompanyVo {
            private Long id;
            private String companyName;
            private Integer bizType;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建数据层文件结构**（画面 1）
    *   **描述**：讲师在 IDE 中展示 `bulls-stock-user` 项目的目录结构，重点指向 `dao` 包下的 `TradeAccountDao` 和 `ITradeUserFileDao` 接口文件，说明本节将围绕这些文件进行开发。

*   **场景二：定义 DAO 接口**（画面 2-3）
    *   **描述**：讲师在 `ITradeAccountDao` 接口中定义了 `insert` 和 `getByAccountNo` 方法，并在 `StockUserMapper.xml` 文件中编写了对应的 `insert` SQL 语句，使用 `@SelectKey` 注解来获取自增主键 `id`。

*   **场景三：创建实体类**（画面 4）
    *   **描述**：讲师展示 `TradeAccount` 实体类，其中包含 `id`、`userId` 等字段，并说明其继承自 `BaseEntity`，用于映射数据库表 `t_trade_account`。

*   **场景四：创建文件映射接口**（画面 5-6）
    *   **描述**：讲师在 `ITradeUserFileDao` 接口中定义了 `insert` 方法，并在 `TradeUserFileMapper.xml` 文件中编写了对应的 `insert` SQL 语句，用于映射 `TradeUserFile` 实体类。

*   **场景五：创建校验接口**（画面 7-8）
    *   **描述**：讲师在 `IStockUserDao` 接口中定义了 `checkRegister` 方法，用于校验用户是否已注册。并在 `StockUserMapper.xml` 文件中编写了对应的 `checkRegister` 查询语句，用于根据用户编号、邮箱或手机号查询用户。

*   **场景六：创建公司信息接口**（画面 9-10）
    *   **描述**：讲师在 `IStockUserDao` 接口中定义了 `getCompanyVoById` 方法，用于根据公司 ID 获取公司对象。并在 `StockUserMapper.xml` 文件中编写了对应的 `getCompanyVoById` 查询语句，用于查询 `t_company` 表中的公司信息。

*
