# 5.9 TableEnvironment介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.9 TableEnvironment介绍_【海量资源尽在 666java.com】.mp4
- 时长 4分56秒（音频 297s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们来给大家介绍一下Flink Table API和Circle编程的一个非常重要的核心的一个类这个类叫做Table Environment那么Table Environment是用来创建Table API和Circle程序的上下文执行环境也就是说它是Table和Circle程序的一个入口我们的Table和Circle程序所有的功能都是围绕着Table Environment这个核心类展开的
[00:29] 那么这个类的主要作用有什么呢第一它在我们内部的目录中注册表第二它在我们外部的目录中注册表第三它可以执行Circle的一个查询第四它能够注册用户定义的一些函数这些函数包括我们的指标啊表啊聚合啊等等第五它能够把DataStream和DataSet转换成Table第六它是
[00:55] Execution Environment和Stream Execution Environment的附类那么在Flink 1.8中一共有7个Table Environment而在最新的1.9的版本中社区对它进行了重构和优化只保留了5个Table Environment那么在实现上是5个面向用户的接口也就是说我们程序开发的时候是可以直接使用的接口而在这些接口的底层呢它其实实现了不同的一个实践
[01:24] 那么五个接口包括一个table environment两个batch table environment两个stream的table environment这五个接口那么这五个接口的话有两个是属于skeleton也就是说有一个是batch table environment的一个skeleton另外一个是stream table environment的类我们如果使用java来开发的时候我们其实只需要关注三个类那么一个叫table environment一个叫batch table environment.java另外一个是
[01:52] Stream Table Environment解加吧那么这个Table Environment这种顶级它是一个顶级的一个接口我们的Batch Table Environment和Stream Table Environment都是这个接口的一个具体的实现那么另外一方面Table Environment作为一个统一的一个接口它其实有一个统一性的一个表现那么统一性表现主要有两个方面一方面是说它对于所有的基于GVM的语言
[02:22] 也就是说是Scalar语言和Java语言它是统一的那么BatchTableEvents.java和BatchTableEvents.scala都是继承TableEvents而StreamTableEvents和StreamTableEvents.scalaJava和Scalar这两个版本的也都是继承自TableEvents那么第二点是说它针对于这种有界的数据和无界的数据它是做了统一的处理
[02:51] 也就是说在table environment这个层面上它提供了这种纯粹的table生态上的一个上下文它适用于整个作业都使用这种table API和circle编程用简单的话来讲的话一是对于语言的统一性二是对于有界数据和无界数据的一个统一性它都体现在table environment这个类里边那么两个stream table environment
[03:16] 分别对应于Java的流计算和Scalar的流计算那么流计算的对象呢分别是Java的DataStream和Scalar的DataStream那么相比于TableEvents这种StreamTableEvents提供了DataStream和Table之间的相互转换的接口也就是说我们可以把我们的DataStream和Table相互之间进行转换我们后面会给大家详细的介绍这种转换的一种方式那么两个
[03:45] P处理的场景的话P处理的这种Events它分别对应于Java的P处理场景和Skeleton的P处理场景P处理里的对象呢又分别是我们的Java的Dataset和Skeleton的Dataset那么这两个两者之间的话相应的会对于Dataset和Table之间进行相互转换看一下我们以前开发的这个事例程序这个事例程序中就是说我们的
[04:12] Stream Table Environment它是由我们的Stream Table Environment直接创建的对吧它创建的时候是创建的是根据了我们的Stream Execution Environment作为参数来创建的那么我们在这个地方稍微看一点点看一点点什么呢我们的Data Stream比如说我们Data Stream它的操作是和谁相关的呢它是和我们的Evolution也就是Stream Execution Environment相关的我们可以由Stream Execution Environment
[04:42] 来创建我们的datastream但是对于table来讲的话它是由stream table environment来创建的好这是我们对于我们的整个table environment做的一个详细的讲解谢谢大家

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

