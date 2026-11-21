# 画面线理解：25.实现微聊系统之实现WebSocket的业务逻辑

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\25.实现微聊系统之实现WebSocket的业务逻辑【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:30, 05:21, 06:46, 08:40, 11:00, 12:07, 13:19, 14:18, 15:39, 16:52, 18:09, 19:12, 20:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:49:39

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 WebSocket 的即时通讯（IM）服务端实现，包括消息处理、会话管理、拦截器配置和调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 MessageHandler 类的代码，定义了 @Component 注解、私有属性 messageDAO 和 SESSIONS，以及 afterConnectionEstablished 方法用于获取用户 ID。
画面2：展示 IM 服务的流程图，用户A发送消息到 IM 服务器，服务器存入 MongoDB 消息表，然后判断用户B是否在线，若在线则发送给用户B。
画面3：在 IntelliJ IDEA 中创建 MessageHandshakeInterceptor 类。
画面4：展示 MessageHandshakeInterceptor 类的代码，实现 beforeHandshake 方法，用于校验路径并设置用户 ID。
画面5：展示 ImApplication 启动类的代码，使用 @SpringBootApplication 注解。
画面6：展示 MessageHandler 类中 handleTextMessage 方法的代码，用于处理文本消息，包括保存到 MongoDB、判断接收方是否在线、发送消息和更新消息状态。
画面7：展示 WebSocketConfig 配置类的代码，配置 WebSocketHandler 和拦截器。
画面8：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。
画面9：展示应用启动日志，显示 Tomcat 成功启动。
画面10：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。
画面11：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 session 和 msg 的值。
画面12：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 jsonNode 和 msg 的值。
画面13：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 session 和 msg 的值。
画面14：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import cn.itcast.haoke.im.pojo.UserData;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import java.util.HashMap;
import java.util.Map;

@Component
public class MessageHandler extends TextWebSocketHandler {
    @Autowired
    private MessageDAO messageDAO;
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final Map<Long, WebSocketSession> SESSIONS = new HashMap<>();

    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        Long uid = (Long) session.getAttributes().get("uid");
        // 更新消息状态为已读
    }
}
```

画面2：
无代码，为流程图。

画面3：
```java
package cn.itcast.haoke.im.websocket;
public class MessageHandshakeInterceptor {
```

画面4：
```java
public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler handler, Map<String, Object> attributes) {
    String path = request.getURI().getPath();
    String[] ss = StringUtils.split(path, '/');
    if (ss.length != 2) {
        return false;
    }
    if (!StringUtils.isNumeric(ss[1])) {
        return false;
    }
    attributes.put("uid", Long.valueOf(ss[1]));
    return true;
}
```

画面5：
```java
package cn.itcast.haoke.im;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ImApplication {
    public static void main(String[] args) {
        SpringApplication.run(ImApplication.class, args);
    }
}
```

画面6：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面7：
```java
import org.springframework.context.annotation.Configuration;
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MessageHandler messageHandler;
    @Autowired
    private MessageHandshakeInterceptor messageHandshakeInterceptor;

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(this.messageHandler, "/ws").addInterceptors(this.messageHandshakeInterceptor);
    }
}
```

画面8：
无代码，为客户端界面。

画面9：
无代码，为启动日志。

画面10：
无代码，为客户端界面。

画面11：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面12：
```java
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage textMessage) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    JsonNode jsonNode = MAPPER.readTree(textMessage.getPayload());
    String msg = jsonNode.get("msg").asText();
    Message message = Message.builder()
            .from(UserData.USER_MAP.get(uid))
            .to(UserData.USER_MAP.get(toId))
            .msg(msg)
            .build();
}
```

画面13：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面14：
无代码，为客户端界面。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
架构图：
- 用户A → 发送消息 → IM服务器
- IM服务器 → 存入 MongoDB 消息表
- MongoDB 消息表 → 判断用户B是否在线
- 用户B在线 → 发送给用户B
- 用户B不在线 → 标记为已读

画面8：
无 PPT 标题或表格数据。

画面14：
无 PPT 标题或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
