# 30-代理服务登录鉴权-登录鉴权拦截处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始学习代理服务增加登录健全拦截的处理功能

这一块逻辑该如何实现处理呢?咱们回到代码当中

找到代理服务的数据接收处理器

Stalker Proxy Server Handle

既然要做登录健全,那么就必须在接收数据之前就要开始做处理

这个逻辑应该是要放在业务逻辑执行之前

所以在这里咱们加上教验用户登录健全处理

那么咱们再去封装一个方法

CheckLogic传递Channel Handler Context

传递Stalker Message

咱们对这个方法做个实现

添加注释检查用户是否已登录

这一块处理逻辑是怎样呢?

首先咱们要判断用户所发过来的接口请求

如果用户发送的是登录接口类型

那在这里就不需要做拦截判断

所以首先咱们要去排除用户登录接口

Stalk Message

Get Stock Head

从头部获取他的请求类型

通过PB里面的枚举做判断

Use Login

Use Login这个枚举不存在

咱们要去PB文件里面增加对应的接口定义

回答了这些问题

到PB数据结构工程

找到PB的头部文件定义

在这里咱们增加一个接口请求类型

用户登录

Use Login

接着咱们通过脚本重新编一下

这个是在Net下面

好编译完成

再回到刚才的代码处理逻辑

Stalk Blocks

Service Handle下面

这里就选取刚才咱们所定义的Use Login接口

接着咱们要去获取

Channel的ID

Stream Channel ID

Handle Context

这个转换为长整形的文本

也就是一个字符类型

接着咱们就要去查询缓存

Cache

Cache Manager

Cache Manager

Cache Manager这里也先将它注入进来

添加注释

这个是缓存管理器

再回到刚才Check Login的方法

保路对应的依赖

在Spring Work下面

Get Cache

传递了建值

Stock

Moxy

User Key

然后做一个唯空判断

如果这个缓存不存在

咱们接下来逻辑就要给它抛出一个异常

Slu

New

Complaint

一个Savage

Application

Add Code

给它一个错误码

提示呢

用户未有效登录

外层呢

咱们要抛出异常登录

Sluice

Complaint

Except

好

那咱们再回到讲义当中

代理服务

登录健全的拦截处理呢

只需要加上Check Login方法

这个呢

一定要在业务处理之前

注意它的处理顺序

否则是不能做到严格的工资

接下来咱们再回顾一下

整体的处理流程

在这里咱们是封装了Check Login的方法

用于呢

健全逻辑的处理

如果是不符合健全要求

咱们要抛出异常

中断了逻辑的处理

接下来的逻辑呢

就没必要继续进行

然后呢

咱们要返回错误提示消息

Check Login方法呢

咱们必须要先排除对应的登录方法

登录借口呢

必须要暴露公开出来

否则的话呢

你是没办法去做到

权限拦截的工资

因为登录方法都不能进来的话呢

就不会有用户的缓存信息

整个的判断处理逻辑呢

也比较简单

是通过缓存

去查

查询判断用户呢

是否已经登录

这里要注意一下

有了登录缓存的记录

那么在用户推出的时候呢

也需要将缓存做清楚

这个处理逻辑

在后面实现APP预警通知

推送的功能当中

还会做具体的实现

在这里

咱们是侧重掌握代理服务

登录健全功能的处理

好

