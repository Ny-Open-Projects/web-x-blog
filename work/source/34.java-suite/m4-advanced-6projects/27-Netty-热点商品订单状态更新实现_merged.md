# 27-Netty-热点商品订单状态更新实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们要实现用户的一个热点商品抢单状态更新通知

那这一块该怎么做呢

我们在这里来实现就可以了

这一块怎么做呢

大家看

从这里开始去执行热点商品抢单

那么抢单的话

如果说进入到这里

我们这里要进行一次通知的

这个是什么通知呢

这个是商品受清通知

对吧

那么这一块是什么呢

我们来看一下

到这里那肯定是抢单成功通知

对吧

那么还有另外一种情况

大家想一下

如果此时到这来了

那这个执行到这来了

有可能我们这里获取这个锁是失败的

对不对

获取锁失败了

我们也要通知

通知在这里通知

叫抢单失败通知

那么这些通知我们都知道有

紧接着我们就要去另一个map对象

来实现消息的封装

在这里我们可以定一个map的样子

实现消息封装

然后每次把这个map给发送过去

其实就可以了

好

那么等会要发送的话

因此我们要给当前这个消息微服务

给它创建一个份的一个接口

在这里来创建一个接口

接口名字呢

我们就叫

message

份就可以了

在这里写一个叫份client

写个skill

杠

message

把刚才的一个消息这个接口给拷贝过来

行

这个给拷贝到这边

这里呢就得写一个写杠

message了

这个是我们的消息发送

那么消息发送这一块有了

紧接着我们一会儿这里要去调它

所以要写一个依赖

在这里来写个依赖

叫

skill

杠

message

api

行

依赖也行

还有了我们开始去实现这个消息操作了

在我们这里把它给注入进来

把这个消息发送对象给注入进来

message份autoride

那开始实现消息封装了

这里呢

我就定义一个消息

封装对象

叫做map

string

object

datamap

bluehashmap

就是这一块

那么这里面呢

该怎么去封装这个消息呢?

那么这里面呢该怎么去封装这个消息呢?

我们开始来实现一下哈

首先第一个

这个是商品授青

点往里面put一下

put什么东西呢?

首先第一个

我们要给它一个状态码叫code

对不对?

code要给它

那么这个已经授青的是

200001

再给它一个提示信息

提示信息的就叫做

message

商品已授青

对不对?

接着我们开始发送消息

message

message.

message.

发消息

user id就是用户的id

在这一块有用户的id

我们来找一下就是user name

给它去发消息

发了消息呢

接生点转成字符串类型

message map

好了这里有个异常

我们要抛一下

对吧

抛一下这个异常就可以了

行

这是这一块

我们接着往后面看

那下面这里呢是

抢单成功

对不对

那么抢单成功是20000

这个是

抢单成功

20000这一块就是ok了

200吧

抢单成功

那么下面这一块呢

还有一个地方

如果执行这一些的话

那就是抢单有问题了

在这里最后不要忘了return

如果没经过这里面

那这就是

抢单失败

好

这一块我们就搞完了

不要忘了在这一块给它配置一下对应的一个份的地址

就是secure

message份

我们看一下是不是这个地址

好ok就可以了

那这一块呢刚才在这里有一个地方是有异常的对不对

我们看在哪里

有一个异常的

抛出去

就行了

那总体这一块我们就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“秒杀”（seckill）的分布式高并发电商系统的技术实现讲解。核心内容聚焦于如何通过 **Redisson 分布式锁** 和 **消息推送（WebSocket）** 来解决商品抢购时的并发问题，并实现订单状态的实时通知。讲师通过在 IntelliJ IDEA 中展示代码，逐步演示了如何在订单服务中集成分布式锁、清理用户排队信息、记录用户购买商品、以及通过 WebSocket 向用户发送抢购成功或失败的通知。整个过程体现了分布式系统中“幂等性”、“状态一致性”和“实时性”的设计思想。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1: 项目结构与依赖管理 (约 00:00 - 00:05)**
    *   展示了 `seckill-order` 模块的项目结构。
    *   重点讲解了 `pom.xml` 文件中的依赖，包括 `spring-kafka`、`redisson-spring-boot-starter` 和 `seckill-seata`（分布式事务框架）。

*   **章节 2: 订单服务核心逻辑 (约 00:05 - 00:15)**
    *   在 `OrderServiceImpl.java` 中，讲解了 `hotAdd` 方法的实现。
    *   重点演示了如何使用 `RedissonDistributedLocker` 获取分布式锁，以确保同一商品在同一时间只能被一个用户成功下单。
    *   代码中包含了 `tryLock` 方法的调用，以及对 Redis 中 `num` 字段的读取和更新逻辑。

