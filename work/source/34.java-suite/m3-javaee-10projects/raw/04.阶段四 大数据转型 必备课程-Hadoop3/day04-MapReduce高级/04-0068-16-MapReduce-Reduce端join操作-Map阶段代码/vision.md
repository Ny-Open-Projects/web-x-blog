# 画面线理解：16-MapReduce-Reduce端join操作-Map阶段代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\16-MapReduce-Reduce端join操作-Map阶段代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:23, 00:58, 01:14, 01:41, 02:53, 03:21, 03:34, 03:53, 04:34, 05:13, 05:43, 06:26, 07:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:02:40

1) 这一组画面整体在讲 MapReduce 中的 Reduce Join 操作，通过代码实现对 products.txt 和 orders.txt 两个数据源的关联查询。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了 Map 阶段的数据处理流程图。
- 输入文件：products.txt（包含产品信息）和 orders.txt（包含订单信息）。
- K1 和 V1：products.txt 的键值对（p0001,小米5,1000,2000；p0002,锤子T1,1000,3000）和 orders.txt 的键值对（1001,20150710,p0001.2；1002,20150710,p0002.3 等）。
- K2 和 V2：Map 阶段输出的键值对，其中 V2 包含了关联后的数据。
- 底部显示了 Reduce Join 的结果，包括 NULL 和关联后的数据。

画面2：
- 展示了 IntelliJ IDEA 中的项目结构。
- 项目路径：day04_mapreduce_combiner。
- 包结构：cn.itcast.mapreduce_reduce_join。
- 文件结构：包含 ReduceJoinMapper、ReduceJoinReducer 等类。

画面3：
- 展示了 ReduceJoinMapper.java 文件的代码。
- 代码内容：
  package cn.itcast.mapreduce_reduce_join;
  import org.apache.hadoop.io.LongWritable;
  import org.apache.hadoop.io.Text;
  import org.apache.hadoop.mapreduce.Mapper;
  import java.util.*;
  import org.apache.hadoop.conf.Configuration;
  import org.apache.hadoop.fs.Path;
  import org.apache.hadoop.io.*;
  import org.apache.hadoop.mapreduce.*;
  import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
  import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
  import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
  import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.*;
  import org.apache.hadoop.mapreduce.lib.join.Tuple;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce.lib.join.JoinMapper;
  import org.apache.hadoop.mapreduce.lib.join.JoinOutputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinInputFormat;
  import org.apache.hadoop.mapreduce.lib.join.JoinCombiner;
  import org.apache.hadoop.mapreduce.lib.join.JoinReducer;
  import org.apache.hadoop.mapreduce
