# 画面线理解：6.5 项目实时计算主程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.5 项目实时计算主程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:44, 03:22, 04:49, 06:32, 08:25, 10:08, 11:28, 13:12, 14:39, 16:04, 17:50, 19:37, 20:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:32:11

1) 这一组画面整体在讲什么（一句话）：
编写一个基于 Flink 的 Kafka 数据流处理程序，实现从 Kafka 消费数据、进行转换计算、再写入另一个 Kafka 主题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IDEA 中右键点击项目目录，选择“Build Module 'cold-flink'”进行模块构建。
画面 2: 编辑器中显示 StreamingJob 类的开头，包含注释“//设置环境信息”、“//设置检查点”、“//设置流计算”、“//设置输出”。
画面 3: 在代码中调用 env.getCheckpointConfig()，弹出方法提示框，显示可设置的检查点相关方法。
画面 4: 设置检查点模式为 DEFAULT_MODE，并设置重启策略为 fixedDelayRestart，参数为 restartAttempts=4 和 delayBetweenAttempts=1000。
画面 5: 在代码中调用 Properties 类的 setProperty 方法，弹出方法提示框，显示可设置的属性。
画面 6: 设置 Kafka 的连接属性，包括 bootstrap_servers、group_id 和 auto.offset.reset。
画面 7: 创建 FlinkKafkaConsumer 实例，用于从 Kafka 消费数据。
画面 8: 在代码中调用 DataStream.addSource 方法，弹出方法提示框，显示可设置的源。
画面 9: 设置并行度，调用 map 方法进行数据转换，将字符串解析为 MessageEntity 对象。
画面 10: 设置并行度，调用 map 方法进行数据转换，将字符串解析为 MessageEntity 对象。
画面 11: 调用 addSink 方法，准备将处理后的数据写入 Kafka。
画面 12: 创建 FlinkKafkaProducer 实例，用于将数据写入 Kafka。
画面 13: 定义 map 函数，用于将 MessageEntity 对象转换为字符串。
画面 14: 代码完整显示，包含设置环境、检查点、Kafka 消费者、数据转换、Kafka 生产者等部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
无

画面 2:
package com.thema.cold.flink;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        //设置检查点
        //设置流计算
        //设置输出
    }
}

画面 3:
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
public class StreamingJob {
    public static void main(String[] args) {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 4:
import org.apache.flink.streaming.api.environment.CheckpointConfig;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
public class StreamingJob {
    public static void main(String[] args) {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 5:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置流计算
        //设置输出
    }
}

画面 6:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
    }
}

画面 7:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        //设置输出
    }
}

画面 8:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        DataStream<MessageEntity> stream = env.addSource(consumer)
            .setParallelism(1)
            .map(string -> JSON.parseObject(string, MessageEntity.class));
        //设置输出
    }
}

画面 9:
import java.util.Properties;
public class StreamingJob {
    public static void main(String[] args) {
        //设置环境信息
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //设置检查点
        env.enableCheckpointing(5000);
        //设置检查点
        env.getCheckpointConfig().setCheckpointingMode(CheckpointConfig.DEFAULT_MODE);
        //设置重启策略
        env.getCheckpointConfig().setRestartStrategy(RestartStrategies.fixedDelayRestart(4, 1000));
        //设置Kafka列属性
        Properties properties = new Properties();
        properties.setProperty("bootstrap.servers", "172.17.0.143:9092");
        properties.setProperty("group.id", "coldlink");
        properties.setProperty("auto.offset.reset", "earliest");
        //设置Kafka列的消费者，接收Kafka发来的数据
        FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<String>(kafla_topic, new SimpleStringSchema(), properties);
        consumer.setStartFromEarliest();
        //设置流计算
        DataStream<MessageEntity> stream = env.addSource(consumer)
            .setParallelism(1)
            .map(string -> JSON.parseObject(string, MessageEntity.class));
        //设置输出
        DataStream<MessageEntity> outStream = stream.map(new MessageAggregate());
        //写入Kafka
        outStream.addSink(new SinkToSQL());
    }
}

画面 10:
import java.util.Properties;
public class StreamingJob {
