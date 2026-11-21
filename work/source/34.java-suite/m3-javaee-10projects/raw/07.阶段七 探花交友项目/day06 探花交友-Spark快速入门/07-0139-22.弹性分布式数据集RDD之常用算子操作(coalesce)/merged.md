# 22.弹性分布式数据集RDD之常用算子操作（coalesce）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\22.弹性分布式数据集RDD之常用算子操作（coalesce）_【海量资源尽在 666java.com】.mp4
- 时长 3分3秒（音频 184s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这个coverless这个操作那么这个函数呢主要是将RDD做一个重新的一个分区那么你比如说前面呢我们做我们测试的时候呢我们指定它为三个分区对吧然后呢如果说我们觉得可能三个分区有点不太合理了那么这个时候呢我们需要对这个分区呢做调整比如说设置成有两个分区或者说五个分区
[00:29] 那么这个时候呢就需要对耳第里做一个重新分区了那么就可以通过这个方法呢来做一个实现那么它的第一个这个参数呢是重新分区的一个数量那第二个参数呢就是是否做一个suffer然后的末运呢是fos那么接下来呢我们来实际的来测试一下那我们把这个代码呢来拷贝一下来给大家做一些这个讲解OK
[00:54] 好那么可以看到在这个位置我们定义了这样的一个RDD的一个数据那么就是1到10然后首先我们要明确一点是我们并没有给他设置这个分区并没有设置分区那么在这个位置他会拿到他的一个默认的一个分区我们这个会拿到一个4这样的一个分区然后我们对我们这个RDD做一个重新分区比如说我们目标设置为是两个分区
[01:22] 让suffer设置为false当然你设置为true也可以如果你有需要的话但是我们要注意的一点就是那么如果我们重新分区的分区数量比原有分区大的话那么要必须设置为suffer设置为true才行否则分区数是不变的然后在下面这个位置再打印它的一个分区数是这样的一个效果我们先来执行一下然后走
[01:51] 那么来看一下它的一个这个结果啊怎么样好那么我们可以看到结果呢是不是打印这个4和2呀对吧那么是不是做了一重新啊做了一个这个分区那么我们可以来测试一下原有分区呢是4比如说我要把它设置为6啊6个分区那么我们把这个support呢设置为force看它会怎么样好那我们来执行一下走好那么我们来看一下这个结果那么我们可以看到在这个位置呢是不是
[02:21] 依然打印的还是4对吧那就说明什么呢这个分区失败了或者说我们调用这个方法呢最终是其实没有达到我们的一个预期那么如果我们把这个suffer设置为true设置为true让它重新去做一个数据的分配那么我们再来看一下这个结果好那我们稍微等待一下那么OK来看一下这个结果那么结果在第二个打印的值是不是6那么第二个打印值是我们的这个重新分区之后的一个分区数
[02:51] 所以说可以看到这个才是有效的所以这一点大家一定要注意好那么关于我们coverless的一个重新分区的方法使用的就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
19/08/12 23:37:16 INFO Utils: Successfully started Service 'org.apache.Spark.network.netty.NettyBlockTransferService'.
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

