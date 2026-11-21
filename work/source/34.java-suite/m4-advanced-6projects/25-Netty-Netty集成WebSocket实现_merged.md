# 25-Netty-Netty集成WebSocket实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接下来开始去实现一下

Laty加WebSocket的一个集成

来改善我们这一块

它的一个通信效率

这一块我们主要是改善它的通信效率

在业务执行流程方面

我们可能看不到太大的一个区别

好 我们开始来实现一下

像这个Laty集成WebSocket

我们将采用一个开源项目

叫Laty WebSocket Supreme Boot Starter

这是这个

这是咱们国产的

也是国人写的

像这块我们就使用它来集成一下

就OK了

它的集成是非常轻松的

比我们用Laty去实现

要更加的简洁

更加的方便

我们来搭建一个工程

叫SQL Message

这个我们先停掉

在这里右键新建一个工程

叫做SQL Message

好 点击下一步

点击Finish

那么这一块我们主要是

用我们的Laty

来改善了我们当前WebSocket的一个操作

但其实它的流程跟之前差别不大

首先我们先引入一下相关的一个依赖包

首先我们要把DB这块给引入进来

好 依赖一下

接着它这里也有一个包

也需要我们引入

我们把它给引入进来

引入进来了之后

我们开始给它配置一个核心配置文件

我们来配置一下核心配置文件

也就是我们的portstrap.yaml

这里面的配置

我就直接拷贝一下

等会我们再来讲解

那这个是它的一个应用的名称

就不说了

这个是Redis的一个连接配置

这个连接配置

我也不说了

这里还有一个叫WSPortHost

这其实就是WebSocket的一个通信的端口号

这个是对应的一个IP地址

行 这个写了

由于我们这里等会会用到Redis

所以我这里就把Redis的配置也给拷贝

com.sql redis-configure

好 在这一块我们加上一个configuration

行 这里面的配置我就不去写了

我就直接拷贝了

因为这个我们之前项目里面是有的

我就直接拷贝过来就可以了

这个是对咱们Redis的一个序的话题

这个是对咱们Redis的一个序的话题

这个是对咱们Redis的一个序的话题

的一个操作

这就不去详细讲解了

好 这里就搞定了

紧接着我们将去实现一下

我们这一块它的一个WebSocket的相关操作

那跟之前一样

也先新建一个对象

叫做LatyWebSocketServer

这一块也需要交给我们的Spring管理

它这里也有一个注解

跟之前是一样的

叫ServerUnderPoint

但是注意选下面这个包

不要选上面这个

选这个

这里也需要去给它相关的请求路径

叫pass

pass我们可以跟之前写法一样

ws

加上一个userID就可以了

方口你要写上去

port

方口咋写呢

注意ws.port

也就是这一块的路径

这一块写的端口号

还有一个host也得写一下

写个叫ws.host

这一块我们就搞定了

跟之前其实差别不大

好 接下来我们开始在这里写和之前相关的一些操作

第一个就是建立连接

那么建立连接怎么写呢

注意建立连接也非常简单

void叫unopen

在这里有一个注解叫

unopen

注意选上面这个包

这个

那这个时候unopen

我需要接收这个参数怎么办呢

需要接收这个参数

它有一个注解

我们介绍一下

这个注解呢

叫做

pass verb

但这里一块是个map

pass verb

这个

行

我们来写下

这里这么写

注意不要选spin的

选上面这个

你可以写个map

好

这是这个

那如果你需要当前用户的绘画的话

你就写一个session

这个session呢

不要选上面那个

选下面这个

选它

这个session

这个session呢

你可以去看一下

它这里其实就封装了我们当前litty相关的操作

这个操作将不再是我们简简单单的一个web-sort操作了

是我们litty相关的操作了

这是这一块

好

有了这个绘画对象

有了当前这个参数的封装信息

那我们可以获取这个userid了

那怎么获取呢

直接写个pass map.get

写个叫userid

那现在这一块我们就可以拿到用户的ID了

那跟之前一样哈

这是用户的文言ID

那如果我想获取session呢

我可以用这个session的ID

怎么获取呢

也是可以

也是可以获取这个ID的

怎么获取呢

session.这里有一个channel.id

不要忘了转成字图串的形

这个是session的ID

这一块都获取了

紧接着我们进行操作

怎么操作呢

绘画对象是不能存到我们redis里面去的

怎么办

一样的

也仍然定义一个map

存储所有绘画

那么怎么存呢

简单

跟之前是一样的

这里早写了写个叫session

好

这里写个session

那这一块我们就搞定了

搞定了

就开始往里面存

来存

点put一次

userid给他

还有个是什么呢

还有个是session给他

这是这一块哈

存储用户绘画信息

是这个

好

存了之后这个还不够

我们之前说过

我们需要根据用户的一个

当前绘画的一个session ID去找user ID

