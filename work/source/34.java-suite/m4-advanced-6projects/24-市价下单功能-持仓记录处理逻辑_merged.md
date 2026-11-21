# 24-市价下单功能-持仓记录处理逻辑 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们去实现持仓记录的生成处理

首先咱们看一下整体的实现思路

这里是先判断订单的买卖方向

如果是买方向的

接着还去判断仓位信息是否存在

不存在则新增持仓

存在的话呢

就要做仓位的合并处理

仓位合并处理

最主要要去计算更新它的成本价

以及它的成交均价

接下来如果是卖方向的

同样也要先去判断它的仓位记录是否存在

如果是不存在呢

说明这个业务逻辑处理是存在异常的

你要卖股票

那么必须要有持仓记录

所以在这里咱们会抛出一个异常提示信息

接下来还要去判断它的可卖数量

如果不充足

同样也要抛出异常提示

最后

逻辑校验通过之后

就是对仓位进行合并处理

卖方向的仓位合并也是一样的

要去更新它的成本价

还有更新它的成交均价

好

这个呢就是整理的实现思路

那咱们回到代码当中

做对应实现

首先创建对应的方法

我们添加对应的注射

这个呢是要去生成

并更新

持仓记录信息

这里面的更新并非数据库的保存

而是将仓位所涉及到的成本价

还有它的成交均价做对应的计算更新

生成完持仓记录之后

后面再做数据的保存

好

我们来实现它的具体代码

首先第一步

根据交易账号ID和股票产品ID

获取持仓记录

定义Chad Position

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

Chad Position.io

获取股票产品ID

找到对应持仓记录之后

我们就要做对应的判断

首先根据买卖方向

Direction

如果是买方向的

我们来实现对应的买方向的处理逻辑

那么首先判断持仓记录是否存在

如果是不存在呢

在这里就要去创建持仓记录

组装仓位信息

属性的组装

咱们就从讲习当中直接copy进来

这里就是要组装仓位的必要属性

将这些信息填充进去

这里要注意一下

我们默认采用股票的CFD合约形式

合约模式

它是可以支持T加0的交易

T加0的意思是当天买入可以当天卖出

所以在这里它的可卖数量

我们可以直接将成交的数量设置进去

这个是作为模拟盘

当然如果是实盘交易

比如说是接入了深交所上交所

那么咱们国内的A股交易制度

是采用T加1的模式

也就是当天买入第二天才能卖出

那么在这里它的可卖数量

就不能将当前的成交数量加入进去

这一点大家要注意一下

接着咱们再处理下面的逻辑

这里是仓位的合并更新处理

首先要去更新它的成本价

成本价的更新公式

咱们从展示当中来看一下

它其实就是总的成交金额

再除以总的成交数量

这公式咱们扣比进来

总的成交金额怎么去计算呢

它是拿到持仓的成本价

再乘以持仓的数量

本次的成交均价

以及本次的成交数量

也就是说你拿到原来的持仓总金额

再加上你本次成交的总金额

这样就得出来一个总的成交金额

再去除以总的成交数量

总的成交数量

也就是将当前的持仓数量

再加上本次的成交数量

我们先定一个原始持仓的总金额

这一部分并不包含

当前订单的成交总金额

将持仓均价获取出来

还有持仓的数量

将持仓均价和持仓数量相乘

就是持仓的总金额

然后我们还去计算

本次订单的成交总金额

接着我们就去计算

就可以计算它的成本均价

long

cost price

mass utils

UILong

这个要做长者型运算

UILong这里是将总的成交金额

再除以总的成交数量

总的成交金额

就是原始的持仓金额

再加上本次订单的成交金额

这里面要做一个相加

mass utils

add yqi command

cur command

然后它要去除以总的成交数量

总的成交数量呢

就是持仓数量

再加上本次成交数量

mass utils

add

get position

get volume

get deal

再获取本次的成交数量

cuse volume

就计算了它的成本均价

将成本均价设置进去

z cost price

然后要去更新成交均价

成交均价的计算更新公式

它是由上一次成交均价

加上本次成交均价

然后除以2

万里成交多少次

它都是由上一次成交均价

再加上本次成交均价

然后再除以2

进去成交均价

就计算得出的set average price

mass utils

dial

拿到上一次的成交均价

average price

再加上本次的成交均价

xcuse price

再除以2

接下来就要设置它的

持仓数量

set volume

get position

get volume

share deal

get excuse volume

get excuse volume

最后再设置它的可卖数量

set value

sale volume

再加上本次的成交数量

好这一块呢

就是买方向的仓位处理逻辑

接着的话呢

就是卖方向的仓位处理逻辑

这一块处理逻辑和上面的买方向处理逻辑比较类似

那我们就不再独一去敲写代码

直接从讲习当中copy

将卖方向的持仓处理逻辑copy进来

先将错误处理一下

