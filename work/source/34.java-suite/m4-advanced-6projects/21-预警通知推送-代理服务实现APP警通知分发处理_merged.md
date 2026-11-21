# 21-预警通知推送-代理服务实现APP警通知分发处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们开始学习和讲解代理服务去实现APP预警通知的分发功能

要实现通知的分发咱们要知道目前在线的用户信息

需要增加在线的用户反存记录

一个系统随着不断的去使用可能会有上亿的用户

但同一时间在线的用户数却不一定会有这么多

那么在发送预警通知的时候咱们只针对在线的用户进行发送

首先要在用户登录的时候增加相应的记录

这个咱们在用户登录接口实现的时候已经做了处理

咱们可以再回顾下相应的代码

回到工程当中在stock user process下面

通过record cache方法做了相应的处理

这里会记录通道和账户的关联缓存

然后还会记录在线的用户缓存记录

为了防止用户同时登录造成map信息不一致

这里需要加入分布式锁的功能

分布式锁的集成和运用咱们之前在知心服务的时候已经做了讲解

通过对分布式锁的封装它的使用就比较简单

这里是加锁的处理

最下面是对锁的释放处理

如果有新的用户登录

它会去更新相应的缓存信息

好咱们再回到讲义当中

接下来

在用户退出的时候需要做相应的清除操作

用户如果退出

Channel的连接通道就会被收回

那么在收回时呢

咱们要同时清除在线用户信息的缓存记录

这里咱们要做相应的实现

将清除部分代码做个copy

回到工程当中

定位到stockc, proxy, server-handle

在handle入MV的方法下面

我们增加对应的实现

这里先要获取到Channel的ID

咱们定义下

Channel, ID

这里会去清除用户的登录缓存

然后会去清除账户和通道的关联缓存

这里咱们将错误做个修正

需要注入分布式锁的接口

这里咱们修改下

添加outline的注写

添加注释

这个是分布式锁的实现接口

再回到刚才的代码

通过分布式锁是要保障缓存数据更新的一致性

最后要对锁进行释放处理

这里还要添加一个结束服务

好

那这个就是对用户缓存记录信息的清除处理

咱们回到讲义当中

接下来咱们要去实现代理服务的GRBC接口

去完成预警通知的分发功能

这里将代码做个引用

回到工程当中

在Proxy工程下面

咱们创建一个新的包

包名叫GRBC

然后创建GRBC接口的实现类

然后创建GRBC接口的实现类

名称叫GRBC Talk Proxy Service

这里将代码引入进来

检查并修正相关的错误

将包名做个修正

这个是GRBC下面的包

将这个包给做一个修正

将Channel ID导入进来

下面这个One Message Data

它是在Netty的包下面

因为上面已经引入了GRBC的包

这里咱们就要采用它完整的包名

在Netty下面

我们就要采用它完整的包名

咱们去Copy一下

再回到刚才的代码

删贴

这里也替换一下

好

错误都已经修正完成

那咱们来看一下

整体的实现处理流程

这个接口是代理服务

提供给交易调度服务使用的

首先它会去判断

接受的参数里面

有没有预警通知数据

如果是存在

那么接着处理下面的逻辑

为了提升处理效率

在这里根据账户ID

对数据做了一个分组汇总

如果一个用户下面有多条预警通知

那么分组汇总之后就会放在一起

下发的时候就不会逐条发送

而是作为一个整体一次性发送给客户端

这样就减少了传输开销

提升了整体的处理性能

下面是要组装推送给客户端的头部消息

这里要去标识接口数据类型

然后第四个步骤

要获取当前在线的用户缓存

拿到在线用户缓存之后

接着对通知消息做便利处理

在做消息发送的时候

它会根据Channel通道信息

查找通道是否有效存在

如果通道是正常

接着才能够进行消息的下发

下面就是对每个账户的

所有预警通知消息进行便利转换处理

这里采用的数据集合

是可以支持批量消息的发送

消息转换处理完成之后

会去记录发送的预警通知消息ID

然后去组装完整的客户端消息

最后通过Channel通道将消息发送给客户端

接口调用成功之后

也会将响应消息返回给调用方

也就是交易调度服务

