# 23-市价下单功能-成交记录处理逻辑 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着去实现成交记录的业务逻辑处理

在做代码实现之前

咱们先了解一下整个的实现思路

回到讲义当中

前面我们学习过深度成交的原理

那么各报价层级该如何去匹配

大家都知道买方和卖方有不同的档位

从买1至买5

卖方有卖1至卖5

这个匹配逻辑该怎么去处理

如果一个订单是实现了多个档位的成交

也就是深度成交

那么它的最终均价该如何去计算

买卖方向我们又该怎么去处理

涉及的业务处理逻辑点比较多

咱们怎么去实现更为高效

而且维护起来也更为优雅

好,那咱们就来看一下

具体的实现方法

实现实录

首先咱们根据买卖方向

将各档位的报价转换为有序的MAP集合

我们可以画下整个图形

在外围我们先定义两个MAP

一个是买方向的

一个是卖方向的

另外一个是卖方向的

这两个MAP我们按照有序的方式

去存储盘口信息

在这里呢

比如说我们存储了买方向的

买1至买5

买5的五个盘口

卖方向的也存储了五个盘口档位信息

这里是卖1

然后到卖5

这里呢是买1

然后是买5

MAP里面存储的结构是价位和数量

Key是价格

Value是成交量

也就是数量

卖方向的也是一样

这里Key是价格

Value是数量

有了这两个MAP之后

我们就可以进行撮合的匹配

因为这两个是有序的MAP

按先后顺序进行存储

第一条记录是买1的报销信息

那么对应卖方的MAP集合

第一条记录是卖1的信息

那我们回到讲义当中

再看一下下面的处理逻辑

有了MAP数据之后

咱们就要去遍历MAP集合

这里呢又分为两种情况

一种呢是当前档位能够满足请求条件

也就是在这里

如果买方发起了下单信息

比如在10块钱的价格下面下了100手

那么卖方卖1的档位

他完全能够满足

卖1在这里挂了1000手

那么这个订单呢

只需要去撮合一个档位就可以

并不会涉及到下面的档位

也不会触发深度成交

这个是第一种情况

直接一个档位能够满足请求条件

另外一种是当前档位不能够满足请求条件

咱们可以再回到刚才的流程图

如果卖1这个档位不能够满足

他就会找卖2第二个档位

由此类推

完成整个订单的撮合处理

这样就能实现深度成交

咱们再回到讲义当中

按照深度成交的撮合处理机制

后面无论是扩展了多少个档位报价

这里面的核心处理逻辑都不用再去做任何调整

咱们可以回到流程图

如果后面有10个档位或者是上百个档位

按照深度成交的机制

咱们是不需要再去调整整个的处理逻辑

以及整个map的存储结构

这就是咱们为什么要采用这种方式去做处理逻辑的逻辑

最主要的是要理解整个的处理流程

好

回到讲义当中

接下来呢

我们要去理解相关的计算公式

比如说均价的计算

均价计算按照业务规则来处理

它是由所有档位的价格和数量相乘之后

然后计算它的总和

接着再去除以所有档位的成交数量

这样呢

就能够处理整个的处理流程

得出来它一个均价

简单一点就是总价去除以总的成交数量

下面还会涉及到账户组的佣金的计算

最后呢就去组装成交记录

这样就完成了成交记录的处理逻辑

好

那咱们回到代码当中来做具体实现

创建一个新的方法

Generate

Chaddle

添加对应的注释

这个方法呢

这个方法是生成成交记录

首先第一步要去转换报价的深度

组装为有序的MAP集合

定义MAP结构

Long

Long

这里面的价格是长整形

成交数量呢也是一个长整形

通过Carven的DealOffers这个方法

去做对应的转换

传递Quadrast

还有你的买卖方向

咱们来看一下这个方法逻辑的具体实现

我们来看一下这个方法逻辑的具体实现

在这里他会去判断订单的买卖方向

如果是买方向的

那他就要和卖方的信息做撮合匹配

所以MAP存储的就是他相反的方向

卖1至卖5的价格信息

那如果是卖方向的

在这里他要相反的去存储买1至买5的喊口信息

好再继续刚才的处理逻辑

下面的话呢

我们要去记录成交总价

第一

定义amount的属性

下面记录成交总数

定义volume

咱们还要去记录一个剩余成交数量

在深入成交的时候呢

需要使用到

他初始化的词呢

就是请求数量

是剩余所需要成交的数量

接下来咱们就要去逐个档位便利

计算成交总价与总数

总的数量

做便利处理

将MAP存储的数量

