# 画面线理解：7-MapReduce-流量统计求和-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\7-MapReduce-流量统计求和-测试运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:10, 00:16, 00:31, 00:39, 01:19, 01:37, 01:51, 02:13, 02:28, 02:39, 02:50, 02:56, 03:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:31:25

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Hadoop 集群上运行一个 MapReduce 流量统计任务，包括数据准备、代码编写、任务提交和结果查看。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示一个文本编辑器（Notepad++）中的数据文件，内容为多行以空格分隔的数字和网站信息，如“1363157995066 13726230503 00-FT-07-A4-72-B8:CMCC 120.196.100.82 102.c.allimg.com 游戏娱乐 24 27”。
画面 2: 与画面 1 相同，未变化。
画面 3: 显示 Windows 桌面，右键点击“此电脑”弹出菜单，鼠标悬停在“属性”选项上。
画面 4: 在 SecureCRT 终端中，执行 `rz -E` 命令等待接收文件，随后列出目录内容，包含 `data_flow.dat`、`hadoop-3.1.1.tar.gz`、`jdk-8u141-linux-x64.tar.gz`、`wordcount.txt`、`zookeeper-3.4.9.tar.gz` 等文件。
画面 5: 与画面 4 相同，未变化。
画面 6: 在 IntelliJ IDEA 中，显示 MapReduce 任务的 Java 代码，`JobMain` 类中设置输入路径为 `hdfs://node01:8020/input/`，并设置 Mapper 和 OutputKey 类。
画面 7: 在 IntelliJ IDEA 中，右键点击 `day04_mapreduce_combiner.jar`，弹出菜单，鼠标悬停在“Run”选项上。
画面 8: 在 SecureCRT 终端中，执行 `rm day04_mapreduce_combiner-1.0-SNAPSHOT.jar` 命令，然后再次执行 `rz -E` 命令，弹出文件传输对话框。
画面 9: 在 IntelliJ IDEA 中，显示 `day04_mapreduce_combiner-1.0-SNAPSHOT.jar` 文件被选中，下方显示“INFO] Final Memory: 29M/22M”。
画面 10: 在 SecureCRT 终端中，执行 `hadoop jar day04_mapreduce_combiner-1.0-SNAPSHOT.jar cn.itcast.mapreduce.flowcount.JobMain` 命令，输出日志信息，显示任务提交成功。
画面 11: 在 SecureCRT 终端中，显示 MapReduce 任务执行后的统计信息，包括 Spilled Records、Shuffled Maps、GC time elapsed、CPU time spent、Memory 使用情况等。
画面 12: 在浏览器中打开 Hadoop 文件浏览器，点击文件 `part-r-00000`，弹出“File information - part-r-00000”对话框，显示 Block ID、Block Pool ID、Generation Stamp、Size 和 Availability 信息。
画面 13: 与画面 12 相同，鼠标悬停在“Head the file (first 32K)”按钮上。
画面 14: 在 EditPlus 文本编辑器中，显示文件 `part-r-00000` 的内容，为多行以空格分隔的数字，如“1 3480253104 3 3 180 180”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_flowcount");
        // 一个任务对象
        // 1. 设置输入路径
        FileInputFormat.setInputPaths(job, new Path("hdfs://node01:8020/input/"));
        // 2. 设置Mapper类
        job.setMapperClass(JobMain.class);
        // 3. 设置输入格式
        job.setInputFormatClass(TextInputFormat.class);
        // 4. 设置输出路径
        FileOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/output/"));
        // 5. 设置Reducer类
        job.setReducerClass(FlowCountReducer.class);
        // 6. 设置输出key类
        job.setOutputKeyClass(Text.class);
        // 7. 设置输出value类
        job.setOutputValueClass(LongWritable.class);
        // 8. 设置分组
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 9. 设置分区
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 10. 设置排序
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 11. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 12. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 13. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 14. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 15. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 16. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 17. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 18. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 19. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 20. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 21. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 22. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 23. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 24. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 25. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 26. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 27. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 28. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 29. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 30. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 31. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 32. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 33. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 34. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 35. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 36. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 37. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 38. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 39. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 40. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 41. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 42. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 43. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 44. 设置分组比较器
        job.setGroupingComparatorClass(FlowCountGroupingComparator.class);
        // 45. 设置分区比较器
        job.setPartitionerClass(FlowCountPartitioner.class);
        // 46. 设置排序比较器
        job.setSortComparatorClass(FlowCountSortComparator.class);
        // 47. 设置分组比较器
        job.setGroupingComparatorClass(FlowCount
