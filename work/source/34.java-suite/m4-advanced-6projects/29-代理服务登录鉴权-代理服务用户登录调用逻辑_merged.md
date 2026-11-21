# 29-代理服务登录鉴权-代理服务用户登录调用逻辑 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们就去实现代理服务登录接口调用的处理

交易服务实现完用户登录接口之后

代理服务呢就要去作为调用方去调用用户的登录接口

那咱们看一下代理服务PB的数据结构该如何去定义

咱们回到代码当中

找到公用的PB数据结构工程

找到内体对外的数据结构定义

咱们就在stock message下面

增加相关的接口定义

首先咱们给它的请求消息体增加一个数据消息结构

咱们往下面添加

不要修改它原来的序号

login data

这里等于3

咱们再去定义login data的数据结构体

在下面

message

login data

这个是用户登录接口的

请求数据

它只要传递用户的账号

以及用户的密码

用户账号

用户密码

接着咱们再定义一个用户登录的响应数据包结构

这里记录用户登录返回的账号相关信息

用户登录接口的响应数据包

定义一个用户ID

然后交易账户ID

定义完成之后

咱们将这两个对象加入进去

上面的请求数据体

我们就把这两个对象加入进去

咱们已经加入进去了

那么咱们就完成了

代理服务

Netty的对外用户登录接口的数据结构第一

咱们将代码生成下

这里就要采用Netty的脚本

这里的Netty是负责代理服务

和外部用户的接口通讯

接下来咱们要去代理服务

增加用户登录接口的处理器

在Processor包下面

咱们创建一个

新的处理器

stock user processor

同样它要去继承AppStack的

抽象处理器

然后要去实现

公用的处理器接口

我们加上注解

service

MocopoJ2的位置注解

增加注释

这个是用户接口的处理器

这里也添加一个注释

负责用户接口请求数据处理

然后我们再去做一个

接口的处理

接下来咱们去注入GRBC的接口

stock user service grbc

这里采用注释方式进行调用

stock

经以GRBC client

指向了

GRBC服务端的配置

这里指向的是交易服务

GRBC

用户

服务接口

接着咱们来梳理一下

用户登录接口的调用处理流程

首先呢

咱们要去转换

请求参数对象

获取参数信息

接着我们要去调用

远程的GRBC

用户登录接口

登录完成之后

这个逻辑是不是就处理结束了

还没有咱们呢

还要去

记录用户在线缓存信息

这边呢

包含

用户在线缓存信息

也就是说咱们要知道

在系统当中

有多少个用户在线

在消息下发或者广播的时候呢

咱们就能够呢

去根据用户在线缓存信息

推送给对应的用户

那么广播推送呢

咱们还必须拿到

用户的连接通道

对不对

所以咱们还需要去记录

用户

账户ID

和连接

通道的

联系通道

对不对

所以咱们还需要去记录

用户

通道的

关联缓存信息

主要呢

就这两部分缓存的记录

最后呢

就要返回处理报文给客户端

这些呢

就是用户登录接口调用的

整体处理逻辑

那首先

咱们去实现辅助方法

也就是说

用户缓存记录信息的处理

定一个新的方法

report.kg

panelID

login response

内体包下面

添加对应的注释

这边呢

包括两部分

这部分的处理逻辑是怎样呢

咱们同样

咱们先做个梳理

第一步咱们要去记录

通道ID

与账户ID的关联缓存信息

达到Key取对象

通过Key取manage去获取

Key取manage

因为很多地方都会使用

咱们就将它定义在抽象的附类当中

Key取manage

录入进来

这个呢就是缓存管理器

好

再回到咱们的user processor

在这里就可以拿到

可以取manage对象

获取对应的缓存

传递Key值

stock

login

userKey

然后记录连接通道

与用户ID的缓存

channelID

将它转换为一个长整性文本

接着就存储

这个缓存的关键

我们先去做一个

我们先去做一个

我们先去做一个

我们先去做一个

我们先去做一个

我们先去做一个

我们先去做一个

接着就存储用户账户ID

接着就存储用户账户ID

第二步呢

咱们要去记录

第二步呢

咱们要去记录

在线用户缓存

在线用户缓存

Hedge ReadyWhatever

Hedge ReadyWhatever

Hedge ReadyWhatever

Online

Online

从缓存当中获取

从缓存当中获取

Global Consistency

Global Consistency

传递Key

传递Key

