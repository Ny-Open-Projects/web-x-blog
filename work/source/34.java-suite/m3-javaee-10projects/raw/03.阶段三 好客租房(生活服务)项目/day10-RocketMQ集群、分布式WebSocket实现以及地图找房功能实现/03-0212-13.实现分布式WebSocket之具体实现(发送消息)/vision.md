# 画面线理解：13.实现分布式WebSocket之具体实现（发送消息）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\13.实现分布式WebSocket之具体实现（发送消息）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:27, 01:08, 01:33, 02:39, 04:05, 05:37, 06:29, 07:09, 07:45, 08:20, 08:54, 09:35, 09:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:19:23

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 RocketMQ，实现消息的发送与状态更新。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 PDF 讲义中“4.2、导入RocketMQ相关依赖”的内容，包含两个 Maven 依赖配置。
画面2: 展示了 PDF 讲义中“4.3、添加SpringBoot配置”的内容，包含 RocketMQ 的配置项。
画面3: 展示了 IntelliJ IDEA 中的 application.properties 文件，其中配置了 Spring Boot 应用名、端口、MongoDB 连接 URI 和 RocketMQ 服务地址及生产者组。
画面4: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含将消息保存到 MongoDB、判断用户是否在线、更新消息状态的逻辑。
画面5: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含 @Autowired 注解注入的 RocketMQ 相关组件。
画面6: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含在用户离线时向 RocketMQ 发送消息的逻辑。
画面7: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含从 TextMessage 中解析消息内容并构建 Message 对象的逻辑。
画面8: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含将消息保存到 MongoDB 的逻辑。
画面9: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含更新消息状态和向 RocketMQ 发送消息的逻辑。
画面10: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含向 RocketMQ 发送消息的逻辑。
画面11: 展示了 IntelliJ IDEA 中 Message.java 文件的代码，其中包含 ObjectId 类的定义。
画面12: 展示了 PDF 讲义中“4.3、添加SpringBoot配置”的内容，包含 onMessage 方法的代码。
画面13: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含处理消息的逻辑。
画面14: 展示了 RocketMQ 控制台页面，显示了主题为 "haoke-im-send-message-topic" 的消息列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client</artifactId>
    <version>4.3.2</version>
</dependency>
```

画面2:
```properties
spring.rocketmq.nameServer=172.16.55.185:9876
spring.rocketmq.producer.group=haoke-im-websocket-group
```

画面3:
```properties
# Spring boot application
spring.application.name = itcast-haoke-im
server.port = 18081
spring.data.mongodb.uri=mongodb://172.16.55.185:27017/testdb
spring.rocketmq.nameServer=172.16.55.185:9876
spring.rocketmq.producer.group=haoke-im-websocket-group
```

画面4:
```java
// 消息保存到MongoDB
message - this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(magJson));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面5:
```java
import java.util.HashMap;
import java.util.Map;
@Component
public class MessageHandler extends TextWebSocketHandler {
@Autowired
private RocketMQTemplate (org.apache.rocketmq.spring.core)
private RocketMQTransactionAnnotationProcessor (org.apache.rocketmq.spring.config)
private RocketMQLocalTransactionListener (org.apache.rocketmq.spring.core)
private RocketMQLocalTransactionState (org.apache.rocketmq.spring.core)
private RocketMQTemplate (org.apache.rocketmq.spring.core)
```

画面6:
```java
// 消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String magJson = MAPPER.writeValueAsString(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(magJson));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
} else {
    // 该用户可能下线，可能在其他的节点中，发送消息到MQ系统
    this.rocketMQTemplate.convertAndSend(destination: "haoke-im-send-message-topic", msgJson);
}
```

画面7:
```java
Long toId = jsonNode.get("toId").asLong();
String msg = jsonNode.get("msg").asText();
Message message = Message.builder()
    .from(UserData.USER_MAP.get(uid))
    .to(UserData.USER_MAP.get(toId))
    .msg(msg)
    .build();
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String magJson = MAPPER.writeValueAsString(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(magJson));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
} else {
    // 该用户可能下线，可能在其他的节点中，发送消息到MQ系统
    this.rocketMQTemplate.convertAndSend(destination: "haoke-im-send-message-topic", msgJson);
}
```

画面8:
```java
// 消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String magJson = MAPPER.writeValueAsString(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(magJson));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
} else {
    // 该用户可能下线，可能在其他的节点中，发送消息到MQ系统
    this.rocketMQTemplate.convertAndSend(destination: "haoke-im-send-message-topic", msgJson);
}
```

画面9:
```java
// 更新消息状态为已读
this.messageDAO.updateMessageState(message.getId(), status: 2);
// 该用户可能下线，可能在其他的节点中，发送消息到MQ系统
this.rocketMQTemplate.convertAndSend(destination: "haoke-im-send-message-topic:SEND_MSG", msgJson);
```

画面10:
```java
// 更新消息状态为已读
this.messageDAO.updateMessageState(message.getId(), status: 2);
// 该用户可能下线，可能在其他的节点中，发送消息到MQ系统
this.rocketMQTemplate.convertAndSend(destination: "haoke-im-send-message-topic:SEND_MSG", msgJson);
```

画面11:
```java
public final class ObjectId implements Comparable<ObjectId>, Serializable {
    private static final long serialVersionUID = 367007998654483072L;
    private static final int LOW_ORDER_THREE_BYTES = 16777215;
    private static final int MACHINE_IDENTIFIER;
    private static final short PROCESS_IDENTIFIER;
    private static final AtomicInteger NEXT_COUNTER = new AtomicInteger(new SecureRandom().nextInt());
    private static final char[] HEX_CHARS = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
    private final int timestamp;
    private final int machineIdentifier;
    private final short processIdentifier;
    private final int counter;
}
```

画面12:
```java
// 更新消息状态为已读
this.messageDAO.updateMessageState(message.getId(), status: 2);
// topic:tags 设置主题和标签
this.rocketMQTemplate.send("haoke-im-send-message-topic:SEND_MSG", msgJson);
```

画面13:
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String magJson = MAPPER.writeValueAsString(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(magJson));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
} else {
    // 该用户可能下线，可能在其他的节点中，