对不对

需要去实现的

这个时候我们怎么实现呢

我们可以把它存储到我们的redis缓存去

所以在这里我可以注入一下redis缓存

操作对象

redistemplate

注入之后我们开始往里面存

怎么存呢

存储session ID和user ID的映射关系

怎么存呢

我们存到hashmap去

这里我可以写下websocket

letwebsocket user

点put一次

注意key用谁呢

用这个ID了

值用谁呢

值用用户的ID了

那这一块就搞定了

好

这个是我们的session ID了

这是我们这一块存

但是有另外一个问题

就是用户再开一个窗口

那么这个时候这个session会变

对不对

再开一个窗口

session会变怎么办呢

做这么一个事

做什么事情呢

仍然一个道理

首先我要先去取出当前这一块

用户对应的一个绘画对象

对不对

我们看有没有

好怎么做

先来取一下

获取用户对应的

绘画对象

session map

点get一下

把当前这一块这个ID给拿到

这个挪到后面来

挪到这里来

把当前user ID给它

好了

就得到了一个session

user session

我们来看一下这个user session是否有数据

如果有我们就删除一次就可以了

好我们开始清理

这个是清理对应的一个绘画对象

我们来看看这个绘画信息

首先我们要从这里面去把它给移除掉

在这里面

点remove

谁把当前这一块user ID给它

先移除这一个

移除之后

我们这个release里面也是需要去操作的

怎么操作

也非常容易

点

叫delete

把谁给删掉了

当前这一块这个session ID对应的信息给删掉

但是session对应的ID信息

你得去查询才行

那么怎么查询

大家看一下

怎么去查询呢

其实非常容易

我们只需要得到这个ID就行了

也就是你的ID

就这个ID

直接拿到

不是这个ID是他的

对不对

直接拿到你的ID就行了

点

签了

点

ID

不要忘了

扑斯君

那么这个时候就把它从这里面给删掉了

紧接着再走这个

存储过程

就不会出现我们的张数据问题了

好这是这一块

第一个这个是建立链接

紧接着我们再写另外一个

就是

连接关闭

那么连接关闭了也是一样的

没有多大区别

public void

叫unclose

那么unclose这一块该怎么做呢

一样

它也提供了一个注解叫unclose

所以不要选下面这个

选上面这个

那里面的话既然是关闭

你肯定也要把绘画给我对不对

那绘画给我呢

我需要做这么一个事情

首先第一个

要从这个SessionMap中移除对应的绘画

第二个

我要从

当前这个reddittemplate里面

把他给移除

那首先我们要先把对应的用户对象给找到

就是用户的一个usid给找到

那这个其实也容易哈

一个是

先根据

SessionID

从reddit中

查找

查找什么呢

查找

userid

对吧

那么有了userid

紧接着根据

userid

删除

SessionMap

中的

Session

同时不要忘了删除我们的reddit

userid的

映射信息

就是这一块

行我们先去取一下

这个取了是很容易取的

我们来取一下

点get一下

谁呢就是sessionid

这个其实就是用户的id

这个整体是用户的id

好

用户ID拿到了

紧接着我们就开始做一个删除操作

那么删除了我们是删除我们的sessionmap里面的

这个操作呢

也是非常简单哈

直接写个叫sessionmap

点

remove

userid

当然前提是你要判断一下这个userid的

这个usid的

usid存在

如果不存在你删除

这是会报错的

接着我们再做另外一个事情

就是删除reddit中userid的映射信息

那这个简单

好把上面这个拷贝过来

这一块换成什么呢

delete就可以了

这个删除也就搞定了

这个是关闭

还有一个是什么呢

就是我们说的一个

叫

发生异常

public with on error

这个是一样的哈

它也有个注解

on error

所以它这一块的整体其实就是参考了我们前面那一块的实现

只是它这里集成了我们的letty

不需要我们手动去操作letty了

比较的方便

会化会给我

session

还有个异常呢

我们也可以抛除一下

我们直接把异常给输出吧

这里写下

叫做

userid

加上

我们这一块要从reddit template中去获取一下

session.get

channel.id.tushjun

这个时候就可以获取用户ID了

那这个时候我可以打印一下用户的ID

加句话

通信

发生异常

开了这个是发生异常

紧接着我们再说另外一个

那客户端发送消息呢

接收

客户端

发送的

消息

那这个怎么做呢

也是非常容易

public void

on message

既然是发送消息

消息一定得有

还有一个是谁发的是不是得有session呢

它这里也有个注解

on

message

这一块也是非常容易

行我们接着也来给输出一下

首先第一个这个是当前的userid

下面这里我们来写下

我们来写下

这里我们来写下

给我

发送的消息是

加上这个message

可以了这个是接收消息

同时我们也可以回复客户端

怎么回复呢

session.这里直接有一个

send text

