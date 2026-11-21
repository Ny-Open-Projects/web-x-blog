# 30-Jdbc查询Druid实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们已经讲解了Z SQL

以及Z SQL的一些常用语法

那我们现在可以利用Z SQL

编写出查询

分析我们热点商品的一些Z SQL语句了

但是我们要想实现在加密程序中

自动查询怎么办呢

接着我们讲解JDBC查询我们的Apache Z

那我们要去查询我们Apache Z的话

这一块不能用普通的JDBC驱动

我们得用Carsight它的JDBC驱动

Apache Carsight

它是面向Hadoop新的查询引擎

它提供了标准的Z SQL语言

多种查询优化和连接各种数据源的能力

除此之外

Carsight还提供了ORAP和流处理的查询引擎

因此我们可以用Apache Carsight

去查询我们的Apache Z

那如果我们想用

Carsight

去查询我们的Apache Z的话

这个时候是需要引入依赖包的

那其他的操作流程呢

几乎是一样的

我们来实现一下

其他的流程就按JDBC的流程去写就可以了

好我们来测试一次

把我们的工程打开

在这一块有一个工程叫做Monitor

在这里

首先我们要引入Carsight的依赖包

把它给导入进来

导入进来

导入进来之后呢

接着我们在这里写一个Test就可以了

我就写一个简单的测试了

最的

Circle Test

我就不写太详细哈

直接写个主方法就好了

这个流程呢

我们完全可以按照JDBC的流程去编写就行了

好

这个是我们数据库的连接地址

接着我们会做什么事呢

会获取连接对象

然后我们会获取Statement的对象

Statement的对象获取之后呢

我们紧接着会开始准备一个Circle语句了

Circle语句有了

我们会去执行查询

查询执行之后

我们会解析结果集

结果集解析了

不要忘了关闭资源

这个是以前JDBC的操作流程

我们就把这个JDBC操作流程给写完

好

连接对象这一块

我们写Connection

等于DriverManager.getConnection

连接地址给他

不要忘了抛个异常

好

这是这一块

紧接着我们获取Statement的对象

点CreateStatement

Statement的对象有了

准备一下语句

语句呢

我就写一下Circle

等于

Select

SignalForum

Logs

Items

就是这边的一个查询语句

这个最的Circle

可以的

好

Circle语句有了

接着执行查询

Statement

点执行查询

查询之后呢

就有结果集

结果集有了

紧接着我们就便利结果集

好

我们就获取URI就可以了

点输出一次

最后不要忘了关闭资源

还有我们的Statement点Close

还有我们的Collection点Close

好

我们来测试一次

看看效果怎么样

这个还不能测试

咱们太着急了

这一块就是我们的JDBC操作流程

对吧

怎么把它换成查询我们的ApacheJS呢

这个地址要换

这个连接对象换一下就可以了

好

地址换成这个地址换成这个地址

就OK了

端口注意一下

是8082

好

这个连接对象换成谁呢

换成我们

注意要换成他了

这里强转一次

可以了

那这个时候我们就可以执行的一个查询了

大家看一下

看现在行与不行

运行一次

好

我们看这个运行的结果

运行的结果呢

运行的结果呢

运行的结果呢

运行的结果呢

运行的结果呢

这一块

全部输出了

于是我们这一块

利用GDBC去查询我们的罪的也是可以的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于 **Apache Druid** 数据库的实战教学课程。讲师通过 IntelliJ IDEA 开发环境，演示了如何使用 Java 语言通过 JDBC 驱动程序连接到 Druid 数据库，并执行一个简单的 SQL 查询。视频内容主要围绕以下几个方面：
- **技术背景**：介绍 Druid 是一个面向 Hadoop 的新查询引擎，支持标准 SQL 语言和 OLAP 流处理。
- **环境准备**：展示如何在 Maven 项目中引入 Avatica JDBC 驱动依赖。
- **代码实现**：编写一个 `DruidSQLTest` Java 类，完成数据库连接、SQL 执行和结果集解析的完整流程。
- **实战演示**：通过控制台日志，验证了连接成功并执行了查询，成功获取了数据。

整个过程旨在帮助学习者掌握如何在 Java 应用中集成和操作 Druid 数据库。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下时间点是根据画面内容和典型教学视频的结构进行的合理推断：

