# 画面线理解：11-MapReduce分区-代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\11-MapReduce分区-代码实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:06, 00:46, 03:44, 05:53, 06:34, 07:06, 07:37, 08:10, 08:36, 09:11, 10:04, 10:44, 11:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:00:43

1) 这一组画面整体在讲如何通过自定义 Partitioner 实现 Hadoop MapReduce 任务中按单词长度进行数据分区，使长度大于等于5的单词分到一个Reduce任务，小于5的分到另一个Reduce任务。

2) 按时间顺序列出每张画面的要点：
画面1：展示单词统计任务的逻辑，输入文件a.txt（300M），要求将单词长度>=5的统计结果放在一个文件中，长度<5的放在另一个文件中。图示了三个数据节点（dn1, dn2, dn3）分别经过MapTask处理后，数据流向ReduceTask，最终输出结果（hello 3, world 2, hadoop 1）。
画面2：展示Hadoop源码中HashPartitioner类的定义，用于默认的分区逻辑。
画面3：展示自定义Partitioner类PartitionOwn的初始代码框架，继承自Partitioner。
画面4：在PartitionOwn类中，开始编写getPartition方法，使用text.toString().length()判断单词长度。
画面5：完成getPartition方法的逻辑，根据单词长度判断返回0或1，分别对应第一个或第二个ReduceTask。
画面6：在JobMain类中，设置输入格式、Mapper类、输出键值类型。
画面7：在JobMain类中，设置自定义的Partitioner类PartitionOwn。
画面8：展示PartitionOwn类的完整代码，包括字段声明和getPartition方法。
画面9：在JobMain类中，设置Reducer类、输出键值类型，并设置Reduce任务数量为2。
画面10：在终端中使用rz命令上传编译好的jar包到Hadoop集群。
画面11：在终端中查看Hadoop任务提交日志，显示任务执行过程和完成状态。
画面12：在HDFS浏览器中查看文件part-r-00000，显示其Block信息，包括Block ID、Block Pool ID、大小和可用节点。
画面13：在HDFS浏览器中查看文件part-r-00001，显示其Block信息，包括Block ID、Block Pool ID、大小和可用节点。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```java
package org.apache.hadoop.mapreduce.lib.partition;
import ...
@Public
@EStable
public class HashPartitioner<K, V> extends Partitioner<K, V> {
    public HashPartitioner() {
    }
    @Override
    public int getPartition(K key, V value, int numReduceTasks) {
        return (key.hashCode() & 0x7fffffff) % numReduceTasks;
    }
}
```

画面3：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner {
}
```

画面4：
```java
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner<Text, LongWritable> {
    Text text; // 表示K1
    LongWritable longWritable; // 表示V2
    int reduce个数;
    @Override
    public int getPart...
    if(text.toString().length() >= 5){
        return 0;
    }else{
        return 1;
    }
}
```

画面5：
```java
@Override
public int getPartition(Text text, LongWritable longWritable, int i) {
    if(text.toString().length() >= 5) {
        return 0;
    } else {
        return 1;
    }
}
```

画面6：
```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        //打包放在私有空间时，需要做一个配置
        job.setInputFormatClass(TextInputFormat.class);
        //第一步：设置输入文件的路径
        TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/wordcount"));
        //第二步：设置Mapper类
        job.setMapperClass(WordCountMapper.class);
        //设置Map阶段的输出类型：K2 和V2的类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        //第三、四、五、六步采用默认方式（分区，排序，规约，分组）
        //设置我们的分区类
        job.setPartitionerClass(PartitionerOwn.class);
```

画面7：
```java
//第七步：设置文的Reducer类
job.setReducerClass(WordCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//第八步：设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
```

画面8：
```java
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;
public class PartitionerOwn extends Partitioner<Text, LongWritable> {
    Text text; // 表示K1
    LongWritable longWritable; // 表示V2
    int reduce个数;
    @Override
    public int getPartition(Text text, LongWritable longWritable, int i) {
        //如果单词的长度 >= 5,进入第一个分区 ——第一个reduceTask ——reduce编号是0
        if(text.toString().length() >= 5){
            return 0;
        }else{
            //如果单词的长度 < 5,进入第二个分区 ——第二个reduceTask ——reduce编号是1
            return 1;
        }
    }
}
```

画面9：
```java
//第七步：设置文的Reducer类
job.setReducerClass(WordCountReducer.class);
//设置Reduce阶段的输出类型
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(LongWritable.class);
//第八步：设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
//设置Reduce的个数
job.setNumReduceTasks(2);
```

画面10：
```bash
[root@node01 software]# rz -E
rz waiting to receive.
? a? zmodem ??.
Ctrl+C ??
Transferring day03_mapreduce_wordcount-1.0-SNAPSHOT.jar...
100% 6 KB 6 KB/s 00:00:01 0 ?
```

画面11：
```bash
2019-05-01 11:11:02,835 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/root/.staging/job_1556425124335_0013
2019-05-01 11:11:03,193 INFO input.FileInputFormat: Total input files to process : 1
2019-05-01 11:11:03,345 INFO mapreduce.JobSubmitter: number of splits:1
2019-05-01 11:11:03,387 INFO Configuration: deprecation: system.metrics-publisher.enabled is deprecated. Instead, use yarn.system-metrics-publisher.enabled
2019-05-01 11:11:03,615 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1556425124335_0013
2019-05-01 11:11:03,617 INFO mapreduce.JobSubmitter: Executing with tokens: []
2019-05-01 11:11:03,619 INFO conf.Configuration: resource-types.xml not found
2019-05-01 11:11:03,909 INFO impl.YarnClientImpl: Submitted application application_1556425124335_0013
2019-05-01 11:11:04,054 INFO mapreduce.Job: Running job: job_1556425124335_0013
2019-05-01 11:11:04,056 INFO mapreduce.Job: Job job_1556425124335_0013 running in uber mode : false
2019-05-01 11:11:04,056 INFO mapreduce.Job:  map 0% reduce 0%
2019-05-01 11:11:21,496 INFO mapreduce.Job:  map 100% reduce 100%
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：架构图，展示数据从dn1、dn2、dn3流向MapTask，再流向ReduceTask，最终输出结果。
画面6：代码注释中提到“第二步：设置Mapper类”、“第三、四、五