0发送的消息

4

加上我们的message

OK搞定了

这个是接收客户端发的消息

那还有一个

我们要主动

给客户端发消息了

那么怎么主动发

是一样的public void

send的

message

那么首先第一个你要把

用户的id给我

第二个你要把

消息给我

或者两个换个位置一样的啊

可以了

那我们来实现一下

信息有了

userid有了

userid可以从这里获取

用户的一个

会话

对吧我们来获取一次

获取

用户会话

接着是不是就可以发送消息了

行我们来写一下

点get一下

userid给他

那么用户的会话我们就拿到了

当会话不为空的时候我们就发消息

那怎么发呢这个就简单了哈

send text

发送的消息

直接写个message吧

可以了消息发送就搞定了

那么这一块整体的操作我们就实现了

紧接着我们开始进行相关的一些测试操作哈

我们看一下这里有个地方报错了是吧

在这里

这里忘了写这个封号

好接着我们开始给他创建一个启动类

那么启动类这一块呢要注意一下

我们写下叫做

lety-web-socket

application

sperm

boot application

这里呢我们

仍然要做这么一个操作哈

仍然是数据库这一块

我们不需要去加载启动

行

接着写个

主方法

这个我就不去说了哈

这个是很简单的了

他这里呢跟之前一样也是要创建那个对象

叫做

server

endpoint

export对象

public

注意

仍然选这个包不要给选错了啊

行

紧接着写一个bin

注解就可以了

那么这一块搞定了

我们再来给他

创建一个

控制器用于

主动给

客户端发消息

我们来创建一个控制器

主动给

指定的客户端发消息

那这个主动发消息呢

我们就直接把刚才写的这个controller控制器

给拿过来就行了

这个给拿过来就可以了

行

在这一块我们来看一下

右键新建一个控制器的包

控制器

把刚才这个直接给拷过来就可以了

那么拷过来呢

这个对象就换掉就不要他了

privity

lettywebsocket server

用他就行了

发消息

这个是一样的

先给消息再给userid

这一块就整体搞定了

那么上面这一块我们就不要这个了

行我们这个测试也写完了

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于“秒杀系统”项目中“Netty + WebSocket”模块的实现。讲师旨在通过一个名为 `seckill-message` 的项目，演示如何利用 Spring Boot 的 `netty-websocket-spring-boot-starter` 依赖，快速集成 Netty 和 WebSocket 技术，以实现一个支持用户抢购状态实时通知的服务器端。课程内容主要围绕服务器端的配置、核心业务逻辑（如建立连接、关闭连接、异常处理、接收与发送消息）展开，并使用 Redis 作为会话存储和用户状态管理的中间件。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程开始，讲师介绍本节内容为“Netty + WebSocket”集成。
*   **00:00:05 - 00:00:15**：讲师说明将使用 `netty-websocket-spring-boot-starter` 依赖来简化集成过程，并介绍项目 `seckill-message` 的用途。
*   **00:00:15 - 00:00:30**：讲师展示 `pom.xml` 文件，添加 `seckill-message` 和 `netty-websocket-spring-boot-starter` 依赖。
*   **00:00:30 - 00:00:45**：讲师展示 `bootstrap.yml` 配置文件，设置 WebSocket 服务端口为 `28082`。
*   **00:00:45 - 00:01:00**：讲师展示 `NettyWebSocketServer.java` 的核心类结构，包括 `@Component` 和 `@ServerEndpoint` 注解。
*   **00:01:00 - 00:01:15**：讲师讲解 `@ServerEndpoint` 注解的路径配置，以及 `@OnOpen` 方法用于建立连接。
*   **00:01:15 - 00:01:30**：讲师在 `onOpen` 方法中，通过 `pathMap` 获取用户 ID，并创建一个 `Session` 对象。
*   **00:01:30 - 00:01:45**：讲师使用 `sessionMap` 存储用户会话，并通过 `RedisTemplate` 将用户 ID 与会话信息绑定到 Redis 中。
*   **00:01:45 - 00:02:00**：讲师讲解 `onClose` 方法，用于在用户断开连接时，从 `sessionMap` 和 Redis 中清理对应的数据。
*   **00:02:00 - 00:02:15**：讲师讲解 `onError` 方法，用于处理连接异常，并打印错误日志。
*   **00:02:15 - 00:02:30**：讲师讲解 `onMessage` 方法，用于接收客户端发送的消息。
*   **00:02:30 - 00:02:45**：讲师讲解 `sendMessage` 方法，用于向指定用户发送消息。
*   **00:02:45 - 00:03:00**：讲师展示 `NettyWebSocketApplication.java` 的启动类，用于启动 WebSocket 服务。
*   **00:03:00 - 00:03:15**：讲师展示 `MessageController.java`，用于提供 HTTP 接口，触发 WebSocket 服务发送消息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   课程标题：“5.2 Netty+WebSocket”。
    *   项目名称：“seckill-message”。
    *   依赖库：“netty-websocket-spring-boot-starter”。
    *   配置文件：“bootstrap.yml”。
    *   核心类：“NettyWebSocketServer.java”。
    *   启动类：“NettyWebSocketApplication.java”。
    *   控制器：“MessageController.java”。

