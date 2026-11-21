# 06-资金额度调整-挂单服务增加额度调整处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢

在挂单服务里面去增加额度调整的实现

参与一下咱们已经实现了交易服务对额度调整的调用处理

那挂单服务呢

他需要做撮合交易处理

也需要调整账户的资金信息

所以咱们在挂单服务里面也需要增加额度调整接口的调用处理

那咱们就去做改造实现

去修改原来的业务实现类

回到工程代码当中

定位到业务实现类

那同样在挂单服务里面也要去修改生成成交记录的方法

Generate,Cut the deal

把调用逻辑放在最后面

这里咱们就不再重复去编写代码

从交易服务里面做一个copy

Generate,Cut the deal

回到Stock,Share,Pending,Service实现类当中

将这段代码copy

进来

然后要去增加GRBC接口配置

这个咱们也做一个copy

快速做实现

回到Pending,Service

将资金服务的GRBC接口输入进来

然后在学的第二方法里面

我们再检查一下

原有逻辑都不需要做调整

只需要在最后面的去增加资金服务额度调整功能接口的调用

最后咱们还去修改工程服务配置

增加GRBC资金服务的调用配置

在最下面

这里我们增加一个Current

然后下面是资金服务的配置信息

名称是GRBC,Binance

Service,Generance,Adjust

Discovery

三个斜杠

指向资金服务

Stock,Binance

Enable,Keep Alive,DRUE

然后是Keep Alive,Without cost,DRUE

最后是传输协议内容格式

为文本方式

这个不能配置错了

否则调用的时候会出现异常

好

那在这里咱们就实现了挂单服务增加资金服务额度调整接口的调用实现

那这一讲的内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“挂单服务”模块的开发讲解。核心内容是实现“挂单服务增加额度调整”的功能。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 `StockTradePendingServiceImpl` 类中，调用一个名为 `StockFinanceService` 的 gRPC 服务来调整用户的账户资金。整个过程包括：定义接口、实现业务逻辑、生成交易记录、调用金融服务更新账户余额，并在失败时抛出异常。视频重点在于展示如何在交易处理流程中集成资金调整的分布式服务调用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中定位到章节 `3.4 挂单服务增加额度调整实现`，并说明本节目标是实现挂单时的资金调整。
*   **00:00:05 - 00:00:15**: 讲师在 IDE 中打开 `StockTradePendingServiceImpl.java` 文件，展示其类结构和依赖的 DAO 接口。
*   **00:00:15 - 00:00:30**: 讲师将光标移动到 `generateTradeDeal` 方法，并开始讲解其内部逻辑，包括生成交易记录和调用金融服务。
*   **00:00:30 - 00:00:45**: 讲师展示如何通过 `@GrpcClient` 注解注入 `StockFinanceServiceBlockingStub`，并调用其 `updateAccount` 方法来更新账户余额。
*   **00:00:45 - 00:01:00**: 讲师演示了 `updateAccount` 方法的调用逻辑，包括构建请求、处理响应并抛出异常。
*   **00:01:00 - 00:01:15**: 讲师在 `StockDealServiceImpl.java` 中展示了 `calcOrderStatus` 方法，用于计算订单状态（全成交、部分成交、等待）。
*   **00:01:15 - 00:01:30**: 讲师在 `StockDealServiceImpl.java` 中展示了 `generateTradeDeal` 方法，用于计算成交价格、数量和佣金。
*   **00:01:30 - 00:01:45**: 讲师在 `StockTradePendingServiceImpl.java` 中展示了 `generateTradeDeal` 方法的完整实现，包括设置交易记录和调用金融服务。
*   **00:01:45 - 00:02:00**: 讲师在 `bootstrap-dev.yml` 配置文件中展示了 gRPC 服务的配置，包括端口、线程池和连接保持时间。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `3.4 挂单服务增加额度调整实现`
    *   **核心要点**: “挂单服务需要做撮合交易处理，也需调整账户的资金信息，我们在挂单服务里面增加额度调整处理接口的调用。”
    *   **代码示例**: `@GrpcClient("grpc-finance-server") private StockFinanceServiceGrpc.StockFinanceServiceBlockingStub stockFinanceServiceBlockingStub;`