那这一讲内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-proxy”的Java项目中，如何在Netty代理服务中实现用户登录鉴权拦截处理的开发演示。讲师通过在IntelliJ IDEA中逐步修改 `StockProxyServerHandler` 类的 `checkLogin` 方法，实现了基于缓存（Cache）的用户登录状态校验。核心逻辑是：首先判断请求类型是否为登录请求，然后从ChannelHandlerContext中获取用户的channelId，最后通过Spring Cache管理器查询该channelId对应的缓存数据。如果缓存中不存在或为空，则抛出 `ComponentException` 异常，从而中断后续业务处理，实现鉴权拦截。整个过程展示了如何将业务逻辑（鉴权）封装到Netty的ChannelHandler中，并利用Spring框架的缓存能力进行状态管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示课程PPT，标题为“3.3 代理服务增加鉴权拦截处理”，并列出本节目标、步骤和实现。
*   **00:00:05 - 00:00:15**: 讲师在IDE中打开 `StockProxyServerHandler.java` 文件，定位到 `checkLogin` 方法的定义位置。
*   **00:00:15 - 00:00:30**: 讲师开始编写 `checkLogin` 方法的逻辑。首先判断请求类型是否为 `StockHeadProto.RequestType.USER_LOGIN`。
*   **00:00:30 - 00:00:45**: 讲师从 `channelHandlerContext` 中获取当前用户的 `channelId`。
*   **00:00:45 - 00:01:00**: 讲师引入Spring Cache管理器 `cacheManager`，并尝试获取一个名为 `STOCK_PROXY_USER_KEY` 的缓存。
*   **00:01:00 - 00:01:15**: 讲师编写条件判断语句，检查缓存对象 `cache` 是否为 `null`，或者 `cache.get(channelId)` 的结果是否为 `null`。
*   **00:01:15 - 00:01:30**: 讲师在条件为真时，抛出 `ComponentException` 异常，并传入错误码 `ApplicationErrorCodeEnum.NOT_VALID_LOGIN`。
*   **00:01:30 - 00:01:45**: 讲师在PPT上总结，说明 `checkLogin` 方法的作用是封装鉴权逻辑，如果不符合要求则抛出异常中断处理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **章节标题**: “3.3 代理服务增加鉴权拦截处理”
    *   **方法签名**: `private void checkLogin(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) throws ComponentException`
    *   **核心逻辑描述**:
        *   封装 `checkLogin` 方法，用于鉴权逻辑处理，如果不符合鉴权要求，抛出异常，中断逻辑处理，返回错误提示信息。
        *   `checkLogin` 方法，先要排除登陆等不需要鉴权的接口，然后通过缓存查询判断用户。

*   **代码关键内容**:
    *   **方法定义**:
        ```java
        private void checkLogin(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) throws ComponentException {
        ```
    *   **请求类型判断**:
        ```java
        if(stockMessage.getStockHead().getRequestType() != StockHeadProto.RequestType.USER_LOGIN) {
        ```
    *   **获取channelId**:
        ```java
        String channelId = channelHandlerContext.channel().id().asLongText();
        ```
    *   **缓存查询**:
        ```java
        Cache cache = cacheManager.getCache(GlobalConstants.STOCK_PROXY_USER_KEY);
        ```
    *   **鉴权失败抛出异常**:
        ```java
        if(null == cache || cache.get(channelId) == null) {
            throw new ComponentException(ApplicationErrorCodeEnum.NOT_VALID_LOGIN);
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：方法定义与初始化**
    *   讲师在IDE中定位到 `StockProxyServerHandler` 类，并在 `channelRead` 方法中添加了 `checkLogin` 方法的调用。
    *   讲师在PPT上展示了 `checkLogin` 方法的完整签名和注释，明确了方法的输入参数和返回类型。

*   **场景二：请求类型校验**
    *   讲师在IDE中编写了 `if(stockMessage.getStockHead().getRequestType() != StockHeadProto.RequestType.USER_LOGIN)` 的条件判断语句。
    *   该语句用于排除非登录请求，确保只有登录请求才会进入后续的鉴权逻辑。

*   **场景三：获取用户标识**
    *   讲师通过 `channelHandlerContext.channel().id().asLongText()` 获取了当前用户的 `channelId`。
    *   这个 `channelId` 是Netty中用于标识一个客户端连接的唯一标识符，是后续缓存查询的关键。

*   **场景四：缓存鉴权**
    *   讲师通过 `cacheManager.getCache(GlobalConstants.STOCK_PROXY_USER_KEY)` 获取了缓存管理器。
    *   讲师编写了 `if(null == cache || cache.get(channelId) == null)` 的条件判断，用于检查用户是否已登录。
    *   如果缓存中不存在该用户的登录状态，则抛出 `ComponentException` 异常，错误码为 `NOT_VALID_LOGIN`。

*   **场景五：异常处理与总结**
    *   讲师在PPT上总结了 `checkLogin` 方法的作用，强调了其在拦截非登录请求和验证用户登录状态中的关键作用。
    *   讲师通过IDE中的代码高亮和注释，清晰地展示了整个鉴权逻辑的流程。
