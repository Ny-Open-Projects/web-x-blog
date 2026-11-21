# 19-预警通知推送-接口数据结构定义 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,这一讲咱们开始去实现接口数据结构的定义

首先咱们来定义内部的GRBC接口传输数据结构

将定义脚本做一个copy

回到工程当中

在PB公用工程下面

Resource, Total

在GRBC下面增加一个新的脚本定义文件

New File

名称就叫stock

Proxy

Service.Proto

这个是用于代理服务的接口数据结构定义

咱们将脚本内容粘连进去

我们来看一下整体的数据结构

在上面是定义了一个发送预警通知消息的RPC接口

由代理服务提供

下面是预警通知的请求消息体

这个请求消息体是一个数据集合

因为调度服务会将预警通知记录批量传送给代理服务

所以在这里定义的请求结构是要支持集合的处理

下面是预警通知的具体消息

包括用户信息、账户信息、预警类型以及通知内容

然后是返回的数据结构

这里包括状态、响应消息以及ID集合

这个ID就是代表预警通知记录处理成功返回对应的ID集合

比如说有10条通知记录

那么有7条发送成功

在这里就需要记录7条通知记录

接下来要去定义Neti的对外传输数据结构

Proxy代理服务它是接收预警通知消息

我们需要定义响应的数据包

将响应数据包发送给客户端

不需要定义请求的数据包

因为这个是Proxy代理服务主动推送给客户端的

而咱们将数据结构做一个copy

将预警通知消息复制

回到工程当中

在Neti目录下面

StalkMessage里面

咱们增加对应的结构

这里是预警通知消息的返回体

它是一个数据集合

我们来看一下它具体的数据结构

这里包括用户ID、账户ID、预警类型以及通知内容

和GRBC里面定义的数据结构基本上是一致的

接下来我们去修改响应数据包

ResponseMessage

在这里咱们增加刚才定义的数据结构

这个是账户预警通知信息的返回数据包

WarnMessage

给它一个序号11

定义完成之后要在StockHead里面

增加一个专门用于推送预警通知信息的业务类型

类型名称为NotifyWarnMessage

接下来咱们继续生成相应的交易代码

在Proto下面

Open Intomino

执行RotoGRBC脚本

接下来再执行NetEase的脚本

好执行完成

那这一讲就是对预警通知推送

接口数据结构的定义

这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于“预警告知推送实现”的技术课程，主要讲解了如何在基于 gRPC 和 Netty 的分布式系统中，定义和实现一套完整的预警通知数据结构。课程内容聚焦于服务端（Java）与客户端（gRPC）之间的通信协议设计，包括：

*   **gRPC 接口定义**：使用 `.proto` 文件定义服务接口 `StockProxyService` 及其请求/响应消息体 `WarnMessageDataRequest` 和 `WarnMessageDataResp`。
*   **Netty 传输协议**：定义了 `StockMessage.proto` 文件，用于在 Netty 服务端与客户端之间传输多种类型的消息（如登录、下单、行情、预警等），并使用 `StockHead.proto` 定义消息头和请求类型枚举。
*   **数据结构设计**：详细定义了预警通知的请求参数（如 `stockId`, `warnType`, `stopRate`）和响应结构。
*   **代码实现**：展示了在 Java 服务端（`AccountWarnSettingServiceImp`）中如何根据配置缓存和数据库查询，生成并保存预警通知记录。

整个过程体现了从协议设计到代码实现的完整开发流程，强调了数据结构在分布式系统中的核心作用。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **00:00 - 00:15**：课程引入，展示课程大纲，定位到“第3章 预警告知推送实现”下的“3.1 定义接口数据结构”。
*   **00:15 - 00:30**：讲解 gRPC 服务接口定义，展示 `StockProxyService.proto` 文件，定义了 `notifyWarnMessage` 方法。
*   **00:30 - 00:45**：讲解 gRPC 请求和响应消息体结构，展示 `WarnMessageDataRequest` 和 `WarnMessageDataResp` 的定义。
*   **00:45 - 01:00**：讲解 Netty 传输协议，展示 `StockMessage.proto` 文件，定义了 `StockHead` 和 `StockData` 消息体。
*   **01:00 - 01:15**：讲解 `StockHead.proto` 文件，定义了 `RequestType` 枚举，用于区分不同类型的请求。
*   **01:15 - 01:30**：展示 Java 服务端代码 `AccountWarnSettingServiceImp`，讲解如何根据缓存和数据库查询生成预警通知。
*   **01:30 - 01:45**：展示 `StockMessage.proto` 文件中 `RequestType` 枚举的完整定义，包括 `NOTIFY_WARN_MESSAGE`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：清晰列出了“第3章 预警告知推送实现”的子章节，包括“3.1 定义接口数据结构”、“3.2 调度服务实现APP在线预警通知推送功能”、“3.3 代理服务实现APP预警通知分发功能”。
*   **gRPC 接口定义**：
    ```protobuf
    syntax = "proto3";
    option java_multiple_files = true;
    option java_package = "com.itcast.trade.stock.struct.grpc.trade";
    option java_outer_classname = "StockProxyServiceProto";

    // 代理服务接口
    service StockProxyService {
        rpc notifyWarnMessage (WarnMessageDataRequest) returns (WarnMessageResponse) {}
    }
    ```
