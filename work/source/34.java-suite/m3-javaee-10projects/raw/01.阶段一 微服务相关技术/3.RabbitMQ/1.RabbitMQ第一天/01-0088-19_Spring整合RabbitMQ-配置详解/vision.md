# 画面线理解：19_Spring整合RabbitMQ-配置详解

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\19_Spring整合RabbitMQ-配置详解_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:30, 00:36, 01:16, 01:30, 01:57, 03:28, 04:02, 04:37, 04:50, 04:58, 06:57, 07:52, 08:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:41:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Spring AMQP 配置 RabbitMQ 的消费者、生产者、队列、交换机及绑定关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示消费者监听器类 SpringQueueListener.java，其中 onMessage 方法用于打印接收到的消息内容。
画面 2: 展示生产者配置文件 spring-rabbitmq-producer.xml，其中定义了两个扇形队列（fanout queue）及其绑定关系。
画面 3: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 4: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 5: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 6: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 7: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的连接工厂（connection-factory）配置，包括 host、port、username、password 和 virtual-host。
画面 8: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的队列（queue）配置，包括 id、name、auto-declare、durable 等属性。
画面 9: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的扇形交换机（fanout exchange）及其绑定关系。
画面 10: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的直接交换机（direct exchange）及其绑定关系。
画面 11: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的主题交换机（topic exchange）及其绑定关系。
画面 12: 展示 spring-rabbitmq-producer.xml 文件中定义了 RabbitMQ 的模板（rabbitTemplate）配置，用于发送消息。
画面 13: 展示 spring-rabbitmq-consumer.xml 文件中定义了消费者容器（rabbitListener-container），配置了多个监听器及其对应的队列。
画面 14: 展示 spring-rabbitmq-consumer.xml 文件中定义了消费者容器（rabbitListener-container），配置了多个监听器及其对应的队列。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.lithina.rabbitmq.listener;
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
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
    <context:property-placeholder location="classpath:rabbitmq.properties"/>
    <rabbit:connection-factory
