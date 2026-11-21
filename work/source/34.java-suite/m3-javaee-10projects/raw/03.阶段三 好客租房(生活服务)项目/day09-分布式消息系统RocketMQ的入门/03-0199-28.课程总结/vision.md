# 画面线理解：28.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\28.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 00:31, 00:41, 00:51, 01:09, 01:14, 01:33, 01:41, 01:57, 02:54, 03:32, 03:38, 03:47, 04:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:10:52

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了RocketMQ的消息中间件，涵盖其简介、安装、核心概念、生产者与消费者模式、消息存储机制（CommitLog、ConsumeQueue）以及同步/异步刷盘等关键技术点。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1（第1张）：课程介绍页，列出学习目标：了解RocketMQ概念、核心概念、安装与使用、producer/consumer详解、特性。
画面2（第2张）：展示RocketMQ发展历史时间轴，从2007年Notify到2016年Apache孵化，标注了各阶段产品及特性。
画面3（第3张）：展示Java代码，创建Topic，设置Broker地址并创建主题。
画面4（第4张）：展示ConsumerDemo类的导入语句和类结构，准备消费消息。
画面5（第5张）：展示SynProducerFilter类代码，发送带属性的消息。
画面6（第6张）：展示ConsumerFilterDemo类代码，订阅指定条件的消息。
画面7（第7张）：说明需要在broker配置文件中添加enablePropertyFilter=true以支持属性过滤。
画面8（第8张）：展示OrderProducer类代码，模拟订单消息发送。
画面9（第9张）：讲解push和pull两种消费模式的区别及长轮询机制。
画面10（第10张）：介绍RocketMQ存储技术，采用mmap + write方式，文件系统为Linux Ext4。
画面11（第11张）：展示消息存储架构图，Producer发送消息到CommitLog，Consumer通过ConsumeQueue读取。
画面12（第12张）：展示CommitLog结构，包含8字节偏移量、4字节大小、8字节消息标签哈希码。
画面13（第13张）：介绍同步刷盘与异步刷盘，同步刷盘消息写入磁盘后返回成功，异步刷盘写入内存后返回成功。
画面14（第14张）：展示同步刷盘与异步刷盘的对比图，同步刷盘写入磁盘，异步刷盘写入内存。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
public class TopicDemo {
    public static void main(String[] args) throws MQClientException {
        DefaultMQProducer producer = new DefaultMQProducer("HAOKE_IM");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        // 
        // 
        producer.createTopic("broker_haoke_im", "haoke_im_topic", 8);
        System.out.println("创建topic成功");
    }
}
```

画面5：
```java
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;
import java.io.UnsupportedEncodingException;
import java.util.List;
import java.util.List;
public class SynProducerFilter {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer("HAOKE_IM");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        String msgStr = "美女001";
        Message msg = new Message("haoke_menin_topic", "SEND_MSG",
                msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
        msg.putUserProperty("age", "18");
        msg.putUserProperty("sex", "女");
        // 发送消息
        SendResult sendResult = producer.send(msg);
        System.out.println("消息状态：" + sendResult.getSendStatus());
        System.out.println("消息id：" + sendResult.getMessageId());
    }
}
```

画面6：
```java
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.message.MessageExt;
import java.io.UnsupportedEncodingException;
import java.util.List;
public class ConsumerFilterDemo {
    public static void main(String[] args) throws Exception {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer("HAOKE_IM");
        consumer.setNamesrvAddr("172.16.55.185:9876");
        // 订阅topic，接收此Topic下的所有消息
        consumer.subscribe("haoke_menin_topic", MessageSelector.bySql("age=20 AND sex='女'"));
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            @Override
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> msgs,
                    ConsumeConcurrentlyContext context) {
                for (MessageExt msg : msgs) {
                    try {
                        System.out.println(new String(msg.getBody(), "UTF-8"));
                    } catch (UnsupportedEncodingException e) {
                    }
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            }
        });
        consumer.start();
    }
}
```

画面7：
```properties
#加入到broker的配置文件中
enablePropertyFilter=true
```

画面8：
```java
package cn.itcast.rocketmq.order;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.common.RemotingHelper;
public class OrderProducer {
    public static void main(String[] args) throws Exception {
        DefaultMQProducer producer = new DefaultMQProducer("HAOKE_ORDER_PRODUCER");
        producer.setNamesrvAddr("172.16.55.185:9876");
        producer.start();
        for (int i = 0; i < 100; i++) {
            String msgStr = "order" + i;
            int orderid = i % 10; // 模拟生成订单id
            Message message = new Message("haoke_order_topic", "ORDER_MSG",
                    msgStr.getBytes(RemotingHelper.DEFAULT_CHARSET));
            producer.send(message);
        }
        producer.shutdown();
    }
}
```

画面13：
```text
• 同步刷盘
    • 具体流程是：消息写入内存的PAGECACHE后，立刻通知刷盘线程刷盘，然后刷盘线程执行完成后顺带等待的线程，返回消息与成功的状态。
• 异步刷盘
    • 在返回写成功状态时，消息可能只被写入了内存的PAGECACHE，写操作的返回快，吞吐量大。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：时间轴图，从左到右依次为：2007（Notify）、2010（Napoli）、2011（ActiveMQ内核）、2012（MetaQ v1.0）、2015（Alivware MQ v1.0）、2016（Apache RocketMQ）。
画面11：架构图，Producer指向CommitLog，CommitLog指向多个ConsumeQueue，每个ConsumeQueue指向Consumer1和Consumer2。
画面12：CommitLog结构图，包含三个部分：CommitLog Offset（8字节）、Size（4字节）、Message Tag Hashcode（8字节）。
画面14：对比图，左侧为异步刷盘，Producer写入JAVA HEAP，再写入MEMORY；右侧为同步刷盘，Producer写入JAVA HEAP，再写入MEMORY，最后写入磁盘。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
