# 画面线理解：5.10 在表空间中注册表

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.10 在表空间中注册表_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:56, 02:22, 03:39, 03:43, 04:16, 04:30, 04:31, 04:35, 04:53, 04:59, 05:22, 05:43, 05:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:26:29

1) 这一组画面整体在讲什么（一句话）：
讲解 Flink Table API 中如何在表空间中注册表，包括注册 TableSource 和 TableSink 的代码示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 Flink Table API 的核心概念：TableEnvironment 是维护按名称注册的表的目录，输入表可在 API 和 SQL 查询中引用，输出表可用于将查询结果发送到外部系统。
- 代码示例：创建 StreamExecutionEnvironment 和 BatchTableEnvironment。
- 代码示例：注册表的两种方式（从表空间中查询或用注册表注册另一个表）。

画面 2:
- 展示了注册 TableSource 的代码示例。
- 代码示例：创建 TableSource 对象并注册到 TableEnvironment。

画面 3:
- 展示了注册 TableSink 的代码示例。
- 代码示例：创建 TableSink 对象并注册到 TableEnvironment。

画面 4:
- 展示了注册 TableSink 的代码示例，包括定义字段名和类型。
- 代码示例：使用 registerTableSink 方法注册 TableSink。

画面 5:
- 展示了注册 TableSink 的代码示例，包括定义字段名和类型。
- 代码示例：使用 registerTableSink 方法注册 TableSink。

画面 6:
- 展示了注册 TableSink 的代码示例，包括定义字段名和类型。
- 代码示例：使用 registerTableSink 方法注册 TableSink。

画面 7:
- 展示了注册 TableSource 的代码示例。
- 代码示例：创建 TableSource 对象并注册到 TableEnvironment。

画面 8:
- 展示了注册 TableSource 的代码示例。
- 代码示例：创建 TableSource 对象并注册到 TableEnvironment。

画面 9:
- 展示了注册 TableSource 的代码示例。
- 代码示例：创建 TableSource 对象并注册到 TableEnvironment。

画面 10:
- 展示了注册 TableSink 的代码示例，包括定义字段名和类型。
- 代码示例：使用 registerTableSink 方法注册 TableSink。

画面 11:
- 展示了 Table 执行过程分析的标题。
- 代码示例：创建 StreamTableEnvironment。

画面 12:
- 展示了 Table 执行过程分析的标题。
- 代码示例：创建 StreamTableEnvironment。

画面 13:
- 展示了 Table 执行过程分析的标题。
- 代码示例：创建 StreamTableEnvironment。

画面 14:
- 展示了创建 ExecutionEnvironment 和 BatchTableEnvironment 的代码示例。
- 代码示例：创建 StreamExecutionEnvironment 和 BatchTableEnvironment。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.apache.flink.table.api.java.StreamTableEnvironment;
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
// 创建流表环境的TableEnvironment
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);

import org.apache.flink.table.api.java.ExecutionEnvironment;
import org.apache.flink.table.api.java.BatchTableEnvironment;
ExecutionEnvironment benv = ExecutionEnvironment.getExecutionEnvironment();
// 创建批表环境的TableEnvironment
BatchTableEnvironment btableEnv = BatchTableEnvironment.create(benv);
```

画面 2:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 从表空间中查询表，并执行select操作
Table projTable = tableEnv.scan("tableName").select(...);
// 用一个表注册成另外一个表
tableEnv.registerTable("projectedTable", projTable);
```

画面 3:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSource
TableSource csvSource = new CsvTableSource("/path/to/file", ...);
// 将TableSource注册成表：CsvTable
tableEnv.registerTableSource("CsvTable", csvSource);
```

画面 4:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 5:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 6:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 7:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSource
TableSource csvSource = new CsvTableSource("/path/to/file", ...);
// 将TableSource注册成表：CsvTable
tableEnv.registerTableSource("CsvTable", csvSource);
```

画面 8:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSource
TableSource csvSource = new CsvTableSource("/path/to/file", ...);
// 将TableSource注册成表：CsvTable
tableEnv.registerTableSource("CsvTable", csvSource);
```

画面 9:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSource
TableSource csvSource = new CsvTableSource("/path/to/file", ...);
// 将TableSource注册成表：CsvTable
tableEnv.registerTableSource("CsvTable", csvSource);
```

画面 10:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 11:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 12:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
```

画面 13:
```java
// 创建StreamTableEnvironment (BatchTableEnvironment的用法类似)
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);
// 创建TableSink
TableSink csvSink = new CsvTableSink("/path/to/file", ...);
// 定义字段名和类型
String[] fieldNames = {"a", "b", "c"};
TypeInfo[] fieldTypes = {Types.INT, Types.STRING, Types.LONG};
// 将TableSink注册成表：CsvSinkTable
tableEnv.registerTableSink("CsvSinkTable", fieldNames, fieldTypes, csvSink);
``
