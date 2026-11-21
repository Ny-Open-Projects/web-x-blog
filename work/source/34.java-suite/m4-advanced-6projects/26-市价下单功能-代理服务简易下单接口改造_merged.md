# 26-市价下单功能-代理服务简易下单接口改造 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去完成代理服务的改造,去实现试驾下单接口的调用处理。

首先,我们需要增加获取用户账号的方法。

由于交易记录它需要关联交易账户的ID,所以我们要通过代理服务直接将账户ID传递过来。

不需要再通过客户端传递,减少不必要的参数。

由于很多交互接口都需要用到交易账户ID,针对于这个方法具有普遍性,我们就把它封装在抽箱内当中。

下面是该方法的具体实现。

将它copy到代码里面,放在AppStack Stock Processor复集处理器下面,将代码放在最下面,导入相关的包。

这个是内体下面的。

我们来看一下它是如何实现的。

首先,它从缓存当中获取交易。

我们来看一下它从缓存当中获取交易账户的ID。

之前,咱们在用户登录的时候,将用户的交易账号ID和Channel通道ID进行了关联,然后将这个关联信息放入至缓存当中。

这里我们就需要使用到该缓存,通过Channel ID来获取当前交易账户的ID信息。

如果是没有获取有效的交易账户ID,在这里我们就要抛出异常提示信息。

用户登录接口缓存的处理逻辑,咱们可以再回顾一下。

在Stock User Processor下面,我们找到用户登录的请求处理方法。

下面有个缓存的处理,Record Catch。

Record Catch方法下面,首先做的就是记录通道ID以及账户ID的关联缓存。

可以看到,它将通道ID和交易账户的ID做了一个关联缓存。

再回到AppStack Stock Processor下面。

在这里,咱们就能看到,它将交易账户的ID和通道ID做了一个关联缓存。

在这里,咱们就能够通过它的通道ID去获取对应的交易账户ID。

好,这块逻辑处理完成之后,接下来咱们就要去改造下单处理器的实现逻辑。

回到讲义当中。

下单处理器的改造,最主要是修改两部分。

第一,要去增加交易账户ID的传递。

第二,就是外围要去增加异常的补货处理。

因为咱们知道,4家下单接口会抛出对应的交易账户ID。

如果我们在代理服务端不增加外围异常的补货,那么客户端就无法获取到业务异常的提示信息。

好,那我们回到代码当中,做相应的修改。

打开Stock Deal Processor。

我们在外围添加CheckEdge异常补货。

这里面是要补货两类异常,还有一类的话是ComponentException,咱们的业务异常。

将调用的处理逻辑。

我们Copy进来。

这里我们要去设置交易账户ID。

Set Account ID。

要用附内的Get Use Account ID方法。

这里我们要传递连接通道。

下面就要去组装异常盘回消息。

那首先,我们将Stock Head以及Response Message抽取出来。

Response Message,Stock Head,Ploto。

在这里做个替换。

把它驱除。

下面我们就去封装。

业务异常。

Log点Add。

1点Get Message。

Stock Head。

再用附内的生成头部信息方法。

Stock Message。

Get Stock Head。

然后传递错误码信息。

Response Message。

New Builder。

Stock Head。

将头部信息传递进去。

Set Message。

获取。

错误码的异常。

异常提示信息。

要用Build方法进行构建。

好。

最后呢,咱们就要封装系统异常的提示信息。

同样先打印错误日志。

这里呢,我们就做个copy。

这一块就要修改一下。

Global Consistence。

返回错误状态。

然后将异常提示信息呢,返回出去就可以。

1点Get Message。

好,这个就是系统异常的封装返回处理。

好,那咱们回到简易当中。

这一讲,咱们就完成了代理服务的改造。

在原来的简易下单接口的基础上面做了一个调整。

实现了4加单接口功能的调用。

那这一讲内容,咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的股票交易系统（基于 Netty 和 gRPC）的开发课程。讲师正在讲解如何改造代理服务，以实现“下单”功能。核心内容是将用户账户ID的获取逻辑从客户端移至代理服务端，通过缓存机制来减少网络传输和参数冗余。同时，讲师演示了如何在具体的处理器 `StockDealProcessor` 中，通过 `try-catch` 块捕获并封装业务异常，将 `ComponentException` 转换为标准的 `ResponseMessage` 返回给客户端。整个过程体现了服务端解耦、异常处理和响应封装的工程实践。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 文档中展示课程大纲，定位到“3.3 代理服务改造”章节。
*   **00:00:05 - 00:00:15**：讲师讲解“3.3.1 增加获取用户账号方法”，说明将用户ID从客户端传递改为由代理服务通过 `ChannelHandlerContext` 获取，并封装到抽象类 `AbstractStockProcessor` 中。
*   **00:00:15 - 00:00:30**：讲师切换到 IntelliJ IDEA，展示 `AbstractStockProcessor.java` 文件，重点讲解 `getUserAccountId` 方法的实现。
*   **00:00:30 - 00:00:45**：讲师在 `AbstractStockProcessor.java` 中，通过 `cacheManager.getCache` 获取缓存，从 `channel.id()` 中提取交易账户ID。
*   **00:00:45 - 00:01:00**：讲师演示 `catch` 块，展示如何捕获 `ComponentException` 并封装成 `ResponseMessage`。
*   **00:01:00 - 00:01:15**：讲师在 `StockDealProcessor.java` 中，演示如何调用 `AbstractStockProcessor` 中的 `getUserAccountId` 方法，并将结果设置到 `PlaceOrderRequest` 中。
*   **00:01:15 - 00:01:30**：讲师演示如何调用 gRPC 服务端下单接口 `placeOrder`。
*   **00:01:30 - 00:01:45**：讲师演示如何封装返回的 `PlaceOrderResponse`，并将其转换为 `ResponseMessage`。
*   **00:01:45 - 00:02:00**：讲师在 `catch` 块中，演示如何根据 `ComponentException` 的 `errorCodeEnum` 和 `message` 来构建 `ResponseMessage`。
*   **00:02:00 - 00:02:15**：讲师在 `StockDealProcessor.java` 中，演示如何使用 `GlobalConstants` 和 `GlobalChannelTrafficCounter` 等全局配置。
*   **00:02:15 - 00:02:30**：讲师切换回 Typora 文档，展示“3.3.2 登陆接口记录账户信息”和“3.3.3 下单处理器改造”的内容，为后续章节做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **核心目标**：将用户ID的传递从客户端移至代理服务端，减少不必要的参数传递。
*   **抽象类封装**：`com.itcast.trade.stock.quote.proxy.processor.AbstractStockProcessor`。
*   **方法签名**：
    ```java
    protected Long getUserAccountId(ChannelHandlerContext ctx) throws ComponentException
    ```
