# 15.弹性分布式数据集RDD之概述

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\15.弹性分布式数据集RDD之概述_【海量资源尽在 666java.com】.mp4
- 时长 5分34秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来看一下这个弹性分布式的一个数据集叫做RDD那么这个RDD呢其实在前面呢我们在编码的过程中啊已经设计到了那我们来看一下之前我们写的这个代码那么可以看到呢在我们之前所写的这个word count的这个程序中啊那么当我们去读取我们的这个文件的时候呢
[00:26] 最后所返回的一个对象是不是就是这个加尔RDD是不是也是一个RDD然后呢我们去把我们这个文件中的内容呢去做一个压扁的一个操作的时候那么它返回的是不是也是一个RDD叫加尔RDD那么我们去对单词就计数的时候返回的是不是也是RDD对吧然后呢我们做这个单词相同的做相加的时候呢
[00:56] 它返回的也是RDD那么这个RDD到底是一个什么东西呢那么接下来我们将详细的去学习这一块的内容因为RDD呢是Spark的一个重点内容那么首先呢第一个我们来看一下RDD的一个概述那么第一个问题呢就是什么是RDDRDD它的全称呢叫做Released Distributed Dataset它其实叫做什么呢
[01:25] 叫做弹性分布式数据集它是SPAC中最基本的其实也是最重要的这样的一个数据的抽象那么它所代表的是一个不可变的可分区的里面的元素可以进行计算的这样的一个集合那么它所具备的特点有什么呢自动的容错位置的感知性的一个调度
[01:55] 和可伸缩性那么RDD它允许用户在执行多个查询的时候显示的将数据缓存在内存中那么后续的查询能够重用这些数据极大的提升了查询的速度那么这个其实就是对RDD是一个数据集这样的一个定义那么它主要是这三个特性那我们来看一下
[02:21] 那么首先它肯定是一个什么呢数据集对吧用于去存放数据那么其次呢它呢是做分布式存储的那么可以去做一些分布式的一些计算那么它的数据呢可以存储在内存中那么也可以去存储在什么磁盘中这个就是它的一个什么弹性的啊这样的一个这样的一个特性那么第二个问题呢就是那么为什么会产生这个RDD呢我们一起来看一下
[02:50] 那么传统的这个MapReduce呢它所具备有什么呢自动的容错呢平衡负载以及这个可扩展性的一些优点但是它的最大的一个问题呢就是它所采用的是一个非循环式的一个数据流模型那么什么意思呢就是在它所迭代计算中呢需要做一个大量的一个磁盘IO的一个操作
[03:16] 就要做磁盘L的操作那么显然呢这样去做它的一个这个效率是不是就会比较低啊那么RDD呢其实就是在解决这样的一个问题解决这样的一个问题所抽象出来的这样的一种解决方案那么RDD呢其实是SPARK所提供一个最重要的一个抽象概念这个前面我们也提到了它呢是一种具备有浓厝机制的一个特殊的一个集合那么可以分布在集群上的一些这个节点上面
[03:45] 那么以函数式的编程来操作集合那么进行各种的一些这种操作那么其实可以看到在前面呢我们所编写的这个代码中呢是不是可以看到那么这个rdd啊比如说我们去读取到这个文件那么它所返回这个rdd是不是我们就可以做一系列的其他操作那么比如说我们去flatmap去做一个压扁的一个处理那么我们再去做一个奇数的处理啊再去做其他的处理啊等等
[04:14] 那么我们可以做一系列的这样的一些这种处理的操作那么可以把这个RDD的数据的做缓存那么方便多次的做一个调用然后呢重用啊那么去避免啊重复的一个计算这个呢是它的一个特点其实简单来说呢就是我们所面临的或者说面对的呢是一个分布式所存储的这样的一个数据那我们需要去把这么一堆这个数据
[04:43] 对吧我们看作是一个集合去做一个处理而这个集合的一个抽象那么就叫什么呢就叫RDD那么所以说呢以后呢在我们去编写我们的SPARK的时候呢那么我们所操作的大部分的都是在操作谁呢这个RDD所提供的一些这种API去做一些操作那么无论是我们做一些这种什么一些这个技术啊
[05:09] 还是我们的一些这个压扁呢等等这种操作那么或者是说我们去通过它的一些API去把我们的一些这个输出去写入到文件啊等等这样的操作呢都会通过这个RDD啊所提供的一些API呢来做一个完成那么OK这个呢就是关于RDD的一个概述好那么关于这个RDD的概述那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Java API 编写一个 Spark WordCount 程序，并穿插讲解 RDD 的基本概念。

2) 按时间顺序列出每张画面的要点：
画面1：
要点：展示 WordCountApp.java 中的 reduceByKeyRDD.reduceByKey 操作和 saveAsTextFile 保存结果的代码段。

画面2：
要点：展示 WordCountApp.java 的 main 方法，初始化 SparkConf、JavaSparkContext，以及读取文件并进行 flatMap 操作的代码。

画面3：
要点：展示 WordCountApp.java 中 flatMap 操作的 call 方法，将字符串按空格分割成单词数组。

画面4：
要点：展示 WordCountApp.java 中 mapToPairRDD.mapToPair 操作，将单词转换为 (单词, 1) 的键值对。

画面5：
要点：展示 WordCountApp.java 中 reduceByKeyRDD.reduceByKey 操作，对键值对按单词进行聚合求和。

画面6：
要点：展示 WordCountApp.java 中 reduceByKeyRDD.saveAsTextFile 保存结果到指定目录的代码。

画面7：
要点：展示 PPT 页面，标题为“6. 弹性分布式数据集 RDD”，子标题“6.1.1. 什么是 RDD”，内容解释 RDD 是 Resilient Distributed Dataset，具有不可变、可分区、可容错等特性。

