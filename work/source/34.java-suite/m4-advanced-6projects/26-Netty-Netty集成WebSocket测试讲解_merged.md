# 26-Netty-Netty集成WebSocket测试讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接下来启动测试一下看看效果怎么样

好我们启动一下

等它启动

启动之后我们就开始去访问一下那几个websocket的页面

但是一定要记住我们这一块它的端口变了

端口这一块是28082

对不对

这是这一个

我们来把这个给改一下

改成28082

行

这个是张三的

我们再来改李氏的

这个是28082

好我们开始把页面打开

这是这个页面

这是这个页面

这两个页面呢

把它给拆开

好我们还要拆一个页面来

我们来看一下这一块

这个先去刷新一次

这个再去刷新一次

这有两个刷新一次

我输入一下hello

好点击发送消息

你看收到了吧

这个也是一样

也输入一个hello

多加几个感叹发送一次

也是成功的

对不对

我们接着开始去做这么一个事情

就是去主动给某一个用户发消息

那么主动给某一个用户发消息

这一块地址各方面都是不会变化的

我们来试一下

回车一次

我们看一下

这个时候给谁发送了

这个来整个叫做张三

对吧

那个叫张三

UUID

回车一次

看谁发送了

好这个刷新一次

行

我再刷新一次

这个是不是有问题

我们看一下这里是怎么走的

来再来刷新一次

好过来了

我们看一下过来的

这个时候注意我们会去获取张三的一个绘画

对不对

那么张三的一个绘画很明显

是不是为空

为空说明什么问题

说明我们上面这一块哪里有问题

对不对

我们看一下这个sysmap

这是这一块sysmap

好我们先整一个

这个是张三来刷新一次过来

过来之后我们看看这个UserID

这个UserID咱们是不是获取为空

那么UserID获取为空怎么看呢

怎么去处理呢

我们在这一块

我们整一个password

写个value

等于UserID

这后面直接去接就行了

行了就不需要这么多事情了

对不对

这个就非常简单了

行

我们再来测试一次

看看效果如何好

等它启动

启动之后呢

我们再来测试一次

重新建立连接过来了

这个UserID是张三的

对不对

这个时候就放大过去

那么其他的我们都不去管了

来发一个消息

哈喽好

发送成功

这个了

我们来刷新一次

来个demo

发送一次可以了

我现在给当前张三发送

那么张三这一块呢

来个UID回测一次

UID过来了

我们给谁发了

给另外一个叫李氏

也过去了

那咱们这一块也就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是一节关于使用 Spring Boot 和 Netty 实现 WebSocket 服务端的实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个支持用户会话管理的 WebSocket 服务。核心内容包括：
- 项目结构与依赖配置（`pom.xml` 和 `bootstrap.yml`）。
- 服务端核心代码实现，包括 `@OnOpen` 和 `@OnMessage` 事件处理器。
- 使用 `Map<String, Session>` 本地存储用户会话。
- 利用 Spring Data Redis 将用户会话信息持久化到 Redis 中，以实现会话的跨服务或跨实例共享。
- 通过浏览器访问 WebSocket 服务并进行消息收发的演示。

整个过程旨在教授开发者如何构建一个可扩展、可管理的实时通信服务。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的绝对时间点，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**: 视频开场，显示桌面和“黑马程序员”、“博学谷”的Logo，介绍课程来源。
- **00:05 - 00:15**: 讲师打开 IntelliJ IDEA，展示项目结构，重点是 `NettyWebSocketApplication.java` 文件，准备进行代码编写。
- **00:15 - 00:30**: 讲师在 `bootstrap.yml` 文件中配置 WebSocket 服务的端口（`port: 28082`）和主机（`host: 0.0.0.0`），并配置了 Nacos 服务发现。
- **00:30 - 00:45**: 讲师在 `NettyWebSocketServer.java` 中编写 `@OnOpen` 方法，用于建立用户会话并将其存储在 `sessionMap` 中。
- **00:45 - 01:00**: 讲师在 `NettyWebSocketServer.java` 中编写 `@OnMessage` 方法，用于接收客户端消息并根据用户 ID 发送回消息。
- **01:00 - 01:15**: 讲师在 `NettyWebSocketServer.java` 中添加了使用 Redis 持久化会话的代码，通过 `redisTemplate.boundHashOps` 将 `Session` 对象存储到 Redis 中。
- **01:15 - 01:30**: 讲师启动服务，通过浏览器访问 `localhost:28082`，并打开一个新标签页访问 `localhost:18088/message`，演示消息收发。
- **01:30 - 01:45**: 讲师在 `MessageController.java` 中编写了用于发送消息的接口，并在 `NettyWebSocketServer.java` 中调用该接口来发送消息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### 代码关键内容：

