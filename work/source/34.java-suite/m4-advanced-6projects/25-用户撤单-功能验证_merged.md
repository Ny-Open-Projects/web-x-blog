# 25-用户撤单-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始对用户测单的整体功能做个测试和验证

在测试验证之前要做好相应的准备

启动好交易服务挂单服务以及代理服务

在下面的不同测试场景当中可能还需要用到航行服务

在做测试之前咱们要去封装测单的调用方法

这里是测单调用接口的实现

那咱们将它copy一下

回到咱们工程当中

找到模拟器

在business handle下面

咱们去增加一个接口

将刚才的代码copy进来

这个就是测单接口

咱们可以看到测单接口定义了一个参数

这个参数是订单ID

加入这个参数是可以让咱们在终端的时候

去输入不同的订单号来做对应的测试和验证

拿到订单号之后

接着就要去

去构造请求信息

请求信息我们可以看到

它会去传递订单ID

然后呢还会去传入股票产品ID

这里咱们就默认将股票产品ID置为1

如果要对其他股票产品的订单做测单处理

记得要在这里做相应的调整修改

接下来咱们要去增加对应的菜单交付指令

在client.wonderhead里面

我们去修改show menu这个方法

这里咱们增加一个输出

序号指定为4

名称做个调整

叫recall order

这个呢就是用户测单

然后咱们要去增加对应的指定处理

这里呢我们也先做copy

指定号是为4

这个是用户测单的结果

这样方法名称就可以修改

recall order

我们还传递订单ID

我们还传递订单ID

对不对

在这里我们就要去定义一个参数

接收输入的订单ID

radio input

这个参数要改成order

radio input是读取用户的输入指定

在这里会将接收的信息作为支付串返回

那么用户输入指定为4的结果之后

下面他在输入订单信息

在这里呢就可以接收

然后呢咱们就去调用测单的结果做对应的处理

模拟器的接口处理完成之后

接着咱们就来启动服务做对应的验证

首先咱们去启动交易服务

右键run运行

接下来咱们去启动挂单服

然后启动代理服务

代理服务启动完成之后

接着咱们去启动模拟客户端

Semillette Planner

右键run运行

首先咱们进行用户的登录

首先咱们进行用户的登录

然后下一个订单

好可以看到

订单ID是2533

2533这条订单ID咱们要记录下

接下来呢咱们就去发出

测单的请求

测单的指定是4

接下来

咱们要去输入

要撤回的

订单ID

2533

确认回车

好可以看到

二题是咱们呢

测单处理成功对不对

这个时候我们可以去验证数据库

看一下这个订单的状态

是不是已经改成了手工测单

我们在数据库里面

去查询最新的订单信息

按qr

可以看到最新的订单记录R533

和控制台里面的订单ID是一致的

那我们看一下他的订单状态呢

已经改成了3对不对

3就是代表手工测单

咱们可以查看一下这个状态的说明

在CHAT ORDER表里面

我们看一下STATES的描述

STATES 0是代成交

1是部分成交

3是手工测单

好

那在这里呢就验证了

测单功能的处理是能够正常运行的

刚才测试是针对于

代成交的订单做了撤回处理

咱们还有一种订单状态是可以进行撤回的

那就是部分成交

那接下来咱们就对部分成交的情况做一个测试

部分成交就需要通过行情

去进行

撤回处理

那咱们要将行情服务启动下

行情推送频率是30秒一次

我们看一下这个下单的参数信息是怎样的

查看PLACE ORDER方法

在这里呢

它的下单请求信息

成交数量是26000

是之前咱们做限价委托挂单测试的验证条件

26000是可以触发多次成交

在这里咱们再通过模拟扣除的方式去做测试

现在通过模拟客户端去做一个下单

输入指定号为2

下单成功

订单ID是2534

这个时候咱们去数据库里面查看一下

2534

只要记录的话呢

已经生成了

我们注意观察它的成交数量

目前还是为0对不对

订单状态是待成交

我们再次刷新一下

好现在已经变成了部分成交

这个时候咱们要先将行情服给停止掉

