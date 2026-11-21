# 4.15 Flink数据流编程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.15 Flink数据流编程_【海量资源尽在 666java.com】.mp4
- 时长 17分12秒（音频 1032s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来学习一下Flink Data Stream编程那么我们前面提到了Flink的数据流呢分成两大类一类叫做Data Stream一类叫做Data Set那么Data Stream呢是属于我们的这种流数据或者叫流逝数据那么Data Set呢是属于P数据那么我们现在呢给大家讲解我们的流数据的一个处理编程的一个思想编程的一个原理
[00:26] 那么批数据的dataset的数据处理呢我们在后边给大家讲解那么流数据处理的方式我们先看一下我们整个的一个大致的一个过程那首先的话呢这是我们的一个Flink那Flink的话我们把它理解为就是要处理数据的一个数据工厂那相应的我们是有一批数据要进来的对吧这种数据的话有可能是属于我们的叫datastream
[00:56] 或者说要叫流数据流数据那还有的话可能是说我们的批量的数据对吧批数据那么流数据就是data stream那批数据就是data set那下一个来讲的话我们在Flink里边实际上就是叫做计算了那计算完的结果我们要对它进行流出那流出的时候我们需要可以往它流出到什么呢比如说master code数据库里边
[01:32] 那我还可以流出到我们的卡普卡里边或者是流出到其他的文本文件或者socket某个端口等等各种各样的我们可以把它流出到各种各样的一个地方那针对于这个过程实际上就是三部分了第一部分来讲的话叫做数据的输入输入输入流那中间部分叫做数据的转换转换或操作吧
[02:07] 那第三部分的话叫做输出流所以无论是我们的流数据还是后边我们讲的批数据它的整个的过程都是输入流数据的转换操作数据的输出流就是这样的一个过程我们先看一看我们流数据的一个输入流那么流数据的输入流它的内容或者说输入流的输入是从哪来的呢我们可以用streamexecutionenvironment这个环境变量来添加一个用这个方法
[02:43] add sourceadd source呢我们这个source可以基于的也就是说我们的文件的输入流这种输入流到底是有什么东西呢我们可以用基于文件的也就是说我在这个地方这种输入流的数据我们可以是我们的文件那还可以是什么呢还可以是我们的socket或者是我们的java的一个集合还有什么还有我们自己定义的一些方式对吧
[03:22] 这是我们的输入流那不同的方式我们其实有不同的方法比如说我要定义一个文件的那其实就是我们用Evident的StreamExecutionEvident然后ReadTextFile这样的一个方法那么就能够逐行的读取文本文件那么把他们以字符串的方式返回
[03:47] 那返回就给了我们的一个叫什么呢给了我们一个给了stream对吧这是我们还有另外的话我们可以通过read file那么按照指定的格式来返回文件这些方法呢都是我们通过这种文件的方式那么读取文件内容那第二类的话是基于我们的socket这种socket的话是说我们可以读取我们的
[04:18] 一个某一个端口里边的socket那么我们前面也给大家讲了我们的针对于我们单词统计的这样的一个事例它就是针对于我们的这个socket端口来读取的数据那第三类的话其实就是一个Java的一个集合对象那么Java集合对象的创建方式相对来讲也比较简单一些那么我们后边也会给大家做一些相应的一些讲解
[04:48] 那我们再看一看第二种那就是数据的一个转换操作数据的转换操作的话其实对于数据流对于流数据那它的转换方式其实是有很多种我们前面也提到了数据类型的数据的一个操作那么这种操作更多的是我们对于数据类型的一个转换那比如说我们可以通过map的方式来进行转换这种转换的话是我们
[05:17] 由一个datastream转换成另外一个datastream就是中间的这个这个map的方法那么调用我们自己定义的map function然后呢形成新的一个datastream也就是说这里边的这个代码例子里边的我开始的时候有一个datastreamdatastream里边的数据呢是一个整形的那我经过一个map之后
[05:46] Map的方法是什么呢我返回原值乘以2也就是说把原来的一个整形的数据流我把它转换成另外一个数据流而数据流的内容呢是原来原值的一个乘以2二倍那第二种的话叫FlatMapFlatMap它也是把我们的一个DataStream转换成另外一个DataStream那么它的主要作用呢是对于输入的元素处理后生成一个或者多个元素
[06:16] 我们比如看看下面这个例子我们将我们的某一个单词我们用空格来进行拆分拆分之后呢形成一个新的数据流那么这个新的数据流呢就是一个进行拆分的一个过程那么这个就是我们的flat map那第三类的话是叫做filterfilter的话是我们把
[06:43] 数据流按照某一种条件来过滤那么过滤之后其实就相当于是原来数据流的一个子集那么在这种情况下我们由一个数据流转换成另外一个更小的数据流比如我们看看这个例子这个例子就是一个filter的方法filter它会filter会执行一个new一个filter而new这个filter的话我们得到的是什么呢得到的是如果这个value不等于0的也就是说我们把
[07:13] 这个数据流把value等于0的给排除掉了那第四个的话KyKy是一个非常非常重要的一个数据流因为我们从前面我们介绍到的单词统计事例里边其实就用了Ky也就是说我的一个数据我们按照或者说我们有某一个数据流的一个对象一个对象的数据流我们按照某一个字段的值对它进行分组那么分组之后我们就可以
[07:40] 执行别的一些操作了比如说我们可以执行合并啊求和啊等等各种各样的一些操作那么如果出现以下这种情况的时候那么这些类型其实是不能成为Kby的比如说如果它是pojo类型的但是不覆盖hashcode的方法并且依赖于我们的hashcodeobject的hashcode的这种实现这种的话是不能够这个字段是不能成为K的那
[08:07] 另外一个的话它是任何类型的数组也就是说数组不能成为Kby那么成为Kby的话我们明显能想到的一个类型是什么比如说是一个磁针类型的我们就可以成为Kby对不对那第五类的话叫ReduceReduce的话和Kby一般结合起来用的比较多一些比如我们把某一个数据流某一个Kby的一个K的一个数据流
[08:36] 我们按照进行某一个主件进行分组之后我要按照主件相同的这些数据我要对它进行求和累加甚至于做其他的计算这也就叫做一个reduce的一个过程它的这个reduce过程和Hadoop体系里面的MapReduce的方式和原理是一样的对吧我们都是对于先拆分拆分成不同的任务然后把任务的结果给它合并出来那第六个的话叫Fold
[09:06] Food的话它是由一个KitStream到一个DataStream的一个过程它是具有初始值的建控数据流上的一个滚动的折叠也就是说我们当出现一个序列比如说像这种的时候我们的数据有一些重叠的部分的时候我们需要对它一个滚动的一个折叠的一个部分比如我们现在start-1start-1-2start-1-3这些地方的时候我们其实可以把前面的这几个都给它折叠起来的
[09:34] 那第七类类型类型的话叫aggregationaggregation实际上叫做聚合的那么它是由一个k的stream到一个data stream的一个转换它的这种转换的话比如我们是滚动聚合数据流上的一些聚合也就是说我们针对于结果进行一个结果进行处理那另外一个是windowwindow的话就是我们针对于k的stream到一个window的stream的一个
[10:03] 一个处理我们先进行了一些分组分组之后呢我们在时间窗口内进行一些计算比如说五秒钟内到达的一些数据那还有一个就是windowallwindowall是把我们的这个detstream转换成allwindow的streamwindow可以是常规的detstream上的一些定义window根据某些特征比如最后到达五秒钟到达的一些数据对所有数据流事件进行一些分组
[10:33] 那么有一种情况呢很多情况是并行的一些转换第十个是window的apply这个方法这个方法的话会把我们的window的stream转变成delta stream或者是把all window stream转换成stream这些功能呢它这个功能是把应用于整个窗口的我们整个窗口的一个应用的一个转换那还有一个就是我们针对于window的reduce
[11:01] WindowReduce的话是我们真是把一个Window的stream转换成一个Window的stream的那么这种功能是减少功能用应用于窗口并返回减少的一些值第12种的话是FoodFood的话它是把Window的stream转换成DataStream它将折叠功能应用于窗口并返回折叠的值也就是说刚才我们提到的我们的12345Starter12345
[11:31] 那么我们将用的把它给折叠起来那第13个的话是我们对于windowswindows上面的也是窗口上面的一个聚合啊它是把windows的stream转换成datastream那么我们这个这个方法实际上就是聚合窗口里边的内容第14个的话是把我们就是unitunit是两个是什么两个数据集的一个合并嘛我有有一个数据集是一个
[11:58] 字符类型的另外一个字符类型的数据数据的流那么我们把两个流合成一个大的一个字符类型的数据流这是一个unit那window join的话其实是把两个也就是说这个join你可以理解为我们的类似于什么呢类似于mycircle里边的join那么我们根据一个流我们把它添加
[12:21] 我们添加上一个数据流有自转ABC另外一个数据流自转DEF那么我们合成一个数据流的话就是ABCDEF那么它和UNI大家需要注意一点的UNI的话是两个数据流的类型是一样的那第16个的话就是我们的interval joininterval join的话它是在给定时间间隔内使用公共的一个可以连接两个监控流的两个元素1和1
[12:50] 以便使我们一的一个时间和加上一个我们最小的值那么小于等于我们一二的一个最小时间或者说同时也小于等于我们的一的一个时间戳再加上我们的最大值这样的一个数量它是一个我们根据给定的时间间隔使用的一个监控流那第十七种的话是我们的co-group
[13:17] code group的话它是把两个delta stream转换成一个delta stream这种的话是有个公共的一个key有个主见的key和一个公共的实验窗口上做一个code group的一个操作那第18个的话是我们的connect就是连接嘛我们连接的话连接两个delta stream形成一个connected delta stream这种的话connected这样的一个计算主要是为了合并两种或多种不同类型的数据集
[13:46] 那么合并后会保留原来数据级的数据类型那第十九的话是call map和call flat map它呢是类似于map和flat map的第二十个的话就是slip我们在我们的这种单词统计事例里边我们给大家介绍了我们将一个标准的数据流切分成两个或更多的一个数据流第二十一个的话是我们的select
[14:15] 那么select数据流的话它是相当于是把selected的这种stream再转变成一个delta stream也就是说我们从拆分流中选择一个或多个这种数据流我们要选拆分之后我们进行选择那么第22个intervalinterval的话实际上是我们经过一个也就是说它是一个循环的一个数据流循环计算的一个数据流它将我们的一个数据流转换成interval stream
[14:44] 最后再转换成DataStream那么通过将一个运算符的输出从定向到先前的一个运算符在流中创建反馈循环第23个的话是我们的提取时间戳也就是说我们从一个DataStream到另外一个DataStream来那么第24个就是我们元素元组数据流的一个转换那么通过我们的
[15:10] 一个delta stream到另外一个delta stream的一个转换因为我们的数据的类型可能有包含原组的这种数据类型我们通过它来讲的话来进行一个转换这是我们针对于我们数据流转换的给大家的一个讲解大家可以看到这些方法其实是非常的多但是大家需要注意或者记住一点就OK了就是我们对于这个转换过程呢其实就是我们把一个数据流
[15:38] 转换成另外一个数据流的这样的一个过程那么这两个数据流我可能是说类似于原始的这个数据流转换成分组的数据流或转换成拆分的数据流等等这样的一些操作这是我们对于数据流转换的一个讲解那么下面我们来输出介绍一下输出流输出流的话是指我们将我们的数据输出输出存储到不同的
[16:08] 有不同的目的地址里比如像存储的MySQL里边存储的Kafka里边或者文件或者Socket等等这些地方那么这个输出流的话我们有很多的一些方法比如这个方法里边我们可以write as text也就是把我们的数据流直接输出成我们的这些这个文本文件或者输出成CSV文件或者是直接把它打印还可以输出到我们的Socket里边那么
[16:35] 还有另外一种非常强大的功能就是我们自定义接收器也就是说我们的AdSync这个方法这个方法的话我们可以绑定到其他的一些其他的系统里面比如像卡普卡MySQLRedis等等这些的话我们都可以通过AdSync这个方法自定义我们的接收器好了这是我们针对于今天针对于我们的Data Stream数据流编程的一个大致的一个介绍从我们的输入流到我们的
[17:08] 数据流的一个转换到我们输出流

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Flink 数据流处理的核心概念，包括输入流、数据流转换和输出流的实现方式与相关 API。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Flink 文档中“3.1 输入流”章节，介绍 SourceFunction 和基类文件（如 TextInputFormat、FileInputFormat）。
画面2：展示一个 Flink 架构图，左侧“流数据”和“批数据”指向中间“Flink 计算”框，右侧“mysql”、“Kafka”、“文件”、“socket”等指向“Flink 计算”框。
画面3：在画面2基础上，添加了“输入流”、“数据转换或操作”、“输出流”三个文字标签，分别位于图中对应位置。
画面4：展示 Flink 文档中“3.1 输入流”章节，重点在“基类文件”部分，列出 TextInputFormat 和 FileInputFormat 的用法。
画面5：展示一个包含多个窗口的截图，包括“day04 - Flink 程序设计与开发.m”文档、终端窗口、文件夹结构等，用于说明开发环境。
画面6：展示 Flink 文档中“3.2 数据流转换”章节，包含一个数据流转换操作的流程图，图中包含 DataStream、KeyedStream、WindowedStream、ConnectedStream、SplitStream 等节点，以及 apply、keyBy、reduce、connect、map、split、select、coMap 等操作。
画面7：展示 Flink 文档中“3.2 数据流转换”章节，具体说明 Map、FlatMap、Filter、KeyBy 四种转换操作的代码示例。
画面8：展示 Flink 文档中“3.2 数据流转换”章节，具体说明 Fold、Aggregations 两种转换操作的代码示例。
画面9：展示 Flink 文档中“3.2 数据流转换”章节，具体说明 Window Reduce、Window Fold 两种转换操作的代码示例。
画面10：展示 Flink 文档中“3.2 数据流转换”章节，具体说明 Connect、CoMap、CoFlatMap 三种转换操作的代码示例。
画面11：展示 Flink 文档中“3.3 输出流”章节，具体说明 assignTimestamps、project 两种转换操作的代码示例。
画面12：展示一个 Flink 架构图，左侧“文件”、“Socket”、“java集合”指向中间“Flink 计算”框，右侧“mysql”、“Kafka”、“文件”、“socket”等指向“Flink 计算”框。
画面13：展示 Flink 文档中“3.3 输出流”章节，具体说明 writeAsText、writeAsCsv、print、writeUsingOutputFormat、writeToSocket、addSink 等输出操作的代码示例。
画面14：展示 Flink 文档中“3.2 数据流转换”章节，流程图与画面6相同，但下方显示了“DataStream”和“keyBy”等操作的代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
StreamExecutionEnvironment .addSource(sourceFunction)
```
画面4：
```
• readTextFile(path): TextInputFormat 逐行读取文本文件，即将会覆盖的文件，并将它们作为字符串返回。
• readFile(fileInputFormat, path): 按指定的文件输入格式读取（一次）文件。
• readFile(fileInputFormat, path, watchType, interval, pathFilter, typeInfo): 这里有两个内部调用的方法。它 path 根据指定的文件输入格式 fileInputFormat。根据提供的路径 watchType，就可以实现（每 Interval）刷新（fileInputFormat）的文件。如果使用 watchType = FileProcessingMode.PROCESS_ONCE，使用 pathFilter，用户可以进一步筛选正在处理的文件。
```
画面6：
```
1. Map: DataStream → DataStream:
  用用户自定义的 MapFunction 对 DataStream[T] 数据进行处理，形成新的 DataStream[T]，其中数据格式可能会发生变化。常用作对数据集内数据的清洗和转换。
  如下所示：它将输入的元素值增加一倍：
  DataStream<T> map(Stream<T> stream) {
  }