这里它会返回已经接收处理的预警通知消息ID

好

这个就是代理服务预警通知消息

推送的整体处理流程

最后还要检查工程配置

是否配置了GRBC服务端信息

咱们检查一下

好

在这里已经配置了GRBC的服务端信息

这里指定了一个端口是8977

好

那咱们回到讲义当中

这一讲就是对代理服务实现APP

预警通知分发功能的讲解

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-proxy` 的股票交易代理服务的开发教程，重点讲解了如何实现“APP预警通知的分发功能”。该功能的核心是：当系统产生预警通知时，需要精准地推送给当前在线的APP客户端，而不是所有用户。实现方案依赖于一个基于 Redis 的在线用户缓存机制，通过 `StockProxyServerHandler` 监听客户端的连接和断开事件，并在 `StockUserProcessor` 中维护用户与通道的映射关系。服务端通过 gRPC 接口接收预警通知，根据用户ID从缓存中查找在线通道，然后通过 Netty 的 `channel.writeAndFlush` 方法将消息推送给对应的客户端。整个过程涉及缓存管理、分布式锁（RedisLock）和 gRPC 服务调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，当前章节为“3.3 代理服务实现APP预警通知分发功能”。
*   **00:00:05 - 00:00:15**: 讲解核心概念：系统有上亿用户，但预警通知只针对“在线用户”发送。
*   **00:00:15 - 00:00:30**: 展示代码 `recordCache` 方法，说明用户登录时会将 `ChannelId` 和 `accountId` 的映射关系存入缓存。
*   **00:00:30 - 00:00:45**: 展示 `handlerRemoved` 方法，说明当客户端断开连接时，会从缓存中移除对应的用户记录。
*   **00:00:45 - 00:01:00**: 展示 `StockProxyServerHandler` 的 `@Autowired` 注入的 `RedisLockService` 和 `StockProcessorFactory`。
*   **00:01:00 - 00:01:15**: 展示 `GrpcStockProxyService` 的 gRPC 服务类定义，用于接收外部的预警通知请求。
*   **00:01:15 - 00:01:30**: 展示 `notifyWarMessage` 方法的实现，核心逻辑是根据 `accountId` 从缓存中获取在线的 `ChannelId`。
*   **00:01:30 - 00:01:45**: 展示 `for-each` 循环，遍历 `accountId` 和 `messageDataList`，通过 `StockProxyServerHandler.channels.find` 方法查找对应的 `ChannelId`。
*   **00:01:45 - 00:02:00**: 展示构建 `WarnMessageDataResp` 消息体，并调用 `channel.writeAndFlush` 将消息推送给客户端。
*   **00:02:00 - 00:02:15**: 展示 `responseObserver` 的 `onNext` 和 `onCompleted` 方法，用于处理 gRPC 服务的响应。
*   **00:02:15 - 00:02:30**: 展示 `bootstrap-dev.yml` 配置文件，其中配置了 `grpc` 服务的 `client` 地址和 `keepAliveWithoutCalls` 参数。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.3 代理服务实现APP预警通知分发功能`。
    *   核心概念：`一个系统可能有上亿的用户，但同一时间在线用户却不会有这么多，在发送预警通知的时候，只针对在线用户发送。`
    *   代码注释：`记录缓存`、`清除用户登陆缓存`、`获取账户信息`、`清除在线用户缓存`、`解锁处理`。

