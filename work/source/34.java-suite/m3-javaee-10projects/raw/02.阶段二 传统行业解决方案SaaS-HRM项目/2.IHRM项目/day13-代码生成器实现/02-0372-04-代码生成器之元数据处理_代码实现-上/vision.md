# 画面线理解：04-代码生成器之元数据处理：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\04-代码生成器之元数据处理：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:06, 02:07, 03:09, 04:14, 05:45, 06:52, 07:40, 09:31, 10:23, 11:07, 12:00, 13:09, 13:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:56:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中通过 JDBC 获取数据库元数据，包括获取数据库中的所有表及其字段信息，并实现表名前缀移除功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `getSchemas` 方法，用于获取数据库中的所有模式（catalogs）。
画面 2: 展示 `getDbInfo` 方法，用于获取数据库中的所有表信息。
画面 3: 在 `getDbInfo` 方法中，调用 `ResultSet` 的 `next()` 方法遍历表。
画面 4: 在 `getDbInfo` 方法中，创建 `Table` 对象并赋值。
画面 5: 在 `getDbInfo` 方法中，为 `Table` 对象设置表名。
画面 6: 在 `getDbInfo` 方法中，为 `Table` 对象设置表注释。
画面 7: 查看 `typeConverter.properties` 配置文件，定义了数据库类型与 Java 类型的映射关系。
画面 8: 在 `removePrefix` 方法中，使用 `PropertiesUtils.customMap` 获取配置。
画面 9: 在 `removePrefix` 方法中，使用 `StringUtils.removePrefix` 移除前缀。
画面 10: 在 `removePrefix` 方法中，使用 `StringUtils.split` 拆分前缀。
画面 11: 查看 `DatabaseMetaData` 类的 JavaDoc，了解 `getPrimaryKeys` 方法的用途。
画面 12: 在 `getDbInfo` 方法中，调用 `getPrimaryKeys` 获取主键信息。
画面 13: 在 `getDbInfo` 方法中，为 `Table` 对象设置主键名。
画面 14: 在 `getDbInfo` 方法中，为 `Table` 对象设置主键注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public static List<String> getSchemas(Database db) throws Exception {
    //1.获取连接
    Connection connection = getConnection(db);
    //2.获取所有的连接类
    DatabaseMetaData metaData = connection.getMetaData();
    //3.获取所有的数据库
    ResultSet rs = metaData.getCatalogs();
    List<String> list = new ArrayList<>();
    while (rs.next()) {
        list.add(rs.getString(columnIndex));
    }
    rs.close();
    connection.close();
    return list;
}
```

画面 2:
```java
/**
 * 获取数据库中的表和字段构造实体类
 * Table对象
 * 1.参数
 * DataBase 数据库对象
 * 2.操作步骤
 * 1.获取连接
 * 2.获取databasemetadata
 * 3.获取当前数据库中的所有表
 * 4.获取每个表中的所有字段
 * 5.创建java对象即可
 */
public static List<Table> getDbInfo(Database db) throws Exception {
    //1.获取连接
    Connection connection = getConnection(db);
    //2.获取元数据
    DatabaseMetaData metaData = connection.getMetaData();
    //3.获取当前数据库中的所有表
    ResultSet tables = metaData.getTables(catalog: null, schemaPattern: null, tableNamePattern: null, new String[]{"TABLE"});
    List<Table> list = new ArrayList<>();
    while (tables.next()) {
        Table tab = new Table();
        //1.表名
        String tableName = tables.getString(columnLabel: "TABLE_NAME"); //bs_user User
        //2.表注释
        String remarks = tables.getString(columnLabel: "REMARKS");
        //3.主键
        ResultSet primaryKeys = metaData.getPrimaryKeys(catalog: null, schema: null, tableName);
        String keys = "";
        while (primaryKeys.next()) {
            String keyname = primaryKeys.getString(columnLabel: "COLUMN_NAME");
            keys += keyname + ",";
        }
        tab.setTableName(tableName);
        tab.setClassName(removePrefix(tableName));
        tab.setRemarks(remarks);
        tab.setKeys(keys);
        list.add(tab);
    }
    return list;
}
```

画面 3:
```java
while (tables.next()) {
    Table tab = new Table();
    //1.表名
    String tableName = tables.getString(columnLabel: "TABLE_NAME"); //bs_user User
    //2.表注释
    String remarks = tables.getString(columnLabel: "REMARKS");
    //3.主键
    ResultSet primaryKeys = metaData.getPrimaryKeys(catalog: null, schema: null, tableName);
    String keys = "";
    while (primaryKeys.next()) {
        String keyname = primaryKeys.getString(columnLabel: "COLUMN_NAME");
        keys += keyname + ",";
    }
    tab.setTableName(tableName);
    tab.setClassName(removePrefix(tableName));
    tab.setRemarks(remarks);
    tab.setKeys(keys);
    list.add(tab);
}
```

画面 4:
```java
public static String removePrefix(String tableName) {
    String prefix = PropertiesUtils.customMap.get("tableRemovePrefixes");
    //bs_ tb_ co_ bs
    String temp = tableName;
    for (String pf : prefix.split(",")) {
        temp = StringUtils.removePrefix(temp, pf, ignoreCase: true);
    }
    return StringUtils.makeAllWordFirstLetterUppercase(temp);
}
```

画面 5:
```java
#SQL类型和java类型映射规则
1. VARCHAR-String
2. BIGINT-Long
3. INT-Integer
4. DATE-java.util.Date
5. DATETIME-java.util.Date
6. DOUBLE-Double
7. TEXT-String
8. VARCHAR2-String
9. NVARCHAR2-String
10. NUMBER-Long
11. CHAR-String
12. #Table的前缀或者后缀
tableRemovePrefixes="bs_,tb_,co_,bs"
```

画面 6:
```java
public static String removePrefix(String tableName) {
    String prefix = PropertiesUtils.customMap.get("tableRemovePrefixes");
    //bs_ tb_ co_ bs
    String temp = tableName;
    for (String pf : prefix.split(",")) {
        temp = StringUtils.removePrefix(temp, pf, ignoreCase: true);
    }
    return StringUtils.makeAllWordFirstLetterUppercase(temp);
}
```

画面 7:
```java
/**
 * Retrieves a description of the primary key columns that are
 * referenced by the given table's foreign key columns (the primary keys
 * imported by a table). They are ordered by PKTABLE_CAT,
 * PKTABLE_SCHEMA, PKTABLE_NAME, and KEY_SEQ.
 * <p>Each primary key column description has the following columns:
 * <UL>
 * <LI>PKTABLE_CAT (String) primary key table catalog
 * being imported (may be <code>null</code>)
 * <LI>PKTABLE_SCHEMA (String) primary key table schema
 * being imported (may be <code>null</code>)
 * <LI>PKTABLE_NAME (String) primary key table name
 * being imported
 * <LI>PKCOLUMN_NAME (String) primary key column name
 * being imported
 * </UL>
 */
ResultSet getPrimaryKeys(String catalog, String schema, String table) throws SQLException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
