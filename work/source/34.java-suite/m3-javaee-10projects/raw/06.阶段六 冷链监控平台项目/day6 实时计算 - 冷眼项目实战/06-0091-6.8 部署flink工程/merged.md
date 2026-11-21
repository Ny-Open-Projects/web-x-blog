# 6.8 部署flink工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.8 部署flink工程_【海量资源尽在 666java.com】.mp4
- 时长 3分29秒（音频 209s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来部署一下我们的codeflink这个工程我们要把codeflink工程生成的这个jar 包部署到我们的这个Flink机讯里边那首先我们要生成jar 包在我们的mainway里边用install我们的这个jar 包一种方式是我们通过后台提交jar 包的方式来提交整个Flink的工程那还有一种方式是我们在我们的Flink的一个dashboard就是它的面板上可以提交
[00:30] 那么我们本地安装的集群里边有一个这种管理端啊管理外部的页面这个管理外部页面里边就是有一个这种submit new job的这样的一个按钮一个菜单那么在这儿我们看一下啊在这个里边我们可以提交我们的整个的这个甲包啊ok那我们现在已经呃呃编译生成完了那我选择我点点这个add new然后呢我选择我的mayway
[01:00] 呃生成的这个叫什么呢生成的这个codeflink这个jar 包的路径啊选择一下选中之后呢我们在页面上会看到一个upload按钮我点击upload按钮它会把我们整个的这个jar 包上传到服务器集群里边去然后现在上传了啊百分之七十多八十多OK现在已经上传完了那上传完了之后呢我们会看到啊在这儿我们选中选中这一条
[01:31] codeflink-1.0.0.j这个包那么它的intricast也就是说是主函数实际上就是我们的streaming job我选中点一下这个主函数那么我们在这儿我们就能看到我们的这个streaming的一个我们的Flink的一个价包的主函数那么我们点这个submit也就是说让它来执行OK此时我们就能够看到我们的running的job就是
[02:05] 当前执行的job就是这么一个job了而这个job里边这个页面里边我们大概分成这么几部分吧一部分来讲是overview的话我们看到一个页面的一个视图这里边的话我们会看到从我们的source到mapping到mapping然后到最终把这个数据sync到我们的有一个路sync到我们的mycircle里边以及sync到我们的kabaca里边这个地方它的并行度实际上是1
[02:35] 我们timeline里边其实也能看到我们整个的它的一个过程一个schedule的一个过程那exception的话现在还是没有异常当前的我们再看它是一个running的一个状态对吧我们在这儿的话是一样task的话多多一个然后running的一个状态那么我们到我们的页面里边我们页面里边我们看到我们的数据OK现在数据其实已经有了
[03:04] 这数据就是从我们的Flink数据拿到的Flink执行计算之后把数据存储到我们的服务器里边数据库里边然后存储到数据库的时候我们在实时报警的时候就查清数据库里边查清到的一个结果这个就是我们把我们的Flink的工程Flink的jar 包然后上传到我们Flink机器里边执行的这样的一个过程

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
//设置数据源，Kafka队列
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

