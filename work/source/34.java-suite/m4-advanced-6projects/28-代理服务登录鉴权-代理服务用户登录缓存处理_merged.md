# 28-代理服务登录鉴权-代理服务用户登录缓存处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现代理服务用户接口请求数据的处理流程。

首先,咱们去定义responseMessage返回对象,接着定义返回头部信息,stockhead,接着去实现请求参数的转换处理,定义loginData,从stockMessage当中拿取loginData信息。

换成咱们加上checkH,conclude,t,这里是系统异常信息的封装返回处理,将异常日子返回出来,组装头部消息,用生成头部信息的方法,传递stockhead,以及处理的状态,stace,add,组装responseMessage返回消息对象,new builder。

将头部信息设置进去。

设置message消息内容,将异常信息返回出去,要用build构建方法。

最后,要将信息发送返回给客户端,通过channel,handler,context,将responseMessage输出返回给客户端。

给出一个日子提示,copy process的名称,UseLogin的方法。

提示呢?

处理结束。

好,接着咱们来实现内部的处理调用逻辑。

定义LoginRequest,new builder。

咱们在这里呢,要将转发的请求参数呢,设置进去。

login data,get user number,设置用户的密码。

同样,从用户端所接受的login data里面呢,获取用户传递的密码。

然后进行build。

接下来呢,就是调用远程的GRVC登录接口。

定义呢,接受的返回对象,response,通过user服务接口,信息远程调用。

传递request对象。

调用完成之后,要对处理结果做一个判断,loboconsistence,判断是否处理成功。

response,拿到它的状态。

接着,就是对用户返存信息的处理。

调用record cache方法。

拿取channel ID。

传递了response返回对象。

这个ID呢,是一个方法。

接下来呢,服务端要去记录channel,stock,blocksy,servor handle。

之前呢,咱们定义了个channel groups,对不对?

现在呢,咱们要将用户登录的有效连接通道呢,加入进去,context.channel。

咱们可以看一下,channel是这个对象,是一个channel group。

之前呢,咱们也做了讲解。

接下来呢,就要去返回处理报文。

这个呢,是返回的程序。

成功处理报文。

stock head。

组装呢,它的头部消息。

传递stock message.get stock head。

状态呢,为处理成功。

接着,咱们还去组装接口的返回消息体。

login.dat.response.new builder。

要设置呢,用户的信息。

这个呢,就从调用结果当中,去拿取用户信息。

response.get.

创造的usid。

然后呢,设置账户的ID。

从response对象当中呢,去拿取它们的ID。

点击build。

再用build。

进行构建。

然后,组装客户端的返回消息。

response.message。

new builder。

将头部信息设置进去。

stock head。

再设置login.dat的信息。

设置message。

从response对象当中获取。

最后,该用build进行构建。

这里呢,是成功报问的处理逻辑。

如果是调用失败呢。

那就要返回失败的报问数据。

同样,组装一个stock head。

stock message。

get stock head。

这里的状态呢,就要标示为失败。

然后,组装response message对象。

设置头部信息。

这里呢,就没有业务消息体。

直接设置message。

好,在这里呢,就完成了代理服务对用户登录接口的调用处理逻辑。

咱们回到讲义当中。

这里为了提升健全处理速度,咱们加入了ladies缓存。

登录成功之后呢,会去记录用户的信息。

用户登录成功之后呢,同样咱们也会将他的channel,纳入统一的channel group当中进行管理。

这样呢,就具有接收广播消息的权限。

如果需要发送广播消息,那么通过channel group进行一个便利寻发就可以实现。

在这里缓存的处理,咱们也运用到了分布式锁。

在这里呢,咱们是先将他移植过来,让大家呢,有一个初步的认识,了解他相关的用法。

对具体的实现呢,咱们暂时不做讲解。

在这里咱们是侧重代理服务登录健全的处理。

后面章节当中,咱们还会对分布式锁方案再做详细的讲解。

接下来呢,还去开启Splink cache的缓存功能。

因为这里呢,用户登录的时候,咱们用到了ladies缓存。

处理。

缓存的集成配置也比较简单。

在这里咱们要添加两个依赖。

一个呢,是自动化的缓存依赖。

另外一个呢,是缓存实现的具体依赖。

在这里呢,是基于ladies实现的缓存处理。

那咱们回到用户代理服务工程当中。

去查看POM文件。

检查了有没有添加进来。

缓存依赖呢,在这里已经添加进来了。

咱们可以看到,这两个组件呢,都已经加入成功。

接下来,

还要去检查它的启动内,是否开启了缓存的注解。

启动内的开启缓存功能的注解呢,也已经加入进来。

那咱们回到讲义当中。

在这里呢,代理服务也就实现了7K的集成配置。

这一讲呢,咱们是对代理服务,用户登录接口,调用逻辑的实现。

