# 7.21 项目实战 - Druid JDBC工具类

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.21 项目实战 - Druid JDBC工具类_【海量资源尽在 666java.com】.mp4
- 时长 5分36秒（音频 336s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来开发我们的这个Dread helper也就是说我们Avetica gdbc它的一个工具类那么我们先创建我们的这个package在我们comment里边然后呢创建我们的Avetica的一个Dread helper那么这个Dread helper呢其实就是啊发起Dread的gdbc
[00:34] 工具类我们这个工具类那么这个工具类呢包括了我们几个啊这种方法第一个方法来讲的话直接上是说我们的一个啊获得对的连接那第二个来讲的话是我们要把关闭关闭资源这是我们基本的两个方法那第一个方法获得获得连接获得连接的话我们就需要定义我们的这个private的
[01:07] 我们的一个connection这种connection的话我们定义connection等于空另外的话我们还需要定义我们的一个stringurl这个url的话实际上是我们的evotica它的连接字不是gdbcevotica然后remote然后url等于我们的这个url等于什么呢
[01:43] 等于 http://ip 然后端口此时是J的它的API的接口v2sql然后呢vk OK这是我们的一个URL就是apache J的GDPC的URL那么还有一个就是我们的一个private的一个我们的propertyraw propertiesproperty
[02:24] 等于我们的什么呢等于我们的newok这是我们定义的今天定义了一个变量那么下面的话我们就开发我们的这个连接publicpublic的一个连接的一个connection我们get一个connectionok这个getconnection的话这个时候我们需要创建的我们现在还没有创建的我们如果是说try cache
[03:13] 如果我们的connection等于空那么我们需要等于driverManager.getConnection.rel.fig此时我们再return我们的connection这个时候我们就可以获得我们的connection了那下一步来讲的话我们需要close我们的一个电量public void close
[03:51] 还有什么呢connection然后还有一个statement还有我们的result set我们把这几个都是需要进行关闭的如果是如果是我们的connection不等于空我们要把我们的connection关闭掉那么如果我们的这个statement不等于空我们要把statement
[04:51] 关闭掉然后如果我们的这个resultSet不等于我们同样也需要把resultSet给它load掉OK 这是我们的一个J的它的一个GDPC的工具类而这个J的GDPC的工具类呢我们可以来使用的使用它那么使用它的这个方式相对来讲也比较简单我可以创建一个create一个GDPC然后呢相应的这个
[05:22] get一个GDPCGDPC然后执行我们的创建我们的statement然后来创建我们的执行我们的搜索语句然后得到我们的result set通过这样的方式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

