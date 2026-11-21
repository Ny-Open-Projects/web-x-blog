# 22-WebSocket-服务端实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们实现WebSocket的服务端

它主要是为我们刚才写的前端客户端那一块

提供一个服务操作

服务操作这一块

我们就做一个独立的微服务就可以了

我们来新建一个微服务

这个微服务的名称

我们就给它取一个名字

名字就叫Secure WebSocket

那么这一块

它主要是为我们前端的WebSocket提供服务的

这主要是WebSocket的服务

那这一块

它需要依赖一些相关的包

所以这里我们把依赖给先导入一下

首先要依赖我们Web相关的包

接着那这一块既然是实现WebSocket的服务端

所以WebSocket的服务端的包

我们也是需要的

这个服务端的包

在这一块有

大家可以直接烤过去用就可以了

烤到这里来

等会儿我们这里要把它启动

然后为我们前端WebSocket提供服务

所以这一块

它得有一个核心配置文件

核心配置文件呢

我们就直接拷贝一下

然后改一下就可以了

随便烤一个改一下

1808

18088吧

这个数据库这一块

我们是不需要的

这个服务的名字呢

我们换成WebSocket

那别的我们就不需要去改变它了

好

接着再往这一块

这里看

我们接着就要开始去配置一下

为前端提供服务的内

那为前端提供服务的内呢

我们就新建一个对象

com.sql.websocket.config.

这个对象的名字呢

我们就跟这里保持一致就可以了

行

那这个对象呢

你要就把它交给Spring管理

并且你要把这一块暴露出去

那暴露出去的话呢

你总得有一个请求地址

这个请求地址呢

有一个叫server end point

用它来暴露就行了

在这一块我们可以给个value

value呢就是暴露的地址是什么

ws

如果你希望遵循我们的restful方式

来请求这一块

你可以这样写

写个user id

这个跟我们

Spring MVC里面的pass verb是很相像的

行

接着开始去写和我们前端对接的一些方法和事件

首先第一个事件在这一块

如果你的前端跟我这里建立连接

那我这一块要获取连接相关的信息怎么办呢

那这一块有一个建立连接

后调用该方法

这个它会自动去调用

不需要我们去操作哈

那我们只需要提供这个方法就可以了

unopen

在这里可以写个注册

叫onopen注解就行了

这一块呢

如果你想获取请求路径中的一部分作为一个参数

就类似我们的pass verb

它这里提供了一个注解

pass parameter

这个注解

你可以写user id

定义一个变量接受一下

就表示接收请求路径中这一个参数

这个参数呢

我们可以作为用户的一个唯一标识服务

好

除此之外

在这一块

我们再提供一个叫做绘画对象

session

绘画对象

session

那这个session呢

有这么一个特点

就在这一块啊

要注意一个问题

什么问题呢

就是这一块它是属于常链接类型

当前绘画属于常链接类型

因此不能持久化对象到db中

所以这个时候要注意

我们不能够用数据库来存储这个绘画信息

因为这一块当前绘画是常链接对应的类型

是属于一个有状态的

说白了就是有状态的

跟我们普通的http无状态是有区别的

所以你不能把它持久化存储到数据库中的

就是这一块

那这个时候不能存到数据库

只能在哪里存呢

当前内存进行操作就行了

我可以在这里定义一个变量

定义一个map用来存储用户绘画

我刚才说过这个user是作为用户的一个唯一ID

key可以用谁来做key呢

key用当前的user ID

好那值就是当前的绘画了

来让我们定义一个存一下试一下

private static map string session

session map

luxury map

这里是session map

我写个叫做string session

行开始往里面存

那么怎么存呢

我写到这里

存储用户的绘画信息

点put一下user ID给他

session给他

那这一块就结束了

行我们接着来看

来接着来看这一块

那么刚才这里是建立连接

那建立连接它也有可能会关闭连接

对不对

关闭连接

我也需要得到通知

为什么希望得到通知呢

得到通知

我可以把这里面的这个session map

这一块它里面的一个绘画给移除

如果你不移除

这一块会有脏数据产生

所以我们要移除的

怎么移除呢

先写方法unclose

好这里有一个注解叫unclose注解

那如果链接一旦关闭了

绘画一旦关闭了将会调用该方法

那这一块该怎么做呢

要注意一下

这一块我们要把绘画传过来

叫做session

绘画传过来了

我们希望做这么一个事情

把当前这个绘画对象

从这个map中移除

对不对

那么如何移除呢

这就是一个问题了

这里它只有这个session

没有别的东西了

并没有这个user id

那怎么办呢

可以做这么一个事情

你前面这里不是有session吗

我可以把这个session

的唯一id取出来

然后跟这个user的一个信息

建立一个映射关系