*   **关键代码片段**：

    **1. `pom.xml` 依赖配置：**
    ```xml
    <dependency>
        <groupId>com.seckill</groupId>
        <artifactId>seckill-message</artifactId>
        <version>0.0.1-SNAPSHOT</version>
    </dependency>

    <dependency>
        <groupId>org.yeauty</groupId>
        <artifactId>netty-websocket-spring-boot-starter</artifactId>
        <version>0.9.5</version>
    </dependency>
    ```

    **2. `bootstrap.yml` 配置：**
    ```yaml
    #websocket配置
    #:
    port: 28082
    host: 0.0.0.0
    ```

    **3. `NettyWebSocketServer.java` 核心逻辑：**

    ```java
    @Component
    @ServerEndpoint("/ws/{userid}")
    public class NettyWebSocketServer {

        private static Map<String, Session> sessionMap = new HashMap<>();

        @Autowired
        private RedisTemplate redisTemplate;

        @OnOpen
        public void onOpen(@PathVariable Map<String, String> pathMap, Session session) {
            String userid = pathMap.get("userid");
            String id = session.channel().id().toString();

            Session userSession = sessionMap.get(userid);
            if (userSession != null) {
                sessionMap.remove(userid);
                redisTemplate.boundHashOps(key: "NettyWebSocketUser").delete(userSession.channel().id().toString());
            }

            sessionMap.put(userid, session);
            redisTemplate.boundHashOps(key: "NettyWebSocketUser").put(id, userid);
        }

        @OnClose
        public void onClose(Session session) {
            String userid = redisTemplate.boundHashOps(key: "NettyWebSocketUser").get(session.channel().id().toString());
            sessionMap.remove(userid);
            redisTemplate.boundHashOps(key: "NettyWebSocketUser").delete(session.channel().id().toString());
        }

        @OnError
        public void onError(Session session, Throwable throwable) {
            Object userid = redisTemplate.boundHashOps(key: "NettyWebSocketUser").get(session.channel().id().toString());
            System.out.println("用户ID" + userid + "，通信发生异常！");
        }

        @OnMessage
        public void onMessage(String message, Session session) {
            Object userid = redisTemplate.boundHashOps(key: "NettyWebSocketUser").get(session.channel().id().toString());
            System.out.println("用户ID" + userid + "发送的消息是：" + message);

            session.sendText("您发送的消息是：" + message);
        }

        public void sendMessage(String message, String userid) {
            Session session = sessionMap.get(userid);
            if (session != null) {
                session.sendText(message);
            }
        }
    }
    ```

    **4. `MessageController.java` 控制器：**

    ```java
    @RestController
    @RequestMapping(value = "/message")
    public class MessageController {

        @Autowired
        private NettyWebSocketServer nettyWebSocketServer;

        // 发送消息
        @GetMapping("/send")
        public String sendMessage(@RequestParam String message, @RequestParam String userid) {
            nettyWebSocketServer.sendMessage(message, userid);
            return "消息已发送";
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   讲师在 IDE 中打开 `pom.xml` 文件，演示如何添加 `seckill-message` 和 `netty-websocket-spring-boot-starter` 依赖，为后续开发做准备。

*   **场景二：WebSocket 服务端口配置**
    *   讲师打开 `bootstrap.yml` 文件，将 WebSocket 的端口配置为 `28082`，并设置 `host` 为 `0.0.0.0`，以便外部访问。

*   **场景三：服务器端核心逻辑开发**
    *   讲师在 `NettyWebSocketServer.java` 中编写核心逻辑：
        *   **建立连接 (`@OnOpen`)**：获取用户 ID，创建 `Session` 对象，并将用户 ID 与 Session 存储在 `sessionMap` 中，同时将用户 ID 与 Session ID 的映射关系存储到 Redis。
        *   **关闭连接 (`@OnClose`)**：从 `sessionMap` 和 Redis 中移除对应用户的数据。
        *   **异常处理 (`@OnError`)**：在发生异常时，从 Redis 中获取用户 ID 并打印错误日志。
        *   **接收消息 (`@OnMessage`)**：接收客户端发送的消息，并向客户端回显。
        *   **发送消息 (`sendMessage`)**：根据用户 ID 从 `sessionMap` 中获取对应的 `Session`，并调用 `sendText` 方法向客户端发送消息。

*   **场景四：控制器接口开发**
    *   讲师创建 `MessageController.java`，并编写一个 `@GetMapping("/send")`
