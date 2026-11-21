# 画面线理解：09_RabbitMQ快速入门-生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\09_RabbitMQ快速入门-生产者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:40, 03:09, 05:03, 05:29, 08:10, 09:21, 10:36, 11:55, 15:41, 19:09, 20:16, 21:16, 22:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:35:22

1) 这一组画面整体在讲 RabbitMQ 的快速入门，通过编写一个生产者发送消息到队列、消费者接收消息的简单程序，演示其基本使用流程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程标题页“3. RabbitMQ 快速入门”下的子章节“3.1 入门程序”。
画面2: 在 IntelliJ IDEA 中配置项目，设置项目名称为“rabbitmq”，SDK 为“1.8 (Java 1.8.0_211)”，并显示一个简单的消息流程图（P -> [消息队列] -> C）。
画面3: 在 Notepad++ 中编辑 Maven 项目的 pom.xml 文件，显示了 XML 声明和 schemaLocation 配置。
画面4: 展示课程标题页“3. RabbitMQ 快速入门”下的子章节“3.2 小结”。
画面5: 展示 PPT 标题“1.6 RabbitMQ 简介”，内容包括 RabbitMQ 的发布年份、开发语言（Erlang），并附带一个架构图：Producer -> Connection -> Channel -> Exchange -> Binding -> Queue -> Consumer，其中 Broker(RabbitMQ Server) 包含 Virtual Host、Exchange、Queue 等组件。
画面6: 在 IntelliJ IDEA 中，显示了 RabbitMQ 的架构图，同时在代码编辑器中展示了 ConnectionFactory 的相关方法，如 setUserName、setPassword、setVirtualHost 等。
画面7: 在 RabbitMQ Management 管理界面中，显示了“Queues”页面，可以添加新队列，当前无队列。
画面8: 在 IntelliJ IDEA 中，显示了 RabbitMQ 的架构图，同时在代码编辑器中高亮了 ConnectionFactory 的 getExceptionHandler 方法。
画面9: 在 IntelliJ IDEA 中，显示了 RabbitMQ 客户端库的源码，包括 exchangeDeclare、queueDeclare、messageCount 等方法。
画面10: 在 IntelliJ IDEA 中，显示了 Producer_HelloWorld.java 文件，代码中调用 channel.queueDeclare 方法创建队列。
画面11: 在 IntelliJ IDEA 中，显示了 Producer_HelloWorld.java 文件，代码中调用 channel.basicPublish 方法发送消息。
画面12: 在 IntelliJ IDEA 中，显示了 Producer_HelloWorld.java 文件，代码中调用 channel.close 和 connection.close 方法关闭连接。
画面13: 在 RabbitMQ Management 管理界面中，显示了“Queues”页面，当前无队列。
画面14: 在 IntelliJ IDEA 中，显示了 Producer_HelloWorld.java 文件，代码中定义了消息体为“hello rabbitmq”，并调用 channel.basicPublish 方法发送消息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面3: 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
```

画面6: 
```java
//1.创建连接工厂
ConnectionFactory factory = new ConnectionFactory();
//2.设置连接参数
factory.setHost("localhost");
factory.setPort(5672);
factory.setUsername("guest");
factory.setPassword("guest");
//3.创建连接
Connection connection = factory.newConnection();
//4.创建Channel
Channel channel = connection.createChannel();
//5.创建队列
queueDeclare(String queue, boolean durable, boolean exclusive, boolean autoDelete, Map<String, Object> arguments)
```

画面10: 
```java
//5.创建队列
channel.queueDeclare("hello_world", true, false, false, null);
```

画面11: 
```java
//6.发送消息
String body = "hello rabbitmq";
channel.basicPublish("", "hello_world", null, body.getBytes());
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面5: PPT 标题“1.6 RabbitMQ 简介”，内容包括：
- 2007年，Rabbit 技术公司基于 AMQP 标准开发的 RabbitMQ 1.0 发布，RabbitMQ 采用 Erlang 语言开发。
- Erlang 语言由 Ericson 设计，专门为开发高并发和分布式系统的一种语言，在电信领域使用广泛。
- RabbitMQ 基础架构图：Producer -> Connection -> Channel -> Exchange -> Binding -> Queue -> Consumer，其中 Broker(RabbitMQ Server) 包含 Virtual Host、Exchange、Queue 等组件。

画面6: 架构图结构：Producer -> Connection -> Channel -> Exchange -> Binding -> Queue -> Consumer，其中 Broker(RabbitMQ Server) 包含 Virtual Host、Exchange、Queue 等组件。

画面8: 架构图结构：Producer -> Connection -> Channel -> Exchange -> Binding -> Queue -> Consumer，其中 Broker(RabbitMQ Server) 包含 Virtual Host、Exchange、Queue 等组件。

画面9: 无具体架构图，仅显示源码。

5) 无其他内容。