*   **gRPC 请求/响应消息体**：
    ```protobuf
    // 预警通知消息请求体
    message WarnMessageDataRequest {
        repeated WarnMessageData warnMessageDataList = 1;
    }

    // 预警通知消息体
    message WarnMessageData {
        int64 id = 1;
    }
    ```
*   **Netty 传输协议**：
    ```protobuf
    // 请求消息
    message StockMessage {
        // 头部消息
        StockHead stockHead = 1;

        // 消息体
        oneof StockData {
            LoginData loginData = 2;
            PlaceOrderData placeOrderData = 3;
            KlineData klineData = 4;
        }
    }
    ```
*   **StockHead.proto 枚举**：
    ```protobuf
    // 请求类型
    enum RequestType {
        // 用户登陆
        USER_LOGIN = 0;
        // 用户下单
        PLACE_ORDER = 1;
        // 实时行情数据
        QUOTE_REALTIME = 2;
        // 获取行情K线数据
        QUOTE_KLINE = 3;
        // 获取订单详情
        RECALL_ORDER = 4;
        // 获取用户持仓数据
        GET_ORDER = 5;
        // 获取用户持仓列表
        GET_ALL_POSITIONS = 6;
        // 获取资金总览
        GET_FINANCE_OVERVIEW = 7;
        // 获取账户结算信息
        GET_ACCOUNT_SETTLEMENTS = 8;
        // 账户预警通知设置接口
        ACCOUNT_WARN_SETTING = 9;
        // 推送预警通知信息
        NOTIFY_WARN_MESSAGE = 10;
    }
    ```
*   **Java 服务端代码片段**：
    ```java
    // 1. 通过所有的有效股票产品
    stocks.getKeys().forEachEach(stockId -> {
        TradeStockQuoteLast quoteLast = TradeStockQuoteLast.get(stockId);
        if (null != quoteLast) {
            // 2. 根据股票产品ID, 获取对应的KEY
            Set<String> keys = redisTemplate.keys(pattern: GlobalConstants.ACCOUNT_WARN_SETTING_STOCK_KEY + stockId);
            if (null != keys && !keys.isEmpty()) {
                String prefixKey = GlobalConstants.ACCOUNT_WARN_SETTING_STOCK_KEY + stockId;
                Cache cache = cacheManager.getCache(prefixKey);
                keys.forEach(key -> {
                    // 4. 根据股票产品ID, 获取用户的预警设置信息
                    Cache.ValueWrapper valueWrapper = cache.get(key);
                    if (null != valueWrapper && null != valueWrapper.get()) {
                        AccountWarnSettingBo accountWarnSettingBo = (AccountWarnSettingBo) valueWrapper.get();
                        if (checkAccountWarnSetting(accountWarnSettingBo)) {
                            // 6. 生成预警通知记录
                            saveAccountWarnNotifyMessage(accountWarnSettingBo, quoteLast);
                        }
                    }
                });
            }
        }
    });
    ```

---

### 4) 关键场景与演示描述

*   **场景一：gRPC 接口定义** (画面 1, 4, 5)
    *   **描述**：讲师在 Typora 文档中展示 `StockProxyService.proto` 文件，重点讲解了 `notifyWarnMessage` 方法的定义，以及如何通过 `option` 指令指定 Java 包名和类名。演示了如何在 `.proto` 文件中定义服务接口和消息体。
*   **场景二：Netty 传输协议设计** (画面 6, 7, 8, 9, 10)
    *   **描述**：讲师切换到 `StockMessage.proto` 文件，演示了如何定义一个包含头部 `StockHead` 和可选消息体 `StockData` 的 `StockMessage`。重点讲解了 `oneof` 关键字的使用，以及 `StockHead.proto` 中 `RequestType` 枚举的定义，用于区分不同类型的请求。
*   **场景三：Java 服务端实现** (画面 2, 3)
    *   **描述**：讲师在 IntelliJ IDEA 中打开 `AccountWarnSettingServiceImp.java` 文件，演示了如何在 Java 服务中实现预警通知的逻辑。代码逻辑包括：1) 遍历所有有效股票产品；2) 根据股票ID获取Redis缓存中的预警设置键；3) 从缓存中获取预警设置对象；4) 校验设置是否有效；5) 生成并保存预警通知记录。
*   **场景四：项目结构与文件管理** (画面 3, 11)
    *   **描述**：讲师在 IDEA 中展示了项目结构，重点指出了 `src/main/proto` 目录下存放的 `.proto` 文件，如 `StockProxyService.proto`、`StockMessage.proto` 等。演示了如何通过右键菜单将 `.proto` 文件添加到项目中，并展示了 `StockHead.proto` 文件中 `RequestType` 枚举的完整定义。
