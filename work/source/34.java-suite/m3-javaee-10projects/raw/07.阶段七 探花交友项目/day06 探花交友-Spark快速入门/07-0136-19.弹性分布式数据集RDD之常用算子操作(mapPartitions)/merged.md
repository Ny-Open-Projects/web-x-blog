# 19.弹性分布式数据集RDD之常用算子操作（mapPartitions）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\19.弹性分布式数据集RDD之常用算子操作（mapPartitions）_【海量资源尽在 666java.com】.mp4
- 时长 4分40秒（音频 281s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下这个Map Partitions这个是什么意思呢,我们一起来看一下那么Map Partitions呢,它其实是Map的一种变种那么Map呢,是输入的函数是应用于RDL中的每一个元素但是要注意的是呢,在Map Partitions中它所输入函数的是应用于每一个分区
[00:27] 把每一个分区中的内容作为一个整体来做一个处理那么这个是什么意思呢简单的给大家来解释一下就是说比如说这个呢是我们的一个数据就是我们存储的啊这么一堆这个数据那么其实在我们啊Spark在去做存储的时候呢其实呢我们是需要把这个数据呢去做什么呢去做分区的啊比如说我们哎这个这样来画一下比如说我们画它啊
[00:56] 我们去做分区然后比如说我们做了三个分区去做一个存储这个里面有数据这个里面也有这个里面也有可能每个里面的数据可能会不一样比如说这个有三个这样的数据
[01:10] 那么之前呢我们的map这个操作啊它是会对应到每一个这个元素去做一个操作啊这个是map操作那么现在呢我们这个map partitions呢它呢其实对应的是这个什么这个数据啊整体这个数据啊整体这个数据去做一个处理这个大家应该明白了吧接下来呢我们来看一下我们的这个案例啊那么可以看到在这个位置啊我们去定义了我们的一个
[01:39] 新的RDD它的值呢是1到10然后呢后面呢在这个位置我们指定了一个3代表着说我们这个数据呢去按照三个分区去做一个存储然后呢下面呢我们在这个位置那么我们通过我们的这个Map Partitions去做一个处理那我们拿到的是一个迭代器然后呢我们对这个迭代器去做一个处理那么前面我们说过那么
[02:08] 我们这十个数据分到三个区去做存储那么每一个区肯定不只是一个数据那么必然这个迭代器就会拿到一个多条数据所以在这个里面需要有一个Val的处理然后下面我们在这个位置去把我们的Route打印出来就是去把我们迭代器中所有的数据都给它遍地出来丢到我们的list集合中
[02:35] 然后呢最后呢我们返回了我们的一个迭代器然后最后呢去做一个数据的一个打印了好那么接下来呢我们来看一下这个效果啊它是怎么样的一个效果呢好那么接下来呢我们就在这个位置呢去做一个执行好那我们来等待一下它的一个执行好那么下面呢我们来看一下我们的一个这个执行的结果啊那么其实可以看到在这个位置呢我们是不是已经
[03:03] 就把我们的十个数据呢去分了三个区去做一个存储一个呢是有三条数据一个是四条数据一个呢是三条数据啊这样的一个处理那么从这个位置其实就可以看出啊那么我们的这个数据是按照这个分区的数据作为一个整体去传入到这个里面来对不对OK那么因为我们在这个位置呢是做这样的一个打印嘛哎OK
[03:30] 好那么下面呢其实这个呢所得到的结果啊跟我们MAP的结果你看起来是一样的啊其实它是不一样的啊那么可能有同学就会有疑问的就是说我们既然有这个MAP这个操作那么为什么还会有这个MAP partitions这样的一个操作呢其实原因是呢比如说假设啊假设呢我们在这个去遍历我们的集合遍历我们这个RDD中的数据的时候
[03:58] 那我们需要去把它持久化的数据库的话假设我说假设有这样的一个需求的话那么如果我们针对于每一个元素去做操作和我们针对于每一个我们的一个这个分区去做操作那么这两个执行的效率显然是不同的那么按照分区去做一个执行的效率显然是不是要比每一个这个元素去做操作是不是效率高对不对
[04:26] 所以说呢这个有些时候啊我们会使用这个map partitions去做这个操作ok那么大家这个理解他们之间的一个区别了吗ok好那么关于这个map partitions我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Spark 中 mapPartitions 操作的代码实现与执行结果，通过控制台输出展示数据按分区处理的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Spark 文档中 6.3.4. mapPartitions 小节，代码示例为测试方法 testMapPartitions，创建 SparkConf、JavaSparkContext，创建 RDD 并应用 mapPartitions 操作。
画面2：代码编辑器中显示 testMapPartitions 方法，注释“分区间操作”，代码逻辑为对整数序列 1-10 进行 mapPartitions 操作。
画面3：代码编辑器中显示 testMapPartitions 方法，注释“分区间操作”，代码逻辑为对整数序列 1-10 进行 mapPartitions 操作。
画面4：代码编辑器中显示 testMapPartitions 方法，注释“分区间操作”，代码逻辑为对整数序列 1-10 进行 mapPartitions 操作。
画面5：控制台输出 Spark 任务执行日志，包括 DAGScheduler、TaskSetManager、Executor 等组件的启动与完成信息，以及最终的“分区数据”输出。
画面6：控制台输出中“分区数据”部分被红色框选，显示三个分区的数据：[1, 2, 3]、[7, 8, 9, 10]、[4, 5, 6]。
画面7：控制台输出中“分区数据”部分被红色框选，显示三个分区的数据：[1, 2, 3]、[7, 8, 9, 10]、[4, 5, 6]。
画面8：控制台输出中“分区数据”部分被红色框选，显示三个分区的数据：[1, 2, 3]、[7, 8, 9, 10]、[4, 5, 6]。
画面9：控制台输出中“分区数据”部分被红色框选，显示三个分区的数据：[1, 2, 3]、[7, 8, 9, 10]、[4, 5, 6]。
画面10：代码编辑器中显示 testMapPartitions 方法，注释“分区间操作”，代码逻辑为对整数序列 1-10 进行 mapPartitions 操作。
画面11：代码编辑器中显示 testMapPartitions 方法，注释“分区间操作”，代码逻辑为对整数序列 1-10 进行 mapPartitions 操作。
画面12：控制台输出显示测试通过，Spark UI 停止，MapOutputTrackerMasterEndpoint 等信息。
画面13：控制台输出显示测试通过，Spark UI 停止，MapOutputTrackerMasterEndpoint 等信息。
画面14：展示 Spark 文档中 6.3.5. mapToPair 小节，介绍 mapToPair 操作的功能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void testMapPartitions() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10),3);
    JavaRDD<Integer> rdd2 = rdd.mapPartitions(integerIterator -> {
        List<Integer> result = new ArrayList<>();
        while (integerIterator.hasNext()) {
            Integer i = integerIterator.next();
            result.add(i);
        }
        System.out.println("分区数据：" + result);
        return result.iterator();
    });
    List<Integer> list = rdd2.collect();
    list.forEach(integer -> System.out.println(integer));
}
```

画面2：
```java
public void testMapPartitions() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10),3);
    JavaRDD<Integer> rdd2 = rdd.mapPartitions(integerIterator -> {
        List<Integer> result = new ArrayList<>();
        while (integerIterator.hasNext()) {
            Integer i = integerIterator.next();
            result.add(i);
        }
        System.out.println("分区数据：" + result);
        return result.iterator();
    });
    List<Integer> list = rdd2.collect();
    for (String o : list) {
        System.out.println(o);
    }
}
```

画面3：
```java
.setAppName("RddOperation")
.setMaster("local[*]");
JavaSparkContext jsc = new JavaSparkContext(sparkConf);
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello Spark"));
JavaRDD<String> rdd2 = rdd.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
// 收集数据
List<String> list = rdd2.collect();
for (String o : list) {
    System.out.println(o);
}
```

画面4：
```java
public void testMapPartitions() {
    SparkConf sparkConf = new SparkConf()
        .setAppName("RddOperation")
        .setMaster("local[1]");
    JavaSparkContext jsc = new JavaSparkContext(sparkConf);
    JavaRDD<Integer> rdd = jsc.parallelize(Arrays.asList(1,2,3,4,5,6,7,8,9,10),3);
    JavaRDD<Integer> rdd2 = rdd.mapPartitions(integerIterator -> {
        List<Integer> result = new ArrayList<>();
        while (integerIterator.hasNext()) {
            Integer i = integerIterator.next();
            result.add(i);
        }
        System.out.println("分区数据：" + result);
        return result.iterator();
    });
    List<Integer> list = rdd2.collect();
    for (String o : list) {
        System.out.println(o);
    }
}
```

画面5：
```java
19/08/12 23:22:11 INFO DAGScheduler: Created broadcast 0 from broadcast at DAGScheduler
19/08/12 23:22:11 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, local, PROCESS_LOCAL, 16777216 bytes)
19/08/12 23:22:11 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, local, PROCESS_LOCAL, 16777216 bytes)
19/08/12 23:22:11 INFO TaskSetManager: Starting task 2.0 in stage 0.0 (TID 2, local, PROCESS_LOCAL, 16777216 bytes)
19/08/12 23:22:11 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
19/08/12 23:22:11 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
19/08/12 23:22:11 INFO Executor: Running task 2.0 in stage 0.0 (TID 2)
19/08/12 23:22:11 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 854 bytes
19/08/12 23:22:11 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 821 bytes
19/08/12 23:22:11 INFO Executor: Finished task 2.0 in stage 0.0 (TID 2). 768 bytes
19/08/12 23:22:11 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 3
19/08/12 23:22:11 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 3
19/08/12 23:22:11 INFO TaskSetManager: Finished task 2.0 in stage 0.0 (TID 2) in 4
19/08/12 23:22:11 INFO DAGScheduler: ResultStage 0 (collect at RddOperation.java:9)
19/08/12 23:22:11 INFO SparkContext: Job 0 finished: collect

