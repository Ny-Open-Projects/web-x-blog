# 11-仓位总览-持仓服务仓位总览实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始在持商服务里面去实现仓位的总览接口

首先咱们去创建GRBC的服务实现类

回到咱们工程当中

在position服务下面

GRBC的保下面咱们创建一个class

将名称扣底下OK

然后我们要继承GRBC的接口

extends

stock

position

serviceGRBC

employment base

增加对应的注解

GRBC service

加上日子插件

of project2

这里GRBC的整个调用流程

处理起来相对比较简单

那咱们就从讲义当中将代码扣比进来

这里替换

将相关的错误修正

导入对应的包

这个是GRBC下面的

导入完成之后

接着咱们要去实现

获取所有持仓数据的业务层逻辑

我们先看一下外层这一块是如何处理的

在这里它首先根据账户ID

去获取所有的持仓数据

通过position service

负责具体业务的实现

这里传递的是交易账户的ID

核心逻辑是在service层接口的处理

get all position

稍后咱们来看看

我们来做具体的实现

拿取到所有持仓数据之后

在这里会做一个便利

将获取的持仓对象转换成为PB的对象结构

然后输出给调用房

咱们可以看到这里构建了响应消息体

将转换后的对象加入进去

最后的话通过response of server对象

将数据输出给调用房

好

外层GRBC的结果是什么样的结果呢?

在这些结果处理逻辑讲解完成之后

接着咱们去实现service层的业务代码

首先咱们创建对应的接口

istock position service

接着再创建实现方

implement

创建它的实现类

stock position service implement

这里要去实现对应的接口

istock position service

这里呢

咱们将类型改成interface

再回到刚才的实现类

咱们先添加一个service的注解

接下来咱们去实现获取所有持仓数据的业务层接口

定义返回对象

get position

get all positions

传递account ID

添加注释

这个是获取所有用户的所有持仓数据的接口

下面是根据账户ID获取所有持仓数据信息

下面是根据账户ID获取所有持仓数据信息

咱们先将用到的主件录入进来

addis

gauge manager

autowide

这个是返送管理器

接下来咱们再注入数据层的接口

iTrader position

添加autowide注解

这个是持仓的数据层接口

这个是持仓的数据层接口

接下来呢

咱们就来做具体的业务实现

list

get position

position list

get all 还有account ID

查询完持仓数据之后

咱们做一个唯空判断

position list

建立集合的数据

for each

建立集合的数据呢是为了计算每条持仓的浮动盈亏

这里咱们通过一个封装的方法做对应的实现

传递持仓数据

建立完成之后

要返回持仓的数据对象

接着咱们对浮动盈亏的计算做一个实现

创建一个方法

添加注释

这个是

计算

仓位的

浮动盈亏

我们就来做个具体实现

第一步呢要获取到最新的行情报价

因为你根据最新的行情才能算出它当前是盈利还是亏损

所以我们先把这个行情报价

定义

set board last

最新行情的数据对象

咱们呢也通过一个方法去封装处理

set

stock board last

这里传递股票ID

stock ID

那咱们来实现这个接口

edit 加 enter

创建对应的方法

添加注释

这个是获取

股票

产品的

最新报价

咱们要从

反存对象里面

获取数据

定义一个catch对象

last price

catch

readies

catch manager

get catch

herb consistence

传递最新行情的

key值

last price key

然后拿到反存的value对象

order last

传递股票ID

定义最新的股票行情对象

咱们接着就来判断

反存的此对象是否尾空

如果不尾空

咱们就取出反存的数据信息

share

stock board last

将它做一个强转

最后呢咱们就返回最新的行情对象

board last

最新报价的

实现处理完成之后

接着咱们再回到浮动盈亏的计算处理

咱们拿到最新的

行情对象做一个微空判断

然后是浮动盈亏的计算

浮动盈亏相关的计算

这里咱们采用的是整形处理

精度是保持两位

采用

长整形

做计算

保留两位小数

那浮动盈亏是如何计算的

这里咱们列出一个公式

浮动盈亏等于最新价

减去成本价

然后再乘以持仓数量

注意这里有可能为负数

因为最新价可能会低于成本价

好那咱们做一个计算

计算他们的价差

mess utils

做一个减法

传递最新价

get last price

再传递持仓的成本价

get cost price

拿到价差之后

咱们再做一个浮盈计算

mess utils

这里呢就要做一个乘法

传递价差

然后传递数量

volume

这个是持仓的数量

计算完成之后

咱们将信息设置到持仓对象里面

set profit

再设置它的最新价

set last price

quad last

get last price

计算完后

再浮盈之后

