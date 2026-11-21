# 03-代码生成器之元数据处理：操作步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\03-代码生成器之元数据处理：操作步骤分析_【海量资源尽在 ubkz.com】.mp4
- 时长 6分50秒（音频 410s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们完成了自定义数据的这部分的处理那接下来就是第二部分就是原数据处理那这个原数据处理是什么含义咱们简单的再来说一下其实就是加载指定数据库里面所有表那加载表当中的每一列把这些内容给它封装到我们之前写好的table以及这个column这两个对象当中应该都能理解没错吧好了
[00:33] 那接下来我们来看一下如何去做那其实这些内容呢咱们可以把它写到我们之前配置的一个工具类里叫做Database Utils那这个Database Utils我们之前根据原数据的形式是不是得到了一个获取数据列表的这么一个操作那除了这个操作之外那接下来我们补充第二个操作那第二个操作它的主要目的就是获取获取数据库中的
[01:05] 表和字段构造实体类那构造的实体类就是构造成table对象那这个table对象我们简单的和各位再一起来看一下好了table那这个table对象里面呢有很多的属性那这一个table属性有表名有处理后的表的这个名称当然这个呢咱们可以把它理解为比如说可以把它理解为抽象成我们的实体类的这个名称其实就可以好了还有
[01:35] comment这个comment指的是表的一个注释还有key就是它的主件一个表他们都知道它有自己表的名称有抽象成Java实体类的名称这边有自己的介绍有自己的主件那千万别忘了一个表当中它还有很多的列那这些列是一个粒子集合那这每一列里面通过column的对象来抽取那这里面有column name这个列的名称
[02:02] 还有个column name 2这个其实代表的就是根据列名抽象的属性名称抽象的属性名称当然了这边还有这个列它的类型这个类型指的是我们Java类型还有一个就是数据库类型比如说呢Whatcha是不是对应成我们的Java类型就应该是死菌没错吧还有列的备注就是列的一些描述信息接着还有个column key这个column key代表的是
[02:31] 是否是主件因为对一个列来说有可能是主件有可能不是主件这个各位应该也能理解没错吧所以咱们要把数据库当中的这些内容抽象到我们的这个实体列当中OK我们一起来看一下如何去做首先我在这边配置一方法好了这个方法的名称叫什么Public注意这个方法呢咱们以工具类的形式来做就可以了Static
[02:58] list集合因为我们知道一个数据库当中它可能有很多个表所以我给你指定一个数据库你直接给我分装的是是多个table对象多个一个表代表一个table对象一个表代表一个所以我这边返回的是一个list table对象好了这个各位应该也能理解叫做get dbinfoinfo那这边你传递的参数get dbinfo好了
[03:32] 死肉我就来个死肉死吧死肉死exceptionOK把这个方法多了两个括弧啊OK好那接下来我们来看一下对于这个方法我们关注的点首先第一个它的参数究竟有什么好了第二个就是我们的操作步骤操作步骤那对于参数呢大家都应该不言而喻了那对于我们现在要借助原数据其实原数据咱们只需要想方设法的
[04:06] 获取数据库连接就可以了那获取数据库连接咱们需要用户名密码数据库的UIL和驱动而这些内容我们之前已经封装到一个Database数据库连接或者数据库配置的这么一个对象数据库对象所以在我这边需要的参数就来一个DatabaseDB即可那这个DatabaseDB是我们之前自己封装的一个对象里面有URL
[04:35] 有driver有password有username我们已经获取到了好了那获取到了之后我们来分析一下我这里面的操作步骤又应该是怎么样的那对于我这个操作步骤呢其实各位应该都有所了解那我们之前呢自己玩过原数据那原数据呢有三种有databasemetadata还有parametermetadata
[04:59] 还有我们叫做result set metadata而我们现在要查询所有数据库表的这些信息那这些信息我们是不是可以借助database也就是数据库原数据来获取啊那所以操作步骤它就应该是如下这么几步首先呢第一件事我们要获取连接那有了连接之后接下来获取database metadata印象吧这是database metadata好了有了这个之后接下来那通过
[05:31] 原数据我们直接就能够拿到所有获取当前数据库中的所有所有所有表信息那拿到所有表信息之后注意咱们继续有了表是不是就能获取到表中的所有字段了每个表中的所有字段那接下来这些都获取到了我们是不是把它封装到我们的Java对象中
[06:08] 即可这个步骤希望各位心里也有这么一个简单的印象能理解吧当然了这里面的很多个小的细节比如说获取当前数据库当中的所有表或者是获取某个表中的所有词段这些我们在之前的原数据练习过程当中原数据Database Metal Data咱们一起来看这是获取指定库中的表所有表好印象吧咱们继续往下看
[06:41] 这个获取指定某一个表的字段那这些我们之前是不是都玩过呀各位所以这个代码其实也不难

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

