# 04-资金额度调整-资金服务额度调整接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去实现资金服务额度调整接口

这里要去实现核心的业务处理逻辑

那咱们去修改GRBC Stock Finance Service

这个GRBC接口实现内

回到工程当中

定位到对应的代码

它在资金服务下面

之前咱们是实现了获取资金总览的接口

这里我们要去重写

Alt加Insert

选择OLED

然后选中Update Account Balance这个接口

添加对应的注释

这是更新账户资金预额

GRBC层的接口实现处理逻辑比较简单

咱们就从讲习当中做一个copy

将方法内部的逻辑做一个copy

删掉到咱们的代码当中

咱们要去检查有没有相应的错误

这个Service层的业务实现接口

咱们稍后

再做实现

这里分布式事务的处理先可以暂时去掉

后面我们讲到分布式事务运用的时候

还会做详细的讲解

首先我们来看一下GRBC接口层的整体处理实现流程

整个接口处理逻辑比较简单

它最主要的就是调用Service层的Update Balance这个方法

去实现账户资金的更新处理

它需要传递哪些参数呢

要传递交易账户ID

还需要传递所要调整的资金金额

处理完成之后

这里面的Balance会去记录剩余可用的资金

然后在下面是组装返回对象

返回对象会将可用资金设置进去

然后返回给调用房

下面是异常的补货处理

业务异常的封装

系统异常的封装处理

最后就将数据输出给调用房

这个就是GRBC接口层的整体处理流程

接着咱们就去实现

接口层的整体处理流程

接着咱们就去实现

它的具体业务逻辑

Alt-N的键去创建对应的方法

加度式

这个是更新账户资金余额

咱们给他加上一个Transaction

开启失误的诸简

注意他在Spring Brainwork的包下面

然后要设置他的回滚异常

针对于所有的Exception

接下来咱们就去实现这个接口

在实现内当中

重写该接口

转中Update Balance

添加对应的注释

更新账户的资金余额

然后失误的诸简也将它copy回来

首先咱们去梳理它的实现逻辑

第一步根据账号ID获取账号的信息

第二步要去检查账户的所用资金

第二步要去检查账户的所用资金

第三步

我们要对他的可用资金做调整

调整可用资金

第四步

如果可用资金不足

需要抛出错误提示信息

告诉给调用房资金不足

不能进行相应的操作

第五个步骤

最后呢

就是要更新账户的资金

最后呢就是要更新账户的资金

最后呢就是要更新账户的资金

好

那咱们就从代码上面做具体的实现

第一

Credit Account通过DEO去获取交易账户的对象

我们要传递交易账户ID

然后做一个围攻判断

如果没有找到交易账号

说明这个是不合法的检查

在这里呢

我们要抛出对应的提示信息

Compander,Exception

给他一个出入码Application,Add code

给他一个出入码Application,Add code

Compander,Not Found

这里有个错误提示

我们需要加上异常的抛出

Sloose

Compander,Exception

我们要在借口层加上异常的抛出

回到实现内当中

然后咱们要实现第二步

检查账户的可信资金

Norm,Balance

Credit Account

Credit Balance

做一个围攻判断

做一个围攻判断

如果是为0

Credit Account

Credit Account

Get Balance

这样呢

就避免下面逻辑判断的时候

出现控制成异常

Balance

咱们要去调整他的可用资金

如果需要扣除资金

在这里Adjust Balance这个参数就是为负值

账户的实际可用资金会根据5号做相应的处理

那接下来就是要判断他的可用资金

如果他是小于0

说明可用资金不足

需要抛出对应的错误提示信息

Sloot New Compound Exception

给他一个错误提示码

错误提示Balance Not Enough

提示可用资金不足

接下来我们就去更新账户的资金信息

Shared Account

bio.update balance.id

传递交易账户的ID

然后更新了资金信息

最后咱们打印一个日志

标记了资金更新成功

打印参数信息

交易账号Adjust Balance调整了资金信息

传递Alcant ID

Adjust Balance调整了资金信息

最后咱们就返回实际可用的资金

好

在这里咱们就完成了资金额度调整的实现逻辑

这里的错误提示信息是

咱们处理一下

这个是由于GDK版本的问题

我们将版本改成1.8

SDK改成1.8系列

