# 17.弹性分布式数据集RDD之常用算子操作（filter）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\17.弹性分布式数据集RDD之常用算子操作（filter）_【海量资源尽在 666java.com】.mp4
- 时长 3分1秒（音频 181s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下future这个操作那么我们首先来看一下这个方法的一个定义那么future呢它其实是对rdd中的一些每一个元素呢都执行一个指定的函数来过滤一个新的一个rdd那么任何原有的rdd中的元素在新的rdd中呢都有且只有一个元素与之对应那么也就是说它其实
[00:27] 相比较我们之前的一个map操作呢是可以去做一个过滤的这样的一个操作啊好那么接下来呢我们就实际的来测试一下那么下面呢我们就来写一个操作啊叫做写个方法那么返回指南式word叫test什么啊就fuse好那么我们给大家一个test这样的一个注解然后呢我们就把前面的这两个啊把这个吧这三个我们拷贝过来
[00:56] 那么拷贝过来之后呢我们就去做一个filt这样的一个处理那么它所接收的呢我们可以直接来写就是这个Lamb的表达式那么比如说我们这个V1比如说我们设置一个条件就是我们这个位置去过滤我们的这个数据比如说我们要求这个大于2的数据这个形成
[01:26] 用这个我们这样写吧就是用这个大于2的数据然后呢来这个组成组成一个新的新的RDD那么比如说我们这个V1大于2OK那么它所返回的呢其实就是一个新的一个RDD了这叫RDD什么呢2OK好那么接下来呢我们就对这个RDD呢去做一个便利2
[01:56] 然后呢点connector去做一个这个收集然后呢我们去拿到一个list然后呢对它呢去做一个便利for each然后呢我们去通过lamb的表达式然后呢去做一个输出那么我们就直接来输出我们的这个值吧最后呢去做一个关闭就是gsc.stop
[02:26] OK好那么到这里呢就测试完成了那么接下来呢我们就来运行一下好那我们来等待它的一个执行那么OK那么这个结果呢就出来了那么可以看到呢在我们控制台呢我们输出的内容啊我们这个新的这个RDD呢它的值呢是345那么是不是就满足了我们这个条件就是大于2这个条件来组成一个新的一个这个RDD
[02:52] OK好那么这个操作呢其实就是谁呢Future这样的一个操作OK好那么关于这个Future过滤那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 Spark RDD 的 filter 操作，对数据进行过滤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Spark RDD 的 filter 操作的代码示例。
- 代码内容：
  ```java
  // 收集数据
  List<Object> list = rdd2.collect();
  for (Object o : list) {
      System.out.println(o);
  }
  ```
- 页面左侧显示了课程大纲，当前章节为“6.3.2. filter”。

画面 2：
- 展示了 IntelliJ IDEA 中的代码编辑器，显示了 RDD 的 map 操作代码。
- 代码内容：
  ```java
  // 将rdd1中每一个元素都乘以2，生成新的rdd
  JavaRDD<Integer> rdd2 = rdd1.map(new MyFunction()); // 方案一
  JavaRDD<Integer> rdd2 = rdd1.map(v1 -> v1 * 2); // 方案二
  List<Integer> list = rdd2.collect();
  list.forEach(integer -> System.out.println(integer));
  jsc.stop();
  ```

画面 3：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `@Test public void testFilter() {` 方法的起始位置。
- 代码内容：
  ```java
  @Test
  public void testFilter() {
  ```

画面 4：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `public void testMap() {` 方法的起始位置。
- 代码内容：
  ```java
  @Test
  public void testMap() {
      SparkConf sparkConf = new SparkConf()
              .setAppName("RddOperation")
              .setMaster("local[*]");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      // 生成一个测试rdd数据集
      JavaRDD<Integer> rdd1 = jsc.parallelize(Arrays.asList(1, 2, 3, 4, 5));
      // 将rdd1中每一个元素都乘以2，生成新的rdd
      JavaRDD<Integer> rdd2 = rdd1.map(new MyFunction()); // 方案一
      JavaRDD<Integer> rdd2 = rdd1.map(v1 -> v1 * 2); // 方案二
      List<Integer> list = rdd2.collect();
      list.forEach(integer -> System.out.println(integer));
      jsc.stop();
  }
  ```

