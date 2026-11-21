# 17-SEATA集成运用-资金服务额度调整接口改造 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去改造资金服务的额度调整接口

增加全局分布式事务标识ID的网评处理

咱们回到工程代码当中

在资金服务下面

我们找到了GRBC接口

GRBC Stock Finance Service

咱们要去修改调整的是更新账户资金的接口

Update Account Balance

这里面该如何去加入分布式事务的资金呢

其实实现起来比较简单

只要一行代码就可以

咱们增加对应的实现

root context.band

这里叫绑定所传递过来的getxid

咱们还记得之前的实现

不管是交易服务还是发展服务

他们的XID呢

都是通过root context获取的

对不对

root context呢

里面会记录存储

全局分布

都是事务ID的标识

那么咱们在额度调整的接口下面

就需要将XID绑定在root context下面

root context内部是如何存储呢

它实际上是采用strived local

将相关的信息放置现成内部的存储区域

咱们可以看一下它代码实现进入band的方法

我们可以看到它放的是一个context hold

对不对

那context hold是一个什么呢

我们点击看一下

它是通过load的方法进入band的方法

去创建了

我们进入load

load里面呢

有个instance

我们再跟踪进去

instance是context call

context call呢

是创建了一个strived local

对不对

这个呢

就用到了现成的内部存储

这个就是theta

分布式事务存储的基本原理

我们添加一个注释

网定

分布式事务的全局

标示ID

只需要一行代码资金服务的更新账户资金余额的接口

就能够实现分布式事务的管理

好

那这一讲咱们就完成了资金服务

额度调整接口的改造

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个分布式金融系统（`bulls-stock`）中“资金服务额度调整”功能的代码实现与修改过程。核心内容是为 `GrpcStockFinanceService` 服务的 `updateAccountBalance` 方法增加对全局分布式事务ID（`TX_ID`）的绑定功能，以支持分布式事务的上下文传递。讲师通过IDE（IntelliJ IDEA）展示了代码的修改、调试以及底层 `RootContext` 工具类的实现原理，旨在说明如何在微服务架构中实现事务一致性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 中展示课程大纲，定位到当前章节“3.7 资金服务额度调整接口修改”。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示 `GrpcStockFinanceService` 类中的 `updateAccountBalance` 方法，指出需要在此处增加对 `TX_ID` 的绑定。
*   **00:15 - 00:25**: 讲师在代码中添加了 `RootContext.bind(request.getTxId());` 语句，并在日志中打印 `TX_ID` 以进行调试。
*   **00:25 - 00:35**: 讲师展示 `RootContext` 类的源码，解释其如何通过 `ThreadLocal` 来存储和获取 `TX_ID`。
*   **00:35 - 00:45**: 讲师展示 `ContextCoreLoader` 类的源码，解释 `RootContext` 是如何通过单例模式加载并初始化的。
*   **00:45 - 00:55**: 讲师回到 `GrpcStockFinanceService` 的代码，强调 `RootContext.bind()` 方法的作用是将当前请求的 `TX_ID` 绑定到线程上下文，以便后续服务调用可以获取到这个ID。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.7 资金服务额度调整接口修改`
    *   **修改目标**: `修改com.ictast.trade.stock.finance.service.grpc.GrpcStockFinanceService实现类，增加全局分布式事务ID的绑定`
    *   **代码片段**:
        ```java
        /**
         * 更新账户资金余额
         * @param request
         * @param responseObserver
         */
        @Override
        public void updateAccountBalance(UpdateBalanceRequest request,
                StreamObserver<UpdateBalanceResponse> responseObserver) {
            // ... 代码省略 ...
            RootContext.bind(request.getTxId());
            // ... 代码省略 ...
        }
        ```

*   **代码关键内容**:
    *   **`GrpcStockFinanceService.java`**:
        *   `updateAccountBalance` 方法：用于更新账户余额，现在需要绑定 `TX_ID`。
        *   `RootContext.bind(request.getTxId());`：这是核心修改，用于将当前请求的事务ID绑定到线程上下文。
    *   **`RootContext.java`**:
        *   `public static String getTxId() { return CONTEXT_HOLDER.get(TX_ID); }`：用于获取当前线程绑定的 `TX_ID`。
        *   `public static void bind(String txId) { ... }`：用于将 `txId` 绑定到当前线程的 `ThreadLocal` 中。
    *   **`ContextCoreLoader.java`**:
        *   `public static ContextCore load() { ... }`：负责加载 `ContextCore` 单例。
        *   `private static class ContextCoreHolder { ... }`：内部类，用于实现单例模式。

---

### 4) 关键场景与演示描述

*   **场景一：修改接口方法**
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `GrpcStockFinanceService.java` 文件，定位到 `updateAccountBalance` 方法。他首先展示了方法的原始代码，然后在方法体中添加了 `RootContext.bind(request.getTxId());` 语句，并在日志中打印 `TX_ID` 以进行调试。
    *   **技术点**: 通过在方法中调用 `RootContext.bind()`，将请求的 `TX_ID` 绑定到当前线程，为后续的分布式事务处理提供上下文。

*   **场景二：演示 `RootContext` 工具类**
    *   **描述**: 讲师切换到 Maven 项目中的 `RootContext.java` 文件，展示了其源码。他解释了 `RootContext` 类如何通过 `ThreadLocal` 来存储 `TX_ID`，并演示了 `bind` 和 `getTxId` 方法的使用。
    *   **技术点**: `ThreadLocal` 是实现线程局部变量的关键，确保在同一个线程内，`TX_ID` 的值是唯一的，从而支持分布式事务的上下文传递。

*   **场景三：演示 `ContextCoreLoader` 单例模式**
    *   **描述**: 讲师进一步展示了 `ContextCoreLoader.java` 文件，重点讲解了 `ContextCoreHolder` 内部类的实现。他解释了 `ContextCore` 如何通过 `EnhancedServiceLoader` 加载，并通过 `ThreadLocal` 初始化。
    *   **技术点**: 单例模式确保了 `RootContext` 的全局唯一性，避免了多个实例导致的上下文混乱。

*   **场景四：总结与回顾**
    *   **描述**: 讲师回到 Typora 的 PPT 页面，总结了本次修改的核心内容：通过 `RootContext.bind()` 方法，将 `TX_ID` 绑定到线程上下文，从而支持分布式事务的上下文传递。
    *   **技术点**: 本次修改是实现分布式事务一致性的重要一步，为后续的事务协调和回滚提供了基础。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解视频中的技术要点和实现过程。
