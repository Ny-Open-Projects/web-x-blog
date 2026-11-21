# 08-资金额度调整-功能验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始在挂单服务里面

去增加可用资金的判断和交易

上面咱们已经实现了

额度调整接口的调用处理

那在挂单的时候呢

还需要增加对资金的交易判断

如果资金充足

挂单呢才能成功处理

这里我们没有采用

冻结金额的方式来做实现

在成交的时候呢

是增加了一层对资金的判断

来做具体控制

但是在实际生产当中

是要有冻结金额的处理

目的是要防止交易所

接收到虚拟的交易信息

如果不去冻结它的金额

那么用户可以随意发送

任何金额的下单数据

而在交易所里面

每笔挂单必须是真实有效的

不能发送虚假的价格和委托数量

好接下来咱们从代码上

做具体实现

咱们去修改资金脚本文件

回到工程当中

定位到Proto文件

这里咱们要定义一个

获取账户资金的接口

咱们从讲义当中将代码copy进来

这里是定义了

获取账户资金的RPC接口

还需要定义一个请求参数对象

以及响应对象

回到讲义当中

将代码copy在最下面

获取账户资金的接口

账户资金接口的请求数据结构比较简单

只需要传递HKID

这个由代理服从文件当中获取

下面是获取账户资金的返回数据结构

返回的信息比较简单

交易账户ID以及可用的资金

定义完成之后

通过脚本工具生成对应的交易代码

右键Open in terminal

执行Proto GRPC

好生成成功

咱们检查一下

在这里刷新

可以看到获取账户资金的传输结构代码

就已经生成完成

回到讲义当中

那接下来我们就在资金服务里面

增加账户资金查询接口的处理

我们去修改资金服务的GRPC接口

定义到对应的代码

回到讲义当中

将对应的接口copy进来

放在最下面

咱们检查一下

整个调用处理逻辑比较简单

外层是做了一层封装

通过stock finance service

get balance这个方法去做具体的实现

我们将get balance这个方法做一个实现

alt加enter

创建对应的方法

添加注释

这个是获取账户资金的余额

给他抛出业务异常

接着我们去实现内当中

去实现该方法

将注释copy进来

再去实现内当中

去实现该方法

将注释copy进来

回到实现内

让咱们去做具体实现

首先要获取账号信息

share account

通过DAO

去获取具体的交易账户对象

传递account id

然后做一个唯空判断

如果唯空

咱们要抛出对应的异常

srew new compound exception

给他一个异常错误码

account not found

然后我们要返回资金的余额

share account get balance

如果唯空

那么返回为0

不要返回为none

不唯空的话

就返回实际的可用资金

好

这个就是获取账户资金余额的接口

咱们再回到GRBC的接口层

好

这里就没再报错

那资金服务的获取账户资金的接口

就已经实现完成

接下来我们去挂单服务里面

增加对资金的调研判断

找到stock pending

去修改stock pending的实现类

我们首先要去定义GRBC的远程调用接口

这个之前已经定义好了

那我们直接去增加账户资金的判断处理

增加账户资金的判断

要在创建订单之前

所以咱们去找到

rate

share order的方法

我们在最上面增加判断处理逻辑

首先要调用资金服务接口

获取账户的可用资金

get balance request

发送请求

get balance

构造请求参数对象

set count id

传递交易账户ID

build进行构建

接着咱们定义响应对象

get balance response

通过GRBC接口做远程调用

传递请求参数对象

那咱们要对处理结果做一个判断

如果不等于成功的状态

那咱们要抛出对应的异常提示

首先增加日子打印

get account balance

记录错误码

记录错误信息

get balance response

get statement

记录信息

将响应参数里面的

消息

传递进去

接着我们抛出异常提示

application

add code

做一个异常码的转换

get balance

response

拿到返回的错误码

这里就是获取账户可用资金的处理

接着我们要去判断

账户

资金是否充足

long

balance

获取可用资金

然后要去计算出该笔订单所需要的资金

e-amount

mass utils

参考的成交数量

还有请求价格

做一个乘法处理

得出该笔订单所需要的资金

然后和可用资金做判断

如果是大于可用资金

说明资金余额不足

我们要给出

错误异常提示

compend exception

给它一个错误异常码

pending

balance

not enough

好

这一讲呢

我们就实现了

挂单服务

对账户可用资金的判断处理

咱们定义了获取账户的资金接口

然后在资金服务里面

增加了账户资金查询接口的

处理和实现

最后是在挂单服务里面增加了账户资金的判断

好

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“挂单服务”功能的开发与实现。核心内容是为挂单操作增加一个“可用资金判断校验”的环节，以确保用户在下单时账户资金充足。该功能通过 gRPC 服务进行跨模块通信，具体实现包括：
- **定义新的 gRPC 接口**：在 `StockFinanceService.proto` 文件中新增 `GetBalanceRequest` 和 `GetBalanceResponse` 消息结构。
- **实现服务端逻辑**：在 `StockFinanceServiceImpl` 中编写 `getBalance` 方法，通过 DAO 层查询账户余额。
- **调用服务端逻辑**：在 `StockTradePendingServiceImpl` 中，于创建订单前调用 `getBalance` 接口，并根据返回结果判断是否抛出异常。

