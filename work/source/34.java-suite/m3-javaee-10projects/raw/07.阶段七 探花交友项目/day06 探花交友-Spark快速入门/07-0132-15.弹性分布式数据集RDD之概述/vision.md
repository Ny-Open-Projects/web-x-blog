# 画面线理解：15.弹性分布式数据集RDD之概述

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\15.弹性分布式数据集RDD之概述_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:19, 00:24, 00:33, 00:44, 00:51, 01:05, 02:46, 03:57, 04:03, 04:10, 04:15, 04:51, 05:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:27:26

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
        // spark的配置
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
