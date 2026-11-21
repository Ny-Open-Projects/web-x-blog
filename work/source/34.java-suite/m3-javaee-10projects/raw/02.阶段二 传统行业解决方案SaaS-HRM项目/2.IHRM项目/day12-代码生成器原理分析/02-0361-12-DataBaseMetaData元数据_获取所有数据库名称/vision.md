# 画面线理解：12-DataBaseMetaData元数据：获取所有数据库名称

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\12-DataBaseMetaData元数据：获取所有数据库名称_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:42, 00:55, 01:12, 01:28, 01:46, 02:20, 02:39, 02:54, 03:19, 03:26, 03:40, 04:08, 04:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:48:42

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库的基本信息和数据库列表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 DatabaseMetaDataTest 中的 test01 方法，用于获取数据库基本信息，包括驱动、URL、用户名、密码，并通过 DriverManager 获取连接，再调用 connection.getMetaData() 获取 DatabaseMetaData 对象，最后打印数据库用户名、是否支持事务、数据库产品名。
画面2：展示在 SQLyog 中查看数据库列表，弹出的数据库列表包含多个数据库名，如 information_schema、test、mysql 等。
画面3：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.supportsTransactions()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面4：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面5：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面6：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面7：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面8：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面9：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面10：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面11：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面12：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面13：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面14：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
/**
 * 获取数据库基本信息
 */
@Test
public void test01() throws Exception {
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306?useUnicode=true&characterEncoding=utf8";
    String username = "root";
    String password = "111111";

    Properties props = new Properties();
    props.put("remarksReporting", "true"); //获取数据库的备注信息
    props.put("user", username);
    props.put("password", password);

    //1.获取连接
    Class.forName(driver); //注册驱动
    Connection connection = DriverManager.getConnection(url, props);

    //2.获取元数据
    DatabaseMetaData metaData = connection.getMetaData();

    //3.获取数据库基本信息
    System.out.println(metaData.getUserName()); //是否支持事务
    System.out.println(metaData.supportsTransactions()); //是否支持事务
    System.out.println(metaData.getDatabaseProductName()); //数据库产品名
}
```

画面2：
无代码，仅展示数据库列表。

画面3：
无代码，仅展示 IDE 提示。

画面4：
无代码，仅展示 IDE 提示。

画面5：
无代码，仅展示 IDE 提示。

画面6：
无代码，仅展示 IDE 提示。

画面7：
无代码，仅展示 IDE 提示。

画面8：
无代码，仅展示 IDE 提示。

画面9：
无代码，仅展示 IDE 提示。

画面10：
无代码，仅展示 IDE 提示。

画面11：
无代码，仅展示 IDE 提示。

画面12：
无代码，仅展示 IDE 提示。

画面13：
无代码，仅展示 IDE 提示。

画面14：
无代码，仅展示 IDE 提示。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
