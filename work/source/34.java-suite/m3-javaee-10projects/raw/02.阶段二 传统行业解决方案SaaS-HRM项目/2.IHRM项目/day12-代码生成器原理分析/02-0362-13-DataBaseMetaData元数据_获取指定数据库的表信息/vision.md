# 画面线理解：13-DataBaseMetaData元数据：获取指定数据库的表信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\13-DataBaseMetaData元数据：获取指定数据库的表信息_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:38, 01:10, 02:02, 05:23, 05:53, 06:22, 06:42, 06:51, 07:04, 07:28, 07:39, 08:12, 08:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:49:14

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库元数据信息，包括数据库连接、数据源信息、表信息等，并通过调试器查看运行时对象状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 MySQL 数据库的 schema 列表，包含多个数据库，如 information_schema、test、springboot 等。
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
