# 13-仓位总览-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们去对客户端做个调用实现

以及对仓位总打功能做一个测试和验证

首先咱们在代理服务工程下面

去修改Business Handle的业务接口实现内

增加对持仓服务里面的仓位总打接口的调用

咱们将这段代码copy下

找到咱们的模拟器实现

修改Business Handle

在最下面增加获取持仓数据接口的调用

整个调用处理也比较简单

这里不需要传递任何参数

只需要告诉请求接口的类型

这个接口类型是要获取所有的持仓数据信息

不要传递错误

接下来咱们再去修改交互的菜单

以及操作指令

在下面咱们增加一行输出

修改它的名称

Get Positions

这个是查询用户持仓数据

咱们再添加对应的操作指令

这里copy下

指定号为6

这个是查询用户持仓数据

不需要传递输入的参数

这个可以去除

接口要调整下

改成Get All Positions

接下来咱们就启动相关的服务

做一个功能上的测试

我们来做一个测试验证

首先咱们要启动交易服务

右键让运行

接下来我们要启动仓位服务

交易服务已经启动完成

咱们要把仓位服务再次启动一下

右键让运行

接下来咱们还启动代理服务

右键让运行

好代理服务已经启动成功

接着咱们来启动模拟客户端

右键让运行

咱们先调用登录的指令

再查询查询服务

在查询服务的仓位信息之前

咱们先去数据库中的表

来看一下当前的数据

我们找到shadow position这张表

当前有两条数据

一条是股票ID1的持仓

一条是股票ID为4的持仓数据信息

接着咱们就通过接口调用

来验证一下

跟数据库当中的数据信息

是否能够匹配

咱们输入指定6

查询用户的持仓详情

这个时候可以看到

客户端就已经接收到

返回的持仓数据信息

总共只有两条数据

一个是股票ID为1的持仓

另外一个是股票ID为4的持仓信息

所以这里并没有显示

浮动盈亏的信息

但是咱们是做了

对应逻辑的实现

为什么没有显示出来呢

这个是因为巨星的行情报价

和咱们的持仓的

成本价格是一致的

他们的浮动盈亏

都是为0

对于为0的属性信息

PB数据结构

在这里并不会展示出来

所以咱们需要启动

行情服务

让行情价格产生变化

然后再去请求持仓信息

去查看盈亏的计算结果

去查看盈亏的计算结果

好那咱们去启动行情服务

这里我们会发送

模拟的行情信息

模拟行情信息咱们知道

它的实现会产生随机的价格变化

启动完行情服务

等待客户端接收

最新的行情数据

咱们再做一个持仓数据的接口发送验证

好在这里咱们接收到了

行情推出过来的实时数据

在这里我们可以看到

价格已经产生了变化

我们再次去发送

持仓数据的查询

输入指定为6

这里咱们可以看到

还是没有显示浮动盈亏的信息

这个原因是因为

咱们在行情服务里面

开启的是模拟行情的推送

它进入的是

模拟行情的发送处理逻辑

模拟行情它并不会去

更新最新的

缓存行情报价

我们查看NASPRESS CASH

在这里

它生成完随机价格之后

并不会去重新更新对应的缓存

下面并没有引用操作的地方

对不对

好在这里咱们就需要

采用真实的行情信息推送

这里我们改成R

这里我们改成R

然后再次启动行情服务

咱们的目的是要让

最新行情的缓存

让它的价格信息产生变化

让它的价格信息产生变化

这样咱们在模拟终端

才能够验证持仓的盈亏数据

才能够验证持仓的盈亏数据

好咱们来看一下

行情服务已经成功启动

并且抓取了最新的行情信息

咱们回到模拟客户端

它也接收到了最新的行情数据

那咱们去发送获取持仓数据的接口

那咱们去发送获取持仓数据的接口

指定为U

咱们先将行情服务停止

防止它继续推送

防止它继续推送

那咱们来看一下

在模拟客户端

咱们接收的数据

现在就可以看到盈亏的变化

这个是盈亏金额

这个是盈亏比例

上面股票ID为1的持仓数据

它的盈亏信息也发生了变化

它的盈亏信息也发生了变化

