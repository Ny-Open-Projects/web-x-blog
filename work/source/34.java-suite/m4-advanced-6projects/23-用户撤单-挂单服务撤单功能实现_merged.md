# 23-用户撤单-挂单服务撤单功能实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现测单接口的核心处理逻辑

之前咱们对整体实现流程做了一个梳理

并且对外层的代码做了一个简单实现

那接着咱们就来实现第二个步骤

获取挂单符对应的缓存对列消息

在这里呢,要定义挂单缓存对列的器质

Key Key

Global Consistence

Stock, Pending, Limit Order

再加上Support的关口

接下来获取Cache的缓存对象

通过Cache Manager

传递Cache Key

接着咱们对缓存做一个围攻判断

如果挂单对列这个缓存数据不存在

那么咱们要抛出异常

如果挂单缓存对列数据不存在

有可能是订单已处理

或者是根本没有接受到对应的挂单

那咱们要抛出异常提示信息

Sloot

New Compend Exception

给它一个异常错误码

错误提示叫Order as Process

说明订单呢是已经做了对应的处理

接下来我们就要根据股票的ID去获取

委托挂单信息的缓存超速对应

好

我们先把对象拿取Cache里面的Value by Chapter

定义stockCache

通过Cache对象拿取缓存的值

接stockID

咱们拿到缓存值的操作对象之后

要做一个围攻判断

stockCache

并且stockCache它的值不能围攻

我们将下面的处理步骤移植进去

接下来我们要去获取委托挂单的列表信息

List

Limit

Place Order

Request Viewer

Viewer List

做一个强转

Cache Get

接着的话呢我们就要去便利挂单的列表信息

然后做匹配处理

如果是匹配成功对链发生了变更

咱们要去更新缓存信息

所以在这里咱们还需要去定义一个标记

标识缓存对链是否已经修改

接下来进行循环迭代

Iterator Request Viewer

ITR要等于Place Order Request Viewer List

Add Next

在循环内部咱们就要去根据账户ID和订单ID

去匹配对应的挂单信息

匹配成功之后就要进行相应的信息清除

首先咱们要拿到迭代的对象

Place Order Request Viewer List

Place Order ITR.Next

然后做一个判断比较

Place Order.Get Order ID

Equals Request.Get Order ID

这个是订单比较

接下来的话呢

就要去比较账户ID

Get Account ID

Equals Request.Get Account ID

这里必须要加上交易账户的ID

否则的话你随便传入一个订单ID

不能把别人的信息进行撤回操作

这一点要将它控制好

判断成功之后

咱们就将信息进行清除

修改标记

自为True Break

接下来我们就要去判断

刮弹兑电是否发生了变更

变更之后要进行返存的更新

If Is Modified

Page 进行更新操作

Request.Get Start ID

将刮弹兑电更新进去

最后咱们要去对数据库里面的订单信息做撤回处理

这个逻辑放在外面

咱们通过service神接口做对应的处理

Record 定义一个新的方法

Record 传递Request的参数对象

接着咱们来实现这个方法

Edit 加 Enter 键

创建Method

给方法添加对应的注释

这个是刮弹数据撤回的处理接口

让咱们去service做一个实现

打开它的实现内

在最下面咱们就去实现了

咱们添加对应的方法

添加OLED的图简

首先第一步要根据订单ID

获取订单信息

定义CAD ORDER对象

通过Service神接口

根据ID

查找对应的对象

还递订单ID参数

下面咱们做个围空判断

如果order围空

数据库找不到对应的数据

咱们要返回抛出一场

Sloot

New Compound Exception

传递一个错误码Application

Add Code

提示订单没有找到

再翻往上面

旁边要抛出一场信息

Compound Exception

在接口内上面

也增加对应的处理

再回到刚才的业务实现层

订单找到之后

咱们还做一个判断

判断这里面的交易账户ID

是否和咱们传递的交易账户ID一致的

如果不一致

说明它不具备该订单的撤回权限

那么在这里

咱们也要抛出一个异常提示

不一致

抛出一场

Sloot

New Compound Exception

Application

Add Code

给它一个错误码

和交易账户为匹配

接下来咱们还对订单状态做判断处理

对订单状态做判断处理

如果是等待成交

或者是部分成交的状态

咱们才允许它进行撤回

如果订单已经完全成交了

这个时候是不允许撤回的

这一点大家要注意一下

过去订单的状态

做一个比较

Order Stays

这个是订单的待成交

或者订单的部分成交状态

Order Stays

Data

这个长辆代表是部分成交

符合条件之后

咱们才允许对数据进行撤回

符合判断条件

