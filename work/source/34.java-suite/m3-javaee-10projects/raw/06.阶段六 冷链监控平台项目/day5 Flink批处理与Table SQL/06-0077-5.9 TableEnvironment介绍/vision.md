# 画面线理解：5.9 TableEnvironment介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.9 TableEnvironment介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：10 帧 @ 01:34, 02:10, 04:07, 04:08, 04:24, 04:29, 04:33, 04:45, 04:47, 04:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:25:39

1) 这一组画面整体在讲如何使用 Flink 的 Table API 将 DataStream 转换为 Table 并执行 SQL 查询。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Flink Table API 的文档，说明 TableEnvironment 的作用和实现类，包括 org/apache/link/table/api/TableEnvironment.java、org/apache/link/table/api/java/BatchTableEnvironment.java、org/apache/link/table/api/java/scala/BatchTableEnvironment.scala、org/apache/link/table/api/java/scala/StreamTableEnvironment.scala。
画面2：与画面1内容相同，为文档页面的延续。
画面3：在 IntelliJ IDEA 中展示 TableTest.java 文件，代码开始定义执行环境和数据源。
画面4：代码中注释显示“定义执行环境”、“定义输入源”、“转换为 Table”、“执行 SQL 查询操作”、“执行流处理程序”。
画面5：代码中定义了两个 DataStream<Order>，分别命名为 orderA 和 orderB。
画面6：代码中将 DataStream 转换为 Table，创建了两个 Table 对象 tableA 和 tableB。
画面7：代码中执行 SQL 查询操作，使用 tEnv.sqlQuery() 方法。
画面8：代码中执行 SQL 查询操作，SQL 语句为：SELECT * from tableA where amount > 2 union all select * from tableB where amount > 2。
画面9：代码中执行 SQL 查询操作，SQL 语句为：SELECT * from tableA where amount > 2 union all select * from tableB where amount > 2。
画面10：代码中执行 SQL 查询操作，SQL 语句为：SELECT * from tableA where amount > 2 union all select * from tableB where amount > 2。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3-10：
```java
public static void main(String[] args) throws Exception {
    //1. 定义执行环境
    StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
    StreamTableEnvironment tEnv = StreamTableEnvironment.create(env);

    //2. 定义输入源
    DataStream<Order> orderA = env.fromCollection(Arrays.asList(
        new Order(user: 1L, product: "book1", amount: 3),
        new Order(user: 2L, product: "book2", amount: 4),
        new Order(user: 3L, product: "book3", amount: 2)
    ));

    DataStream<Order> orderB = env.fromCollection(Arrays.asList(
        new Order(user: 4L, product: "book4", amount: 2),
        new Order(user: 5L, product: "book5", amount: 2),
        new Order(user: 6L, product: "book6", amount: 1)
    ));

    //将数据流转换成 Flink Table
    Table tableA = tEnv.fromDataStream(orderA, "user, product, amount");
    Table tableB = tEnv.fromDataStream(orderB, "user, product, amount");

    //执行 SQL 查询操作
    Table result = tEnv.sqlQuery("SELECT * from tableA where amount > 2 union all select * from tableB where amount > 2");
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
