# 画面线理解：19.弹性分布式数据集RDD之常用算子操作（mapPartitions）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\19.弹性分布式数据集RDD之常用算子操作（mapPartitions）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:29, 01:54, 02:44, 02:47, 02:55, 03:01, 03:07, 03:11, 03:17, 03:23, 03:27, 03:30, 03:40, 04:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:30:14

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
JavaRDD<String> rdd = jsc.parallelize(Arrays.asList("hello world","hello spark"));
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