才可以撤回

通过数据层接口

CAD ORDER DO

去修改订单的状态

传递订单ID

CAD ORDER ID

传递修改的订单状态

这里就要改成手动测单的状态

我们可以看到这个长辆

它代表的意思是手动测单

系统测单是在系统结算的时候

进行自动测单

这两者是有区别的

这个是符合条件的处理逻辑

那么它不符合条件的话呢

咱们也要抛出对应的提示异常

else

订单已经完全成交

不允许撤回

srew

new

compand exception

传递异常错误码

order

motor recall

这个就是设备层

对挂单撤回处理的操作

回到刚才的GRPC的调用实现层

在这里呢

就已经完成了整个用户测单接口的处理逻辑

这里呢

主要是做了两部分事情

一部分的话呢

是撤回数据库的订单信息

另外一部分呢

要去更新挂单对电的缓存信息

在这里呢

咱们就实现了挂单服务

对测单功能的处理

这些处理步骤大家要注意一下

测单功能对缓存对电数据

它会做对应的修改

所以需要去加索出来的功能

来处理

这里采用的是和挂单处和交易一样的对象锁

都是基于Store ID

股票产品ID

进行加锁处理

在下面呢

业务层的实现逻辑

大家要注意一下

这里面呢

要去根据账户ID做对应匹配

账户ID匹配的情况下面

才允许去修改订单的状态

权限控制千万不能错乱

整体逻辑的处理顺序

咱们也要注意一下

这里我们是先处理缓存

再对数据库当中的数据做处理

如果是出现缓存处理成功

但数据库处理出现异常

为了保持一致性

只要数据库恢复正常

仍然可调用成功

如果你是先操作数据库

在这里呢

重复去操作

条件校验是不能通过

会抛出对应的提示异常

所以呢

咱们在这里是

先处理缓存

数据库操作失败

只要下次再发起调用

仍然是可以调用成功的

所以逻辑上的实现和调用顺序

这些浓错的方面

要考虑清楚

好

这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于“股票挂单撤销”功能实现的技术课程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `GrpcStockPendingService` 服务中实现一个 `recallOrder` 方法。该方法的核心逻辑是：首先，通过缓存（`PendingQuoteConsumer`）获取与股票ID关联的挂单列表；然后，遍历该列表，根据请求中的账户ID和订单ID进行匹配，若匹配成功则将订单状态更新为“手动撤销”；最后，将更新后的订单信息写回数据库，并将处理结果返回给客户端。整个过程涉及缓存操作、数据库操作、异常处理和状态判断，体现了典型的分布式系统中订单状态管理的实现方式。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 开场，展示项目结构和当前文件 `GrpcStockPendingService.java`。
*   **00:00:05 - 00:00:15**: 讲师定位到 `recallOrder` 方法，并开始讲解其核心逻辑：获取缓存中的挂单列表。
*   **00:00:15 - 00:00:30**: 讲师在代码中添加注释，说明需要获取缓存对象，并展示如何通过 `PendingQuoteConsumer.getStockId()` 获取缓存。
*   **00:00:30 - 00:00:45**: 讲师开始遍历挂单列表，展示 `for (Iterator<LimitPlaceOrderRequestVo> itr = _placeOrderRequestList; itr.hasNext(); )` 的循环结构。
*   **00:00:45 - 00:01:00**: 讲师在循环体内编写匹配逻辑，展示 `if(placeOrder.getOrderId().equals(request.getOrderId()) && placeOrder.getAccountId().equals(request.getAccountId()))` 的条件判断。
*   **00:01:00 - 00:01:15**: 讲师展示如何在匹配成功后，将订单状态更新为“手动撤销”，并更新缓存。
*   **00:01:15 - 00:01:30**: 讲师展示如何将更新后的订单信息写回数据库，调用 `tradeOrderDao.updateOrderStatusById(...)`。
*   **00:01:30 - 00:01:45**: 讲师展示如何在处理完成后，将结果封装为 `RecallOrderResponse` 并返回。
*   **00:01:45 - 00:02:00**: 讲师切换到 `StockTradePendingServiceImpl.java` 文件，展示 `recallOrder` 方法的实现。
*   **00:02:00 - 00:02:15**: 讲师在 `StockTradePendingServiceImpl` 中展示如何根据订单ID获取订单信息，并进行状态判断。
*   **00:02:15 - 00:02:30**: 讲师展示如何根据订单状态判断是否允许撤销，并调用 `tradeOrderDao.updateOrderStatusById(...)` 更新状态。
*   **00:02:30 - 00:02:45**: 讲师展示如何在状态判断后，将结果封装并返回。
*   **00:02:45 - 00:03:00**: 讲师切换到 `Day15.md` 文档，展示该功能的文档化描述。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **缓存获取**:
        ```java
        synchronized (PendingQuoteConsumer.getStockId()) {
            // 获取缓存对象
            Cache.ValueWrapper stockCache = cache.get(request.getStockId());
            if (null != stockCache && null != stockCache.get()) {
                // 获取挂单列表
                List<LimitPlaceOrderRequestVo> placeOrderRequestList = (List<LimitPlaceOrderRequestVo>) stockCache.get();
                boolean isModify = false;
                for (Iterator<LimitPlaceOrderRequestVo> itr = _placeOrderRequestList; itr.hasNext(); ) {
                    LimitPlaceOrderRequestVo placeOrder = itr.next();
                    if (placeOrder.getOrderId().equals(request.getOrderId()) && placeOrder.getAccountId().equals(request.getAccountId())) {
                        // 匹配成功，更新状态
                        tradeOrderDao.updateOrderStatusById(request.getOrderId(), GlobalConstants.ORDER_STATUS_MANUAL_CANCEL);
                        isModify = true;
                    }
                }
                if (isModify) {
                    cache.put(request.getStockId(), placeOrderRequestList);
                }
            }
        }
        ```
    *   **数据库操作**:
        ```java
        public void recallOrder(RecallOrderRequest request) throws ComponentException {
            TradeOrder order = tradeOrderDao.getById(request.getOrderId());
            if (null == order) {
                throw new ComponentException(ApplicationErrorCodeEnum.ORDER_NOT_FOUND);
            }
            if (!order.getAccountId().equals(request.getAccountId())) {
                throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_NOT_MATCH);
            }
            if (order.getStatus() == GlobalConstants.ORDER_STATUS_WAIT || order.getStatus() == GlobalConstants.ORDER_STATUS_PART) {
                tradeOrderDao.updateOrderStatusById(request.getOrderId(), GlobalConstants.ORDER_STATUS_MANUAL_CANCEL);
            } else {
                throw new ComponentException(ApplicationErrorCodeEnum.ORDER_STATUS_NOT_ALLOW);
            }
        }
        ```
    *   **状态常量**:
        ```java
        ORDER_STATUS_WAIT = 0
        ORDER_STATUS_PART = 1
        ORDER_STATUS_MANUAL_CANCEL = 2
        ```