把它存起来也是可以的

也是一个map

它是存储session的id

和user id的一个映射关系

做这么一个事

privately写个static map

alice map

luhashi map

可以了

那现在怎么存呢

这么存

你这个时候是存储绘画

接着还要存储绘画的id

和用户和user id的映射关系

要存一下

怎么存

id是map

点put一下

当前session有一个唯一id

点get id

这是一个字符串的信

再把user id也给存进去

好

存了之后

那么现在这边怎么做呢

注意上面存了

下面这里可以先做这么一个事

就是从我们的alice map中

是根据session的id

从alice map中取出我们的user id

然后再做什么事情

user id取出来了

那么可以从这里面

获取到我们对应的一个绘画了

也可以把它直接给移除了

对吧

那就开始从这里移除了

从这里移除绘画了

移除user id对应的绘画

为了保证这一块没有脏数据

你还需要把id map中的一个映射关系也给移除

移除alice map中

session的id对应的user id信息

都要移除的

这一块我们就来操作一下

首先第一个

我们要取出我们的一个

user id在alice map中

点get一下session.get id

这个时候就可以获取到user id了

user id有了

接着就移除一下我们的user id

叫做session map remove user id

移除就搞定了

移除搞定了之后

接着我们还要去移除id map中对应的数据

行了可以了

这是这一块

那整体来说

好像没有问题

但其实还有一些细节点

我们要注意一下

细节点在哪个地方

这一块大家可以看到

看到这么一个问题发生

什么问题

我们可以看一下

比如用户第一次

这是张三用户

他做什么事情

他第一次来建立连接的时候

会调这个方法

调这个方法

他有新开的一个窗口

有可能会刷新

那么新开窗口

我们先不妨说

先说第一次操作

第一次操作

他会把这个数据存到这里面去

存到这里面怎么存

注意是user id对应的session

这是存第一次

那么这个时候session的id是多少

我写一下

等于abc随便写的

那么这个时候id map里面会有什么数据

会有这么一些数据

那叫做abc

它所对应的一个数据是谁

张三

这是这一块

如果用户张三

他这个时候新开了一个窗口

再刷新一次

刷新一次之后

这个时候是怎么样的

这仍然是张三

仍然是张三

仍然会调这个方法

调这个方法来会怎么做

仍然先会往session map中

存对应的数据

那么存的话是怎么存的

要注意一下

前面这个user对应的session这一块是不变的

但是有一个问题

有一个问题

就前面这个user key是user id

这个是不变

这个session肯定会变

对不对

但是第二个后面这一块会有问题的

后面这里会有什么问题

session id有可能不是abc了

有可能是aa

前面这一块是不会有什么重复数据的

也就是第一个session map里面

数据是不会重复的

因为他这里key是唯一的

而另外一个问题发生了

下面这里会有问题了

下面这里会有什么问题呢

我们简单说一下

现在这一块abc

他的值是张三

那现在会多另外一条数据

就是aa他的值是张三

会多这么一条数据

所以像这种情况

我们要考虑一下

怎么考虑呢

非常容易

你每次把这个user

id传过来的时候

我可以先去这里面去获取一下你的绘画信息

如果有绘画信息

我把这里面移除

把这里面对应的绘画也移除

然后再做这些添加操作

其实就可以了

我们现在就按刚才这一块分析来实现一下

做这么一个事

先根据user id获取绘画session

然后做这么一个事

根据session

id和user id移除可能存在的冗余数据

来整一下session

user session

等于sessionmap.get userid给他

那此时如果说user session不为空

那就需要去把这些冗余数据给移除了

好来怎么移除呢

很容易

第一个这里面移除是没啥问题的

但是移除之前要注意一下

他下面这里也有数据

也是需要你要移除的

行我们先把id map移除

remove谁呢

user session.get id把它移除

接着把这里面的也给移除一次

移除是当前的user id

可以了

移除之后再来做这个存储

是不会有脏数据的

行让我们建立连接搞定了

还有一个关闭连接也搞定了

接着就是另外一个

就是有可能连接过程中发生异常

异常处理这一块也是一个问题

那么异常处理怎么处理呢

on arrow

在这一块有一个注解叫做on arrow

那么这里会传什么过来呢

你可以把当前的绘画传过来

另外一个就是异常的类型

你可以写一下

行这个时候我们就输出一下

用户id

用户id加上

从这里面可以获取用户的id

就是id map里面来获取一下

点get

点get

session.get id

这是用户id

然后在这里写发生了异常

发生了异常

那什么异常呢

我们把异常给写过来

可以了

这个是异常处理

好

建立连接

关闭连接

异常处理都有了

紧接着我们再做另外一个操作

什么操作呢

就是接收客户端消息

因为他客户端有可能会给我们发消息

