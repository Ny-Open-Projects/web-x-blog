# 画面线理解：6.8 部署flink工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.8 部署flink工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:38, 00:48, 00:51, 00:53, 00:56, 01:06, 02:35, 02:47, 02:55, 02:58, 03:01, 03:16, 03:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:34:05

1) 这一组画面整体在讲如何通过 IntelliJ IDEA 编写并提交一个 Flink 流处理作业，然后在 Flink Web Dashboard 上监控其运行状态，并展示一个配套的监控系统界面。

2) 按时间顺序列出每张画面的要点：
画面1：Flink Web Dashboard 主页，显示集群状态（4个Task Managers，8个Task Slots，7个可用Task Slots）和作业列表（已完成作业）。
画面2：点击导航栏中的“Submit new Job”选项，进入提交新作业页面。
画面3：在 IntelliJ IDEA 中打开 StreamingJob.java 文件，代码中定义了从 Kafka 消费数据、转换、写入 MySQL 的 Flink 流处理逻辑。
画面4：在 IntelliJ IDEA 中点击“install”按钮，准备将项目打包。
画面5：在 Flink Dashboard 的“Submit new Job”页面，弹出文件选择对话框，准备选择作业 JAR 文件。
画面6：在文件选择对话框中，导航至项目 target 目录，选择“cold-link-1.0.0.jar”文件。
画面7：将选中的 JAR 文件上传至 Flink Dashboard 的“Submit new Job”页面。
画面8：作业提交成功后，进入作业的“Timeline”页面，显示作业的执行流程图（Source -> Map -> Sink）和时间轴。
画面9：在 Flink Dashboard 的“Running Jobs”页面，显示作业正在运行。
画面10：切换到一个名为“冰眼”的监控系统界面，显示报警记录表格。
画面11：在“冰眼”系统中点击“实时报警”菜单项。
画面12：在“冰眼”系统中“实时报警”页面显示实时报警数据。
画面13：在“冰眼”系统中“实时报警”页面，鼠标悬停在“实时报警”菜单项上。
画面14：返回 Flink Dashboard 的“Running Jobs”页面，作业仍在运行。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面3代码：
```java
//Kafka队列consumer，接收patty发过来的数据
FlinkKafkaConsumer<String> consumer = new FlinkKafkaConsumer<>(kafka_topic, new SimpleStringSchema(), properties);
consumer.setStartFromLatest();
//设置数据源，kafka队列
DataStream<MessageEntity> stream = env.addSource(consumer)
        .map(string -> JSON.parseObject(string, MessageEntity.class))
        .map(string -> JSON.parseObject(string, MessageEntity.class))
        .map(string -> JSON.parseObject(string, MessageEntity.class));
//从redis中获取报警信息，并合并消息中
DataStream<MessageEntity> outStream = stream.map(new MessageAggregate());
//存储设备报警信息
outStream.addSink(new SinkToMySQL());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8：作业执行流程图：
Source (Custom Source) -> Map -> Sink (Sink)
表格数据：
| 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 | 21:40:47 |

画面10表格数据：
| 企业名称 | 仪表编号 | 管理主机号 | 仪表名称 | 采集日期 | 温度 | 温度阈值 | 湿度 | 湿度阈值 | 温度报警 | 湿度报警 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cccc | M201002001 | H100220002 | M201002001 | 20191204133340 | 36℃ | 10 / 46 | 20 | 36 / 75 | 低温报警 | 低温报警 |
| cccc | M402003001 | H209214531 | M402003001 | 20191204133340 | 55℃ | 20 / 10 | 84 | 40 / 70 | 低温报警 | 高温报警 |

画面12表格数据：
| 仪表编号 | 仪表名称 | 管理主机号 | 企业名称 | 采集日期 | 温度 | 温度阈值 | 湿度 | 湿度阈值 | 温度报警 | 湿度报警 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M402001002 | M402001002 | H200230001 | 胡同二号 | 好方运输 | 20191204134140 | 57℃ | 15 / 25 | 52% | 低温报警 | 低温报警 |
| M402003001 | M402003001 | H209214531 | 胡同三号 | 好方运输 | 20191204134150 | -16℃ | 20 / 10 | 35% | 正常 | 低温报警 |

5) 不要评价画面美观，不要输出与课程无关的内容。
