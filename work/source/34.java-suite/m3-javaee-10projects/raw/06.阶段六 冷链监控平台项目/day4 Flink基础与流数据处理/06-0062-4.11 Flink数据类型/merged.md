# 4.11 Flink数据类型

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.11 Flink数据类型_【海量资源尽在 666java.com】.mp4
- 时长 6分31秒（音频 391s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来介绍一下blink的数据类型这种数据类型指的是我们的一个datastream或者说dataset这个数据集合里边的一条一条数据它的一个数据类型比如我们像现在这张图里边上一节课里边提到的datastream和dataset那么这种datastream、dataset呢它是由单个的数据记录来组成的而这个数据记录到底是一个什么类型的这是我们现在要
[00:27] 需要学习和需要了解的一个地方那么Flink的这种数据集合或者数据类型呢它包含了以下这些类型第一种来讲的话叫数据元祖Java的数据元祖或者说是Skyla的一个案例的一个类型那么第二种来讲的话是Java的扑救对象也就是说和我们Java的尸体对象是一样的第三种的话叫做Java的原始类型第四类的话是常规类型那么第五类就是直类型
[00:56] 第六类的话是我们和Hadoop体系里边的Hadoop的Writeable的一个数据类型我们先看一看这种原组类型原组类型的话我们是包含了多种的这种固定数量的具有各种类型字段的一个复合类型也就是说我一个原组里边可以包含两个或者三个四个五个一直到25个这样的一个数据类型那么它里边的这种字段呢
[01:25] 字段类型可以是多种多样的比如说我们有两个字段构成了一个原组类型那么这两个字段呢是两个属性也就是两个字段嘛那么一个呢是string类型的一个是inter类型的那么比如说我们像下面这个我们定义我们的data stream的时候我们的data stream的这种原组是tuple2
[01:52] 表示是两个元素组成的那么一个类型的话是string类型的一个是integer类型的那么由它来构成的一个数据流那么这个数据流的话我们可以通过一些方式来创建吧这种创建的方式包括我们的用我们的当前的一个执行环境的然后手工的给它创建创建上这是我们
[02:18] 后边给大家介绍程序代码的时候会给大家介绍一下我们整个呃元祖数据类型呃然后他是如何来创建的如何来进行进行MAP或者进行其他操作的但大家在这个地方只需要了解和技术元祖类型它是由1-25个字段构成的一个数据类型那么每一个字段呢又有自己的类型就是基本的数据类型那第二种的话是我们的PUG类型PUG类型大家
[02:47] 理解为就是一个我们的Java对象的一个类型这个类呢是一个公开的类而且这个类必须有一个无参的构造函数或者叫做默认的构造构造函数那么所有的字段呢必须是这种都是这种公共的或者是通过get或set的方法能够访问的一个数据类型比如说我们有一个有一个对象这个对象呢其实就比如说像现在这个例子里边叫whatcom的
[03:15] 那么word count它的两个字段一个叫word一个叫count然后它是public的然后它的构造函数其实是一个无参的构造函数这种类型我们可以把它转换成实际上就是一个一个pojou或者pojou的类型这种pojou类型我们可以把这种pojou类型在我们的datastream里边来使用比如在这里边我们datastream的数据类型是一个word count
[03:41] Water with count,那么Water with count我们可以对它进行初始化复制这是我们的Pogeo类型那我们第三种类型的话是我们的基础的数据类型而这种基础的数据类型的话就比如说像Integer或者String,Double那种Java的原始的或者是Scalar我们现在主要给大家讲的是这种类型那么它的这种基本的八大数据类型吧那第四类的话是常规类型
[04:09] 常规类型的话其实和POJO类型有一点点类似所有未标示为POJO的类型那么都由Flink作为常规类型来处理Flink将这些数据呢视为这种黑盒子并且无法访问其内部的内容我们使用序列化的话可以使用这种KR row这种对数据进行一些序列化常规类型我们用到的其实
[04:36] 在我们实际工作或者实际的这种开发过程中用到的不太多像我们的这种原族类型和我们的普及类型用到的相对来讲比较多一点那第五种类型的话是一个直类型这种直类型其实就是一个具体的一个数值这种数值的话和我们的这种和前面提到的基础的基本的基础的数据类型稍微有一点点不太一样直类型的话它是手工描述和序列化
[05:06] 其序列化和反序列化的它们不是通过通用框架通用的序列化框架产生的而是通过这种比如说我们的Flink type的一个value使其方法进行读取和写入的一些方法这一类数据这些数据它充当了一些基本数据类型的一些可变的变体比如说我们的它们的值呢可以被变更那允许我们程序的方式通过重新的方式
[05:35] 重用对象啊并且从垃圾收集器里面消除一些压力那第六种类型的话就是我们针对于数据的一个存储比如说数据我要想把它存储到Hadoop HDFS里面那么就有一个Hadoop的Writeable的一个这种数据类型刚才也提到了常用的我们在写程序里面比较常用的就是我们的原组类型然后包括我们的Pojo类型以及我们的常规的基础数据类型
[06:03] 这些类型是我们在我们开发Flink程序里边比较常用的那其他那些类型的话也会有一些不同的适用场景比如说Hadoop的redbaud这种数据类型我们实际上要把这种数据的结果要存储到HDFS数据库里边去的这是我们对于整个我们的Flink的数据类型的一个理解那么理解了Flink的数据类型那么我们下一步就可以开发我们的Flink的一些程序了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Flink 中 DataStream 支持的六种数据类型，包括元组、POJO、基础类型、常规类、值和 Hadoop Writables。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Flink 数据类型章节标题，列出六种数据类型：1. Java元组和Scala案例类，2. Java POJO，3. 原始类型，4. 常规类，5. 值，6. Hadoop Writables。同时展示一个流程图，包含四个步骤：1. 基于单条记录 filter/map，2. 基于时间窗口 window，3. 合并数据流 Union, join, connect，4. 拆分数据流 split。
画面 2: 展示 2.2.1 元组章节，代码示例：DataStream<Tuple2<String, Integer>> wordCounts = env.fromElements( new Tuple2<String, Integer>("hello", 1), new Tuple2<String, Integer>("world", 2)); wordCounts.map(new MapFunction<Tuple2<String, Integer>, Integer>() { @Override public Integer map(Tuple2<String, Integer> value) throws Exception { return value.f1; } });
画面 3: 在画面 2 的代码基础上，添加了 wordCounts.keyBy(0); // also valid .keyBy("f0")。
画面 4: 展示 2.2.1 元组章节末尾，过渡到 2.2.2 POJOs 章节标题。
画面 5: 展示 2.2.2 POJOs 章节，列出 POJO 的要求：类必须公开类，它必须有一个没有参数的公共构造函数（默认构造函数），所有字段都是公共的，或者必须通过 getter/setter 访问，注解的序列化程序必须支持字段的类型。并展示一个 WordWithCount 类的代码示例。
画面 6: 在画面 5 的代码基础上，添加了构造函数 public WordWithCount(String word, int count) { this.word = word; this.count = count; }。
画面 7: 展示 2.2.2 POJOs 章节末尾，过渡到 2.2.3 基础数据类型章节标题。
画面 8: 展示 2.2.3 基础数据类型章节，内容为：Flink 支持所有 Java/Scala 的原始类型，如 Integer，String 和 Double。并展示 2.2.4 常规类章节标题。
画面 9: 展示 2.2.2 POJOs 章节末尾，过渡到 2.2.3 基础数据类型章节标题。
画面 10: 展示 2.2.4 常规类章节，内容为：Flink 支持大多数 Java/Scala 类（API 自定义），限制适用于包含无法序列化的字段的类，如文件指针，I/O 流或其他非机资源。遵循 Java Beans 约定的类通常可以很好地工作。所有未标记为 POJO 类型的类都由 Flink 作为常规类型处理。Flink 将这些数据类型视为黑盒子，并且无法访问其内容（例如，用于有效排序）。使用序列化框架 Kryo 对常规类型进行反序列化。
画面 11: 展示 2.2.5 值章节，内容为：值类型手动描述序列化和反序列化。它们不是通过通用序列化框架，而是通过 org.apache.Flink.types.Value 使用方法 read 和实现接口为这些类型提供自定义代码 write。当通用序列化效率非常低时，使用值类型是合理的。一个示例将元素的顺序与数组类型实现。知道数组大部分为窄，可以对非零元素使用特殊编码，而通用序列化只涵盖所有数组元素。并展示 Flink 与基本数据类型对应的定义值类型：(ByteValue, ShortValue, IntValue, LongValue, FloatValue, DoubleValue, StringValue, CharValue, BooleanValue)。
画面 12: 展示 2.2.2 POJOs 章节末尾，过渡到 2.2.3 基础数据类型章节标题。
画面 13: 展示 2.2.3 基础数据类型章节，内容为：Flink 支持所有 Java/Scala 的原始类型，如 Integer，String 和 Double。并展示 2.2.4 常规类章节标题。
画面 14: 展示 2.2.1 元组章节，代码示例：DataStream<Tuple2<String, Integer>> wordCounts = env.fromElements( new Tuple2<String, Integer>("hello", 1), new Tuple2<String, Integer>("world", 2)); wordCounts.map(new MapFunction<Tuple2<String, Integer>, Integer>() { @Override public Integer map(Tuple2<String, Integer> value) throws Exception { return value.f1; } });

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
DataStream<Tuple2<String, Integer>> wordCounts = env.fromElements(
new Tuple2<String, Integer>("hello", 1),
new Tuple2<String, Integer>("world", 2));
wordCounts.map(new MapFunction<Tuple2<String, Integer>, Integer>() {
@Override
public Integer map(Tuple2<String, Integer> value) throws Exception {
return value.f1;
}
});

