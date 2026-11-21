# 画面线理解：1-MapReduce-计数器

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\1-MapReduce-计数器【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:23, 01:58, 02:27, 03:56, 04:54, 06:05, 07:20, 08:27, 09:33, 10:03, 10:48, 11:27, 12:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:16:37

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 MapReduce 中自定义计数器，并通过代码实现对 map 阶段输入记录数和 reduce 阶段输入键值对数的统计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Hadoop Day 04 课程的 PPT 页面，标题为“1. MapReduce 中的计数器”。
- 内容包括计数器的作用、Hadoop 内置计数器列表（MapReduce任务计数器、文件系统计数器、作业计数器）。
- 展示了 MapReduce 任务执行后的日志输出，包含 File System Counters 和 Job Counters。

画面 2：
- 展示了 SecureCRT 中的终端输出，显示了 MapReduce 任务执行成功后的日志。
- 日志内容包括 File System Counters（如 Number of bytes read/written）和 Job Counters（如 Launched map tasks, Data-local map tasks）。

画面 3：
- 展示了 SecureCRT 中的终端输出，显示了 MapReduce 任务执行后的详细性能统计。
- 内容包括 Reduce shuffle bytes、Reduce input/output records、Spilled Records、GC time elapsed、CPU time spent、Physical/Virtual memory snapshot、Peak Map/Reduce memory usage、Shuffle Errors（BAD_ID, CONNECTION）等。

画面 4：
- 展示了 Typora 中的 PPT 页面，标题为“第一种方式”。
- 内容包括实现自定义计数器的步骤：定义 MapReduce 的计数器、通过 Context 上下文对象获取计数器、在 map 函数中进行记录。
- 展示了 SortMapper.java 的代码片段，其中包含获取计数器和增加计数器的代码。

画面 5：
- 展示了 IntelliJ IDEA 中的项目结构和代码编辑器。
- 项目结构显示了 day03_mapreduce_wordcount 的目录结构，包括 src、test、target、resources 等。
- 代码编辑器中显示了 SortMapper.java 的代码，其中包含对输入数据进行拆分并写入上下文的逻辑。

画面 6：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 SortMapper.java 的代码。
- 代码中包含获取计数器的语句：Counter counter = context.getCounter("MR_COUNT", "MapReduceCounter");。
- 同时显示了 IDE 的自动补全提示，包括 Counter 类的成员方法（如 getDisplayName, getName, getValue, setValue 等）。

画面 7：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 SortMapper.java 的代码。
- 代码中包含获取计数器并增加计数器的语句：Counter counter = context.getCounter("MR_COUNT", "MapReduceCounter"); counter.increment(1);。
- 同时显示了注释说明：//对每一行数据进行拆分，然后写到PairWritable对象中，作为key和value。

画面 8：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 SortReducer.java 的代码。
- 代码中包含自定义计数器的枚举类 MyCounter，包含两个常量：REDUCE_INPUT_KEY_RECORDS 和 REDUCE_INPUT_VALUE_RECORDS。
- 代码中包含 reduce 函数的实现，用于统计 reduce 阶段的输入键值对数量。

画面 9：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 SortReducer.java 的代码。
- 代码中包含自定义计数器的枚举类 MyCounter，包含两个常量：REDUCE_INPUT_KEY_RECORDS 和 REDUCE_INPUT_VALUE_RECORDS。
- 代码中包含 reduce 函数的实现，用于统计 reduce 阶段的输入键值对数量。
- 同时显示了 IDE 的自动补全提示，包括 JobConfig 类的成员变量（如 JOB_NAME, AM_NODE_LABEL_EXP, APPLICATION_ATTEMPT_ID 等）。

画面 10：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 SortReducer.java 的代码。
- 代码中包含自定义计数器的枚举类 MyCounter，包含两个常量：REDUCE_INPUT_KEY_RECORDS 和 REDUCE_INPUT_VALUE_RECORDS。
- 代码中包含 reduce 函数的实现，用于统计 reduce 阶段的输入键值对数量。
- 同时显示了 IDE 的自动补全提示，包括 JobConfig 类的成员变量（如 JOB_NAME, AM_NODE_LABEL_EXP, APPLICATION_ATTEMPT_ID 等）。