```
画面7：
```
2. FlatMap: DataStream → DataStream
  主要对输入的元素处理之后生成一个或者各个元素。如下示例：将予以拆分成单词：
  dataStream.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public void flatMap(String value, Collector<String> out) throws Exception {
      for(String word: value.split(" ")){
        out.collect(word);
      }
    }
  });
```
画面8：
```
6. Fold: KeyedStream → DataStream
  具有初始值的键控数据流上的“滚动”折叠，将当前元素与最后折叠的值组合并发出新值。
  折叠函数。当应用于序列（1,2,3,4,5）时，发出序列“start-1”, “start-1-2”, “start-1-2-3”...
  DataStream<String> result =
    keyedStream.fold("start", new FoldFunction<Integer, String>() {
      @Override
      public String fold(String current, Integer value) {
        return current + "-" + value;
      }
    });
```
画面9：
```
11. Window Reduce WindowedStream → DataStream
  将减少功能应用于窗口并返回减少的值。
  WindowedStream.reduce(new ReduceFunction<Tuple2<String, Integer>>() {
    public Tuple2<String, Integer> reduce(Tuple2<String, Integer> value1, Tuple2<String, Integer> value2) throws Exception {
      return new Tuple2<String, Integer>(value1.f0, value1.f1 + value2.f1);
    }
  });
