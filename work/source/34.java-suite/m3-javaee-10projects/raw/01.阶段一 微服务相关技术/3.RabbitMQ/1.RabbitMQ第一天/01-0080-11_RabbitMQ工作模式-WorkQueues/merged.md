# 11_RabbitMQ工作模式-WorkQueues

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\11_RabbitMQ工作模式-WorkQueues_【海量资源尽在 ubkz.com】.mp4
- 时长 7分30秒（音频 451s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 介绍完RabbitMQ的快速入门程序我们对RabbitMQ的一个基本的代码编写有大概的一个印象了那么接下来呢我们就来介绍RabbitMQ的工作模式其实呢对于工作模式我们在官网上刚才也看到了对应的工作模式你注意看我们最简单的刚才写的Hallowood它是不是一个生产者对应一个消费者呀
[00:23] 那么不同的工作模式其实指的就是它一个消息的一个路由的策略和方式不太一样这个地方你看一个生产者是不是可以对两个或者多个消费者那么这个地方呢还有加了路由的一个机制其实呢所谓的工作模式啊我们其实呢就指的是消息路由的分发的一种方式而已那么我们第一种简单的Hello World就不再去讲了我们从Work Cues工作对立开始讲起
[00:53] 那么下来呢我们一个一个来学这其他的四种工作模式那么首先我们来说第一个work queues工作对立的模式那么我们可以来看一下模式的一个图啊一个生产者发了一条消息之后发了对立里边注意看啊这个对立是不是对应着两个消费者呀
[01:16] 那么注意啊这个地方一定不要混淆这两个消费者从这个队列里边去取消息他们两个是处于的是一个竞争的关系换句话说他们两个只有一个人能取到这条消息OK吧那么这种模式有什么用呢你注意看啊有什么用呢其实呢对于一些任务过重或任务较多的情况工作队列可以提高任务处理的速度比如说
[01:46] 我们这边很多人往队列里边发消息比如说一秒钟呢我可以发上1000条消息但是呢CE它只能处理500个消息那么这个CE只能处理500个那我再找个队友CR也能处理500个他们两个一起处理理论上是不是就可以处理1000条消息了OK吧大概就是这么一个意思那么这种方式呢它的代码跟我们刚才写的代码基本上是一样的
[02:16] 只是说再复制一份监听一个队列就可以了我们可以来编写一下代码来说一下我们在这个地方呢先来写这个producer那我们复制一份这个代码叫做workworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkworkwork
[02:47] 好贴过来放这个地方好那么接下来呢我们把这个代码改造一下当然这个地方呢不叫Hello World了我们改它名叫做WorkersWorkers可以有UES好那么接下来呢再来再来呢我们这个消息呢其实呢我们就不换了OK吧那么我们这个发送消息的这个对列名称呢我们叫Workers没问题吧但是呢注意啊
[03:16] 因为发一条消息当然看不出来这个效果了对吧所以呢我们在这里边呢多发几条消息啊我们for i循环一下发上个10条消息吧我们从1开始啊i小于等于10然后呢每个消息呢前边我们加上一个i这个非常简单啊好然后呢我们把这两行代码呢给它放到对应的放到for循环里边去那么发消息的时候呢你看这个消息是不是每个前边都带着数字编号1
[03:45] 到时我们一次呢发了10条这样的消息那么发完了10条消息之后那么在消费者这一段注意看我们的消费者呢也给他改造一下consumer复制一份那么这个地方叫做consumer叫做walkerqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
[04:14] 那么同理啊刚才那个对立的名称呢就不能再叫Hello World了我们把Hello World都过来关掉然后呢这个叫做WorkCuse这么一个对立的名称好复制过来然后呢接下来我们在这个里边呢我们叫做WorkCuse没问题吧好消费的时候叫WorkCuse那么这样呢其实就就OK了没有什么太大的区别啊但是呢在这里边为了看的更方便一些我们把这些呢
[04:43] 其他的信息都注释掉我们只留下Ball Day的信息来看对应的数字编号这样可能看的更清晰一些好第一个呢我们就弄完了弄完了之后呢我们Ctrl C复制一份WorkCuse2好这个代码是不用改的一模一样的两个代码是一模一样的就是说我们要启动两个这么一个消费者从同一个堆垒里边去争抢这个消息
[05:09] 其实呢这两个是一个顺序消费的关系就是C1取一条然后C2取一条它们是很和谐的我们可以来尝试一下现在我还没有去生产消息的那换句话说呢在我的对列里边其实并没有一个workcuse名字的对列没有吧OK吧那么现在呢我们就可以来分别启动这两个消费者好启动第一个cuse1好启动了
[05:39] 然后接下来我们再启动第二个两个都起起来你注意啊这个方法是不是并没有执行因为还没有监听的消息嘛好这两个都执行了之后呢我们可以来看一下这个队列是不是就创建出来了就两个consumer没问题吧那么接下来呢我们就一次来生产这么十条消息好把这个呢也执行一下run一下执行一下之后呢你注意看这个效果好执行完了执行完了之后呢我们clear一下clear一下来看这边
[06:09] 你注意看24680consumer2是不是消费的是24680那你猜1消费啥那肯定是13579了对吧所以呢这就是我们所说的工作对列的方式你可以看一下好这边没问题吧那么工作对列呢就是说我有10条消息他消费13579他消费24680他们两个人把这个压力就分担了OK
[06:37] 工作对立基本上的一个代码的编写我们也就说完了那么最后呢我们来做一个小节工作对立与简单的这个代码是一样的那么他们多个消费者之间对于同一个消息的关系是一个竞争的关系这个一定要搞清楚不是说C1和C2都分别能消费同一个消息他们只能有一个消费好那么work queues呢是对于任务比较重的时候
[07:06] 那么我们可以来提高任务处理的速度比如说发短信短信服务呢肯定要部署多个将来那么肯定只有一个服务能把这个短信发出去要不是如果每一个CECR都发短信那那个人是不是就失了很多条短信了这样呢也是一种资源的浪费啊好嘞那么简单的我们就说了一下这个工作对列的这么一种方式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RabbitMQ 的工作模式，重点演示了 Work queues（工作队列）模式的生产者与消费者代码实现及 RabbitMQ 管理界面的队列状态。

