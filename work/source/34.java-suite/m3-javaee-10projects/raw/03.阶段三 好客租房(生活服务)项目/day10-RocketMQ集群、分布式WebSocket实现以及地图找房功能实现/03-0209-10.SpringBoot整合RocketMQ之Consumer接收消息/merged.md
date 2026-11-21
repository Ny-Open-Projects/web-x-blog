# 10.SpringBoot整合RocketMQ之Consumer接收消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\10.SpringBoot整合RocketMQ之Consumer接收消息【海量资源尽在 ubkz.com】.mp4
- 时长 4分17秒（音频 257s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来编写消费者的代码然后呢我们再还是回到我们这个Spring这个包下面呢我们来写一个类就叫SpringConsumer然后呢要注意的是那么我们自己写这个Consumer呢需要去做一个接口的一个实现实现什么呢叫LoggerLoggerMQ然后呢Listener然后呢它有一个范形就代表我们消息的类型我们是这块
[00:31] 然后我们去实现接口中的一个方法就是onMessage这个方法那么当我们有消息的时候就会执行我们这个方法那么我们需要给我们写这个类consumer这个类添加两个读解一个是component就是把它加入到spring的容器中然后另外一个我们需要加一个什么叫roctor然后roctormq
[00:58] 然后呢message listener这样的一个注解那么在这个注解中呢我们需要给他添加啊这么几个内容那么首先呢是第一个呢是这个topic就是我们所要去订阅的那个topic是谁呢我们来看一下刚刚我们呃所测试啊写的这个topic那就是他了那么就订阅这个topic来获取这个里面的消息那么第一个内容是他那么第二个内容呢就是需要给他去添加一个
[01:27] consumer的一个grip就是分组那么OK那我们就可以写一个叫做spring然后呢consumer然后呢grip然后呢这是第二个第三个呢我们来看有哪些内容啊那么我们来看一下这个是他的一个选择的一个就是我们去订阅啊订阅的时候他的一个规则那就是新啊那就是新那么新呢就代表着是不是我们获取所有的一个消息啊那我们看还有哪些内容吗
[01:58] 比如说你看在这个位置还有一个consumer的一个这个model对吧model那么我们是不是可以去做一个选择来看一下啊在这个里面它默认是不是就是container啊这个这种类型那么它还有一次old类型对吧那我们来看一下那我们就给它其实我默认就可以了啊默认选中它就行了那还有种是不是叫old这种类型啊ok好那么呃有有这几个呢基本上也就够了啊也就够了
[02:26] 好那么在这个里面呢当我们有消息的时候呢我们就会去执行我们这个方法然后呢我们去打印出来那就写个什么呢叫接收到这个消息然后呢去加一个这个打印哎OK好那么我们来看一下我们怎么样去做一个测试呢我们来看一下那么我们就把这个啊把我们这个跑起来跑起来之后呢我们这个消费者他其实就已经开始去监听
[02:56] 我们的这个队列OK那么我们只要给它启动就好了来等待它的一个执行好到这里是不是已经启动OK了那么下面呢我们在这个位置呢再重新去发送一条消息然后呢我们来看一下走
[03:13] 发送条消息那么等待他这个我们来看一下在这个位置呢消息呢已经是发送成功了那么我们在消费者这一端呢可以看到已经接收到消息了那为什么有两条呢原因是在前面我们做测试的时候已经发送了一条所以呢这是第一条对吧我们可以再来测一下啊那么我们在这个位置吧就是说我的第二条再去发一条我们再试一下走那么等待他的一个执行
[03:41] 我们回到我们消费者这一端看他是否能够再次接收到消息好那么我们可以看到在这个位置他是不是已经接收到了消息了那么OK好那么这个我们所演示的就是消费者其实我们会发现当我们使用了spring或者Spring Boot他的去使用的话那么在我们使用lockedmq API的时候变得是不是非常的简单
[04:07] 变得非常的简单那么OK好那么关于我们Spring Boot整合RocketMQ的一个消费者的一个使用以及编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 9: 在 IntelliJ IDEA 中，编辑 SpringConsumer.java 文件，光标位于 import org.apache.RocketMQ.spring.core.RocketMQListener; 语句后，显示了 Java 中的常用输出语句。
画面 10: 在 IntelliJ IDEA 中，编辑 MyApplication.java 文件，光标位于 main 方法的右大括号后，显示了 Spring Boot 应用启动的命令行。
画面 11: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息。
画面 12: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息，终端显示了应用启动日志。
画面 13: 在 IntelliJ IDEA 中，编辑 TestSpringRocketMQ.java 文件，光标位于 @Test 注解后，显示了测试类中定义的 testSendMsg 方法，用于发送消息，终端显示了应用启动日志。
画面 14: 展示 PDF 讲义中关于“3.4. 消费消息”的章节，其中包含消费者类的代码示例，定义了 @Component、@RocketMQMessageListener 注解，并指定了 topic、consumerGroup 和 selectorExpression。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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
import org.apache.RocketMQ.spring.core.RocketMQListener;
```

画面 10:
```java
package cn.itcast.RocketMQ.spring;
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
package cn.itcast.RocketMQ.spring;
import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
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

