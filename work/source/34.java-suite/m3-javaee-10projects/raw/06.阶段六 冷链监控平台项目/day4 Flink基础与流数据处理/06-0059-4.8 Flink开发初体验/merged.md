# 4.8 Flink开发初体验

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.8 Flink开发初体验_【海量资源尽在 666java.com】.mp4
- 时长 9分28秒（音频 568s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面我们学习了Flink的一个安装配置以及我们如何使用Flink安装目录下的一个示例程序来演示了我们Flink它到底能做什么样的事情而这个演示示例呢是我们监听某个socket服务器的一个端口然后实现的是我们当前的这个端口里边的一些单词数量的一个统计
[00:27] 那么下面的话我们就来以此为例来开发一个Flink的一个工程那么首先的话我们可以用我们的这个一个Mave命令来创建一下我们的一个Flink的一个工程而这个Flink当前实际上是1.9.1我们使用了就是1.9.1的这个Mave命令来创建我们的来创建我们的这个工程
[00:57] 那我们在我们的目录里边来输入一个cmd然后呢在我们cmd的目录窗口里边我们把我们的这个啊meiwei命令拷贝进去那么这个meiwei命令是mvaarchetype冒号generator也就是说它是generator生成生成我们的工程那么我们的architect group id呢是apache的Flink那么我们的
[01:25] Artifact ID是Flink-quickstart-java也是一个java的模板那么当前的一个版本是1.9.1我们点回车那此时它会给我们下载我们的Flink 1.9.1的一个快速启动的一个模板我们输入我们的group ID这group ID是com.it黑码
[01:56] 然后紧接着输入我们的artifact id这是我们工程的artifact id我们输入我们的code-blink那下面的话是我们当前的这工程的版本1.0.0我们的packagepackage包的名字比如说是com.it推码.我们的code.blink那么紧接着我们就可以在
[02:29] 按回车OK那此时我们的这个程序已经下载下来了也就是说它根据Vivy命令来专门生成了一个Flink的一个Flink的一个template的一个工具就是它的一个模板来生成我们的整个的Flink的一个示例程序那下面的话我们来打开这个示例程序我们打开ID工具
[03:01] 那此时它在加载我们的包比如说像Flink的一些包或者其他的一些包它都在加载我们程序已经加载完了那么加载完了我们先看一看程序的一个结构那首先呢它是一个java的工程这里边有两个两个java类一个叫做best job那么另外一个呢叫做streaming job那么我们看一看这个结构
[03:28] BatchJob和StreamingJob都是属于一个Main函数都有一个Main函数而Main函数里边针对于StreamingJob的话它是有一个StreamingExecutionEnvironment而对于BatchJob的话它是一个ExecutionEnvironment这两个是什么呢它是指针对于我们数据流的运行时环境一个是针对于流的运行时环境一个是针对于我们的这个叫批处理的
[03:58] 运行式环境那么我们开发一个简单的一个例子来演示一下看看是如何操作的那这一块呢我们可以先把它先先把它干掉那这个本身它的意思是注视掉的意思实际上就是我创建的这个数据流呢我对数据流进行额外的一些操作然后执行那我们把它去掉之后我们看整个的Flink程序它的执行过程
[04:28] 大致分成这么几步第一步就是构建或者说是定义设置设置我们的执行环境刚才也说了这个执行环境有这种批处理的执行环境还有我们的流逝处理的执行环境这取决于我们使用的是哪一个类那么第二步的话是我们定义数据源
[05:00] 而这个数据语言的话其实可以从文本文件里边从文件系统里边文件拿到我们的数据也可以从socket端口里边读取数据还可以从Kafka队列里边读取数据那么从文本文件里边读取数据其实就是一个静态的一个批处理那么从Kafka队列里边拿到数据就是一个流处理这个是定义数据语言那第三步的情况下其实就是我们的对数据的一个处理
[05:32] 处理数据或者叫数据的转换处理那第四步的话就是我们要执行我们的程序执行blink程序那我们看一下我们定义我们的语言我们设置执行变量执行环境刚才已经说了它包含包括这种streaming execution environment或者说叫我们的execution environment
[06:08] 那么我们定义数据源的时候我们其实当前的时候就是一个data stream那data stream是一个数据流这个数据流的话它有数据流的类型数据的类型对吧这种数据类型的话我们现在使用的是一个叫做string就是基本的数据类型加把的基本数据类型这个string那其实还可以用什么temp或者是pojo等等各种其他的这种类型temp
[06:38] 我们后边会给大家详细介绍我们的Flink它的数据源的数据类型那我定义了一个数据流这个数据流等于什么呢txt等于env.sockettextstream那么这个是什么意思呢它就是这个函数是指我们当前的执行环境里边我要读取我们某一个socket然后呢
[07:10] 把这个socket里边的数据当做我们的数据字符串然后返回过来那此时我们设置一下我们服务器的IP和端口这是IP然后呢我们有个端口比如说这个端口我们用9000然后我们再有一个分割符这个分割符的意思是说我用回车来进行分割的那此时我们就读取了我们socket端口的一个数据
[07:41] 然后把这个数据作为一个数据流返回过来得到了这个数据流那下一步的话我就对数据进行转换那这种转换我现在不做额外的转换我直接对这个数据进行一个进行一个打印也就是说此时我们要如果要做进行转换的操作的时候我们可以看一看我们这个转换操作有包含什么dit.map对吧有map有cogroup有connect
[08:12] 有Counter,Window,有Filter那么我们从这些名字里边我们现在还不太知道这些到底是什么意思但是我们从名字里边可以看出来它从一个我们的数据流那么要把它转换成另外的数据流比如说我们这个呢Filter要对它进行过滤那FlatMap呢我要从一个数据流转换成另外一个数据流那么我们现在可以稍微执行一下我们这个函数了这个方法
[08:41] 首先我需要在我们的服务里边把我们的这个端口给打开了当然现在是9000对吧我9000我就使用9000把这个端口给打开那然后呢我们可以启动我们的这个购物端的服务然后在我们的服务器端输入我们的字符串ABC ABC DEF那么我们服务启动了之后呢我们可以看一下OK
[09:12] 此时他就直接把我们的这个数据给打印出来了对吧这个是我们想要执行的一个效果那这个是我们一个基本的一个数据流数据流的一个执行情况那么所有程序的数据流执行的情况都是这样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Flink 的 SocketWindowWordCount 示例，通过命令行生成数据并用 Flink 程序进行单词统计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Flink 的 Web UI 界面，配置了 SocketWindowWordCount 示例，端口为 9010，允许恢复状态，提交按钮可用。
画面 2: 展示命令行界面，准备执行命令。
画面 3: 展示 Maven 项目创建成功，使用 Archetype `Flink-quickstart-java:1.9.1`，项目路径为 `D:\项目\cold-Flink`。
画面 4: 展示 IntelliJ IDEA 启动界面，版本为 Ultimate 2018.1。
画面 5: 展示 IntelliJ IDEA 中的项目结构，包含 `cold-Flink` 项目，`src/main/java` 目录下的 `StreamingJob` 类。
画面 6: 展示 `StreamingJob` 类的代码，包含 `StreamExecutionEnvironment env` 的初始化。
画面 7: 展示 `StreamingJob` 类的代码，注释为“1. 设置执行环境”。
画面 8: 展示 `StreamingJob` 类的代码，注释为“2. 定义数据源”。
画面 9: 展示 `StreamingJob` 类的代码，注释为“3. 数据的转换、处理”。
画面 10: 展示 `StreamingJob` 类的代码，注释为“4. 执行link”，并输入 `DataStream<String>`。
画面 11: 展示 `StreamingJob` 类的代码，弹出的补全建议中包含 `countWindowAll` 方法。
画面 12: 展示命令行界面，执行 `nc -l 9010` 命令，准备接收数据。
画面 13: 展示命令行界面，执行 `nc -l 9010` 命令，准备接收数据。
画面 14: 展示 `StreamingJob` 类的代码，执行 `env.execute(jobName)`，并显示 Flink 任务启动日志。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
[ root@node2-virtual-machine ]# nc -l 9010
abc abc def dfs def
ttt ttt qqq qqq
```

画面 3:
```
Confirm properties configuration:
groupId: com.itehima
artifactId: cold-Flink
version: 1.0.0
package: com.itehima.cold.Flink

