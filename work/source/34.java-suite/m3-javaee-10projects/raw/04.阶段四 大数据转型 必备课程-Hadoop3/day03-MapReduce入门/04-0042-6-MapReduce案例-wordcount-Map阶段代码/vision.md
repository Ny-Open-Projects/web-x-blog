# 画面线理解：6-MapReduce案例-wordcount-Map阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\6-MapReduce案例-wordcount-Map阶段代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 02:21, 02:56, 03:35, 05:14, 06:52, 08:17, 09:00, 10:16, 11:05, 11:28, 12:58, 13:43, 14:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:46:34

1) 这一组画面整体在讲如何编写一个自定义的 Hadoop MapReduce WordCount Mapper 类，包括继承 Mapper 类、定义输入输出类型、重写 map 方法并实现单词计数逻辑。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中，为 WordCountMapper.java 文件选择继承类，弹出的类建议列表中包含 Mac、MacSpi、MailcapCommandMap 等类。
画面2: 代码中将 WordCountMapper 类继承自 Mapper<LongWritable, Text, Text, LongWritable>，并注释说明 Mapper 的泛型定义。
画面3: 代码中将 WordCountMapper 类继承自 Mapper<Long, String, String, Long>，并注释说明 Mapper 的泛型定义。
画面4: 查看 LongWritable 类的源码，其中包含私有静态 final 字段 ENCODER_FACTORY 和 DECODER_FACTORY，以及常量 EMPTY_BYTES、DEFAULT_MAX_LEN、LEAD_BYTE。
画面5: 代码中将 WordCountMapper 类继承自 Mapper<LongWritable, Text, Text, LongWritable>，并注释说明 Mapper 的泛型定义。
画面6: 展示 Hadoop MapReduce 的整体流程图，包括 Map 阶段、Shuffle 阶段和 Reduce 阶段，以及各阶段的输入输出数据示例。
画面7: 在 WordCountMapper.java 文件中，编写 map 方法的骨架，注释说明输入输出类型。
画面8: 在 WordCountMapper.java 文件中，编写 map 方法的骨架，注释说明输入输出类型。
画面9: 在 WordCountMapper.java 文件中，为 map 方法添加一个 finalize() 方法的自动补全建议。
画面10: 在 WordCountMapper.java 文件中，编写 map 方法的实现，包括将输入的 Text 转换为 String 数组并遍历。
画面11: 在 WordCountMapper.java 文件中，为 map 方法添加一个 context 对象的自动补全建议。
画面12: 在 WordCountMapper.java 文件中，为 map 方法添加一个 new Text() 的自动补全建议。
画面13: 在 WordCountMapper.java 文件中，为 map 方法添加一个 context.write() 方法的自动补全建议。
画面14: 在 WordCountMapper.java 文件中，编写 map 方法的完整实现，包括创建 Text 对象并调用 context.write() 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package en.itcast.mapreduce;

import org.apache.hadoop.mapreduce.Mapper;

// Mapper的泛型：
// KEYIN: k1的类型
// VALUEIN: v1的类型
// KEYOUT: k2的类型
// VALUEOUT: v2的类型
public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
```

画面5:
```java
package en.itcast.mapreduce;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// Mapper的泛型：
// KEYIN: k1的类型
// VALUEIN: v1的类型
// KEYOUT: k2的类型
// VALUEOUT: v2的类型
public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
```

画面7:
```java
// map 112.431111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
