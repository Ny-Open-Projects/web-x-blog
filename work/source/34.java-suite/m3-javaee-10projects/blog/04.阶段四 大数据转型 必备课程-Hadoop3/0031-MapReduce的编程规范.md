# MapReduce 编程规范：八步骨架与 Mapper、Reducer、Driver 的泛型约定

知道了 MapReduce 的构思和框架结构，真要动手写代码时还是会卡住：一个完整的作业到底由几段代码组成，数据从哪进来、中间谁处理、结果从哪出去，类怎么继承、泛型怎么填。编程规范回答的就是这些问题。它把一次计算固定成八个步骤，用户只实现其中两小段业务逻辑，其余全部交给框架的默认组件。

## 先给结论

- 一个 MapReduce 程序从读文件到写结果共八步：Map 阶段 2 步，Shuffle 阶段 4 步，Reduce 阶段 2 步。
- Map 阶段：InputFormat 读取原文件并切成键值对 K1 V1；自定义 Mapper 把 K1 V1 转成 K2 V2。
- Shuffle 阶段：对 K2 V2 做分区、排序、规约、分组，四步框架都有默认实现。
- Reduce 阶段：自定义 Reducer 把分组后的 K2 V2 汇总成 K3 V3；OutputFormat 把结果写到指定位置。
- 用户要写的代码只有三块：Mapper、Reducer、负责装配的 Driver，其余步骤用默认组件即可。

## 一、八步骨架：数据从原文件到结果文件

把总体上的 Map、Reduce 两阶段再细分，会多出一个 Shuffle 阶段，八步由此而来。Map 阶段占两步：InputFormat 把原文件读进来切成一个个键值对，这就是 K1 V1；接着进入第二步，自定义 map 逻辑，把 K1 V1 转成另一个键值对 K2 V2。Shuffle 阶段占四步，处理对象都是 K2 V2：分区、排序、规约、分组。Reduce 阶段占两步：Reducer 对 Map 产生的结果排序并汇总，转成新的 K3 V3；再由 OutputFormat 把结果输出到指定位置，比如写到文件里。

分区可以这样理解：数据量大了以后，常需要给中间结果做分类。比如统计单词时，想把长度小于 5 的单词存一个文件、5 到 8 之间的存一个、大于 8 的存另一个，这个分类动作就是分区。排序是把键值对按要求排成有序。规约是 Map 端提前把 Reduce 该干的一部分活干掉，降低 Reduce 阶段的压力。分组是 K 相同的键值对归入一个集合，分组之后 K2 还是单词，V2 变成了 `1,1,1` 这样的值序列。整个骨架画出来是这样：

```mermaid
flowchart LR
    A["原文件"] --> B["1. InputFormat<br/>读取并切成 K1 V1"]
    B --> C["2. Mapper<br/>K1 V1 转 K2 V2"]
    C --> D["3. 分区"]
    D --> E["4. 排序"]
    E --> F["5. 规约"]
    F --> G["6. 分组<br/>相同 K2 归入一个集合"]
    G --> H["7. Reducer<br/>汇总成 K3 V3"]
    H --> I["8. OutputFormat<br/>写出结果文件"]
```

关键路径：第 1 步和第 3 到第 6 步、第 8 步由框架自动完成，用户真正动笔的只有第 2 步的 Mapper 和第 7 步的 Reducer。

## 二、Mapper：四个泛型定死进出类型

自定义 Mapper 要继承框架的 `Mapper` 类并重写 `map` 方法。类声明上有四个泛型，前两个对应 K1 V1 的类型，后两个对应 K2 V2 的类型。课程真实工程里的 Mapper（包名统一改写为 `com.study.mapreduce`）：

```java
package com.study.mapreduce;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

// 四个泛型依次是 K1 V1 K2 V2 的类型：
// KEYIN   K1 行偏移量  LongWritable
// VALUEIN V1 一行文本  Text
// KEYOUT  K2 每个单词  Text
// VALUEOUT V2 固定值 1 LongWritable
public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        // key 是 K1 行偏移量，value 是 V1 一行文本
        String line = value.toString();
        String[] split = line.split(",");
        for (String word : split) {
            // 每个单词输出一次 <单词, 1>，即 K2 V2
            context.write(new Text(word), new LongWritable(1));
        }
    }
}
```

四个泛型不是随手填的：K1 由输入组件决定，`TextInputFormat` 按行读文件，给的是字节偏移量；V1 是一行文本；K2 V2 由业务决定，词频统计要输出单词和计数 1。泛型填错，`map` 方法的参数类型就跟着错，作业运行时对不上。

## 三、Reducer：泛型必须与 Mapper 的输出对齐

Reducer 同样继承框架类、重写方法，四个泛型前两个是 K2 V2，后两个是 K3 V3。前两个必须与 Mapper 的 KEYOUT、VALUEOUT 一致，数据才能接得上：

```java
package com.study.mapreduce;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

// 四个泛型依次是 K2 V2 K3 V3 的类型
public class WordCountReducer extends Reducer<Text, LongWritable, Text, LongWritable> {
    @Override
    protected void reduce(Text key, Iterable<LongWritable> values, Context context)
            throws IOException, InterruptedException {
        // key 是 K2 单词，values 是分组后该单词收到的所有 1
        long count = 0;
        for (LongWritable value : values) {
            count += value.get();
        }
        // 写出 K3 V3
        context.write(key, new LongWritable(count));
    }
}
```

