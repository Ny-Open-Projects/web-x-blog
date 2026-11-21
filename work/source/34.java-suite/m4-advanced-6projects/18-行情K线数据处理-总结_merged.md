# 18-行情K线数据处理-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们要对行情K线数据整体功能做一个测试和验证

首先我们要对K线数据的生成功能做一个验证

整个处理流程该如何去验证呢

我们首先要等待行情的接收

达到一分钟后我们再去检查数据库

大家在这里要注意一下

如果是修饰之前已经生成了修饰的最后一条数据

所以不会再生成新的数据

因为代码当中是根据了时间做了一个去从的处理

大家之前应该还记得

我们的ChadstockCourtLess的这个数据层接口

可以找到给大家看一下

这里提供的数据层查询接口

是要根据股票ID和时间去获取对应的对象

是做了一个去从判断

所以如果是修饰之后

所接收到的行情时间

它就是修饰结束

结束的那个时间点不会再产生新的时间上的变化

所以它就不会去生成新的数据

但目前已经是修饰时间

那么我们该如何去验证呢

针对这种情况

咱们提供了一个模拟行情推送的逻辑

那么我们来看一下模拟行情处理逻辑

这块是如何实现的

咱们要修改FedgestalkCourt这个方法

之前我们是发送了实时行情

它会去聚合数据层平台上面拉取

实时行情数据

因为受到交易时间的限制

我们在这里提供了一个发送模拟行情的接口

大家可以根据需要自行去做对应的控制

发送模拟行情接口

它是如何实现的

我们点进去可以看一下

它是从之前行情缓存当中拉取到对应的数据

然后做了一点加工

会生成一个随机的价格

那么它的时间呢

就是取

当前的系统时间

这样的就能够源源不断的产生不同的行情数据

但是前提咱们要先通过第三方行情平台生成真实的行情数据

行情数据保存在缓存当中之后

我们才能够去使用模拟行情

或者说你自行插入一些行情数据到缓存当中

这个也是可以的

不过为了确保数据的正确性

最好还是从第三方行情平台当中

将数据拉取保存到缓存当中

确保缓存当中存有数据之后

咱们再进行模拟行情的推送

有了模拟行情数据之后

咱们就可以去测试和验证K线数据的生成

在做测试验证之前

我们要确保分片的规则是设定正确的

在ProcessK栏方法当中

这里我们加上SetDataType信息

它的意思是指定生成一分钟的周期K线数据

如果是要生成五分钟的周期K线数据

那么在这里要改成300

在这里我们测试一分钟的周期K线数据的生成就可以

这里面的信息会用于分片规则的处理

在之前我们做分片配置的时候

DataSource Table

这里面我们去配置了它的分片规则

这里面我们去配置了它的分片规则

这里面我们去配置了它的分片规则

这个GetValue正是取得刚才的DataType里面的信息

这个GetValue正是取得刚才的DataType里面的信息

它根据Type里面所配置的值

会将数据生成在不同的表当中

会将数据生成在不同的表当中

这一点大家要理解清楚

接着咱们就来启动服务做个测试验证

首先确保中间键Nacos Ladies是启动成功

那么接着我们就去启动行情服务

启动行情服务之前

咱们先检查数据库当中的数据

检查一分钟K线

周期表

这个是ChadStoreKLAN-1

这个是ChadStoreKLAN-1

我们可以刷新一下

目前的话是没有数据

那么我们启动行情服务

右键Run运行

打空置窗口

启动完成之后

它会调用咱们的K线生成的方法

Schedule

Positions

在这里就会去检索

实时行情数据

生成对应的K线信息

生成对应的K线信息

我们可以看到空置台已经输出了对应的日志

我们可以看到空置台已经输出了对应的日志

在这里就会去检索

注意看这条语句

Inselect into ChadStoreKLAN-1

这张表

它插入了一条数据

是中国平安的K线数据

这个已经生成成功

我们可以刷新一下这张表

在这里面插入了两条数据

这两条数据

跟咱们在产品表里面配置的数据信息

是一致的

可以看到

我们是配置了两只股票

那么它一分钟之后生成了两条K线数据

那么它一分钟之后生成了两条K线数据

好

好

好

好

好

好

好

好

好

好

好

好

好

好

,

那在这里

咱们就测试了K线数据的生成功能

接下来我们就通过模拟客户端

去调用验证获取行清K线的数据接口

为了便于测试验证

我们先将K线生成数据的方法给注射掉

让它不产生新的K线数据

我们回到行情服务当中

重新启动行情服务

然后我们再启动交易服务

右键让运行

启动完交易服务式