画面 11：
- 展示了 SecureCRT 中的终端输出，显示了在软件目录下执行的命令。
- 命令包括：ls（列出文件）、rm day03_mapreduce_wordcount-1.0-SNAPSHOT.jar -f（删除 jar 文件）、rz -E（接收文件）。
- 输出显示了文件传输完成，文件大小为 11 KB。

画面 12：
- 展示了 SecureCRT 中的终端输出，显示了在软件目录下执行的命令。
- 命令包括：ls（列出文件）、rm day03_mapreduce_wordcount-1.0-SNAPSHOT.jar -f（删除 jar 文件）、rz -E（接收文件）。
- 输出显示了文件传输完成，文件大小为 11 KB。
- 同时显示了执行 Hadoop 命令：hadoop jar day03_mapreduce_wordcount-1.0-SNAPSHOT.jar cn.itcast.mapreduce_sort.JobMain。
- 输出显示了 HDFS 文件系统中 /out/sort_out 目录被移动到 /Trash/Current/out/ 目录。

画面 13：
- 展示了 SecureCRT 中的终端输出，显示了 MapReduce 任务执行后的详细性能统计。
- 内容包括 Reduce output records、Spilled Records、Shuffled Maps、Failed Shuffles、Merged Map outputs、GC time elapsed、CPU time spent、Physical/Virtual memory snapshot、Peak Map/Reduce memory usage、Shuffle Errors（BAD_ID, CONNECTION）等。
- 同时显示了自定义计数器的输出：MR_COUNT MapReduceCounter=7。

画面 14：
- 展示了 SecureCRT 中的终端输出，显示了 MapReduce 任务执行后的详细性能统计。
- 内容包括 Failed Shuffles、Merged Shuffles、GC time elapsed、CPU time spent、Physical/Virtual memory snapshot、Peak Map/Reduce memory usage、Shuffle Errors（BAD_ID, CONNECTION, IO ERROR, WRONG_LENGTH, WRONG_MAP）等。
- 同时显示了自定义计数器的输出：MR_COUNT MapReduceCounter=7。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4：
```java
public class SortMapper extends Mapper<LongWritable, Text, PairWritable, Text> {
    private PairWritable mapOutKey = new PairWritable();
    private PairWritable mapOutValue = new PairWritable();
    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //自定义他们的计数器，这里实现统计map阶段的数据记录条数
        Counter counter = context.getCounter("MR_COUNT", "MapReduceCounter");
        counter.increment(1);
        String lineValue = value.toString();
        String[] strs = lineValue.split("\t");
```

画面 5：
```java
import java.io.IOException;

public class SortMapper extends Mapper<LongWritable, Text, PairWritable, Text> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //1:对每一行数据进行拆分，然后写到PairWritable对象中，作为key和value
        String[] split = value.toString().split("\t");
        PairWritable pairWritable = new PairWritable();
        pairWritable.setFirst(split[0]);
        pairWritable.setSecond(Integer.parseInt(split[1]));
        //2:将key和value写入上下文中
        context.write(pairWritable, value);
    }
}
```

画面 6：
```java
Counter counter = context.getCounter("MR_COUNT", "MapReduceCounter");
```

画面 7：
```java
Counter counter = context.getCounter("MR_COUNT", "MapReduceCounter");
counter.increment(1);
```

画面 8：
```java
public class SortReducer extends Reducer<PairWritable, Text, PairWritable, NullWritable> {
    //自定义计数器：使用枚举
    public static enum MyCounter{
        REDUCE_INPUT_KEY_RECORDS, REDUCE_INPUT_VALUE_RECORDS
    }
    @Override
    protected void reduce(PairWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        for (Text value : values) {
            context.write(key, NullWritable.get());
        }
    }
}
```

画面 9：
```java
public class SortReducer extends Reducer<PairWritable, Text, PairWritable, NullWritable> {
    //自定义计数器：使用枚举
    public static enum MyCounter{
        REDUCE_INPUT_KEY_RECORDS, REDUCE_INPUT_VALUE_RECORDS
    }
    @Override
    protected void reduce(PairWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        context.getCounter(MyCounter.REDUCE
