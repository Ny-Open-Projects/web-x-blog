# 画面线理解：4.9 开发单词统计程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.9 开发单词统计程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:20, 01:04, 02:09, 02:54, 04:35, 04:54, 07:31, 08:02, 08:37, 09:43, 10:34, 11:08, 11:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:15:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写一个基于 Flink 的 Java 流式数据处理程序，实现对 Socket 输入数据的单词计数功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 StreamingJob.java 文件的开头部分，包含注释和 main 方法的骨架。光标位于 main 方法的开始处。
画面 2: 光标移动到 main 方法内部，开始编写代码。注释显示“监听socket端口”和“流处理”。
画面 3: 代码中添加了 Flink 环境的创建和数据源的定义，光标位于 env.socketTextStream(...) 行。
画面 4: 定义了 WordWithCount 类，用于存储单词和计数。光标位于类定义处。
画面 5: 为 WordWithCount 类添加了构造函数和成员变量的定义。
画面 6: 为 DataStream<String> text 变量添加了 flatMap 操作，光标位于 .flatMap(...) 行。
画面 7: 为 flatMap 操作选择 FlatMapFunction<String, WordWithCount> 类型。
画面 8: 为 flatMap 操作选择 .timeWindow(...) 方法。
画面 9: 为 .timeWindow(...) 方法选择 .reduce(...) 方法。
画面 10: 为 .reduce(...) 方法选择 reduce 函数。
画面 11: 为 reduce 函数选择 WordWithCount 类型。
画面 12: 为 reduce 函数选择 .print() 方法。
画面 13: 代码编写完成，显示了完整的 StreamingJob.java 文件内容。
画面 14: 切换到终端窗口，显示了 Flink 任务的执行日志和结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
// For a tutorial how to write a Flink streaming application, check the
// tutorials and examples on the "a href="http://link.spark.org/docs/stable/"Flink Website/a>.
// To package your application into a .jar file for execution, run:
// mvn clean package on the command line.
// If you change the name of the main class (with the public static void main(String[] args)
// method, change the respective entry in the POM.xml file (simply search for "mainClass").
public class StreamingJob {
```

画面 2:
```java
// 监听socket端口
// 流处理
```

画面 3:
```java
// 3. 定义数据源
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 4:
```java
public static class WordWithCount {
    public String word;
    public long count;
    public WordWithCount() {}
    public WordWithCount(String word, long count) {
        this.word = word;
        this.count = count;
    }
}
```

画面 5:
```java
public WordWithCount reduce(WordWithCount wordWithCount1, WordWithCount wordWithCount2) throws Exception {
    return new WordWithCount(wordWithCount1.word, wordWithCount1.count + wordWithCount2.count);
}
```

画面 6:
```java
final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
// 3. 定义数据源
DataStream<String> text = env.socketTextStream(hostname: "172.17.0.143", port: 9000, delimiters: "\n");
```

画面 7:
```java
text.flatMap(new FlatMapFunction<String, WordWithCount>() {
    @Override
    public void flatMap(String value, Collector<WordWithCount> out) throws Exception {
        for (String word : value.split("\\s+")) {
            out.collect(new WordWithCount(word, 1));
        }
    }
});
```

画面 8:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 9:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 10:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 11:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 12:
```java
.text.print();
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 13:
```java
// 3. 定义数据源
// 4. Flink
env.execute(jobName: "Flink Streaming Java API Skeleton");
```

画面 14:
```bash
[root@node2 ~]# nc -l 9000
abc def
abc def
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
