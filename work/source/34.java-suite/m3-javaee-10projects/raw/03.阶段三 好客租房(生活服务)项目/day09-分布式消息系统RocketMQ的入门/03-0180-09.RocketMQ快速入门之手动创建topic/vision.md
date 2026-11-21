# 画面线理解：09.RocketMQ快速入门之手动创建topic

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\09.RocketMQ快速入门之手动创建topic【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:07, 01:16, 01:35, 02:11, 02:36, 02:58, 03:41, 04:01, 05:13, 05:25, 05:51, 06:09, 06:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:59:39

1) 这一组画面整体在讲如何使用 RocketMQ Java 客户端创建一个 Topic。

2) 按时间顺序列出每张画面的要点：
画面1：展示 RocketMQ 的架构图，包含 producer、nameserver、broker 集群、consumer，以及 broker 内部的 topic 和 message queue。
画面2：IDEA 项目结构，显示项目名为 itcast-rocketmq，包含 src、test、resources、pom.xml 等目录。
画面3：IDEA 项目结构，选中了 topic 包下的 TopicDemo.java 文件。
画面4：显示 TopicDemo.java 文件的开头部分，包含 package 声明和 main 方法。
画面5：在 main 方法中导入 org.apache.rocketmq.client.producer.DefaultMQProducer。
画面6：在 main 方法中创建 DefaultMQProducer 实例，并设置 nameserver 地址。
画面7：在 main 方法中设置 nameserver 地址为 "172.16.55.185:9876"。
画面8：在 main 方法中调用 producer.createTopic 方法，但尚未完成。
画面9：终端中显示 RocketMQ 的安装目录和配置文件目录。
画面10：在 main 方法中添加注释说明 createTopic 方法的参数。
画面11：在 main 方法中调用 producer.createTopic 方法，参数为 broker 名称、topic 名称和 queue 数量。
画面12：在 main 方法中添加 System.out.println 语句用于打印创建成功信息。
画面13：在 main 方法中添加 producer.shutdown() 语句用于关闭生产者。
画面14：显示 RocketMQ 控制台界面，列出已创建的 topic，包括 my-topic。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
import org.apache.rocketmq.client.producer.DefaultMQProducer;

画面6：
DefaultMQProducer producer = new DefaultMQProducer (producerGroup: "haoke");

画面7：
producer.setNamesrvAddr("172.16.55.185:9876");

画面10：
/**
 * 创建topic, 参数分别是: broker的名称, topic的名称, queue的数量
 */

画面11：
producer.createTopic (key: "broker_haoke_im", newTopic: "my-topic", queueNum: 8);

画面12：
System.out.println("topic创建成功!");

画面13：
producer.shutdown();

画面14：
package cn.itcast.rocketmq;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.MQProducer;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，producer 指向 broker 集群，broker 集群指向 nameserver，consumer 指向 broker，broker 指向 topic，topic 指向 Message queue。
画面14：PPT 标题为“2. 快速入门”，子标题为“2.1、创建topic”，并显示了代码示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