还需要计算浮动盈亏的比例

这里仍然是采用长整形

保留四位小数

比如说169988

那么它实际代表的就是169%

然后点9988

保留了四位小数

转换为长整形

好让咱们在post里面去set

它的浮盈比例

做bit late

用过mess utils工具做对应的计算

外层做个除法

这里拿到它的浮动盈亏

然后去除以它的总价

最后再保留四位小数

这公式咱们写一下

计算公式

盈亏比例

等于浮动盈亏

再除以

成本价

再乘以它的持仓数量

注意是拿成本价不是最新价

这里呢就要拿成本价

再乘以它的持仓数量

好保留四位小数

这个呢就是持仓

浮动盈亏的计算处理逻辑

咱们将这个方法

抽取到接口层

右键

reflect

formal bus up

点击reflect

抽取完成之后咱们再回到GRPC的接口层

在这里

整个代码就没有包错

好那咱们再回到讲义当中

在这里要注意一下

为了防止客户端出现科学技术类型的问题

这里咱们采用的是长者型做计算处理

建议咱们在项目当中的所有的运算逻辑处理

都要采用长者型做计算

双进度它也能够实现

但是呢它会存在进度丢失的可能

通过这个方法去解决这个问题

这个例子我们就可以发现

双进度的计算

会存在科学计算的问题

这里呢是一个简单的运算

这个是乘法这个是除法

我们这里做了个截图

经过运算处理之后

这里的输出

显示的是科学技术类型

科学技术它只是显示的问题

并不是结果会有问题

咱们可以去采用格式化的方式做处理

但是在实际工作当中

对经常要做运算或存在复杂运算的业务

还是要尽量采用长者型做处理

保持整体计算的准确性

好这一讲就是对持仓服务

仓位总占接口的实现

那这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统中“持仓服务仓位总览”功能的实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何构建一个基于 gRPC 的远程服务接口，并实现其底层业务逻辑。核心内容包括：
- 定义 gRPC 服务接口 `GrpcStockPositionService`。
- 实现服务的业务逻辑层 `StockPositionServiceImpl`。
- 在服务层中，通过数据访问对象（DAO）获取持仓数据。
- 计算持仓的浮动盈亏，并将结果更新到实体对象中。
- 使用 Redis 缓存来获取最新的行情报价，以提高性能。
- 最后，讲师讨论了在金融系统中处理浮点数和长整型计算的精度问题，强调了使用 `BigDecimal` 和 `long` 类型的重要性。

整个过程体现了典型的分层架构（接口层、服务层、数据访问层）和现代 Java 开发中对性能和精度的考量。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:15**: 介绍本节内容，展示 gRPC 服务接口 `GrpcStockPositionService` 的定义。
- **00:15 - 00:30**: 展示服务实现类 `GrpcStockPositionService` 的代码结构，包括注入的 `RedisTemplate`、`CacheManager` 和 `IStockPositionService`。
- **00:30 - 00:45**: 跳转到服务实现类 `StockPositionServiceImpl`，展示其继承 `IStockPositionService`。
- **00:45 - 01:00**: 在 `StockPositionServiceImpl` 中，展示如何通过 `tradePositionDao` 获取持仓数据。
- **01:00 - 01:15**: 展示如何遍历持仓列表，并调用 `calcProfit` 方法计算浮动盈亏。
- **01:15 - 01:30**: 详细演示 `calcProfit` 方法的实现，包括获取最新行情报价。
- **01:30 - 01:45**: 展示如何从 Redis 缓存中获取最新的行情报价。
- **01:45 - 02:00**: 展示如何计算浮动盈亏（`long diffPrice = MathUtils.mul(...)`）并更新到实体对象。
- **02:00 - 02:15**: 展示如何计算浮动盈亏比例（`pos.setProfitRate(MathUtils.div(...))`）。
- **02:15 - 02:30**: 回顾并总结 `getPositions` 方法的完整逻辑。
- **02:30 - 02:45**: 讨论金融系统中浮点数精度问题，展示 `DecimalFormat` 的使用。
- **02:45 - 03:00**: 总结浮动盈亏和比例的计算公式，并强调使用长整型计算的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **章节标题**: “3.3 持仓服务仓位总览接口实现”。
- **核心概念**: “定义名为 `getAllPositions` 的 rpc 接口，返回参数与 Netty 对外的返回参数保持一致。”
- **浮点数处理**: “科学计数法只是显示问题，可以采用格式化处理：`DecimalFormat df = new DecimalFormat("0.##");`”。
- **计算公式**:
    - **浮动盈亏**: `(最新价 - 成本价) * 持仓数量`。
    - **浮动盈亏比例**: `浮动盈亏 / (成本价 * 持仓数量)`。
    - **精度要求**: “客户端一般保留 2 位小数（盈亏），4 位小数（比例）”。

