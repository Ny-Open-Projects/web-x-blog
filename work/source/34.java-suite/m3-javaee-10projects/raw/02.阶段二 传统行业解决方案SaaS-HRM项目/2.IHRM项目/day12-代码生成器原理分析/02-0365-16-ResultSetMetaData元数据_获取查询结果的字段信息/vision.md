# 画面线理解：16-ResultSetMetaData元数据：获取查询结果的字段信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\16-ResultSetMetaData元数据：获取查询结果的字段信息_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 01:38, 02:00, 02:39, 02:54, 03:18, 03:46, 04:33, 05:09, 06:03, 06:37, 07:35, 08:47, 09:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:51:08

1) 这一组画面整体在讲如何通过 Java 代码获取数据库查询结果集的元数据信息，包括列名和列类型。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表结构，查询 `bs_user` 表数据，用于后续测试。
画面2：展示 PPT 内容，讲解 `ResultSetMetaData` 的概念和常用方法。
画面3：展示项目结构，重点是 `application.yml` 配置文件。
画面4：展示 `ResultSetMetaDataTest.java` 文件，准备测试代码。
画面5：展示 `ParameterMetaDataTest.java` 文件，用于测试参数元数据。
画面6：展示 `ResultSetMetaDataTest.java` 文件，编写 SQL 和 PreparedStatement。
画面7：在 `ResultSetMetaDataTest.java` 中调用 `rs.getMetaData()`。
画面8：在 `ResultSetMetaDataTest.java` 中获取列数 `getCount()`。
画面9：在 `ResultSetMetaDataTest.java` 中使用 `for` 循环遍历列。
画面10：在 `ResultSetMetaDataTest.java` 中添加打印列名的代码。
画面11：在 `ResultSetMetaDataTest.java` 中添加打印列类型的方法 `getColumnTypeName()`。
画面12：运行测试，输出列名及其 Java 类型。
画面13：运行测试，输出列名及其 SQL 类型。
画面14：展示 PPT 内容，页面为空，可能为过渡或结束页。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3 - application.yml：
```yaml
#微服务注册到Eureka
eureka:
  client:
    service-url: http://localhost:6868/eureka
  server:
    port: 9002
spring:
  #服务名配置
  application:
    name: ihrm_system #指定服务名
  #数据库配置
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
    #jpa
    database: MySQL
    show-sql: true
    open-in-view: true
    redis:
      host: 127.0.0.1
      port: 6379
    jwt:
      config: 
```

画面5 - ParameterMetaDataTest.java：
```java
@Before
public void init() throws Exception {
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306/ihrm?useUnicode=true&characterEncoding=utf8";
    String username = "root";
    String password = "111111";
    Properties props = new Properties();
    props.put("remarksReporting","true");//获取数据库的备注信息
    props.put("user",username);
    props.put("password",password);
    //1.获取连接
    Class.forName(driver);//注册驱动
    connection = DriverManager.getConnection(url,props);
}
```

画面6 - ResultSetMetaDataTest.java：
```java
String sql = "select * from bs_user where id=?";
PreparedStatement pstmt = connection.prepareStatement(sql);
pstmt.setString(parameterIndex, "1", "1863705482939731968");
```

画面7 - ResultSetMetaDataTest.java：
```java
ResultSetMetaData metaData = rs.getMetaData();
```

画面8 - ResultSetMetaDataTest.java：
```java
int count = metaData.getColumnCount();
```

画面9 - ResultSetMetaDataTest.java：
```java
for(int i=1;i<count;i++){
```

画面10 - ResultSetMetaDataTest.java：
```java
String columnName = metaData.getColumnName(i);
System.out.println(columnName);
```

画面11 - ResultSetMetaDataTest.java：
```java
String columnType = metaData.getColumnTypeName(i);
System.out.println(columnName+"---"+columnType);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：PPT 标题为“3.4 结果集元数据”，内容包括 `ResultSetMetaData` 的定义和常用方法。
画面14：PPT 标题为“1.4 数据库之元数据”，内容为空。

5) 无。