*   **代码关键内容**:

    **1. `StockTradePendingServiceImpl.java` - 生成交易记录并调用金融服务**

    ```java
    @Transactional(rollbackFor = Exception.class)
    public TradeDeal generateTradeDeal(TradeStockQuoteLast quoteLast) {
        // ... 生成交易记录的代码 ...
        // 更新账户资金
        UpdateBalanceRequest updateBalanceRequest = UpdateBalanceRequest.newBuilder()
            .setAdjustBalance(getAdjustBalance(request.getDirection(), amount))
            .setAccountId(request.getAccountId())
            .build();
        UpdateBalanceResponse updateBalanceResponse = stockFinanceServiceBlockingStub.updateAccount(updateBalanceRequest);
        if (!GlobalConstants.STATUS_OK.equals(updateBalanceResponse.getStatus())) {
            log.warn("update account balance error => code: {}, msg: {}", updateBalanceResponse.getCode(), updateBalanceResponse.getMsg());
            throw new ComponentException(ApplicationErrorCodeEnum.parseByCode(updateBalanceResponse.getCode()));
        }
        return deal;
    }
    ```

    **2. `StockDealServiceImpl.java` - 计算订单状态**

    ```java
    private int calcOrderStatus(long initVolume, long dealVolume) {
        if (initVolume == dealVolume) {
            return GlobalConstants.ORDER_STATUS_ALL;
        } else if (initVolume > dealVolume) {
            return GlobalConstants.ORDER_STATUS_PART;
        } else {
            log.error("Process in GrpcDealService.calcOrderStatus method, error: dealVolume > initVolume");
            return GlobalConstants.ORDER_STATUS_WAIT;
        }
    }
    ```

    **3. `StockDealServiceImpl.java` - 计算成交价格和数量**

    ```java
    // 计算成交价格和数量
    deal.setExecPrice(MathUtils.divLong(amount, volume));
    deal.setExecTime(new Date());
    deal.setDirection(request.getDirection());
    deal.setCommission(MathUtils.calcCommission(amount, tradeGroup.getCommissionRate()));
    deal.setStatus(0);
    ```

    **4. `bootstrap-dev.yml` - gRPC 服务配置**

    ```yaml
    grpc:
      server:
        port: 19996
      task:
        corePoolSize: 5
        maxPoolSize: 10
        queueCapacity: 500
        keepAliveSeconds: 60
    ```

---

### 4) 关键场景与演示描述

*   **场景一：环境与目标设定 (00:00:00-00:00:15)**
    *   讲师首先在 Typora 文档中定位到 `3.4 挂单服务增加额度调整实现` 章节，明确了本节的开发目标。
    *   接着，讲师在 IntelliJ IDEA 中打开 `StockTradePendingServiceImpl.java` 文件，展示了该服务类的结构和其依赖的 DAO 接口，为后续的代码修改做好准备。

*   **场景二：核心业务逻辑实现 (00:00:15-00:00:45)**
    *   讲师将光标移动到 `generateTradeDeal` 方法，开始讲解其内部逻辑。
    *   讲师重点演示了如何通过 `@GrpcClient` 注解注入 `StockFinanceServiceBlockingStub`，并调用其 `updateAccount` 方法来更新账户余额。
    *   讲师展示了 `updateAccount` 方法的调用逻辑，包括构建请求、处理响应并抛出异常，确保资金调整的原子性和错误处理。

*   **场景三：辅助功能演示 (00:01:00-00:01:30)**
    *   讲师切换到 `StockDealServiceImpl.java` 文件，演示了 `calcOrderStatus` 方法，用于计算订单状态（全成交、部分成交、等待）。
    *   讲师接着演示了 `generateTradeDeal` 方法，用于计算成交价格、数量和佣金，为挂单服务提供必要的交易数据。

*   **场景四：配置文件查看 (00:01:45-00:02:00)**
    *   讲师在 `bootstrap-dev.yml` 配置文件中展示了 gRPC 服务的配置，包括端口、线程池和连接保持时间，说明了服务的运行环境和资源分配。

---

以上是根据视频画面进行的结构化技术分析。