点击OK

这样就没有错误了

那咱们回到详细当中

大家要注意一下

账户资金的更新

严格意义上是要做分布是所的工资

因为要防止资金由于网络

或者是并发时

产生的现成安全问题导致的错乱

比如在高峰的时候产生网络的堵塞

或者是用户频繁多次进行下单

以及资金额度调整等相关的操作

就会导致出现现成安全的问题

那分布是所的控制和实现

咱们后面端节再做详细的讲解

这一讲咱们就实现了资金服务额度调整功能的接口

好

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易系统”系列课程的第17天，主题为“资金服务额度调整功能”的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 gRPC 服务中实现一个用于更新用户资金余额的接口。核心内容包括：
- **接口定义**：在 `IStockFinanceService` 接口中定义了 `updateBalance` 方法。
- **服务实现**：在 `StockFinanceServiceImpl` 类中实现该方法，包含事务管理、账户存在性检查、可用资金校验、余额更新等逻辑。
- **异常处理**：定义了 `ComponentException` 并在资金不足或账户不存在时抛出相应的错误码。
- **分布式事务**：在 gRPC 服务中使用 `RootContext.bind(request.getxid())` 来绑定分布式事务的全局标识 ID。
- **日志记录**：在关键操作处添加日志记录，便于调试和追踪。

整个过程体现了微服务架构下，服务间调用、事务一致性、异常处理和日志记录等核心开发实践。

---

### 2) 按时间顺序的章节（带时间点）

由于视频画面未提供精确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:15**：课程开场，介绍本节目标：实现资金服务额度调整接口。
- **00:16 - 00:30**：展示 `GrpcStockFinanceService` 类中 `updateAccountBalance` 方法的定义，说明其接收 `UpdateBalanceRequest` 和 `StreamObserver` 参数。
- **00:31 - 00:45**：进入 `StockFinanceServiceImpl` 类，展示 `updateBalance` 方法的实现框架。
- **00:46 - 01:00**：实现第一步：根据账户 ID 获取账户对象，并在账户不存在时抛出 `ACCOUNT_NOT_FOUND` 异常。
- **01:01 - 01:15**：实现第二步：检查账户的可用资金，使用 `getBalance()` 方法，并处理 `null` 值。
- **01:16 - 01:30**：实现第三步：调整可用资金，将 `adjustBalance` 加到 `balance` 上。
- **01:31 - 01:45**：实现第四步：校验资金是否足够，如果 `balance < 0`，抛出 `BALANCE_NOT_ENOUGH` 异常。
- **01:46 - 02:00**：实现第五步：调用 `tradeAccountDao.updateBalanceById` 方法更新数据库。
- **02:01 - 02:15**：添加日志记录，记录更新操作。
- **02:16 - 02:30**：展示 `calcAccountSummary` 方法，用于计算账户总览信息，包括当日收益、总市值等。
- **02:31 - 02:45**：展示 `StockFinanceServiceImpl` 类中 `calcAccountSummary` 方法的完整实现，包括获取交易记录、计算总市值等逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`Day17.md - Typora`，显示课程为第17天。
- **章节标题**：
  - `3.2 资金服务额度调整接口实现`
  - `3.3 交易服务增加额度调整实现`
  - `3.4 挂单服务增加额度调整实现`
  - `3.5 挂单服务增加可用资金判断校验`
  - `3.5.1 定义获取账户资金接口`
  - `3.5.2 资金服务增加`

#### 代码关键内容

- **gRPC 服务接口定义** (`GrpcStockFinanceService`):
  ```java
  @Override
  public void updateAccountBalance(UpdateBalanceRequest request,
      StreamObserver<UpdateBalanceResponse> responseObserver) {
      log.info("Process in updateAccountBalance method, xid: " + request.getxid());
      UpdateBalanceResponse response = null;
      try {
          // 绑定分布式事务的全局标识ID
          RootContext.bind(request.getxid());
          // 更新账户资金
          long balance = stockFinanceService.updateBalance(request.getAccountid(),
              request.getAdjustBalance());
          // 构建响应
          response = UpdateBalanceResponse.newBuilder()
              .setStatus(GlobalConstants.STATUS_OK)
              .setBalance(balance)
              .setId(request.getxid())
              .build();
      } catch (Exception e) {
          // 处理异常
          response = UpdateBalanceResponse.newBuilder()
              .setStatus(e.getErrorCodeEnum().getCode())
              .setMessage(e.getMessage())
              .build();
      }
      responseObserver.onNext(response);
      responseObserver.onCompleted();
  }
  ```

