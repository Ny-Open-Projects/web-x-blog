# 28.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\28.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 4分32秒（音频 272s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一个总结那么首先我们要说明的一点是在我们讲课程介绍的时候呢后面有两个内容一个呢是错误消息的从事另外一个呢就集群的一个搭建那么这两个内容呢我们把它放到下面下一天的课程中去做一个讲解那我们来看一下今天我们学了哪些内容那么今天我们一天呢其实就是围绕着log.mq去做一个学习那么我们首先学了他的一些这个对他做了一些了解啊简介以及他的一些安装
[00:29] 那么安装包括非Dock的安装以及Dock的一个安装OK那么我们在安装完成之后我们对它做了一个快速的入门那么学习了一下它的一些基础的一些API的一些使用包括它的创建topic然后发送消息那么发送消息又分同步和异步的一个发送那么然后后面我们是不是学习了它的一个消费者这样的一个代码的一个编写
[00:55] 那么在我们消费者编写的时候在这个位置我们是不是重点讲他的一个订阅的方式你可以通过订阅一个新或者是通过一个tag是不是做一个筛选那么后面我们是不是又讲了消费者的一个消息的过滤器那么这个过滤器是不是非常类似于我们的编写的circle语句中的这样的一些写法那么就是这样的一种写法
[01:17] 那么但是呢要注意的是那么要想去这么去玩你必须要给他开启一个什么呢自定义啊属性这种方式要在我们的blog的配置文件中做这样的开启要不然的话啊是不可以做一个筛选的ok那么下面呢我们对我们的生产者做了一些这个详解包括我们讲他的顺序消息对吧以及他这个顺序消息的原理
[01:40] OK那么下面呢我们也讲了他的一些分布式的一个事物的消息这个呢是我们今天课程的一个重点的内容希望大家呢好好的理解然后呢去动手去敲一下去理解一下他是怎么去实现我们的分布式事物的啊OK好然后呢我们在下面呢对我们的consumer呢做了一个讲解OK那么讲了他的两种模式一种是推一种是拉这两种模式但是他的底层的实现是不是都是这个拉曲的方式
[02:08] OK那么在这个里面呢我又引出了一个引出了一个解决方案吧叫什么叫做长轮旬长轮旬的一个解决方案就是长连接加轮旬的方式叫做长轮旬这种方式OK好那么在后面呢我们是不是又去讲了他的消费者消息消费这个消息的模式就是一种是集群模式一种是广播模式
[02:33] 然后后面我们又去讲了一个重复消息的解决方案这个在我们做项目的时候你一定会遇到这个问题那么这是不是我们在这个里面其实讲了很重要一点就是我们要保证我们的消费者这一端的一个应用逻辑的一个密等性密等性OK好那么最后我们去介绍了一下LogMQ的一些存储的
[02:57] 一些它的一些底层存储的一些这个技术点那包括它采用的是零拷贝的技术然后呢文件系统啊采用的是这个Linux上面的ext4啊这样的一个文件系统做一个存储那么它底层的一个存储结构呢是有两个文件一个是commit log一个是consumer的一个
[03:18] Q这样这两个做一个配合完成那么consumerQ呢是做一个存储我们的那个索引那么comiclog呢这个里面存储的是我们真正的数据OK那么我们来看一下他的一个这个图啊在这个图里面是不是也是去说明前面我们所说这个内容啊OK好然后呢我们是不是又去查看了一下他的一个具体的一个这个文件的一些目录的结构
[03:46] OK好然后最后我们其实去给大家介绍了一下它的一个刷盘的方式有同步刷盘和异步刷盘这两种方式那么如何选择我们也给大家讲过了对吧那么要根据它的一个特点或者说它的优缺点去做出一个选择要结合我们的业务做选择OK那么这个就是我们今天的内容今天的一天我们都是在围绕着这个消息而来做一个展开的希望大家能够去
[04:13] 动手去写一些代码然后去理解一些它的一些内容那么这样的话我们才能够对log.mq有一个比较全面的一个学习和一个认知ok好那么这个就是我们今天的所有课的一些内容ok那么今天课程我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.RocketMQ.client.consumer.listener.MessageListenerConcurrently;
import org.apache.RocketMQ.client.exception.MQClientException;
import org.apache.RocketMQ.common.message.MessageExt;
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
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.RocketMQ.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.RocketMQ.client.consumer.listener.MessageListenerConcurrently;
import org.apache.RocketMQ.client.exception.MQClientException;
import org.apache.RocketMQ.common.message.MessageExt;
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
package cn.itcast.RocketMQ.order;
import org.apache.RocketMQ.client.producer.DefaultMQProducer;
import org.apache.RocketMQ.client.producer.SendResult;
import org.apache.RocketMQ.common.message.Message;
import org.apache.RocketMQ.remoting.common.RemotingHelper;
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