可以看到盈亏数据盈亏比例

好,在这里咱们就不对盈亏数据

做计算核对

大家有时间可以根据实时行情的价格

大家有时间可以根据实时行情的价格

以及咱们所提供的公式做一个核对验证

以及咱们所提供的公式做一个核对验证

好,在这里咱们就完成了对仓位总览的测试和验证

好,在这里咱们就完成了对仓位总览的测试和验证

好,在这里咱们就完成了对仓位总览的测试和验证

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统（`bulls-stock`）的客户端调用与服务端实现的演示。核心内容是展示如何通过一个名为 `stock-proxy` 的代理服务，将客户端的请求（如获取持仓、下单、撤单等）转发到后端的 `stock-position` 和 `stock-quote` 服务，并最终实现客户端与服务端的交互验证。演示中使用了 IntelliJ IDEA 开发环境，涉及 Spring Boot、gRPC、Netty 等技术栈，并通过控制台日志和打印语句来验证功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确判断视频中各画面的具体时间点，以下章节是根据画面内容和逻辑顺序进行的结构化划分：

*   **00:00 - 00:03**: **课程导航与章节定位**
    *   展示了课程的 Markdown 文档大纲，当前章节为“第3章 账户资金总览功能”，具体聚焦于“3.5 客户端调用实现与验证”。

*   **00:03 - 00:07**: **客户端调用接口实现**
    *   在 `BusinessHandler` 类中，演示了如何实现 `getAllPositions()` 方法。
    *   代码逻辑包括：打印日志、构造请求头、构建 `StockMessage` 消息体、并调用 `sendMsg` 方法发送请求。

*   **00:07 - 00:11**: **客户端命令处理逻辑**
    *   在 `ClientBoundHandler` 类中，演示了用户输入命令的处理逻辑。
    *   代码逻辑包括：根据用户输入的数字（如“2”代表登录，“3”代表下单）调用 `BusinessHandler` 对应的方法。

*   **00:11 - 00:14**: **服务端启动与配置**
    *   展示了 `StockPositionApplication` 和 `StockProxyApplication` 的主类。
    *   通过右键菜单选择“Run”来启动服务端应用，控制台输出显示服务已成功启动并绑定到端口（如 12345）。

*   **00:14 - 00:17**: **客户端连接与初始化**
    *   在 `SimulateClient` 类中，演示了如何使用 Netty 初始化客户端连接。
    *   代码逻辑包括：配置 `Bootstrap`、设置 TCP 选项（如 `SO_KEEPALIVE`）、初始化 `ChannelPipeline`。

*   **00:17 - 00:21**: **服务端业务逻辑与数据处理**
    *   在 `StockPositionServiceImpl` 类中，演示了获取持仓数据的逻辑。
    *   代码逻辑包括：调用 `getTradeStockQuoteLast` 获取行情数据，进行类型转换和格式化处理。

*   **00:21 - 00:25**: **服务端服务启动**
    *   展示了 `StockQuoteApplication` 的主类。
    *   通过右键菜单选择“Run”来启动服务端应用，控制台输出显示服务已成功启动。

*   **00:25 - 00:29**: **服务端模拟行情生成**
    *   在 `StockQuoteServiceImpl` 类中，演示了 `sendSimulationQuote` 方法。
    *   代码逻辑包括：生成模拟行情数据、更新行情、并发送到客户端。

*   **00:29 - 00:33**: **客户端接收与显示**
    *   展示了客户端接收到的持仓数据。
    *   控制台输出显示了 `getAllPositionData` 的返回结果，包含 `accountId`、`stockId`、`costPrice`、`volume`、`lastPrice` 等字段。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`第3章 账户资金总览功能`，包含子章节 `3.5 客户端调用实现与验证`。
    *   代码文件路径：`bulls-stock-proxy`、`bulls-stock-position`、`bulls-stock-quote`。

