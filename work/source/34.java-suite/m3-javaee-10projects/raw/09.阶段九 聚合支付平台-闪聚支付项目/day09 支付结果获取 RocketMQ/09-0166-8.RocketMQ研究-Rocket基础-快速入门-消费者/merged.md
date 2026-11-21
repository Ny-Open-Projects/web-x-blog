# 8.RocketMQ研究-Rocket基础-快速入门-消费者

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\8.RocketMQ研究-Rocket基础-快速入门-消费者【海量资源尽在 666java.com】.mp4
- 时长 6分11秒（音频 372s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么生产者发消息的功能我们完成之后呢接下来我们就可以来做消费者对吧那消费者其实和我们生产者的工程还是稍微有些差别的那么生产者工程大家你也看到了我们建一个bin然后调用模板然后发就可以了但消费者你也知道他要干嘛他要监听了
[00:22] 对吧他要监听了好那么监听仍然我们还是要把他这个监听的类给他创建出来然后进入到消费者的工程中然后我们仍然是在这创建一个包好然后在这里头呢我们肯定要把这个监听的类创建好那么有人说老师监听那咋监听呢首先这个监听的类他一定是个bin对吧你得用component给他标一下然后其次他要监听
[00:49] 那么他就会用一个叫RocketMQ message怎么样那么他要监听你看这里头有什么呀你看topic对吧还有一个东西我们这两个东西都得写啊一个是我们说的topictopic他监听哪个呢各位这个主题是不是叫my topic对他就监听这个分类my topic懂吧然后呢消费者也要建一个组
[01:15] 对消费者也要建一个组原来我们生产者是不是建一个组现在消费者也要建一个组那有时候老师这是啥意思呢那一会我统一给你解答就是两个组的事你在脑子里边先记着一个生产者组一个消费者组好吧好那现在呢我们这样就开始去干嘛去鉴定了你要知道消费者工程一启动的时候他也会连这个name server对吧他连name server的时候你看他这在注解当中咱们看到他是不是就指定了
[01:44] 这个topic呀所以他连上name server呢他就去name server当中找找这个topic下边凡是包含这个my topic的这个broker有哪些以及他的消息队列有哪些懂吗所以他就找到了broker以及消息队列他就开始监听了就这个这个类就开始监听了那么监听呢有时候老师那监听那我监听到了咋弄呢我监听到消息他是不是应该调一个方法呀没错
[02:14] 这时候呢我们要实现一个东西对监听的时候我就让他监听哎呦这个好像弄错了啊不是这个这个类弄错了哦好他监听到消息他就会自动调on message那这个行餐啊对他就会干嘛得到消息对这个方法
[02:44] 这个形态就是消息那所以这里边你看我我先简单打印一下比如这个我们把它改一个名MSG看这就是一个什么一个消费者有时候老师这个太简单了是吧打印一个东西那其实我们在实际生产当中这是要编写什么呀对编写业务逻辑的
[03:07] 那你是不是要接收到消息啊此方法被调用你记着此方法被调用那么就表示接收到什么消息了MSG这个行参就是消息的内容懂我意思吧你接收到消息之后那你说很显然这里边就开始干嘛开始处理消息等等等等对不对这里边我只是先简单打印一下是吧好那
[03:35] 我们说这个消费者工程就起来了呀起来了之后那怎么弄啊我们是不是就可以把它启动起来让它接消息了好看好那我这里面就开始启动它了来启动起来之后呢我们时刻关注控制台看它能不能打印出我们发的怎么样叫第一条同步消息对吧我这是还有一个异步消息你注意啊我说一下因为
[04:02] 这个my topic你注意这个主题你也看到了里边我有好多测试你看见吗很有可能里边是堆积的消息他也给接到了大家理解吧一会呢我再写测试呢我就换一个名很讲义上可能不是很一样好那下边呢我们再看这个消费者工程已经起来了那我那我现在呢准备再发一条我再发一条行不行哎好那我现在再发一条我发一条啥呀嗯我就发一条这是第二条通报消息
[04:32] 行不行好那我就这发了啊这一发那消费者是不是正在监听呢那消费者监听他就拿到消息了我只要一发消费对这一友他就拿到了你注意看这是消费者对吧注意看拿到了吧就说明这个消息是不是被消费掉了吧对所以以上呢就是我们说的什么快速入门
[04:58] 那么这个快速入门通过快速入门我们知道我们是如何编写生产者如何编写消费者那生产者程序编写的方法非常简单我们写一个Spring的bin然后呢里边主要我们要使用RocketMQ的template这个模板对象它这里边有很多的发送方法稍后我们还会详细去学那么在发消息的时候一定要指定两个参数啊这两个参数是必须要指定的后边我们还会学其他的参数比如说topic和什么
[05:27] MSG一个是主题你发往哪一个主题下边的消息队列这就相当于一级分类另外还有个MSG就是消息内容那么消费者他也不复杂消费者主要是监听消息那你监听哪一个topic对吧那么发动者是向topic发那消费者呢是监听topic另外消费者要指定一个消费者组对吧这个组一会儿我再说
[05:54] 那么还要实现一个rocket.mq的listener这个接口然后呢这样它的一个实现方法就只要这个方法被调用那就说明它接收到消息了那我们就可以在这个方法当中来写一些业务处理了这就是整个的我们说rocket.mq的快速出门程序

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RocketMQ 实现消息的发送与接收，包括创建生产者和消费者工程、编写监听类、配置以及测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 画面标题：RocketMQ 实战 - 2.3.3.2 发送同步消息
- 内容：展示一个名为 ProducerSimple 的 Java 类，用于发送同步消息。
- 代码：
```java
/**
 * RocketMQ发送消息类
 * @author Administrator
 * @version 1.0
 **/
@Component
public class ProducerSimple {
    @Autowired
    private RocketMQTemplate rocketMQTemplate;

    /**
     * 发送同步消息
     * @param topic
     * @param msg
     */
    public void sendSyncMsg(String topic, String msg){
        rocketMQTemplate.syncSend(topic,msg);
    }
}
```

