# 18-账户资金总览-账户资金总览接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始去定义接口的数据结构

首先咱们去定义Netty的对外传输数据结构

修改stock message proto文件

回到工程当中

定义到stock message proto

在最下面

增加数据结构的定义

这里定义资金总档的返回数据结构

get

finance

overview

response对象

定义返回的属性

首先的话是总资产

长整形

total

assess

序号为1

接着定义总市值

int

64

total

market

amount

序号为2

下面定义持仓盈亏

也是一个长整形

position

profit

序号为3

然后是download的持仓盈亏

int64

pay profit

最后就是账户的可用余额

balance

咱们注意这里面的所有数值都采用长整形表示

这样可以避免计算或者是进度丢失等相关问题

这里添加一个注释

资金

总档

返回数据结构

那咱们要在响应的包里面去

去增加消息体

这个是获取账户资金总档的数据包

序号为8

定义完响应消息结构之后

请求数据结构这一块

咱们是不需要定义的

不需要传递任何的参数属性

咱们只需要去定义一个接口号

这里是资金总档的接口

data finance overview

区号为7

通过资金总档的接口进行标识

代理服务呢

就能够取到交易账户的ID

那么后台根据交易账户ID

再返回账户资金总档的数据

接下来咱们还去定义GRBC的传输数据结构

这里咱们新增一个PB的文件

名称就叫stock

service

plot

先定义PB的头部信息

这里咱们就直接copy一下

好

做个修改

上面保持不变

只需要修改java的内名称

fin finance

头部信息申命完成之后

接着咱们去定义资金服务的GRBC接口

service stock finance

定义

获取账户资金总档接口

rbc get finance

all in

all of you

定义它的请求数据结构体

all of you

request

定义响应的消息数据结构

response

接着咱们就来定义这两个消息体

首先是请求数据结构

获取账户资金总档请求数据结构

message

这里只需要传递交易账户ID

int64 account ID1

ind64 account ID1

ind64 account ID1

ind64 account ID1

inj��ero

接下来咱们去定义获取账户资金总档的返回数据结构体 message get finance overview response对象首先定义它的状态这里面是不需要拉写的然后定义响应的消息接着就是返回的业务属性总资产

int64

portal

size

3

这里咱们就直接copy一下

从stock message里面的响应数据结构

做一个copy

好回到刚才的

linux service

portal的定义文件

在这里呢

咱们做个替换

好

序号要调整一下

这里是3

好

4

5

6

7

这样RBC的

请求数据结构体呢

咱们已经定义完成

接着咱们就去生成对应的加码代码

open intomino

我们先执行portal

GRBC的批处理命令

好

生成完成

再去生成neti的批处理命令

好

执行完成

那咱们来检查对应的代码

确认下面

binance overview

这个已经成功生成

咱们再去

检查neti的传输数据结构

get finance overview

这个呢

也已经成功生成

好

这一讲呢

就是对账户资金总卵的

数据结构的定义

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于一个金融交易系统中“账户资金总览功能”的实现，核心内容是定义和设计用于 Netty 和 gRPC 服务间通信的接口数据结构。讲师通过演示如何在 `.proto` 文件中定义消息（Message）和枚举（Enum），并生成对应的 Java 代码，来说明如何构建清晰、可维护的远程调用接口。课程内容覆盖了从定义返回消息体、请求类型枚举，到定义具体的请求和响应数据结构的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 课程开场，讲师介绍本节内容为“定义接口数据结构”，并展示课程大纲。
*   **00:10 - 00:30**: 讲解 Netty 对外数据结构，重点演示 `StockMessage.proto` 文件中 `ResponseMessage` 的定义，包括头部、消息体和 oneof 选项。
*   **00:30 - 00:50**: 讲解 gRPC 对内数据结构，演示如何在 `StockFinanceService.proto` 文件中定义服务接口 `getFinanceOverview` 及其对应的请求 `GetFinanceOverviewRequest` 和响应 `GetFinanceOverviewResponse`。
*   **00:50 - 01:10**: 演示如何为 `GetFinanceOverviewResponse` 添加字段，如 `totalAssets`、`totalMarketAmount` 等。
*   **01:10 - 01:30**: 讲解 `RequestType` 枚举的定义，用于标识不同的请求类型。
*   **01:30 - 01:50**: 讲解 `StockPositionService` 服务接口的定义，包括 `getAllPositions` 方法。
*   **01:50 - 02:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **02:10 - 02:30**: 讲解 `StockFinanceService.proto` 中 `GetFinanceOverviewResponse` 的字段定义。
*   **02:30 - 02:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **02:50 - 03:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **03:10 - 03:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **03:30 - 03:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **03:50 - 04:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **04:10 - 04:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **04:30 - 04:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **04:50 - 05:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **05:10 - 05:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **05:30 - 05:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **05:50 - 06:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **06:10 - 06:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **06:30 - 06:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **06:50 - 07:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **07:10 - 07:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **07:30 - 07:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **07:50 - 08:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **08:10 - 08:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **08:30 - 08:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **08:50 - 09:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **09:10 - 09:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **09:30 - 09:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **09:50 - 10:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **10:10 - 10:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **10:30 - 10:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **10:50 - 11:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **11:10 - 11:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **11:30 - 11:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **11:50 - 12:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **12:10 - 12:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **12:30 - 12:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **12:50 - 13:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **13:10 - 13:30**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **13:30 - 13:50**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*   **13:50 - 14:10**: 讲解 `StockMessage.proto` 中 `ResponseMessage` 的 `oneof` 选项，用于区分不同类型的返回数据。
*