这个呢就叫userKey Online

这个呢就叫userKey Online

在做缓存记录的时候

在做缓存记录的时候

大家要注意一下

这个系统是可以允许用户

同时进行登录

这个系统是可以允许用户

同时进行登录

也就是说用户可以拿手机登录

也可以拿iPad

或者是PC浏览器进行登录

也可以拿iPad

或者是PC浏览器进行登录

如果出现极端情况

如果出现极端情况

用户呢

同时登录

要去修改在线用户缓存

要去修改在线用户缓存

那么

就会出现一个

并发安全性问题

并发安全性问题

也就是在某个线程

也就是在某个线程

进行操作的时候

另外一个线程呢

又拿取到缓存

然后进行了更新

然后进行了更新

这样就会造成

数据的不一致性问题

数据的不一致性问题

那怎么去解决呢

在这里咱们就去

加入分布式锁

加入分布式锁

目的呢

目的呢

就是防止

就是防止

用户

用户

同时登录

造成缓存

造成缓存

信息记录

信息记录

不一致问题

分布式锁的代码实现

咱们先移植过来

咱们先移植过来

在后面章节

分布式锁的运用的时候呢

咱们还会做具体的讲解

将用到的

基于Ladies的

分布式锁加入进来

这个service名称呢

叫LadiesLockService

将它先注入进来

这个注入是

基于Ladies分布式锁的实现

在这里引入分布式锁

是让大家

先有一个初步的概念

后面章节呢

咱们再来做具体的讲解

回到刚才的

缓存记录方法

在线用户缓存记录的对象呢

是一个MAP结构

log

channelID

account.info

外围加上cache异常

ctrl-add-t

bycache

打印异常章信息

log.al

还加上fundlead

这个呢

是要解锁处理

就是不管在什么情况下面

咱们就要将Ladies的锁呢

进行释放

unlock

这里呢

传递一个key就可以了

box userkey

锁的运用呢

也比较简单

在这里调用trylock的方法

global consistence stock

box userkey

然后咱们要去做一个判断处理

如果

在线用户缓存部位空

那咱们就要做一个更新处理

将account.info

做一个转换

从缓存当中获取具体的对象

如果是不存在

在这里就要去

新增缓存记录

account.info

UHMAP

接着就要将账户ID

和通道呢

做一个关联

response

get account ID

最后呢

要去更新Ladies的缓存

cache

put

传入key

这个呢是allman

将MAP对象呢

打进去

好

咱们回到讲义当中

这一讲呢

咱们就完成了

用户登录接口处理器

调用逻辑的处理

以及用户缓存信息的记录处理

下一讲

咱们再去对

用户登录接口的调用处理逻辑

做个具体的实现

