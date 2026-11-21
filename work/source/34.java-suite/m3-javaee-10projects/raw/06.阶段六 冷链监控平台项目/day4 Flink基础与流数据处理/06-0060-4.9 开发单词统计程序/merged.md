# 4.9 开发单词统计程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.9 开发单词统计程序_【海量资源尽在 666java.com】.mp4
- 时长 11分46秒（音频 707s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们现在看一下它的一个出现的次数也就是说是一个word count的一个一个数据的一个一个过程那我们的我们定义的是什么呢我们监听socket端口然后我们统计单词的数量那还是相同的相同的这个方法那么设置执行环境定义数据语言然后再对数据进行转换处理
[00:35] 然后呢执行那在我们的这个例子里边我们要监听我们某一个socket的一个端口那现在已经监听了那么我们要统计数量单词数量这个时候我们可以定义一个数据流当中的数据的一个类型我们可以想象一下我们的如果是计算单词的数量它其实包含两个字段一个叫做单词一个叫数量所以我们可以定义一个public的一个类thetic
[01:05] 然后这个类呢叫做what with countwhat with count这个类里边它有两个函数两个属性一个叫做word词证类型的另外一个是lang型的或者inter型的我们用lang型的它数量更长更多那么这个叫count紧接着我们要定义一个public的
[01:39] 我们的叫做数据的构造函数我的位置这个构造函数我们是一个空的构造函数这后边我们会给大家介绍我们数据类型的时候我们会介绍这个地方如果是一个POJO类型的POJO类型的数据也就是数据流中的数据是一个POJO类型的那么它需要有两
[02:16] 它的这个属性是属于这种public的同时它还需要有一个我们的这种空参数的一个构造函数那我们还可以再定义另外一个叫做非空的构造函数就是参数不是空的那么string word一个参数叫word一个参数叫做count
[02:45] 那这个时候我们可以把我们的word设置设置给我们的参数了把我们传入的这个count也可以设置给我们的countOK那此时我们的有参的构造函数已经创建上了那紧接着我们还需要做一个动作就是我们需要把我们的可以把整个类型给它就是我们的toString这个方法可以复写一下
[03:18] 那托斯利用这个方法那么这个方法我们要写成什么呢我们要写成return了一个我们的word再加上加上我们的count就是打印的是word with countok那这个时候我们定义好了我们数据流中的这个数据数据类型是word with count那下一步的话我们就可以开发我们的这个执行程序了那么这个执行程序第一步设置执行环境还是
[03:53] 还是一样的不变的第二步我们要定义一个数据源而这个数据源呢其实是属于我们的这个是属于我们的一个一个strain类型的这个strain类型的我们可以看一下这个strain类型我们应该如何来来做那么我们此时拿到了一个strain类型的数据流那下一步的话我们要对这个数据流进行一个转换那么我要把它转换成什么呢
[04:24] 我要把它转换成一个我的位置count的这种类型的对吧有字有单词然后呢同时也有我们的每个单词的数量那么我们要经过第一我要data streamdata stream的类型呢是我的位置count那么这个时候我的位置count stream等于txttxt点什么呢我们要对它进行一个转换flat mapflat map我们就可以使用new flat
[04:54] my function那么在这里边的时候我们要将某一个单词给它转换成我们想要的一个结果也就是说我此时已经有了这么一个字符帅了对不对我们传输过来的实验上是这样的一个字符帅那下一步的时候我要对它进行一个怎么说呢一个拆分我要由这么一个数数据流得到的数据我要对它按照
[05:23] 回车按照空格来对它进行拆分那么所以我这个里边的数据就是包什么呢包word这个字段呢它是一个我们需要对我们的数据按空格来进行拆分的一个那拆分之后呢我得到的是我的这样的一个数组对不对我这个数组我就可以按它来进行一个
[05:53] 数组的一个数据的一个集合我collection那么我们要创建一个newword countword然后它的数据量呢每一个单词呢其实是一个一个对吧我们再简单的介绍一下这个地方可能大家需要注意一下不太好理解我们本身已经有了一个数据流了
[06:23] 这个数据流呢是我们从我们的socket对象里socket端口里面拿到的一个字符串这个字符串呢我们要想统计每一个单词的数量那我首先需要做的一步就是把整个数据流对它进行一个拆分我们按空格来进行拆分那此时我现在的这个数据呢abc abc df我要拆分成三个三个对象
[06:53] 这三个对象呢都叫做what with count那么what with count里边其中abc这个对象呢主键是abc然后呢值是1对吧我的这个word是abc然后我们的count是1那第二个也是一样第三个也是一样对吧都是word等于等于这个字符帅然后它的count等于1那执行完这个之后呢我们得到了一个字符一个数据流而这个数据流
[07:22] 中间的数据类型就变成了一个我的位置看他了对不对那下一步的时候我们要做什么操作我们都要对他按我们的主键进行一个分组我可以拜我可以拜什么呢我其实是不需要按照我的来进行k8了对吧我根据因为我现在已经有了一个新的数据流这个新的数据流的数据类型呢是我的位置看他的那么下一步呢我要对这个
[07:51] 单词按word来进行一个kby就是分组分组完了之后呢我要按时间窗口time window我要按时间窗口来进行一个求和或者说是进行一个处理那time second实际上是按每五秒钟我要处理每五秒钟我要合并一次那下一步的时候我要做什么我已经得到了
[08:17] 我已经得到了我的三个一个新的一个按照每五秒钟我得到了这样的一个已经分组好的我们的这个数据流那下一步我其实要执行那个reduce操作对不对这个reduce操作其实就是要做合并操作那么合并这个合并的话我按相同的比如说我们abc是相同abc和abc都是相同的我合并成一个那我要对于它来进行每个每个按照每个单词来进行
[08:47] 这个count的累加就是1加1加1那有几个我就加几个对吧是这么一个过程那么我现在的话就是reducereduce一个newreduce function那么这个reduce function的话我就需要定义一个新的一个我的with count了对不对因为我刚才的话是每个我的with count都是按照单词和它的数量是1来
[09:15] 进行拆分的那么我要生成一个新的what with count数据流那么这个新的what with count数据流呢就是我们需要创建一个new一个what with count而它的这个count呢是什么呢它的word呢是what with count的这个字段的word那它的count值是什么呢是what with count这个字段的count再加上新的
[09:48] 第一点这个地方需要大家好好地体会一下我本身原来是一个由单词组成的一个数据流那么我把它生成新的数据流的时候假设我第一个我第一个ABC的时候我此时就是ABC那么ABC1对不对我到了第二个的时候那其实变成了什么呢ABC2
[10:15] 因为它是前面的一个是1再加上后边的这一个1加加加等于等于2了那最后的话我们就得到了一个按单词分组之后的我们这样的一个数量了那下一步的话我们可以设置我们的what with count这个这个数据流的一个比如说我们把它打印出来那么打印出来我们还可以设置我们的并行并发度并发度是2
[10:42] 或者变化度等于1都可以变化度是执行的一个过程对吧那下一步我们就直接执行我们整个Flink程序了这就是我们针对于数据数据的一个计算或者说数据的一个转换我们从一个数据流转换成另外一个数据流那么我们再来执行一下我们这个过程那么我们先启动那下一步的时候我们把我们的客户端给它启动起来我们要连接我们的这个
[11:11] 9001的这样的就9000的这样的一个端口那执行完了之后呢我们可以输入我们相同的数据这个数据就是ABC ABCDEF对吧三个字不帅的ABC ABC空格DEF回车那此时我们就拿到得到了DEF等于1ABC等于2这个数据量是等于2了这是我们对于整个数据啊我们what we count就是我们统计单词这个
[11:41] 统一单词这个功能的一个开发

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写一个基于 Flink 的 Java 流式数据处理程序，实现对 Socket 输入数据的单词计数功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 StreamingJob.java 文件的开头部分，包含注释和 main 方法的骨架。光标位于 main 方法的开始处。
画面 2: 光标移动到 main 方法内部，开始编写代码。注释显示“监听socket端口”和“流处理”。
画面 3: 代码中添加了 Flink 环境的创建和数据源的定义，光标位于 env.socketTextStream(...) 行。
画面 4: 定义了 WordWithCount 类，用于存储单词和计数。光标位于类定义处。
画面 5: 为 WordWithCount 类添加了构造函数和成员变量的定义。
画面 6: 为 DataStream<String> text 变量添加了 flatMap 操作，光标位于 .flatMap(...) 行。
画面 7: 为 flatMap 操作选择 FlatMapFunction<String, WordWithCount> 类型。
画面 8: 为 flatMap 操作选择 .timeWindow(...) 方法。
画面 9: 为 .timeWindow(...) 方法选择 .reduce(...) 方法。
画面 10: 为 .reduce(...) 方法选择 reduce 函数。
画面 11: 为 reduce 函数选择 WordWithCount 类型。
画面 12: 为 reduce 函数选择 .print() 方法。
画面 13: 代码编写完成，显示了完整的 StreamingJob.java 文件内容。
画面 14: 切换到终端窗口，显示了 Flink 任务的执行日志和结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// For a tutorial how to write a Flink streaming application, check the
// tutorials and examples on the "a href="http://link.Spark.org/docs/stable/"Flink Website/a>.
// To package your application into a .jar file for execution, run:
// mvn clean package on the command line.
// If you change the name of the main class (with the public static void main(String[] args)
// method, change the respective entry in the POM.xml file (simply search for "mainClass").
public class StreamingJob {
```

画面 2:
```java
// 监听socket端口
// 流处理
```

画面 3:
```java
// 3. 定义数据源
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 4:
```java
public static class WordWithCount {
    public String word;
    public long count;
    public WordWithCount() {}
    public WordWithCount(String word, long count) {
        this.word = word;
        this.count = count;
    }
}
```

画面 5:
```java
public WordWithCount reduce(WordWithCount wordWithCount1, WordWithCount wordWithCount2) throws Exception {
    return new WordWithCount(wordWithCount1.word, wordWithCount1.count + wordWithCount2.count);
}
```

画面 6:
```java
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
// 3. 定义数据源
DataStream<String> text = env.socketTextStream(hostname: "172.17.0.143", port: 9000, delimiters: "\n");
```

画面 7:
```java
text.flatMap(new FlatMapFunction<String, WordWithCount>() {
    @Override
    public void flatMap(String value, Collector<WordWithCount> out) throws Exception {
        for (String word : value.split("\\s+")) {
            out.collect(new WordWithCount(word, 1));
        }
    }
});
```

画面 8:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 9:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 10:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 11:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 12:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 13:
```java
// 3. 定义数据源
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 14:
```bash
[root@node2 ~]# nc -l 9000
abc def
abc def
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

