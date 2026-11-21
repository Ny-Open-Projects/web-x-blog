# 画面线理解：21.弹性分布式数据集RDD之常用算子操作（reduceByKey）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\21.弹性分布式数据集RDD之常用算子操作（reduceByKey）_【海量资源尽在 666java.com】.mp4
- 抽帧：11 帧 @ 00:29, 00:49, 00:51, 00:55, 00:56, 00:57, 01:00, 01:04, 01:05, 01:08, 01:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:31:50

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark RDD 的 reduceByKey 操作对单词计数进行聚合，并展示代码执行过程和控制台输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark RDD 的 reduceByKey 操作代码，包括创建 SparkConf、JavaSparkContext、生成 RDD、flatMap 分割、mapToPair 标记计数、reduceByKey 聚合、collect 收集数据等步骤。
画面2：代码与画面1相同，但光标位置在 reduceByKey 行，强调该操作。
画面3：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(spark,1)。
画面4：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(spark,1)。
画面5：代码与画面1相同，但光标位置在 reduceByKey 行，右键弹出菜单，选择“Run 'testReduceByKey'”。
画面6：代码与画面1相同，但光标位置在 reduceByKey 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(spark,1)。
画面7：代码与画面1相同，但光标位置在 collect 行，弹出“Installing tools...”提示框，表示正在安装工具。
画面8：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(hello,1)、(world,1)、(hello,1)、(spark,1)。
画面9：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(spark,1)、(hello,1)、(world,1)。
画面10：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(spark,1)、(hello,1)、(world,1)。
画面11：代码与画面1相同，但光标位置在 collect 行，展示运行结果：(spark,1)、(hello,1)、(world,1)。

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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
