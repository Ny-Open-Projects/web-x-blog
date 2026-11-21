# 12.编写Spark应用（wordcount应用）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\12.编写Spark应用（wordcount应用）_【海量资源尽在 666java.com】.mp4
- 时长 14分14秒（音频 854s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢 我们就来编写我们的Spark应用啊那么前面呢 我们是使用了这个Spark为我们提供的一些这个example去做了一些体验那么下面我们就动手来做一个应用的编写那么首先需要说明的一点呢 是编写Spark应用那么官方所推荐使用的语言呢 是Scala语言但是呢 我们本课程呢 又不会涉及到Scala语言的
[00:29] 语法的讲解所以呢我们将使用这个加尔语言的做应用的编写那么如果如果这个观看视频的同学呢你对这个Segara语言如果比较熟悉的话那么也可以使用这个Segara语言去做一个编写OK好那么接下来呢我们就来创建我们的工程那么创建一个工程点击Create New一个Project
[00:57] 那么下面呢我们点击下一步然后呢group id呢就叫cn.itcast.Spark然后呢artifact id呢那就叫my.Spark然后呢-test好那么点击下一步然后呢我们去输入它然后呢点击finish完成那么这个工程呢就创建好了那么创建好之后呢我们就需要去导入一些相关的一些依赖
[01:27] 好 那么我们这个工程就创建好了那么我们在这个位置去启用一个自动的导入那么接下来我们就需要在我们的POM文件中来导入我们所需要的依赖那么我们把这个就拷贝过来包括下面这个build好 那我们往这一贴那么其实可以看到在这个位置我们导入了是我们的Spark的
[01:54] 这个依赖那么使用的这个版本呢是2.4.3啊这样的一个版本那么下面这个呢是我们的java编译的一个插件那么指定的我们JDK的版本呢是1.8啊这样一个版本好那么接下来那么在这个位置呢我们就需要来编写我们的这个代码了那么主要呢也是来编写这个word count啊这样的一个程序那么首先呢我们先来去看一个我们的一个文件啊
[02:23] 那么在我们的这个f凡code下面有一个word这样的一个文件那么我们用这个edit plus把它打开一下来看一下那么这个文件大概是这样的一个文件就是跟我们刚刚所测试的文件是一样的这样的一个文件那么接下来我们就通过java代码来编写一个SPA的应用程序来统计一下这个文件中的一些单词的一些技术
[02:51] 然后在这个位置我们创建一个包那么创建一个叫做cn.ititcast.Spark这样的一个包然后在这个里面这个包名字写错了我们重命名一下然后ark好然后我们就可以来编写具体的代码了
[03:19] 那么在这个下面我们写一个类的名字就叫什么WordCountApp好那么写这样的一个类然后在下面写一个我们的一个MEM方法那么首先在这个位置我们需要去定义我们的上下文对象那么我们在这需要使用的是一个Java SparkContactor这样的一个对象那么就叫JSC这样的一个对象
[03:48] 去new一个java Spark contact的对象它是非常关键的因为它是什么呢它是我们程序的一个入口可以这样去做一个理解然后在上面我们需要给它定义一个我们的一个配置因为在这个中需要传入一个配置那我们就定一个Spark Spark configure这样的一个对象那么定义一个它去new一个Spark configure
[04:18] 对象然后呢我们把它呢传递过去那么在这个sparkconfig中呢需要去定义哪些参数呢我们一起来看一下我们需要给它set一个app name那么这个就是我们的一个应用的名称那我们就叫word count app然后呢我们再来去set一个什么呢master那么master呢在这呢我们本地呢我们就采用本地模式叫做什么呢local然后呢来一个c
[04:48] 那么这个是什么意思啊我们就设置是什么的本地模式啊并且呢呃并且这个使用呃使用和呃并且使用和什么呢和我们的这个cpu的内核内核数相同的内核数相同的这个现成数啊进行啊执行这个大家能不能够理解啊什么意思呢
[05:17] 就是说如果我在这个位置设置为2的话就代表着当前的我这个应用呢用两个线程去做一个执行那么如果我用C呢就代表着说它会读取到我当前这个机器的这个CPU的内核数去做一个执行这样的话呢就可以让每一核CPU去执行一个线程得到CPU的一个这个效率的一个最大化这个大家理解了吧然后呢上面这个呢我们加一个注释就叫什么呢是我们的一个SPARK
[05:46] 的一个的什么呢的一个配置啊这样的一个信息呃那么有了它之后呢那么在最后要注意我们需要关闭一下啊需要关闭一下然后呢释放啊释放资源那么通过这个jsc.stop去做一个stop就ok了呃然后呢在下面这个位置就可以去编写我们的具体的这个业务逻辑了那么我们现在要实现的呢是一个
[06:15] 单词的一个技术那我们就需要先去干嘛呢读取读取读取我们的一些这个文件那么怎么读呢就通过jsc.textfile去做一个读取那么这个文件呢我们就在F盘对吧F盘下面的有一个code下面的有一个叫做这个word.txt这样的一个文件那么它读到之后呢就会
[06:44] 返回一个什么呢我们的一个叫做fail吧rdd啊这样的一个对象那么这个文件读到之后呢我们就需要干嘛呢是不是给它压扁然后呢按照一个空格是不是做一个分割啊那么就是需要做什么呢压扁压扁操作啊并且按照空按照按照空格啊分割然后呢我们来操作一下通过failrdd点什么呢
[07:16] 有个叫做flatMap做这样的一个操作我们需要去给它new一个这样的一个操作那么我们在这个位置把这个object改成string因为我们操作都是这么串那么我们可以看到这个实现类它需要响应的返回的是一个迭代器所以在这个位置我们需要这么来玩一下
[07:44] 在这个位置呢我们拿到这个S拿到这个S它其实就是我们拿到的我们的数据啊我们需要对这个S呢做一个split是不是按照空格是不是做一个分割啊然后呢我们去拿到一个我们的返回值比如说叫SS那我们怎么得到一个那么得到这个SS呢它其实就是我们的一个宿主啊那么宿主我们怎么去得到我们的一个迭代器呢这个
[08:12] 我们重来一下刚刚选错了应该选它然后这个是SS好那么这个就是我们的一个迭代器那么怎么样去得到这个迭代器我们需要通过一个arrivance然后按list把这个速度给它然后去得到一个迭代器这样的一个操作那么其实这个操作完成之后我们就会
[08:42] 得到我们的一个这个flatmaprd那么它其实拿到的就是已经完成了一个空格的分割那就是一个一个的词那么接下来我们要做的操作呢其实就是我们需要对词呢做一个技术对吧那么就是需要去对这个单词做这个技术的一个技术的这样的一个处理那么怎么样处理呢我们通过这个flatmap.app
[09:11] 然后它有一个map to pair这样的一个操作就是要去形成一个kv的这样的一个这样的一个结构的一个数据了那么我们去new一个它的一个这个pair的一个这个function那么去得到它ok好那么最后呢我们其实可以看到return的是一个这个chop这样的一个对象那么怎么样去拿到它呢我们来看一下
[09:40] 那么我们这个返回的应该返回的是我们的一个数字就是integ对象就可以了那么不用去去写这个object了那么因为我们每一个单词呢先把它标记为1对吧那么我们这块去new一个这个chip然后呢第一个这个参数就是s就是我们这个单词第二个参数的值呢就是为1那么这个时候呢其实我们只是说对每一个单词做了一个
[10:09] 数字1的一个标记对不对那我们就写一个这个这个rdd吧对吧又得到一个rdd然后呢我们再去对什么呢对这个相同的这个单词啊做一个这个呃相加呃相加的一个操作那么这个来看一下怎么做呢map to pairrdd点
[10:37] 我们前面也去敲过这个命令啊怎么呢叫Reduce By Key对吧通过一个这个操作就是按照相同的相同的一个相同那个key我们去做一个计数那么这两个计数呢就是它的这个值其实就是我们上面所得到的这个数字啊那我们只要去V1加V2啊就可以了这个就是它的一个结果了
[11:06] 那么它的一个结果拿到了之后呢那就是一个reduce by k的一个rdd了rdd那么有了这个之后呢最后呢我们就需要什么呢去做一个这个去真正去做一个执行啊计算了啊计算那么这个怎么玩呢reduce by krdd.connect那么它呢就会得到最终的一个集合了
[11:35] 那么最终的一个这个集合然后呢我们去把它啊便利出来啊就可以了呃那么我们来啊便利一下那么怎么样便利呢呃去迭代一下它呃然后呢我们拿到我们去打印吧这个这个某一个单词啊这个出现我们先拿到这个单词那就是就是它了我们把它简化一下吧就叫obj吧
[12:02] 好那么我们拿到它的这个单词点什么呢这个是它的这个就是我们前面是单词啊后面是它的数量呢就是这个1然后呢去加上什么呢这个单词出现的次数次数为多少呢再去加一个这个obj点点什么呢2啊次数把它打印出来好那么我们来我们先来看一下我们刚刚的所写的这个
[12:31] 代码吧那么首先呢是不是去读取这个文件对吧那么读取到之后呢去按照空格去做一个分割得到我们的单词然后呢为每一个单词去设置一个数量为1做一个这个计数的一个标记然后呢我们对相同的单词呢做一个这个count的一个相加就是V1加这个V2然后呢最后就可以去计算得到这个结果了那我们来执行一下看一下这个效果
[12:58] 那么OK这个结果呢就已经出来了那么可以看到呢是这样的一个这个结果对吧这样的结果那么hello呢出现了四次mvc一次其他呢也都是一次啊这样的一个结果结果呢是符合我们预期的对不对但是呢大家可以看一下这个用java编写这个代码我们虽然能够看懂啊也能够把它写出来但是呢的确有点繁琐啊相比较之前啊我们看到了这个
[13:27] 这样的一个代码实在是不是复杂很多呢那么其实呢我们也可以去对我们刚刚所写这个代码的做一些这个简化那么我们先写到这来吧就是我们的这个实现我们把这个给大家来记录一下就是实现那么这个是什么呢就是为简化或者说为优化的一个代码那么下面这个呢其实我们就是
[13:55] 优化之后的一个优化之后的一个代码那么我们主要是通过什么呢通过这个java jdk所提供的一个Lamb的表达式去做一个这样的一个优化ok好那么关于我们这个word count的一个应用的一个编写那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建一个 Spark Java 应用，并编写一个 WordCount 程序。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档“Spark快速入门1.md”，内容为“5.1、创建工程”，并展示 IntelliJ IDEA 的“New Project”窗口，用于创建新项目。
画面 2: 显示 IntelliJ IDEA 中的 `pom.xml` 文件，内容为 Maven 项目配置。
画面 3: 显示 EditPlus 编辑器界面，无具体内容。
画面 4: 显示 IntelliJ IDEA 中的 `pom.xml` 文件，光标在 `<version>2.4.1</version>` 行，弹出“Create New Class”对话框。
画面 5: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，代码开始编写 Spark 应用的主函数。
画面 6: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写读取文件的代码，`JavaRDD<String>` 类型。
画面 7: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `flatMap` 函数，弹出方法提示。
画面 8: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `flatMap` 函数的实现。
画面 9: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `mapToPair` 函数的实现。
画面 10: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现。
画面 11: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现，弹出方法提示。
画面 12: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，正在编写 `reduceByKey` 函数的实现。
画面 13: 显示 Typora 文档“Spark快速入门1.md”，内容为“5.2、编写WordCount程序”，并展示 `WordCountApp.java` 文件的代码结构。
画面 14: 显示 IntelliJ IDEA 中的 `WordCountApp.java` 文件，代码已编写完成，底部显示“Job 0 finished: collect at WordCountApp.java:50, took 0.956583 s”，表示程序执行成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.Spark</groupId>
    <artifactId>my-Spark-test</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面 4:
