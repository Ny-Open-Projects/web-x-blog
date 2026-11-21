# 画面线理解：7.10 JDBC查询Druid数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.10 JDBC查询Druid数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:52, 02:19, 03:20, 04:38, 05:27, 05:52, 07:15, 08:23, 08:40, 09:12, 09:36, 10:02, 10:20, 10:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:44:11

1) 这一组画面整体在讲如何通过 Java 代码连接 Apache Druid 数据库并执行 SQL 查询。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT内容，介绍 Apache Calcite 是一个动态数据管理框架，包含多个常用典型数据库系统的经典模块，省略了一些关键功能，如数据存储、数据处理逻辑和元数据存储，并给出示例代码片段。
画面2：在PPT中绘制了“Apache Druid”与“数据 druid数据”之间的双向箭头，表示 Druid 的数据管理能力。
画面3：在PPT中添加了“我们能应用”框，并在中间层标注“apache Calcite”和“apache calcite Avatica”，说明应用通过 Calcite 和 Avatica 与 Druid 数据交互。
画面4：展示 IntelliJ IDEA 中的 `pom.xml` 文件内容，添加了对 `org.apache.calcite.avatica` 依赖。
画面5：展示 `Wiki.java` 文件的初始状态，准备编写代码。
画面6：在 `Wiki.java` 文件中添加了注释“//1. 设置jdbc的参数”和“//2. 执行sql语句”。
画面7：在 `Wiki.java` 文件中编写了设置 JDBC URL 和 Properties 的代码。
画面8：在 `Wiki.java` 文件中，为 `Properties` 类添加了 `import java.util.Properties;`。
画面9：在 `Wiki.java` 文件中，为 `Connection` 类添加了 `import java.sql.Connection;` 和 `import java.sql.DriverManager;`。
画面10：在 `Wiki.java` 文件中，为 `DriverManager` 类添加了 `import java.sql.DriverManager;`。
画面11：在 `Wiki.java` 文件中，编写了 SQL 查询语句 `select * from wikipedia order by _time desc limit 10`。
画面12：在浏览器中打开 Apache Druid 的查询界面，显示了查询结果。
画面13：在 `Wiki.java` 文件中，编写了遍历 ResultSet 并打印结果的代码。
画面14：在 `Wiki.java` 文件中，编写了获取列标签并打印的代码，编译成功。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithems.demo</groupId>
    <artifactId>druid-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.apache.calcite.avatica</groupId>
            <artifactId>avatica-core</artifactId>
            <version>1.18.0</version>
        </dependency>
    </dependencies>
</project>
```

画面7：
```java
String url = "jdbc:avatica://http://172.17.0.143:8888/druid/v2/sql/avatica/";
Properties properties = new Properties();
```

画面11：
```java
String sql = "select * from wikipedia order by _time desc limit 10";
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：
- “Apache Druid” 框通过双向箭头指向 “数据 druid数据” 框。

画面3：
- “Apache Druid” 框通过双向箭头指向 “apache Calcite” 框。
- “apache Calcite” 框通过双向箭头指向 “数据 druid数据” 框。
- “我们能应用” 框通过单向箭头指向 “apache Calcite” 框。

5) 无
