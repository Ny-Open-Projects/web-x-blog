# 画面线理解：22.弹性分布式数据集RDD之常用算子操作（coalesce）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\22.弹性分布式数据集RDD之常用算子操作（coalesce）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:47, 00:51, 00:53, 01:49, 01:52, 01:58, 02:01, 02:03, 02:17, 02:19, 02:33, 02:40, 02:42, 03:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:32:40

1) 这一组画面整体在讲什么（一句话）：
演示 Spark RDD 的 coalesce 操作，通过修改 shuffle 参数观察分区数变化对执行结果的影响。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Spark 文档中关于 coalesce 的说明，以及一个测试用例的代码片段，其中 shuffle 参数默认为 false。
画面 2: 展示了测试用例中对 RDD 进行 flatMap、mapToPair 和 reduceByKey 操作的代码。
画面 3: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false。
画面 4: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false。
画面 5: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false。
画面 6: 展示了测试用例运行后控制台输出的 Spark 日志，显示作业开始并成功执行。
画面 7: 展示了测试用例运行后控制台输出的 Spark 日志，显示作业开始并成功执行。
画面 8: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false。
画面 9: 展示了测试用例运行后控制台输出的 Spark 日志，显示作业开始并成功执行。
画面 10: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false。
画面 11: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 false，但运行时抛出 FactoryConfigurationError 异常。
画面 12: 展示了测试用例中 coalesce 操作的代码，shuffle 参数为 true。
画面 13: 展示了测试用例运行后控制台输出的 Spark 日志，显示作业开始并成功执行。
画面 14: 展示了 Spark 文档中关于 coalesce 的说明，以及一个测试用例的代码片段，其中 shuffle 参数默认为 false。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Test
public void testCoalesce() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
    System.out.println(rdd.getNumPartitions()); //4
    JavaRDD<Integer> rdd2 = rdd.coalesce(2, shuffle:false);
    System.out.println(rdd2.getNumPartitions()); //2
    //收集数据
    List<Integer> list = rdd2.collect();
    for (Integer o : list) {
        System.out.println(o);
    }
}
```
画面 2:
```java
JavaRDD<String> rdd1 = rdd.flatMap(s -> Arrays.asList(s.split(regex)).iterator());
// 把每一个单词的出现数量标记为1
JavaPairRDD<Object, Integer> rdd2 = rdd1.mapToPair(s -> new Tuple2<>(s, 1));
// 按照key相同的数进行相加操作
JavaPairRDD<Object, Integer> rdd3 = rdd2.reduceByKey((v1, v2) -> v1 + v2);
//收集数据
List<Tuple2<Object, Integer>> list = rdd3.collect();
for (Tuple2<Object, Integer> o : list) {
    System.out.println(o);
}
```
画面 3:
```java
@Test
public void testCoalesce() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
    System.out.println(rdd.getNumPartitions()); //4
    JavaRDD<Integer> rdd2 = rdd.coalesce(2, shuffle:false);
    System.out.println(rdd2.getNumPartitions()); //2
    //收集数据
    List<Integer> list = rdd2.collect();
    for (Integer o : list) {
        System.out.println(o);
    }
}
```
画面 4:
```java
@Test
public void testCoalesce() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
    System.out.println(rdd.getNumPartitions()); //4
    JavaRDD<Integer> rdd2 = rdd.coalesce(2, shuffle:false);
    System.out.println(rdd2.getNumPartitions()); //2
    //收集数据
    List<Integer> list = rdd2.collect();
    for (Integer o : list) {
        System.out.println(o);
    }
}
```
画面 5:
```java
//生成RDD
JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
System.out.println(rdd.getNumPartitions()); //4
// 重分区，shuffle: 是否重分配存储，如果分区数大于原有分区数，就需要设置为true
JavaRDD<Integer> rdd2 = rdd.coalesce(numPartitions:2, shuffle:false);
```
画面 6:
```text
19/08/12 23:37:16 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService'.
19/08/12 23:37:16 INFO BlockManagerMaster: Registering block manager WIN-A...
19/08/12 23:37:16 INFO BlockManagerMasterEndpoint: Registering block manager WIN-A...
19/08/12 23:37:16 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(drive...
19/08/12 23:37:16 INFO SparkContext: Starting job: collect at RddOperation.java:160
19/08/12 23:37:16 INFO DAGScheduler: Got job 0 (collect at RddOperation.java:160)
19/08/12 23:37:16 INFO DAGScheduler: Parents of final stage: List()
19/08/12 23:37:16 INFO DAGScheduler: Missing parents: List()
19/08/12 23:37:17 INFO MemoryStore: Block broadcast_0 stored as values in memory (4...
19/08/12 23:37:17 INFO BlockManagerInfo: Added broadcast_0 piece0 stored as bytes in memory on...
```
画面 7:
```text
19/08/12 23:37:16 INFO BlockManagerMaster: Registering block manager BlockManagerId(drive...
19/08/12 23:37:16 INFO BlockManagerMasterEndpoint: Registering block manager WIN-A...
19/08/12 23:37:16 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(drive...
19/08/12 23:37:16 INFO SparkContext: Starting job: collect at RddOperation.java:160
19/08/12 23:37:16 INFO DAGScheduler: Got job 0 (collect at RddOperation.java:160)
19/08/12 23:37:16 INFO DAGScheduler: Parents of final stage: List()
19/08/12 23:37:16 INFO DAGScheduler: Missing parents: List()
19/08/12 23:37:17 INFO MemoryStore: Block broadcast_0 stored as values in memory (4...
19/08/12 23:37:17 INFO BlockManagerInfo: Added broadcast_0 piece0 stored as bytes in memory on...
```
画面 8:
```java
@Test
public void testCoalesce() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[*]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10));
    System.out.println(rdd.getNumPartitions()); //4
    JavaRDD<Integer> rdd2 = rdd.coalesce(2, shuffle:false);
    System.out.println(rdd2.getNumPartitions()); //2
    //收集
