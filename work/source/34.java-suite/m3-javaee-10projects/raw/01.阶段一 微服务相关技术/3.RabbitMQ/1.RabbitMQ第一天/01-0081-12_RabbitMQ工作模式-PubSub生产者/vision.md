# 画面线理解：12_RabbitMQ工作模式-PubSub生产者

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\12_RabbitMQ工作模式-PubSub生产者_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 03:25, 04:57, 05:32, 06:37, 06:57, 07:36, 10:07, 11:45, 13:39, 14:08, 14:37, 15:58, 16:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:37:15

1) 这一组画面整体在讲 RabbitMQ 的 Pub/Sub 订阅模式，通过代码演示如何创建交换机、队列并绑定，实现消息的发布与消费。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PPT 标题“4. RabbitMQ 的工作模式”下的子标题“4.2 Pub/Sub 订阅模式”，并配有模式图：生产者 P -> 交换机 X -> 队列（红色方块）-> 消费者 C1、C2。
画面 2: IDE 中展示 Producer_PubSub.java 代码，包含创建连接、声明队列、发送消息的逻辑，注释说明“交换机名称”、“队列名称”、“routingKey”。
画面 3: IDE 中展示 Producer_PubSub.java 代码，光标位于 exchangeDeclare 方法的参数列表，显示交换机类型和参数。
画面 4: IDE 中展示 Producer_PubSub.java 代码，光标位于创建连接和声明交换机的代码段，注释说明“创建交换机”。
画面 5: IDE 中展示 Decompiled class file 的 Channel.class 源码，高亮显示 exchangeDeclare 方法的多个重载版本。
画面 6: IDE 中展示 Decompiled class file 的 AutorecoveringChannel.class 源码，高亮显示 exchangeDeclare 方法的多个重载版本。
画面 7: IDE 中展示 Producer_PubSub.java 代码，光标位于交换机类型定义处，注释说明 DIRECT、FANOUT、TOPIC、HEADERS 四种类型。
画面 8: IDE 中展示 Producer_PubSub.java 代码，光标位于交换机类型定义处，注释说明 DIRECT、FANOUT、TOPIC、HEADERS 四种类型。
画面 9: IDE 中展示 Producer_PubSub.java 代码，光标位于 queueBind 方法，注释说明“绑定队列和交换机”。
画面 10: IDE 中展示 Producer_PubSub.java 代码，光标位于 queueBind 方法，注释说明“绑定队列和交换机”，并显示代码：channel.queueBind(queueName, exchangeName, "");。
画面 11: IDE 中展示 Producer_PubSub.java 代码，右键菜单弹出，显示“Run 'Producer_PubSub.main()'”选项。
画面 12: IDE 中展示运行结果，终端显示“SLF4J: Failed to load class 'org.slf4j.impl.StaticLoggerBinder'”，并提示“Defaulting to no-operation (NOP) logger implementation”。
画面 13: IDE 中展示 Producer_PubSub.java 代码，光标位于 channel.basicPublish 方法，注释说明“发送消息”，并显示代码：channel.basicPublish(exchangeName, "", basicProperties, null, body.getBytes());。
画面 14: IDE 中展示运行结果，终端显示“Process finished with exit code 0”，表示程序成功执行。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```java
// 1. 创建连接
ConnectionFactory factory = new ConnectionFactory();
// 2. 设置参数
factory.setHost("172.16.98.132"); // 服务器地址
factory.setPort(5672); // 端口，默认是 5672
factory.setVirtualHost("/itcast"); // 虚拟主机，默认是 /
factory.setUsername("heima"); // 用户名，默认是 guest
factory.setPassword("heima"); // 密码，默认是 guest
// 3. 创建连接
Connection connection = factory.newConnection();
// 4. 创建通道
Channel channel = connection.createChannel();
// 5. 声明交换机
channel.exchangeDeclare("test_fanout", "fanout");
// 6. 声明队列
channel.queueDeclare("test_fanout_queue1", true, false, false, null);
// 7. 绑定队列和交换机
channel.queueBind("test_fanout_queue1", "test_fanout", "");
// 8. 发送消息
String body = "日志信息：张三调用了findALL方法...日志级别：info...";
channel.basicPublish("test_fanout", "", null, body.getBytes());
// 9. 关闭资源
channel.close();
connection.close();
```

画面 7:
```java
// 1. 交换机类型
String exchangeName = "test_fanout";
channel.exchangeDeclare(exchangeName, BuiltinExchangeType.FANOUT, true, false, false, null);
// 2. 队列名称
String queueName = "test_fanout_queue1";
// 3. 交换机名称
String exchangeName = "test_fanout";
// 4. 绑定队列和交换机
channel.queueBind(queueName, exchangeName, "");
```

画面 13:
```java
String body = "日志信息：张三调用了findALL方法...日志级别：info...";
channel.basicPublish(exchangeName, "", basicProperties, null, body.getBytes());
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1: PPT 标题“4. RabbitMQ 的工作模式”，子标题“4.2 Pub/Sub 订阅模式”，架构图：生产者 P -> 交换机 X -> 队列（红色方块）-> 消费者 C1、C2。
画面 5: 展示 Channel.class 的源码，包含 exchangeDeclare 方法的多个重载版本。
画面 6: 展示 AutorecoveringChannel.class 的源码，包含 exchangeDeclare 方法的多个重载版本。
画面 7: 展示交换机类型定义，注释说明 DIRECT、FANOUT、TOPIC、HEADERS 四种类型。
画面 8: 展示交换机类型定义，注释说明 DIRECT、FANOUT、TOPIC、HEADERS 四种类型。
画面 9: 展示 queueBind 方法，注释说明“绑定队列和交换机”。
画面 10: 展示 queueBind 方法，注释说明“绑定队列和交换机”，并显示代码：channel.queueBind(queueName, exchangeName, "");。
画面 13: 展示 channel.basicPublish 方法，注释说明“发送消息”，并显示代码：channel.basicPublish(exchangeName, "", basicProperties, null, body.getBytes());。

5) 无。