- **服务接口定义** (`IStockFinanceService`):
  ```java
  @Transactional
  @Override
  long updateBalance(long accountId, long adjustBalance);
  ```

- **服务实现** (`StockFinanceServiceImpl`):
  ```java
  @Transactional(rollbackFor = Exception.class)
  @Override
  public long updateBalance(long accountId, long adjustBalance) throws ComponentException {
      // 1. 根据账号ID，获取账号的信息
      TradeAccount tradeAccount = tradeAccountDao.getById(accountId);
      if (null == tradeAccount) {
          throw new ComponentException(ApplicationErrorEnum.ACCOUNT_NOT_FOUND);
      }
      // 2. 检查账户的可用资金
      long balance = tradeAccount.getBalance() == null ? 0 : tradeAccount.getBalance();
      // 3. 调整可用资金
      balance += adjustBalance;
      // 4. 如果可用资金不足，抛出错误提示信息
      if (balance < 0) {
          throw new ComponentException(ApplicationErrorEnum.BALANCE_NOT_ENOUGH);
      }
      // 5. 更新账户的资金信息
      tradeAccountDao.updateBalanceById(accountId, balance);
      log.info("update balance, accountId: {}, adjustBalance: {}", accountId, adjustBalance);
      return balance;
  }
  ```

- **计算账户总览信息** (`calcAccountSummary`):
  ```java
  @Override
  public AccountOverviewVo calcAccountSummary(long accountId) throws ComponentException {
      AccountOverviewVo accountView = new AccountOverviewVo();
      long positionProfits = 0;
      long dayProfits = 0;
      long totalMarketAmount = 0;
      long totalAssets = 0;
      // 获取交易记录
      List<TradeDeal> dealList = tradeDealDao.getTradeDealByAccountIdAndTime(accountId, DateUtil.getToday());
      // 计算总市值
      for (TradeDeal deal : dealList) {
          totalMarketAmount += deal.getMarketAmount();
      }
      // 计算总资产
      totalAssets = totalMarketAmount + balance;
      accountView.setTotalMarketAmount(totalMarketAmount);
      accountView.setTotalAssets(totalAssets);
      return accountView;
  }
  ```

#### 公式

- **当日收益计算公式**：
  $$
  \text{当日收益} = \sum (\text{当前仓位收益}) = \sum (\text{当日卖出数量} \times \text{最新价格} - \text{当日买入数量} \times \text{最新价格})
  $$

- **总市值计算公式**：
  $$
  \text{总市值} = \sum (\text{股票最新价} \times \text{持仓股数})
  $$

- **总资产计算公式**：
  $$
  \text{总资产} = \text{总市值} + \text{可用资金}
  $$

---

### 4) 关键场景与演示描述

- **场景一：接口定义与实现** (00:16 - 00:45)
  - 讲师首先在 `GrpcStockFinanceService` 中定义了 `updateAccountBalance` 方法，该方法接收一个请求对象和一个响应观察者。
  - 接着，讲师切换到 `StockFinanceServiceImpl` 类，展示如何实现 `updateBalance` 方法。

- **场景二：事务与异常处理** (00:46 - 01:45)
  - 讲师在 `updateBalance` 方法中添加了 `@Transactional(rollbackFor = Exception.class)` 注解，确保事务在发生异常时回滚。
  - 讲师演示了如何根据账户 ID 获取账户对象，并在账户不存在时抛出 `ACCOUNT_NOT_FOUND` 异常。
  - 讲师演示了如何检查账户的可用资金，并在资金不足时抛出 `BALANCE_NOT_ENOUGH` 异常。

- **场景三：日志与数据库更新** (01:46 - 02:00)
  - 讲师演示了如何使用 `tradeAccountDao.updateBalanceById` 方法更新数据库中的账户余额。
  - 讲师添加了日志记录，记录更新操作的详细信息。

- **场景四：账户总览计算** (02:16 - 02:30)
  - 讲师展示了 `calc
