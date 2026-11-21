# 画面线理解：16-MapReduce排序-集群运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\16-MapReduce排序-集群运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:23, 01:06, 01:40, 01:58, 02:09, 02:25, 02:45, 03:03, 03:30, 03:36, 03:46, 03:59, 04:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:13:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hadoop集群上编写、打包并运行一个MapReduce程序，实现对文本数据的排序和词频统计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在IDE中展示MapReduce程序JobMain.java的代码，其中设置了输入格式、Mapper和Reducer类。同时显示了项目结构和编译成功。
画面2：展示PPT内容，讲解MapReduce的序列化和排序机制，包括Writable接口的作用和数据示例。
画面3：在SecureCRT中执行HDFS命令，创建输入目录：hdfs dfs -mkdir /input。
画面4：在IDE中执行Maven的package命令，准备打包项目。
画面5：在IDE中执行Maven的install命令，将项目安装到本地仓库。
画面6：在SecureCRT中使用rz命令准备上传jar包，弹出文件选择对话框。
画面7：在SecureCRT中使用rz命令上传jar包，显示传输进度。
画面8：在IDE中右键点击JobMain.java，选择“Run 'JobMain'”运行程序。
画面9：在SecureCRT中执行Hadoop命令提交作业：hadoop jar day03_mapeuduce_wordcount-1.0-SNAPSHOT.jar cn.itcast.mapeuduce_sort.JobMain。
画面10：在SecureCRT中显示作业提交成功并运行的详细日志。
画面11：在Hadoop Web UI的Browse Directory页面，查看HDFS中的文件列表。
画面12：在Hadoop Web UI中点击文件part-r-00000，查看其块信息，显示该文件分布在多个节点上。
画面13：在Excel中打开下载的排序结果文件part-r-00000，显示排序后的数据。
画面14：在Excel中查看排序后的数据，确认结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码：
```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_sort");
        //打包放在集群运行时，需要一个配置
        job.setJarByClass(JobMain.class);
        //第一步：设置读取文件的格式：K1 V1
        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("hdfs://node01:8000/input/sort"));
        //第二步：设置Mapper类
        job.setMapperClass(SortMapper.class);
        //设置Map阶段的输出类型：k2 和v2的类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);
        //第三步，第四步，第五步，第六步采用默认方式（分词，排序，约分，分组）
        //第二步，设置文的Reducer类
        job.setReducerClass(SortReducer.class);
        //设置输出格式
        job.setOutputFormatClass(TextOutputFormat.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        //设置分组比较器
        job.setGroupingComparatorClass(TextComparator.class);
        //设置分区器
        job.setPartitionerClass(MyPartitioner.class);
        //设置reduce任务数
        job.setNumReduceTasks(2);
        boolean b = job.waitForCompletion(true);
        return b ? 0 : 1;
    }
}
```

画面3命令：
```bash
[root@node01 servers]# hdfs dfs -mkdir /input
```

画面4命令：
```bash
mvn package
```

画面5命令：
```bash
mvn install
```

画面6命令：
```bash
rz -E
```

画面7命令：
```bash
rz -E
```

画面9命令：
```bash
hadoop jar day03_mapeuduce_wordcount-1.0-SNAPSHOT.jar cn.itcast.mapeuduce_sort.JobMain
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2PPT标题：
6. MapReduce序列化和排序

PPT内容：
- 序列化(Serialization)是把结构化对象转化为字节流。
- 反序列化(Deserialization)是把字节流转化为对象，当在进程间传递对象或持久化对象的时候，就需要把对象序列化为字节流。反之当要接收字节流时，就要进行反序列化。
- Java的序列化(Serializable)是一个重量级序列化，一个对象被序列化后，会携带很多额外的信息（各种检验信息、header、继承体系等），不适合在网络中传输。所以Hadoop自己开发了一套序列化机制(Writable)。精确高效。不像Java对象一样传输多层的父子关系，需要加非特性数据传输的开销。
- Writable是Hadoop的序列化格式，Hadoop定义了这样一个Writable接口，一个类只要支持可序列化只需实现这个接口即可。
- 另外Writable有一个接口是WritableComparable。WritableComparable是可实现排序，也可以对key进行比较。我们这里可以通过自定义Key实现WritableComparable来实现我们的排序功能。

数据格式如下：
```
a 1
a 5
a 7
a 9
b 3
b 8
b 10
```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
