# 画面线理解：20_SpringBoot整合RabbitMQ-生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\20_SpringBoot整合RabbitMQ-生产者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 03:18, 04:58, 06:07, 08:41, 09:40, 11:13, 12:07, 12:49, 13:57, 15:03, 16:17, 17:03, 17:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:42:48

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SpringBoot 项目中整合 RabbitMQ，包括添加依赖、配置连接信息、定义交换机和队列、绑定关系，以及使用 RabbitTemplate 发送消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程标题页，列出生产者实现的五个步骤：创建工程、引入依赖、编写 yml 配置、定义交换机/队列/绑定、注入 RabbitTemplate 并发送消息。
画面 2: 在 IDEA 中打开 pom.xml 文件，准备添加 SpringBoot AMQP 依赖。
画面 3: 在 application.yml 文件中配置 RabbitMQ 的连接参数，包括 host、port、username、password、virtual-host。
画面 4: 在 src/main/java/com/itheima/rabbitmq/config 包下创建 RabbitMQConfig.java 文件。
画面 5: 在 RabbitMQConfig.java 中导入必要的包，并定义一个 @Configuration 类。
画面 6: 在 RabbitMQConfig.java 中定义交换机，使用 ExchangeBuilder 创建一个 topic 类型的交换机。
画面 7: 在 RabbitMQConfig.java 中定义队列，使用 QueueBuilder 创建一个队列。
画面 8: 在 RabbitMQConfig.java 中定义绑定关系，使用 BindingBuilder 将队列绑定到交换机。
画面 9: 在 RabbitMQConfig.java 中完成绑定关系的代码，指定队列名、交换机名和路由键。
画面 10: 在 test 包下创建 ProducerTest.java 文件，并导入 SpringBootTest 和相关注解。
画面 11: 在 RabbitMQConfig.java 中完成交换机和队列的定义。
画面 12: 在 ProducerTest.java 中编写测试方法 testSend()，使用 rabbitTemplate.convertAndSend() 发送消息。
画面 13: 运行测试，终端显示测试通过，日志显示 SpringBoot 应用启动成功。
画面 14: 在 ProducerTest.java 中完成测试方法的编写，并在测试结果中显示测试通过。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

画面 3:
```yaml
rabbitmq:
  host: 127.0.0.1 # ip
  port: 5672
  username: guest
  password: guest
  virtual-host: /
```

画面 5:
```java
package com.itheima.rabbitmq.config;

import org.springframework.amqp.core.Exchange;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.amqp.support.converter.MessageConverter;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.adapter.MessageListenerAdapter;
import org.springframework.amqp.rabbit.support.RabbitResourceHolder;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
import org.springframework.amqp.rabbit.support.RabbitTemplate;
