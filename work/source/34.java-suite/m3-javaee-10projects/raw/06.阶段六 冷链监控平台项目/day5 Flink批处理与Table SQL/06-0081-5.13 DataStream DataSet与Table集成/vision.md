# 画面线理解：5.13 DataStream DataSet与Table集成

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.13 DataStream DataSet与Table集成_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:24, 02:03, 02:41, 03:24, 04:05, 04:47, 05:19, 06:10, 06:59, 09:10, 09:38, 10:10, 10:56, 12:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:27:49

1) 这一组画面整体在讲如何在 Flink 中将 DataStream 转换为 Table 并注册为表。

2) 按时间顺序列出每张画面的要点：
画面1：展示教材内容，讲解“2.6 流和批与Table集成编程”章节，说明 DataStream 或 DataSet 可以在 TableEnvironment 中注册为表。
画面2：IDEA 编辑器中显示 TransferTable.java 文件，准备编写代码。
画面3：在 TransferTable.java 中，光标位于 main 方法的起始位置。
画面4：在 main 方法中，导入 StreamTableEnvironment，并创建 StreamExecutionEnvironment。
画面5：在 main 方法中，创建 StreamableEnvironment。
画面6：在 main 方法中，定义数据源，创建 DataStream。
画面7：在 main 方法中，将 DataStream 转换为 Table。
画面8：在 main 方法中，将 DataStream 注册为 Table。
画面9：在 main 方法中，将 Table 转换为 DataStream。
画面10：在 main 方法中，将 Table 注册为 DataStream。
画面11：在 main 方法中，使用 IDE 的自动补全功能选择 registerDataStream 方法。
画面12：在 main 方法中，将 Table 转换为 DataStream。
画面13：在 main 方法中，定义 TupleTypeInfo。
画面14：在 main 方法中，完成将 Table 转换为 DataStream 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
2.6 流和批与Table集成编程
表API和SQL查询可以轻松集成并嵌入到DataStream和DataSet程序中，例如，可以直接从外部表（例如来自RDBMS），进行一些领域处理，例如过滤、投射，聚合或与元数据连接，然后使用DataStream或DataSet API进一步处理数据。这种相互作用可以通过转换 DataStream 或 DataSet 转换来实现，Table 反之亦然。
2.6.1 将DataStream或DataSet注册为表
DataStream 或 DataSet 可以在 TableEnvironment 表中注册。注册表的模式取决于已注册 DataStream 或 DataSet 的数据类型 DataSet。
```

画面4：
```
import org.apache.flink.table.api.java.StreamTableEnvironment;
```

画面5：
```
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
StreamableEnvironment streamableEnvironment = StreamableEnvironment.create(env);
```

画面6：
```
DataStream<Tuple2<String, Integer>> stream = env.fromElements(
    new Tuple2<>("hello", 3),
    new Tuple2<>("world", 2)
);
```

画面7：
```
Table table = streamableEnvironment.fromDataStream(stream, "word_count");
```

画面8：
```
streamableEnvironment.registerDataStream("table", stream, "word_count");
```

画面9：
```
DataStream<Tuple2<String, Integer>> dataStream = streamableEnvironment.toAppendStream(table);
```

画面10：
```
streamableEnvironment.registerDataStream("table", stream, "word_count");
```

画面13：
```
TupleTypeInfo<Tuple2<String, Integer>> tupleTypeInfo = new TupleTypeInfo<>(
    Types.STRING,
    Types.INT
);
```

画面14：
```
DataStream<Tuple2<String, Integer>> dataStream = streamableEnvironment.toAppendStream(table, tupleTypeInfo);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