#### 代码关键内容

- **gRPC 服务接口定义**:
    ```protobuf
    message GetAllPositionResponse{
        string status = 1;
        string message = 2;
        repeated GetAllPositionData getAllPositionData = 3;
    }
    ```

- **gRPC 服务实现类**:
    ```java
    @GrpcService
    @Log4j2
    public class GrpcStockPositionService extends StockPositionServiceGrpc.StockPositionServiceImplBase {
        @Autowired
        private RedisTemplate redisTemplate;
        @Autowired
        private CacheManager cacheManager;
        @Autowired
        private IStockPositionService stockPositionService;
    }
    ```

- **服务实现类**:
    ```java
    @Service
    public class StockPositionServiceImpl implements IStockPositionService {
        @Autowired
        private ITradePositionDao tradePositionDao;
    }
    ```

- **获取持仓数据方法**:
    ```java
    public List<TradePosition> getAllPositions(Long accountId) {
        List<TradePosition> positionList = tradePositionDao.getAllByAccountId(accountId);
        if (null != positionList) {
            positionList.forEach(pos -> {
                calcProfit(pos);
            });
        }
        return positionList;
    }
    ```

- **计算浮动盈亏方法**:
    ```java
    private void calcProfit(TradePosition pos) {
        // 1. 获取最新的行情报价
        TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(pos.getStockId());
        if (null != quoteLast) {
            // 2. 采用长整型计算，保留两位小数
            long diffPrice = MathUtils.mul(quoteLast.getLastPrice().sub(pos.getCostPrice()), pos.getQuantity());
            pos.setLastPrice(diffPrice);
            // 3. 计算浮动盈亏比例
            long profitRate = MathUtils.div(diffPrice, MathUtils.mul(pos.getCostPrice(), pos.getQuantity()));
            pos.setProfitRate(profitRate);
        }
    }
    ```

- **获取行情报价方法**:
    ```java
    private TradeStockQuoteLast getTradeStockQuoteLast(Long stockId) {
        Cache lastPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_LAST_PRICE_KEY);
        Cache.ValueWrapper quoteLastWrapper = lastPriceCache.get(stockId);
        if (null != quoteLastWrapper) {
            return quoteLastWrapper.get();
        }
        return null;
    }
    ```

---

### 4) 关键场景与演示描述

- **场景一：定义 gRPC 接口** (00:00-00:15)
    - 讲师在 Typora 文档中展示 `getAllPositions` 的 gRPC 返回消息结构，强调其与 Netty 服务的参数一致性。

- **场景二：构建 gRPC 服务实现** (00:15-00:30)
    - 讲师在 IntelliJ IDEA 中展示 `GrpcStockPositionService` 类，说明其继承自 `StockPositionServiceGrpc.StockPositionServiceImplBase`。
    - 展示了 `@Autowired` 注入的 `RedisTemplate`、`CacheManager` 和 `IStockPositionService`，说明服务依赖的组件。

- **场景三：实现业务逻辑层** (00:30-01:00)
    - 讲师切换到 `StockPositionServiceImpl` 类，展示其 `@Service` 注解和 `implements IStockPositionService`。
    - 展示了 `@Autowired` 注入的 `ITradePositionDao`，为后续数据访问做准备。

- **场景四：数据获取与处理** (01:00-01:30)
    - 讲师在 `getAllPositions` 方法中，通过 `tradePositionDao.getAllByAccountId(accountId)` 获取持仓数据。
    - 通过 `positionList.forEach(pos -> calcProfit(pos))` 遍历并调用 `calcProfit` 方法。

- **场景五：计算浮动盈亏** (01:30-02:00)
    - 讲师在 `calcProfit` 方法中，通过 `getTradeStockQuoteLast` 获取最新行情。
    - 展示了如何从 Redis 缓存中获取行情数据。

- **场景六：长整型计算** (02:00-02:30)
    - 讲师使用 `MathUtils.mul` 和 `MathUtils.div` 进行长整型计算，避免浮点数精度问题。
    - 展示了 `diffPrice = MathUtils.mul(...)` 和 `profitRate = MathUtils.div(...)` 的计算过程。

- **场景七：精度处理讨论** (02:30-03:00)
    - 讲师在 PPT 中讨论了金融系统中浮点数精度问题。
    - 展示了 `DecimalFormat` 的使用，用于格式化显示。
    - 强调了在复杂运算中应优先使用长整型计算，以保证精度。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解该技术课程的内容。