这是它接下来的行情推送

造成了订单完全成交

那咱们再次刷新一下这个订单信息

确保它的订单状态是属于1

也就是部分成交

接下来咱们再通过模拟终端去测回2534的这个订单

在模拟器下面

输入指定号为4

回车

咱们再输入刚才的订单ID

2534

再次确认回车

可以看到

返回结果是处理成功

那咱们再去数据库当中做个验证

重新查询订单信息

咱们可以看到

2534这个订单的状态就已经改为3

也就是手工测单的状态

那这个也就验证了针对于部分成交的订单

咱们测单功能也是能够正常处理了

那回到讲义当中

这一讲呢

咱们就对用户测单功能

做了一个全面的验证

模拟了两种主要的场景

一种是待成交的订单

另外一种呢

就是多次撮合的挂单

挂单是属于部分成交的情况

那咱们也做了一个测试

这个也是能够正常测回

大家如果是有时间

可以再做全面的验证

比如说这个订单已经完全成交

再次去测回

看下它的处理结果会是怎样

还可以针对已经测回的订单

再次发送测单请求

看下它的返回结果

通过全面的测试验证

可以帮助大家加深对业务功能的理解

大家要多去操作实践

发现实践过程当中的一些缺陷

去完善整个功能流程的处理

好

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个股票交易系统中“用户撤单功能”的实现与功能验证。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Spring Boot 项目中，通过代理服务（`ClientBoundHandler`）向业务处理服务（`BusinessHandler`）发送撤单请求，并最终在数据库中验证订单状态的变更。整个过程涉及网络通信、协议封装、业务逻辑处理和数据库操作，旨在验证系统功能的完整性和正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，当前章节为“3.4 功能验证”，并列出“准备”和“封装撤单调用方法”两个子项。
*   **00:06 - 00:15**: 讲师切换到 IntelliJ IDEA，展示 `ClientBoundHandler` 类的代码，其中包含 `recallorder` 方法，用于处理撤单请求。
*   **00:16 - 00:25**: 讲师展示 `BusinessHandler` 类中的 `recallOrder` 方法，该方法负责构造并发送撤单请求消息。
*   **00:26 - 00:35**: 讲师在 `ClientBoundHandler` 中展示 `run` 方法的逻辑，其中包含一个 `while` 循环，用于处理用户输入的指令，包括“0. 用户登录”、“1. 下单”、“2. 获取K线数据”和“M. 退出”。
*   **00:36 - 00:45**: 讲师演示了在 `ClientBoundHandler` 中，当用户输入“M”时，会调用 `businessHandler.recallOrder(orderId)` 方法来执行撤单操作。
*   **00:46 - 00:55**: 讲师切换到 `StockDealApplication` 的启动类，展示其 `main` 方法，并启动了 `StockDealApplication`。
*   **00:56 - 01:05**: 讲师在 `SimulateClient` 类中设置服务器 IP 地址为 `127.0.0.1`，并启动客户端程序。
*   **01:06 - 01:15**: 讲师在 Navicat 数据库管理工具中，展示 `trade_order` 表的结构和数据，用于后续验证。
*   **01:16 - 01:25**: 讲师在 `BusinessHandler` 中展示 `recallOrder` 方法的实现，其中构造了 `StockMessage` 消息体。
*   **01:26 - 01:35**: 讲师在 `ClientBoundHandler` 中展示 `recallOrder` 方法的调用逻辑，并在控制台中模拟用户输入“M”来触发撤单。
*   **01:36 - 01:45**: 讲师在控制台中输入撤单指令，系统成功发送请求并返回确认信息。
*   **01:46 - 01:55**: 讲师在 Navicat 中查询 `trade_order` 表，显示订单状态已从 `1` 更新为 `3`，验证了撤单功能成功执行。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.4 功能验证”。
    *   **子项**: “1. 模拟一次性成交的挂单请求”、“2. 模拟多次撮合的挂单请求”。
    *   **总结**: “订单数据已经更新”、“状态改变为3，验证处理成功”。