对不对

我写一个叫做on message

给我发的是什么消息呢

我不知道

我先写一下on message

那来写一下消息

message

还有一个是谁给我发的消息呢

会有一个叫做session

会话会给我的

这是这一块

那同样一个道理

我仍然可以输出这么一段操作

这一块发送的信息

接收到的信息是

把这个信息给打印一下

接收到的信息是

可以了

这个是接收消息处理

接收消息处理之后

紧接着我们来整另外一个事情

我们说过外部socket的这一块

我可以实现后端跟前端之间的一个消息通信

前端能给我发消息

我后端也能给前端发消息

对不对

我接着写一个叫做消息发送了

那么消息发送

写个oid叫send message就行了

send message的话

你要给哪个会话发消息呢

发的是什么消息

这个我得知道对不对

所以你要把消息给我传过来

你还可以把userid给我传过来

因为userid可以从我们当前这一块

去获取到用户的会话

行我来写一下

根据userid获取会话对象

然后开始给指定会话发送消息

好来写一下

叫做sessionmap.get userid给他

session就拿到了

此时如果说session不得用空

那么我们就开始发送消息操作了

消息怎么做

session.get有一个叫basicremote.sendtxt

你还可以发送一些文件都是可以的

我们就发送文本内容吧

这一块就搞定了

那发送消息的一个接收

以及我们这一块建立连接关闭连接

所触发的操作都搞定了

都搞定了

接着我们来创建一个启动类

来实现一下相关的一个测试了

在这一块右键新建一个启动类

启动类就叫websocket application

这里写一个叫supreme boot application

在这一块注意要禁止一下数据库的启动

好这一块写个supreme application run

当前这一块它的自己码给它

args给它

然后我们这一块还要创建另外一个对象

这个对象给大家说一下

这个对象它的主要作用

其实就是把我们对应的websocket的对应的服务给暴露出去

同时它会禁止我们当前server的容器

容器去扫描这一个

websocket的一个地址

在这一块不要让我们当前server的容器去扫描它

在这一块

好怎么做呢

直接new这个对象就行了

不要忘了把它交给supreme管理

OK

这一块我们整个websocket的服务端就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一节关于使用 Spring Boot 和 Java WebSocket 实现实时通信服务的实战教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个 WebSocket 服务端。核心内容包括：配置项目依赖、编写 `@ServerEndpoint` 注解的服务器端点类、实现 `onOpen`、`onClose` 和 `onError` 三个生命周期方法以管理用户会话，以及实现 `sendMessage` 方法用于向指定用户发送消息。整个过程旨在教授开发者如何构建一个基础的、可扩展的实时通信模块。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示项目结构。讲师在 IntelliJ IDEA 中打开了名为 `seekillproject` 的项目，其包含 `seekill-parent`、`seekill-gateway`、`seekill-service` 等多个模块，其中 `seekill-websocket` 模块是本次演示的核心。
*   **00:06 - 00:15**: 介绍 WebSocket 服务。讲师打开 `seekill-websocket` 模块下的 `pom.xml` 文件，展示了项目依赖，包括 `spring-boot-starter-websocket`。
*   **00:16 - 00:30**: 编写 WebSocket 服务端点。讲师在 `src/main/java/com/seekill/websocket` 包下创建 `WebSocketServer.java` 文件，并编写了 `@ServerEndpoint` 注解的类，定义了连接路径 `/ws/{userid}`。
*   **00:31 - 00:45**: 实现会话管理。讲师在 `WebSocketServer` 类中定义了两个静态 `Map`：`sessionMap` 用于存储用户ID与会话的映射，`idsMap` 用于存储会话ID与用户ID的映射，以实现双向查找。
*   **00:46 - 01:00**: 实现 `onOpen` 方法。讲师编写了 `onOpen` 方法，用于在客户端连接时，将用户ID和会话信息存入 `sessionMap` 和 `idsMap`。
*   **01:01 - 01:15**: 实现 `onClose` 方法。讲师编写了 `onClose` 方法，用于在客户端断开连接时，从两个 `Map` 中移除对应的用户ID和会话ID。
*   **01:16 - 01:30**: 实现 `onError` 方法。讲师编写了 `onError` 方法，用于在通信发生异常时，打印错误信息。
*   **01:31 - 01:45**: 实现 `sendMessage` 方法。讲师编写了 `sendMessage` 方法，用于向指定用户ID发送消息。
*   **01:46 - 02:00**: 配置 WebSocket 服务。讲师在 `WebSocketApplication.java` 中配置 `ServerEndpointExporter`，以便 Spring Boot 能够自动扫描并注册 WebSocket 端点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码：WebSocket 服务端点类 (`WebSocketServer.java`)**
    ```java
    @Component
    @ServerEndpoint(value = "/ws/{userid}")
    public class WebSocketServer {
        // 存储用户会话信息，key为userid
        private static Map<String, Session> sessionMap = new HashMap<String, Session>();
        // 存储SessionID和userid的映射关系
        private static Map<String, String> idsMap = new HashMap<String, String>();
        
        @OnOpen
        public void onOpen(@PathParam("userid") String userid, Session session) {
            // 存储用户会话信息
            sessionMap.put(userid, session);
            // 存储会话的id和userid的映射关系
            idsMap.put(session.getId(), userid);
        }
        
        @OnClose
        public void onClose(Session session) {
            // 根据Session的ID从idsMap中取出userid
            String userid = idsMap.get(session.getId());
            // 从sessionMap中移除userid对应的会话
            sessionMap.remove(userid);
            // 移除idsMap中Session的ID对应的userid信息
            idsMap.remove(session.getId());
        }
        
        @OnError
        public void onError(Session session, Throwable throwable) {
            System.out.println("用户：" + idsMap.get(session.getId()) + "，通信发生了异常：" + throwable.getMessage());
        }
        
        // 给指定会话发送消息
        public void sendMessage(String message, String userid) {
            Session session = sessionMap.get(userid);
            if (session != null && session.isOpen()) {
                try {
                    session.getBasicRemote().sendText(message);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    ```