画面 2:
- 画面标题：2.3.4.2 消费消息
- 内容：展示一个名为 ConsumerSimple 的 Java 类，用于监听消息。
- 代码：
```java
package com.shanjuipay.test.RocketMQ.message;

import org.apache.RocketMQ.spring.annotation.ConsumeMode;
import org.apache.RocketMQ.spring.annotation.RocketMQListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

/**
 * 消费消息监听类
 * @author Administrator
 * @version 1.0
 **/
@Component
@RocketMQMessageListener(topic = "my-topic",consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {

    //按手到消息调用此方法
    @Override
    public void onMessage(String s) {

    }
}
```

画面 3:
- 内容：IDE 中显示了测试通过的界面，表明测试成功。
- 信息：测试通过，退出码为 0。

画面 4:
- 内容：IDE 中显示了 ConsumerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
@RocketMQMessageListener(topic = "my-topic", consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {
```

画面 5:
- 内容：空白画面，无具体信息。

画面 6:
- 内容：IDE 中显示了 ConsumerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
@RocketMQMessageListener(topic = "my-topic", consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {
```

画面 7:
- 内容：IDE 中显示了 ConsumerApplication 类的代码，其中包含主方法。
- 代码：
```java
@SpringBootApplication
public class ConsumerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }
}
```

画面 8:
- 内容：IDE 中显示了 ConsumerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
@RocketMQMessageListener(topic = "my-topic", consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {
```

画面 9:
- 内容：IDE 中显示了 ConsumerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
@Override
public void onMessage(String s) {
    System.out.println(s);
}
```

画面 10:
- 内容：IDE 中显示了测试通过的界面，表明测试成功。
- 信息：测试通过，退出码为 0。

画面 11:
- 内容：RocketMQ 控制台界面，显示了消息主题列表。
- 信息：主题列表中包含多个主题，如 SELF_TEST_TOPIC、TP_PAYMENT_RESULT 等。

画面 12:
- 内容：IDE 中显示了 ProducerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
public void sendSyncMsg(String topic, String msg){
    rocketMQTemplate.syncSend(topic,msg);
}
```

画面 13:
- 内容：IDE 中显示了 pom.xml 文件的内容。
- 代码：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>test-RocketMQ</artifactId>
        <groupId>com.shanjuipay</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>RocketMQ-producer</artifactId>
</project>
```

画面 14:
- 内容：IDE 中显示了 ConsumerSimple 类的代码，其中包含注解和实现。
- 代码：
```java
@RocketMQMessageListener(topic = "my-topic", consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {

    //按手到消息调用此方法
    @Override
    public void onMessage(String s) {
        System.out.println(s);
    }
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