## 四、Driver：把八步装配成一个 Job

Mapper 和 Reducer 只是两段逻辑，把八步串成任务的是 Driver，也就是主程序。框架提供了固定模板：继承 `Configured`、实现 `Tool` 接口，`main` 方法里用 `ToolRunner.run` 启动，`run` 方法里创建 Job 对象并按八步依次设置。真实工程 JobMain 的装配代码（做了精简）：

```java
package com.study.mapreduce;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] args) throws Exception {
        // 创建任务对象，第二个参数是任务名，可自定义
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");

        // 第一步：设置读取文件的类，它负责产生 K1 V1，并指定从哪里读
        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/wordcount"));

        // 第二步：设置 Mapper 类与 Map 阶段输出类型 K2 V2
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);

        // 第三到六步：分区、排序、规约、分组，采用框架默认实现

        // 第七步：设置 Reducer 类与 Reduce 阶段输出类型 K3 V3
        job.setReducerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        // 第八步：设置输出类与输出路径
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));

        boolean b = job.waitForCompletion(true);
        return b ? 0 : 1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}
```

两个容易混淆的方法在这里就能分清：`setMapOutputKeyClass` 设的是 K2 的类型，`setOutputKeyClass` 设的是 K3 的类型。K2 与 K3 经常同型但不必然，按各自泛型如实设置。真实工程还通过 `job.setCombinerClass` 挂了一个规约类，那是第八步之外的可选优化，属于高级篇的内容。

## 五、KV 类型为什么不能用 String 和 int

按 Java 习惯，K1 是数字该写 Long，V1 是一行文本该写 String。Hadoop 不接受这些原生类型，因为 KV 对象要在节点之间高频序列化传输，Java 自带的序列化机制代码臃肿、附带信息多，框架专门设计了一套实现 Writable 接口的类型做精简序列化。常用对应关系：`LongWritable` 对应 `long`，`IntWritable` 对应 `int`，`Text` 对应 `String`，Text 内部封装的其实是一个字节数组。所以四个泛型写成 `LongWritable, Text, Text, LongWritable`，map 方法里也要先 `value.toString()` 拿到字符串才能做切分。计数用 `LongWritable` 还是 `IntWritable` 都行，前提是 Mapper 与 Reducer 两边声明一致。

## 常见误区

- **泛型顺序背反着写。** Mapper 的四个泛型依次是 K1 V1 K2 V2，前两个输入、后两个输出；写成 `Mapper<Text, LongWritable, LongWritable, Text>` 等于输入一个单词、输出一行文本，方向完全弄反。
- **Map 输出类型与最终输出类型设错位置。** `setMapOutputKeyClass` 管 K2，`setOutputKeyClass` 管 K3，两者含义不同；漏设前者时框架按后者推断，类型对不上就在运行时报错。
- **认为八步都要自己实现。** 用户只写 Mapper、Reducer、Driver 三块，Shuffle 四步的默认实现已内置，需要定制分区规则等场景才去覆盖。
- **用 String、int 直接当 KV 泛型。** 它们没有实现 Hadoop 的序列化接口，编译期通不过，必须换用 Text、IntWritable、LongWritable 这套 Writable 类型。

## 面试可能被问到的问题

1. 面试官追问：「一个 MapReduce 程序分几个阶段、共几步？」
   答：分 Map、Shuffle、Reduce 三个阶段共八步。Map 两步：InputFormat 读取文件切成 K1 V1，自定义 Mapper 转成 K2 V2；Shuffle 四步：分区、排序、规约、分组；Reduce 两步：Reducer 汇总成 K3 V3，OutputFormat 输出。
2. 面试官追问：「Mapper 的四个泛型分别是什么？」
   答：以词频统计为例，依次是 K1 的 LongWritable（行偏移量）、V1 的 Text（一行文本）、K2 的 Text（单词）、V2 的 LongWritable（计数 1）。前两个由输入格式决定，后两个由业务决定。
3. 面试官追问：「为什么 KV 类型不用 String 而用 Text？」
   答：Hadoop 要在节点间高频序列化键值对，Java 原生序列化臃肿低效，框架自建了 Writable 序列化体系。Text 对应 String、内部封装字节数组，LongWritable 对应 long，IntWritable 对应 int。
4. 面试官追问：「规约 Combiner 的作用是什么？」
   答：它在 Map 端提前做一部分 Reduce 端的聚合，比如本地先合并同一个单词的多个 1 再传输，减少网络流量、降低 Reduce 压力。适合求和、计数这类满足结合律的操作。
5. 面试官追问：「setMapOutputKeyClass 和 setOutputKeyClass 有什么区别？」
   答：前者设置 Map 阶段输出 K2 的类型，后者设置 Reduce 阶段最终输出 K3 的类型。K2 与 K3 类型可能不同，必须按各自泛型如实设置，否则运行时类型校验失败。

## 配套资料

- 代码：`materials/code/04/day04-MapReduce高级/day04/代码/day04_mapreduce_combiner/src/main/java/`，课程真实词频统计工程，正文 Mapper、Reducer 与 JobMain 装配代码摘自该工程并做了精简，包名统一改写为 `com.study.mapreduce`。
- 本课为规范讲解课，day03 资料包未收录讲义与源码，八步骨架图按课堂讲解重绘。
