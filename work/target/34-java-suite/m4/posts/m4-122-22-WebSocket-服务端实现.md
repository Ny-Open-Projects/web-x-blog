---
title: "WebSocket 服务端与 Netty 集成实战：热点商品抢单状态实时推送"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 千亿级电商秒杀解决方案]
tags: [Java, 项目实战, Netty]
---

# WebSocket 服务端与 Netty 集成实战：热点商品抢单状态实时推送

客户端就绪之后轮到服务端。这一篇先搭独立的 seckill-websocket 微服务，把张三、李四两个客户端的消息收发与定向推送跑通；随后正视 WebSocket 底层 BIO 的并发瓶颈，引入 Netty 的三大特性，用国产 starter 完成集成改造，最后把热点商品抢单的售罄、成功、失败三类状态接进推送链路，完成订单状态通知的闭环。

## 先给结论

- 服务端做成独立微服务 seckill-websocket：依赖 web 与 spring-boot-starter-websocket，端口 18088，不连数据库，启动类排除数据源自动配置。
- 端点类用 `@ServerEndpoint("/ws/{userid}")` 暴露，@OnOpen/@OnClose/@OnError/@OnMessage 四个生命周期方法由框架自动回调；Session 是长连接的有状态对象，不能持久化到数据库，只能放内存 Map。
- 会话管理用两个 Map：sessionMap（userid → Session）与 idsMap（sessionId → userid）。同一用户刷新或新开窗口会生成新 sessionId，sessionMap 因 userid 唯一不会重复，idsMap 却会堆积旧映射——onOpen 存储前先按 userid 取旧会话，不为空就两边都清一遍再存。
- 定向推送：sendMessage(message, userid) 从 sessionMap 取会话，`session.getBasicRemote().sendText(message)` 发出；HTTP 控制器 `/message/{userid}` 接收参数转调即可。
- WebSocket 底层是 BIO，每个连接独占线程、并发弱；Netty 基于 NIO：Selector 单线程轮询处理所有连接、零拷贝省掉 Socket 缓冲区的两次拷贝、Channel/ChannelPipeline/ByteBuf 封装大幅减少 NIO 代码量。
- Netty 改造用 org.yeauty 的 netty-websocket-spring-boot-starter：注解同款但要选对包，sessionId → userid 的映射改存 Redis hash（NettyWebSocketUser），通信端口换成 28082；热点抢单在售罄、成功、获取锁失败三个节点封装 code + message 的 Map，经 Feign 调消息服务推送给用户。

## 服务端实现：seckill-websocket 微服务

服务端是为前端客户端提供服务的，做成一个独立微服务即可。工程引入 web 依赖和 WebSocket 服务端包 spring-boot-starter-websocket；核心配置里端口设为 18088，服务名换成 websocket，数据库相关的配置直接删掉——这个服务不碰数据库。

端点类与前端对接，核心是 `@ServerEndpoint` 暴露的请求地址，写法与 Spring MVC 的 @PathVariable 很像：

```java
@Component
@ServerEndpoint(value = "/ws/{userid}")
public class WebSocketServer {

    // 存储用户会话，key 为 userid
    private static Map<String, Session> sessionMap = new HashMap<>();
    // 存储会话 ID 与 userid 的映射关系
    private static Map<String, String> idsMap = new HashMap<>();

    @OnOpen
    public void onOpen(@PathParam("userid") String userid, Session session) {
        // 同一用户刷新或新开窗口时，先清理可能存在的冗余会话
        Session userSession = sessionMap.get(userid);
        if (userSession != null) {
            idsMap.remove(userSession.getId());
            sessionMap.remove(userid);
        }
        // 存储用户会话与会话 ID 的映射
        sessionMap.put(userid, session);
        idsMap.put(session.getId(), userid);
    }

    @OnClose
    public void onClose(Session session) {
        // 根据会话 ID 反查 userid，两边一起清，避免脏数据
        String userid = idsMap.get(session.getId());
        sessionMap.remove(userid);
        idsMap.remove(session.getId());
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        System.out.println("用户：" + idsMap.get(session.getId())
                + "，发生了异常：" + throwable.getMessage());
    }

    @OnMessage
    public void onMessage(String message, Session session) throws IOException {
        System.out.println("接收到的信息是：" + message);
        // 回显：客户端发什么就回什么
        session.getBasicRemote().sendText("收到的消息：" + message);
    }

    // 给指定用户发消息
    public void sendMessage(String message, String userid) throws IOException {
        Session session = sessionMap.get(userid);
        if (session != null && session.isOpen()) {
            session.getBasicRemote().sendText(message);
        }
    }
}
```