那这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的股票交易系统（或其代理服务）的开发演示。核心内容是实现一个用户登录功能，该功能涉及 gRPC 服务调用、缓存（Cache）管理以及分布式锁（Redis Lock）机制，以确保用户登录状态的一致性。演示者通过 IntelliJ IDEA 编辑器，逐步在 `StockUserProcessor` 类中编写和调试代码，重点展示了如何将用户登录信息（如账户ID和通道ID）存入缓存，并使用 Redis 分布式锁来防止并发写入导致的数据不一致问题。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示 `GrpcStockUserService` 服务类中的 `userLogin` 方法，该方法接收登录请求和响应观察者。
*   **00:03 - 00:07**: 代码跳转至 `StockUserProcessor` 类，这是一个处理用户登录请求的处理器。
*   **00:07 - 00:12**: 在 `StockUserProcessor` 中，演示者开始编写 `processRequest` 方法，用于处理接收到的 `StockMessage`。
*   **00:12 - 00:17**: 代码聚焦于 `recordCache` 方法，用于记录用户缓存信息。演示者定义了多个常量，如 `STOCK_PROXY_USER_KEY` 和 `STOCK_PROXY_USER_KEY_ONLINE`。
*   **00:17 - 00:22**: 在 `recordCache` 方法中，演示者使用 `cacheManager` 获取缓存实例，并将用户ID和通道ID存入缓存。
*   **00:22 - 00:27**: 代码进入 `try` 块，演示者开始编写分布式锁逻辑，调用 `redisLockService.tryLock` 方法。
*   **00:27 - 00:32**: 代码中使用 `FieldInfoWithAnnotation` 类来获取 `onlineWrapper` 对象的字段信息，用于后续的缓存更新。
*   **00:32 - 00:37**: 代码逻辑判断 `onlineWrapper` 是否为 `null`，如果是，则创建一个新的 `HashMap` 来存储用户信息。
*   **00:37 - 00:42**: 代码将用户ID和通道ID存入 `accountInfos` 映射中，并在 `catch` 块中处理异常。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **gRPC 服务接口**:
        ```java
        @Override
        public void userLogin(LoginRequest request, StreamObserver<LoginResponse> responseObserver) {
            LoginResponse response = null;
            try {
                // 根据用户ID，查找获取用户对象信息(校验判断，如果用户不存在，则抛出异常提示)
                // ... (后续代码)
            } catch (Exception e) {
                // ... (异常处理)
            }
        }
        ```
    *   **缓存处理器**:
        ```java
        public class StockUserProcessor extends AbstractStockProcessor implements IBinaryAnnotation {
            // ... (其他代码)
        }
        ```
    *   **缓存记录方法**:
        ```java
        private void recordCache(ChannelId channelId, LoginResponse response) {
            // 1. 记录通过ID与账户ID的关联缓存信息
            Cache cache = cacheManager.getCache(GlobalConstants.STOCK_PROXY_USER_KEY);
            cache.put(channelId.asLongText(), response.getAccountID());

            // 2. 记录在线用户缓存
            Cache.ValueWrapper onlineWrapper = cache.get(GlobalConstants.STOCK_PROXY_USER_KEY_ONLINE);

            // 3. 分布式锁，防止用户同时登陆，造成缓存信息记录不一致问题
            redisLockService.tryLock(GlobalConstants.STOCK_PROXY_USER_KEY);

            // 4. 更新缓存信息
            if (null != onlineWrapper) {
                accountInfos = (Map<Long, ChannelId>) onlineWrapper.get();
            } else {
                accountInfos = new HashMap<Long, ChannelId>();
                accountInfos.put(response.getAccountID(), channelId);
            }
        }
        ```
    *   **常量定义**:
        ```java
        String STOCK_PROXY_USER_KEY = "stock:proxy:user";
        String STOCK_PROXY_USER_KEY_ONLINE = "stock:proxy:user:online";
        String STOCK_QUOTE_LAST_PRICE_KEY = "stock:quote:lastprice";
        String STOCK_QUOTE_OPEN_PRICE_CUR_KEY = "stock:quote:openprice:cur";
        String STOCK_QUOTE_CLOSE_PRICE_CUR_KEY = "stock:quote:closeprice:cur";
        String STATUS_OR = "200";
        String OAUTH_KEY_USER_DETAILS = "oauth:user:details";
        ```

---

### 4) 关键场景与演示描述

*   **场景一：用户登录服务接口** (00:00-00:03)
    *   演示者在 `GrpcStockUserService` 类中展示了 `userLogin` 方法，该方法用于处理用户的登录请求。方法接收一个 `LoginRequest` 对象和一个 `StreamObserver<LoginResponse>` 对象，用于异步返回响应。

*   **场景二：登录请求处理** (00:03-00:12)
    *   代码跳转到 `StockUserProcessor` 类，这是一个处理用户登录请求的处理器。演示者开始编写 `processRequest` 方法，该方法接收 `ChannelHandlerContext` 和 `StockMessage` 作为参数，用于处理接收到的登录消息。

*   **场景三：缓存记录逻辑** (00:12-00:22)
    *   演示者在 `recordCache` 方法中，首先通过 `cacheManager` 获取缓存实例，并将用户ID和通道ID存入缓存。接着，他定义了多个常量，用于标识不同的缓存键。

*   **场景四：分布式锁实现** (00:22-00:37)
    *   代码进入 `try` 块，演示者调用 `redisLockService.tryLock` 方法，使用 `STOCK_PROXY_USER_KEY` 作为锁的键。接着，他使用 `FieldInfoWithAnnotation` 类来获取 `onlineWrapper` 对象的字段信息，用于后续的缓存更新。

*   **场景五：缓存更新与异常处理** (00:37-00:42)
    *   代码逻辑判断 `onlineWrapper` 是否为 `null`，如果是，则创建一个新的 `HashMap` 来存储用户信息。接着，他将用户ID和通道ID存入 `accountInfos` 映射中，并在 `catch` 块中处理异常。

---

以上是根据视频画面进行的结构化技术分析。