*   **缓存获取逻辑**：
    ```java
    Cache cache = cacheManager.getCache(GlobalConstants.STOCK_PROXY_USER_KEY);
    String channelId = ctx.channel().id().asLongText();
    if (cache != null && cache.get(channelId) == null) {
        return Long.parseLong(channelId);
    }
    ```
*   **异常处理**：
    ```java
    throw new ComponentException(ApplicationErrorCodeEnum.SYS_NOT_ACCESS_USER);
    ```
*   **异常封装**：
    ```java
    log.error(e.getMessage(), e);
    stockHead = generateStockHead(stockMessage.getStockHead(), e.getErrorCodeEnum().getCode());
    responseMessage = ResponseMessage.newBuilder().setStockHead(stockHead).setMessage(e.getErrorCodeEnum().getMessage()).build();
    ```

#### 代码关键内容

*   **`AbstractStockProcessor.java`**：
    *   `protected Long getUserAccountId(ChannelHandlerContext ctx) throws ComponentException`
    *   使用 `cacheManager` 获取缓存。
    *   从 `channel.id()` 提取 `channelId`。
    *   如果缓存中不存在，则抛出 `ComponentException`。
*   **`StockDealProcessor.java`**：
    *   `public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage)`
    *   `try` 块中：
        *   获取 `PlaceOrderData`。
        *   构建 `PlaceOrderRequest`，并调用 `getUserAccountId` 设置 `accountId`。
        *   调用 `stockTradeDealServiceBlockingStub.placeOrder`。
        *   封装返回的 `PlaceOrderResponse`。
    *   `catch (ComponentException e)` 块：
        *   记录错误日志。
        *   生成 `StockHead`。
        *   构建 `ResponseMessage`。
    *   `catch (Exception e)` 块：
        *   记录错误日志。
        *   生成 `StockHead`。
        *   构建 `ResponseMessage`。

---

### 4) 关键场景与演示描述

1.  **场景一：抽象类封装用户ID获取逻辑**
    *   **描述**：讲师在 Typora 文档中指出，为了减少客户端传递参数，需要将获取用户ID的逻辑封装到抽象类 `AbstractStockProcessor` 中。随后，讲师在 IntelliJ IDEA 中打开 `AbstractStockProcessor.java`，并定位到 `getUserAccountId` 方法。
    *   **演示**：讲师通过 `cacheManager.getCache` 获取一个名为 `STOCK_PROXY_USER_KEY` 的缓存，并从 `channel.id()` 中提取交易账户ID。如果缓存中不存在，则抛出 `ComponentException`。

2.  **场景二：在具体处理器中调用抽象方法**
    *   **描述**：讲师在 `StockDealProcessor.java` 中，演示如何在 `processRequest` 方法中调用 `AbstractStockProcessor` 的 `getUserAccountId` 方法。
    *   **演示**：讲师在 `try` 块中，先获取 `PlaceOrderData`，然后构建 `PlaceOrderRequest`，并调用 `getUserAccountId` 方法设置 `accountId`。接着，调用 gRPC 服务端的 `placeOrder` 方法。

3.  **场景三：异常处理与响应封装**
    *   **描述**：讲师演示如何在 `catch` 块中处理 `ComponentException`，并将其封装为标准的 `ResponseMessage`。
    *   **演示**：讲师在 `catch (ComponentException e)` 块中，首先记录错误日志。然后，根据 `e.getErrorCodeEnum()` 获取错误码和错误信息，生成 `StockHead`。最后，使用 `ResponseMessage.newBuilder()` 构建并返回 `ResponseMessage`。

4.  **场景四：全局配置与日志记录**
    *   **描述**：讲师在 `StockDealProcessor.java` 中，演示如何使用 `GlobalConstants` 和 `GlobalChannelTrafficCounter` 等全局配置。
    *   **演示**：讲师在 `catch` 块中，使用 `GlobalConstants` 获取常量，并使用 `GlobalChannelTrafficCounter` 记录流量。同时，使用 `log.error` 记录异常信息。

5.  **场景五：代码结构与流程控制**
    *   **描述**：讲师在 `StockDealProcessor.java` 中，演示了 `try-catch` 块的结构和流程控制。
    *   **演示**：讲师在 `try` 块中，依次执行获取参数、构建请求、调用服务、封装响应等步骤。在 `catch` 块中，根据异常类型进行不同的处理，如记录日志、生成响应等。
