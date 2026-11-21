# 画面线理解：15-MapReduce排序-其他代码编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\15-MapReduce排序-其他代码编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:44, 02:20, 03:44, 04:30, 05:05, 06:10, 07:56, 08:36, 09:41, 10:29, 11:24, 12:03, 12:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:11:03

1) 这一组画面整体在讲如何使用 Hadoop MapReduce 编写一个自定义排序程序，包括自定义 Mapper、Reducer 和 Job 配置。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，当前编辑的是 SortMapper.java 文件，位于 cn.itcast.mrproduce_sort 包下。
画面2：在 SortMapper.java 中导入 Hadoop 相关包，并定义类 SortMapper 继承 Mapper<LongWritable, Text, PairWritable, Text>。
画面3：展示 MapReduce 的执行流程图，包括 Map、Shuffle、Reduce 阶段，以及自定义的 PairWritable 类实现 WritableComparable 接口。
画面4：在 SortMapper.java 中编写 map 方法，对输入的每一行按空格分割，将第一个字段作为 key，第二个字段作为 value，封装成 PairWritable 对象。
画面5：在 SortReducer.java 中定义类 SortReducer 继承 Reducer<PairWritable, Text, PairWritable, NullWritable>。
画面6：在 SortReducer.java 中设置输入和输出类型，输入为 PairWritable 和 Text，输出为 PairWritable 和 NullWritable。
画面7：展示 MapReduce 执行流程图，包括 Map、Shuffle、Reduce 阶段，以及自定义的 PairWritable 类实现 WritableComparable 接口。
画面8：在 JobMain.java 中导入 Hadoop 相关包，并定义类 JobMain 继承 Configured implements Tool。
画面9：展示 ToolRunner 类的源码，用于解析命令行参数并设置 Configuration。
画面10：在 JobMain.java 中编写 run 方法，创建 Job 实例并设置相关配置。
画面11：在 JobMain.java 中编写 main 方法，创建 Configuration 实例，调用 ToolRunner.run 方法执行 Job。
画面12：在 JobMain.java 中设置 Mapper 类为 SortMapper，设置 Map 阶段的输出类型为 K2 和 V2。
画面13：在 JobMain.java 中设置 Reducer 类为 SortReducer，设置 Reduce 阶段的输出类型为 K3 和 V3。
画面14：在 JobMain.java 中设置 Reducer 类为 SortReducer，设置 Reduce 阶段的输出类型为 K3 和 V3。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
```
画面4：
```java
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    //对每一行数据进行拆分，然后分别找到PairWritable对象，作为key和value
    String[] split = value.toString().split("\t");
    PairWritable pairWritable = new PairWritable();
    pairWritable.setFirst(split[0]);
    pairWritable.setSecond(Integer.parseInt(split[1]));
    //将K1和V2写入上下文中
```
画面5：
```java
import org.apache.hadoop.mapreduce.Reducer;
```
画面6：
```java
import org.apache.hadoop.mapreduce.Reducer;
```
画面8：
```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
```
画面10：
```java
public int run(String[] strings) throws Exception {
    Job job = Job.getInstance(super.getConf(), "mapreduce_sort");
    job.setJarByClass(JobMain.class);
    job.setInputFormatClass(TextInputFormat.class);
    TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/sort"));
    job.setMapperClass(SortMapper.class);
    job.setMapOutputKeyClass(PairWritable.class);
    job.setMapOutputValueClass(Text.class);
    job.setPartitionerClass(PartitionerOwn.class);
    job.setReducerClass(SortReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(LongWritable.class);
    job.setNumReduceTasks(2);
    job.setOutputFormatClass(TextOutputFormat.class);
    TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));
    boolean b = job.waitForCompletion(true);
    return b ? 0 : 1;
}
```
画面11：
```java
public static void main(String[] args) throws Exception {
    Configuration configuration = new Configuration();
    int run = ToolRunner.run(configuration, new JobMain(), args);
    System.exit(run);
}
```
画面12：
```java
//第二步，设置Mapper类
job.setMapperClass(SortMapper.class);
//设置Map阶段的输出类型：K2 和V2的类型
job.setMapOutputKeyClass(PairWritable.class);
job.setMapOutputValueClass(Text.class);
//第三、四、五、六步采用默认方式（分区，排序，规约，分组）
job.setPartitionerClass(PartitionerOwn.class);
```
画面13：
```java
//第七步，设置定义的Reducer类
job.setReducerClass(SortReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//设置Reduce的个数
job.setNumReduceTasks(2);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：标题为“MapReduce执行流程图”，包含输入文件、Map阶段、Shuffle阶段、Reduce阶段。
输入文件指向 Map 阶段，Map 阶段指向 Shuffle 阶段，Shuffle 阶段指向 Reduce 阶段。
画面7：标题为“MapReduce执行流程图”，包含输入文件、Map阶段、Shuffle阶段、Reduce阶段。
输入文件指向 Map 阶段，Map 阶段指向 Shuffle 阶段，Shuffle 阶段指向 Reduce 阶段。

5) 不要评价画面美观，不要输出与课程无关的内容。
