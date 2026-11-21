# 29-XXL_JOB集成运用-获取交割单接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

这一讲我们就去学习和实现资金服务

获取账户交个单接口的处理

GRBC接口层的处理逻辑比较简单

这里呢

咱们就直接引用过去

定位到GRBC

Stalk

Finance

Service

放置最下面

咱们来看一下它的具体实现

在这里它是通过业务层接口

去获取账户的交个单数据

拿到账户交个单数据之后

做一个围攻判断

然后做便利

复制对应的数据

将数据包装为传输的数据结构

最后将整个响应包输出给调用方

这里要注意一下

在做数据复制的时候

采用的是自定义的接口

去实现数据的复制

目的是为了避免

Protot主性复制的时候

出现空置成异常

然后下面是针对于日期

做了特殊处理

复制的时候做了排除

将日期转换为Log长整形

然后下面是针对于日期

接着咱们再去实现

它的业务层接口

创建好对应的接口

给它添加注释

这个是获取账户的交个单数据

然后进入实现类

然后我们将它

拷贝至实现类当中

放在最下面

增加Olay的增加Public

接下来我们来做具体实现

首先我们要去转换

传入的时间参数

这里面传入的时间参数

传递的是时间戳Log类型

那么我们要将它转换为字符类型

定义String

TimeStart

DataUtils

GetFormat

DateBySeconds

传递TimeStart

这个方法的意思

就是将当前的时间戳

转化为格式化的日期

这格式化的日期是精确到秒

它会返回一个String字符类型

我们再定义String

TimeEnd

DateUtils

GetFormat

DateBySeconds

TimeEnd

然后我们要定义

账户的交购单数据集合

Resource

通过SharedAccountSettlementDuo

我们去获取交购单数据

AccountID

StringTimeStart

StringTimeStart

TimeEnd

然后是Return

Resource

接下来我们再回到GRBC的接口层

检查一下还有没有错误

这里还需要抛出对应的业务异常

我们要在接口里面增加Sloot

Sloot

CompandException

在时间类里面

我们也增加对应的异常抛出

Sloot

CompandException

好

那代码呢

就没有再包错

整个代码的处理呢

我们就已经实现完成

好这一讲就是对资金服务

获取账户交购单接口的实现

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个金融交易系统中“资金服务获取账户交割单接口”的实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 gRPC 服务层（`GrpcStockFinanceService`）中定义并实现一个异步流式接口 `getAccountSettlement`，该接口用于获取指定账户在指定时间范围内的交割单数据。实现的核心在于服务层的接口定义、底层业务逻辑的调用（通过 `StockFinanceServiceImpl`），以及对时间戳进行格式化处理（使用 `DateUtils` 工具类）。整个过程展示了如何将业务需求转化为具体的代码实现，并处理了异常情况。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开始，展示课程大纲，定位到章节 **3.9 资金服务获取账户交割单接口实现**。
*   **00:03 - 00:08**: 讲师在 `GrpcStockFinanceService` 接口文件中，展示需要新增的 `getAccountSettlement` 方法的定义，该方法接收 `GetAccountSettlementRequest` 和 `StreamObserver<GetAccountSettlementResponse>` 参数。
*   **00:08 - 00:13**: 讲师切换到 `StockFinanceServiceImpl` 文件，展示底层实现类 `StockFinanceServiceImpl` 的结构，包括其依赖的 DAO 层接口（`ITradePositionDao`, `ITradeDealDao`）。
*   **00:13 - 00:18**: 讲师在 `StockFinanceServiceImpl` 中定位到 `getTradeAccountSettlements` 方法，该方法用于获取交割单数据。
*   **00:18 - 00:23**: 讲师展示 `DateUtils` 工具类，重点是其 `getFmtDateByTime` 方法，用于将毫秒级时间戳转换为 `yyyy-MM-dd HH:mm:ss` 格式的字符串。
*   **00:23 - 00:28**: 讲师在 `StockFinanceServiceImpl` 中，将 `timeStart` 和 `timeEnd` 参数通过 `DateUtils.getFmtDateByTime` 方法转换为字符串。
*   **00:28 - 00:33**: 讲师调用 `tradeAccountSettlementDao.getSettlementsByTimeRange` 方法，传入账户ID和转换后的时间字符串，获取交割单列表。
*   **00:33 - 00:38**: 讲师在 `GrpcStockFinanceService` 中，将获取到的交割单列表 `settlementList` 通过 `StreamObserver` 的 `onNext` 方法逐条发送给客户端。
*   **00:38 - 00:43**: 讲师展示 `GrpcStockFinanceService` 中的异常处理逻辑，包括 `ComponentException`（业务异常）和 `Exception`（系统异常）的捕获与响应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **gRPC 服务接口定义 (`GrpcStockFinanceService.java`)**:
    ```java
    public void getAccountSettlement(GetAccountSettlementRequest request,
        StreamObserver<GetAccountSettlementResponse> responseObserver) {
        // 业务逻辑...
    }
    ```