*   **关键代码**:
    *   **`ClientBoundHandler.java`**:
        ```java
        public void recallorder(String orderIdStr) {
            Long orderId = Long.valueOf(orderIdStr);
            System.out.println("******* Send Recall Order, Parameters *******");
            System.out.println("= " + orderId);
            // 构造头部信息
            StockHeadProto.StockHead stockHead = StockHeadProto.StockHead.newBuilder()
                .setSeqId(seqId)
                .setRequestType(StockHeadProto.RequestType.RECALL_ORDER).build();
            // 构造请求体
            StockMessage stockMessage = StockMessage.newBuilder()
                .setStockHead(stockHead)
                .setStockCode(stockCode)
                .setTimeStart(timeStart)
                .setTimeEnd(timeEnd)
                .setOrderId(orderId)
                .setDirection(direction)
                .setVolume(volume)
                .setPrice(price)
                .setOrderType(orderType)
                .setAccount(account)
                .setStockId(stockId)
                .build();
            // 发送消息
            sendMsg(stockMessage);
        }
        ```
    *   **`BusinessHandler.java`**:
        ```java
        public void recallOrder(Long orderId) {
            // 构造撤单请求消息
            StockMessage stockMessage = StockMessage.newBuilder()
                .setStockHead(stockHead)
                .setStockCode(stockCode)
                .setTimeStart(timeStart)
                .setTimeEnd(timeEnd)
                .setOrderId(orderId)
                .setDirection(direction)
                .setVolume(volume)
                .setPrice(price)
                .setOrderType(orderType)
                .setAccount(account)
                .setStockId(stockId)
                .build();
            // 发送消息
            sendMsg(stockMessage);
        }
        ```
    *   **`SimulateClient.java`**:
        ```java
        public class SimulateClient {
            private static final String serverIp = "127.0.0.1";
            // ... 其他代码 ...
        }
        ```

*   **关键图表**:
    *   **数据库表结构**: `trade_order` 表，包含 `id`, `stockid`, `direction`, `intvolume`, `execute`, `executetime`, `requestprice` 等字段。
    *   **数据查询结果**: 展示了订单状态从 `1` 更新为 `3` 的记录。

---

### 4) 关键场景与演示描述

*   **场景一：功能验证准备** (00:00-00:05)
    *   讲师在 Typora 中展示课程大纲，明确当前章节为“3.4 功能验证”，并强调需要完成“准备”和“封装撤单调用方法”两个步骤。

*   **场景二：撤单请求封装** (00:06-00:15)
    *   讲师在 IntelliJ IDEA 中打开 `ClientBoundHandler.java` 文件，展示 `recallorder` 方法的实现。该方法接收字符串形式的订单ID，将其转换为 `Long` 类型，并构造一个包含请求头和请求体的 `StockMessage` 消息，最后调用 `sendMsg` 方法发送。

*   **场景三：业务处理逻辑** (00:16-00:25)
    *   讲师切换到 `BusinessHandler.java` 文件，展示 `recallOrder` 方法。该方法接收 `Long` 类型的订单ID，构造一个 `StockMessage` 消息，并调用 `sendMsg` 方法发送。这表明业务处理服务负责接收并处理来自代理服务的撤单请求。

*   **场景四：客户端交互逻辑** (00:26-00:35)
    *   讲师在 `ClientBoundHandler.java` 中展示 `run` 方法的 `while` 循环。该循环根据用户输入的指令，调用 `businessHandler` 对象的相应方法，如 `userLogin()`, `placeOrder()`, `getKline()`, `recallOrder()` 等，实现用户与系统的交互。

*   **场景五：功能执行与验证** (01:36-01:45)
    *   讲师在控制台中输入撤单指令，系统成功发送请求并返回确认信息。
    *   讲师在 Navicat 中查询 `trade_order` 表，发现订单状态已从 `1` 更新为 `3`，成功验证了撤单功能的正确性。

*   **场景六：总结** (01:46-01:55)
    *   讲师在 Typora 中展示总结页面，明确指出“订单数据已经更新”和“状态改变为3，验证处理成功”，标志着本次功能验证圆满完成。
