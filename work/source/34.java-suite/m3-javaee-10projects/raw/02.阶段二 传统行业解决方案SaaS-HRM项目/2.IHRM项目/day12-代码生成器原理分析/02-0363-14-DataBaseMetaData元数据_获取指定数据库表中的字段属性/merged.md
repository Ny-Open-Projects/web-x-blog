# 14-DataBaseMetaData元数据：获取指定数据库表中的字段属性

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\14-DataBaseMetaData元数据：获取指定数据库表中的字段属性_【海量资源尽在 ubkz.com】.mp4
- 时长 7分18秒（音频 438s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们刚才简单的看了一下通过数据库获取表的这些信息那其实除了获取表信息之外呢还能够获取什么呢就是指定的某一个表里面的所有字段那指定的某一个表的所有字段那我们接下来一起来看一下如何去做就是获取指定表中的字段信息OKETA testpublic我从上面把这个抄一下吧好了04
[00:36] 04OK当然我这个操作过程呢基本上都是一模一样的好了首先第一件事也是通过连接获取到我们的原数据OK那原数据获取到了之后接下来根据原数据又要去做第二件事就是获取我们的表中的获取表中的字段信息
[01:06] 信息ok 那这一步呢其实也比较简单也是通过 metal data 里面的方法来做的metal data 打点 getc u l u m n columnsget columns这个方法就是去获取我们数据库表当中的全部的我们自断的一些内容ok 我们可以一起来看一下它的一些参数把这四个参数呢我也给它拿过来control ccopy 过来我们一起简单的来看一下首先呢第一个 catalog第二个
[01:39] 我习惯就叫Skimmer了第三个TableNameOK第四个ColumnName那这个其实不难其实比较简单其中呢跟刚才一样Catalog跟SkimmerCatalog其实指的是你要操作的是哪一个数据库MySQL呢咱们比如说呢你操作的是哪个跟你的连接有关系我们的连接是IHM所以操作的就是我们这个IHM数据库所以对于MySQL来说你可以天空
[02:12] 没问题你填IHM也没有问题OK那接着来Skimmer那对于Skimmer来说呢我们一般用那那对于如果Oracle的话写它的用户名大写就可以了OK那接着第三个TableName那对于TableName来说其实就是表的名称你要操作哪张表啊你告诉我呀那接着这个表当中的哪一列你想看一下这个表当中具体是哪一列的信息你如果呢想写它的列名比如说我要操作U的这个表
[02:41] 我想看ID那我就写ID列名列名如果你不写查所有列就这个意思能理解吧OK那好了接着我们一起来看一下catalog我们可以用空就可以了我就写None了OKSkimmer用None好了这一回我们数据库的表名注意表名BS下滑线user我就想看一下用户表
[03:04] 那我就看一下这个IHRM里面的用户表那千万别搞错了我这写的是数据库IHRM你给我搜一个其他的买Batis里面的表那显然就没有数据了没错吧所以一定要匹配上OKBS user那接下来后面这个我传一个最后一个就是你要看一下表的名称那哪个字段的名称OK那当然了最后这个是字段名字段名的话如果你填写了就拿你某一个字段的所有它的一些信息那如果你那得到所有
[03:38] 它其实就是拿到所有字段了OK那好了有了之后跟之前逻辑一样well循环我们一起来看一下RS究竟代表的什么含义来走debug抱歉没设断点好了有断点了OK那进来之后呢我们关注一下RS result set那注意关注的还是Fuse这个内容太多了这个看起来有点麻烦那先等待一下Fuse找到了
[04:11] 那首先能看到它有很多个这回一列当中的它有20多个属性那看一下信息比如说呢这边有table cat究竟属于是哪一个数据库这边还有table schema还有很多很多我们一起来找一下关注的circle data tab这个circle data tab代表的是它这个在circle里面它究竟属于哪种类型这个太多了咱们不一个一个来说了OK
[04:47] 那有的朋友说呢我就想要看一下或者想要获取到里面的某一个数据那我们应该怎么办呢那其实不难我们可以一起来参考一下就是JDK提供的一些文档那那边呢会有对它的返回值的一个说明那其实在今天资料当中呢也给各位把JDK的一个API文档给各位准备好了那可以双击打开它好了我们这边呢在搜索部分可以简单的搜索一下比如说呢我搜索的这个方法get columns
[05:17] Ctrl C拿过来Ctrl V搜索一把注意是Metal Data里面的方法OK点进来好了Ctrl F搜索那各位来看这边呢有一个Get Columns得到Result Set那点进来呢这边其实要对它返回的每一个列里面呢有说明一是刚才看到的TableCat二是什么什么这个就不跟各位一个说了那比如说我想获取到Column Name那Column Name我这边直接复制过来
[05:49] 从这边就去获取column name即可所以这边呢就是rs打点get string把这个下去了column name即可column nameok注意这边都是大写的好了那这个呢我们搞好了之后可以一起正常启动运行一下来看一下效果是不是能把这个column name代表的不就是列明吗获取到ok各位来看
[06:17] ID 毛表等等等等我数据库表里面的所有列名都已经获取到了那跟我们这边数据库基本上都是匹配的没错吧OK那如果说各位要希望获取到其他的数据类型可以从这边去一个一个去比对找一下比如说你这边想要用列的名称那就列名比如说要想用这个数据的类型那就是Data Type比如说想要什么Column Size指的是你数据数组的这个大小那就是Column Size
[06:46] 还有一些其他的内容当然了有需要哪个你就去用哪个其实就可以了OK那到目前为止呢其实我们已经把第二块内容这个原数据里面的这个数据库相关的我们就已经都说清楚了一共看到了基本的数据信息看到了能够获取所有数据库的信息可以看到获取数据库里面的某一个表的信息可以看到某一个表里面所有这么列的这些信息没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库元数据，包括获取数据库表信息和列信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Java 代码中获取数据库元数据的 `test03` 方法。
- 代码注释说明了 `catalog`、`schema`、`tableNamePattern`、`types` 参数的含义。
- `catalog` 示例值：mysql、oracle:xxx:1521:orcl。
- `schema` 示例值：mysql: null、oracle: 用户名（大写）。
- `tableNamePattern` 示例值：null（查询所有表）、为空（查询目标表）。
- `types` 示例值：TABLE（表）、VIEW（视图）。
- 代码调用 `metaData.getTables` 方法获取表信息。

