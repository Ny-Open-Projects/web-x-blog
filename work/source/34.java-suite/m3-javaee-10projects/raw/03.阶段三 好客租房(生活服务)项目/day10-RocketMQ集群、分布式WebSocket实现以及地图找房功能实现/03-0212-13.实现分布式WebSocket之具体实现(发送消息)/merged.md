# 13.实现分布式WebSocket之具体实现（发送消息）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\13.实现分布式WebSocket之具体实现（发送消息）【海量资源尽在 ubkz.com】.mp4
- 时长 10分12秒（音频 612s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面我们就来做具体的一个实现那么首先呢我们需要先来打开我们的这个工程啊那么咱们先把这个刚刚所测试的一些这个都给它停掉好那么我们来打开我们的IM那个工程打开这个IM就在这打开它哎OK那么打开之后啊打开之后呢我们首先需要
[00:25] 给他去添加我们的依赖添加什么依赖呢是不是添加我们的RogatMQ相关的一些依赖因为我们在这个里面要用到的是不是就是我们这个消息啊对吧好那么我们丢到这个位置吧把它丢过来那么有了这个依赖之后呢我们紧接着还需要给他添加一个配置那么添加一个什么配置来看一下把这两个是不是靠过来那么一个呢去指定我们Nameserver的一个地址另外一个呢去指定我们的一个Produced Grip
[00:55] OK是一个分组那我们来看一下这个分组的名字叫做浩克IM WebSocket Group就做这样的一个分组那么OK好那么到这里呢我们这个配置是不是基本上就实现了那么接下来呢我们就需要去按照刚刚我们所分析的这个原理这个逻辑去做一个具体的一个实现那么我们就要回到我们的这个WebSocket下面有一个MessageHunter那么具体的业务逻辑是不是都在这个里面去做一个实现啊
[01:25] 对吧那么我们去向我们的这个发消息的时候就A用户给B用户发的时候那么逻辑是不是在这里你看在这个位置做了一个判断就判断这个to这个session不等于空并且这个to这个session is open的时候是不是向他去发送这个消息对吧那么我们是不是可以加一个else如果没有就当前这个JVM里面没有这个用户那么是不是该用户
[01:55] 可能下线对吧有可能下线了也有可能是什么呢可能是在其他的这个节点中对不对这有个错别字叫可能对吧可能在可能在其他的节点中那么我们是不是就需要去发送消息对吧就要发送消息到我们的这个MQ系统那么我们又该如何去发送消息呢
[02:28] 那么在这个位置我们是不是直接去注入注入谁呢刚刚我们所写的那个叫做RocketMQMQtemplate模板把这个模板注进来把模板注进来是不是我们就可以去发送消息了对吧那么发送什么消息呢我们可以看一下叫RocketMQtemplate.是不是有一个叫做ConvertAnd Send是不是去做这样的一个
[02:58] 发送网对吧发送这个消息那么需要有两个内容需要有两个内容一个呢就是我们的一个目标topic另外一个呢就是说我们发送的消息的具体的一个内容好那么我们这个topic呢我们就给他叫做什么呢就叫浩克浩克-im然后呢我们来给他的一个就是叫比如说send然后呢messagesend message然后呢topic
[03:28] 这是我们的一个topic对吧然后呢我们需要去给他发一个我们的一个消息去做一个发送一个消息这个消息他显然呢肯定是需要去做一个把我们这个match对象是不是去做一个序列化那么在这个位置是不是也做了一个序列化那么我们是不是可以这么来玩把上面这个统一去让他去做一个序列化那么他的返回值呢我们可以把它作为是一个叫做json
[03:57] 叫msg叫jasonok然后呢去他是做这样的一个发送那么我们下面这个位置是不是也可以去做这样的一个发送对吧来拷贝一下做这样的一个发送ok那么这个是不是就已经完成了一个发送对吧但是呢这个地方呢我们其实有这样的一个需求就是发送消息的时候呢我们希望他去跟一个什么呢去跟一个
[04:27] 我们的或者说去添加一个我们的一个Tag添加一个Tag就是添加一个Tag那么为什么要去添加Tag呢是不是我们便于便于我们其他的便于我们的消费者的一个对消息的一个筛选对不对消费者对消息的一个筛选筛选筛选OK那么问题来了在我们的这个Square去发这个消息的时候
[04:58] 那么如何添加一个tag呢是这样来添加啊那么是通过在这个位置有个冒号注意啊是前面的这个topic然后后面来一个冒号比如说我们tag叫什么呢send messageOK比如说这个就是我们的一个tag前面这个就是一个topic好那么这样的话呢我们是不是就已经完成了一个消息的一个发送那么接下来呢我们来做一个测试看一下我们
[05:26] 给未在线的用户就说不是未在线啊是他不是在这个我们当前这个JVM里面的用户去发消息那么去走这个逻辑啊好那么下面呢我们在这个位置吧我们还是去打一个断点我们来debug启动一下启动一下我们这个工程然后呢我们来做一个测试啊那么我们找到他吧然后debug启动走那么等待他的一个启动
[05:51] 我们这个服务呢就跑起来了那么跑起来之后呢我们去打开我们的两个测试的工具一个呢是我们安装的一个这个插件对吧另外一个呢就是在线的这样的工具那我们来测一下比如说我们把它拷贝一下那么这个呢我们去打开要注意端口呢是18081然后呢我们连接的是1001我们这个用户轴OK到这儿是不是已经连接成功了我们去发一个消息那我们来看这个消息的内容是什么内容呢
[06:20] 在我们之前的这个代码中我们来看一下它呢是有两个内容对吧通过我们这个消息然后呢去拿到两个就是to id一个是message就是你要发给谁呢我们写一个这个json然后呢我们去写一个这个改成英文然后呢to id我要发给比如说1003这个用户我发给1003或者1002都行啊然后呢我这个message内容是怎么呢
[06:48] 我写一个叫你好你好你好在吗OK我发这样的消息然后点击发送走那么可以看到我们这个消息逻辑是不是就走到这来了对吧然后往下面走走走走看一下当前用户在不在线并不在线并不在当前JVM里面因为他并也不知道在不在线是吧所以我就去选择去发消息到我的RockMQ中然后通过走
[07:17] 那我这个消息是不是就已经发送完成了对吧发送完成那么我进入到进入到我们这个控制台来看一下那我们还是刷新一下找到我们那个topic叫什么topic呢看一下就叫浩克im send messenger这个topic找一下找到浩克是不是就这他呀点击一下来看一下那么可以看到这个是不是就是我们的消息对吧消息ID然后呢tag是不是也添加上来了这个tag是不是刚刚我们在
[07:45] 在我们的这个位置通过一个冒号后面是不是添加一个这个tag叫sendmessage然后我们点击它的消息的一个内容那么消息的内容是不是就是长这个样子对吧长这个样子就说这个你好在吗你好在吗当然了这个里面还是稍微有一点点问题的就是我们发出了这个消息这个ID我们看到它其实是什么样的来看一下
[08:12] 这个ID有点问题就是我们这个match对象我们定义的这个ID是一个object ID他把这个object对象也做了一个这个序列化其实我们不需要他去做这样的序列化我们只需要拿到他的一个具体的一个值是不是就可以了因为这个在mongoDB里面我们一个拿到他是一个支付创对吧这个支付创就OK了OK好那么我们接下来先把这个问题我们处理一下那么处理完成之后下面我们是不是就开始编写我们的消费者对不对
[08:42] 好那么我们先把这个问题来处理一下来看一下他是该如何去做一个处理呢那么我们是需要给我们这个ID去添加一个注解添加什么注解呢我们来看一下在我们的讲义中有这样的一个注解先把它丢过来那么有这样的一个注解就是说我们去指定它的一个序列化的方式让它在序列化的时候呢去给我们序列化成一个字符串就可以了那么没必要是说把整个对象
[09:08] 去做一个序列化那么OK那么我们再次重启我们这个服务我们再去做一个测试看他发出的消息将会是怎么样的消息那么我们现在已经启动起来了那么我们来再去做一个测试就是我们还是去连接到我们的他就是说你好给1003去发一个消息就你好在吗你好1我们就随便来写一个然后发送走然后往下面走走走走走走
[09:37] 那么我们通过走然后呢我们来回到我们的这个控制台来看一下是不是又多了一条消息啊那么我们来看最新的一条消息走来看一下那么你可以看到这个ID是不是就正常了对吧就拿到这个ID的这个值那么就OK了好嘞那么这个呢就是这个就是我们这个发送消息我们是不是基本上呢就已经搞定了那么接下来我们要去
[10:03] 处理的问题就是我们的一个消息的一个消费对不对好那么我们关于发动消息我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 RocketMQ，实现消息的发送与状态更新。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 PDF 讲义中“4.2、导入RocketMQ相关依赖”的内容，包含两个 Maven 依赖配置。
画面2: 展示了 PDF 讲义中“4.3、添加Spring Boot配置”的内容，包含 RocketMQ 的配置项。
画面3: 展示了 IntelliJ IDEA 中的 application.properties 文件，其中配置了 Spring Boot 应用名、端口、MongoDB 连接 URI 和 RocketMQ 服务地址及生产者组。
画面4: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含将消息保存到 MongoDB、判断用户是否在线、更新消息状态的逻辑。
画面5: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含 @Autowired 注解注入的 RocketMQ 相关组件。
画面6: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含在用户离线时向 RocketMQ 发送消息的逻辑。
画面7: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含从 TextMessage 中解析消息内容并构建 Message 对象的逻辑。
画面8: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含将消息保存到 MongoDB 的逻辑。
画面9: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含更新消息状态和向 RocketMQ 发送消息的逻辑。
画面10: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含向 RocketMQ 发送消息的逻辑。
画面11: 展示了 IntelliJ IDEA 中 Message.java 文件的代码，其中包含 ObjectId 类的定义。
画面12: 展示了 PDF 讲义中“4.3、添加Spring Boot配置”的内容，包含 onMessage 方法的代码。
画面13: 展示了 IntelliJ IDEA 中 MessageHandler.java 文件的代码，其中包含处理消息的逻辑。
画面14: 展示了 RocketMQ 控制台页面，显示了主题为 "haoke-im-send-message-topic" 的消息列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-client</artifactId>
    <version>4.3.2</version>
</dependency>
```

画面2:
```properties
spring.RocketMQ.nameServer=172.16.55.185:9876
spring.RocketMQ.producer.group=haoke-im-WebSocket-group
```

画面3:
```properties
# Spring boot application
spring.application.name = itcast-haoke-im
server.port = 18081
spring.data.mongodb.uri=mongodb://172.16.55.185:27017/testdb
spring.RocketMQ.nameServer=172.16.55.185:9876
spring.RocketMQ.producer.group=haoke-im-WebSocket-group
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
private RocketMQTemplate (org.apache.RocketMQ.spring.core)
private RocketMQTransactionAnnotationProcessor (org.apache.RocketMQ.spring.config)
private RocketMQLocalTransactionListener (org.apache.RocketMQ.spring.core)
private RocketMQLocalTransactionState (org.apache.RocketMQ.spring.core)
private RocketMQTemplate (org.apache.RocketMQ.spring.core)
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

