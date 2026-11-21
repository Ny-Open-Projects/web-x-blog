# 画面线理解：3-MapReduce-Combiner规约-代码实现

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\3-MapReduce-Combiner规约-代码实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:54, 01:47, 02:57, 04:34, 05:40, 06:33, 07:28, 08:11, 09:12, 10:19, 11:15, 11:52, 12:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:21:03

1) 这一组画面整体在讲什么（一句话）：
讲解 Hadoop MapReduce 中 Combiner 的作用、实现步骤及与 Reduce 的区别，并通过代码和流程图对比演示使用 Combiner 前后的数据传输和处理效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程 PPT 的标题页，内容为“Hadoop Day 04”，并列出了本节内容：1. MapReduce 中的计数器、2. 约定 Combiner、3. 低置信度。
- PPT 中详细介绍了 Combiner 的作用：对 map 端的输出先做一次合并，以减少 map 和 reduce 节点之间的网络传输，提高网络 IO 性能。
- 列出了 Combiner 的关键点：是 MR 框架中 Mapper 和 Reducer 之外的一种组件；其组件的父类是 Reducer；运行位置在每个 maptask 节点；作用是每个 maptask 输出的中间结果做局部汇总。

画面2：
- 展示了 IntelliJ IDEA 中的 Maven 项目结构，项目名为 “day04_mapreduce_wordcount”。
- 显示了 `pom.xml` 文件中的依赖配置，其中包含：
  ```xml
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
  <repositories>
      <repository>
          <id>cloudera</id>
          <url>https://repository.cloudera.com/artifactory/cloudera-repos/</url>
      </repository>
  </repositories>
  <dependencies>
      <dependency>
          <groupId>org.apache.hadoop</groupId>
          <artifactId>hadoop-common</artifactId>
          <version>3.1.1</version>
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

画面3：
- 展示了 `JobMain.java` 文件中的代码，用于设置 MapReduce 作业的配置。
- 代码中设置了 Reducer 类、输出键值类型、输出路径等：
  ```java
  job.setReducerClass(WordCountReducer.class);
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(LongWritable.class);
  job.setOutputFormatClass(TextOutputFormat.class);
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount"));
  boolean b = job.waitForCompletion(true);
  ```

画面4：
- 展示了电脑桌面，有“黑马程序员”和“博学谷”的标志，以及一些文件图标，如 `day03_map...`、`MapReduce.bmp` 等。

画面5：
- 展示了 SecureCRT 中的 Linux 命令行界面，用户在 `software` 目录下执行 `rz` 命令上传文件。
- 弹出的文件传输对话框显示了上传文件的选项。

画面6：
- 展示了 SecureCRT 中的错误日志，显示了 Hadoop YARN 的异常堆栈信息，主要涉及 `SerializedExceptionPBImpl` 和 `ContainerLauncherImpl`。

画面7：
- 展示了 SecureCRT 中的命令行界面，用户执行了 `ntpdate` 命令同步时间，并删除了 HDFS 中的 `wordcount_out` 目录：
  ```bash
  crontab: no changes made to crontab
  [root@node01 software]# /usr/sbin/ntpdate ntp4.aliyun.com
  2 May 12:55:27 ntpdate[33435]: step time server 203.107.6.88 offset 40564.628326 sec
  2 May 12:55:37 ntpdate[33438]: adjust time server 203.107.6.88 offset -0.019597 sec
  [root@node01 software]# hdfs dfs -rm -r /wordcount_out
  ```

画面8：
- 展示了 MapReduce 作业的执行结果，显示了 Map 和 Reduce 的输入输出记录数、字节数、GC 时间等统计信息：
  ```
  Map input records=4
  Map output records=8
  Map output bytes=114
  Map output materialized bytes=136
  Input split bytes=107
  Combine input records=0
  Combine output records=0
  Reduce input groups=3
  Reduce input records=8
  Reduce output records=3
  Spilled Records=16
  Shuffled Maps=1
  Failed Shuffles=0
  Merged Map outputs=1
  GC time elapsed (ms)=214
  CPU time spent (ms)=2670
  Physical memory =659763200
  ```

画面9：
- 展示了 IntelliJ IDEA 中的 `JobMain.java` 文件，用户正在创建一个新类 `WordCountReducer`。
- 代码中设置了 MapReduce 作业的配置，包括设置输入输出格式、Mapper 和 Reducer 类等。

画面10：
- 展示了 `WordCountReducer.java` 文件中的代码，用于实现 Reduce 方法。
- 代码中定义了 `reduce` 方法，用于遍历值集合、累加值、写入上下文：
  ```java
  protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException {
      long count = 0;
      //1:遍历values集合
      for (LongWritable value : values) {
          //2:将集合中的值相加
          count += value.get();
          //3:将结果写入上下文中
          context.write(key, new LongWritable(count));
      }
  }
  ```

画面11：
- 展示了 `JobMain.java` 文件中的代码，用户正在设置 Combiner 类。
- 代码中设置了 Combiner 类为 `MyCombiner`，并设置了 Reducer 类和输出键值类型：
  ```java
  //第七步：设置的Reducer类
  job.setReducerClass(WordCountReducer.class);
  //设置Reducer的个数
  job.setNumReduceTasks(1);
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount"));
  ```

画面12：
- 展示了 SecureCRT 中的命令行界面，用户执行了 `rm` 命令删除了本地的 JAR 文件，并使用 `rz` 命令上传了新的 JAR 文件。
- 命令行显示了文件传输的进度和最终的文件列表。

画面13：
- 展示了 MapReduce 作业的执行结果，显示了 Map 和 Reduce 的输入输出记录数、字节数、GC 时间等统计信息：
  ```
  Total vcore-milliseconds taken by all reduce tasks=4814
  Total megabyte-milliseconds taken by all map tasks=4472832
  Total megabyte-milliseconds taken by all reduce tasks=4929536
  Map input records=4
  Map output records=8
  Map output bytes=114
  Map output materialized bytes=55
  Input split bytes=107
  Combine input records=0
  Combine output records=3
  Reduce input groups=3
  Reduce input records=8
  Reduce output records=3
  Spilled Records=1
  Failed Shuffles=0
  Merged Map outputs=1
  ```

画面14：
- 展示了流程图，对比了“没有使用规约”和“使用规约”两种情况下的数据传输过程。
- 图中显示了三个数据节点（dn1、dn2、dn3）分别通过 MapTask 处理数据，然后通过网络传输到 ReduceTask。
- “没有使用规约”时，Reduce 输入记录数为 8，输出记录数为 3。
- “使用规约”时，Reduce 输入记录数为 3，输出记录数为 3。
- 图中还显示了 Combiner 在 MapTask 后对数据进行局部汇总，减少了网络传输量。