最上面他们要抛出compend exception

最后呢

咱们还要返回持仓记录对象

return

觉得不值

我们来看一下卖方向的持仓处理逻辑是如何实现的

首先做校验和判断

如果仓位有一空

抛出异常提示

可卖数量如果不足

创出对应的异常提示

接着的话呢

就是仓位的合并处理

和咱们买方向处理的逻辑也基本上是一致

要去更新成本价

接着话呢

要去更新他的成交均价

那么不同的是呢

他的成本价更新的方式会有些不一样

上面买方向的呢

他是一个累加

然后进行一个更新处理

那么卖方向的就要减去当前的成交总金额

然后再除以剩余的

持仓数量

这样呢

就能计算他的持仓成本价

这里咱们要注意一下

如果是足够多的盈利

他的成本均价呢

是可以为负数的

比如说你之前买了一只股票

他当时的价格呢

是10块钱

你买了1000手

过了一段时间

这只股票呢

他上涨至50元

其中的话

你赚了多少

每一手价差的话呢

就赚了40元

那么1000手就赚了4万

对不对

每一手又等于100股

那么总共的话呢

就盈利了400万

这个是盈利金额

那么你在50块钱的时候

将所有股票全部抛出

就剩一手

当时的话呢

成本价是10元

而现在呢

是涨到了50元

你的盈利呢

是400万

那么这个时候

你说成本价还是10元吗

如果这个时候成本价还是10元

那么以当前最新的价格50元

减去10元

价差是40元

一手再乘以40元

是无法得出400万的

对不对

所以这个成本价

他就会变为负数

通过负数才能和你的盈利持平

好

这个呢

就是成本均价可能为负数的原因

那下面的

成交均价的计算逻辑

和买方向的计算逻辑呢

都是一致的

好

在这里呢

咱们就实现了

持仓记录的生成处理逻辑

大家要理解整体的处理流程

它的业务规则

相关公司的计算

如果代码要更为优雅一些

可以再进一步对各层逻辑

再做一层封装

比如说咱们在这里

可以针对于卖方向

再做一层方法的封装

买方向呢

也做一层方法的封装处理

这样呢

整个方法逻辑看起来呢

就更为直观简洁

好

这一讲内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“生成持仓记录”功能的代码实现讲解。讲师通过在 IntelliJ IDEA 开发环境中，逐步演示 `StockDealServiceImpl` 类中的 `generatePosition` 方法。该方法的核心逻辑是根据一笔交易（`TradeDeal`）和用户账户（`TradeAccount`）信息，生成或更新用户的持仓记录（`TradePosition`）。演示重点在于处理“买入”和“卖出”两种交易方向下的持仓更新逻辑，特别是如何计算持仓成本价（`costPrice`）和平均成交价（`avgPrice`），并处理了持仓不足的异常情况。整个过程展示了如何在服务层进行业务逻辑的封装和异常处理。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频中的时间戳，以下时间点是根据画面内容和逻辑顺序进行的合理推断：

*   **0:00 - 0:05**: 视频开头，展示课程大纲，定位到“4. 生成持仓记录”章节。
*   **0:05 - 0:15**: 展示 `generatePosition` 方法的签名和注释，介绍方法的输入参数（`TradeDeal`, `PlaceOrderRequest`, `TradeAccount`, `TradeStock`）和返回值。
*   **0:15 - 0:30**: 讲解方法的第一部分逻辑：根据交易ID和股票ID查询或创建持仓记录。
*   **0:30 - 0:45**: 进入 `if` 分支，处理“买入”方向的持仓更新逻辑。
*   **0:45 - 1:00**: 详细讲解买入时成本价的计算公式：`costPrice = (上一次成本价 * 持仓数量 + 本次成交价 * 本次成交数量) / (持仓数量 + 本次成交数量)`。
*   **1:00 - 1:15**: 讲解买入时平均成交价的计算公式：`avgPrice = (上一次平均价 * 持仓数量 + 本次成交价 * 本次成交数量) / (持仓数量 + 本次成交数量)`。
*   **1:15 - 1:30**: 讲解买入时有效卖出量（`validSellVolume`）的更新逻辑。
*   **1:30 - 1:45**: 进入 `else` 分支，处理“卖出”方向的持仓更新逻辑。
*   **1:45 - 2:00**: 讲解卖出时成本价和平均价的更新逻辑。
*   **2:00 - 2:15**: 讲解卖出时有效卖出量的更新逻辑。
*   **2:15 - 2:30**: 讲解在“卖出”方向下，如果持仓记录不存在（`null`），则抛出 `ComponentException` 异常，提示“无持仓数据”。
*   **2:30 - 2:45**: 讲解在“卖出”方向下，如果有效卖出量不足以满足本次卖出（`validSellVolume < execVolume`），则抛出 `ComponentException` 异常，提示“持仓不足”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲中明确列出了“4. 生成持仓记录”。
    *   在代码注释中，有对方法功能的说明：“生成/更新持仓记录”。

