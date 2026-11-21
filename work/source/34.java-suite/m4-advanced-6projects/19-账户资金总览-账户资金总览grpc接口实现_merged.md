# 19-账户资金总览-账户资金总览grpc接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们开始去讲解资金服务账户资金从哪接口的实现

回到工程当中

首先咱们去实现GRBC的接口

在资金服务下面

GRBC的包下面

咱们去创建一个新的实现类

New JAL Class

名字我们就叫GRBC Stock Finance Service

在这里要去继承

Stock Finance Service

GRBC的附类

Employment Space

增加注解

GRBC Service

增加日子查件

Login Project 2

首先咱们要去注入资金服务的业务实现接口

这里咱们还没有实现

我们先做一个DE

右键New JAL Class

Interface

先定义它的接口

Stock Finance Service

接下来我们再去创建它的实现类

New Package

Employment

创建它的实现类

右键New JAL Class

Stock Finance Service

Employment

实现刚才所定义的资金服务的接口

好

再回到咱们的GRBC

这个是GRBC的接口层

将刚才所定义的业务层接口录入进来

Stock Finance Service

Outwide

增加注释

这个是资金服务的业务实现类

接下来咱们去重写它的接口

Edit Insert

Overlay Methods

选中Get Finance Overview

咱们对该接口做一个重写

添加注释

这个是Forge.com.au

Forge.com.au

上户资金总打的接口

接着咱们去定义返回的消息体

Response

注意这个是在GRBC的包下面

Response

证明为Now

后外围增加

Try Catch 异常捕获

Catch 异常处理

咱们就从讲义当中将代码扣币过来

最下面还要增加数据的输出

Response

Opensaw

On Next

将Response

对象输出给调用方

response of the

标记完成 on complete

接下来咱们继续实现

GRPC接口的处理逻辑

这里是调用

业务接口

获取账户资金

总览的

信息

咱们要拿到获取账户资金

总览的信息

需要定义一个vgo对象

做相应的记录

在这里咱们就来创建一个新的vgo

叫cast

名称叫

account

overview

上面增加

longbook的data标记

这里我们要定义它的

业务属性的信息记录

long

position

for bit

这个是总的持仓盈亏

下面我们还定义

它的当日持仓盈亏

long day for bit

当日持仓盈亏

接下来定义它的总市值

long

total

market

amount

这个是总市值

总市值

然后再定义它的总资产

long内型

total

assess

总资产

最后我们还定义账户的余额

long

balance

账户余额信息

好

这里咱们就定义完成了账户资金总卖的vgo

阐述对象

那回到刚才的GRBC的service

然后定义account overview vgo

记录处理的结果

通过stonefinance service

业务接口做对应处理

这个接口咱们还没实现

先定义好

account summary

summary

传递交易账户的ID

然后我们要对处理结果做一个包装返回

转换为tb的数据结构对象

new

builder

set

day profit

account overview vgo

get day profit

然后传递持仓收益

position profit

position profit

设置总市值

总市值

总市值

total market

total market command

来设置它的总市场

total assets

account overview vgo.get total assets

设置balance可用于

account overview vgo.get balance

最后就是设置状态

这里并没有显示出来

让咱们看一下

注意这个对象呢

不要导入错误

我们要导入GRBC包下面的项目

好

这里做个替换

是overview response

接着我们再设置它的处理状态

states

global

consistence

.states ok

要用new的方法进行构建

好

在这里呢就是至今总体的GRBC结构层的实现

下面的章节咱们再去实现service的处理逻辑

好

那这一讲的内容咱们就先讲到这里

好

我们下期再见

拜拜

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock` 的金融系统项目中，实现一个基于 gRPC 协议的“资金服务账户资金总览”接口的开发过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建 gRPC 服务类 `GrpcStockFinanceService`，并实现其核心方法 `getFinanceOverview`。该方法负责调用下游的业务服务（`IstockFinanceService`）获取账户资金汇总数据，并将结果封装成 gRPC 响应对象返回。整个过程强调了服务层的职责划分、异常处理和数据结构的使用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，明确当前章节为 **3.4 资金服务账户资金总览接口实现**。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，打开项目 `bulls-stock`，并定位到 `GrpcStockFinanceService.java` 文件，准备进行代码实现。
*   **00:15 - 00:30**: 讲师展示 `GrpcStockFinanceService` 类的结构，这是一个继承自 `StockFinanceServiceGrpc.StockFinanceServiceImplBase` 的 gRPC 服务类。它通过 `@Autowired` 注入了 `ITradePositionDao` 和 `IstockFinanceService` 两个依赖。
*   **00:30 - 00:45**: 讲师开始编写 `getFinanceOverview` 方法的主体。该方法接收一个 `GetFinanceOverviewRequest` 请求和一个 `StreamObserver<GetFinanceOverviewResponse>` 响应观察者。
*   **00:45 - 01:00**: 讲师在方法中初始化一个 `GetFinanceOverviewResponse` 响应对象，并开始编写 `try-catch` 异常处理块，用于捕获业务异常和系统异常。
*   **01:00 - 01:15**: 讲师调用业务服务接口 `stockFinanceService.calAccountSummary(request.getAccountId())` 来获取账户资金汇总信息，并将返回值赋给 `AccountOverviewVo` 对象。
*   **01:15 - 01:30**: 讲师使用 `GetFinanceOverviewResponse.newBuilder()` 构建器，将 `AccountOverviewVo` 中的各个字段（如 `dayProfit`, `positionProfit`, `totalMarketAmount` 等）设置到响应对象中。
*   **01:30 - 01:45**: 讲师完成代码编写，将响应对象通过 `responseObserver.onNext(response)` 发送给客户端。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: `3.4 资金服务账户资金总览接口实现`。
    *   **代码注释**: `// 调用业务接口获取账户资金总览的信息`。
    *   **异常处理注释**: `// 业务异常返回` 和 `// 系统异常返回`。

