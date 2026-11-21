# 30-XXL_JOB集成运用-代理服务交割单接口转 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们要去实现代理服务增加账户交割单的接口功能转发

这里呢就要和之前交易服务处理器的改造一样

要做相应的封装和调整

因为呢它要支持多个接口的转发处理

可以看到这里面有获取账户资金总览

获取账户交割单两个不同的接口

下面呢是针对于这两个接口做的封装处理

那整体实现起来并不复杂

为了节省时间

咱们就将这个代码做一个copy

回到工程当中

进入到代理服务的stock finance processor

这个呢是资金服务的处理器

我们将整个代码呢做个覆盖

检查有没有出现错误

这里还需要在pb结构文件当中增加一个接口定义

咱们回到pb文件

再是扫个header下面

咱们要增加

获取

我们可以看到这个代码

在材料中

يد考键

紧记要去检查

这是在

explicar

以上

课题

第十一 justify

代理 own

ě

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个金融交易系统（`bulls-stock`）中“代理服务”模块的开发教学。核心内容是为代理服务增加“账户交割单”接口的转发功能。讲师通过在 IntelliJ IDEA 中演示，修改了 `StockFinanceProcessor` 类，使其能够根据客户端请求类型（如 `GET_ACCOUNT_SETTLEMENTS`）调用相应的业务方法（如 `getAccountSettlements`），并处理返回结果。同时，视频也展示了如何通过 `StockProcessorFactory` 工厂类来管理并注册新的处理器，以支持动态扩展。整个过程涉及 Java、gRPC、Protocol Buffers 等技术栈。

---

### 2) 按时间顺序的章节（带时间点）

由于无法提供精确的时间戳，以下章节按画面内容和逻辑顺序排列：

*   **00:00 - 00:05**: **课程引入与目标说明**。讲师在 Typora 文档中定位到章节 `3.10 代理服务增加账户交割单接口转发`，并说明本节目标是修改处理器以支持新接口。
*   **00:05 - 00:15**: **修改处理器 `StockFinanceProcessor`**。讲师在 IntelliJ IDEA 中打开 `StockFinanceProcessor.java` 文件，展示其继承自 `AbstractStockProcessor` 并实现了 `IBaseStockProcessor` 接口。重点讲解了 `processRequest` 方法中的 `switch` 语句，用于根据请求类型分发处理。
*   **00:15 - 00:25**: **实现 `getAccountSettlements` 方法**。讲师将光标移动到 `case GET_ACCOUNT_SETTLEMENTS:` 分支，展示如何调用 `getAccountSettlements` 方法。随后，他切换到该方法的实现，展示如何构建 gRPC 请求、调用远程服务并处理响应。
*   **00:25 - 00:35**: **构建 gRPC 请求与处理响应**。在 `getAccountSettlements` 方法中，讲师演示了如何使用 `GetAccountSettlementRequest.newBuilder()` 构建请求对象，并设置账户ID、时间范围等参数。接着，他展示了如何遍历服务返回的 `SettlementSingle` 列表，将其转换为响应对象 `GetAccountSettlementRespData`，并最终构建返回给客户端的 `ResponseMessage`。
*   **00:35 - 00:45**: **工厂模式与接口注册**。讲师切换到 `StockProcessorFactory` 类，说明其作用是管理所有处理器。他展示了如何通过工厂类将 `StockFinanceProcessor` 注册到系统中，以便代理服务能够动态发现并调用它。
*   **00:45 - 00:55**: **Protocol Buffers 定义回顾**。讲师切换到 `StockHead.proto` 文件，回顾了 `StockHead` 消息结构中定义的 `RequestType` 枚举，确认 `GET_ACCOUNT_SETTLEMENTS` 是一个合法的请求类型，为后续的 `switch` 语句提供依据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `3.10 代理服务增加账户交割单接口转发`。
    *   **处理器调整**: `修改 com.ictast.trade.stock.quote.proxy.processor.StockFinanceProcessor`。
    *   **工厂管理**: `2. 工厂管理员增加新接口支持`。