*   **代码关键内容**:
    *   **方法签名**:
        ```java
        private TradePosition generatePosition(TradeDeal tradeDeal, PlaceOrderRequest request, TradeAccount tradeAccount, TradeStock tradeStock) throws ComponentException
        ```
    *   **买入方向逻辑**:
        ```java
        // 更新成本价
        Long costPrice = MathUtils.divLong(MathUtils.add(origAmount, curAmount), MathUtils.add(tradePosition.getVolume(), tradeDeal.getExecVolume()));
        // 更新平均价
        tradePosition.setAvgPrice(MathUtils.divLong(total, tradePosition.getVolume() + tradeDeal.getExecVolume()));
        // 更新有效卖出量
        tradePosition.setValidSellVolume(tradePosition.getValidSellVolume() + tradeDeal.getExecVolume());
        ```
    *   **卖出方向逻辑**:
        ```java
        // 更新成本价和平均价
        tradePosition.setCostPrice(costPrice);
        tradePosition.setAvgPrice(MathUtils.divLong(total, tradePosition.getVolume() + tradeDeal.getExecVolume()));
        // 更新有效卖出量
        tradePosition.setValidSellVolume(tradePosition.getValidSellVolume() + tradeDeal.getExecVolume());
        ```
    *   **异常处理**:
        ```java
        if (null == tradePosition) {
            throw new ComponentException(ApplicationErrorCodeEnum.NO_STOCK_POSITION_DATA);
        }
        if (tradePosition.getValidSellVolume() < request.getExecVolume()) {
            throw new ComponentException(ApplicationErrorCodeEnum.NO_ENOUGH_POSITION_VOLUME);
        }
        ```

*   **公式**:
    *   **买入成本价公式**:
        $$
        \text{costPrice} = \frac{\text{上一次成本价} \times \text{持仓数量} + \text{本次成交价} \times \text{本次成交数量}}{\text{持仓数量} + \text{本次成交数量}}
        $$
    *   **买入平均价公式**:
        $$
        \text{avgPrice} = \frac{\text{上一次平均价} \times \text{持仓数量} + \text{本次成交价} \times \text{本次成交数量}}{\text{持仓数量} + \text{本次成交数量}}
        $$
    *   **卖出成本价和平均价公式**:
        $$
        \text{costPrice} = \frac{\text{上一次成本价} \times \text{持仓数量} + \text{本次成交价} \times \text{本次成交数量}}{\text{持仓数量} + \text{本次成交数量}}
        $$
        $$
        \text{avgPrice} = \frac{\text{上一次平均价} \times \text{持仓数量} + \text{本次成交价} \times \text{本次成交数量}}{\text{持仓数量} + \text{本次成交数量}}
        $$

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与参数说明 (0:05-0:15)**
    *   讲师在 IDE 中定位到 `StockDealServiceImpl` 类中的 `generatePosition` 方法。
    *   通过鼠标悬停和注释，向观众解释该方法的作用是“生成/更新持仓记录”，并列出其四个参数：交易对象、订单请求、账户对象和股票对象。

*   **场景二：买入方向逻辑演示 (0:30-1:30)**
    *   讲师将光标移动到 `if (request.getDirection() == GlobalConstants.ORDER_DIRECTION_BUY)` 分支。
    *   通过逐步滚动和高亮，演示了如何计算 `costPrice` 和 `avgPrice`。
    *   讲师特别强调了 `MathUtils.divLong` 和 `MathUtils.add` 等自定义工具类方法的使用，以处理大数运算和避免精度丢失。
    *   讲师还演示了如何更新 `validSellVolume` 字段。

*   **场景三：卖出方向逻辑演示 (1:30-2:30)**
    *   讲师将光标移动到 `else` 分支，开始演示卖出方向的逻辑。
    *   讲师展示了如何更新 `costPrice` 和 `avgPrice`，并强调了与买入方向计算逻辑的相似性。
    *   讲师演示了如何更新 `validSellVolume`。
    *   讲师特别强调了在卖出方向下，需要对持仓记录进行校验，如果不存在则抛出异常。

*   **场景四：异常处理演示 (2:15-2:45)**
    *   讲师在 `else` 分支内，展示了两个关键的 `if` 判断语句。
    *   第一个 `if` 判断：如果 `tradePosition` 为 `null`，则抛出 `ComponentException`，错误码为 `NO_STOCK_POSITION_DATA`。
    *   第二个 `if` 判断：如果 `validSellVolume` 小于 `execVolume`，则抛出 `ComponentException`，错误码为 `NO_ENOUGH_POSITION_VOLUME`。
    *   讲师通过高亮和注释，向观众解释了这些异常的业务含义：持仓数据不存在或持仓不足。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