画面 3:
wordCounts.keyBy(0); // also valid .keyBy("f0")

画面 5:
public class WordWithCount {
public String word;
public int count;
public WordWithCount() { }
public WordWithCount(String word, int count) {
this.word = word;
this.count = count;
}
}

画面 6:
DataStream<WordWithCount> wordCounts = env.fromElements(
new WordWithCount("hello", 1),
new WordWithCount("world", 2));
wordCounts.keyBy("word"); // key by field expression "word"

画面 8:
Flink 支持所有 Java/Scala 的原始类型，如 Integer，String 和 Double。

画面 10:
Flink 支持大多数 Java/Scala 类（API 自定义），限制适用于包含无法序列化的字段的类，如文件指针，I/O 流或其他非机资源。遵循 Java Beans 约定的类通常可以很好地工作。所有未标记为 POJO 类型的类都由 Flink 作为常规类型处理。Flink 将这些数据类型视为黑盒子，并且无法访问其内容（例如，用于有效排序）。使用序列化框架 Kryo 对常规类型进行反序列化。

画面 11:
值类型手动描述序列化和反序列化。它们不是通过通用序列化框架，而是通过 org.apache.Flink.types.Value 使用方法 read 和实现接口为这些类型提供自定义代码 write。当通用序列化效率非常低时，使用值类型是合理的。一个示例将元素的顺序与数组类型实现。知道数组大部分为窄，可以对非零元素使用特殊编码，而通用序列化只涵盖所有数组元素。
Flink 与基本数据类型对应的定义值类型：(ByteValue, ShortValue, IntValue, LongValue, FloatValue, DoubleValue, StringValue, CharValue, BooleanValue)。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: 标题为“2.2 数据类型”，子标题为“Flink对DataSet或DataStream中可以包含的元素类型设置了一些限制，以便于更有效的执行策略。”，并列出六种数据类型：1. Java元组和Scala案例类，2. Java POJO，3. 原始类型，4. 常规类，5. 值，6. Hadoop Writables。流程图包含四个步骤：1. 基于单条记录 filter/map，2. 基于时间窗口 window，3. 合并数据流 Union, join, connect，4. 拆分数据流 split。
画面 5: 标题为“2.2.2 POJOs”，列出 POJO 的要求：类必须公开类，它必须有一个没有参数的公共构造函数（默认构造函数），所有字段都是公共的，或者必须通过 getter/setter 访问，注解的序列化程序必须支持字段的类型。并展示“序列化”小标题。
画面 8: 标题为“2.2.3 基础数据类型”，内容为“Flink 支持所有 Java/Scala 的原始类型，如 Integer，String 和 Double。”，并展示“2.2.4 常规类”标题。
画面 10: 标题为“2.2.4 常规类”，内容为“Flink 支持大多数 Java/Scala 类（API 自定义），限制适用于包含无法序列化的字段的类，如文件指针，I/O 流或其他非机资源。遵循 Java Beans 约定的类通常可以很好地工作。所有未标记为 POJO 类型的类都由 Flink 作为常规类型处理。Flink 将这些数据类型