画面8：
要点：展示 PPT 页面，标题为“6. 弹性分布式数据集 RDD”，子标题“6.1.2. 为什么会产生 RDD？”，解释传统 MapReduce 的缺陷和 RDD 的优势。

画面9：
要点：展示 WordCountApp.java 中 reduceByKeyRDD.reduceByKey 操作的代码，用于对键值对按单词进行聚合求和。

画面10：
要点：展示 WordCountApp.java 中 flatMap 操作的 call 方法，将字符串按空格分割成单词数组。

画面11：
要点：展示 WordCountApp.java 中 mapToPairRDD.mapToPair 操作的代码，将单词转换为 (单词, 1) 的键值对。

画面12：
要点：展示 WordCountApp.java 中 reduceByKeyRDD.reduceByKey 操作的代码，用于对键值对按单词进行聚合求和。

画面13：
要点：展示 WordCountApp.java 中 reduceByKeyRDD.saveAsTextFile 保存结果到指定目录的代码。

画面14：
要点：展示 PPT 页面，标题为“6.1.1. 什么是 RDD”，内容解释 RDD 是 Resilient Distributed Dataset，具有不可变、可分区、可容错等特性。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd.reduceByKey(new Function2<Integer, Integer, Integer>() {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
});
// 保存结果到指定的目录或文件
reduceByKeyRdd.saveAsTextFile(args[1]);
// 关闭，释放资源
jac.stop();
```

画面2：
```java
public class WordCountApp {
    public static void main(String[] args) {
        // Spark的配置
        SparkConf sparkConf = new SparkConf()
                .setAppName("WordCountApp");
        // 定义上下文对象，它是程序的入口
        JavaSparkContext jac = new JavaSparkContext(sparkConf);
        // 读取文件
        JavaRDD<String> fileRdd = jac.textFile(args[0]);
        // 互转操作，并且按照空格分割
        JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
            @Override
            public Iterator<String> call(String s) throws Exception {
                String[] ss = s.split(" ");
                return Arrays.asList(ss).iterator();
            }
        });
    }
}
```

画面3：
```java
// 定义上下文对象，它是程序的入口
JavaSparkContext jac = new JavaSparkContext(sparkConf);
// 读取文件
JavaRDD<String> fileRdd = jac.textFile(args[0]);
// 互转操作，并且按照空格分割
JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面4：
```java
// 互转操作，并且按照空格分割
JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
// 对单词做计数
JavaPairRDD<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object, Integer>() {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
```

画面5：
```java
// 对单词做计数
JavaPairRDD<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object, Integer>() {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
```

画面6：
```java
// 对相同的单词做加操作
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd.reduceByKey(new Function2<Integer, Integer, Integer>() {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
});
// 保存结果到指定的目录或文件
reduceByKeyRdd.saveAsTextFile(args[1]);
// 关闭，释放资源
jac.stop();
```

画面7：
```markdown
6. 弹性分布式数据集 RDD
6.1. RDD概述
6.1.1. 什么是RDD
RDD（Resilient Distributed Dataset）叫做弹性分布式数据集，是Spark中最基本的数据抽象，它代表一个不可变、可分区、可容错并可并行计算的集合。RDD具有数据流模型的特点：自动容错、位置感知调度和可伸缩性。RDD允许用户在执行多个查询时显式地将数据保存在内存中，后续的查询能够重用这些数据，这极大地提升了查询速度。
• Dataset：一个数据集合，用于存放数据。
• Distributed：RDD中的数据是分布式存储的，可用于分布式计算。
• Resilient：RDD中的数据可以存储在内存中或者磁盘中。
6.1.2. 为什么会产生RDD？
传统的MapReduce虽然具有自动容错、平衡负载和可扩展性的优点，但是其最大的缺点是采用非循环的数据流模型，使得在迭代计算中要进行大量的磁盘IO操作。RDD正是解决这一缺点的抽象方法。
RDD是Spark提供的最重要的抽象的概念，它是一种具有容错机制的特殊集合，可以分布在集群的节点上，以迭代式编程操作集合，进行各种并行操作，可以把RDD的原始数据进行缓存，方便进行多次重用，避免重复计算。
```

画面8：
```markdown
6. 弹性分布式数据集 RDD
6.1. RDD概述
6.1.2. 为什么会产生RDD？
传统的MapReduce虽然具有自动容错、平衡负载和可扩展性的优点，但是其最大的缺点是采用非循环的数据流模型，使得在迭代计算中要进行大量的磁盘IO操作。RDD正是解决这一缺点的抽象方法。
RDD是Spark提供的最重要的抽象的概念，它是一种具有容错机制的特殊集合，可以分布在集群的节点上，以迭代式编程操作集合，进行各种并行操作，可以把RDD的原始数据进行缓存，方便进行多次重用，避免重复计算。
6.2. RDD的类型
Spark中的操作大致可以分为四类操作，分别是创建操作、转换操作、控制操作和行动操作。
```

画面9：
```java
// 对相同的单词做加操作
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd.reduceByKey(new Function2<Integer, Integer, Integer>() {
    @Override
    public Integer call(Integer v1, Integer v2) throws Exception {
        return v1 + v2;
    }
});
```

画面10：
```java
// 互转操作，并且按照空格分割
JavaRDD<String> flatMapRdd = fileRdd.flatMap(new FlatMapFunction<String, String>() {
    @Override
    public Iterator<String> call(String s) throws Exception {
        String[] ss = s.split(" ");
        return Arrays.asList(ss).iterator();
    }
});
```

画面11：
```java
// 对单词做计数
JavaPairRDD<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object, Integer>() {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
```

画面12：
```java
// 对相同的单词做加操作
JavaPairRDD<Object, Integer> reduceByKeyRdd = mapToPairRdd

