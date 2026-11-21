# 21.弹性分布式数据集RDD之常用算子操作（reduceByKey）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\21.弹性分布式数据集RDD之常用算子操作（reduceByKey）_【海量资源尽在 666java.com】.mp4
- 时长 1分25秒（音频 85s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下ReduceByKey这个操作那么其实这个操作呢我们应该是比较熟悉了那么就是在我们的KeyV对的一些这个数据中呢按照我们相同的这个Key呢去做一个这样的一个分组然后呢我们会把一些它的value值呢做一些这种操作那么其实就是我们前面所写的这个单词的一个统计
[00:27] 那么接着前面的我们例子中呢其实在这个位置我们通过这个map2.pale呢去得到一个kv这样的一个结构然后呢在这个位置呢我们就会把相同这个k的这个两个值呢给它去做一个相加的操作那么就可以得出我们那个单词的一个奇数啊这样的一个功能好那么我们来看一下啊这样这个API的使用
[00:52] 那么其实这个操作在前面我们是不是已经写过类似的这样的一个代码了OK好我们来执行一下看一下它的一个效果我们来等待一下它的一个执行好那么我们来看一下结果结果是不是在这个位置把相同的key然后它的值做一个相加OK好那么这个其实就是我们所讲的reduced by key这样的一个算子操作
[01:20] 好 那么关于这个ReduceByK的一个操作就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark RDD 的 reduceByKey 操作对单词计数进行聚合，并展示代码执行过程和控制台输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark RDD 的 reduceByKey 操作代码，包括创建 SparkConf、JavaSparkContext、生成 RDD、flatMap 分割、mapToPair 标记计数、reduceByKey 聚合、collect 收集数据等步骤。
画面2：代码与画面1相同，但光标位置在 reduceByKey 行，强调该操作。
画面3：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(Spark,1)。
画面4：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(Spark,1)。
画面5：代码与画面1相同，但光标位置在 reduceByKey 行，右键弹出菜单，选择“Run 'testReduceByKey'”。
画面6：代码与画面1相同，但光标位置在 reduceByKey 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(Spark,1)。
画面7：代码与画面1相同，但光标位置在 collect 行，弹出“Installing tools...”提示框，表示正在安装工具。
画面8：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(Spark,1)。
画面9：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(Spark,1)、(hello,1)、(world,1)。
画面10：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(Spark,1)、(hello,1)、(world,1)。
画面11：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(Spark,1)、(hello,1)、(world,1)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void testReduceByKey() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 按照key相同的键进行相加操作
    JavaPairRDD<Object, Integer> rdd3 = rdd2.reduceByKey((v1, v2) -> v1 + v2);
    //收集数据
    List<Tuple2<Object, Integer>> list = rdd3.collect();
    for (Tuple2<Object, Integer> o : list) {
        System.out.println(o);
    }
}
```

画面2：
```java
@Test
public void testReduceByKey() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 按照key相同的键进行相加操作
    JavaPairRDD<Object, Integer> rdd3 = rdd2.reduceByKey((v1, v2) -> v1 + v2);
    //收集数据
    List<Tuple2<Object, Integer>> list = rdd3.collect();
    for (Tuple2<Object, Integer> o : list) {
        System.out.println(o);
    }
}
```

画面3：
```java
@Test
public void testMapToPair() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 收集数据
    List<Tuple2<Object, Object>> list = rdd2.collect();
    for (Tuple2<Object, Object> o : list) {
        System.out.println(o);
    }
}
```

画面4：
```java
@Test
public void testMapToPair() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 收集数据
    List<Tuple2<Object, Object>> list = rdd2.collect();
    for (Tuple2<Object, Object> o : list) {
        System.out.println(o);
    }
}
```

画面5：
```java
@Test
public void testReduceByKey() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 按照key相同的键进行相加操作
    JavaPairRDD<Object, Integer> rdd3 = rdd2.reduceByKey((v1, v2) -> v1 + v2);
    //收集数据
    List<Tuple2<Object, Integer>> list = rdd3.collect();
    for (Tuple2<Object, Integer> o : list) {
        System.out.println(o);
    }
}
```

画面6：
```java
@Test
public void testReduceByKey() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现数量标记为1
    JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    // 按照key相同的键进行相加操作
    JavaPairRDD<Object, Integer> rdd3 = rdd2.reduceByKey((v1, v2) -> v1 + v2);
    //收集数据
    List<Tuple2<Object, Integer>> list = rdd3.collect();
    for (Tuple2<Object, Integer> o : list) {
        System.out.println(o);
    }
}
```

画面7：
```java
@Test
public void testReduceByKey() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生产RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world