四个回调方法建立连接、关闭连接、异常、收消息各管一段，都是框架在事件发生时自动调用的，只需要提供方法。onClose 里没有 userid 可用，所以 onOpen 除了存 userid → Session，还要存一份 session.getId() → userid 的映射，关闭时才能反查。

这里有一个必须想清楚的问题：Session 属于长连接的有状态对象，与无状态的普通 HTTP 不同，不能持久化到数据库，会话信息只能放在内存里操作。

存储本身还有个细节坑。用户张三第一次建连，sessionMap 存入"张三 → session"，idsMap 存入"abc → 张三"；刷新或新开窗口后仍是张三，新的 sessionMap 条目因为 key 唯一不会重复，但会话 ID 变了，idsMap 里会多出"aa → 张三"这样的旧映射。上面的 onOpen 已经处理：存储前先按 userid 取旧会话，取到就先删 idsMap 里旧会话 ID 的映射、再删 sessionMap 里的旧条目，然后才做新的存储，不会再有脏数据。

启动类注意两件事：这个服务不用数据库，排除数据源自动配置；注册 ServerEndpointExporter Bean，把 WebSocket 端点暴露出去，同时不让 servlet 容器去扫描这个地址：

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

## 消息收发测试：双客户端与定向推送

主动给指定用户发消息需要一个 HTTP 入口，控制器注入 WebSocketServer 转调即可：

```java
@RestController
@RequestMapping(value = "/message")
public class MessageController {

    @Autowired
    private WebSocketServer webSocketServer;

    // 给指定用户发消息
    @GetMapping(value = "/{userid}")
    public String send(@PathVariable(value = "userid") String userid, String msg) throws IOException {
        webSocketServer.sendMessage(msg, userid);
        return "OK";
    }
}
```

测试准备了两个客户端页面：张三连接 `ws://localhost:18088/ws/张三`，李四连接 `ws://localhost:18088/ws/李四`。启动服务后打开两个页面，各自输入消息发送：张三发"哈喽"、李四发"你好"，服务端都在控制台打印收到的信息并回显"收到的消息：xxx"，收发链路没问题。

定向推送走 HTTP 接口：请求 `http://localhost:18088/message/张三?msg=...`，张三的页面立刻收到推送；把路径换成李四，李四的页面同样收到。前端 onmessage 事件接到数据后追加到页面元素里，整个"服务端主动推 → 客户端实时收"的闭环就验证完了。

## Netty 为什么快：BIO 短板与三大特性

通信是通了，但原生的 WebSocket 底层用的是 BIO，性能效率和并发处理能力有限，Netty 就是为改善这个问题引入的。Netty 是一个广泛使用的 Java 网络编程框架，提供易于使用的客户端、服务端 API，Facebook 等大型公司和很多流行框架都用到了它的核心代码。它的优势可以总结为三点：并发高、传输快、封装好。

并发高源于 NIO。BIO（阻塞 IO）下，一个用户发起 Socket 请求，后端就开一个线程专门等待、接收、处理、响应，每个请求独占线程——线程很耗费服务器资源，而服务器能开的线程数量又是有限的，所以 BIO 的并发处理能力偏弱。NIO（非阻塞 IO）换了一个模型：一个 Selector 对象接收所有请求的数据，然后循环处理每个请求，一个线程就能服务大量连接，并发能力强得多。

