# 画面线理解：8.RocketMQ研究-Rocket基础-快速入门-消费者

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\8.RocketMQ研究-Rocket基础-快速入门-消费者【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:20, 00:36, 00:49, 01:08, 01:26, 01:40, 02:18, 02:48, 03:40, 04:05, 04:24, 05:08, 06:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:08:17

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RocketMQ 实现消息的发送与接收，包括创建生产者和消费者工程、编写监听类、配置以及测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 画面标题：RocketMQ 实战 - 2.3.3.2 发送同步消息
- 内容：展示一个名为 ProducerSimple 的 Java 类，用于发送同步消息。
- 代码：
```java
/**
 * rocketmq发送消息类
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
package com.shanjuipay.test.rocketmq.message;

import org.apache.rocketmq.spring.annotation.ConsumeMode;
import org.apache.rocketmq.spring.annotation.RocketMQListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
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
        <artifactId>test-rocketmq</artifactId>
        <groupId>com.shanjuipay</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>rocketmq-producer</artifactId>
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
