# 画面线理解：7-MapReduce案例-wordcount-Reduce阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\7-MapReduce案例-wordcount-Reduce阶段代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:06, 01:29, 02:01, 02:38, 03:17, 04:13, 05:52, 06:06, 06:19, 07:27, 08:26, 08:52, 09:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:49:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在Hadoop中实现一个WordCount程序，包括编写Map和Reduce阶段的Java代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示WordCountMapper.java文件，其中map方法将输入行按空格分割成单词，并将每个单词设置为新值。
画面2：展示Hadoop MapReduce的流程图，包括Map阶段、Shuffle阶段和Reduce阶段，以及各阶段的数据转换。
画面3：在WordCountReducer.java中，选择继承Reducer类。
画面4：在WordCountReducer.java中，指定KEYIN和VALUEIN为Text类型。
画面5：在WordCountReducer.java中，指定KEYOUT和VALUEOUT为LongWritable类型。
画面6：在WordCountReducer.java中，编写reduce方法的骨架，调用super.reduce。
画面7：在WordCountReducer.java中，显示reduce方法的参数和注释。
画面8：在WordCountReducer.java中，显示K2和V2的示例数据。
画面9：在WordCountReducer.java中，显示K3和V3的示例数据。
画面10：在WordCountReducer.java中，显示K3和V3的示例数据。
画面11：在WordCountReducer.java中，显示context对象的可用方法。
画面12：在WordCountReducer.java中，显示context对象的可用方法。
画面13：在WordCountReducer.java中，编写reduce方法，初始化count，遍历values集合，累加值，并写入输出。
画面14：在WordCountReducer.java中，编写reduce方法，初始化count，遍历values集合，累加值，并写入输出。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    Text text = new Text();
    //1:对每一行的数据进行字符串拆分
    String line = value.toString();
    String[] split = line.split(" ");
    //2:遍历数组，获取每一个单词
    for (String word : split) { //word 1
        text.set(word);
    }
}
```

画面2：
无代码，为流程图。

画面3：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.mapreduce.Reducer;
public class WordCountReducer extends Reducer<Text, Text, Text, Text> {
}
```

画面4：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 Text 每个单词
public class WordCountReducer extends Reducer<Text, Text> {
}
```

画面5：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
}
```

画面6：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    super.reduce(key, values, context);
}
```

画面7：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        super.reduce(key, values, context);
    }
}
```

画面8：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        super.reduce(key, values, context);
    }
}
```

画面9：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        super.reduce(key, values, context);
    }
}
```

画面10：
```java
package cn.itcast.mapreduce;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 LongWritable 集合中泛型的类型
// KEYOUT:K3 Text 每个单词
// VALUEOUT:V3 LongWritable 每个单词出现的次数
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
        super.reduce(key, values, context);
    }
}
```

画面11：
```java
@Override
protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
    long count = 0;
    //1:遍历values集合
    for (LongWritable value : values) {
        //2:将集合中的值相加
        count += value.get();
    }
    //3:将K3和V3写入上下文中
    context.write(key, new LongWritable(count));
}
```

画面12：
```java
@Override
protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
    long count = 0;
    //1:遍历values集合
    for (LongWritable value : values) {
        //2:将集合中的值相加
        count += value.get();
    }
    //3:将K3和V3写入上下文中
    context.write(key, new LongWritable(count));
}
```

画面13：
```java
@Override
protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
    long count = 0;
    //1:遍历values集合
    for (LongWritable value : values) {
        //2:将集合中的值相加
        count += value.get();
    }
    //3:将K3和V3写入上下文中
    context.write(key, new LongWritable(count));
}
```

画面14：
```java
@Override
protected void reduce(Text key, Iterable<LongWritable> values, Context context) throws IOException, InterruptedException {
    long count = 0;
    //1:遍历values集合
    for (LongWritable value : values) {
        //2:将集合中的值相加
        count += value.get();
    }
    //3:将K3和V3写入上下文中
    context.write(key, new LongWritable(count));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
流程图结构：
- “a.txt”（源文件） → “TextInputFormat” → “K1 V1”（Map阶段输入）
- “K1 V1” → “Map阶段” → “K2 V2”（Map阶段输出）
- “K2 V2” → “Shuffle阶段” → “新 K2 V2”（Shuffle阶段输出）
- “新 K2 V2” → “Reduce阶段” → “K3