我们要启动代理服务

Proxy

右键让运行

确保服务启动成功

这个可以看到

代理服务已经接收到

行情服务推送的模拟行情数据

这个咱们先暂时不用管

我们去启动模拟客户端

右键让运行

首先进行用户登录

好 用户登录成功

先不急着去请求数据

咱们首先看一下

数据库当中的数据信息

我们是做了分表的设计

那么查询的时候

它能否将所有分表的数据

全部汇总在一起呢

那我们来简单看一下

我们是分了三张表

从KLAN1到KLAN30

我们打开这三张表

看一下这里面的具体数据

KLAN1里面有两条数据

KLAN5里面的话呢

有六条数据

KLAN30下面没有任何数据

那我们的模拟终端

它获取K线的参数

传递的是股票编号为601398

那601398在KLAN5这张表当中

存在六条数据

KLAN1这张表当中存在一条数据

那总共的话呢

就会有七条数据

好 接着咱们回到模拟终端

发送获取股票K线行情数据的接口

序号为3

我们可以看到

它能够成功接收到响应消息

再检查一下它所接收消息的数量

这里面有一条

两条

三条

四条

五条

六条

七条

再一个size也是为7

从中咱们就能知道

K线数据的接口呢

能够正常交互

它也能将所有分表的数据汇总在一起

业务接口的数据查询

是不需要做任何调整和改动

刷顶接DBC

会自动帮咱们去做对应的实现

好 在这里咱们就完成了

行情K线数据处理功能的测试和验证

对K线数据生成功能做了测试验证

模拟客户端

获取K线数据接口也做了测试和验证

最后咱们还验证了分表功能的查询处理

都能够正常处理

那这讲内容就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于“行情服务K线分表”技术实现的课程，重点演示了如何在分布式系统中，通过 Spring Boot 和 ShardingSphere 实现 K 线数据的生成、缓存、分表存储及客户端调用的完整流程。核心内容包括：
- **功能验证**：启动行情服务、代理服务和交易服务，验证 K 线数据生成与缓存机制。
- **数据生成逻辑**：在 `StockQuoteServiceImpl` 中，通过 `processKline` 方法处理行情数据，判断是否需要生成新的 K 线或更新现有 K 线。
- **缓存与分表**：使用 Redis 缓存最新行情数据，并通过 ShardingSphere 对 K 线表进行分表，确保数据按规则分布。
- **客户端调用**：通过 `SimulateClient` 模拟客户端向代理服务发送行情请求，验证数据流和缓存命中。
- **数据库验证**：最终在 Navicat 中查询数据库，确认 K 线数据已成功写入分表。

整个过程展示了从数据源到数据库的完整数据链路，强调了缓存、分表和分布式服务间的协作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **0:00 - 0:30**：课程介绍与功能验证目标。展示 PPT 页面，明确本节要验证的功能：启动服务、生成 K 线、模拟客户端调用。
- **0:30 - 1:00**：K 线数据生成服务实现。展示 `StockQuoteServiceImpl` 中的 `processKline` 方法，讲解如何从缓存中获取最新行情数据，并根据时间差判断是否生成或更新 K 线。
- **1:00 - 1:30**：模拟客户端调用服务。展示 `SimulateClient` 类，讲解如何构造行情数据并发送请求。
- **1:30 - 2:00**：代理服务与交易服务启动。展示 `StockProxyApplication` 和 `StockDealApplication` 的启动日志，验证服务间通信。
- **2:00 - 2:30**：缓存与分表逻辑。展示 `StockQuoteServiceImpl` 中的 `sendSimulationQuote` 方法，讲解如何从 Redis 获取行情数据，并通过 ShardingSphere 分表写入数据库。
- **2:30 - 3:00**：数据库验证。切换到 Navicat，展示 `t_trade_stock_kline_5` 表中的数据，验证 K 线数据已成功写入。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 页面**：显示了课程大纲，重点在“3.8 功能验证”部分，包括：
  - 启动 `stock-quote`、`stock-proxy`、`stock-deal` 三个服务。
  - 等待接收行情数据，达到一分钟检查数据。
  - 模拟客户端调用验证。

#### 代码关键内容

