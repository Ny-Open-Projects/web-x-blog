# 画面线理解：5.4 DataSet转换操作

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.4 DataSet转换操作_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:43, 02:13, 02:17, 02:51, 03:34, 03:57, 04:01, 04:48, 06:00, 06:57, 08:12, 08:58, 09:03, 09:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:23:04

1) 这一组画面整体在讲什么（一句话）：
Flink DataSet API 中的转换操作，包括 Map、FlatMap、MapPartition、Filter、Reduce、ReduceGroup、Aggregate、Distinct、Join、OuterJoin、CoGroup、Cross、Union、Rebalance、Hash-Partition、Range-Partition、自定义分区和排序分区等算子的代码示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 标题：1.3 转换操作
- 内容：介绍 Map、FlatMap、MapPartition 等转换操作。
- 代码示例：
  data.map(new MapFunction<String, Integer>() {
      public Integer map(String value) { return Integer.parseInt(value); }
  });
  data.flatMap(new FlatMapFunction<String, String>() {
      public void flatMap(String value, Collector<String> out) {
          for (String s : value.split(" ")) {
              out.collect(s);
          }
      }
  });
  data.mapPartition(new MapPartitionFunction<String, Long>() {
      public void mapPartition(Iterable<String> values, Collector<Long> out) {
          long c = 0;
          for (String s : values) {
              c++;
          }
          out.collect(c);
      }
  });

画面 2:
- 代码示例：
  data.mapPartition(new MapPartitionFunction<String, Long>() {
      public void mapPartition(Iterable<String> values, Collector<Long> out) {
          long c = 0;
          for (String s : values) {
              c++;
          }
          out.collect(c);
      }
  });

画面 3:
- 代码示例：
  data.filter(new FilterFunction<Integer>() {
      public boolean filter(Integer value) { return value > 1000; }
  });

画面 4:
- 代码示例：
  data.reduce(new ReduceFunction<Integer>() {
      public Integer reduce(Integer a, Integer b) { return a + b; }
  });

画面 5:
- 代码示例：
  data.reduceGroup(new GroupReduceFunction<Integer, Integer>() {
      public void reduce(Iterable<Integer> values, Collector<Integer> out) {
          int prefixSum = 0;
          for (Integer i : values) {
              prefixSum += i;
          }
          out.collect(prefixSum);
      }
  });

画面 6:
- 代码示例：
  data.reduceGroup(new GroupReduceFunction<Integer, Integer>() {
      public void reduce(Iterable<Integer> values, Collector<Integer> out) {
          int prefixSum = 0;
          for (Integer i : values) {
              prefixSum += i;
          }
          out.collect(prefixSum);
      }
  });

画面 7:
- 代码示例：
  Dataset<Tuple3<Integer, String, Double>> input = // [...]
  Dataset<Tuple3<Integer, String, Double>> output = input.aggregate(SUM, 0).and(MIN, 2);

画面 8:
- 代码示例：
  data.distinct();
  result = input.join(input2)
  .where(0)
  .equalTo(1);

画面 9:
- 代码示例：
  result = input1.leftOuterJoin(input2)
  .where(0)
  .equalTo(1)
  .with(new JoinFunction<String, String, String>() {
      public String join(String v1, String v2) {
          // v1 might be null for leftOuterJoin
          // v2 might be null for rightOuterJoin
          // v1 or v2 might be null for fullOuterJoin
      }
  });

画面 10:
- 代码示例：
  result = input1.cross(input2);
  Dataset<Tuple2<Integer, String>> result = data1.cross(data2);

画面 11:
- 代码示例：
  Dataset<String> result = data1.union(data2);

画面 12:
- 代码示例：
  Dataset<String> result = in.rebalance()
  .map(new Mapper());

画面 13:
- 代码示例：
  Dataset<Tuple2<String, Integer>> in = // [...]
  Dataset<Integer> result = in.partitionByHash(8).mapPartition(new PartitionMapper());

画面 14:
- 代码示例：
  Dataset<Tuple2<String, Integer>> in = // [...]
  Dataset<Integer> result = in.partitionByRange(8).mapPartition(new PartitionMapper());

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
