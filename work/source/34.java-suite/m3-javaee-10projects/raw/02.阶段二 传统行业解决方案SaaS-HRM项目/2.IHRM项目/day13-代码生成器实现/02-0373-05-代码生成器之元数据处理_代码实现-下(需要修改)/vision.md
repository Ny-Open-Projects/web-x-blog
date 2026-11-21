# 画面线理解：05-代码生成器之元数据处理：代码实现-下（需要修改）

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\05-代码生成器之元数据处理：代码实现-下（需要修改）_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:23, 02:42, 04:12, 06:22, 06:54, 08:22, 09:09, 09:40, 10:12, 11:03, 11:39, 12:36, 13:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:57:34

1) 这一组画面整体在讲如何通过 Java 代码读取数据库元数据并生成对应的 Java 实体类结构信息。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `DataBaseMetaDataTest.java` 文件中 `test04` 方法，用于获取数据库表的元数据信息，通过 `ResultSet` 遍历列并打印列名。
画面2：展示 `DataBaseUtils.java` 文件中处理主键逻辑的代码，获取主键列名并设置到 `Table` 对象中。
画面3：展示 `DataBaseUtils.java` 文件中处理列信息的代码，创建 `Column` 对象并设置属性，同时展示 IDE 的自动补全建议。
画面4：展示 `DataBaseUtils.java` 文件中 `removePrefix` 方法，用于移除表名前缀并转换为驼峰命名。
画面5：展示 `DataBaseUtils.java` 文件中处理列信息的代码，获取列名、属性名、数据库类型并设置到 `Column` 对象。
画面6：展示 `DataBaseUtils.java` 文件中 `StringUtils` 工具类的 `containsCount` 方法，用于统计关键字出现次数。
画面7：展示 `DataBaseUtils.java` 文件中 `StringUtils` 工具类的 `toUnderscoreName` 方法，用于将驼峰命名转换为下划线命名。
画面8：展示 `DataBaseUtils.java` 文件中处理主键逻辑的代码，判断列名是否包含主键标识并设置主键属性。
画面9：展示 `DataBaseUtils.java` 文件中处理列信息的代码，设置列名、属性名、数据库类型和备注。
画面10：展示 `DataBaseUtils.java` 文件中 `main` 方法的代码，用于测试 `DataBaseUtils` 类的功能。
画面11：展示 `DataBaseUtils.java` 文件中 `main` 方法的代码，创建 `DataBase` 对象并调用 `getDBInfo` 方法获取数据库表信息。
画面12：展示 `DataBaseUtils.java` 文件中 `main` 方法的代码，设置数据库连接参数并调用 `getDBInfo` 方法。
画面13：展示 `DataBaseUtils.java` 文件中 `main` 方法的代码，打印获取到的数据库表信息。
画面14：展示 `DataBaseUtils.java` 文件中 `main` 方法的代码，打印获取到的数据库表信息，包含表名、列名、类型、备注等详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//获取指定表中的字段信息
@Test
public void test04() throws Exception {
    DatabaseMetaData metaData = connection.getMetaData();

    //获取表中的字段信息
    /*
    * catalog
    * schema
    * tableName
    * columnName
    */
    ResultSet rs = metaData.getColumns(catalog: null, schemaPattern: null, tableNamePattern: "bo_user", columnNamePattern: null);

    while (rs.next()) {
        System.out.println(rs.getString("COLUMN_NAME"));
    }
}
```

画面2：
```java
String className = removePrefix(tableName);
//主键
ResultSet primaryKeys = metaData.getPrimaryKeys(catalog: null, schema: null, tableName);
String keys = "";
while (primaryKeys.next()) {
    String keyname = primaryKeys.getString("COLUMN_NAME");
    keys += keyname + ",";
}
tab.setTableName(tableName);
tab.setTableName2(className);
tab.setComment(remarks);
tab.setKey(keys);
//处理表中的所有字段
ResultSet columns = metaData.getColumns(catalog: null, schemaPattern: null, tableName, columnNamePattern: null);
List<Column> columnList = new ArrayList<>();
while (columns.next()) {
    Column cn = new Column();
    //列名
    String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
    //属性名
    String attName = StringUtils.toJavaVariableName(columnName);
    //java类型
    String javaType = PropertiesUtils.customMap.get(dbType);
    //备注
    String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
    //是否主键
    if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
        //主键
        cn.setColumnType("PRI");
        columnList.add(cn);
    }
}
tab.setColumns(columnList);
list.add(tab);
return list;
```

画面3：
```java
//处理表中的所有字段
ResultSet columns = metaData.getColumns(catalog: null, schemaPattern: null, tableName, columnNamePattern: null);
List<Column> columnList = new ArrayList<>();
while (columns.next()) {
    Column cn = new Column();
    //列名
    String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
    //属性名
    String attName = StringUtils.toJavaVariableName(columnName);
    //java类型
    String javaType = PropertiesUtils.customMap.get(dbType);
    //备注
    String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
    //是否主键
    if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
        //主键
        cn.setColumnType("PRI");
        columnList.add(cn);
    }
}
tab.setColumns(columnList);
list.add(tab);
return list;
```

画面4：
```java
public static String removePrefix(String tableName) {
    String prefix = PropertiesUtils.customMap.get("tableRemovePrefixes");
    //bs_ tb_ //bs_user
    String temp = tableName;
    for(String pf : prefix.split(regexp: ",")) {
        temp = StringUtils.removePrefix(temp,pf, ignoreCase: true);
    }
    return StringUtils.makeAllWordFirstLetterUpperCase(temp);
}
```

画面5：
```java
//列名
String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
//属性名
String attName = StringUtils.toJavaVariableName(columnName);
//java类型
String javaType = PropertiesUtils.customMap.get(dbType);
//备注
String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
//是否主键
if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
    //主键
    cn.setColumnType("PRI");
    columnList.add(cn);
}
```

画面6：
```java
//列名
String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
//属性名
String attName = StringUtils.toJavaVariableName(columnName);
//java类型
String javaType = PropertiesUtils.customMap.get(dbType);
//备注
String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
//是否主键
if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
    //主键
    cn.setColumnType("PRI");
    columnList.add(cn);
}
```

画面7：
```java
//列名
String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
//属性名
String attName = StringUtils.toJavaVariableName(columnName);
//java类型
String javaType = PropertiesUtils.customMap.get(dbType);
//备注
String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
//是否主键
if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
    //主键
    cn.setColumnType("PRI");
    columnList.add(cn);
}
```

画面8：
```java
//列名
String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
//属性名
String attName = StringUtils.toJavaVariableName(columnName);
//java类型
String javaType = PropertiesUtils.customMap.get(dbType);
//备注
String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
//是否主键
if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
    //主键
    cn.setColumnType("PRI");
    columnList.add(cn);
}
```

画面9：
```java
//列名
String columnName = columns.getString("COLUMN_NAME"); //user_id user_id, create_time createTime
//属性名
String attName = StringUtils.toJavaVariableName(columnName);
//java类型
String javaType = PropertiesUtils.customMap.get(dbType);
//备注
String columnRemark = columns.getString("REMARKS"); //VARCHAR,DATETIME
//是否主键
if (StringUtils.contains(keys.split(regexp: ""), columnName)) {
    //主键
    cn.setColumnType("PRI");
    columnList.add(cn);
}
```

画面10：
```java
public static void main(String[] args) {
    DataBase db = new DataBase();
    DataBaseUtils.getDBInfo(db);
}
```

画面11：
```java
public static void main(String[] args) throws Exception {
    DataBase db = new DataBase(dbType: "MYSQL");
    List<Table> dbInfo = DataBaseUtils.getDBInfo(db);
    for (Table table : dbInfo) {
        System.out.println(table);
    }
}
```

画面12：
```java
public static void main(String[] args) throws Exception {
    DataBase db = new DataBase(dbType: "MYSQL");
    List<Table> dbInfo = DataBaseUtils.getDBInfo(db);
    for (Table table : dbInfo) {
        System.out.println(table);
    }
}
```

画面13：
```java
public static void main(String[] args) throws Exception {
    DataBase db = new DataBase(dbType: "MYSQL");
    List<Table> dbInfo =
