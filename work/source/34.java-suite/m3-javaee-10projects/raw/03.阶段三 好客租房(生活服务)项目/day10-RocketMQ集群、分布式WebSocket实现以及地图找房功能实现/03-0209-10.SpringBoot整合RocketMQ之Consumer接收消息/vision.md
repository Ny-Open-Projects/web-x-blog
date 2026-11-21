# 画面线理解：10.SpringBoot整合RocketMQ之Consumer接收消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\10.SpringBoot整合RocketMQ之Consumer接收消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:18, 00:27, 00:47, 01:03, 01:15, 01:43, 02:12, 02:32, 02:54, 03:10, 03:21, 03:37, 04:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:17:15

1) 这一组画面整体在讲如何使用 Spring Boot 集成 RocketMQ 实现消息的消费，通过编写消费者类并配置监听器来接收消息。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PDF 讲义中关于“3.4. 消费消息”的章节，其中包含消费者类的代码示例，定义了 @Component、@RocketMQMessageListener 注解，并指定了 topic、consumerGroup 和 selectorExpression。
画面 2: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 extends 和 implements 之间，提示用户使用 Ctrl+Shift+Enter 修正代码。
画面 3: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 implements 后面，准备输入接口名。
画面 4: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，已编写 @Component 注解和 implements RocketMQListener<String>，并定义了 onMessage 方法。
画面 5: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 @RocketMQMessageListener 注解的括号内，显示了该注解的属性及其默认值。
画面 6: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 @RocketMQMessageListener 注解的括号内，显示了该注解的属性及其默认值。
画面 7: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 @RocketMQMessageListener 注解的括号内，显示了该注解的属性及其默认值。
画面 8: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 @RocketMQMessageListener 注解的括号内，显示了该注解的属性及其默认值。
画面 9: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 import org.apache.rocketmq.spring.core.RocketMQListener; 语句后，显示了 Java 中的常用输出语句。
画面 10: 在 IntelliJ IDEA 中，编辑 MyApplication.java 文件，光标位于 main 方法的右大括号后，显示了 Spring Boot 应用启动的命令行。
画面 11: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息。
画面 12: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息，终端显示了应用启动日志。
画面 13: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息，终端显示了应用启动日志。
画面 14: 展示 PDF 讲义中关于“3.4. 消费消息”的章节，其中包含消费者类的代码示例，定义了 @Component、@RocketMQMessageListener 注解，并指定了 topic、consumerGroup 和 selectorExpression。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "my-topic",
consumerGroup = "haoke-consumer",
selectorExpression = "*")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String msg) {
System.out.println("接收到消息 -> " + msg);
}
}
```

画面 4:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "my-topic",
consumerGroup = "haoke-consumer",
selectorExpression = "*")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String s) {
}
}
```

画面 5:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@RocketMQMessageListener()
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String s) {
}
}
```

画面 6:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "spring-my-topic",
consumerGroup = "spring-consumer-group",
selectorExpression = "*")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String s) {
}
}
```

画面 7:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "spring-my-topic",
consumerGroup = "spring-consumer-group",
selectorExpression = "*",
consumeThreadMax = 64,
consumeMode = "CONCURRENTLY",
selectorType = "TAG")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String s) {
}
}
```

画面 8:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "spring-my-topic",
consumerGroup = "spring-consumer-group",
selectorExpression = "*",
consumeThreadMax = 64,
consumeMode = "CONCURRENTLY",
selectorType = "TAG")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String s) {
}
}
```

画面 9:
```java
import org.apache.rocketmq.spring.core.RocketMQListener;
```

画面 10:
```java
package cn.itcast.rocketmq.spring;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {
public static void main(String[] args) {
SpringApplication.run(MyApplication.class, args);
}
}
```

画面 11:
```java
@Test
public void testSendMsg() {
String msg = "我的第一个SpringRocketMQ消息！";
this.springProducer.sendMsg(topic: "spring-my-topic", msg);
System.out.println("发送成功");
}
```

画面 12:
```java
@Test
public void testSendMsg() {
String msg = "我的第一个SpringRocketMQ消息！";
this.springProducer.sendMsg(topic: "spring-my-topic", msg);
System.out.println("发送成功");
}
```

画面 13:
```java
@Test
public void testSendMsg() {
String msg = "我的第二个SpringRocketMQ消息！";
this.springProducer.sendMsg(topic: "spring-my-topic", msg);
System.out.println("发送成功");
}
```

画面 14:
```java
package cn.itcast.rocketmq.spring;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "my-topic",
consumerGroup = "haoke-consumer",
selectorExpression = "*")
public class SpringConsumer implements RocketMQListener<String> {
@Override
public void onMessage(String msg) {
System.out.println("接收到消息 -> " + msg);
}
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
