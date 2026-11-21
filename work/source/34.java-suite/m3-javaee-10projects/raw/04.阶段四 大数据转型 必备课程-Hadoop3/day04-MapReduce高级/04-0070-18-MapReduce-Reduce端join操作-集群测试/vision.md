# 画面线理解：18-MapReduce-Reduce端join操作-集群测试

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\18-MapReduce-Reduce端join操作-集群测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:14, 00:50, 01:12, 01:22, 01:45, 02:28, 03:20, 03:38, 03:52, 04:20, 04:41, 05:01, 05:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:12:23

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并配置一个 Hadoop MapReduce 程序，实现 Reduce Join 操作，并在终端中创建 HDFS 输入目录。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IntelliJ IDEA 中的项目结构，当前选中的是 `JobMain.java` 文件。
- 代码内容为空，仅显示类声明 `public class JobMain { }`。
- 项目结构中可见 `mapreduce_reduce_join` 包下的 `JobMain`、`ReduceJoinMapper`、`ReduceJoinReducer` 等类。

画面 2：
- 展示了 `JobMain.java` 文件的后半部分代码。
- 代码注释说明“第八步：设置输出类”和“设置输出的路径”。
- 代码内容包括：
  ```java
  job.setNumReduceTasks(4);
  job.setOutputFormatClass(TextOutputFormat.class);
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/flowcount_out"));
  boolean b = job.waitForCompletion(true);
  return b ? 0 : 1;
  ```
- `main` 方法中包含启动 Job 的代码：
  ```java
  public static void main(String[] args) throws Exception {
      Configuration configuration = new Configuration();
      //启动 个任务
      int run = ToolRunner.run(configuration, new JobMain(), args);
      System.exit(run);
  }
  ```

画面 3：
- 展示了 `JobMain.java` 文件的前半部分代码。
- 代码注释说明“第一步：设置读取文件的 K1 和 V1”和“第二步：设置 Mapper 类”。
- 代码内容包括：
  ```java
  import org.apache.hadoop.extends ToolRunner implements Tool {
  @Override
  public int run(String[] strings) throws Exception {
      Job job = Job.getInstance(super.getConf(), "mapreduce_reduce_join");
      //打包放在集群运行时，需要做一个配置
      job.setJarByClass(JobMain.class);
      //第一步：设置读取文件的 K1 和 V1
      job.setInputFormatClass(TextInputFormat.class);
      TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/reduce_join"));
      //第二步：设置 Mapper 类
      job.setMapperClass(ReduceJoinMapper.class);
      //设置 Map 阶段输出类型：K2 和 V2 的类型
      job.setMapOutputKeyClass(Text.class);
      job.setMapOutputValueClass(FlowBean.class);
  ```
- 注释说明“第三、四、五、六步采用默认方式（分区、排序、缓存、分组）”。

画面 4：
- 展示了 `JobMain.java` 文件中设置 Reducer 的代码部分。
- 代码注释说明“第七步：设置定义的 Reducer 类”和“设置 Reduce 阶段的输出类型”。
- 代码内容包括：
  ```java
  //第七步：设置定义的 Reducer 类
  job.setReducerClass(ReduceJoinReducer.class);
  //设置 Reduce 阶段的输出类型
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(FlowBean.class);
  ```

画面 5：
- 展示了 `JobMain.java` 文件中设置 Reduce 任务数和输出格式的代码部分。
- 代码注释说明“第七步：设置定义的 Reducer 类”和“第八步：设置输出类”。
- 代码内容包括：
  ```java
  //第七步：设置定义的 Reducer 类
  job.setReducerClass(ReduceJoinReducer.class);
  //设置 Reduce 阶段的输出类型
  job.setOutputKeyClass(Text.class);
  job.setOutputValueClass(FlowBean.class);
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/reduce_join_out"));
  ```

画面 6：
- 展示了 `JobMain.java` 文件中设置输出格式和路径的代码部分。
- 代码内容包括：
  ```java
  //第八步：设置输出类
  job.setOutputFormatClass(TextOutputFormat.class);
  //设置输出的路径
  TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/reduce_join_out"));
  boolean b = job.waitForCompletion(true);
  ```

画面 7：
- 展示了终端窗口，执行 HDFS 命令。
- 命令为：
  ```bash
  [root@node01 ~]# hdfs dfs -mkdir /input/reduce_join
  ```
- 该命令用于在 HDFS 上创建输入目录，为后续 MapReduce 程序准备数据输入路径。
