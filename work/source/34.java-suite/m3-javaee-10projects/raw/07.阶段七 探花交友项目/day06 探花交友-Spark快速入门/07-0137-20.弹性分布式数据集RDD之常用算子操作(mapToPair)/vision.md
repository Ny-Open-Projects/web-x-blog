# 画面线理解：20.弹性分布式数据集RDD之常用算子操作（mapToPair）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\20.弹性分布式数据集RDD之常用算子操作（mapToPair）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:41, 00:42, 01:11, 01:13, 01:15, 01:18, 01:19, 01:21, 01:23, 01:24, 01:25, 01:27, 01:39, 01:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:31:04

1) 这一组画面整体在讲什么（一句话）：
演示 Spark Java API 中 mapToPair 和 reduceByKey 操作的代码实现与执行过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 中的文档，内容为 6.3.5. mapToPair 小节，代码示例展示了如何创建 SparkConf、JavaSparkContext，生成 RDD，使用 flatMap 分割字符串，再使用 mapToPair 将每个单词映射为 (单词, 1) 的键值对，最后使用 collect() 收集结果。
画面2：展示 Typora 中的文档，内容为 6.3.6. reduceByKey 小节，文字解释 reduceByKey 的含义：对 RDD 中 Key 相同的元素的 Value 进行 reduce。
画面3：与画面1内容相同，是同一段代码的截图。
画面4：展示 IntelliJ IDEA 中 WordCountApp.java 文件的代码，包含 mapToPairRdd.mapToPair 的实现，以及 reduceByKeyRdd.reduceByKey 的实现，用于对单词计数。
画面5：展示 IntelliJ IDEA 中 testMapPartitions 方法的代码，创建 SparkConf 和 JavaSparkContext，生成包含数字 1 到 10 的 RDD，然后使用 mapPartitions 操作对每个分区的数据进行处理。
画面6：展示 IntelliJ IDEA 中 testMapPartitions 方法的代码，与画面5内容相同。
画面7：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同。
画面8：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，光标位于注释“按空格分割”之后。
画面9：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，光标位于生成 RDD 的代码行上。
画面10：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，终端显示任务执行完成。
画面11：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，终端显示任务执行完成，结果为 (hello,1)、(world,1)、(spark,1)。
画面12：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，终端显示任务执行完成，结果为 (hello,1)、(world,1)、(spark,1)。
画面13：展示 IntelliJ IDEA 中 testMapToPair 方法的代码，与画面1内容相同，光标位于注释“按空格分割”之后。
画面14：与画面1内容相同，是同一段代码的截图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现次数标记为1
    JavaPairRDD<Object, Object> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    //收集数据
    List<Tuple2<Object, Object>> list = rdd2.collect();
    for (Tuple2<Object, Object> o : list) {
        System.out.println(o);
    }
}
```
画面2：
```java
// 命名含义，reduceByKey就是对元素为KV的RDD中Key相同的元素的Value进行reduce。因此，Key相同的多个元素的值被reduce为一个值，然后与原RDD中的Key组成一个新的KV对。
```
画面4：
```java
// 对单词做计数
@Override
public Tuple2<Object, Integer> mapToPairRdd = flatMapRdd.mapToPair(new PairFunction<String, Object> {
    @Override
    public Tuple2<Object, Integer> call(String s) throws Exception {
        return new Tuple2<>(s, 1);
    }
});
// 对相同的单词做加法操作
@Override
public Integer call(Integer v1, Integer v2) throws Exception {
    return v1 + v2;
}
```
画面5：
```java
public void testMapPartitions () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 分区操作
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10), numSlices: 3);
    JavaRDD<Integer> rdd2 = rdd.mapPartitions(integerIterator -> {
        List<Integer> result = new ArrayList<>();
        while (integerIterator.hasNext()) {
            Integer i = integerIterator.next();
            result.add(i);
        }
        return result.iterator();
    });
    System.out.println("分区数据：" + result);
    return result.iterator();
}
```
画面6：
```java
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
JavaPairRDD<Object, Object> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
List<Tuple2<Object, Object>> list = rdd2.collect();
for (Tuple2<Object, Object> o : list) {
    System.out.println(o);
}
```
画面7：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现次数标记为1
    JavaPairRDD<Object, Object> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
    //收集数据
    List<Tuple2<Object, Object>> list = rdd2.collect();
    for (Tuple2<Object, Object> o : list) {
        System.out.println(o);
    }
}
```
画面8：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
    // 按照空格分割
    JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split("")).iterator());
    // 把每一个单词的出现次数标记为1
    JavaPairRDD<Object, Object> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
}
```
画面9：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
}
```
画面10：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
}
```
画面11：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
}
```
画面12：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    // 生成RDD
    JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
}
```
画面13：
```java
@Test
public void testMapToPair () {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*
