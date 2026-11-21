# 画面线理解：17.弹性分布式数据集RDD之常用算子操作（filter）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\17.弹性分布式数据集RDD之常用算子操作（filter）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 00:37, 00:48, 00:52, 00:59, 01:08, 01:13, 01:55, 02:00, 02:11, 02:19, 02:27, 02:34, 02:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:28:38

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