画面2：
- 继续展示 `test03` 方法，代码执行 `rs.next()` 并打印表名。
- 代码注释说明了 `rs.getString("TABLE_NAME")` 的作用。

画面3：
- 展示了 `test04` 方法的开始部分，用于获取表的列信息。
- 代码注释说明了 `catalog`、`schema`、`tableName` 参数的含义。
- 代码调用 `metaData.getColumns` 方法获取列信息。

画面4：
- 展示了 `test03` 方法中 `schema` 参数的值，oracle 的 schema 为用户名（大写）。
- 代码注释说明了 `tableNamePattern` 和 `types` 参数的含义。

画面5：
- 展示了 `test04` 方法中调用 `metaData.getColumns` 方法的代码。
- 代码注释说明了 `catalog`、`schemaPattern`、`tableNamePattern`、`columnPattern` 参数的含义。

画面6：
- 展示了 IntelliJ IDEA 的调试器界面，显示了 `test04` 方法的执行状态。
- 调试器显示了 `test04` 方法的执行过程。

画面7：
- 展示了 `test04` 方法的调试器界面，显示了 `rs.next()` 的执行过程。
- 调试器显示了 `rs` 对象的类型为 `com.mysql.jdbc.JDBCResultSet`。

画面8：
- 展示了 `test04` 方法的调试器界面，显示了 `rs` 对象的 `fields` 字段。
- `fields` 字段显示了列的详细信息，如 `AUTO_INCREMENT_FLAG`、`NO_CACHED_INFO` 等。

画面9：
- 展示了 Windows 文件资源管理器，显示了 `ihrm` 文件夹下的 `day5` 文件夹。
- 文件夹结构显示了 `day1` 到 `day12` 的文件夹。

画面10：
- 展示了 JavaDoc 文档界面，显示了 `ResultSet` 类的 `getColumns` 方法的文档。
- 文档说明了 `getColumns` 方法的参数和返回值。

画面11：
- 展示了 `test04` 方法的调试器界面，显示了 `rs` 对象的 `fields` 字段。
- `fields` 字段显示了列的详细信息，如 `AUTO_INCREMENT_FLAG`、`NO_CACHED_INFO` 等。