- **0:00 - 0:30**：课程引言与背景介绍。讲师在 PPT 上讲解了 Apache Druid 的概念、功能和应用场景。
- **0:30 - 1:00**：环境搭建与依赖配置。讲师在 IDEA 中展示 `pom.xml` 文件，并演示如何添加 Avatica JDBC 驱动的 Maven 依赖。
- **1:00 - 2:00**：创建测试类与编写代码。讲师创建 `DruidSQLTest.java` 文件，并编写了连接数据库和执行查询的 Java 代码框架。
- **2:00 - 3:00**：代码细节与调试。讲师逐步完善代码，包括设置连接 URL、创建 Statement 对象、编写 SQL 查询语句、执行查询和解析结果集。
- **3:00 - 3:30**：运行与结果验证。讲师运行程序，通过控制台日志确认连接成功，并打印出查询结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 标题**：`4.2.5 JDBC查询Apache Druid`
- **核心内容**：
  - Apache Calcite 是面向 Hadoop 的新查询引擎，提供标准 SQL 语言、多种查询优化和连接各种数据源的能力。
  - Calcite 还提供了 OLAP 流处理的查询引擎。
  - **Java 连接方式**：使用 Calcite JDBC 驱动程序进行 Druid SQL 查询。
  - **依赖配置**：需要引入 `avatica-core` 包，并提供 Maven 依赖的 XML 代码。
  - **连接 URL 格式**：`jdbc:avatica:remote:url:http://192.168.211.137:8082/druid/v2/sql/avatica/`

#### 代码关键内容

- **Maven 依赖 (XML)**：
  ```xml
  <dependency>
      <groupId>org.apache.calcite.avatica</groupId>
      <artifactId>avatica-core</artifactId>
      <version>1.15.0</version>
  </dependency>
  ```

- **Java 代码 (`DruidSQLTest.java`)**：
  ```java
  public class DruidSQLTest {
      public static void main(String[] args) throws Exception {
          // 数据库连接地址
          String url = "jdbc:avatica:remote:url:http://192.168.211.137:8082/druid/v2/sql/avatica/";
          
          // 获取连接对象
          Connection connection = (AvaticaConnection) DriverManager.getConnection(url);
          
          // Statement
          Statement statement = connection.createStatement();
          
          // SQL语句
          String sql = "SELECT * FROM logitems";
          
          // 执行查询
          ResultSet resultSet = statement.executeQuery(sql);
          
          // 解析结果集
          while (resultSet.next()) {
              System.out.println(resultSet.getString("uri"));
          }
          
          // 关闭资源
          resultSet.close();
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：环境与依赖配置**
  - 讲师在 IntelliJ IDEA 中打开一个名为 `seckill` 的 Maven 项目。
  - 在 `pom.xml` 文件中，讲师通过鼠标操作，添加了 `avatica-core` 的依赖项，并展示了其完整的 XML 配置。

- **场景二：创建测试类与编写代码**
  - 讲师在项目中创建了一个名为 `DruidSQLTest` 的 Java 类。
  - 讲师在代码中定义了 `main` 方法，并逐步编写了数据库连接、SQL 查询和结果解析的代码。
  - 讲师使用了 IDEA 的智能提示功能（如 `Ctrl+Shift+Space`），来选择 `Connection`、`Statement` 和 `ResultSet` 等类的成员方法。

- **场景三：SQL 查询与结果解析**
  - 讲师编写了 SQL 查询语句：`SELECT * FROM logitems`。
  - 讲师使用 `ResultSet` 对象的 `next()` 方法遍历查询结果，并使用 `getString("uri")` 方法获取指定列的值。
  - 讲师在代码中添加了 `System.out.println` 语句，用于在控制台打印查询结果。

- **场景四：运行与结果验证**
  - 讲师运行程序后，控制台输出了 Druid 数据库中 `logitems` 表的 `uri` 字段值。
  - 控制台日志显示了 HTTP 请求的详细信息，包括连接成功、路由分配和请求头等，证明了连接和查询的正确性。

---

以上是根据视频画面进行的结构化技术分析，旨在帮助学习者系统地理解 Apache Druid 的 JDBC 连接与查询操作。