*   **关键代码片段**:

    *   **`StockFinanceProcessor` 类定义**:
        ```java
        @Service
        @Log4j2
        public class StockFinanceProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
            @GrpcClient("grpc-finance-server")
            private StockFinanceServiceGrpc.StockFinanceServiceBlockingStub stockFinanceServiceStub;
        }
        ```

    *   **`processRequest` 方法**:
        ```java
        @Override
        public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
            switch (stockMessage.getStockHead().getRequestType()) {
                case GET_FINANCE_OVERVIEW:
                    getFinanceOverview(channelHandlerContext, stockMessage);
                    break;
                case GET_ACCOUNT_SETTLEMENTS:
                    getAccountSettlements(channelHandlerContext, stockMessage);
                    break;
                default:
                    log.error("Process in StockDealProcessor.processRequest method => Not Match RequestType!");
            }
        }
        ```

    *   **`getAccountSettlements` 方法**:
        ```java
        private void getAccountSettlements(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
            ResponseMessage responseMessage = null;
            StockHeadProto.StockHead stockHead = null;
            try {
                GetAccountSettlementData accountSettlementData = stockMessage.getAccountSettlementData();
                // 构造请求信息
                GetAccountSettlementRequest request = GetAccountSettlementRequest.newBuilder()
                    .setAccountId(getUserAccountId(channelHandlerContext))
                    .setTimeStart(accountSettlementData.getTimeStart())
                    .setTimeEnd(accountSettlementData.getTimeEnd())
                    .build();
                // 调用 gRPC 服务
                final GetAccountSettlementResponse response = stockFinanceServiceStub.getAccountSettlements(request);
                // 复制数据
                List<GetAccountSettlementRespData> settlementRespDataList = new ArrayList<>();
                response.getGetAccountSettlementSingleList().forEach(settlement -> {
                    GetAccountSettlementRespData settlementRespData = GetAccountSettlementRespData.newBuilder();
                    BeanAssistant.copyNotNullProps(settlement, settlementRespData);
                    settlementRespDataList.add(settlementRespData);
                });
                // 返回成功报文
                stockHead = generateStockHead(stockMessage.getStockHead(), response.getStatus());
                responseMessage = ResponseMessage.newBuilder()
                    .setStockHead(stockHead)
                    .setMessage(response.getMessage())
                    .setGetAccountSettlementRespDataList(settlementRespDataList)
                    .build();
                channelHandlerContext.writeAndFlush(responseMessage);
                log.info("Process in StockFinanceProcessor.getAccountSettlements write: " + responseMessage);
            } catch (Exception e) {
                log.error("Process in StockFinanceProcessor.getAccountSettlements error: " + e.getMessage(), e);
                responseMessage = ResponseMessage.newBuilder()
                    .setStockHead(stockMessage.getStockHead())
                    .setMessage("Internal Server Error")
                    .setGetAccountSettlementRespDataList(Collections.emptyList())
                    .build();
                channelHandlerContext.writeAndFlush(responseMessage);
            }
        }
        ```

    *   **Protocol Buffers 定义 (`StockHead.proto`)**:
        ```protobuf
        syntax = "proto3";

        option java_package = "com.ictast.bulls.stock.struct.netty.trade";
        option java_outer_classname = "StockHeadProto";

        message StockHead {
            ProtoVer protoVer = 1;
            RequestType requestType = 2;
            int64 seqId = 3;
            string status = 4;
        }

        enum ProtoVer {
            VER_1 = 0;
            VER_2 = 1;
        }

        enum RequestType {
            GET_FINANCE_OVERVIEW = 0;
            GET_ACCOUNT_SETTLEMENTS = 1;
            // ... 其他请求类型
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：处理器功能修改**。
    *   **描述**: 讲师在 Typora 中定位到课程大纲，然后在 IntelliJ IDEA 中打开 `StockFinanceProcessor.java` 文件。他首先展示了类的结构，然后重点讲解了 `processRequest` 方法中的 `switch` 语句。他通过光标移动，将观众的注意力引导至 `case GET_ACCOUNT_SETTLEMENTS:` 分支，说明这是新增的处理逻辑。

*   **场景二：实现具体业务方法**。
    *   **描述**: 讲师点击并跳转到 `getAccountSettlements` 方法的实现。他通过逐行代码演示，展示了如何从 `StockMessage` 中提取数据，使用 Protocol Buffers 的 `newBuilder()` 方法构建 gRPC 请求对象，调用 `stockFinanceServiceStub.getAccountSettlements(request)` 方法，然后将服务返回的 `SettlementSingle` 列表转换为响应对象，并最终构建 `ResponseMessage` 返回给客户端。他特别强调了 `BeanAssistant.copyNotNullProps` 方法用于数据复制。

*   **场景三：工厂模式与接口注册**。
    *   **描述**: 讲师切换到 `StockProcessorFactory` 类，说明其作为工厂类的作用。他通过代码演示，展示了如何将 `StockFinanceProcessor` 实例注册到工厂中，以便代理服务在运行时能够动态发现并调用它，从而实现接口的灵活扩展。

*   **场景四：Protocol Buffers 定义确认**。
    *   **描述**: 讲师切换到 `StockHead.proto` 文件，通过高亮显示 `RequestType` 枚举，确认 `GET_ACCOUNT_SETTLEMENTS` 是一个合法的请求类型。这为 `processRequest` 方法中的 `switch` 语句提供了类型安全的依据，确保了代码的正确性。