*   **关键代码**:
    *   **gRPC 服务类定义**:
        ```java
        @GrpcService
        @Log4j2
        public class GrpcStockFinanceService extends StockFinanceServiceGrpc.StockFinanceServiceImplBase {
            @Autowired
            private ITradePositionDao tradePositionDao;
            @Autowired
            private IstockFinanceService stockFinanceService;
        }
        ```
    *   **核心方法 `getFinanceOverview`**:
        ```java
        @Override
        public void getFinanceOverview(GetFinanceOverviewRequest request, StreamObserver<GetFinanceOverviewResponse> responseObserver) {
            GetFinanceOverviewResponse response = null;
            try {
                // 调用业务接口获取账户资金总览的信息
                AccountOverviewVo accountOverviewVo = stockFinanceService.calAccountSummary(request.getAccountId());
                response = GetFinanceOverviewResponse.newBuilder()
                    .setDayProfit(accountOverviewVo.getDayProfit())
                    .setPositionProfit(accountOverviewVo.getPositionProfit())
                    .setTotalMarketAmount(accountOverviewVo.getTotalMarketAmount())
                    .setTotalAssets(accountOverviewVo.getTotalAssets())
                    .setBalance(accountOverviewVo.getBalance())
                    .build();
                responseObserver.onNext(response);
            } catch (ComponentException e) {
                log.error(e.getMessage(), e);
                response = GetFinanceOverviewResponse.newBuilder().setStatusCode(e.getErrorCodeEnum().getCode()).build();
                responseObserver.onError(e);
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                response = GetFinanceOverviewResponse.newBuilder().setStatusCode(GlobalConstants.STATUS_ERROR).build();
                responseObserver.onError(e);
            }
        }
        ```
    *   **数据传输对象 `AccountOverviewVo`**:
        ```java
        private long positionProfit; // 当日持仓利润
        private long dayProfit;      // 当日利润
        private long totalMarketAmount; // 总市值
        private long totalAssets;    // 总资产
        private long balance;        // 余额
        ```

---

### 4) 关键场景与演示描述

*   **场景一：服务类创建与依赖注入** (00:05-00:15)
    *   讲师在 IntelliJ IDEA 中打开项目，导航至 `GrpcStockFinanceService.java`。
    *   通过代码展示，讲师说明该类继承自 gRPC 服务基类，并通过 `@Autowired` 注入了两个核心依赖：`ITradePositionDao` 和 `IstockFinanceService`，体现了服务层与数据层、业务层的解耦。

*   **场景二：核心方法实现** (00:30-01:30)
    *   讲师在 `getFinanceOverview` 方法中，首先创建一个响应对象 `GetFinanceOverviewResponse`。
    *   通过 `try-catch` 块，讲师演示了如何处理业务异常和系统异常，并将错误码封装到响应中。
    *   讲师调用 `stockFinanceService.calAccountSummary(request.getAccountId())` 方法，这是与业务逻辑层的交互。
    *   讲师使用 `GetFinanceOverviewResponse.newBuilder()` 构建器，将从业务层获取的 `AccountOverviewVo` 对象中的多个字段（`dayProfit`, `positionProfit`, `totalMarketAmount`, `totalAssets`, `balance`）逐一设置到响应对象中。
    *   最后，通过 `responseObserver.onNext(response)` 将最终的响应发送给客户端。

*   **场景三：数据结构与异常处理** (01:00-01:15)
    *   讲师在编写代码时，通过鼠标悬停和 IDE 的智能提示，展示了 `AccountOverviewVo` 类的结构，包括 `positionProfit`, `dayProfit`, `totalMarketAmount` 等字段。
    *   讲师在 `catch` 块中，演示了如何将异常信息记录到日志，并根据异常类型设置不同的错误码，体现了服务层对异常的统一处理和错误信息的标准化。

---

以上是根据视频画面进行的结构化技术分析。
