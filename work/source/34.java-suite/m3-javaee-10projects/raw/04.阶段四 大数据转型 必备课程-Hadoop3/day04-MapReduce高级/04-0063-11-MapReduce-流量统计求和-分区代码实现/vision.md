# 画面线理解：11-MapReduce-流量统计求和-分区代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\11-MapReduce-流量统计求和-分区代码实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:41, 02:11, 02:40, 03:35, 03:55, 04:38, 05:13, 05:52, 06:20, 06:50, 07:46, 08:39, 09:12, 09:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:41:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hadoop MapReduce 中自定义分区器，将不同开头的手机号码分配到不同的输出文件中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示需求三“手机号码分区”的说明，以及自定义分区器 FlowPartition 的代码框架。
画面2：展示项目结构，选中 JobMain.java 文件，显示其内容为 MapReduce 作业的主入口。
画面3：在 IDE 中，用户正在编辑 FlowPartition.java 文件，准备编写自定义分区逻辑。
画面4：在 IDE 中，用户正在编写 FlowPartition.java 文件的 getPartition 方法，准备判断手机号开头。
画面5：在 IDE 中，用户正在编写 FlowPartition.java 文件的 getPartition 方法，准备添加 else if 判断。
画面6：在 IDE 中，完成 FlowPartition.java 文件的 getPartition 方法，包含对 135、136、137 开头手机号的判断逻辑。
画面7：在 IDE 中，展示 JobMain.java 文件中设置 Mapper、Reducer、输入输出格式等配置。
画面8：在 IDE 中，展示 JobMain.java 文件中设置 Reducer 的类、输出类型、Reduce 任务数和输出路径。
画面9：在 IDE 中，展示在 Maven 中执行 clean 命令，准备打包项目。
画面10：在 Linux 终端中，用户正在解压 day04_mapreduce_combiner-1.0-SNAPSHOT.jar 文件。
画面11：在 Linux 终端中，用户正在 HDFS 上删除旧的输出目录。
画面12：在 Linux 终端中，用户执行了 Hadoop jar 命令提交 MapReduce 作业。
画面13：在浏览器中，展示 HDFS 上输出文件 part-r-00000 的块信息，显示其分布在 node01、node02、node03 三个节点上。
画面14：再次展示需求三“手机号码分区”的说明和自定义分区器 FlowPartition 的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class FlowPartition extends Partitioner<Text,FlowBean> {
@Override
public int getPartition(Text text, FlowBean flowBean, int i) {
String line = text.toString();
if (line.startsWith("135")){
return 0;
}else if(line.startsWith("136")){
return 1;
}else if(line.startsWith("137")){
return 2;
}else{
return 3;
}
}
}
```

画面2：
```java
package cn.itcast.mr.flowcount_partition;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

public class FlowPartition extends Partitioner<Text,FlowBean> {
@Override
public int getPartition(Text text, FlowBean flowBean, int i) {
//为手机号以哪个数字开头然后返回不同的分区编号
if(text.toString().startsWith("135")){
return 0;
}else if(text.toString().startsWith("136")){
return 1;
}else if(text.toString().startsWith("137")){
return 2;
}else{
return 3;
}
}
}
```

画面7：
```java
//第一步：设置读取文件的类：K1 和V1
TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/flowcount"));
//第二步：设置Mapper类
job.setMapperClass(FlowCountMapper.class);
//设置Map阶段的输出类型：K2 和V2的类型
job.setMapOutputKeyClass(Text.class);
job.setMapOutputValueClass(FlowBean.class);
//第三、四、五、六步采用默认方式（分区、排序、规约、分组）
//第七步：设置文的Reducer类
job.setReducerClass(FlowCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(FlowBean.class);
```

画面8：
```java
//第七步：设置文的Reducer类
job.setReducerClass(FlowCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(FlowBean.class);
//设置Reduce的个数
job.setNumReduceTasks(4);
//第八步：设置输出的路径
TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/flowcount"));
```

画面10：
```bash
[root@node01 software]# rz waiting to receive.
```

画面11：
```bash
[root@node01 software]# hadoop jar day04_mapreduce_combiner-1.0-SNAPSHOT.jar cn.itcast.mr.flowcount_partition.JobMain
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“需求三：手机号码分区”，下方列出需求步骤。
画面14：PPT 标题为“需求三：手机号码分区”，下方列出需求步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
