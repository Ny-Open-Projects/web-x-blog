# 画面线理解：5.14 Mysql数据源

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.14 Mysql数据源_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:17, 01:52, 02:36, 03:37, 04:40, 05:30, 07:22, 08:15, 09:17, 09:47, 10:46, 11:30, 12:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:28:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Flink 中通过 Table API 读取 MySQL 数据表并执行 SQL 查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构和 pom.xml 文件，其中包含 Flink Table API 相关的依赖项。
画面 2: 在项目中右键点击，弹出创建新文件的菜单，准备创建 Java 类。
画面 3: 在 src/main/java/com/itheima/cold.flink/table 包下创建了 TableJob.java 文件。
画面 4: 在 TableJob.java 中导入 Flink 的 ExecutionEnvironment 和 BatchTableEnvironment。
画面 5: 定义执行环境 ExecutionEnvironment 和 BatchTableEnvironment。
画面 6: 定义数据类型 TypeInformation，声明了 INT、STRING、INT 三种字段类型。
画面 7: 创建 JDBCInputFormat 的构建器，准备设置数据库连接参数。
画面 8: 通过 IDE 的自动补全功能，选择并设置 JDBCInputFormat 的参数。
画面 9: 完成 JDBCInputFormat 的配置，包括数据库 URL、用户名、密码和查询语句。
画面 10: 通过 IDE 的自动补全功能，选择并设置 DataSource。
画面 11: 调用 batchTableEnvironment.registerDataSet 注册数据源。
画面 12: 通过 IDE 的自动补全功能，选择并设置 Table 的类型。
画面 13: 定义数据源 DataSource。
画面 14: 完成数据源的定义，准备执行 SQL 查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-streaming-java_${scala.binary.version}</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-table-api-java-bridge_${scala.binary.version}</artifactId>
    <version>${flink.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-table-planner_${scala.binary.version}</artifactId>
    <version>${flink.version}</version>
</dependency>
```

画面 3:
```java
package com.itheima.cold.flink.table;
```

画面 4:
```java
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.table.api.java.BatchTableEnvironment;
```

画面 5:
```java
ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
BatchTableEnvironment batchTableEnvironment = BatchTableEnvironment.create(env);
```

画面 6:
```java
TypeInformation[] fieldTypes = new TypeInformation[] {
    BasicTypeInfo.INT_TYPE_INFO,
    BasicTypeInfo.STRING_TYPE_INFO,
    BasicTypeInfo.INT_TYPE_INFO
};
```

画面 7:
```java
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
```

画面 8:
```java
.setTableName("users")
.setQuery("select * from users")
.setRowTypeInfo(rowTypeInfo)
.finish();
```

画面 9:
```java
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
    .setDBUrl("jdbc:mysql://172.17.0.143:3306/test01?characterEncoding=utf8")
    .setUserName("root")
    .setPassword("123456")
    .setQuery("select * from users")
    .setRowTypeInfo(rowTypeInfo)
    .finish();
```

画面 10:
```java
DataSource source = env.createInput(jdbcInputFormat);
```

画面 11:
```java
batchTableEnvironment.registerDataSet("mTable", source);
```

画面 12:
```java
Table table = batchTableEnvironment.sqlQuery("select * from mTable");
```

画面 13:
```java
TypeInformation[] fieldTypes = new TypeInformation[] {
    BasicTypeInfo.INT_TYPE_INFO,
    BasicTypeInfo.STRING_TYPE_INFO,
    BasicTypeInfo.INT_TYPE_INFO
};
RowTypeInfo rowTypeInfo = new RowTypeInfo(fieldTypes);
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
    .setDBUrl("jdbc:mysql://172.17.0.143:3306/test01?characterEncoding=utf8")
    .setUserName("root")
    .setPassword("123456")
    .setQuery("select * from users")
    .setRowTypeInfo(rowTypeInfo)
    .finish();
DataSource source = env.createInput(jdbcInputFormat);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