```xml
<version>2.4.1</version>
<dependency>
</dependency>
<build>
    <plugins>
        <!-- java编译插件 -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

画面 5:
```java
package cn.itcast.Spark;
import org.apache.Spark.SparkConf;
import org.apache.Spark.api.java.JavaSparkContext;
class WordCountApp {
    public static void main(String[] args) {
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp")
                .setMaster("local[*]");
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    }
}
```

画面 6:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
```

画面 7:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 8:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 9:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 10:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 11:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 12:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面 13:
```java
package cn.itcast.Spark;
import org.apache.Spark.SparkConf;
import org.apache.Spark.api.java.JavaRDD;
import org.apache.Spark.api.java.JavaSparkContext;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;
public class WordCountApp {
    public static void main(String[] args) {
        //设置Spark的配置文件
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp")
                .setMaster("local[*]");
        //创建Spark上下文对象，它是程序的入口，所有的操作都通过它来执行
        JavaSparkContext jsc = new JavaSparkContext(sparkConf);
        //读取文件
        JavaRDD<String> linesJavaRDD = jsc.textFile("F://code//word.txt");
        //对文件中每一行进行按空格切分，并且按照单词进行汇总
        List<Tuple2<String, Integer>> list = linesJavaRDD.flatMap(s -> {
            String[] words = s.split(" ");
            return Arrays.asList(words).iterator();
        }).map(s -> new Tuple2<>(s, 1)).reduceByKey((v1, v2) -> v1 + v2).collect();
        for (Tuple2<String, Integer> obj : list) {
            System.out.println(obj);
        }
    }
}
```

画面 14:
```java
JavaRDD<String> fileRdd = jsc.textFile("F://code//word.txt");
fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“5.1、创建工程”。
画面 13: PPT 标题为“5.2、编写WordCount程序”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

