# 02_高级特性-消息可靠投递-confirm

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\02_高级特性-消息可靠投递-confirm_【海量资源尽在 ubkz.com】.mp4
- 时长 13分27秒（音频 808s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍RaptorMQ的高级特性中的第一个小知识点消息的可靠投递那么对于可靠投递这四个字我相信大家并不难理解比如说我作为一个生产者我肯定期望我将来发送的消息一定能够到达broker也就是到达消息中间件而不至于消息丢失了
[00:25] 所以呢RabbitMQ给我们提供了两种方式来控制消息投递的可靠性第一种呢叫做Confirm确认的模式第二种叫做Return退回的模式那么这两种模式我们先不做介绍我们先来回顾一个知识点就是RabbitMQ整个消息投递的路径是这么样子的首先呢ProducerProducer发送消息把消息发给RabbitMQ的Broker中间键
[00:52] 其实呢也就是说把消息发给了Exchange交换机交换机是收消息的第一站消息换机收到消息之后再将消息通过RoutingK的方式路由到Q存储对列里边然后呢消费者监听一个对列拿到对应的消息数据那么这是整个过程那么接下来我们就来介绍一下这两种模式第一种Confirm模式它指的是Producer
[01:18] 发送消息的时候你可以对发送端设置一个conform的callback监听然后呢将来消息到达或者不到达exchange那么这个监听回调都会被执行如果exchange成功的收到消息将来有个参数它的值就为true如果没有成功收到消息那个参数的值就为false所以第一种呢说消息从producer到exchange
[01:47] 会返回一个叫做conform的callback回调函数那么不管消息是否成功到达exchange这个回调都会执行只不过返回的那个布尔类型的值是true还是false的事这是第一种conform的模式那么第二种呢就是return的退回模式它指的是exchange到q如果exchange将来交换机路由到q失败了
[02:15] 则会去执行一个叫做return callback只有失败才会执行啊所以呢第二种呢是这么一个样子的那么通过这两种模式啊我们就可以来去进行消息可靠性的一个投递了那么也就是说成功的时候其实都还好没有什么问题但是如果说失败了那么RabbitMQ给我们提供的这种模式可以监听到消息投递失败
[02:41] 的一种情况那么我们就可以再通过业务的处理来保证消息再次发送能够成功OK那么介绍了这种可靠性投递那么接下来我们来完成代码的编写在这一小节中我们首先先来完成Confirm确认模式的代码编写打开我们的idea
[03:03] 我们可以看到在这里边我们提前创建好了这么两个工程Spring整合的一个Producer的生产端一个Spring整合后的Consumer消费端那么这个地方呢我们也定义好了一个属性文件叫做RabbitMQ.Properties并且呢用的是默认的用户以及默认的虚拟机并且呢我们提供好了Spring整合的一个Producer生产端的这么一个Xmel的配置文件在这里边加载了配置属性配置文件
[03:30] 然后呢定义了这个连接工厂然后定义了admin来管理这些交换机对列的这么一个admin并且呢我们提供了这个template来简化我们的操作OK那么下来呢我们就可以在里边写对应的配置首先呢我们先来定义一个注释写一个注释这个注释呢是我们的消息的可靠性可靠性投递那么这个可靠性投递指的是
[04:00] 生产端生产端那么当然我们可以在这里边定义一个q再定义一个交换机RabbitMQ的q这个q呢我们给它指定一个id然后呢再指定一个nameid和name呢我们就定义成一样的就可以了这个id呢我们起个名叫做test-q-confirmfirm好
[04:25] 然后呢这个name呢就是这个q的名字我们也叫这个名这样呢我们这个q就定义好了然后接下来我们来定义一个交换机因为现在呢我们这个guest用户下一个q都没有所以呢我们要定义这么两个然后呢定义一个这种direct方式的交换机那么这个交换机呢我们也起个名叫做test-交换机叫做exchange吧anje-conform好
[04:52] 然后这个交换机定义好了之后呢我们给它绑定一下这个Q绑定的时候呢我们Q的名字呢我们叫这个名然后呢这个K呢我们叫叫Firm好了那么这样呢我们就定义好了这个Q和交换机我们可以看一下在我们当前的这个管理界面里边没有一个的对列也没有对应的刚才那个交换机
[05:13] 那么弄好了之后呢接下来我们打开这个提前准备好的这个测试类啊我们已经写好了软位置注解加载好了配置文件并且在里边提供了一个Rabbit Template的一个注解提供好这个配置这个工具类然后呢并且自动注入进来了然后下来呢我们就来写一个测试的方法Public void test confirm好那么这个方法呢我们加一个test注解好
[05:43] 在这里边呢我们写一个文档的注释在这里边我们完成的是确认模式那么我们对这个模式的步骤呢来简单的做一个讲解第一步我们要开启这个确认模式怎么做呢首先呢我们要完成一个确认模式的开启模式的开启开启呢我们需要在这个Connection FactoryFactory中开启
[06:12] 这个在Connection Factory我们这个Connection Factory是不是通过配置的方式定义的你要开启这个确认的这种模式呢它有一个属性我们需要设为True这个属性呢叫做我们来看一下叫做Confirm叫做Publisher Confirms它默认是False就是个确认模式默认是关闭的那么接下来我们要把它开启设为True我们把这个配置呢给它复制过来好第一步呢我们要做这个事情
[06:41] 做完了这个事情之后呢我们第二步我们就可以去定义一个或者说在这个Wrapped Template这个工具类上或者是模板类上去定义一个叫做FIM Conform Callback这么一个回调函数那么将来当你消息一旦发送出去之后这个回调就会自动的被执行
[07:08] 那么我们执行之后呢我们就可以判断它的一个返回的布尔值是true还是false来判定它发送成功还是失败我们可以来尝试一下第一步我们已经做完了那么第二步呢第二步我们来定义这个回调定义回调呢我们用wrapped templatewrapped template.set这么一个叫做confirm callback我们可以new一个confirm callback好new完了之后呢我们在这里边先
[07:36] 打印这么一句话打印一句话说这个confirmconfirm方法被执行了好这个回调呢里边是一个匿名内部类的方式来完成的这里边有一个方法将来消息发送出去这个方法就会被执行那么这个里边有两个参数三个参数这三个参数我们待会再来解释现在定义好了回调之后呢下来最后我们来发送一条消息测试一下发送消息
[08:07] 发送消息用repetitemplate.converterandsend然后写交换机的名称复制一下不要写错了交换机是这个名testexchangeconfirm然后对应的一个routingk叫做confirmconfirm然后消息我们就随便写一个messagemessageconfirm随便写就可以了
[08:33] 那么这样呢我们的代码就写完了写完了之后呢根据刚才我们的分析当这个消息发送出去这个回调是不是就被执行了我们来测试一下现在呢在我的队列里边它会自动创建这个交换机和这个队列稍等一下我们可以来看一下看一下你看这个方法是不是就被执行了并且呢这个消息已经成功的进入了这个队列里边了对吧现在只不过我们没有消费而已
[09:00] 那么接下来我们接着来说现在呢接下来我们来看一下这里边这个回调confirm方法这个方法有三个参数我们来看一下好这个参数呢第一个参数correlation data它其实翻译过来是一些相关的配置信息这个信息呢在哪设置呢
[09:21] 这个信息在我们发送消息的时候Converter and Send转换和发送这个方法里边这个里边其实呢我们用的这个方法它没有参数信息但是呢它提供了一些重载比如说下边你看这个它就可以去设置一些参数的信息我们将来创建这么一个对象在对象里边设置一些配置的信息然后呢我们就可以在这里边获取到这些信息了但是这一块我们先不做设置
[09:48] 那么第二个参数AKK这个就比较关键了这个参数就代表了exchange交换机exchange这个交换机是否成功收到了消息那么true代表成功false代表失败false写错了好什么意思呢就是说将来你的交换机如果
[10:20] 成功收到消息那么这个参数的值就为true那么如果交换器没有收到消息就人民消息发丢了那么这个值就为false将来在这个方法里边我们就要来判断这个参数ACK为true还是false那么第三个cause这个玩意儿呢很简单就是失败的原因失败原因如果将来这个ACK的值为false那么这个strain内心的cause就有值了它呢就是失败的原因了
[10:48] 那么我们可以在这里边来做一个判断如果如果这个AK好AK为处呢这叫做接收成功对吧然后呢else这个玩意呢就是接收失败好接收失败那么接收成功呢我们就随便打一句话说接收成功消息好然后呢我们可以加上这个失败的原因这个时候呢成功了肯定没有失败原因失败原因就会闹
[11:16] 那么同理啊我们在下边也来打印一条这个消息以下边失败说接收失败消息失败了之后呢我们也打下失败的原因那么接下来我们来重新来运行一下当然现在肯定是成功因为现在我们的对应的这个地方的一个交换机是正确的路由K也是正确的所以呢它发送肯定会成功我们可以来看一下稍等正在运行
[11:48] 那么你看现在是不是接收成功了OK吧那么现在我们想失败也很简单随便我们找一个我们比如说把交换机这个地方的名字改错了随便写加三个1是不是就错了那么这个消息肯定不能成功的发送到一个交换机上因为不存在这个交换机那么这个时候肯定会失败我们来看一下它会不会失败呢稍等那这个时候你看一下这个方法被执行了并且接收失败了这个消息
[12:16] 那么失败的信息呢就是我们的错误原因这么大一堆那么这么大一堆呢我们可以往后看这里边有一个no exchange这么一个交换机的名字在当前这个斜杠这个虚拟机里边默认的虚拟机里边他也告诉你呢失败的这么一个原因是什么什么的对吧OK啊那么这样呢我们就知道了我们的消息发送成功还是失败那么至于失败了之后怎么处理呢将来我们可能要去做一些做一些处理哈
[12:45] 处理处理呢让这个消息再次发送要保证它再次能够发送成功那么至于怎么处理这是我们第二部分常见的一些问题里边来讲解的这一块呢我们只需要知道如何来设置这个confirm的callback就可以了那么这一块呢我们简单的讲了第一种的confirm的确认模式它有两个
[13:09] 一个小的操作第一个呢要开启确认模式第二个呢我们要在Wrapped Template里边定义这么一个回调设置这个Conform的Callback这么一个回调函数就可以了OK那么这个第一个确认模式我们就讲解到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RabbitMQ 的 confirm 确认模式来实现消息的可靠投递。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题“1.1 消息的可靠投递”，介绍 RabbitMQ 提供的 confirm 和 return 两种可靠性投递模式，并说明消息投递路径。
画面 2: 展示 IntelliJ IDEA 中的 `spring-RabbitMQ-producer.xml` 配置文件，定义了 `rabbit.connection-factory` 和 `rabbit.template`。
画面 3: 展示 `spring-RabbitMQ-producer.xml` 中定义了 `rabbit:queue` 元素。
画面 4: 展示 RabbitMQ 管理后台的 Exchanges 页面，列出多个交换机。
画面 5: 展示 `ProducerTest.java` 文件，定义了测试类 `ProducerTest`，并使用 `@RunWith(SpringJUnit4ClassRunner.class)` 和 `@ContextConfiguration` 注解。
画面 6: 展示 `spring-RabbitMQ-producer.xml` 中定义了 `rabbit:direct-exchange` 和 `rabbit:binding`。
画面 7: 展示 `ProducerTest.java` 中的 `testConfirm` 方法，准备设置确认回调。
画面 8: 展示 `ProducerTest.java` 中为 `rabbitTemplate` 设置 `ConfirmCallback` 的代码。
画面 9: 展示 `ProducerTest.java` 中调用 `rabbitTemplate.convertAndSend` 发送消息的代码。
画面 10: 展示 RabbitMQ 管理后台的 Exchanges 页面，与画面 4 相同。
画面 11: 展示测试运行结果，显示测试通过，并在控制台输出“confirm方法被执行了...”。
画面 12: 展示 `ProducerTest.java` 中为 `ConfirmCallback` 方法添加了 `if (ack)` 判断逻辑。
画面 13: 展示 `ProducerTest.java` 中在 `else` 分支中添加了打印失败消息的代码，并准备发送一个失败的消息。
画面 14: 展示 `ProducerTest.java` 中修改了 `convertAndSend` 的参数，使消息发送失败，并在控制台输出“接收失败消息”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory"
        host="172.16.98.133"
        port="5672"
        username="guest"
        password="guest"
        virtual-host="//"/>
    <!--定义RabbitMQ连接工厂，从别为-->
    <rabbit:admin connection-factory="connectionFactory"/>
    <rabbit:template id="rabbitTemplate" connection-factory="connectionFactory"/>
