# 7-MapReduce案例-wordcount-Reduce阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\7-MapReduce案例-wordcount-Reduce阶段代码【海量资源尽在 ubkz.com】.mp4
- 时长 9分23秒（音频 564s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在写完map阶段的方法之后接下来咱们来写reduce阶段这里边有个word count reducer这个类呢要去继承一个类叫reducer这个reducer呢有四个范形前两个呢是K2和V2后两个呢是K3和V3来 我们来写一下来给大家加个注释这里边呢这有四个也是有四个一个是K1
[00:30] 这个范型呢是K2K2还有个K这个value1这个呢是V2还有呢是Kout那这个是K3它的类型还有个valueout它是V3的类型好那我们分别来看一下首先呢我们在这把范型加一下那首先呢K2和V2是什么类型呢我们来看一下
[01:05] 画的这个图好我们现在写的代码在这里那在这里的时候呢大家注意给我们这个reducereduce阶段呢传递的K2呢它是一个每个单词它是一个string类型它是一个string类型那在这里呢我们没有string我们在这里用的是什么类型呢我们用的是test的testOK这是我们的K2是test表示每个单词
[01:39] OK那在接下来呢我们来继续看那我们的VR是什么呢VR你看到这是一个集合这里呢我们要写集合中这个类型的范型OK那这个集合里边每一个你认为呢它都是一个long, right, able类型都是一个长等型OK那所以说呢咱们在这里呢继续写这个地方写long, right, ableOK把这个导个爆好所以说呢这个地方是
[02:13] LongWritable这个表示集合中范形的类型好接下来还有个K3和V3而我们的K3和V3什么类型呢我来继续看这个K3呢又是每个单词而V3呢是每个单词出现的次数那不用说也是LongWritable所以说K3 V3是testLongWritableOK这个我们把它复制一下
[02:46] 这个代表每个单词这个呢表示long writable表示每个单词出现的次数好这个写完之后呢接下来我们还需要重写reducer中的一个方法这个方法叫reduce我们来看一下这个方法呢有三个参数分别来解释一下首先呢这个k呢这个参数这个k
[03:29] 其实就是我们的K2这个就是K2这个K2是什么类型呢这个K2代表每个单词而这个values呢这个参数它是一个集合它是一个iterable集合集合那这个集合是什么呢这个集合其实就是我给大家画的图前面这个集合里边都是一样这么一个集合OK那这个context呢是一个上下文对象在刚才呢
[03:59] 给大家介绍过map radius的上下文对象那它呢可以将map radius的各个阶段呢之间相连好那么接下来我们来看这个参数介绍完之后呢首先我们说reduce方法是来干嘛呢reduce是不是将我们的K2和V2是不是转成K3和V3呢这个首先要大家明白reduce方法的作用
[04:35] 是将K2和V2转为K3和V3好那接下来我们再想我们的K2V2长什么样子我们的K3V3长什么样子来我们来描述一下先说我们的K2和V2其实这里的K2和V2呢实际上是应该说是我们新的K2V2为什么这样说呢大家来看
[05:08] 在这个Reduce觉得呢传给他的是不是新KLVOK那这个新的KLV长什么样子呢比如说Hello后面呢他跟的是一个集合1 1 1这么一个集合而Word呢他也是1 1而Hadoop呢他跟的是1 1 1好这么一个集合这是我们的新的KLV
[05:40] 那我们要得到一个什么结果呢我们要得到一个K3V3K3V3那这个结果长什么样呢应该是这样的我们把上面的直接复制过来应该是hello呢这个地方是2word呢是2hadoop呢是3好Hadoop是3那接下来问题来了如何将上面这个K2和V2转为K3和V3呢大家看
[06:20] 上面的V2是一个集合那我可以变你这个集合并且把这里的每个1是不是相加就得到V3了OK那我们来看好首先这是K2那V2呢你认为这个就是V2这个集合那我们来接下来来做这个事情那怎么做呢首先呢既然呢我们的这个集合都在这里那我可不可以变你这个集合所以第一步变你变你
[06:50] values集合好 便利集合之后呢我们要做第二件事将集合中的值相加是不是就可以了OK 那接下来我们看我们来便利这里边呢我们可以获取每一个1那拿到之后干嘛呢相加相加的话呢我可以再定个变量比如说定个变量我们定个lang类型的变量那这个变量叫count
[07:22] 比如说付个0我变了一个1我就相加那我就是count加等value这个value是long writable我还不能直接相加它有个方法叫get通过这个get呢我可以获取它的一个long类型的一个对象OK好把它相加那相加完之后是不是得到v3了那k3呢k3是不是和我们的k2是一样的那这个就是k2
[07:50] 所以说呢拿到这个和之后呢我需要去做一件事情把这个注释放在这位置将第三步将将什么呢将这个k3和v3写入上下文中也就是写给myproducer下一个阶段那这个时候呢我们来看我们用一个context.write第一个参数需要个test也就是这里的k3
[08:31] 也就是这个k那我可以直接写k而这里的value呢我们来看这里的value呢是一个lang-writable类型而我现在的这个count呢是一个lang类型我们可以这样做我们可以new一个lang-writable然后呢把我们的count放进去好这就是k3这就是v3来写入上下文中那写到上下文中写给谁呢我们来看你会发现这里的k3和v3呢向后
[09:02] 写给了一个类叫test output format那它呢就可以自动的把这个数据呢写到文件中好这个不用我们担心了好那这个reduce方法我们就写完了好写完之后呢我们可以进行下一步操作好关于reduce方法我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.Hadoop.mapreduce.Reducer;
public class WordCountReducer extends Reducer<Text, Text, Text, Text> {
}
```

画面4：
```java
package cn.itcast.mapreduce;
import org.apache.Hadoop.mapreduce.Reducer;
// KEYIN: K2 Text 每个单词
// VALUEIN:V2 Text 每个单词
public class WordCountReducer extends Reducer<Text, Text> {
}
```

画面5：
```java
package cn.itcast.mapreduce;
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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
import org.apache.Hadoop.io.LongWritable;
import org.apache.Hadoop.io.Text;
import org.apache.Hadoop.mapreduce.Reducer;
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