*   **关键代码片段**:

    **1. `BusinessHandler.java` - 获取持仓接口实现**
    ```java
    public void getAllPositions() {
        System.out.println("******* Send Get Positions *******");
        StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder().setSeqId(seqId++).build();
        StockMessage stockMessage = StockMessage.newBuilder().setStockHead(stockHead).build();
        sendMsg(stockMessage);
    }
    ```

    **2. `ClientBoundHandler.java` - 用户命令处理**
    ```java
    if("2".equals(command)) {
        businessHandler.userLogin();
    } else if("3".equals(command)) {
        businessHandler.placeOrder();
    } else if("4".equals(command)) {
        businessHandler.getKline();
    } else if("5".equals(command)) {
        businessHandler.getOrderId();
    } else if("6".equals(command)) {
        businessHandler.getIgnoreCase();
    } else {
        showMenu();
    }
    ```

    **3. `StockPositionApplication.java` - 服务端主类**
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    @ComponentScan(basePackages = "com.itcast")
    public class StockPositionApplication {
        public static void main(String[] args) {
            SpringApplication.run(StockPositionApplication.class, args);
        }
    }
    ```

    **4. `SimulateClient.java` - 客户端连接初始化**
    ```java
    Bootstrap bootstrap = new Bootstrap();
    bootstrap.group(group)
        .channel(NioSocketChannel.class)
        .option(ChannelOption.TCP_NODELAY, true)
        .option(ChannelOption.SO_KEEPALIVE, true)
        .handler(new LoggingHandler(LogLevel.INFO))
        .handler(new ChannelInitializer<SocketChannel>() {
            @Override
            public void initChannel(SocketChannel ch) throws Exception {
                ChannelPipeline pipeline = ch.pipeline();
            }
        });
    ```

    **5. `StockPositionServiceImpl.java` - 获取持仓数据**
    ```java
    TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(pos.getStockId());
    if(null != quoteLast) {
        // 采用长整型做计算，保留两位小数
        // ... (省略具体计算逻辑)
    }
    ```

    **6. `StockQuoteServiceImpl.java` - 发送模拟行情**
    ```java
    public void sendSimulationQuote(TradeStock tradeStock, int v) {
        // ... (省略具体实现)
    }
    ```

    **7. `StockQuoteServiceImpl.java` - 获取行情数据**
    ```java
    @Override
    public void fetchStockQuote(TradeStock stock, int closeDiffMins) {
        log.info("Process in StockQuoteServiceImpl.fetchStockQuote method.");
        if(1 == 2) {
            // ... (省略条件判断)
        } else {
            sendSimulationQuote(stock, closeDiffMins);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：客户端调用接口实现**
    *   **描述**：讲师在 `BusinessHandler` 类中编写并演示了 `getAllPositions()` 方法。该方法首先打印日志，然后构造一个 `StockMessage` 消息体，最后调用 `sendMsg` 方法将消息发送到服务端。这展示了客户端如何发起一个获取持仓的请求。

*   **场景二：客户端命令处理逻辑**
    *   **描述**：讲师在 `ClientBoundHandler` 类中展示了用户输入命令的处理逻辑。通过 `switch-case` 或 `if-else` 结构，根据用户输入的数字（如“2”、“3”、“4”）调用 `BusinessHandler` 中对应的方法，如 `userLogin`、`placeOrder`、`getKline` 等。这演示了客户端如何根据用户指令执行不同的操作。

*   **场景三：服务端启动与连接**
    *   **描述**：讲师在 IntelliJ IDEA 中右键点击 `StockPositionApplication` 和 `StockProxyApplication` 的主类，选择“Run”来启动服务端。控制台输出显示服务已成功启动并绑定到指定端口（如 12345），这验证了服务端的正常运行。

*   **场景四：客户端连接与初始化**
    *   **描述**：讲师在 `SimulateClient` 类中演示了如何使用 Netty 初始化客户端连接。通过配置 `Bootstrap`、设置 TCP 选项和初始化 `ChannelPipeline`，客户端成功连接到服务端。这展示了客户端如何建立与服务端的通信通道。

*   **场景五：服务端业务逻辑与数据处理**
    *   **描述**：讲师在 `StockPositionServiceImpl` 类中演示了如何获取持仓数据。通过调用 `getTradeStockQuoteLast` 方法获取行情数据，并进行类型转换和格式化处理。这展示了服务端如何处理客户端的请求并返回数据。

*   **场景六：客户端接收