*   **章节 3: 用户排队与状态管理 (约 00:15 - 00:25)**
    *   讲解了如何在 Redis 中维护用户的排队信息，使用 `boundHashOps` 和 `boundValueOps`。
    *   代码中展示了 `putAll` 和 `set` 方法的使用，用于记录用户购买的商品和设置过期时间。

*   **章节 4: WebSocket 消息推送 (约 00:25 - 00:35)**
    *   展示了 `MessageController.java` 中的 `@GetMapping` 方法，用于通过 WebSocket 向指定用户发送消息。
    *   代码中使用了 `nettyWebSocketServer.send` 方法进行消息推送。

*   **章节 5: 订单状态更新通知 (约 00:35 - 00:45)**
    *   讲解了如何在抢购成功后，通过 Feign 调用 `messageFeign` 服务，向用户发送通知。
    *   代码中展示了 `messageFeign.send` 方法的调用，并构造了包含 `code` 和 `message` 的返回数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容:**
    *   **章节标题:** “5.3 订单状态更新通知”。
    *   **核心思想:** “我们为刚才编写的 WebSocket 编写一个 Feign，并在热点抢购成功的地方调用通知用户抢购成功即可。”
    *   **代码示例:**
        ```java
        @RestController
        @CrossOrigin
        public class SendMessageController {
            @Autowired
            private NettyWebSocketServer nettyWebSocketServer;

            @RequestMapping(value = "/msg")
            public void sendMsg(String msg) {
                nettyWebSocketServer.send(msg);
            }
        }
        ```

*   **关键代码片段:**

    **1. 分布式锁实现 (OrderServiceImpl.java):**
    ```java
    private RedissonDistributedLocker redissonDistributedLocker;

    public void hotAdd(Map<String, String> orderMap) {
        String username = orderMap.get("username");
        String id = orderMap.get("id");

        String key = "SKU_" + id;
        String lockkey = "LOCKSku_" + id;
        String userKey = "USER_" + username + "_" + id;

        boolean bo = redissonDistributedLocker.tryLock(lockkey, 10, 10, TimeUnit.MINUTES);
        if (bo) {
            // 业务逻辑
            if (redisTemplate.hasKey(key)) {
                Integer num = Integer.parseInt(redisTemplate.boundHashOps(key).get("num").toString());
                if (num <= 0) {
                    // 商品售罄
                    messageMap.put("code", 2001);
                    messageMap.put("message", "商品已售罄");
                } else {
                    // 抢购成功
                    messageMap.put("code", 200);
                    messageMap.put("message", "抢购成功！");
                }
            }
            // 解锁
            distributedLocker.unlock(lockkey);
        }
    }
    ```

    **2. WebSocket 消息推送 (MessageController.java):**
    ```java
    @GetMapping(value = "/{userid}")
    public String sendMsg(@PathVariable(value = "userid") String userid, String msg) throws IOException {
        nettyWebSocketServer.send(msg, userid);
        return "OK";
    }
    ```

    **3. Feign 服务调用 (OrderServiceImpl.java):**
    ```java
    private MessageFeign messageFeign;

    // 在抢购成功后调用
    messageFeign.send(username, dataMap);
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 分布式锁的演示**
    *   讲师在 `OrderServiceImpl.java` 中定位到 `hotAdd` 方法。
    *   通过 `redissonDistributedLocker.tryLock(lockkey, 10, 10, TimeUnit.MINUTES)` 方法，演示了如何获取一个 10 秒的锁，以确保同一商品在同一时间只能被一个用户成功下单。
    *   代码中展示了如何读取 Redis 中的 `num` 字段，并根据其值判断商品是否售罄。

*   **场景 2: WebSocket 消息推送的演示**
    *   讲师切换到 `MessageController.java`，展示了 `@GetMapping` 注解的方法。
    *   通过 `nettyWebSocketServer.send(msg, userid)` 方法，演示了如何向指定用户发送消息。
    *   代码中使用了 `@CrossOrigin` 注解，允许跨域请求。

*   **场景 3: 订单状态更新通知的演示**
    *   讲师在 `OrderServiceImpl.java` 中展示了 `messageFeign.send` 方法的调用。
    *   通过构造一个包含 `code` 和 `message` 的 `Map` 对象，演示了如何向用户发送抢购成功或失败的通知。
    *   代码中展示了 `messageFeign.send(username, dataMap)` 的调用，其中 `dataMap` 包含了通知信息。

*   **场景 4: 项目结构与依赖管理的演示**
    *   讲师在 `pom.xml` 文件中，展示了 `spring-kafka`、`redisson-spring-boot-starter` 和 `seckill-seata` 等依赖。
    *   通过 `@EnableFeignClients` 注解，演示了如何启用 Feign 客户端，以便调用其他服务。

---

以上是根据视频画面进行的结构化技术课程分析，希望能帮助您更好地理解视频内容。