和MAP的档位记录做一个便利

N2CED

然后我们要去判断

当前档位能否满足成交量

将你的volume和divoff里面的value进行比较

如果请求的数量小于等于当前档位所提供的数量

这个时候呢

一次性成交就可以了

不需要去进行深入成交

divoff

getkey

将你的volume呢

置为0

因为你通过这一个档位就已经完全成交

下面也不需要再便利

直接break

退出整个循环

接下来还要去判断

如果是当前档位

不能满足成交量

需要

这个时候就要去便利其他的档位

将当前档位的成交量

当前档位信息做一个处理

getvalue

然后我们要去累加计算成交总价

还有成交总数

amount

divoff

getkey

将价格和数量相乘

volume

直接累加它的数量

divoff

getvalue

好

撮合匹配完成之后

最后我们就要去生成成交系统信息

这块逻辑就比较简单

咱们从讲义当中直接copy进来

将这段代码copy进来

做相应的修正

这里面是integer

咱们做一个转换

让点value of

先转成长整形

然后再叫用intervalue方法

转换为整形

这个data咱们导入进来

这里就是组装成交记录的一些必要信息

像股票产品信息

还有货币信息

还有我们上面所计算的成交基础信息

接着就要去计算它的佣金比例

佣金的设置咱们是放在交易账户组当中

所以在这里先要查取到交易账户组信息

然后通过数学运算方法

计算实际的佣金值

咱们可以点进去这个方法

这里是保留4位金路

转换为长整形做对应的计算处理

最后就是设置成交记录的状态

处理完成之后先不要着急保存

因为后面还要去记录定量ID

仓位ID等信息

所以我们只要将成交记录信息组装好

返回出去就可以

好

这一讲就是对成交记录生成的处理实现

这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段来自一个关于股票交易系统开发的实战课程，主要聚焦于“市价单”（Market Order）的处理逻辑。讲师通过 IntelliJ IDEA 开发环境，逐步演示了在 `StockDealServiceImpl` 服务类中，如何实现一个完整的市价单处理流程。该流程包括：获取交易账户和股票产品信息、生成交易记录（`TradeDeal`）、生成持仓记录（`TradePosition`）、生成订单记录（`TradeOrder`）以及保存所有记录。核心难点在于如何根据市价单的请求量，在买卖报价簿（深度）中找到满足条件的最优报价，并计算成交金额和数量，同时处理账户佣金。视频通过代码逐行讲解，辅以注释和逻辑说明，旨在帮助学员理解复杂交易系统的内部实现。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:00**：课程开场，展示项目结构和 `processMarketOrder` 方法的主干逻辑，概述整个市价单处理流程。
*   **00:01:00 - 00:03:00**：深入讲解 `generateTradeDeal` 方法。首先，将报价簿（`TradeStockQuoteLast`）转换为有序的 `Map<Long, Long>` 结构（`deepOffers`），其中键为价格，值为数量。然后，遍历该 Map，按价格从高到低（买方）或从低到高（卖方）的顺序，逐个匹配请求量，计算成交金额和数量，并更新剩余未成交数量。
*   **00:03:00 - 00:05:00**：讲解 `generatePosition` 方法。根据交易记录（`TradeDeal`）和账户信息，生成或更新持仓记录（`TradePosition`），并计算佣金。
*   **00:05:00 - 00:07:00**：讲解 `saveTradeOrder` 方法。将生成的交易记录、持仓记录和订单记录保存到数据库。
*   **00:07:00 - 00:09:00**：总结市价单处理的完整流程，并强调关键点，如深度转换、逐档匹配、佣金计算等。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **`processMarketOrder` 方法 (主流程)**：
    ```java
    public TradeOrder processMarketOrder(PlaceOrderRequest request, TradeStockQuoteLast quoteLast) throws Exception {
        // 1. 获取交易账户信息
        TradeAccount tradeAccount = tradeAccountDao.getById(request.getAccountId());
        // 2. 获取股票产品信息
        TradeStock tradeStock = tradeStockDao.getById(request.getStockId());
        // 3. 生成成交记录
        TradeDeal tradeDeal = generateTradeDeal(quoteLast, request, tradeAccount, tradeStock);
        // 4. 生成持仓信息
        TradePosition tradePosition = generatePosition(tradeDeal, request, tradeAccount, tradeStock);
        // 5. 生成订单信息
        TradeOrder tradeOrder = saveTradeOrder(tradeDeal, request, tradeAccount, tradeStock);
        // 6. 保存持仓记录
        savePosition(tradePosition);
        // 7. 保存成交记录
        saveTradeDeal(tradeDeal);
        return tradeOrder;
    }
    ```

