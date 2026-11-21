# 23-WebSocket-消息生产和消费测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们把这一块进行一个测试

那么测试这一块呢

等会儿我们将实现这么两个操作

第一个就是客户端给我发消息了

那我要给客户端回一下消息

另外一个我要通过用户的一个ID

给指定的用户发消息过去

好那这一块怎么做呢

我们先在这里创建一个控制器

在当前这个控制器这里给用户发消息

这里写个叫resetControllerRequestMapping

value我就写个message

这里呢我就写一个发送消息的一个方法

写个public试验叫send

那你总要把这个消息给我是不是

我就写个msg

那还有一个你要给我这个用户的信息

userID

你总得告诉我给哪个用户发送

对不对

好写个getMapping

value就写个叫做userID

就可以了

然后我们这里返回的就随意返回一下

返回个OK吧

接着我们就是调这一块

它的一个方法就行了

把它给注入进来

privity叫webSocketServer

把它直接给注入进来

注入进来我们开始发送一下消息

点send message

msg给它

userID给它

这一块发消息就搞定了

这是我后端主动给客户端发消息

那接着我们这一块呢

还有一个就是接到用户消息

我给用户回复消息

那怎么回复呢

send.getBasicRemote.sendTax

回一个什么

你给我发什么了

我就给你回什么

收到的消息

message就可以了

好我们启动运行测试一下

那么这个时候

我测试了在这一块

我需要有两个对应的一个页面

在我这里已经提供了两个页面

第一个叫做webSocket的页面

这个其实就是我们当前张三的用户

请求地址是loghost18088ws张三

这表示是张三的客户端

还有另外一个

这个我们也看一下webSocket的ws李氏

这是李氏的客户端

我们用这两个客户端来测试一下

我们用这两个客户端来测试一下

我们用这两个客户端来测试一下

我们用这两个客户端来测试一下

我们用这两个客户端来测试一下

我们用这两个客户端打开

然后我们实现一下

分别向服务端去发送消息

好 我们来开一下这两个客户端

把这个打开

这个是我们的李氏

我们新开一个别的窗口

那么别的窗口是哪一个窗口呢

我们简单看一下

新的窗口就是做这么一个事情

一会儿我要向指定的用户发送消息

就要调这个方法 对不对

行 我们先再看一个

这个一个

这个一个

这个一个

这个一个

这个给弄出来

这个是李氏

这个是张三

对吧

行 这个是我们等会儿要发消息的一个地址

那么发消息的地址呢

我们写一下

是http localhost

你要给谁发呢

18088

w

叫做message

张三

message给你

message给你

好喽

这是一会儿我要发送的

行 我们来开始测试一下

把这个打开

这个也打开

注意这个时候

它是我们的李氏

它是我们的张三 对不对

我们开始实现这个消息的操作

这一块先刷新一次

来 发一下消息

哈喽 这个发了

这个也发一下

就是发个叫做你好

你好

发下消息

发了行

这个都可以的

我们接着开始给指定的用户发消息

现在是给张三发消息

对不对

咱们输入一下这个地址

张三

你看张三收到了吧

把这个换一下

换成谁了

换成我们的李氏

李氏发了消息

换一下

换成李氏

李氏吗

回测一下

发过来了

对吧

这是展这一块

非常简单

行

这个就是我们

这个扣端的这个项目

这个客户端和服务端通信的一个测试

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于使用 Spring Boot 和 WebSocket 实现一个简单的实时消息通信系统的教学内容。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个 WebSocket 服务端（`WebSocketServer`），并将其与一个 HTTP 控制器（`MessageController`）集成，以便通过浏览器前端发送和接收消息。核心内容包括：
- 在 `WebSocketServer` 中定义 `@OnMessage`、`@OnOpen`、`@OnClose` 和 `@OnError` 四个事件处理方法。
- 在 `MessageController` 中使用 `@Autowired` 注入 `WebSocketServer` 实例，并通过 `@RequestMapping` 定义一个 HTTP 接口，用于接收前端发送的消息并转发给 WebSocket 服务端。
- 通过浏览器访问前端页面，模拟两个用户（如用户ID为 `haha1` 和 `haha2`）进行消息收发，验证系统功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断每个画面对应的具体时间点，以下章节是根据画面内容和逻辑顺序进行的划分：

- **章节 1: 项目结构与 WebSocket 服务端代码 (0:00 - 0:15)**
  - 展示项目结构，重点在 `seckill-websocket` 模块。
  - 代码焦点在 `WebSocketServer.java`，演示 `onMessage` 方法用于接收客户端消息并打印日志。

- **章节 2: 定义 WebSocket 服务端事件处理方法 (0:15 - 0:30)**
  - 展示 `WebSocketServer.java` 中的 `onOpen`、`onClose`、`onError` 方法。
  - 代码中包含注释，说明这些方法的作用。

