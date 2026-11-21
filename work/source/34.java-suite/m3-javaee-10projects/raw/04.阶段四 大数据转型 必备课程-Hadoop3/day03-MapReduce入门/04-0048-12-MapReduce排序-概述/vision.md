# 画面线理解：12-MapReduce排序-概述

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\12-MapReduce排序-概述【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:51, 01:56, 02:08, 02:19, 02:48, 02:51, 02:55, 03:01, 03:16, 03:24, 03:38, 03:57, 04:25, 04:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:02:59

1) 这一组画面整体在讲 MapReduce 中的序列化与排序机制，重点介绍 Writable 和 WritableComparable 接口的使用。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 IDE 中的项目结构和 WritableComparable 接口的源码，光标在接口定义处。
画面 2: 在 IDE 中搜索类名，弹出搜索结果，高亮显示 WordCountReducer。
画面 3: 在 IDE 中高亮显示 Writable 接口的 write 和 readFields 方法。
画面 4: IDE 窗口下方出现两个 Typora 文档窗口，显示课程笔记。
画面 5: Typora 中显示 PPT 内容，标题为“6. MapReduce序列化和排序”，介绍序列化、反序列化、Writable 和 WritableComparable。
画面 6: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 7: IDE 中光标在 WordCountReducer 类名上，下方显示“void readFields(DataInput var1) throws IOException;”。
画面 8: IDE 中搜索“Writable”，弹出 Maven 依赖列表，高亮显示 WritableComparable。
画面 9: IDE 中显示 JobMain.java 代码，设置 Reduce 任务数、输出格式和路径。
画面 10: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 11: Typora 中 PPT 页面，展示排序要求。
画面 12: Typora 中 PPT 页面，展示排序要求和解决方案。
画面 13: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 14: Typora 中 PPT 页面，展示数据格式和排序要求。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 9 代码：
```java
//设置Reduce的个数
job.setNumReduceTasks(2);
//第八步:设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
//设置输出的路径
TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));
boolean b = job.waitForCompletion(true);
return b ? 0 : 1;

public static void main(String[] args) throws Exception {
    Configuration configuration = new Configuration();
    //启动一个任务
    int run = ToolRunner.run(configuration, new JobMain(), args);
    System.exit(run);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 5 PPT 标题：“6. MapReduce序列化和排序”
PPT 内容：
- 序列化(Serialization)是将结构化对象转化为字节流
- 反序列化(Deserialization)是序列化的逆过程
- Java 的序列化(Serializable)是一个重量级序列化框架
- Writable 是 Hadoop 的序列化格式，Hadoop 定义了这样一个 Writable 接口，一个类要支持可序列化只需实现这个接口即可
- 另外 Writable 有一个子接口是 WritableComparable，WritableComparable 是即可实现序列化，也可以对key进行比较，我们这里可以通过自定义 Key 实现 WritableComparable 来实现我们的排序功能

画面 6 PPT 数据格式：
```
a 1
b 3
a 7
b 10
```

画面 11 PPT 要求：
- 第一列按字典顺序进行排列
- 第一列相同的时候，第二列按升序进行排列

画面 12 PPT 解决思路：
- 将 Map 输出的 <key,value> 中的 key 和 value 组合成一个新的 key (newKey)，value 不变
- 里边就变成 <(key,value),value>，在针对 newKey 排序的时候，如果 key 相同，就对 value 进行排序

5) 无
