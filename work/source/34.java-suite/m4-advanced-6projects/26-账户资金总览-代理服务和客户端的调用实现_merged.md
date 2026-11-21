# 26-账户资金总览-代理服务和客户端的调用实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们去实现代理服务转发的调用处理

以及客户端模拟器调用接口的请求实现

首先咱们要在代理服务里面去创建资金的服务处理器

Stalk, Binance, Processor回到工程当中

找到代理服务工程

我们在Processor这个包下面去创建一个新的处理器

New,加class,加名称copy过来点击OK

整个调用逻辑实现起来比较简单

那咱们就从讲义当中copy对应的代码

回到工程当中粘贴

好,咱们来看一下它整体的调用处理逻辑

处理器要去基层抽象的附类以及对应的公用接口

添加service诸解

然后我们要去注入GRBC的client

资金服务的调用接口

接下来就是它的具体请求处理

首先去构造对应的请求参数

传递的参数信息也比较简单

主要就传递交易账户ID

然后通过GRBC远程接口去调用账户的资金总打信息

调用完成之后

我们去复制对应的数据信息

将它包装为Netty的响应数据传输结构

然后我们要去组装它的成功响应报文

最后就通过channel通道

输出给调用客户端

接着咱们就要去工厂方法里面增加对应的扩展

增加资金服务的处理器

ibase stock processor

这里我们就直接copy一下

确保处理器名称不要写入错误

否则的话不能正常输入

这个是资金服务的处理器

接下来我们就要去工厂方法里面增加对应的扩展

case get

finance overview

processor 只定下

stock finance processor

break 推出

最后要去工程配置里面增加资金服务的调用

这里配置了行情服务

挂单服务

还有常委服务

然后咱们再增加一个配置

这个就是资金服务

我们只需要修改资金服务的名称

finance

这里要和资金服务的名称保持一致

finance

其他地方不用修改

好

这一块呢

就是对代理服务转发调用的处理实现

接着我们要在客户端模拟器里面去实现对账户资金阻拦接口的调用

咱们将这段调用代码拷贝过去

回到工程当中

在模拟器business handle下面

追加对应的调用处理

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

这个呢就是get account的finance overview

获取账户资金总览信息

客户端调用比较简单

不需要传递任何的参数

他只要去标示我们是调用哪个接口

这个接口呢就是获取账户资金总览的接口

接口名称呢不能写错

然后呢

组装请求信息

接着的话呢

将信息发送给服务端

接下来我们要去修改交互菜单

应用到修menu方法

增加一个菜单项的输出

指定号为7

名称呢就是get finance

summary

它是获取

账户资金总览信息

然后咱们还去增加交互操作指令的处理

在这里我们copy一下

指定改为7

这个是获取

账户资金总览信息

接口名称要改成get account

finance summary

最后要增加响应的输出

修改于C5

protomessage方法

这里面我们要去增加一个判断

get finance overview

直接打印对应的数据

这个呢并不是一个集合

我们就将数据直接打印出来就可以

get finance overview response

好

那在这里呢

咱们就完成了模拟客户端的

对付计划了一遍了

交用实现

