# 画面线理解：7.21 项目实战 - Druid JDBC工具类

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.21 项目实战 - Druid JDBC工具类_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:32, 00:50, 01:13, 02:20, 02:41, 03:14, 03:24, 03:36, 03:59, 04:28, 04:43, 04:53, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:51:02

1) 这一组画面整体在讲什么（一句话）：
编写一个用于获取和关闭 Apache Druid JDBC 连接的工具类 DruidHelper。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IDEA 中，右键点击项目目录，选择“Show Image Thumbnails”选项，准备查看项目结构。
画面 2: 选中并打开 `DruidHelper.java` 文件，准备编写代码。
画面 3: 在 `DruidHelper` 类中添加注释“获取Druid连接”。
画面 4: 在 `DruidHelper` 类中添加注释“关闭资源”。
画面 5: 在 `DruidHelper` 类中导入 `java.sql.Connection` 和 `java.util.Properties`。
画面 6: 在 `DruidHelper` 类中声明私有成员变量 `connection`、`url` 和 `conf`。
画面 7: 在 `DruidHelper` 类中编写 `getConnection()` 方法的开始部分。
画面 8: 在 `getConnection()` 方法中添加 `try` 块和 `catch` 块。
画面 9: 在 `try` 块中，使用 `DriverManager.getConnection(url, conf)` 获取连接。
画面 10: 在 `getConnection()` 方法中添加 `return connection;` 语句。
画面 11: 在 `DruidHelper` 类中编写 `close()` 方法的开始部分。
画面 12: 在 `close()` 方法中添加 `try` 块。
画面 13: 在 `close()` 方法中添加 `if (connection != null) connection.close();` 语句。
画面 14: 在 `close()` 方法中添加 `if (st != null) st.close();` 和 `if (rs != null) rs.close();` 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```java
import java.sql.Connection;
import java.util.Properties;
```

画面 6:
```java
public class DruidHelper {
    private Connection connection = null;
    private String url = "jdbc:avatica:remote:url=http://172.17.0.143:8888/druid/v2/sql/avatica/";
    private Properties conf = new Properties();
```

画面 7:
```java
public Connection getConnection() {
```

画面 8:
```java
public Connection getConnection() {
    try {
        if (connection == null) {
            connection = DriverManager.getConnection(url, conf);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

画面 9:
```java
public Connection getConnection() {
    try {
        if (connection == null) {
            connection = DriverManager.getConnection(url, conf);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return connection;
    }
```

画面 10:
```java
public Connection getConnection() {
    try {
        if (connection == null) {
            connection = DriverManager.getConnection(url, conf);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return connection;
    }
```

画面 11:
```java
public void close(Connection connection, Statement st, ResultSet rs) {
```

画面 12:
```java
public void close(Connection connection, Statement st, ResultSet rs) {
    try {
```

画面 13:
```java
public void close(Connection connection, Statement st, ResultSet rs) {
    try {
        if (connection != null) {
            connection.close();
        }
        if (st != null) {
            st.close();
        }
```

画面 14:
```java
public void close(Connection connection, Statement st, ResultSet rs) {
    try {
        if (connection != null) {
            connection.close();
        }
        if (st != null) {
            st.close();
        }
        if (rs != null) {
            rs.close();
        }
    }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