Using following parameters for creating project from Archetype: Flink-quickstart-java:1.9.1
Parameter: groupId, Value: com.itehima
Parameter: artifactId, Value: cold-Flink
Parameter: version, Value: 1.0.0
Parameter: packageInPomFormat, Value: com.itehima.cold.Flink
Parameter: package, Value: com.itehima.cold.Flink
Parameter: version, Value: 1.0.0
Parameter: groupId, Value: com.itehima
Parameter: artifactId, Value: cold-Flink

WARNING: CP Don't override file D:\项目\cold-Flink\src\main\resources
Project created from Archetype in dir: D:\项目\cold-Flink

BUILD SUCCESS
```

画面 5:
```
cold-Flink
├── src
│   └── main
│       └── java
│           └── com.itehima.cold.Flink
│               └── StreamingJob.java
├── resources
├── pom.xml
└── target
```

画面 6:
```java
public class StreamingJob {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // Here, you can start creating your execution plan for Flink.
        // Start with getting some data from the environment, like
        // env.readTextFile(textFile)
        // then, transform the resulting DataStream<String> using operations
        // like
        // .filter()
        // .flatMap()
        // .join()
        // .groupBy()
        // and many more
    }
}
```

画面 7:
```java
public class StreamingJob {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 1. 设置执行环境
    }
}
```

画面 8:
```java
public class StreamingJob {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 1. 设置执行环境
        // 2. 定义数据源
    }
}
```

画面 9:
```java
public class StreamingJob {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 1. 设置执行环境
        // 2. 定义数据源
        // 3. 数据的转换、处理
    }
}
```

画面 10:
```java
public class StreamingJob {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 1. 设置执行环境
        // 2. 定义数据源
        // 3. 数据的转换、处理
        // 4. 执行link
        DataStream<String> text = env.socketTextStream("172.17.0.143", port: 9000, delimiter: "\n");
        text.print();
        env.execute(jobName: "Flink Streaming Java API Skeleton");
    }
}
```

画面 11:
```
map
addSink(SinkFunction<String> ...): DataStreamSink<String>
assignTimestampsAndWatermarks: SingleOutputStreamOperator<String>
assignTimestampsAndWatermarks: SingleOutputStreamOperator<String>
broadcast(VatStateDescriptor...): DataStream<String>
coGroup(DataStream<T> ...): CoGroupedStreams<String, T>
connect(DataStream<T> ...): ConnectedStreams<String, T>
connect(DataStream<T> ...): ConnectedStreams<String, T>
countWindowAll(long size, long slide): AllWindowedStream<String>
```

画面 12:
```
[ root@node2-virtual-machine ]# nc -l 9010
abc abc def dfs def
ttt ttt qqq qqq
```

画面 13:
```
[ root@node2-virtual-machine ]# nc -l 9010
```

画面 14:
```java
// 4. 执行link
DataStream<String> text = env.socketTextStream("172.17.0.143", port: 9000, delimiter: "\n");
text.print();
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