</beans>
```

画面 3:
```xml
<rabbit:queue id="test_queue" />
```

画面 6:
```xml
<rabbit:direct-exchange name="test_exchange_confirm">
    <rabbit:binding queue="test_queue_confirm" key="confirm"/>
</rabbit:direct-exchange>
```

画面 5:
```java
package com.ithema.test;

import org.junit.runner.RunWith;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:spring-RabbitMQ-producer.xml")
public class ProducerTest {

}
```

画面 7:
```java
public void testConfirm() {
    //1. 确认模式开启：ConnectionFactory中开启publisher-confirms="true"
    //2. 在RabbitTemplate中定义confirmCallback回调函数
}
```

画面 8:
```java
rabbitTemplate.setConfirmCallback(new RabbitTemplate.ConfirmCallback() {
    @Override
    public void confirm(CorrelationData correlationData, boolean ack, String cause) {
        System.out.println("confirm方法被执行了....");
    }
});
```

画面 9:
```java
rabbitTemplate.convertAndSend("test_exchange_confirm", "confirm", "message confirm.");
```

画面 12:
```java
if (ack) {
    //接收成功
} else {
    //接收失败
}
```

画面 13:
```java
rabbitTemplate.convertAndSend("test_exchange_confirm11", "confirm", "message confirm.");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1. RabbitMQ 高级特性”，子标题“1.1 消息的可靠投递”，内容包括：
- 消息投递路径：producer ---> RabbitMQ broker ---> exchange ---> queue ---> consumer
- 两种可靠性投递模式：confirm 确认模式、return 返回模式

画面 4: RabbitMQ 管理后台的 Exchanges 页面表格数据：
- Virtual host: (AMQP default)
- Name: amq.direct, amq.fanout, amq.headers, amq.match, amq.RabbitMQ.log, amq.RabbitMQ.trace, amq.topic
- Type: direct, fanout, headers, headers, topic, topic, topic
- Features: Q, Q, Q, Q, Q, Q, Q

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