下一讲咱们再去实现对账户资金总览功能的测试和验证

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `bulls-stock-proxy` 的 Java 项目，主要讲解如何实现一个**代理服务（Proxy Service）**，用于在客户端与后端多个微服务（如行情服务、持仓服务、资金服务）之间进行**请求转发与处理**。课程内容覆盖了从服务处理器的实现、GRPC客户端调用、到客户端调用逻辑的完整链路。核心目标是构建一个可复用的代理层，能够根据不同的请求类型，动态地将请求路由到相应的业务处理器，并处理返回结果。视频通过IDE（IntelliJ IDEA）和Markdown文档（Typora）展示代码和架构设计，强调了服务解耦、配置管理（如 `bootstrap-dev.yml`）和异常处理的重要性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: **课程引入与目标说明**。讲师在Typora文档中介绍了本章目标，即实现一个代理服务，用于处理客户端的请求并转发给后端服务。
*   **00:16 - 00:45**: **代理服务转发调用处理 (3.6节)**。讲师在IDE中展示 `StockFinanceProcessor` 类的代码，该类继承自 `AbstractStockProcessor` 并实现了 `IBaseStockProcessor` 接口，用于处理资金相关的请求。代码中使用了 `@GrpcClient` 注解来注入GRPC客户端 `stockFinanceServiceStub`。
*   **00:46 - 01:15**: **更新昨收价逻辑**。讲师在 `StockFinanceProcessor` 类中展示 `updateClosePrice` 方法，该方法用于从Redis缓存中读取并更新昨日收盘价。代码中包含了对日期的判断，以确保每天只更新一次，避免数据覆盖。
*   **01:16 - 01:45**: **处理客户端请求**。讲师展示 `StockFinanceProcessor` 中的 `processRequest` 方法。该方法首先构造请求对象，然后通过GRPC客户端调用 `getFinanceOverview` 方法，最后将返回结果封装成响应并返回。
*   **01:46 - 02:15**: **处理器工厂 (StockProcessorFactory)**。讲师展示 `StockProcessorFactory` 类，该类负责根据请求类型（如 `PLACE_ORDER`, `GET_ORDER`, `GET_FINANCE_OVERVIEW`）动态创建并返回相应的处理器实例（如 `StockDealProcessor`, `StockQuoteProcessor`）。
*   **02:16 - 02:45**: **服务配置文件 (bootstrap-dev.yml)**。讲师展示 `bootstrap-dev.yml` 配置文件，其中定义了多个GRPC服务的地址和配置，包括行情服务、持仓服务和资金服务，这些服务通过 `discovery://` 协议进行服务发现。
*   **02:46 - 03:15**: **客户端调用实现与验证 (3.7节)**。讲师在Typora文档中介绍 `BusinessHandler` 接口，该接口定义了获取账户资金总览信息的方法 `getAccountFinanceSummary`。
*   **03:16 - 03:45**: **客户端处理器 (ClientBoundHandler)**。讲师展示 `ClientBoundHandler` 类，该类实现了 `WebSocketClientHandler` 接口，用于处理客户端的WebSocket连接和消息。代码中包含了 `readInput` 方法用于读取用户输入，以及 `prevInvokeMethod` 方法用于根据请求类型调用相应的业务方法。
*   **03:46 - 04:15**: **客户端请求处理逻辑**。讲师展示 `ClientBoundHandler` 中的 `showMenu` 方法，该方法根据用户输入的请求类型，调用相应的业务方法并打印结果。例如，当用户输入 `GET_FINANCE_OVERVIEW` 时，会调用 `getFinanceOverviewResp` 方法并打印返回的数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **Typora 文档 (Day16.md)**: 包含了课程大纲，如“3.6 代理服务转发调用处理”和“3.7 客户端调用实现与验证”。
    *   **代码注释**: 在 `StockFinanceProcessor` 类中，有详细的注释说明了类的功能和方法的作用。
*   **代码关键内容**:
    *   **`StockFinanceProcessor.java`**:
        *   `@Service` 和 `@Log4j2` 注解。
        *   `@GrpcClient("grpc-finance-server")` 注解用于注入GRPC客户端。
        *   `updateClosePrice` 方法：用于更新昨日收盘价，包含日期判断逻辑。
        *   `processRequest` 方法：处理客户端请求，调用GRPC服务并返回结果。
    *   **`StockProcessorFactory.java`**:
        *   `switch (requestType)` 语句：根据请求类型动态创建处理器。
        *   `generateStockProcessor` 方法：根据请求类型返回相应的处理器实例。
    *   **`bootstrap-dev.yml`**:
        *   `grpc-quote-server`、`grpc-pending-server`、`grpc-position-server` 配置：定义了不同服务的地址和配置。
    *   **`BusinessHandler.java`**:
        *   `getAccountFinanceSummary` 方法：定义了获取账户资金总览信息的接口。
    *   **`ClientBoundHandler.java`**:
        *   `readInput` 方法：用于读取用户输入。
        *   `prevInvokeMethod` 方法：用于根据请求类型调用相应的业务方法。
        *   `showMenu` 方法：根据用户输入调用相应的业务方法并打印结果。
*   **公式 / 图表**:
    *   无公式或图表。

---

### 4) 关键场景与演示描述

*   **场景一：代理服务处理器实现**。
    *   **描述**: 讲师在IDE中打开 `StockFinanceProcessor.java` 文件，演示了如何通过继承 `AbstractStockProcessor` 并实现 `IBaseStockProcessor` 接口来创建一个业务处理器。重点展示了 `@GrpcClient` 注解的使用，以及 `updateClosePrice` 方法中如何从Redis缓存中读取并更新昨日收盘价。
*   **场景二：客户端请求处理流程**。
    *   **描述**: 讲师在IDE中打开 `StockFinanceProcessor.java` 文件，演示了 `processRequest` 方法的执行流程。该方法首先构造请求对象，然后通过GRPC客户端调用 `getFinanceOverview` 方法，最后将返回结果封装成响应并返回。
*   **场景三：处理器工厂动态创建处理器**。
    *   **描述**: 讲师在IDE中打开 `StockProcessorFactory.java` 文件，演示了 `generateStockProcessor` 方法的执行流程。该方法根据请求类型（如 `PLACE_ORDER`, `GET_ORDER`, `GET_FINANCE_OVERVIEW`）动态创建并返回相应的处理器实例。
*   **场景四：客户端调用实现与验证**。
    *   **描述**: 讲师在IDE中打开 `ClientBoundHandler.java` 文件，演示了 `showMenu` 方法的执行流程。该方法根据用户输入的请求类型，调用相应的业务方法并打印结果。例如，当用户输入 `GET_FINANCE_OVERVIEW` 时，会调用 `getFinanceOverviewResp` 方法并打印返回的数据。
