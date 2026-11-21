# 05-资金额度调整-交易服务增加额度调整处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就去修改交易服务

去增加实现额度调整功能接口的调用

之前咱们是实现了下单以及挂单的功能

但当时咱们是侧重对应的业务逻辑处理

并没有对账户的资金做相应的修改和调整

这里我们就需要让他完善一下

增加对账户资金额度的调整

这里要注意一下

我们将所有浮点计算都改为长整形处理

从接口结构到业务层实体和数据结构

都要做对应的调整

而下面我们就来做具体的实现

回到工程当中

我们要去修改Stop Deal Service Implement的实现类

先定位到该实现类

如何增加额度调整的调用呢

首先咱们要定义对应的GRB

GRBC接口

Private

Stock

Finance

GRBC

Stock

Blocking Stop

增加对应的注册

GRBC Client

定义配置名称

GRBC Finance 收货

增加注册

这个是资金服务

GRBC接口

如何去修改原有的逻辑呢

那我们要定位到Generator

Shared Deal的方法

这个呢是生成成交记录

我们要在这个方法里面呢

做对应的调整

做对应的修改

把修改逻辑放在最后面

这里是更新账户资金

先要组装额度调整的请求参数

Update Balance Request

创建Request的对象

点New Builder Set Adjust Balance

所要调整的资金额度

这里要通过一个方法去计算

是增加额度还是减少额度

通过Get Adjust Balance方法

做对应的实现

传递买卖方向

然后是调整的金额

Deal

还加上它的手续费

接着的话呢

去设置Account ID

传递Account ID

最后要用Build方法进行构建

接着通过GRBC接口进行远程交易用

咱们先定义它的返回对象

Balance Response

Update Balance Response

通过GRBC接口或调用

调用Update Account Balance方法

传递请求参数

调用完成之后

我们还要判断它的处理结果是否处理成功

Global Consistence

States OK

-1股市

判断它的响应状态

Update Response Get States

为了变异跟踪

咱们要增加一个日之记录

这里呢

是给它一个提示信息

这里呢

是给它一个警告信息

因为处理结果是返回的失败

那我们要将它的参数信息也一并反映出来

Balance

Add

Code

处理了结果

Message

返回的消息

Update

Response

Get States

Get Message

通过这个日之信息打印

咱们就知道它大概的错误

便于追踪和排查

下面还要抛出对应的异常

Compand Exception

给出一个异常错误码

这个错误码就根据响应结果的状态码做一个转换

那么咱们可以在这个枚举里面去扩展一个实现方法

在最下面

咱们增加一个转换的方法

转换方法的名称

Page来扣的

StreetCoin扣的

我们做一个便利

这里面就是便利该枚举里面定义的所有业务异常码

那么怎么拿到所有的业务异常码呢

这个是一个集合通过Values方法

拿到之后我们就根据状态码做判断比较

Get Code

如果是相等

我们就将枚举返回出去

如果是没有找到

就返回一个失败的错误码

添加注释

这个是根据

错误码

转换

枚举对象

好再回到刚才的实现逻辑

我们就可以调用该方法进行枚举的转换

可以指白扣的

将返回的状态码转入进去

这样就完成了账户资金额度调整接口的调用

这里还有一个异常提示

我们需要在方法上面

将异常抛出去

Sluice Compound Exception

整个逻辑处理就已经实现完成

刚才所提到的获取额度调整金额的方法

我们可以来看一下

这个实现就比较简单

它根据买卖方向去判断额度调整的金额

到底是为正数还是负数

如果是买方向的

那么对应就是负数要扣除账户的资金

相反如果是卖出

这个资金就要每加

接下来我们还在工程配置当中

增加对资金服务GRPC接口调用配置

在最下面

这里做一个copy

让配置信息对齐

我们修改一下

这个是资金服务Binance Server

此项的服务名称也要改成Stocker Binance

这个是资金服务的配置信息

可以Ctrl检查一下

这个配置可以识别没有问题

好那咱们再回到讲习当中

这里要注意一下

下方的资金调整是要求保持事务的一致性

因为它是去生成订单信息

还要去修改账户的资金信息

这不是同一个服务

同一个数据源的操作

当然我们可以将资金调整的顺序

放在最后面

整个方法再去加入事务控制

这样是可以保障一致

因为我们可以把资金调整的顺序放在最后面

因为如果是资金调整的接口调用失败

那么它会通过失误做一个回滚

如果资金调整接口是调用成功

这个失误就会提交生效

但是需要严格的顺序控制

业务使用场景就会比较受限

而且如果是跨越多个服务

并且有严格的处理顺序

那这个时候呢

就必须要加入分布式失误的处理

在下面的章节

咱们会讲解该如何去实现

好

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是“交易系统”系列课程的第17天，主题为“额度调整功能”的实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何在交易服务中增加对账户资金的调整功能。核心内容包括：
- **业务逻辑**：在生成交易委托（`TradeDeal`）时，需要调用资金服务（`StockFinanceService`）来更新账户余额。
- **技术实现**：使用 gRPC 调用远程资金服务，通过 `UpdateBalanceRequest` 请求更新余额，并处理返回的响应。
- **异常处理**：对资金服务返回的错误码进行解析，并抛出自定义的 `ComponentException`。
- **代码结构**：展示了 `StockDealServiceImpl` 中 `generateTradeDeal` 方法的修改过程，以及如何集成资金服务的 gRPC 客户端。