画面12：
- 展示了 SQLyog 数据库管理工具界面，显示了 `bs_user` 表的数据。
- 表格显示了 `id`、`username`、`password`、`create_time` 等字段的数据。

画面13：
- 展示了 PDF 文档界面，显示了“3.2.1 概述”部分。
- 文档说明了 `DatabaseMetaData` 是由 `Connection` 对象通过 `getMetaData` 方法获取。
- 文档列出了 `DatabaseMetaData` 的常用方法，如 `getDatabaseProductName`、`getUserName`、`getURL`、`getDriverName`、`getDriverVersion`、`isReadOnly`、`supportsTransactions`。

画面14：
- 展示了 PDF 文档界面，显示了“3.2.2 入门案例”部分。
- 文档列出了 `DatabaseMetaData` 的常用方法，如 `getDatabaseProductName`、`getUserName`、`getURL`、`getDriverName`、`getDriverVersion`、`isReadOnly`、`supportsTransactions`。
- 文档显示了 Maven 依赖配置：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.6</version>
</dependency>
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.获取元数据
DatabaseMetaData metaData = connection.getMetaData();

//2.获取数据库中表信息
String catalog, String schemaPattern,String tableNamePattern, String types[]
catalog: 当前操作的数据库
mysql:
catalog
oracle:
xxx:1521:orcl
catalog
schema:
mysql:
null
oracle:
用户名（大写）
tableNamePattern:
null: 查询所有表
为空: 查询目标表
types: 类型
TABLE: 表
VIEW: 视图
```

画面2：
```java
ResultSet rs = metaData.getTables(catalog: null, schemaPattern: null, tableNamePattern: null, new String[]{"TABLE"});
while (rs.next()) {
    System.out.println(rs.getString("TABLE_NAME"));
}
```

画面3：
```java
//获取指定表中的字段信息
@Test
public void test04() throws Exception {
    DatabaseMetaData metaData = connection.getMetaData();
    //获取表中的字段信息
    //catalog
    //schema
    //tableName
    metaData.getColumns(catalog: null, nd
```

画面4：
```java
catalog:
oracle:
xxx:1521:orcl
catalog
schema:
mysql:
null
oracle:
用户名（大写）
tableNamePattern:
null: 查询所有表
为空: 查询目标表
types:
TABLE: 表
VIEW: 视图
```

画面5：
```java
//获取表中的字段信息
@Test
public void test04() throws Exception {
    DatabaseMetaData metaData = connection.getMetaData();
    //获取表中的字段信息
    //catalog
    //schemaPattern
    //tableNamePattern
    //columnPattern
    metaData.getColumns(catalog: null, nd
```

画面6：
- 无代码或配置。

画面7：
- 无代码或配置。

画面8：
- 无代码或配置。

画面9：
- 无代码或配置。

画面10：
- 无代码或配置。

画面11：
- 无代码或配置。

画面12：
- 无代码或配置。

画面13：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.6</version>
</dependency>
```

画面14：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.6</version>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
- 标题：“3.2.1 概述”
- 内容：“数据库元数据 (DatabaseMetaData) 是由 Connection 对象通过 getMetaData 方法获取而来，主要封装了对数据库本身的一些整体综合信息，例如数据库的产品名称，数据库的版本号，数据库的 URL，是否支持事务等等。”
- 列表：
  - getDatabaseProductName: 获取数据库的产品名称
  - getDatabaseProductVersion: 获取数据库的版本号
  - getUserName: 获取数据库的用户名
  - getURL: 获取数据库连接的 URL
  - getDriverName: 获取数据库的驱动名称
  - driverVersion: 获取数据库的驱动版本号
  - isReadOnly: 查看数据库是否只允许读操作
  - supportsTransactions: 查看数据库是否支持事务

画面14：
- 标题：“3.2.2 入门案例”
- 内容：“（1）构建环境”
- 列表：
  - getDatabaseProductName: 获取数据库的产品名称
  - getDatabaseProductVersion: 获取数据库的版本号
  - getUserName: 获取数据库的用户名
  - getURL: 获取数据库连接的 URL
  - getDriverName: 获取数据库的驱动名称
  - driverVersion: 获取数据库的驱动版本号
  - isReadOnly: 查看数据库是否只允许读操作
  - supportsTransactions: 查看数据库是否支持事务

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无。