*   **关键代码片段**:

    **1. `recordCache` 方法 (用户登录时记录缓存)**

    ```java
    private void recordCache(ChannelId channelId, LoginResponse response) {
        Cache cache = cacheManager.getCache(GlobalConstants.STOCK_PROXY_USER_KEY);
        cache.put(channelId.asLongText(), response.getAccountId());

        // 分布式锁，防止同时写入，MAP信息记录不一致
        try {
            Map<Long, ChannelId> accountInfos = null;
            redisLockService.tryLock(GlobalConstants.STOCK_PROXY_USER_KEY);
            accountInfos = (Map<Long, ChannelId>) onlineWrapper.get();
            if (null != accountInfos) {
                accountInfos.put(response.getAccountId(), channelId);
            } else {
                accountInfos = new HashMap<Long, ChannelId>();
                accountInfos.put(response.getAccountId(), channelId);
            }
            onlineWrapper.set(accountInfos);
        } catch (Exception e) {
            log.error(e.getMessage(), e);
        } finally {
            redisLockService.unlock(GlobalConstants.STOCK_PROXY_USER_KEY);
        }
    }
    ```

    **2. `handlerRemoved` 方法 (用户断开连接时清除缓存)**

    ```java
    @Override
    public void handlerRemoved(ChannelHandlerContext ctx) throws Exception {
        // channelGroup 会自动调用处理，可以不用写
        channels.remove(ctx.channel());
        // 主动关闭，释放资源
        ctx.close();
    }
    ```

    **3. `GrpcStockProxyService` 服务类定义**

    ```java
    @GrpcService
    @Log4j2
    public class GrpcStockProxyService extends StockProxyServiceGrpc.StockProxyServiceImplBase {
        @Autowired
        private CacheManager cacheManager;
    }
    ```

    **4. `notifyWarMessage` 方法 (核心分发逻辑)**

    ```java
    public void notifyWarMessage(NotifyWarMessageRequest request, StreamObserver<WarnMessageResponse> responseObserver) {
        // 1. 根据账户ID，汇总分组数据
        Map<Long, List<WarnMessageData>> accNotifyMessages = request.getWarnMessageDataList().stream()
            .collect(Collectors.groupingBy(WarnMessageData::getAccountId));

        // 2. 组装推送给客户端的头部消息
        StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder()
            .setRequestType(StockHeadProto.RequestType.NOTIFY_WARN_MESSAGE)
            .setSeqId(warnMessageSeqId++)
            .setStatus(GlobalConstants.STATUS_OK)
            .build();

        // 3. 获取当前在线用户缓存
        Cache.ValueWrapper onlineWrapper = cache.get(GlobalConstants.STOCK_PROXY_USER_KEY_ONLINE);
        if (null == onlineWrapper) {
            // 4. 获取当前在线用户缓存
            Map<Long, ChannelId> accountInfos = (Map<Long, ChannelId>) onlineWrapper.get();
            if (null != accountInfos) {
                accNotifyMessages.forEach((accountId, messageDataList) -> {
                    ChannelId channelId = StockProxyServerHandler.channels.find(accountId);
                    if (null != channelId) {
                        // 5. 构建消息体
                        WarnMessageDataResp.Builder messageDataResp = WarnMessageDataResp.newBuilder();
                        messageDataResp.addAllIds(messageDataList.stream().map(WarnMessageData::getId).collect(Collectors.toList()));
                        // 6. 通过channel通道，将消息发送至客户端
                        channel.writeAndFlush(responseMessage);
                    }
                });
            }
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：用户登录缓存记录**
    *   **描述**: 讲师在 `StockUserProcessor` 类中展示 `recordCache` 方法。该方法在用户登录时被调用，首先将 `ChannelId` 和 `accountId` 的映射关系存入 `Cache`。然后，通过 `redisLockService.tryLock` 获取分布式锁，确保在高并发下缓存数据的一致性。最后，将 `accountId` 和 `ChannelId` 的映射关系存入 `onlineWrapper`，并释放锁。

*   **场景二：用户断开连接清除缓存**
    *   **描述**: 讲师在 `StockProxyServerHandler` 类中展示 `handlerRemoved` 方法。当客户端主动断开连接时，该方法会被调用。它会从 `channels` 集合中移除对应的 `ChannelId`，并调用 `ctx.close()` 主动关闭通道。同时，它会调用 `cache.evict(accountId)` 从缓存中移除该用户的记录，确保缓存数据的实时性。

*   **场景三：gRPC 服务接收并分发预警通知**
    *   **描述**: 讲师在 `GrpcStockProxyService` 类中展示 `notifyWarMessage` 方法。该方法接收一个 `NotifyWarMessageRequest` 请求，其中包含多个 `WarnMessageData`。首先，它根据 `accountId` 对消息进行分组。然后，它从缓存中获取当前在线用户的 `ChannelId` 映射关系。接着，它遍历每个 `accountId`，通过 `StockProxyServerHandler.channels.find` 方法查找