```
画面10：
```
18. Connect: DataStream DataStream → ConnectedStreams
  Connect 主要是为了合并两种或者多种不同数据类型的的数据流，合并后会保留原来的数据集的类型。
  连接操作允许共享状态数据，也就是说在多个数据流之间可以操作和查看对方数据集的状态。
  DataStream<Integer> someStream = ...;
  DataStream<String> otherStream = ...;
  ConnectedStreams<Integer, String> connectedStreams = someStream.connect(otherStream);
```
画面11：
```
23. 指取时间戳：DataStream → DataStream
  从记录中提取时间戳，以便使用事件时间语义的窗口。
  stream.assignTimestamps(new FlinkTimestampExtractor {...});
```
画面13：
```
• writeAsText(...): TextOutputFormat - 按字符串顺序写入元素。通过调用每个元素的 toString() 方法获得字符串。
• writeAsCsv(...): CsvOutputFormat - 将元组写为逗分隔值文件。行和字段分隔符是可配置的。每个字段的值来自对应的 toString() 方法。
• print(): printToPrt() 在标准输出流中打印两个元素的字符串（/n）。可选，可以提供前缀（msg），其将被输出。这有助于区分不同的打印流。如果行长度大于，则输出也以生成的任意的任务的标识符为前缀。
• writeUsingOutputFormat(...): fileOutputFormat - 自定义文件输出的方法和基础。支持自定义对象到字节的转换。
• writeToSocket(...) - 将元素写入套接字 SerializationSchema
• addSink(...) - 调用自定义接收器，Flink 将其注册为连接器（如 Apache Kafka）的连接，这些系统实现为接收数据功能。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：架构图中，“流数据”和“批数据”指向“Flink 计算”框，“Flink 计算”框指向“mysql”、“Kafka”、“文件”、“socket”等。
画面3：在画面2基础上，添加了“输入流”、“数据转换或操作”、“输出流”三个文字标签，分别位于图中对应位置。
画面6：流程图中，DataStream 通过 keyBy 指向 KeyedStream，KeyedStream 通过 window 指向 WindowedStream，WindowedStream 通过 apply 指向 DataStream，DataStream 通过 split 指向 SplitStream，SplitStream 通过 select 指向 DataStream，DataStream 通过 connect 指向 ConnectedStream，ConnectedStream 通过 map 指向 DataStream，ConnectedStream 通过 coMap 指向 DataStream，ConnectedStream 通过 coFlatMap 指向 DataStream。
画面12：架构图中，“文件”、“Socket”、“java集合”指向“Flink 计算”框，“Flink 计算”框指向“mysql”、“Kafka”、“文件”、“socket”等。

5) 不要评价画面美观，不要输出与课程无关的内容。