*   **服务实现类 (`StockFinanceServiceImpl.java`)**:
    ```java
    public List<TradeAccountSettlement> getTradeAccountSettlements(long accountId, long timeStart, long timeEnd) {
        String strTimeStart = DateUtils.getFmtDateByTime(timeStart);
        String strTimeEnd = DateUtils.getFmtDateByTime(timeEnd);
        List<TradeAccountSettlement> results = tradeAccountSettlementDao.getSettlementsByTimeRange(accountId, strTimeStart, strTimeEnd);
        return results;
    }
    ```

*   **工具类 (`DateUtils.java`)**:
    ```java
    private static final String FMT_STANDARD = "yyyy-MM-dd HH:mm:ss";
    public static String getFmtDateByTime(long time) {
        return new SimpleDateFormat(FMT_STANDARD).format(new Date(time));
    }
    ```

*   **异常处理逻辑 (`GrpcStockFinanceService.java`)**:
    ```java
    } catch (ComponentException e) {
        log.error(e.getMessage(), e);
        response = GetAccountSettlementResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).build();
    } catch (Exception e) {
        log.error(e.getMessage(), e);
        response = GetAccountSettlementResponse.newBuilder().setStatus(GlobalConstants.STATUS_ERROR).build();
    }
    ```

#### **关键注释与说明**

*   **参数说明**: 传递的时间戳格式为毫秒，通过 `DateUtils.getFmtDateByTime` 方法转换为 `yyyy-MM-dd HH:mm:ss` 格式。
*   **异常处理**: 业务异常（`ComponentException`）和系统异常（`Exception`）均会返回状态码为 `STATUS_ERROR` 的响应。

---

### 4) 关键场景与演示描述

*   **场景一：接口定义与实现**
    讲师首先在 `GrpcStockFinanceService` 接口中定义了 `getAccountSettlement` 方法，该方法接收一个请求对象和一个响应观察者对象。随后，讲师在 `StockFinanceServiceImpl` 中实现了该方法，通过调用 DAO 层的方法获取交割单数据。

*   **场景二：时间格式化处理**
    讲师在 `StockFinanceServiceImpl` 中，将客户端传入的毫秒级时间戳 `timeStart` 和 `timeEnd`，通过 `DateUtils.getFmtDateByTime` 方法转换为 `yyyy-MM-dd HH:mm:ss` 格式的字符串，以便在数据库查询中使用。

*   **场景三：数据查询与流式返回**
    讲师调用 `tradeAccountSettlementDao.getSettlementsByTimeRange` 方法，传入账户ID和格式化后的时间字符串，获取交割单列表。然后，在 `GrpcStockFinanceService` 中，通过 `responseObserver.onNext(response)` 方法，将每一条交割单数据逐条发送给客户端，实现流式传输。

*   **场景四：异常处理**
    讲师展示了如何在 `GrpcStockFinanceService` 中处理异常。无论是业务异常还是系统异常，都会捕获并构造一个包含错误状态码的响应对象，通过 `responseObserver.onError` 方法发送给客户端，以通知客户端请求失败。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解该技术课程的核心内容和实现细节。