2) 按时间顺序列出每张画面的要点：
画面 1: RabbitMQ 管理界面，显示已存在一个名为 "hello_world" 的队列，状态为 Idle。
画面 2: PPT 目录页，当前章节为 "RabbitMQ 的工作模式"。
画面 3: IntelliJ IDEA 编辑器，显示生产者代码文件 Producer_WorkQueues.java，注释为 "//1.创建消息工厂"。
画面 4: PPT 页，标题为 "4.1 Work queues 工作队列模式"，图示 P -> 队列 -> C1, C2，并附有模式说明。
画面 5: IntelliJ IDEA 编辑器，显示生产者代码中 for 循环部分，用于发送 10 条消息。
画面 6: IntelliJ IDEA 编辑器，显示消费者代码文件 Consumer_WorkQueues.java，其中设置了连接工厂的主机、端口、虚拟主机、用户名和密码。
画面 7: IntelliJ IDEA 编辑器，显示消费者代码中调用 channel.queueDeclare 方法创建队列 "hello_world"。
画面 8: IntelliJ IDEA 编辑器，显示消费者代码中定义了 handleDelivery 方法用于处理消息，并调用 channel.basicConsume。
画面 9: IntelliJ IDEA 编辑器，显示消费者代码中创建了 DefaultConsumer 实例并传入 handleDelivery 方法。
画面 10: RabbitMQ 管理界面，显示了多个窗口的截图，包括管理界面、IDE、PPT 等。
画面 11: RabbitMQ 管理界面，显示已存在两个队列："hello_world" 和 "work_queues"，状态均为 Idle。
画面 12: IntelliJ IDEA 编辑器，显示生产者代码中发送消息的 body 为 "hello RabbitMQ---"，并提示 SLF4J 日志绑定失败。
画面 13: IntelliJ IDEA 编辑器，显示终端输出了 10 条消息，内容为 "body: hello RabbitMQ---"。
画面 14: PPT 页，标题为 "4.2 Pub/Sub 订阅模式"。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 3 代码：
```java
package com.ithema.producer;
import ...
public class Producer_WorkQueues {
    public static void main(String[] args) throws IOException, TimeoutException {
        //1.创建消息工厂
    }
}
```

画面 5 代码：
```java
for (int i = 1; i <= 10; i++) {
    String body = i + "hello RabbitMQ---";
    channel.basicPublish("work_queues", null, body.getBytes());
}
```

画面 6 代码：
```java
ConnectionFactory factory = new ConnectionFactory();
factory.setHost("172.16.08.133"); //ip
factory.setPort(5672); //端口
factory.setVirtualHost("/"); //虚拟主机
factory.setUsername("itheima"); //用户名
factory.setPassword("itheima"); //密码
Connection connection = factory.newConnection();
Channel channel = connection.createChannel();
```

画面 7 代码：
```java
channel.queueDeclare("hello_world", true, false, false, null);
```

画面 8 代码：
```java
public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
    System.out.println("ConsumerTag: " + consumerTag);
    System.out.println("Exchange: " + envelope.getExchange());
    System.out.println("RoutingKey: " + envelope.getRoutingKey());
    System.out.println("Properties: " + properties);
    System.out.println("Body: " + new String(body));
}
```

画面 9 代码：
```java
Consumer consumer = new DefaultConsumer(channel) {
    @Override
    public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) {
        // 处理消息的逻辑
    }
};
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2 PPT 标题：
- 目录
- MQ 的基本概念
- RabbitMQ 的安装和配置
- RabbitMQ 快速入门
- RabbitMQ 的工作模式（当前选中）
- Spring 整合 RabbitMQ

画面 4 PPT 标题：
- 4. RabbitMQ 的工作模式
- 4.1 Work queues 工作队列模式
- 模式说明：
  - Work Queues: 与入门程序的简单模式相比，多了一个或一些消费者，多个消费者共同消费同一个队列中的消息。
  - 应用场景: 对于任务过重或任务较多的情况，使用工作队列可以提高任务处理的速度。

画面 14 PPT 标题：
- 4. RabbitMQ 的工作模式
- 4.2 Pub/Sub 订阅模式

5) 无。