| 对比项 | BIO（阻塞 IO） | NIO（非阻塞 IO） |
| :--- | :--- | :--- |
| 线程模型 | 每个 Socket 连接独占一个线程，阻塞等待数据 | Selector 统一接所有连接的数据，线程循环处理各请求 |
| 资源消耗 | 请求越多线程越多，服务器吃不消，线程总量也有限 | 单线程可服务大量连接，并发能力大幅提升 |

传输快依赖 NIO 的零拷贝（Zero-Copy）机制。普通拷贝路径上，数据从 IO 读到堆内存之前要经过 Socket 缓冲区，一次传输相当于拷贝两次，造成资源浪费；零拷贝在堆内存之外开辟一块内存，数据直接从 IO 读进去，省掉了 Socket 缓冲区，速度随之加快。Netty 的 ByteBuffer（ByteBuf）就是字节数据的存储容器：可以读取、操作整个 ByteBuf 对象，也可以按读写索引（readIndex/writeIndex）对其中某一个字节进行读写。

封装好是对 NIO 代码量的拯救：原生 NIO 要写的代码非常多，Netty 封装后代码非常简洁。核心概念围绕 Channel（数据传输流，对应一个请求、一个连接）展开——ChannelHandler 是核心业务处理，要处理的业务就在这里实现；ChannelHandlerContext 用于传输业务数据；ChannelPipeline 保存处理过程需要用到的 ChannelHandler 和 ChannelHandlerContext。

## Netty 集成 WebSocket：改造消息服务并接上抢单通知

集成采用开源项目 netty-websocket-spring-boot-starter——国产、国人写的，比直接用 Netty 手写简洁得多。新建工程 seckill-message，流程与之前的 websocket 服务差别不大：引入 web 依赖和 starter，Redis 配置类与序列化配置从原项目拷贝，bootstrap.yml 里保留应用名、Nacos 注册、Redis 集群配置，再加 WebSocket 的通信端口与 IP：

```yaml
ws:
  port: 28082   # WebSocket 通信端口
  host: 0.0.0.0
```

端点类 NettyWebSocketServer 的注解与之前同名，但一定要选 netty-websocket-spring-boot-starter 包下的 @ServerEndpoint、@OnOpen、@OnClose、@OnError、@OnMessage，不要选成 javax.websocket 的。路径沿用 /ws/{userid}，端口和 host 引用配置里的 ws.port、ws.host：

