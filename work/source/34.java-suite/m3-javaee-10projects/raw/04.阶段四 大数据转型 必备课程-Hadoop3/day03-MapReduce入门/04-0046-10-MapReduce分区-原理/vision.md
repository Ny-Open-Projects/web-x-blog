# 画面线理解：10-MapReduce分区-原理

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\10-MapReduce分区-原理【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:24, 01:48, 03:45, 03:51, 04:13, 04:26, 04:44, 05:29, 05:53, 05:56, 06:17, 08:56, 10:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:57:54

1) 这一组画面整体在讲 MapReduce 的运行模式、编程规范（特别是 WordCount 示例）以及如何通过自定义 Partitioner 实现数据分区处理。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MapReduce 运行模式的讲解，包括集群运行模式的三个步骤，以及提交任务的命令：yarn jar hadoop_hdfs_operate-1.8-SNAPSHOT.jar cn.tcast.hdfs.demo1.JobMain
画面2: 展示了 MapReduce 编程规范，包括 Map、Shuffle、Reduce 阶段的步骤，以及 WordCount 的需求说明。
画面3: 展示了 WordCount 示例的 PPT 页面，包含“自定义 Partitioner”标题和相关说明文字。
画面4: 展示了 IDEA 中 WordCountMapper.java 的代码，其中包含对输入行进行分割和写入中间结果的逻辑。
画面5: 展示了 IDEA 中 WordCountMapper.java 的代码，高亮显示了 map 方法的实现。
画面6: 展示了 PPT 中的架构图，描述了 a.txt 文件被分发到 dn1、dn2、dn3 节点并由 MapTask 处理。
画面7: 展示了 PPT 中的架构图，与画面6相同，但显示了鼠标指针。
画面8: 展示了 PPT 中的架构图，与画面6相同，但画面空白。
画面9: 展示了 PPT 中的架构图，显示了 MapTask 处理后的输出结果，包括 hello、world、hadoop、java、hdfs 等单词及其计数。
画面10: 展示了 IDEA 中 WordCountReducer.java 的代码，高亮显示了 reduce 方法的实现。
画面11: 展示了 IDEA 中 WordCountReducer.java 的代码，高亮显示了 reduce 方法的实现。
画面12: 展示了 PPT 中的架构图，显示了 MapTask 的输出被发送到 ReduceTask。
画面13: 展示了 PPT 中的架构图，显示了根据单词长度对数据进行分区，不同长度的单词被发送到不同的 ReduceTask。
画面14: 展示了 PPT 中的架构图，显示了不同长度单词的统计结果被分别写入不同的文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
yarn jar hadoop_hdfs_operate-1.8-SNAPSHOT.jar cn.tcast.hdfs.demo1.JobMain

画面4:
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    Text text = new Text();
    //1:对每一行的数据进行字符串拆分
    String line = value.toString();
    String[] split = line.split(",");
    //2:遍历数组，获取每一个单词
    for (String word : split) {
        text.set(word);
        context.write(text, new LongWritable(1));
    }
}

画面10:
protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
    long count = 0;
    //1:遍历values集合
    for (LongWritable value : values) {
        //2:将集合中的值相加
        count += value.get();
    }
    //3:将结果写入上下文中
    context.write(key, new LongWritable(count));
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面3:
标题：自定义 Partitioner
说明文字：将数据放在这里，这也是这个类的意义，通过 Partitioner 将数据分发给不同的 Reducer

画面6:
标题：a.txt 300M
结构：dn1 → MapTask → dn2 → MapTask → dn3 → MapTask

画面9:
结构：dn1 → MapTask → hello 1, world 1, hello 1 → ReduceTask → dn2 → MapTask → hadoop 1, world 1, hdfs 1 → ReduceTask → dn3 → MapTask → hello 1, java 1, hadoop 1 → ReduceTask

画面12:
结构：dn1 → MapTask → hello 1, world 1, hello 1 → ReduceTask → dn2 → MapTask → hadoop 1, world 1, hdfs 1 → ReduceTask → dn3 → MapTask → hello 1, java 1, hadoop 1 → ReduceTask

画面13:
结构：dn1 → MapTask → hello 1, world 1, hello 1 → ReduceTask → dn2 → MapTask → hadoop 1, world 1, hdfs 1 → ReduceTask → dn3 → MapTask → hello 1, java 1, hadoop 1 → ReduceTask

画面14:
结构：dn1 → MapTask → hello 1, world 1, hello 1 → ReduceTask → hello 3, world 2, hadoop 1 → 文件 → dn2 → MapTask → hadoop 1, world 1, hdfs 1 → ReduceTask → hdfs 2, java 1 → 文件 → dn3 → MapTask → hello 1, java 1, hadoop 1 → ReduceTask → hello 1, java 1, hadoop 1 → 文件

5) 无