- **`StockQuoteServiceImpl.java` - `processKline` 方法**：
  ```java
  private void processKline(TradeStockQuoteLast quoteLast) {
      TradeStockKline kline = klineMap.get(quoteLast.getStockId());
      if (null == kline) {
          // 生成新的K线数据
          kline = newKline(quoteLast);
          klineMap.put(quoteLast.getStockId(), kline);
      } else {
          // 行情K线存在的处理逻辑
          long diffTime = quoteLast.getTm() - kline.getTm();
          if (diffTime > 0 && diffTime < GlobalConstants.KLINE_PERIOD_60) {
              // 更新K线数据
              if (quoteLast.getLastPrice() < kline.getLowPrice()) {
                  kline.setLowPrice(quoteLast.getLastPrice());
              }
              if (quoteLast.getLastPrice() > kline.getHighPrice()) {
                  kline.setHighPrice(quoteLast.getLastPrice());
              }
          }
      }
  }
  ```

- **`StockQuoteServiceImpl.java` - `sendSimulationQuote` 方法**：
  ```java
  public void sendSimulationQuote(TradeStock stock, int closeDiffMins) {
      TradeStockQuoteLast quoteLast = null;
      try {
          // 从缓存中获取行情
          Cache.ValueWrapper quoteLastWrapper = lastPriceCache.get(stock.getStockCode());
          if (quoteLastWrapper != null) {
              quoteLast = quoteLastWrapper.get();
          }
          // 生成K线数据并保存
          processKline(quoteLast);
      } catch (Exception e) {
          log.error("发送行情数据失败", e);
      }
  }
  ```

- **`StockProxyApplication.java`**：
  ```java
  @SpringBootApplication
  @EnableDiscoveryClient
  @ComponentScan(basePackages = {"com.ictast"})
  @EnableScheduling
  public class StockProxyApplication implements ApplicationRunner {
      // 代理服务启动逻辑
  }
  ```

- **`SimulateClient.java`**：
  ```java
  public class SimulateClient {
      private static final String serverIp = "127.0.0.1";
      // 模拟客户端发送行情数据
      public void sendQuote(TradeStockQuoteLast quoteLast) {
          // 发送请求到代理服务
      }
  }
  ```

#### 数据库与日志

- **ShardingSphere 分表 SQL**：
  ```sql
  INSERT INTO t_trade_stock_kline_5 (amount, datatyp, priceclose, pricehigh, pricelow, priceopen, stockcode, stockname, time, volume, id)
  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
  ```

- **Redis 缓存日志**：
  ```
  INFO 6668 --- [main] c.i.b.stock.quote.StockQuoteService : Process in StockQuoteService.sendSimulationQuote method. stock: 601318
  ```

- **数据库查询结果**：
  - 表 `t_trade_stock_kline_5` 中包含多个 K 线记录，如 `stockcode=601318`，`time=1565577380`，`priceopen=548` 等。

---

### 4) 关键场景与演示描述

#### 场景 1：服务启动与功能验证

- **演示**：讲师在 PPT 上展示“3.8 功能验证”章节，明确要启动三个服务：`stock-quote`、`stock-proxy`、`stock-deal`。
- **操作**：在 IDEA 中启动 `StockQuoteApplication`，观察控制台日志，确认服务启动成功。
- **结果**：服务启动后，系统开始监听行情数据，并准备生成 K 线。

#### 场景 2：K 线数据生成逻辑演示

- **演示**：讲师在 IDEA 中打开 `StockQuoteServiceImpl.java`，聚焦 `processKline` 方法。
- **操作**：通过注释和代码逻辑，演示如何判断行情数据的时间差，决定是生成新 K 线还是更新现有 K 线。
- **结果**：当行情数据时间差在 60 秒内，系统会更新 K 线的最高价和最低价。

#### 场景 3：模拟客户端调用

- **演示**：讲师展示 `SimulateClient.java`，讲解如何构造行情数据并发送请求。
- **操作**：在 IDEA 中运行 `SimulateClient`，观察控制台日志，确认请求已发送。
- **结果**：请求被代理服务接收，并触发 `processKline` 方法，生成或更新 K 线数据。

#### 场景 4：缓存与分表验证

- **演示**：讲师在 `StockQuoteServiceImpl.java` 中展示 `sendSimulationQuote` 方法，讲解如何从 Redis 获取行情数据。
- **操作**：在 IDEA 中运行 `StockQuoteApplication`，观察控制台日志，确认数据已写入 Redis。
- **结果**：数据通过 ShardingSphere 分表写入数据库，确保数据按规则分布。

#### 场景 5：数据库验证

- **演示**：讲师切换到 Navicat，展示 `t_trade_stock_kline_5` 表。
- **操作**：在 Navicat 中执行 SQL 查询，确认 K 线数据已成功写入。
- **结果**：数据库中存在多个 K 线记录，验证了整个数据链路的正确性。

---

以上是根据视频画面进行的结构化技术分析，涵盖了视频的主要内容和关键操作。
