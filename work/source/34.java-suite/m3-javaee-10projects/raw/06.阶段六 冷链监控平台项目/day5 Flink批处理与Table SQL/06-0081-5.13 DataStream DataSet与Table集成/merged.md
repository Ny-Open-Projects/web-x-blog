# 5.13 DataStream DataSet与Table集成

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.13 DataStream DataSet与Table集成_【海量资源尽在 666java.com】.mp4
- 时长 12分29秒（音频 750s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们来介绍一下Flink的DataStream、DataSet与Table的集成编程Table API和Circle API可以轻松地集成并迁入到DataStream或者是DataSet的程序里面例如,我们可以查询外部表进行一些数据的预处理比如像过滤、投影聚合或者是与原数据的一些连接然后使用DataStream或DataSet API进行进一步的处理
[00:30] 那么另外一个过程是我们将table API或者是circle查询也可以应用到我们的datastream或dataset程序里边来那么这种相互的作用或者叫相互的转换呢可以通过datastreamdataset的一个转换来实现table也是这样的情况那么我们来看一看我们能够做的操作比如将我们的datastream或者是dataset注册成为一个表
[00:58] 那么另外一种情况是将我们的DataStream或DataSet转换成一种表一种是注册一种是转换另外一个情况是我们可以将表转换成DataStream或者是我们将表转换成DataSet那么我们来开发一个代码来给大家演示一下如何来做这个操作我们打开我们的ID在我们的Table里边添加一个类
[01:28] 这个类的话叫transfer叫transfertable或者叫table transfer都ok的然后添加名函数那么在这里边我们需要做几个操作第一个操作我们需要把我们的data stream转换成我们的table将data stream转换成table那第二个来讲的话我们将data
[02:04] Stream注册成table那第三个的话我们会将我们的table转换成我们的datastream第三将table转换成datastreamdataset的程序转换其实和当前这个datastream是类似的我们先演示一下我们的datastream
[02:33] 针对于我们的一个dataset程序或者datastream程序我们第一步的时候需要定义什么我们需要定义我们的执行环境第一定义执行环境那么针对于针对于我们的table和datastream我们需要定义两个执行环境一个叫streamexecutionenvironment比如env我们它等于什么呢等于streamexecutionenvironment的这个类然后
[03:02] 得到一个方法叫getExecutionEvents那第二个来讲的话叫streamTableEvents这个呢是针对于Flink table的一个环境变量或者说有个关键的一个环境信息比如像我们的streamTableEvents那么它等于什么呢它等于streamTableEventsCreate用这个方法来创建
[03:30] 那么CREATE的参数其实就是我们的STREAM EXECUTION INVENTOR的这个参数了那第二步来讲的话我们定义一个数据源这个数据源呢我们可以简单的用我们的Java对象来创建或者是我们直接用我们的TEMPO对象DATA STREAM然后它的类型是TEMPO 2也就是说是两个字段一个字段呢叫STREAM一个字段
[04:07] 叫integer那么这个字段呢表示我们用它来表示我们的比如前面我们例子中讲的单词的计数一个是单词一个是单词出现的次数那么我们定义一个stream它等于inv.from elementfrom element而这个element里边我们可以直接用newTempo2然后参数是比如说像hello然后它出现了次数是两次
[04:43] 或者三次那么第二个来讲的话是也是一个newtompo2然后wordhello world然后这个呢出现了两次ok那此时我们定义了一个我们的datastream的数据语言那下一步的话我们要将我们的datastream数据语言转换成我们的表将datastream转换成Flink的
[05:18] 那么这个怎么做呢比如说我们定义一个table这个table的类我们先引入进来然后呢它等于我们的streamtable environment然后在这里边from data stream那么这个data stream相应的我们就有参数了一个参数就是我们的stream对吧那么另外一个我们还需要定义我们这个表的字段
[05:49] 比如说叫一个叫word一个叫countOK那此时我们就将我们的一个datastream转换成了一个Flink table那第二个例子的话我们可以将我们的datastream注册成一个表就是Flink的table那在这里边的时候我们怎么做呢我们有两种方式一种方式是我们stream table
[06:22] Evament它呢用它来直接注册从我们的这个DataStream里面注册就是这个方法叫做Register DataStream然后我们可以定义我们的TableTable1这个时候我们用我们的Stream来作为参数那此时我们就会定义出一个叫Table1的这样的一个表在我们表空间里面也就是说我们Stream
[06:50] table environment这个表空间里边我们会定义这样一个表那第二种方式还有什么方式我们streamtable environment也是用我们的register data from我们的stream但是它的参数呢我们又变成两个或者变成三个参数了比方说刚才会多一个参数一个呢叫做我们的表的名字table2那么还有一个参数就是我们的stream那么第三个参数呢就是我们的表的字段
[07:20] 一个叫word一个叫countOK这两个的话其实是同一个参数对吧但是它两个的参数是不一样的那么第二个方法比第一个方法多了一个表的字段那么有可能有些同学会问了如果我不设置我的表的字段那我的表字段应该是什么呢也就是说针对于这种情况它表的字段就是默认的给设置为F0F1然后一直到
[07:50] 更多的F F1 F2 F3 F4等等这些的话其实就属于我们如果不设置一个表的字段那么它就会自动的将这个表的字段设置成F0 F1这样的一个形式OK这样的话我们将一个DataStream转换成了我们的一个table同时呢我们还可以把我们的table
[08:15] 转换成我们的del stream那么后续的就可以做额外的一些操作无论是我们针对于del table的操作还是说针对于del stream的操作我们都可以做相应的操作对吧那下一步的时候我们还可以将我们的这个表转换成我们的一个del stream对吧现在来讲的话是将我们的del stream转换成了表了那下一步我们将这个表转换成del stream那么转换成del stream的时候稍微麻烦一点点
[08:46] 因为我们要给我们的del stream设置一下它的类型而这个类型我当前我们使用的是什么什么类型的我们使用的tumbler行对不对OK我们先添加一下注注视将表就是flinktable转换成del stream我们将它转换成del stream那么刚才我们说我们的
[09:19] 转换的过程中需要将表的字段的类型转换成一个tumple类型那么这种情况应该怎么做也就是说我们有一个data stream我们要定义一个data stream那么这个data stream它的类型是什么呢tumpletumple2那么tumple2的一个stream类型的那么一个integra类型的然后我们定义的就是我们data stream它等于我们的
[09:57] Stream table environment.toAppendStream,toAppendStream它有参数是什么?
[10:07] 比如说第一个叫我们的推保,那这个推保现在有没有呢?
[10:11] 我们现在有了一个推保,比如说像这个推保,我们有了这个推保,我们有了推保之后,下一步的时候,我还需要定义一个我们的这个类型,我们这个方法的话,
[10:23] 需要有一个参数这个参数就是我们的data set啊data stream它的一个类型那么这个类型的话我们应该怎么做呢我们要定义一个tumple typeinfo这个类而tumple typeinfotumple而tumple typeinfo这个类呢其实是定义的是tumpletumpletumple2而tumple2的一个string一个
[10:56] 那么我们定义了我们这个类型tab type info的类型new tab tab type info然后呢在这里边我们定义什么呢tab.string第一个是tab string那么第二个呢是我们的这里边当然是需要一个括号那第二个的话是什么呢tab.inter
[11:37] 1.8的时候是括号1.9的时候不需要加括号了OK那我们添加了一个这种类型这种类型的话我们就把这个变量放到这里边来了type inferOK那此时我们就将一个我们的表转换成了我们一个data stream那么在这个转换的过程中一个核心点就是
[12:05] 我们的数据类型而这个类型如果不是project类型的比如像table类型的那么这个table类型我们要定义tabletypeinfo来作为我们的这个stream table environment的方法append to stream里边的一个参数好这是我们给大家介绍的两个两者之间data stream data set和table相互之间转换的一个过程谢谢大家

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Flink.table.api.java.StreamTableEnvironment;
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