- **`NettyWebSocketApplication.java` (启动类)**：
  ```java
  @SpringBootApplication
  public class NettyWebSocketApplication {
      public static void main(String[] args) {
          SpringApplication.run(NettyWebSocketApplication.class, args);
      }
  }
  ```

- **`bootstrap.yml` (配置文件)**：
  ```yaml
  discovery:
    nacos-server:
      server-addr: nacos-server:8848
  main:
    allow-bean-definition-overriding: true
  redis:
    cluster:
      nodes:
        - redis-server:7001
        - redis-server:7002
        - redis-server:7003
        - redis-server:7004
        - redis-server:7005
        - redis-server:7006
  ws:
    port: 28082
    host: 0.0.0.0
  ```

- **`NettyWebSocketServer.java` (服务端核心)**：
  ```java
  @Component
  public class NettyWebSocketServer {

      private static Map<String, Session> sessionMap = new HashMap<>();

      @Autowired
      private RedisTemplate redisTemplate;

      @OnOpen
      public void onOpen(@PathVariable Map<String, String> pathMap, Session session) {
          String userId = pathMap.get("userid");
          String id = session.channel().id().toString();
          Session userSession = sessionMap.get(userId);
          if (userSession != null) {
              // 清理会话信息
              sessionMap.remove(userId);
              redisTemplate.boundHashOps(key: "NettyWebSocketUser").delete(userSession.channel().id().toString());
              // 存储用户会话信息
              sessionMap.put(userId, session);
              redisTemplate.boundHashOps(key: "NettyWebSocketUser").put(id, userId);
          }
      }

      @OnMessage
      public void sendMessage(String message, String userId) {
          Session session = sessionMap.get(userId);
          if (session != null) {
              session.sendText(message);
          }
      }
  }
  ```

#### 公式与图表：

- **无公式或复杂图表**。视频主要通过代码和运行日志进行演示。

---

### 4) 关键场景与演示描述

- **场景一：项目初始化与配置** (00:05 - 00:30)
  - 讲师在 IntelliJ IDEA 中打开项目，展示 `NettyWebSocketApplication.java` 和 `bootstrap.yml` 文件。
  - 在 `bootstrap.yml` 中，讲师配置了服务端口为 `28082`，并配置了 Redis 集群和 Nacos 服务发现。

- **场景二：服务端核心代码编写** (00:30 - 01:15)
  - 讲师在 `NettyWebSocketServer.java` 中编写 `@OnOpen` 方法，用于建立用户会话并存储在 `sessionMap` 中。
  - 讲师编写 `@OnMessage` 方法，用于接收客户端消息并根据用户 ID 发送回消息。
  - 讲师添加了使用 Redis 持久化会话的代码，通过 `redisTemplate.boundHashOps` 将 `Session` 对象存储到 Redis 中。

- **场景三：服务启动与浏览器访问** (01:15 - 01:30)
  - 讲师启动服务，通过浏览器访问 `localhost:28082`。
  - 讲师打开一个新标签页访问 `localhost:18088/message`，并输入消息进行测试。

- **场景四：消息收发演示** (01:30 - 01:45)
  - 讲师在 `MessageController.java` 中编写了用于发送消息的接口。
  - 讲师在 `NettyWebSocketServer.java` 中调用该接口来发送消息。
  - 讲师在浏览器中看到消息被成功发送和接收。

---

以上是根据视频画面进行的结构化技术课程分析。