那这一讲内容呢,咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-proxy` 的 Java 项目的技术实现演示，主要聚焦于**代理服务的用户登录功能**。演示者在 IntelliJ IDEA 开发环境中，逐步讲解并编写 `StockUserProcessor.java` 类中的 `processRequest` 方法。该方法的核心流程包括：1) 解析并转换客户端传入的登录请求参数；2) 调用远程 gRPC 服务进行用户登录验证；3) 根据验证结果，将用户信息缓存到本地（如 Redis）；4) 构建并返回包含登录结果的响应消息。整个过程体现了基于 Netty 的网络通信、gRPC 的远程调用、Redis 的缓存机制以及 Spring Boot 的配置和注解应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 开场，展示项目结构和 `StockUserProcessor.java` 文件。
*   **00:00:05 - 00:00:15**: 代码编辑器中，演示者将光标定位到 `processRequest` 方法的开始处，准备进行逻辑编写。
*   **00:00:15 - 00:00:30**: 逐步编写代码，首先声明 `responseMessage` 和 `stockHead` 变量，并开始处理请求参数。
*   **00:00:30 - 00:00:45**: 将 `stockMessage` 中的 `LoginData` 转换为 `LoginRequest` 对象。
*   **00:00:45 - 00:01:00**: 调用 gRPC 服务的 `userLogin` 方法，并对返回的 `LoginResponse` 进行状态判断。
*   **00:01:00 - 00:01:15**: 如果登录成功，调用 `recordCache` 方法将用户信息缓存到 Redis。
*   **00:01:15 - 00:01:30**: 将 `LoginResponse` 中的用户 ID 信息封装到 `LoginDataResp` 中，并设置到 `responseMessage`。
*   **00:01:30 - 00:01:45**: 完成 `processRequest` 方法，返回最终的响应消息。
*   **00:01:45 - 00:02:00**: 切换到 Markdown 文档，展示本节的代码逻辑和相关知识点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / Markdown 文档内容**:
    *   **标题**: “第3章 代理服务登录鉴权实现”
    *   **子章节**: “3.2 代理服务登陆接口调用实现”
    *   **核心代码逻辑**:
        ```java
        ResponseMessage responseMessage = null;
        StockHeadProto.StockHead stockHead = null;
        try {
            // 1. 转换组装请求参数
            LoginData loginData = stockMessage.getLoginData();
            LoginRequest loginRequest = LoginRequest.newBuilder()
                .setUserNo(loginData.getUserNo())
                .setUserPwd(loginData.getUserPwd())
                .build();

            // 2. 调用远程gRPC登陆接口
            LoginResponse response = stockUserServiceStub.userLogin(loginRequest);

            if (GlobalConstants.STATUS_OK.equalsIgnoreCase(response.getStatus())) {
                // 3. 缓存处理
                recordCache(channelHandlerContext.channel().id(), response);
                // 4. 返回成功处理消息
                stockHead = generateStockHead(stockMessage.getStockHead(), GlobalConstants.STATUS_OK);
                LoginDataResp loginDataResp = LoginDataResp.newBuilder().setUserId(response.getUserId()).build();
                responseMessage = ResponseMessage.newBuilder()
                    .setStockHead(stockHead)
                    .setLoginDataResp(loginDataResp)
                    .build();
            }
        }
        ```

*   **代码关键内容**:
    *   **类**: `StockUserProcessor`
    *   **方法**: `processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage)`
    *   **服务**: `stockUserServiceBlockingStub` (gRPC 服务客户端)
    *   **数据结构**: `LoginData`, `LoginRequest`, `LoginResponse`, `StockHeadProto.StockHead`, `ResponseMessage`, `LoginDataResp`
    *   **工具类/方法**: `recordCache(...)`, `generateStockHead(...)`, `GlobalConstants.STATUS_OK`
    *   **依赖**: `@EnableCaching` 注解，用于启用 Spring Cache 功能。

---

### 4) 关键场景与演示描述

*   **场景一：代码编写与调试**
    *   **描述**: 演示者在 IntelliJ IDEA 中，逐行编写 `processRequest` 方法。他首先声明了必要的变量，然后通过 `stockMessage.getLoginData()` 获取原始数据，并使用 `LoginRequest.newBuilder()` 构建一个标准的 gRPC 请求对象。
    *   **技术点**: 展示了如何将业务数据对象转换为 gRPC 协议定义的请求对象，体现了协议的标准化。

*   **场景二：远程调用与状态判断**
    *   **描述**: 演示者调用 `stockUserServiceBlockingStub.userLogin(loginRequest)` 方法发起远程调用。接着，他通过 `response.getStatus()` 获取返回状态，并使用 `GlobalConstants.STATUS_OK.equalsIgnoreCase(response.getStatus())` 进行判断。
    *   **技术点**: 展示了 gRPC 的同步调用模式和状态码的处理逻辑，强调了业务逻辑中对服务返回结果的判断。

*   **场景三：缓存处理**
    *   **描述**: 在确认登录成功后，演示者调用 `recordCache(channelHandlerContext.channel().id(), response)` 方法。他通过 `channelHandlerContext.channel().id()` 获取当前连接的唯一标识，并将 `response` 对象作为缓存数据。
    *   **技术点**: 展示了如何利用 `ChannelHandlerContext` 获取网络连接信息，并将用户登录信息缓存到 Redis 中，实现会话管理。

*   **场景四：响应构建与返回**
    *   **描述**: 演示者将登录成功后的用户 ID 封装到 `LoginDataResp` 对象中，并将其与 `StockHead` 一起构建 `ResponseMessage`。最后，他将 `responseMessage` 返回，完成整个请求处理流程。
    *   **技术点**: 展示了如何将处理结果封装成标准的响应消息，以便客户端接收和解析。

*   **场景五：PPT 与代码对照**
    *   **描述**: 在完成代码编写后，演示者切换到 Markdown 文档，将屏幕上的代码逻辑与 PPT 中的结构化内容进行对比，帮助观众理解代码的业务逻辑和实现步骤。
    *   **技术点**: 通过文档化的方式，将复杂的代码逻辑进行结构化梳理，便于学习和回顾。
