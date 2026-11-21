# 04-代码生成器之元数据处理：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\04-代码生成器之元数据处理：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 时长 13分47秒（音频 828s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那好了我们就开始把这个方法当中的这些代码给它补充完整首先咱们来第一件事就是创建链接或者叫做就叫获取链接吧那获取链接比较简单我们在这个工具类当中之前就自己写好了一个获取链接的这么一个方法叫做getConnection所以呢我在这边直接getConnection把DB对象传递下去即可
[00:29] 那这样一来我的连接已经有了那有了连接直接来我们关注的就是获取原数据原数据那获取原数据Connection打点GetMetalData那这样一来我们得到的是DatabaseMetalData那MetalData我们也获取到了那接下来注意我们关注的是不是就是获取到当前这个数据库当中的锁表
[01:02] 获取当前数据库的锁表那这个步骤应该如何做借助Metal Data我们之前就玩过Metal Data打点叫做GetTables那GetTables里面有很多参数这个之前我们自己也玩过CatalogNo什么SkimmerNoTableNamePersonNo后面只关注一个是不是叫做Table即可OK那这样一来我们把之前写好的这段拷过来
[01:33] 好了那这样一来其实我们所有的内容都已经给它封装到这个RS我叫RS吧要不太长了就叫RS这个对象当中那所有表的信息咱们全部都有了那接下来注意RS看的不清楚叫Tables吧那所有表的信息都封装到Tables了那我们就可以做Val循环那Val循环TablesTablesTables
[02:07] 打点nextOK那在这个过程当中咱们开始循环每一个表那根据每一个表在当中是不是获取每一个表当中的所有列的这些内容啊没错吧那我们都知道table4一个table代表的其实这个一个数据库表代表的其实就是我们的一个table这么一个对象咱们有多个对象最终要得到一个listtable集合所以我在上边
[02:39] 为了这个程序不包错为了这个程序不包错我就先写一个array list好了接着底下给它返回好了那我们中间关注的return list那我们中间关注的就是如何在循环的过程当中构造table好了循环的过程当中构造table等于new一个table那好了底下list.add把table放进去
[03:12] 好了中间这块内容那我们应该要写什么首先第一件事第一件事我们应该把table也就是我们数据库表它所具备的抱歉应该打开table它所具备的基本信息先给它复制先复制基本的剩下这个粒子集合我们一会再搞一会再去搞这个基本集合可以吧OK那咱们先去把这几个属性给它复上值那这几个属性复制的时候首先我应该要
[03:43] 有表名称表名好了接着第二个转化的类名接着第三个我们叫做它的一些中文说明描述信息好了还有第四个第四个来看一下就是它的主件主件OK那表明如何去获取
[04:22] 咱们之前也写过这套诗里我切换过来各位发现rs.get死据这个是不是就能获取到表的名称没错吧OK那这样一来表名已经有了死据类型table name等于好了table打点get死据但是我想跟各位来交代的就是说表名已经有了那我最终是不是要把它转化为类名
[04:57] 那转化的类名我们应该如何去做呢这边各位一定一定要注意一定一定要注意我获取的表明有可能叫做BS下划线user那我这个类名就不能叫BS下划线user我们是不是想把它切换为叫做user并且首字母叫做大写呀没错吧所以我们接下来关注的就是如何去把这个类名也给我生成出来
[05:27] 好了那这一步应该如何去做呢注意我底下呢可以写一个我自己的一个小小的工具类比如说public static死菌类型好了我就叫做remove remove p-r-e-f-x什么意思呢就是要把这个表明的前缀给它替换掉或者要把它删掉那我们首先传递的有一个参数这个参数呢就比如说就叫table nameOK那我底下一起来看一下如何去做
[05:57] 其实底下这个代码写下来比较简单比较简单那我们都知道我们自己写过了一个咱们当前工程的一个配置的这么一个配置文件那这个配置文件呢叫做property私下叫做typeconvert这里面有一个叫做table reboot prefix这么一个参数那么要获取到这个参数里面其实就是我们要替换的所有前缀比如说有tb开头的那我就把tb给它替换掉比如说呢我想有bs开头的我就bs也给它进行替换掉
[06:29] 那这样一来我们先要拿到要准备替换的这个字符串那准备替换的字符串我们获取的方式比较简单已经把它封装到我们的一个PropertyUtil当中了PropertyUtil打点叫做CustomMap好了通过这里面打点Get方法获取那获取用Key直接就能获取到我们待删除的所有钱坠AppleFixOK那好了接下来呢
[07:04] 我要做的事情那table name有可能是BSK头有可能是其他的K头那还有可能有很多所以在这边我只需要对它做一个简单的字符串处理即可用一个fault循环来做那各位来看powerfix咱们拿到的有这一大堆这一大堆其实是有四部分构成所以我对这个字符串进行一个数组的处理然后一个一个的替换能理解什么意思吧
[07:30] OK那好了我们一起来看一下这个呢操作起来就比较简单了PFPORFIX打点SPLITE我用逗号分割好了那分割好了之后这边简单的说一下这边拿到了分割好了之后呢其实就是BS下滑线接着比如说有TB下滑线比如说有接着其他CO什么下滑线等等你要替换的所有都在这摆着
[08:01] 然后呢你一个一个的根据你传递的名称和这个BS一个一个的替换其实就可以了所以我这边所以我这边死菌类型的比如说我就叫一个Temt随便写的这个呢就让它等于TableName那好了接下来底下就可以一个一个的进行替换Temt等于死菌Utils这是我自己写好的一个工具类专门写了一个Remove和Fix的方法
[08:34] 这个remove perfect方法呢你直接把你要替换的字符串拿过来接着你要替换的前缀拿过来接着写一个处它就自动的一个一个去替换了当然如果你不想用我的工具你自己写一个也很简单怎么写根据你传递的这个名称比如说呢你传递的表明叫BS user那你是不是做一个最基础的字符串的一个替换处理就可以啊用一个死军的一个工具是没错吧
[09:05] OK那好了这样一来我就开始循环替换循环替换替换好了之后替换好了之后接着替换好了之后呢我们这个time等现在它其实就变成了叫做小写的youtube各位看到了那接着我们是不是要把首字母给它改成大写是不是就可以了所以接下来我return同样死菌youtube我写了一个工具类打点叫做make a word first letter
[09:39] apport case好了这个代表的含义就是将所有的首字母转化为大写那这样一来我这个工具类写好了那好了接着我们类名也就已经准备好了string class name好了那这样一来我们表名有了类名有了接着描述那描述信息呢其实我们之前呢也看过也看过那这边呢我就直接去使用它了
[10:14] 同样的也是通过我们的RS对象来获取的tables打点打点get打点get string好了这里面装的是什么呢咱们就通过这个fields叫做remarksremarksremarks来获取string好了我们这边叫做remarksok
[10:47] 好了那接着还有一个主件那对于主件的处理对于主件处理呢其实直接呢可以通过metadata来获取metadata打点打点它叫做get tables哎错了叫做get primary keys那各位来看一下这个方法有catalog有schemer还有一个叫做tabletable指的是你当前那个表的名称它指的是通过这一个表获取表中的主件那前面catalog
[11:19] 和Skimmer都跟我们之前获取Table一样全部为空为None即可那我们的TableName这边也获取到了TableNameOK那这样一来得到的就是这么一个PremaryKeys好了那接下来呢我们要做的事情同样的也这边做一个iterAvail的一个循环PremaryKeys点叫做Next好了那对于这里面的内容
[11:50] 那如何进行处理呢其实比较简单了死菌类型比如说就叫KISS等于来一逗号来一逗号那接着我这里面存放需要各位注意的是有可能你一个表里面的主件它是复合主件也就是有多个那有多个的情况抱歉逗号多了那如果有多个的情况下我其实就把多个的主件给它拼接到一个字符串里面再存到我这个table里面其实就可以了所以接下来呢我这里面
[12:22] 要写的就是去循环获取每一个主件它的列名Promptly case打点getter死郡要获取这个列名列名呢叫做column小线name死郡比如说呢这边叫做死郡key name就等于好了那接下来case加等于key namesOK那这样一来case我们也获取到了
[12:58] 获取到了之后最后要做的事情一个一个的set到table当中table打点set name1表明table打点set name2class nameOK好了table打点set comment把那remark存进去以及最后一个table打点set key
[13:30] 好了我们的case那这样一来我们table相应的处理就已经都搞定了那这个搞定了之后底下我们关注的是不是就是处理表中的所有字段

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

