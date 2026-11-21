# 画面线理解：11-DataBaseMetaData元数据：获取数据库基本信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\11-DataBaseMetaData元数据：获取数据库基本信息_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:55, 01:57, 03:54, 04:40, 05:44, 06:13, 07:02, 07:21, 09:04, 09:32, 10:05, 10:32, 10:59, 11:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:48:10

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库的基本信息，包括数据库产品名、版本号、用户名、驱动版本号、是否支持事务等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，标题为“3.2 数据库元数据”，子标题“3.2.1 概述”，介绍DatabaseMetaData是Connection对象通过getMetaData方法获得，封装了数据库基本信息，并列出常用方法如getDatabaseProductName、getUserName等。
画面2：在IDEA中，项目结构显示，正在创建一个新类，同时展示pom.xml中已添加的freemarker依赖。
画面3：在IDEA中，创建了名为DatabaseMetaDataTest的测试类，开始编写测试方法test01。
画面4：在IDEA中，编写代码，准备获取数据库连接，注释为“//1. 获取元数据”。
画面5：切换到另一个项目ihm_parent，展示application.yml文件。
画面6：在SQLyog中，显示数据库列表，包括test、test1、test2等。
画面7：在IDEA中，编写代码，准备获取数据库连接，注释为“//1. 获取元数据”。
画面8：在IDEA中，编写代码，设置数据库连接参数，包括驱动、URL、用户名、密码。
画面9：在IDEA中，编写代码，获取数据库元数据对象。
画面10：在IDEA中，编写代码，调用getUserName方法获取用户名。
画面11：在IDEA中，编写代码，调用supportsTransactions方法检查是否支持事务。
画面12：在IDEA中，编写代码，调用getCatalogs方法获取数据库目录。
画面13：在IDEA中，运行测试，测试失败，提示java.util.Hashtable.put异常。
画面14：在IDEA中，修正代码后运行测试，测试通过，输出结果为true和MySQL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<dependency>
    <groupId>org.freemarker</groupId>
    <artifactId>freemarker</artifactId>
    <version>2.3.28</version>
</dependency>
```

画面8：
```java
String driver = "com.mysql.jdbc.Driver";
String url = "jdbc:mysql://127.0.0.1:3306?useUnicode=true&characterEncoding=utf8";
String username = "root";
String password = "111111";
Properties props = new Properties();
props.put("remarksReporting", "true"); //获取数据库的备注信息
props.put("user", username);
props.put("password", password);
```

画面9：
```java
Class.forName(driver); //注册驱动
Connection connection = DriverManager.getConnection(url, props);
DatabaseMetaData metaData = connection.getMetaData();
```

画面10：
```java
String userName = metaData.getUserName();
```

画面11：
```java
boolean supportsTransactions = metaData.supportsTransactions();
```

画面12：
```java
String[] catalogs = metaData.getCatalogs();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.2 数据库元数据”，子标题“3.2.1 概述”，内容包括DatabaseMetaData的定义和常用方法列表。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