画面 5：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `@Test public void testFilter() {` 方法的起始位置。
- 代码内容：
  ```java
  @Test
  public void testFilter() {
      SparkConf sparkConf = new SparkConf()
              .setAppName("RddOperation")
              .setMaster("local[*]");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      // 生成一个测试rdd数据集
      JavaRDD<Integer> rdd1 = jsc.parallelize(Arrays.asList(1, 2, 3, 4, 5));
  ```

画面 6：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `rdd1.filter(v1 -> v1` 位置，显示了 `Function<Integer, Boolean>` 的自动补全建议。
- 代码内容：
  ```java
  rdd1.filter(v1 -> v1
  ```

画面 7：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `rdd1.filter(v1 -> v1` 位置。
- 代码内容：
  ```java
  rdd1.filter(v1 -> v1
  ```

画面 8：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `rdd1.filter(v1 -> v1` 位置，显示了 `RDDStorageInfo` 等类的自动补全建议。
- 代码内容：
  ```java
  rdd1.filter(v1 -> v1
  ```

画面 9：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `rdd2.collect()` 位置，显示了 `collect()` 方法的自动补全建议。
- 代码内容：
  ```java
  rdd2.collect()
  ```

画面 10：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `rdd1.filter(v1 -> v1 > 2)` 位置。
- 代码内容：
  ```java
  // 过滤数据，用大于2的数据组成一个新的rdd
  JavaRDD<Integer> rdd2 = rdd1.filter(v1 -> v1 > 2);
  List<Integer> list = rdd2.collect();
  ```

画面 11：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `list.forEach(integer -> System.out.println(integer);` 位置，显示了 `int` 类型的自动补全建议。
- 代码内容：
  ```java
  list.forEach(integer -> System.out.println(integer);
  ```

画面 12：
- 展示了 IntelliJ IDEA 中的代码编辑器，光标位于 `list.forEach(integer -> System.out.println(integer);` 位置。
- 代码内容：
  ```java
  list.forEach(integer -> System.out.println(integer);
  ```

画面 13：
- 展示了 IntelliJ IDEA 中的运行面板，显示“Instantiating tests...”。
- 代码内容：
  ```java
  // 无代码内容
  ```

画面 14：
- 展示了 Typora 编辑器中的文档内容，包含“6.3.2. filter”章节。
- 文档内容：
  ```
  filter 是对RDD中的每个元素都执行一个指定的函数来过滤产生一个新的RDD，任何RDD中的元素在新RDD中都有且只有一个元素与之对应。

  @Test
  public void testFilter() {
      SparkConf sparkConf = new SparkConf()
              .setAppName("RddOperation")
              .setMaster("local[*]");
      JavaSparkContext jsc = new JavaSparkContext(sparkConf);
      // 生成一个测试rdd数据集
      JavaRDD<Integer> rdd1 = jsc.parallelize(Arrays.asList(1, 2, 3, 4, 5));
      // 过滤数据，用大于2的数据组成一个新的rdd
      JavaRDD<Integer> rdd2 = rdd1.filter(v1 -> v1 > 2);
      // 收集数据
      List<Integer> list = rdd2.collect();
      for (Integer o : list) {
          System.out.println(o);
      }
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面 1 和 14：PPT 标题为“6.3.2. filter”，内容为“filter 是对RDD中的每个元素都执行一个指定的函数来过滤产生一个新的RDD，任何RDD中的元素在新RDD中都有且只有一个元素与之对应。”
- 无架构图或流程图。
- 无表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 已按要求输出。

