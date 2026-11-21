# 19_Spring整合RabbitMQ-配置详解

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\19_Spring整合RabbitMQ-配置详解_【海量资源尽在 ubkz.com】.mp4
- 时长 8分19秒（音频 500s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完Spring整合RabbitMQ我们发现呢Spring整合之后呢这个代码就非常的少了在Consumer这一端需要写个监听在Producer这一端只需要写一些用一个叫做RabbitTemplate来完成消息的发送就可以了虽然我们的一个代码编写就非常简单但是呢它的配置就增多了很多一大堆的配置都在配置文件中体现
[00:28] 那么这一小节我们将这些配置文件来做一个详解简单来看一下刚才我们把配置文件粘进来之后以运行没有问题大概其实各位也能够去看懂这些个配置只不过里边还有一些属性我们需要单独说一下那么首先先看第一个这个context的冒号这个玩意叫做名称空间这个名称空间的头是Sprint提供的
[00:53] 而下边这些个名称空间都是由RabbitMQ来提供的或者说Spring整合之后提供的有这么一个约束的头这个是Spring整合RabbitMQ提供的这么一个名称空间换句话说它导入了一个约束的文件是这么一个约束文件那么当然这样是为了简化我们的配置我们也可以把它写成bin的一个配置方式
[01:21] 那么使用并标签配置呢就会稍微麻烦一些这其实都是一些并标签的简化配置好嘞那么先前面呢这就是定义一些参数信息然后呢声明了一个Spring封装的Connection Factory这个没有什么好说的那么下面我们主要来看这个地方Rabbit冒号Q其实就相当于声明了一个Q的对列那么这里边有这么些参数我们可以来简单的说一下这个参数
[01:51] 参数这个参数呢第一个IDID呢表示了这个bin的名称注意啊这个ID是bin的名称然后呢这个Name注意啊这个Name是ID一样其实可以不一样这个Name呢就是这个对列Q的这个名称Q的名称我们之前呢用AMQP client的方式来声明对列是不是要给对列指定一个名字呀OK啊
[02:22] 然后呢第三个我们还有那个属性叫auto-declare的declare呢叫做自动的去声明如果它不存在的时候就自动创建啊自动自动创建那么除了这三个属性其实还有一些属性啊好我们可以来看一下比如说auto-delete这个我们之前都介绍过AOTODLETEdelete叫做自动删除你要注意啊这个自动删除我们并没有演示
[02:51] 待会大家可以自己去试验一下就是说最后一个消费者和该对列断开连接后这个后他自动删除删除谁呢删除对列就是没有消费者跟他连着了他就自动删除了当然啊一定是要有消费者连了之后再断开才会自动删那么说这几个呢还有我们也学过的比如说Joyful
[03:22] 这一波呢表示了是否持久化比如说等于处的话呢就是持久化等于false呢就是不持久化是否持久化好那么除了这个呢我们之前也说过还有是否独占连接哈有这么一些属性啊来看一下哎还有呢比如说是否去排他的对吧排他呢就是独占连接哎我们把它写在这也行是否独占OK好嘞
[03:54] 那么这几个参数呢我们也简单的说了一下然后还有一些其他的参数我们下一次呢学了高级的部分再来去讲解其他的一些参数就可以了这是我们对列声明的一些参数那么除了对列声明呢我们还有交换机的一个声明在交换机里边呢你注意看Rabbit Front Exchange表示了呢我们声明的一种广播类型的交换机那么广播类型交换机里边这也相当于是这个bin的名称或者是bin的ID
[04:23] 然后呢下来这个名字表示了交换机的名字自动声明那么交换机里边其实也有一大堆的参数这个我就不挨个写了这个呢表示持久化是否自动删除对吧然后呢还有呢是否内部使用这些参数刚才我们在介绍Client的时候都说过那么除了这样类型的交换机之外我们可以来看一下其实还有一些其他类型的交换机注意看然后这个叫做Rabbit还有呢比如说Direct
[04:53] 这个我们随便写好那么这样呢声明了一个交换机声明了交换机之后呢你注意交换机声明了之后接下来是不是要做一件事就是将对列和交换机做一个绑定不同类型的交换机绑定的时候的规则不一样广播类型的交换机它不需要去指定路由K的名称所以你注意看在这个Rabbit绑定这个里边来绑定的时候
[05:21] 只需要给一个对列的名字就可以了然后呢没有任何绑定的规则因为对应的路由K的默认是空字不串对吧那么我们再来看如果是Direct的这种Exchange那么这种这种交换机绑定的时候要指定路由K并且路由K的名字得去完全匹配
[05:46] 所以呢这个里边你注意看RapidMQBonding这个Bonding里边的属性就不太一样了首先呢它有这么几个第一个呢就是对列的名称我们随便比如说举个例子对列名称那么第二个呢就是K这个K呢就指定的是路由K的名字所以这个地方要注意你注意看虽然他们的标签是一样的标签但是呢他们在的位置不一样那么这个标签里边对应的约束也就不一样
[06:16] 这里边就不能再加K了加K它就是一个错误的属性就爆红了说找不到这个属性对吧所以呢这个地方要注意这么一个事情那么我们在这个里边呢可以来写一下这个东西呢叫做我们DRIECT就是这个叫做类型的交换机来绑定对链绑定对链呢这个K指的就是我们的RO路由K好
[06:46] 然后呢这个Q由1由1这个就指定的是我们的对列名称OK啊上边我们就这个就不再写了当然这一块呢可以这样弄这也是Direct Exchange那么除了Direct Exchange之外呢其实还有下边下边呢还有一种对列我们是讲了三种嘛还有一种Topic的这么一个对Topic的一个交换机不是对列那么这个交换机绑定的时候是不是我们通配服的方式啊你注意看这个地方呢就没有K这个属性了
[07:15] 你看是没有K的属性了而它的属性呢是一个pattern表达式对吧我们可以写信号也可以写警号这样的方式所以呢这个交换机声明的时候我们通过这样的一个名称空间的声明就非常的简单了如果你要通过bin标签来声明这个还是稍微会麻烦一些这就是我们所说的对应的Spring的整合之后的Producer提供的一个配置文件的一个详细解释
[07:44] 那么当然最后呢提供了一个template这也相当于是一个bin将来你通过这个玩意儿呢就可以注入到对应的我们的代码里边来完成消息的发送那么接下来呢consumer里边没有什么好说的consumer里边就定的是bin标签然后呢给了一个class对吧这个class呢就声明了一个bin相当于是个监听器然后这个监听器里边我们把它加到对应的rabbit listener的container监听器容器里边给它加载一下就注册一下就可以了
[08:12] 大概我们的Spring整合之后的一些配置的属性的一个介绍我们就讲解到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Spring AMQP 配置 RabbitMQ 的消费者、生产者、队列、交换机及绑定关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示消费者监听器类 SpringQueueListener.java，其中 onMessage 方法用于打印接收到的消息内容。
画面 2: 展示生产者配置文件 spring-RabbitMQ-producer.xml，其中定义了两个扇形队列（fanout queue）及其绑定关系。
画面 3: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 4: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 5: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 6: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 7: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 8: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的队列（queue）配置，包括 id、name、auto-declare、durable 等属性。
画面 9: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的扇形交换机（fanout exchange）及其绑定关系。
画面 10: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的直接交换机（direct exchange）及其绑定关系。
画面 11: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的主题交换机（topic exchange）及其绑定关系。
画面 12: 展示 spring-RabbitMQ-producer.xml 文件中定义了 RabbitMQ 的模板（rabbitTemplate）配置，用于发送消息。
画面 13: 展示 spring-RabbitMQ-consumer.xml 文件中定义了消费者容器（rabbitListener-container），配置了多个监听器及其对应的队列。
画面 14: 展示 spring-RabbitMQ-consumer.xml 文件中定义了消费者容器（rabbitListener-container），配置了多个监听器及其对应的队列。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.lithina.RabbitMQ.listener;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;
public class SpringQueueListener implements MessageListener {
    @Override
    public void onMessage(Message message) {
        //打印消息
        System.out.println(new String(message.getBody()));
    }
}
```

画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <!--定义广播交换机，不绑定任何队列，不指定路由键，消息会广播到所有绑定的队列-->
    <rabbit:fanout-exchange id="spring_fanout_exchange" name="spring_fanout_exchange" auto-declare="true">
        <rabbit:binding queue="spring_fanout_queue_1" />
        <rabbit:binding queue="spring_fanout_queue_2" />
    </rabbit:fanout-exchange>
</beans>
```

画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133" port="5672" username="heina" password="heina" virtual-host="/itcast"/>
</beans>
```

画面 4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133" port="5672" username="heina" password="heina" virtual-host="/itcast"/>
</beans>
```

画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133" port="5672" username="heina" password="heina" virtual-host="/itcast"/>
</beans>
```

画面 6:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133" port="5672" username="heina" password="heina" virtual-host="/itcast"/>
</beans>
```

画面 7:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory id="connectionFactory" host="172.16.98.133" port="5672" username="heina" password="heina" virtual-host="/itcast"/>
</beans>
```

画面 8:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/rabbit
        http://www.springframework.org/schema/rabbit/spring-rabbit.xsd">
    <context:property-placeholder location="classpath:RabbitMQ.properties"/>
    <rabbit:connection-factory