*   **关键代码：WebSocket 服务配置类 (`WebSocketApplication.java`)**
    ```java
    @SpringBootApplication
    public class WebSocketApplication {
        public ServerEndpointExporter serverEndpointExporter() {
            return new ServerEndpointExporter();
        }
    }
    ```

*   **关键依赖 (POM 文件片段)**:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-websocket</artifactId>
    </dependency>
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:00-00:05)**
    *   **描述**: 讲师首先展示了项目在 IntelliJ IDEA 中的完整结构。通过项目树，观众可以清晰地看到 `seekill-parent`、`seekill-gateway`、`seekill-service` 等模块，以及本次演示的核心模块 `seekill-websocket`。这有助于观众理解项目的整体架构。

*   **场景二：依赖配置 (00:06-00:15)**
    *   **描述**: 讲师打开了 `seekill-websocket` 模块的 `pom.xml` 文件，高亮显示了 `spring-boot-starter-websocket` 依赖。这表明项目已准备好使用 Spring Boot 的 WebSocket 支持。

*   **场景三：编写 WebSocket 服务端点 (00:16-00:30)**
    *   **描述**: 讲师在 `src/main/java/com/seekill/websocket` 包下创建了 `WebSocketServer.java` 文件。他使用 `@ServerEndpoint` 注解定义了服务端点，并设置了连接路径 `/ws/{userid}`。这一步是创建 WebSocket 服务的基础。

*   **场景四：实现会话管理 (00:31-00:45)**
    *   **描述**: 讲师在 `WebSocketServer` 类中定义了两个 `Map`：`sessionMap` 和 `idsMap`。他通过 `sessionMap.put(userid, session)` 将用户ID与会话对象关联，并通过 `idsMap.put(session.getId(), userid)` 建立会话ID与用户ID的映射。这为后续的会话查找和管理提供了数据支持。

*   **场景五：实现生命周期方法 (00:46-01:30)**
    *   **描述**: 讲师依次实现了 `onOpen`、`onClose` 和 `onError` 方法。
        *   `onOpen` 方法：在连接建立时，将用户ID和会话存入 `sessionMap` 和 `idsMap`。
        *   `onClose` 方法：在连接关闭时，从两个 `Map` 中移除对应的用户ID和会话ID。
        *   `onError` 方法：在发生异常时，打印错误信息，便于调试。
    *   **演示重点**: 讲师强调了 `onOpen` 方法中 `sessionMap.put(userid, session)` 和 `idsMap.put(session.getId(), userid)` 的作用，以及 `onClose` 方法中如何通过 `idsMap` 获取用户ID并从 `sessionMap` 中移除会话。

*   **场景六：实现消息发送方法 (01:31-01:45)**
    *   **描述**: 讲师编写了 `sendMessage` 方法。该方法根据用户ID从 `sessionMap` 中获取对应的 `Session` 对象，然后通过 `session.getBasicRemote().sendText(message)` 向客户端发送消息。这实现了向指定用户发送消息的核心功能。

*   **场景七：服务配置 (01:46-02:00)**
    *   **描述**: 讲师在 `WebSocketApplication.java` 中添加了 `@SpringBootApplication` 注解，并配置了 `ServerEndpointExporter`。这一步是为了让 Spring Boot 自动扫描并注册 WebSocket 端点，使服务能够被客户端访问。

---

以上是根据视频画面进行的详细结构化分析。