- **章节 3: 创建消息控制器并注入 WebSocket 服务端 (0:30 - 0:45)**
  - 在 `MessageController.java` 中，使用 `@Autowired` 注入 `WebSocketServer`。
  - 代码中定义了 `send` 方法，用于接收 HTTP 请求并调用 `WebSocketServer` 的 `sendMessage` 方法。

- **章节 4: 配置 WebSocket 服务端并启动应用 (0:45 - 1:00)**
  - 在 `WebSocketApplication.java` 中，配置 `ServerEndpointExporter` Bean。
  - 启动 Spring Boot 应用，观察控制台输出。

- **章节 5: 前端页面演示与消息收发 (1:00 - 1:15)**
  - 展示浏览器中打开的前端页面。
  - 演示两个浏览器窗口分别输入消息并发送，验证消息能够被对方接收。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容：

- **`WebSocketServer.java` (服务端核心代码)**
  ```java
  @Component
  public class WebSocketServer {

      private static final Map<String, Session> sessionMap = new ConcurrentHashMap<>();

      @OnMessage
      public void onMessage(String message, Session session) throws IOException {
          System.out.println("用户: " + idMap.get(session.getId()) + "，接收到的信息是：" + message);
          // 将消息发送给所有连接的客户端
          for (Session s : sessionMap.values()) {
              if (!s.equals(session)) {
                  s.getBasicRemote().sendText(message);
              }
          }
      }

      @OnOpen
      public void onOpen(Session session, EndpointConfig config) {
          String userId = session.getId();
          sessionMap.put(userId, session);
          System.out.println("用户 " + userId + " 连接成功");
      }

      @OnClose
      public void onClose(Session session, CloseReason reason) {
          String userId = session.getId();
          sessionMap.remove(userId);
          System.out.println("用户 " + userId + " 断开连接");
      }

      @OnError
      public void onError(Session session, Throwable throwable) {
          System.out.println("用户: " + idMap.get(session.getId()) + "，通信发生了异常：" + throwable.getMessage());
      }

      public void sendMessage(String message, String userId) throws IOException {
          Session session = sessionMap.get(userId);
          if (session != null) {
              session.getBasicRemote().sendText(message);
          }
      }
  }
  ```

- **`MessageController.java` (控制器代码)**
  ```java
  @RestController
  @RequestMapping("/websocket")
  public class MessageController {

      @Autowired
      private WebSocketServer webSocketServer;

      @RequestMapping(value = "/send", method = RequestMethod.GET)
      public String send(@PathVariable(value = "userId") String userId, String msg) throws IOException {
          webSocketServer.sendMessage(msg, userId);
          return "OK";
      }
  }
  ```

- **`WebSocketApplication.java` (启动类)**
  ```java
  @SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
  public class WebSocketApplication {

      @Bean
      public ServerEndpointExporter serverEndpointExporter() {
          return new ServerEndpointExporter();
      }

      public static void main(String[] args) {
          SpringApplication.run(WebSocketApplication.class, args);
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景 1: 服务端消息接收与广播**
  - 讲师在 `WebSocketServer.java` 中演示 `onMessage` 方法。
  - 代码中使用 `session.getBasicRemote().sendText(message)` 将收到的消息广播给所有其他连接的客户端。
  - 通过控制台输出，验证消息被正确接收和处理。

- **场景 2: 前端页面交互**
  - 讲师打开浏览器，访问前端页面。
  - 在两个不同的浏览器窗口中，分别输入消息并点击“发送”按钮。
  - 演示消息如何从一个客户端发送到另一个客户端，验证 WebSocket 的实时通信能力。

- **场景 3: 服务端事件处理**
  - 讲师演示 `onOpen` 方法，当客户端连接时，将 `Session` 对象存入 `sessionMap`。
  - 演示 `onClose` 方法，当客户端断开连接时，从 `sessionMap` 中移除对应的 `Session`。
  - 通过控制台输出，验证连接和断开事件的触发。

- **场景 4: 控制器与服务端集成**
  - 讲师在 `MessageController.java` 中，通过 `@RequestMapping` 定义一个 HTTP 接口。
  - 通过 `@Autowired` 注入 `WebSocketServer`，并调用其 `sendMessage` 方法。
  - 通过浏览器访问该接口，验证 HTTP 请求能够触发 WebSocket 服务端的消息发送。

- **场景 5: 应用启动与调试**
  - 讲师在 IntelliJ IDEA 中运行 `WebSocketApplication.java`。
  - 观察控制台输出，确认应用成功启动。
  - 通过 `Run Dashboard` 查看应用的运行状态和端口信息。

---

以上是根据视频画面进行的结构化技术课程分析。
