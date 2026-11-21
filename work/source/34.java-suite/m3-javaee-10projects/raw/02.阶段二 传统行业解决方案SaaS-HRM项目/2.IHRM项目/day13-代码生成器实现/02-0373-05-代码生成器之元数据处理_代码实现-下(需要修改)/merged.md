# 05-代码生成器之元数据处理：代码实现-下（需要修改）

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\05-代码生成器之元数据处理：代码实现-下（需要修改）_【海量资源尽在 ubkz.com】.mp4
- 时长 13分55秒（音频 836s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那对于处理表中的所有字段这个呢也是不难我们之前也玩过可以一起来看一下我们之前写的那么之前呢就是通过metadata.getColumns这种方式去查询某一个表当中的所有字段所以我把这一段呢直接Ctrl Ccopy到这边Ctrl V那这边这回这个表名就不能写的叫做BSUser那我们这边是不是通过刚才解析出的table name来进行获取啊
[00:29] 好了那这样一来我们获取了所有的字段的这些内容c-u-l-u-m-nc-u-l-u-m-n-s好了那接下来我们可以要做同样的就是多层负好循环的线套columns打点next好了那这样一来那这样一来一个表当中我们都知道有很多的列那每一列我们都要封装成一个column对象
[01:00] 那这个column对象组成一个list集合要存到table当中这个各位应该都没问题吧所以这边呢也来一个columnlist等于new一个arraylist好了那接下来呢开始往里存放放序环每一列代表一个column对象new一个column好了为了不报错columnlist打点addcn
[01:33] 那接下来table打点set columns把这个column list是不是存放进来我先把大的结构写出来没错吧那接下来我们关注的是不是就是中间这一部分构造column对象这个各位应该也都能接受好了那接下来我们关注构造column对象那column对象里面就有什么列名那抽象成的属性名有扎挖类型
[02:13] 列的数据库类型有备注以及是否主件那针对这几个咱们先来看列名称那对于列名称这个比较简单我们之前自己玩过直接通过RS对象获取一个叫做column name的一个属性OK那这样一来我的column name就有了好了列名称有了那我们接下来是不是要构造这座属性名死郡这个呢属性名ATTRIATT吧
[02:56] 那属性名称呢其实是根据列名称获取而来的那我们都知道列名称比如说会有user小写ID比如说还有比如说呢creator小写tim等等那这些内容我们封装到属性名称的时候比如说user ID咱们一般改成小写user大写ID这边creatortim没错吧它有一个这么字符串的一个处理过程那这个字符串的处理过程我其实也把它封装到一个
[03:27] 简单的工具类里面了就是StringUtils打点叫做to.toJavaValue就是来一个Java的变量类型好了把column直接传递过来就可以了好了那这样一来属性名我已经有了我们已经把属性和列名已经搞定了接下来呢关注的就是继续往下看就是它的Java类型和数据库的这个类型好了这边就是Java
[04:01] 类型和数据库类型那对于乍玩类型和数据库类型如何去做呢咱们都知道对于数据库类型来说呢其实获取起来比较简单好了比如说呢就来一个死菌类型的啊coludb type吧db type那对于这个type我们可以通过columns得到打点getter死菌好了这回呢拿到的就叫做time name那我这个time name拿到的其实代表的就是比如说var char
[04:34] 或者是比如说呢datatab那这些内容注意各位应该似曾相识我这边有个叫做tabconvert.property那各位来看是不是就代表的是它的key的名称啊那这边其实代表的就是我们数据库circle类型和java类型的一个替换规则那前边代表的数据库类型circle类型的后面专门是它的替换规则如果说如果说
[05:00] 你用的这个类型更加特殊一些你这边也需要把它给我替换过来应该能明白意思没错因为我们要用到这里面的内容好了对于这个Property内容我们已经把它放到一个Map集合里所以我们接下来就可以通过Properties Cast Map打点Get DB Tab的形式去获取到我们的Java TabOK这样一来这两个类型咱们也有了接下来
[05:32] 关注的就是备注和它的是否主见备注是否主见那对于备注而言这个就更简单了columns同样跟这个代表的是一模一样只不过呢这回不叫做什么type name这回叫做remark那这样一来我们的备注也已经有了就叫做columnsremarkok
[06:16] 那接着关注一下是否主见那其实这个是否主见呢我们这边已经把它放到了一个叫做kiss这么一个字符串当中了还有印象吧那对于这个字符串来说呢我们底下可以做一个判断if叫做kiss点split通过逗号进行拆分点抱歉我这边应该借助于工具类死菌utils打点contains
[06:58] 这是我写好的工具类主要就是用来判断他们之间的关系是否有匹配关系的那我需要把这个所有的主件字符串拆分成数组那拆分成数组前面呢把我们这个列名传递过来那这样一来呢其实他就要做一个判断了那这个是我自己写好的工具类就是做判断好了那接下来各位来看他的主要目的呢其实就是说
[07:27] 判断一下当前这个主件的述数当中是否包含当前这个他的名称那如果包含的话如果包含的话我就可以在上面定一个死郡PRI primary好了等于一个空如果包含等于primaryOK那这样一来我这个基本的属性处理咱们就已经都搞定了剩下的事情cn打点一个一个set进去即可好了比如说呢可以set
[08:08] Name一个还有这回呢setName2两个继续cn.set这回呢就是dbtype好了cn.setcolumn typejava type传递过去好了接着cn.set备注拿过来cn.set
[08:50] 好了把pri放进去OK那这样一来呢我们这个列也都读取完成了好了那我们当前的这个方法呢都写的差不多了但是最后千万别忘了由于我开启了链接开启了很多的这些资源所以我这边呢有必要对这些资源做一个最后的关闭的一个操作好了当我这边columns循环完成的话我需要columns打点close
[09:23] 好了到这这边的tables也需要做一个close的操作好了同样的我这个connection打点也要做close操作那这样一来我这块代码就已经写好了那这块代码写好了之后我们可以写一个mint方法一起来做一个测试看一下效果OK好了这边呢我call一下dbuttos打点get dbinfo
[10:03] 好了呢这个db info里面呢需要我们构造data base db等于new一个data base那我这个data base里面写了很多个构造方法很多个构造方法那我就以这个构造方法为例去使用一把OK传递的叫做my circlemy circleOK那好了把db传递进去好了得到列表ITR
[10:53] 放循环底下sot打印每一个table那当然了我这个table呢还需要给它构造它的图死性方法这样看的更加直观一些column也加上图死性方法我们一起来试一下效果究竟如何OK在这边走我这边报了一个错误啊是我实在太粗心了就是database只是创建了一个对象那这个对象里面需要打点set
[11:38] 很多的值啊很多的值好了我不用这个勾到方法了这个看起来不太好啊还有一个死君DB我要查询的是哪一个数据库比如说我能这样的查询IHRM这个数据库IHRM数据库好了那接下来呢指定它的userName比如说我的userName叫做rootDB.setPassword我的用户名密码OK那这样一来我数据库的所有内容都已经构造好了那我再来做一个测试看一下效果
[12:11] 走各位来看这样一来其实已经把我这个表里面的内容给我打印出来了比如说我这边bsuser转化成bsusercontinent这边也有column id叫做id死菌类型这个太长了这个太长了挖叉什么column spore的id是否主件也有底下的里面有相应的
[12:43] 咱们要处理的所有内容那这样一来我这边是不是所有的内容咱们都已经处理了没错吧OK那这样一来其实我们就已经通过了一个DatabaseUtils把我们相应要处理的内容全部都已经给它搞定了但是各位仔细去看这个输出其中有一项好像有点不太对劲我们都知道对于数据库这个对象table对象而言Name表名称Name2是处理后的我们叫做实体类名称了
[13:17] 类名称那实体类名称BS user这边呢就应该叫做CT才对因为我们这边加过一个处理是把BS下滑线替换掉了这边问题解决了在这就我这边习惯的写了一双引号各位这个写错了咱们一起再来替换一下看一下效果还是闷方法走看一下是否能处理掉注意观察BS替换成CTBS替换成A没错
[13:47] 这回就已经把我们的所有数据就已经全部都加载出来封装到对象当中了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

