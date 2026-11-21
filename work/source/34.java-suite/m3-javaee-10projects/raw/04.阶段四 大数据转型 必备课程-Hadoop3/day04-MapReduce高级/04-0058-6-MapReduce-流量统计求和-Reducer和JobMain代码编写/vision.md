# 画面线理解：6-MapReduce-流量统计求和-Reducer和JobMain代码编写

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day04-MapReduce高级
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day04-MapReduce高级\6-MapReduce-流量统计求和-Reducer和JobMain代码编写【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:41, 01:54, 03:11, 03:42, 04:13, 04:28, 04:55, 06:00, 06:24, 06:45, 07:14, 08:23, 09:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 04:28:30

1) 这一组画面整体在讲如何编写一个 Hadoop MapReduce 程序，重点是实现一个自定义的 FlowCountReducer 类和 JobMain 驱动类，用于对流量数据进行统计。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，当前编辑的是 FlowCountReducer.java 文件，位于包 cn.itcast.mapproduce_flowcount 中，准备编写 reducer 逻辑。
画面2：展示 Map 阶段和 Reduce 阶段的数据流转示意图，Map 阶段将 Text 转换为 FlowBean，Reduce 阶段对 FlowBean 进行聚合。
画面3：在 Map 阶段示意图中，左侧添加了 LongWritable 作为 Key，表示 Map 阶段输出的 Key 类型。
画面4：在 FlowCountReducer.java 中，开始编写 reduce 方法，声明了变量 upFlow、downFlow、upCountFlow、downCountFlow。
画面5：在 reduce 方法中，使用 value.getUpCountFlow() 获取 FlowBean 中的 upCountFlow 值。
画面6：查看 FlowBean 类的结构，确认其包含 upFlow、downFlow、upCountFlow、downCountFlow 等字段。
画面7：在 reduce 方法中，将 value.getUpCountFlow() 的值累加到 upFlow 变量中。
画面8：在 reduce 方法中，将 value.getDownCountFlow() 的值累加到 downCountFlow 变量中。
画面9：在 JobMain.java 中，开始编写主类，导入必要的包。
画面10：在 JobMain.java 中，编写 run 方法的骨架，返回 0。
画面11：在 JobMain.java 中，创建 Job 对象，并设置输入格式、输入路径、Mapper 类、输出 Key 类和 Value 类。
画面12：在 JobMain.java 中，设置 Combiner 类。
画面13：在 JobMain.java 中，设置 Reducer 类、Reduce 阶段的输出 Key 类和 Value 类。
画面14：在 JobMain.java 中，设置输出格式和输出路径。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面4：
```java
package cn.itcast.mapproduce_flowcount;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class FlowCountReducer extends Reducer<Text, FlowBean, Text, FlowBean> {
    @Override
    protected void reduce(Text key, Iterable<FlowBean> values, Context context) throws IOException, InterruptedException {
        FlowBean flowBean = new FlowBean();
        Integer upFlow = 0;
        Integer downFlow = 0;
        Integer upCountFlow = 0;
        Integer downCountFlow = 0;
        for (FlowBean value : values) {
            upFlow += value.getUpFlow();
            downFlow += value.getDownFlow();
            upCountFlow += value.getUpCountFlow();
            downCountFlow += value.getDownCountFlow();
        }
        flowBean.setUpFlow(upFlow);
        flowBean.setDownFlow(downFlow);
        flowBean.setUpCountFlow(upCountFlow);
        flowBean.setDownCountFlow(downCountFlow);
    }
}
```

画面11：
```java
package cn.itcast.mapproduce;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
import java.io.IOException;

public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapproduce_wordcount");
        job.setJarByClass(JobMain.class);
        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("hdfs://node01:8020/input/flowcount"));
        job.setMapperClass(FlowCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(FlowBean.class);
        job.setCombinerClass(MyCombiner.class);
        job.setReducerClass(FlowCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FlowBean.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/out/flowcount"));
        return job.waitForCompletion(true) ? 0 : 1;
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：Map 阶段：Text (V1) → FlowBean (V2)；Reduce 阶段：FlowBean (V3) → 文件。
画面3：Map 阶段：LongWritable (K1) → FlowBean (V2)；Reduce 阶段：FlowBean (V3) → 文件。
画面11：Job 设置流程：设置输入格式 → 设置输入路径 → 设置 Mapper 类 → 设置 Map 阶段输出类型 → 设置 Reducer 类 → 设置 Reduce 阶段输出类型 → 设置 Combiner 类 → 设置输出格式 → 设置输出路径。
画面12：Job 设置流程：设置输入格式 → 设置输入路径 → 设置 Mapper 类 → 设置 Map 阶段输出类型 → 设置 Reducer 类 → 设置 Reduce 阶段输出类型 → 设置 Combiner 类 → 设置输出格式 → 设置输出路径。
画面13：Job 设置流程：设置输入格式 → 设置输入路径 → 设置 Mapper 类 → 设置 Map 阶段输出类型 → 设置 Reducer 类 → 设置 Reduce 阶段输出类型 → 设置 Combiner 类 → 设置输出格式 → 设置输出路径。
画面14：Job 设置流程：设置输入格式 → 设置输入路径 → 设置 Mapper 类 → 设置 Map 阶段输出类型 → 设置 Reducer 类 → 设置 Reduce 阶段输出类型 → 设置 Combiner 类 → 设置输出格式 → 设置输出路径。

5) 无。