*   **关键 PPT 内容**:
    *   **文档结构**:
        ```
        3.4 功能验证
        1. 模拟一次性成交的挂单请求
        2. 模拟多次撮合的挂单请求
        4. 总结
        第3章 用户撤单功能实现
        1. 目标
        2. 步骤
        3. 实现
        3.1 定义接口数据结构
        3.2 挂单服务撤单功能实现
        3.3 代理服务撤单调用实现
        3.4 功能验证
        4. 总结
        ```

---

### 4) 关键场景与演示描述

*   **场景一：缓存操作演示 (00:00:05 - 00:00:30)**
    *   讲师在 `GrpcStockPendingService.java` 文件中，定位到 `recallOrder` 方法。
    *   讲师通过注释和代码演示如何获取缓存对象 `stockCache`，并检查其有效性。
    *   讲师展示了如何将缓存中的挂单列表赋值给 `placeOrderRequestList` 变量。

*   **场景二：遍历与匹配逻辑演示 (00:00:30 - 00:01:15)**
    *   讲师使用 `for` 循环遍历 `placeOrderRequestList`。
    *   讲师在循环体内编写了 `if` 条件判断，用于匹配请求中的订单ID和账户ID。
    *   讲师演示了如何在匹配成功后，调用 `tradeOrderDao.updateOrderStatusById(...)` 更新订单状态。

*   **场景三：状态判断与异常处理 (00:01:15 - 00:02:30)**
    *   讲师在 `StockTradePendingServiceImpl.java` 文件中，展示了如何根据订单状态判断是否允许撤销。
    *   讲师演示了如何在订单状态为 `ORDER_STATUS_WAIT` 或 `ORDER_STATUS_PART` 时，调用 `updateOrderStatusById` 方法。
    *   讲师展示了如何在状态不匹配时，抛出 `ComponentException` 异常。

*   **场景四：结果返回与文档化 (00:02:30 - 00:03:00)**
    *   讲师在 `GrpcStockPendingService.java` 文件中，展示了如何将处理结果封装为 `RecallOrderResponse`。
    *   讲师切换到 `Day15.md` 文档，展示了该功能的文档化描述，包括目标、步骤和实现细节。