*   **`generateTradeDeal` 方法 (核心逻辑)**：
    ```java
    private TradeDeal generateTradeDeal(TradeStockQuoteLast quoteLast, PlaceOrderRequest request, TradeAccount tradeAccount, TradeStock tradeStock) {
        // 1. 转换报价的深度，组装为有序的MAP集合
        Map<Long, Long> deepOffers = cvtDeepOffer(quoteLast, request.getDirection());
        // 2. 记录成交总价
        long amount = 0;
        // 3. 记录成交总数
        long volume = 0;
        // 4. 记录剩余成交数量，初始化为请求数量
        long needVolume = request.getExecVolume();
        // 5. 逐个档位遍历，计算成交总价与总数量
        for (Map.Entry<Long, Long> deepOffer : deepOffers.entrySet()) {
            // 当前档位能否满足成交数量
            if (needVolume <= deepOffer.getValue()) {
                // 计算成交金额
                amount += needVolume * deepOffer.getKey();
                // 计算成交数量
                volume += needVolume;
                // 剩余未成交数量
                needVolume = 0;
                break;
            } else {
                // 不能满足，继续下一个档位
                amount += deepOffer.getKey() * deepOffer.getValue();
                volume += deepOffer.getValue();
                needVolume -= deepOffer.getValue();
            }
        }
        // 创建并填充 TradeDeal 对象
        TradeDeal deal = new TradeDeal();
        deal.setAccountId(request.getAccountId());
        deal.setAccountNo(tradeAccount.getAccountNo());
        deal.setStockCode(tradeStock.getCode());
        deal.setStockName(tradeStock.getName());
        deal.setStockMarket(tradeStock.getMarketNo());
        deal.setExecVolume(Long.valueOf(volume));
        deal.setExecPrice(MathUtils.divLong(amount, volume));
        deal.setExecTime(new Date());
        deal.setDirection(request.getDirection());
        // 获取账户组信息，计算佣金
        tradeGroup = tradeAccountDao.getTradeGroupByAccountId(request.getAccountId());
        deal.setCommission(MathUtils.calcCommission(amount, tradeGroup.getCommissionRate()));
        deal.setStatus(GlobalConstants.INT_ENABLED);
        return deal;
    }
    ```

#### **关键公式**

*   **成交金额计算**：
    该方法中，成交金额 `amount` 是通过累加每个档位的 `价格 * 数量` 得到的。在满足条件的档位，`amount += needVolume * deepOffer.getKey()`。
*   **成交数量计算**：
    成交数量 `volume` 是通过累加每个档位的 `数量` 得到的。在满足条件的档位，`volume += needVolume`。
*   **佣金计算**：
    佣金 `commission` 的计算公式为：`commission = amount * commissionRate`，其中 `commissionRate` 是账户组的佣金比例。

---

### 4) 关键场景与演示描述

*   **场景一：市价单处理流程总览 (00:00:00)**
    讲师首先展示了 `processMarketOrder` 方法的整体结构，通过注释清晰地划分了七个步骤，帮助学员建立宏观认知。

*   **场景二：深度转换与逐档匹配 (00:01:00)**
    讲师将 `TradeStockQuoteLast` 对象转换为 `Map<Long, Long>`，其中键为价格，值为数量。然后，通过 `for` 循环遍历该 Map，按价格顺序（买方从高到低，卖方从低到高）逐个检查当前档位是否能满足请求量。如果满足，则计算成交金额和数量，并跳出循环；否则，继续检查下一个档位。

*   **场景三：佣金计算与对象填充 (00:03:00)**
    讲师演示了如何根据交易记录 `TradeDeal` 和账户信息，生成 `TradePosition` 对象。同时，通过 `tradeAccountDao.getTradeGroupByAccountId` 获取账户组信息，并调用 `MathUtils.calcCommission` 方法计算佣金，最终设置到 `TradeDeal` 对象中。

*   **场景四：数据库保存 (00:05:00)**
    讲师展示了 `saveTradeOrder` 方法，将生成的 `TradeDeal`、`TradePosition` 和 `TradeOrder` 对象保存到数据库中，确保交易数据的持久化。

*   **场景五：代码调试与注释 (00:07:00)**
    讲师在代码中添加了详细的中文注释，解释了每个步骤的目的和逻辑，例如“记录成交总价”、“记录成交总数”、“逐个档位遍历”等，极大地提升了代码的可读性和教学效果。
