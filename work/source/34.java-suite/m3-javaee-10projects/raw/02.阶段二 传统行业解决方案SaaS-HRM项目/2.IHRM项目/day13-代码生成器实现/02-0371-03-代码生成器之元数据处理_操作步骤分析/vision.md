# 画面线理解：03-代码生成器之元数据处理：操作步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\03-代码生成器之元数据处理：操作步骤分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:21, 00:33, 00:45, 01:16, 01:20, 02:42, 02:59, 03:35, 04:15, 04:39, 06:12, 06:35, 06:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:55:44

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码连接数据库，获取数据库元数据（表和字段信息），并将其映射为 Java 实体类（Table 和 Column）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前章节为“1.3 元数据处理”，并显示了获取数据库表信息的 Java 代码片段。
画面2：展示数据库表结构，当前选中表为“bi_city”，并显示了表的字段信息。
画面3：展示实体类 Column 的 Java 代码，定义了列名、类型、注释等属性及 getter/setter 方法。
画面4：展示工具类 DataBaseUtils.java 中的 getSchemas 方法，用于获取数据库的 schema 列表。
画面5：展示 DataBaseUtils.java 中的 getSchemas 方法，注释说明了其功能。
画面6：展示实体类 Table 的 Java 代码，定义了表名、别名、注释、主键和列集合等属性及 getter/setter 方法。
画面7：展示数据库表结构，当前选中表为“bi_city”，并显示了表的字段信息。
画面8：在 DataBaseUtils.java 中，光标位于 getSchemas 方法末尾，IDE 提示需要添加返回值类型。
画面9：在 DataBaseUtils.java 中，光标位于 getSchemas 方法末尾，IDE 提示需要添加返回值类型。
画面10：在 DataBaseUtils.java 中，光标位于 getDbInfo 方法的注释部分，准备编写方法实现。
画面11：在 DataBaseUtils.java 中，光标位于 getDbInfo 方法的注释部分，准备编写方法实现。
画面12：在 DataBaseUtils.java 中，光标位于 getDbInfo 方法的注释部分，准备编写方法实现。
画面13：在 DataBaseMetaDataTest.java 中，展示获取数据库元数据的代码，包括 catalog、schema、tableNamePattern 和 types 的定义。
画面14：在 DataBaseUtils.java 中，光标位于 getDbInfo 方法的注释部分，准备编写方法实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 获得表及字段信息
 */
public static List<Table> getDbInfo(Database db,String tableNamePattern) throws
Exception {
//创建连接
Connection connection = getConnection(db.getDriver(),db.getUsername(),
db.getPassword(), db.getURL());
//获取元数据
DatabaseMetaData metaData = connection.getMetaData();
//获取所有的数据库表信息
ResultSet tablers = metaData.getTables(null, null, tableNamePattern, new
String[]{"TABLE"});
List<table> list=new ArrayList<table>();
//拼装table
while(tablers.next()) {
Table table = new Table();
```

画面3：
```java
package cn.itcast.generate.entity;
/**
 * 列对象
 */
public class Column {
private String columnName;//列名
private String columnName2;//外名称(处理后的列名称)
private String columnType;//列的类型
private String columnComment;//列的注释
private String columnKey;//是否主键
```

画面4：
```java
public static List<String> getSchemas(Database db) throws Exception {
//获取元数据
Connection connection = getConnection(db);
DatabaseMetaData metaData = connection.getMetaData();
//获取所有的库名列表
ResultSet rs = metaData.getCatalogs();
List<String> list = new ArrayList<>();
while (rs.next()) {
list.add(rs.getString(1));
}
rs.close();
connection.close();
return list;
}
```

画面5：
```java
public static List<String> getSchemas(Database db) throws Exception {
//获取元数据
Connection connection = getConnection(db);
DatabaseMetaData metaData = connection.getMetaData();
//获取所有的库名列表
ResultSet rs = metaData.getCatalogs();
List<String> list = new ArrayList<>();
while (rs.next()) {
list.add(rs.getString(columnindex: 1));
}
rs.close();
connection.close();
return list;
}
```

画面6：
```java
/**
 * 表实体
 */
public class Table {
private String name;//表名
private String name2;//处理后的表名
private String comment;//表注释
private String key;//主键
private List<Column> columns;//列集合
```

画面8：
```java
public static List<String> getSchemas(Database db) throws Exception {
//获取元数据
Connection connection = getConnection(db);
DatabaseMetaData metaData = connection.getMetaData();
//获取所有的库名列表
ResultSet rs = metaData.getCatalogs();
List<String> list = new ArrayList<>();
while (rs.next()) {
list.add(rs.getString(columnindex: 1));
}
rs.close();
connection.close();
return list;
}
```

画面9：
```java
public static List<String> getSchemas(Database db) throws Exception {
//获取元数据
Connection connection = getConnection(db);
DatabaseMetaData metaData = connection.getMetaData();
//获取所有的库名列表
ResultSet rs = metaData.getCatalogs();
List<String> list = new ArrayList<>();
while (rs.next()) {
list.add(rs.getString(columnindex: 1));
}
rs.close();
connection.close();
return list;
}
```

画面10：
```java
/**
 * 获取数据库中的表和字段构造实体类
 * Table对象
 */
public static List<Table> getDbInfo(Database db) throws Exception {
```

画面11：
```java
/**
 * 获取数据库中的表和字段构造实体类
 * Table对象
 */
public static List<Table> getDbInfo(Database db) throws Exception {
```

画面12：
```java
/**
 * 获取数据库中的表和字段构造实体类
 * Table对象
 */
public static List<Table> getDbInfo(Database db) throws Exception {
```

画面13：
```java
/**
 * 获取数据库元数据
 */
String catalog, String schemaPattern,String tableNamePattern, String types[]
catalog:当前操作的数据库
mysql
illum
catalog
oracle
xxx:1521:orcl
catalog
schema:
mysql:
null
oracle:
null
tableNamePattern:
null:查询所有表
为空:查询所有表
types:类型
TABLE:表
VIEW:视图
```

画面14：
```java
/**
 * 获取数据库中的表和字段构造实体类
 * Table对象
 */
public static List<Table> getDbInfo(Database db) throws Exception {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