整个过程体现了在分布式系统中，如何通过服务间调用和异常处理来实现业务功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:30**: 课程引入与目标说明。讲师在 Markdown 文件中指出，本节目标是实现“交易服务增加额度调整”功能，即在下单时同步调整账户资金。
- **00:30 - 01:00**: 代码环境准备。讲师展示 IntelliJ IDEA 中的项目结构，定位到 `StockDealServiceImpl` 类，并准备修改 `generateTradeDeal` 方法。
- **01:00 - 02:00**: 实现资金服务调用。讲师在 `generateTradeDeal` 方法中，创建 `TradeDeal` 对象并设置其属性，然后调用 `StockFinanceServiceBlockingStub` 的 `updateBalance` 方法。
- **02:00 - 03:00**: 处理返回值与异常。讲师演示如何获取 `UpdateBalanceResponse` 的状态码，并根据状态码决定是否抛出异常。代码中使用了 `ApplicationErrorCodeEnum` 来映射错误码。
- **03:00 - 04:00**: 异常处理与抛出。讲师将资金服务的错误码转换为自定义异常 `ComponentException`，并抛出，以确保业务逻辑的完整性。
- **04:00 - 05:00**: 代码审查与总结。讲师对修改后的代码进行快速审查，强调了资金调整与交易生成的强关联性，并指出后续可能需要处理分布式事务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`Day17.md - Typora`
- **章节标题**：`3.3 交易服务增加额度调整实现`
- **关键说明**：
  - “将所有浮点计算都改为长整型处理，从接口结构，业务层，实体和数据结构都要做相应调整。”
  - “下单的资金调整，是要求保持事务的一致性，这不是同一个服务同一个数据源的操作...”

#### 代码关键内容

- **gRPC 客户端定义**：
  ```java
  @GrpcClient("grpc-finance-server")
  private StockFinanceServiceGrpc.StockFinanceServiceBlockingStub _stockFinanceServiceStub;
  ```

- **交易委托生成方法 (`generateTradeDeal`) 的核心部分**：
  ```java
  TradeDeal deal = new TradeDeal();
  deal.setAccountId(request.getAccountId());
  deal.setAccountNo(tradeAccount.getAccountNo());
  deal.setStockId(request.getStockId());
  deal.setStockCode(tradeStock.getCode());
  deal.setStockName(tradeStock.getName());
  deal.setStockMarket(tradeStock.getMarketNo());
  deal.setExecVolume(Long.valueOf(volume).intValue());
  deal.setExecPrice(MathUtils.divLong(amount, volume));
  deal.setExecTime(new Date());
  deal.setDirection(request.getDirection());
  ```

- **调用资金服务更新余额**：
  ```java
  UpdateBalanceRequest updateBalanceRequest = UpdateBalanceRequest.newBuilder()
      .setAccountId(request.getAccountId())
      .setStockId(request.getStockId())
      .setDirection(request.getDirection())
      .setAdjustBalance(getAdjustBalance(request.getDirection(), amount, volume))
      .build();
  UpdateBalanceResponse updateBalanceResponse = _stockFinanceServiceStub.updateBalance(updateBalanceRequest);
  ```

- **异常处理逻辑**：
  ```java
  if (!GlobalConstants.STATUS_OK.equals(updateBalanceResponse.getStatus())) {
      throw new ComponentException(ApplicationErrorCodeEnum.parseByCode(updateBalanceResponse.getStatus()));
  }
  ```

- **自定义错误码枚举类 (`ApplicationErrorCodeEnum`) 的关键方法**：
  ```java
  public static ApplicationErrorCodeEnum parseByCode(String code) {
      for (ApplicationErrorCodeEnum errorCodeEnum : values()) {
          if (errorCodeEnum.code.equals(code)) {
              return errorCodeEnum;
          }
      }
      return null;
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：引入资金调整功能**
  - 讲师在 Typora 文档中指出，之前的下单和挂单功能没有涉及资金调整，现在需要增加对账户资金的调整。
  - 他强调了“浮点计算改为长整型”的重要性，以避免精度问题。

- **场景二：在 `StockDealServiceImpl` 中实现资金调用**
  - 讲师在 IntelliJ IDEA 中打开 `StockDealServiceImpl.java` 文件，定位到 `generateTradeDeal` 方法。
  - 他演示了如何创建 `TradeDeal` 对象并设置其属性。
  - 接着，他通过 `StockFinanceServiceBlockingStub` 调用 `updateBalance` 方法，并传入 `UpdateBalanceRequest`。

- **场景三：处理资金服务的返回值**
  - 讲师展示了如何获取 `UpdateBalanceResponse` 的状态码。
  - 他演示了如何使用 `ApplicationErrorCodeEnum` 来解析状态码，并根据状态码决定是否抛出异常。

- **场景四：抛出自定义异常**
  - 讲师将资金服务的错误码转换为 `ComponentException`，并抛出。
  - 他强调了异常处理的重要性，以确保业务逻辑的完整性和一致性。

- **场景五：代码审查与总结**
  - 讲师对修改后的代码进行了快速审查，强调了资金调整与交易生成的强关联性。
  - 他指出，如果资金调整和交易生成跨多个服务，可能需要引入分布式事务处理。

---

以上是根据视频画面进行的结构化技术分析报告。