整个过程体现了微服务架构下，通过定义清晰的接口和调用链路，实现业务逻辑的解耦与校验。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:05**: 视频开场，展示课程大纲，聚焦于“3.5 挂单服务增加可用资金判断校验”章节。
- **00:05 - 00:15**: 展示 `StockFinanceService.proto` 文件，定义 `GetBalanceRequest` 消息结构。
- **00:15 - 00:25**: 在 IntelliJ IDEA 中，通过右键菜单将 `.proto` 文件编译为 Java 代码。
- **00:25 - 00:35**: 展示 `StockFinanceServiceImpl.java` 文件，编写 `getBalance` 方法的实现逻辑。
- **00:35 - 00:45**: 展示 `StockTradePendingServiceImpl.java` 文件，编写 `createTradeOrder` 方法中调用 `getBalance` 的逻辑。
- **00:45 - 00:55**: 在 `createTradeOrder` 方法中，调用 `getBalance` 接口并处理返回结果，判断余额是否充足。
- **00:55 - 01:05**: 展示 `getBalance` 方法的实现细节，包括查询数据库和抛出异常的逻辑。
- **01:05 - 01:15**: 展示 `createTradeOrder` 方法中，根据 `getBalance` 的返回值决定是否抛出 `ComponentException`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **章节标题**：`3.5 挂单服务增加可用资金判断校验`
- **核心思想**：在挂单时，需要增加对资金的校验，确保资金充足才能成功挂单。生产环境中，必须有冻结金额的处理，防止交易所接收到虚假的交易信息。
- **子章节**：
  - `3.5.1 定义获取账户资金接口`
  - `3.5.2 资金服务增加账户资金查询接口的实现`
  - `3.5.3 增加账户资金判断`

#### 代码关键内容

- **gRPC 接口定义 (`StockFinanceService.proto`)**：
  ```protobuf
  message GetBalanceRequest {
    int64 accountId = 1;
  }

  message GetBalanceResponse {
    int32 status = 1;
    string message = 2;
    int64 balance = 3;
  }
  ```

- **服务端实现 (`StockFinanceServiceImpl.java`)**：
  ```java
  @Override
  public long getBalance(Long accountId) throws ComponentException {
      TradeAccount tradeAccount = tradeAccountDao.getById(accountId);
      if (null == tradeAccount) {
          throw new ComponentException(ApplicationErrorEnum.ACCOUNT_NOT_EXIST);
      }
      return tradeAccount.getBalance();
  }
  ```

- **调用端实现 (`StockTradePendingServiceImpl.java`)**：
  ```java
  @Override
  public TradeOrder createTradeOrder(LimitPlaceOrderRequestVo request) throws ComponentException {
      // 1. 创建订单对象
      TradeOrder order = new TradeOrder();
      order.setDirection(request.getDirection());
      order.setStockId(request.getStockId());
      order.setAccountId(request.getAccountId());

      // 2. 充值股票信息
      TradeStock tradeStock = tradeStockDao.getById(request.getStockId());
      if (null != tradeStock) {
          order.setStockCode(tradeStock.getCode());
      }

      // 3. 调用资金服务，获取账户的可用资金
      GetBalanceRequest getBalanceRequest = GetBalanceRequest.newBuilder()
          .setAccountId(request.getAccountId())
          .build();

      GetBalanceResponse getBalanceResponse = stockFinanceServiceBlockingStub.getAccountBalance(getBalanceRequest);

      // 4. 判断余额是否充足
      if (GlobalConstants.STATUS_OK.equals(getBalanceResponse.getStatus())) {
          // 余额充足，继续处理订单
      } else {
          // 余额不足，抛出异常
          throw new ComponentException(ApplicationErrorEnum.parseByCode(getBalanceResponse.getStatus()));
      }

      // 5. 返回订单对象
      return order;
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：定义 gRPC 接口**
  - **描述**：讲师在 `StockFinanceService.proto` 文件中，新增 `GetBalanceRequest` 和 `GetBalanceResponse` 消息结构，用于定义获取账户余额的请求和响应格式。
  - **演示**：在 IntelliJ IDEA 中，右键 `.proto` 文件，选择“Generate Java Code”选项，自动生成对应的 Java 类。

- **场景二：实现服务端逻辑**
  - **描述**：讲师在 `StockFinanceServiceImpl.java` 文件中，编写 `getBalance` 方法，通过 `tradeAccountDao` 查询数据库获取账户余额。
  - **演示**：在代码中，首先通过 `tradeAccountDao.getById` 查询账户对象，如果账户不存在则抛出 `ComponentException`，否则返回账户余额。

- **场景三：调用服务端逻辑**
  - **描述**：讲师在 `StockTradePendingServiceImpl.java` 文件中，编写 `createTradeOrder` 方法，在创建订单前调用 `getBalance` 接口。
  - **演示**：通过 `stockFinanceServiceBlockingStub.getAccountBalance` 方法调用 gRPC 服务，获取账户余额，并根据返回的状态码判断余额是否充足。如果余额不足，抛出 `ComponentException`。

- **场景四：异常处理**
  - **描述**：在 `createTradeOrder` 方法中，如果 `getBalance` 返回的状态码不是 `STATUS_OK`，则抛出 `ComponentException`，并根据状态码解析具体的错误信息。
  - **演示**：在代码中，使用 `ApplicationErrorEnum.parseByCode` 方法，根据返回的状态码获取对应的错误信息，并抛出异常。

---

以上是根据视频画面进行的结构化技术分析，希望对您有所帮助。
