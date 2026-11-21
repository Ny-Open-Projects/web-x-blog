# 画面线理解：14-DataBaseMetaData元数据：获取指定数据库表中的字段属性

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\14-DataBaseMetaData元数据：获取指定数据库表中的字段属性_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:48, 01:54, 02:20, 02:57, 03:53, 04:08, 04:26, 05:03, 05:28, 05:52, 06:23, 06:51, 07:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:50:03

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
