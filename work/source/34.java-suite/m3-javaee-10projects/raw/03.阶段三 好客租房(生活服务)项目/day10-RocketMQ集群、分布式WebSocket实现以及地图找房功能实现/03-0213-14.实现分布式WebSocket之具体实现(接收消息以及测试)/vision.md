# 画面线理解：14.实现分布式WebSocket之具体实现（接收消息以及测试）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\14.实现分布式WebSocket之具体实现（接收消息以及测试）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:42, 01:21, 02:16, 03:14, 04:19, 05:32, 06:10, 06:58, 08:23, 09:27, 09:57, 11:29, 12:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:20:16

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 RocketMQ 的分布式 WebSocket 消息推送系统，重点展示消息处理逻辑、会话管理、消息状态更新及 RocketMQ 消息发送。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 MessageHandler.java 中的代码，当用户可能下线时，更新消息状态并发送消息到 RocketMQ 主题 "haoke-im-send-message-topic:SEND_MSG"。
画面 2: 显示 MessageHandler.java 的类定义，包含 @Component、@RocketMQMessageListener 注解，以及 @Autowired 注入的 messageDAO 和 rocketMQTemplate。
画面 3: 显示 @RocketMQMessageListener 注解的配置，指定 topic 为 "haoke-im-send-message-topic"，selectorExpression 为 "SEND_MSG"。
画面 4: 显示 MessageHandler 类的 afterConnectionEstablished 方法，用于将用户 session 存入 SESSIONS 映射表。
画面 5: 显示 RocketMQ 控制台，查询主题 "haoke-im-send-message-topic" 下的消息，显示两条消息记录。
画面 6: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 7: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 8: 显示调试器断点，正在执行 onMessage 方法，变量 msg 正在被解析。
画面 9: 显示 Simple WebSocket Client 页面，用户发送消息后，消息日志中显示接收方收到消息。
画面 10: 显示 application.properties 文件，其中包含消息保存到 MongoDB 的配置。
画面 11: 显示调试器断点，正在执行 onMessage 方法，变量 msg 正在被解析。
画面 12: 显示 onMessage 方法中，解析消息 JSON，获取 toId，判断用户是否在线，若在线则发送消息，否则更新消息状态并发送到 RocketMQ。
画面 13: 显示 PPT 页面，标题为“4.1、实现方案”，图示了 socket 客户端与 socket 服务端的交互，服务端通过 Map(session) 管理会话，并订阅消息系统。
画面 14: 显示 Simple WebSocket Client 页面，用户发送消息后，消息日志中显示接收方收到消息，验证消息系统已生效。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
this.messageDAO.updateMessageState(message.getId(), status: 2);
}else{
    //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
    //需求：添加tag，便于消费者对消息的筛选
    this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
```

画面 2:
```java
import cn.itcast.haoke.im.pojo.UserData;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.rocketmq.spring.annotation.RocketMQMessageListener;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.TextWebSocketHandler;
import java.util.HashMap;
import java.util.Map;
@Component
@RocketMQMessageListener(
        topic = "haoke-im-send-message-topic",
        selectorExpression = "SEND_MSG",
        messageModel = MessageModel.CLUSTERING
)
public class MessageHandler extends TextWebSocketHandler implements RocketMQListener<String> {
    @Autowired
    private MessageDAO messageDAO;
```

画面 3:
```java
@RocketMQMessageListener(
        topic = "haoke-im-send-message-topic",
        selectorExpression = "SEND_MSG",
        messageModel = MessageModel.CLUSTERING
)
```

画面 4:
```java
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    //将当前用户的session就置到map中，后面会使用相应的session通信
    SESSIONS.put(uid, session);
}
```

画面 6:
```java
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        long toId = jsonNode.get("to").get("id").longValue();
        //判断用户是否在线
        WebSocketSession toSession = SESSIONS.get(toId);
        if (toSession != null && toSession.isOpen()) {
            //TODO 具体格式需要和前端对接
            toSession.sendMessage(new TextMessage(msg));
        }else{
            //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
            //需求：添加tag，便于消费者对消息的筛选
            this.messageDAO.updateMessageState(message.getId(), status: 2);
            this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
        }
    }catch (Exception e) {
        e.printStackTrace();
    }
}
```

画面 7:
```java
try {
    JsonNode jsonNode = MAPPER.readTree(msg);
    long toId = jsonNode.get("to").get("id").longValue();
    //判断用户是否在线
    WebSocketSession toSession = SESSIONS.get(toId);
    if (toSession != null && toSession.isOpen()) {
        //TODO 具体格式需要和前端对接
        toSession.sendMessage(new TextMessage(msg));
    }else{
        //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
        //需求：添加tag，便于消费者对消息的筛选
        this.messageDAO.updateMessageState(message.getId(), status: 2);
        this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
    }
} catch (Exception e) {
    e.printStackTrace();
}
```

画面 10:
```properties
#将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
String mqJson = MAPPER.writeValueAsString(message);
//判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    //TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(mqJson));
}
```

画面 12:
```java
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        long toId = jsonNode.get("to").get("id").longValue();
        //判断用户是否在线
        WebSocketSession toSession = SESSIONS.get(toId);
        if (toSession != null && toSession.isOpen()) {
            //TODO 具体格式需要和前端对接
            toSession.sendMessage(new TextMessage(msg));
        }else{
            //该用户可能下线，可能在其他的节点中，发送消息到MQ系统
            //需求：添加tag，便于消费者对消息的筛选
            this.messageDAO.updateMessageState(message.getId(), status: 2);
            this.rocketMQTemplate.convertAndSend ( destination: "haoke-im-send-message-topic:SEND_MSG", msg);
        }
    }catch (Exception e) {
        e.printStackTrace();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13:
标题：4.1、实现方案
架构图：
- 左侧：socket 客户端（多个圆形代表客户端）
- 中间：socket 服务端（包含三个 Map(session) 模块）
- 右侧：消息系统
- 箭头：从 socket 客户端指向 socket 服务端，标注“发送消息”；从 socket 服务端指向消息系统，标注“订阅”。

画面 14:
标题：5、地图找房
表格数据：
- 表格标题：消息日志
- 表格内容：
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:1003,username":"wong"}
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:1003,username":"wong"}
  - 时间：10:34:02
  - 消息内容：{"id":"5c1df024757f73648a5c4b0c","msg":"在吗","status":1,"sendDate":"154546892548","toId":"null","from":"id:100
