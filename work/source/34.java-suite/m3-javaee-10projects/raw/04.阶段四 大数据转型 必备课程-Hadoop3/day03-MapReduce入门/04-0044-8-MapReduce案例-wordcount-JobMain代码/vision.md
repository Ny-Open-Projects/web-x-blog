# 画面线理解：8-MapReduce案例-wordcount-JobMain代码

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\8-MapReduce案例-wordcount-JobMain代码【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:15, 03:21, 05:28, 07:59, 10:39, 11:54, 13:39, 14:48, 16:11, 17:27, 18:25, 19:12, 19:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:52:30

1) 这一组画面整体在讲如何使用 Java 编写一个完整的 MapReduce 程序，包括 Mapper、Reducer、JobMain 的实现以及配置过程。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示 MapReduce 的整体结构，包括 Mapper、Shuffle、Reducer 阶段，并列出 WordCount 的步骤。同时展示上传文件到 HDFS 的命令：hdfs dfs -mkdir /wordcount/ 和 hdfs dfs -put wordcount.txt /wordcount/。

画面 2:
要点：展示 JobMain 类的初始结构，包含 main 方法和 run 方法的框架。

画面 3:
要点：展示 ToolRunner 类的 run 方法源码，用于启动 MapReduce 任务。

画面 4:
要点：在 JobMain 类中，使用 ToolRunner.run 方法启动任务，并创建 Job 实例。

画面 5:
要点：在 JobMain 类中，设置 Job 的配置，包括设置 Job ID、优先级等。

画面 6:
要点：在 JobMain 类中，设置 Mapper 类和 InputFormat 类。

画面 7:
要点：在 JobMain 类中，设置 Mapper 类、输出 Key 类和输出 Value 类。

画面 8:
要点：展示 MapReduce 的流程图，包括 Map 阶段、Shuffle 阶段和 Reduce 阶段，以及各阶段的输入输出数据格式。

画面 9:
要点：在 JobMain 类中，设置 Reducer 类、输出 Key 类和输出 Value 类。

画面 10:
要点：在 JobMain 类中，设置 OutputFormat 类。

画面 11:
要点：在 JobMain 类中，设置 InputFormat 类和输入路径。

画面 12:
要点：在 JobMain 类中，设置 OutputFormat 类和输出路径，并调用 waitForCompletion 方法等待任务完成。

画面 13:
要点：展示 MapReduce 的流程图，包括 Map 阶段、Reduce 阶段和 TextOutputFormat 输出到文件。

画面 14:
要点：在 JobMain 类中，设置 Reducer 类、输出 Key 类和输出 Value 类，以及 OutputFormat 类。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
hdfs dfs -mkdir /wordcount/
hdfs dfs -put wordcount.txt /wordcount/

画面 2:
package cn.itcast.mapreduce;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.util.Tool;
public class JobMain extends Configured implements Tool {
    public static void main(String[] args) {
    }
    @Override
    public int run(String[] strings) throws Exception {
        return 0;
    }
}

画面 3:
Decomplied class file, bytecode version 2.0 (Java 8)
@Public
@Stable
public class ToolRunner {
    public ToolRunner() {
    }
    public static int run(Configuration conf, Tool tool, String[] args) throws Exception {
        if (CallerContext.getCurrent() == null) {
            CallerContext ctx = (new Builder("CLI")).build();
            CallerContext.setCurrent(ctx);
        }
        if (conf == null) {
            conf = new Configuration();
        }
        GenericOptionsParser parser = new GenericOptionsParser(conf, args);
        tool.setConf(conf);
        String[] toolArgs = parser.getRemainingArgs();
    }
}

画面 4:
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.util.Tool;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 5:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        job.setJobName("mapreduce_wordcount");
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 6:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        job.setInputFormatClass(TextInputFormat.class);
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 7:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        job.setInputFormatClass(TextInputFormat.class);
        job.setInputPath(new Path("hdfs://node01:8020/wordcount"));
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 8:
Map阶段
K1 V1
0 hello.world
11 hello.hadoop
23 world.hdfs
33 hadoop.java
自动完成
1:自定义一个Mapper类，重写map方法
2:在Map方法中将K1和V1转为K2和V2
world
hello
hadoop
hdfs
hello
world
hadoop
hdfs
hello
world
hadoop
hdfs
Reduce阶段
新 K2 V2
hello <1,1>
world <1,1>
hadoop <1,1>
hdfs <1,1>
自动完成
1:自定义Reducer类
重写reduce方法
2:在reduce方法中要将新的k2和v2转为k3和v3

画面 9:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        job.setInputFormatClass(TextInputFormat.class);
        job.setInputPath(new Path("hdfs://node01:8020/wordcount"));
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        job.setReducerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 10:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] strings) throws Exception {
        Job job = Job.getInstance(super.getConf(), "mapreduce_wordcount");
        job.setInputFormatClass(TextInputFormat.class);
        job.setInputPath(new Path("hdfs://node01:8020/wordcount"));
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        job.setReducerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        return 0;
    }
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}

画面 11:
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.map