```java
@Component
@ServerEndpoint(value = "/ws/{userid}", port = "#{ws.port}", host = "#{ws.host}")
public class NettyWebSocketServer {

    private static Map<String, Session> sessionMap = new HashMap<>();

    @Autowired
    private RedisTemplate redisTemplate;

    @OnOpen
    public void onOpen(@PathVariable Map<String, String> pathMap, Session session) {
        String userid = pathMap.get("userid");
        // 会话 ID 来自 Netty 的 Channel，不再是普通 Web Session
        String id = session.channel().id().toString();

        // 清理同一用户刷新/新开窗口留下的旧会话
        Session userSession = sessionMap.get(userid);
        if (userSession != null) {
            sessionMap.remove(userid);
            redisTemplate.boundHashOps("NettyWebSocketUser")
                         .delete(userSession.channel().id().toString());
        }
        sessionMap.put(userid, session);
        // sessionId -> userid 的映射存入 Redis hash
        redisTemplate.boundHashOps("NettyWebSocketUser").put(id, userid);
    }

    @OnClose
    public void onClose(Session session) {
        // 先按会话 ID 从 Redis 反查 userid，再两边一起清
        String userid = (String) redisTemplate.boundHashOps("NettyWebSocketUser")
                .get(session.channel().id().toString());
        if (userid != null) {
            sessionMap.remove(userid);
        }
        redisTemplate.boundHashOps("NettyWebSocketUser")
                     .delete(session.channel().id().toString());
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        Object userid = redisTemplate.boundHashOps("NettyWebSocketUser")
                .get(session.channel().id().toString());
        System.out.println("用户ID" + userid + "，通信发生异常！");
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        Object userid = redisTemplate.boundHashOps("NettyWebSocketUser")
                .get(session.channel().id().toString());
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

与第一版的两处差别：一是 Session 对象已经封装了 Netty 的 Channel 操作，取会话 ID 用 `session.channel().id().toString()`；二是 sessionId → userid 的映射这次存到 Redis 的 hash 里（key 为 NettyWebSocketUser），不在内存 Map 里。会话仍不能存 Redis，sessionMap 还是内存 Map。脏数据清理逻辑与之前一致：onOpen 先取旧会话，不为空就删 sessionMap 和 Redis 里的旧映射，再存新会话；onClose 先从 Redis 反查 userid，存在才删 sessionMap，最后删掉 Redis 中该会话 ID 的映射。

启动类 NettyWebSocketApplication 与之前一样：排除数据库自动配置，注册 starter 包下的 ServerEndpointExporter；控制器把原来的 webSocketServer 换成 nettyWebSocketServer，注入后调 sendMessage(msg, userid)。

测试时踩到一个问题：给张三定向推送，会话取到的是空——建连时从 `@PathVariable` 的 Map 里取 userid 拿到的是空值。把 Map 接收换成 `@PathVariable(value = "userid")` 直接声明参数，路径里的 userid 就能正常拿到。重启后两个客户端页面的端口改成 28082，刷新建连，各自发 hello 都收到回显；再用 `/message/{userid}` 定向推送，张三、李四都准确收到。业务执行流程上 Netty 版与之前看不到太大区别，改善的是通信效率本身。

最后接业务：热点商品抢单的订单状态更新通知。订单服务的 hotAdd 处理抢单，有三个通知点——进入抢单判断、库存已售罄时是商品售罄通知；扣减成功走到下单是抢单成功通知；获取分布式锁失败则是抢单失败通知。消息封装成 Map，由 Feign 接口调消息服务推送：

```java
// 获得锁后读取库存，决定通知类型
Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());
if (num <= 0) {
    // 商品售罄
    dataMap.put("code", 2001);
    dataMap.put("message", "商品已售罄");
} else {
    // 抢单成功
    dataMap.put("code", 200);
    dataMap.put("message", "抢单成功");
}
// 通过消息微服务推送给用户
messageFeign.send(username, JSON.toJSONString(dataMap));
```

Feign 接口建在订单服务侧，指向消息微服务：

```java
@FeignClient("seckill-message")
public interface MessageFeign {

    @GetMapping(value = "/message/{userid}")
    String send(@PathVariable(value = "userid") String userid, String msg);
}
```

订单服务引入 seckill-message-api 依赖并注入 MessageFeign，三个通知点各自封装 code 与 message 后调用 send，前端排队页面的 WebSocket 连接收到推送，用户就能在排队期间实时拿到抢单结果——热点商品订单状态通知至此闭环。

## 小结

- 服务端 seckill-websocket 微服务：@ServerEndpoint("/ws/{userid}") 暴露端点，四个生命周期回调 + sendMessage 构成完整能力；Session 有状态不能入库，靠 sessionMap 与 idsMap 两个内存 Map 管理，onOpen 先清旧会话防脏数据。
- 测试闭环：双客户端回显验证收发，/message/{userid} 接口验证定向推送。
- Netty 三大特性：NIO Selector 让单线程服务大量连接、零拷贝省掉 Socket 缓冲区两次拷贝、对 Channel/ChannelPipeline/ByteBuf 的封装把 NIO 代码量压下来。
- Netty 集成用 netty-websocket-spring-boot-starter：注解换包不换名，会话 ID 来自 Channel，sessionId → userid 映射迁移到 Redis hash，端口 28082；Map 取路径参数取不到值时改用 @PathVariable 直接声明参数。
- 热点抢单的售罄（2001）、成功（200）、锁失败三类状态封装成消息，经 MessageFeign 调消息服务推送，排队用户的订单状态通知闭环完成。
