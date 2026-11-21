# 画面线理解：11.RocketMQ研究-Rocket基础-自定义消息格式

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\11.RocketMQ研究-Rocket基础-自定义消息格式【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:40, 01:30, 02:25, 03:37, 04:22, 05:35, 06:20, 07:09, 07:51, 08:20, 08:53, 09:33, 10:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:10:17

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 RocketMQ 实现同步消息的发送与接收，包括定义消息实体类、生产者和消费者代码，以及在控制台查看消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前位于“2.3.2 发送同步消息”部分，右侧代码编辑器显示 OrderExt 类的定义，包含 id、createTime、money、title 字段。
画面2：在 IDE 中展示 ProducerSimpleTest.java 文件，代码中包含 onApplicationEvent 方法，用于处理发送失败的回调。
画面3：展示项目结构，选中 OrderExt 类，右侧代码编辑器显示 OrderExt 类的定义，包含 id、createTime、money、title 字段。
画面4：展示 ProducerSimpleTest.java 文件，代码中包含 sendSyncMsg 方法，用于发送同步消息。
画面5：展示 AbstractMessageSendingTemplate.java 文件，代码中包含 convertAndSend 方法，用于发送消息。
画面6：展示 ProducerSimpleTest.java 文件，代码中包含 testSendSyncMsg 方法，用于测试同步消息发送。
画面7：展示 OrderExt 类的代码，代码中包含 setId、setMoney、setCreateTime、setTitle 方法。
画面8：展示 RocketMQ 控制台，显示消息列表，包含 Message ID、Tag、Key、StoreTime 等信息。
画面9：展示课程目录结构，当前位于“2.3.3 消费者工程”部分，右侧代码编辑器显示 ConsumerSimple 类的定义，包含 onMessage 方法。
画面10：展示 ConsumerSimple.java 文件，代码中包含 @Component 注解和 RocketMQMessageListener 注解。
画面11：展示 ConsumerSimpleObj.java 文件，代码中包含 @Component 注解和 RocketMQMessageListener 注解。
画面12：展示 ConsumerSimpleObj.java 文件，代码中包含 @Component 注解和 RocketMQMessageListener 注解。
画面13：展示 ConsumerSimpleObj.java 文件，代码中包含 @Component 注解和 RocketMQMessageListener 注解，右侧控制台显示消息接收日志。
画面14：展示课程目录结构，当前位于“2.7 延迟消息”部分，右侧代码编辑器显示 ConsumerSimpleObj 类的定义，包含 onMessage 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.io.Serializable;
import java.util.Date;

@Data
@NoArgsConstructor
@ToString
public class OrderExt implements Serializable {
    private String id;
    private Date createTime;
    private Long money;
    private String title;
}
```

画面2：
```java
@Override
public void onApplicationEvent( Throwable throwable ) {
    System.out.println(throwable.getMessage());
}
```

画面3：
```java
public class OrderExt implements Serializable {
    private String id;
    private Date createTime;
    private Long money;
    private String title;
}
```

画面4：
```java
public void sendSyncMsg(String topic, String msg) {
    rocketMQTemplate.asyncSendTopic(topic, msg, new SendCallback() {
        @Override
        public void onSuccess(SendResult sendResult) {
            System.out.println(sendResult);
        }
        @Override
        public void onException(Throwable throwable) {
            System.out.println(throwable.getMessage());
        }
    });
}
```

画面5：
```java
public void convertAndSend(Object destination, Object payload, Map<String, Object> headers) {
    this.convertAndSend(destination, payload, headers, MessagePostProcessor(null));
}
```

画面6：
```java
public void testSendSyncMsg() {
    producerSimple.sendSyncMsg("my-topic", "条目同步消息");
    try {
        Thread.sleep(5000);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}
```

画面7：
```java
OrderExt orderExt = new OrderExt();
orderExt.setId("11222");
orderExt.setMoney(168L);
orderExt.setCreateTime(new Date());
orderExt.setTitle("测试");
```

画面8：
无代码，仅显示 RocketMQ 控制台界面。

画面9：
```java
@Component
@RocketMQMessageListener(topic = "my_topic", consumerGroup = "demo_consumer_group")
public class ConsumerSimple implements RocketMQListener<String> {
    @Override
    public void onMessage(String s) {
        System.out.println(s);
    }
}
```

画面10：
```java
package com.shanjugy.test.rocketmq.message;

import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "my-topic", consumerGroup = "demo-consumer-group")
public class ConsumerSimple implements RocketMQListener<String> {
}
```

画面11：
```java
@Component
@RocketMQMessageListener(topic = "my-topic-obj", consumerGroup = "demo-consumer-group-obj")
public class ConsumerSimpleObj implements RocketMQListener<String> {
}
```

画面12：
```java
@Component
@RocketMQMessageListener(topic = "my-topic-obj", consumerGroup = "demo-consumer-group-obj")
public class ConsumerSimpleObj implements RocketMQListener<String> {
}
```

画面13：
```java
@Component
@RocketMQMessageListener(topic = "my-topic-obj", consumerGroup = "demo-consumer-group-obj")
public class ConsumerSimpleObj implements RocketMQListener<String> {
    @Override
    public void onMessage(String s) {
        System.out.println(s);
    }
}
```

画面14：
```java
@Component
@RocketMQMessageListener(topic = "my-topic-obj", consumerGroup = "demo-consumer-group-obj")
public class ConsumerSimpleObj implements RocketMQListener<OrderExt> {
    @Override
    public void onMessage(OrderExt orderExt) {
        System.out.println(orderExt);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.3.2 发送同步消息”，目录结构显示“2.3.2 发送同步消息”。
画面9：PPT标题为“消费者”，目录结构显示“2.3.3 消费者工程”。
画面14：PPT标题为“2.7 延迟消息”，目录结构显示“2.7 延迟消息”。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
