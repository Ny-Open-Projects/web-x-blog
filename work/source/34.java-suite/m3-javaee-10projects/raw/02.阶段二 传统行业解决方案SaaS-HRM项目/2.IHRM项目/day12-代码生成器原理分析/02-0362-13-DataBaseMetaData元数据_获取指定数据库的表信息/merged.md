# 13-DataBaseMetaData元数据：获取指定数据库的表信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\13-DataBaseMetaData元数据：获取指定数据库的表信息_【海量资源尽在 ubkz.com】.mp4
- 时长 8分31秒（音频 511s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们刚才看到的是获取MySQL当中所有数据库它的名称那接下来呢如果说我给定你一个数据库比如说我给定你IHM那我想看一下这个数据库当中它的所有表的这些信息那又该如何去做OK其实也可以通过DatabaseMetadata来进行获取那接着我们一起来看一下获取指定数据库中的
[00:32] 表信息ETA testpublic view id test叫做03好了呢第一件事是一模一样的也是获取链接但是我们现在呢需要给定你的数据库那我们这种写法呢其实是相当于拿到了它的根没错吧那我们现在是不是继续要获取到IHRM这个数据库当中啊所以我这边呢继续要往下去写I3306
[01:04] -IHM我现在只关注于当前咱们这个IHM数据库当中OK那这样一来链接已经搞定了搞定了之后第一件事也是获取原数据好了原数据获取到了之后这边呢有一个异常我处理一下直接来一个最大范围异常OK搞定那接下来获取了原数据我们关注的就是第二项那第二项就比较简单了就是获取数据库中所有
[01:37] 表信息或许数据库中别所有了就表信息吧那这个如何去做那同样的是借助原数据Metadata它有一个方法打点叫做GetTables那需要各位注意这个GetTables呢有这么四个参数好了我点进来和各位把它拷回来咱们一起简单的来说一下这四个参数呢可能会根据你数据库
[02:10] 类型的不同它的填写方式也是不一样的那我这边呢只是以MySQL和Oracle来举例说明了对于MySQL或者Oracle来说Catalog基本上都是一模一样的其实代表的就是你当前操作的是哪一个数据库它专业名称其实就是说你操作的设计哪个目录那其实我们操作的都是这个IHRM没错吧好了那针对这个Oracle来说呢那我们Oracle操作的链接什么
[02:41] 要什么叉叉叉叉冒号比如说我们的端口要玩1那接着再来冒号我们如果习惯的就是ORCL那对于这个Kata log而言其实代表的就是当前联机的这个数据库那我们现在买Circle当中联机的数据库是IHRMHRM所以Kata log其实代表的就是IHRM那对于Oracle代表的就是ORCL能理解吧
[03:12] 好了接下来第一个参数我们说过了catalog当前操作的数据库好了接下来还有第二个第二个叫做schemer对于这个schemer其实在mycircle当中没有什么特别的意义我们可以填写一个空就可以了填写一个空但对于oracle而言oracle其实代表的是用户名称因为oracle跟mycircle它的结构不同我们之前就说过了
[03:52] Oracle这边呢它其实是根据有表空间的含义内部有表空间的含义内部还有用户的含义不同的用户可能操作的表空间是不一样的所以这边的Oracle它其实要填写用名需要注意大写OK那好了接下来第三个就是table name那这个table name指的是你要操作的表这个其实都是一样的表名表名如果是空你可以填空空代表查询所有表
[04:28] 那接下来呢如果说你可以填写的飞空飞空呢就是指查询查询就是目标表OK接着还有第三个参数第三个参数呢叫做tabstabs指的是你查询的数据库这个表的它的数据库的这个它的类型因为这个对于一个数据库它的表来说呢除了有tabletable代表的是一个真真正正的表那还有一种view别忘了叫做视图
[05:00] 能理解吧所以对于我们来说呢我们要把握的其实就是这几个参数那当然对这几个参数来说前两个Catalog和Skimmer它针对的是MySQL或者Oracle它可能有一点点细微的差别那好了我们一起来看一下如何去使用那第一个参数呢其实很简单了IHM都是一模一样的所以呢我们这边呢其实本身操作的链接就是直接定位到IHM当中了所以我这儿直接可以写空这个没问题吧OK
[05:34] 好那接下来第二个第二个参数在针对mycircle这边呢咱们也可以写空OK那接着第三个第三个我要查询哪个表我也写空当然了你写空或者写none都可以都无所谓写none那注意第三个就有问题了第三个人家接收的是一个string类型的数组所以我需要new一个string数组那如果说我只查询所有的表我就写table
[06:10] OK那这样一来得到返回值RS同样的我们去循环便利RS看一下它都有什么内容不要循环RS.nextSOTRS我们一起debug来运行一下其中某一条这个RS里面有几条数据我们来看效果走好了咱们现在已经拿到了第一条
[06:44] 那我们一起关注注意关注的是我们之前说过的叫做Fields这个东西比较多咱们慢慢找别着急FieldsOK那注意这里面现在是一共有五条数据那五条数据第一个代表的是找名称CAT Catalog其实可以理解为我当前的所属的是哪张表所属的是哪个数据库CAT Catalog代表数据库OK那好了接着第二个就是说你这张表它属于哪个数据库
[07:16] 那第二个代表着Skimmer这个Skimmer没有特殊的意义就是空了因为我们选的是空好了接着第三个TableName代表的是表的名称OK这个TableType表的这个类型OK好了继续再来Remarks表是否有一些注释那所以对于我们来说如果说要想获取你这个表究竟叫什么名称的话是我们可以rs.get我们刚才看的getSkip它叫做
[07:50] table name那个fields它其实可以通过这种k的形式获取也可以通过所有的形式获取或者直接用k的形式来做了fieldstable nameok好了这边呢我把程序全部都跑完再去执行一下大家会发现大家会发现现在所有这个库当中的表其实也已经获取到了各位来看BS等等等等什么一直到settingBS等等等等一直到setting都没问题没错吧
[08:23] 那这样一来其实我们就已经获取到了某一个库下所有表的这些数据OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库元数据信息，包括数据库连接、数据源信息、表信息等，并通过调试器查看运行时对象状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 MySQL 数据库的 schema 列表，包含多个数据库，如 information_schema、test、Spring Boot 等。
画面 2: 在 IntelliJ IDEA 中，展示 DatabaseMetaDataTest.java 文件的代码，包含 System.out.println 语句用于打印数据库用户名和是否支持事务。
画面 3: 展示 DatabaseMetaDataTest.java 文件中 init() 方法，用于建立数据库连接，配置了 MySQL 驱动、URL、用户名和密码。
画面 4: 展示 test01() 方法，用于获取数据库元数据并打印用户名和是否支持事务。
画面 5: 展示 test02() 方法，用于获取数据库中的所有库列表。
画面 6: 展示 test03() 方法，用于获取数据库中的表信息，代码中包含对 catalog、schema、tableNamePattern、types 的注释。
画面 7: 展示 test03() 方法中，对 types 数组进行赋值，设置为 {"TABLE"}。
画面 8: 调试器断点处，显示当前运行的 test03 方法，变量窗口中显示 metaData 对象和 connection 对象的属性。
画面 9: 调试器断点处，显示当前运行的 test03 方法，变量窗口中显示 metaData 对象和 connection 对象的属性。
画面 10: 调试器断点处，显示当前运行的 test03 方法，变量窗口中显示 fields 对象的属性，包括 columnLabel、columnName、columnTypeName 等。
画面 11: 调试器断点处，显示当前运行的 test03 方法，变量窗口中显示 fields 对象的属性，包括 columnLabel、columnName、columnTypeName 等。
画面 12: 调试器断点处，显示当前运行的 test03 方法，变量窗口中显示 fields 对象的属性，包括 columnLabel、columnName、columnTypeName 等。
画面 13: 展示 test03 方法运行后，控制台输出了数据库中的表名列表。
画面 14: 展示 test03 方法中，将 types 数组赋值为 {"TABLE"}，并调用 rs.getString(columnIndex) 获取表名。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
public void init() throws Exception {
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306/hrm?useUnicode=true&characterEncoding=utf8";
    String username = "root";
    String password = "111111";
    Properties props = new Properties();
    props.put("useUnicode", "true"); // 获得数据库的字符集信息
    props.put("user", username);
    props.put("password", password);
    // 1.获取连接
    Class.forName(driver); // 注册驱动
    connection = DriverManager.getConnection(url, props);
}
```

画面 4:
```java
@Test
public void test01() throws Exception {
    // 1.获取连接
    DatabaseMetaData metaData = connection.getMetaData();
    System.out.println(metaData.getUserName());
    System.out.println(metaData.supportsTransactions()); // 是否支持事务
    System.out.println(metaData.getDatabaseProductName());
}
```

画面 5:
```java
@Test
public void test02() throws Exception {
    // 1.获取连接
    DatabaseMetaData metaData = connection.getMetaData();
    // 2.获取所有的库列表
    ResultSet rs = metaData.getCatalogs();
    while (rs.next()) {
        System.out.println(rs.getString(columnIndex: 1));
    }
    rs.close();
    connection.close();
}
```

画面 6:
```java
@Test
public void test03() throws Exception {
    // 1.获取连接
    DatabaseMetaData metaData = connection.getMetaData();
    // 2.获取数据库中表信息
    metaData.getTables(
        catalog: "mysql",
        schemaPattern: null,
        tableNamePattern: null,
        types: {"TABLE"}
    );
}
```

画面 7:
```java
String[] types = {"TABLE"};
```

画面 13:
```
em_resignation
em_transferposition
em_user_company
em_user_company_jobs
pe_permission
pe_permission_api
pe_permission_menu
pe_role
pe_role_permission
pe_user
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

