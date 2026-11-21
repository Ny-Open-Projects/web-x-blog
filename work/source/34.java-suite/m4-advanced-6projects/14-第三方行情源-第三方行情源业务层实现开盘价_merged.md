# 14-第三方行情源-第三方行情源业务层实现开盘价 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢,咱们开始实现service神,长期逻辑的处理。

那首先呢,我们要去创建业务实现类。

回到咱们的代码当中,在service下面,我们首先创建一个接口,

interface,i,stock,port,service。

接着呢,我们创建它的实现类,创建一个包,implement,

好,创建一个实现类,stock,port,service,implement。

它要实现i,stock,port,service这个接口,

加上读解,service,加上nombook,日志的读解。

这一块功能代码的实现呢,会比较多。

咱们先从讲义当中,将一些必要的辅助代码呢,先copy进来。

加大的成员属性,还有一些辅助方法,我们呢,先全部copy进去。

咱们侧重呢,去讲解长期员的对接处理流程。

copy放到咱们的代码当中。

好,这些辅助方法呢,咱们用到的时候,还会做一个详细讲解。

这里呢,还有一些数据层接口。

这个数据层接口逻辑来讲呢,并不复杂。

咱们呢,也先将它copy进去。

这个呢,是交易数据员的数据层接口。

好了,放在shared目录下面。

接着呢,咱们再copy业务数据员的数据层接口。

copy完成之后呢,咱们要检查一下它的包路径是否正确。

避免引用的时候呢,产生冲突和问题。

好,copy完成之后,咱们回过头来。

这里爆出了一些错误,咱们先把这些错误呢,除一下。

这个是Data Utils的工具,相当的引入进来。

咱们接着往下面看。

这里有个接口呢,咱们需要定义一下。

Copy到这个层。

它是用于呢,获取所有有效的股票产品。

下面呢,是它的辅助方法,计算了涨跌幅的比例。

在实现主逻辑的过程当中呢,咱们用到的时候,还会做一个详细讲解。

那接着呢,咱们就来实现它的核心逻辑。

咱们编写一个方法。

这个方法呢,是用于获取股票的行情员数据。

参数是stock。

然后还有一个.

收盘的时间差。

也就是说,收盘距离现在的一个时间差。

这个呢,是用于收盘价的处理。

收盘价在后面召集当中,咱们还会做详细的讲解。

咱们加上对应的注射。

这个呢,是获取股票产品的行情员数据。

那咱们将它呢,定义在接口上面。

这里要有一个Ovary的重写方法。

增加日志打印。

建议咱们的分钟和排查。

打印了股票产品电话。

正在请求获取实时行情数据。

接下来咱们来看一下它整体的实现步骤。

第一个步骤呢,是要调用第三方的行情员的接口。

去获取最新的行情报价数据。

行情员的接口呢,之前咱们已经做了封装。

那么在这里就可以直接进行调用。

聚合。

设的API。

getstock.reel。

传递stock参数。

下面。

进行业务逻辑处理。

然后加上一个check catch的补货。

将异常信息呢,反映出来。

这段代码呢,咱们就不用放在check catch里面。

因为在内部呢,它已经做了check catch的异常补货。

接着的话呢,我们继续。

我们就先来看看这个行情报价的逻辑。

先用完成之后呢,要判断实时行情报价。

它是否呢,获取成功。

那做一个围空判断。

取到数据之后。

第三步呢,咱们就要去获取K线加工的缓存管理器。

咱们拿到实时行情之后呢,要将这些数据放到缓存里面。

然后呢,再去加工生成不同周期的K线。

接下来呢,我们就要去做一个K线加工的缓存管理器。

实时行情报价数据呢。

放入缓存。

首先拿到catch对象。

这个呢,从ladies catch manager里面获取。

传递它的T值,global consistence,传量当中获取stock,quota。

T值呢,stock,quota,generate,catch,这个呢是专门用于K线缓存加工的T值。

然后将行情呢,放入缓存当中。

然后呢,我们就要去做一个K线加工的缓存管理器。

这个呢,从ladies catch manager里面获取。

因为咱们有很多个股票产品编号。

所以呢,咱们要通过产品编号,再加上一个时间去作为区分和存储。

从实时行情数据当中获取报价时间,what last。

它的格式呢,就是以一个数线作为一个区分。

不同股票产品的编号是不一样。

第四个步骤呢,就要去更新,处理收盘价。

收盘价呢,必须要在收盘的时候做处理。

它为了预留一个时间缓存,咱们在这里收盘后五分钟之内进行更新。

要做一个判断。

由外层调用的时候呢,做了一个时间判断处理,然后再将这个时间差呢,传进来。

我们就可以直接拿到这个时间差,做一个评价。

并且呢,要小于等于五分钟。

这样就是确定了它在收盘后,而且呢,是收盘后五分钟内。

那至于收盘价的具体处理逻辑呢,咱们后面档节还会做一个详细的讲解与介绍。

第五个步骤呢,就要去更新它的开盘价。

如果行情员呢,它没有提供,需要自定义实现。

在这里,第三方聚合数据源平台呢,它其实已经提供出来了开盘价。

但在这里呢,咱们还是要讲解如何去计算开盘价。

在第三方行情员没有提供开盘价的情况下,

要知道如何去处理和实现。

咱们呢,先画一下开盘价的整个的处理流程是怎样的。

交易市场呢,一般会有个开盘时间。

那在我们A股上面呢,是九点半开始。

然后呢,会有个休市时间。

休市时间一般是下午三点。

那开盘价咱们怎么去记录呢?

开盘价会放在两个地方。

一个呢,是咱们的JVM自身的MAP。

另外一个呢,是Ladies缓存。

这个是MAP缓存。

这个呢,就是Ladies缓存。

咱们放大一点。

Ladies缓存呢,在跨节点的时候,

大家都能够共享相应的数据。

而MAP缓存呢,一般就用于自身节点当中的业务逻辑处理。

开盘价呢,一般是开市的第一口报价。

也就在九点三十分。

如果是九点三十分开盘,那么九点三十分接收到的第一口报价,这个呢,就作为开盘价。

这个时候大家要想一下,如果我们服务一直正常运行,这个行情信息呢,是一时可以连续的记录。

这样呢,是没有问题。

但是咱们服务呢,如果是在九点半到三点的整个过程当中,出现了中断或者是重启。

那么咱们是不是重启的时候就要去Ladies缓存当中,加载对应的开盘价信息。

所以呢,在这里,我们要注意一个点。

在这里,我们要注意一个点。

在这里,我们要注意一个点。

在这里,我们要注意一个点。

时间呢,一般要放在开盘之前,修饰之后处理。

也在下午三点钟之后去进行清除。

你不能在下午三点钟之前就做清除。

那这样的话呢,开盘价,当天的开盘价就会丢失,对不对?

也就是说,这个时间段呢,你必须要在第二天的开盘时间范围之内。

比如说第二天的话呢,是第二天的九点半。

那必须在下午三点至第二天的九点半这段区间之内。

一般咱们呢,就设置在凌晨一点进行执行。

因为下午三点钟之后呢,咱们可能还会有一些任务,比如一些调度任务,要去统计报表,要去拿取当天的一些开盘价做处理。

所以呢,这个时间,我们最好安排在调度任务处理完成之后,也就一般安排在凌晨的时候去进行处理就可以。

那么,除了这两种情况,还有没其他情况呢?

大家想一想,如果说内地是缓存出现了异常,对不对?

这个时候的话呢,我们服务也出现了重启,那不就这个数据就完全丢失了。

该怎么处理呢?咱们就要在行情接收的时候呢,还要加一层判断。

对缓存开盘价信息做判断。

如果不存在,则插入放入开盘价信息。

好,这个呢,就是整体的一个开盘价交互和处理的流程。

在这里,我们开盘价主要就是放在这两个地方。

一个呢,是自身的MAP缓存。

一个呢,是内地的缓存。

这三点逻辑呢,大家一定要理解清楚。

好,接着咱们就从代码做个实现。

咱们再去编写一个方法,去实现开盘价的处理。

这个呢,就是update,open,vice,order last,创建该方法。

这个方法的作用呢,就刚才咱们所讲的第三点。

对缓存呢,要做一个判断。

如果是缓存里面没数据,我们就要放入开盘价信息。

这个呢,不能保证百分之百的准确。

但是这个会拿到它的第一口行情报价作为开盘价信息。

首先呢,它要获取开盘价缓存。

从MAP当中拿取,还录呢,产品ID。

如果open price,它等于空的。

咱们就要去写入开盘价缓存信息。

首先,更新呢,Vadis当中的缓存信息。

这个呢,就要去写入开盘价缓存信息。

获取缓存信息。

从内项。

根据股票ID进行存储。

放入它的最新价格。

最新价格呢,就相当于是第一口的行情报价。

因为在这里,接收到的是实时行情数据。

更新。

MAP缓存。

Proc OpenPage。

这里呢,也是以Store ID作为替。

拿取它的最新报价。

然后在服务启动的时候呢,咱们还去Ladies缓存。

在Ladies缓存当中,去加载开盘价信息。

Publish.

Void.

Unit.

Open.

Vice.

如何初始化加载呢?

咱们通过一个注解。

Hoser.

PencilChart。

加上注释。

初始化。

开盘价缓存信息。

从Ladies缓存中加载数据。

咱们将它呢,定义在接口上面。

然后这里重写。

接下来呢,咱们还要去再实现一个新的缓存。

再实现一个方法。

它的作用呢,是服务运行在第二天的时候呢。

要去清除上一天的开盘价信息。

那咱们呢,先定义好对应的方法。

这个呢,就是一个定时任务。

给它加上对应的注释。

它的作用呢,是要定时重置开盘价缓存信息。

确保当天的开盘价能够正常记录。

这个方法的具体实现。

在下面章节,Slim boot和定时任务整合的时候呢。

咱们还会做具体的讲解。

那这一讲,咱们讲解了开盘价的处理流程。

以及第三方行情员对接的部分业务处理逻辑。

在下面章节呢,咱们还会对开盘价缓存信息呢。

做一个具体的实现。

那这一讲呢,咱们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据处理系统的开发教程，主要聚焦于 `StockQuoteServiceImpl` 服务类的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何处理从第三方行情源（如 `JuheThirdApi`）获取的原始行情数据。核心内容包括：
- **数据封装与转换**：将带精度的价格和时间戳转换为系统内部使用的 `Long` 类型。
- **涨跌幅计算**：实现 `calcPriceRate` 方法，根据最新价和开盘价计算涨跌百分比。
- **缓存管理**：使用 Redis 缓存行情数据（`STOCK_QUOTE_GENERATE_KLINE_KEY`）和开盘价（`STOCK_QUOTE_OPEN_PRICE_CUR_KEY`），并实现定时刷新机制。
- **异常处理**：在数据获取和缓存操作中加入 `try-catch` 块进行错误捕获和日志记录。
- **代码结构**：展示了 Spring Boot 项目结构、注解（如 `@Service`, `@Autowired`, `@Log4j2`）和 Lombok 的使用。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:05**：开场，展示课程大纲和 `StockQuoteServiceImpl` 类的初步代码结构。
- **0:05 - 0:15**：讲解行情数据的封装需求，提及 `MathUtils.roundLong` 和 `cvtDatetime` 方法用于处理价格和时间。
- **0:15 - 0:30**：进入 `calcPriceRate` 方法的实现，展示如何计算涨跌幅（正数、零、负数）。
- **0:30 - 0:45**：演示 `getReal` 方法，调用第三方 API 获取实时行情数据，并处理返回的 JSON。
- **0:45 - 1:00**：讲解如何将获取到的行情数据存入 Redis 缓存，并实现缓存更新逻辑。
- **1:00 - 1:15**：展示 `updateOpenPrice` 方法，用于更新开盘价缓存，并初始化缓存。
- **1:15 - 1:30**：演示 `initOpenPriceCache` 和 `scheduleRestOpenPriceCache` 方法，实现缓存的初始化和定时刷新。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

- **服务类定义**：
  ```java
  @Service
  @Log4j2
  public class StockQuoteServiceImpl implements IstockQuoteService {
      @Autowired
      private TradeStockRepository tradeStockRepository;
  }
  ```

- **涨跌幅计算方法**：
  ```java
  private double calcPriceRate(Long lastPrice, Long openPrice) {
      long diffPrice = MathUtils.sub(lastPrice, openPrice);
      if(diffPrice > 0) {
          priceRate = MathUtils.divDouble(diffPrice, openPrice) * 100;
      } else if(diffPrice == 0) {
          priceRate = 0;
      } else {
          priceRate = -MathUtils.divDouble(diffPrice, openPrice) * 100;
      }
      return priceRate;
  }
  ```

- **获取实时行情并缓存**：
  ```java
  public TradeStockQuoteLast getReal(TradeStock stock) {
      // 构建请求参数
      Map<String, String> params = new HashMap<>();
      params.put("aid", stock.getStockCodeByMarket(stock));
      params.put("key", APPKEY);
      
      // 调用第三方API
      TradeStockQuoteLast quoteLast = JuheThirdApi.getReal(stock);
      
      // 缓存数据
      Cache cache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_GENERATE_KLINE_KEY);
      cache.put(stock.getCode() + "_" + System.currentTimeMillis(), quoteLast);
      
      // 更新涨跌幅
      if(closeDiffMins >= 0 && closeDiffMins <= 5) {
          // TODO 后面章节讲解实现
      }
  }
  ```

- **更新开盘价缓存**：
  ```java
  private void updateOpenPrice(TradeStockQuoteLast quoteLast) {
      Long openPrice = stockOpenCache.get(quoteLast.getStockId());
      if(openPrice == null) {
          Cache curOpenPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
          curOpenPriceCache.put(quoteLast.getStockId(), quoteLast.getLastPrice());
          stockOpenCache.put(quoteLast.getStockId(), quoteLast.getLastPrice());
      }
  }
  ```

- **初始化和定时刷新开盘价缓存**：
  ```java
  @PostConstruct
  public void initOpenPriceCache() {
      // 初始化缓存
      Cache curOpenPriceCache = redisCacheManager.getCache(GlobalConstants.STOCK_QUOTE_OPEN_PRICE_CUR_KEY);
      // ... 初始化逻辑
  }

  public void scheduleRestOpenPriceCache() {
      // 定时刷新缓存
      // ... 定时任务逻辑
  }
  ```

#### **关键注解与配置**

- `@Service`：标识该类为 Spring 服务层组件。
- `@Log4j2`：用于日志记录。
- `@Autowired`：自动装配依赖的 `TradeStockRepository`。
- `@PostConstruct`：在 Bean 初始化后执行初始化方法。
- `@Log`：Lombok 注解，用于简化日志记录。

---

### 4) 关键场景与演示描述

- **场景一：项目结构与服务类初始化**
  - 讲师在 IntelliJ IDEA 中展示项目结构，重点讲解 `StockQuoteServiceImpl` 类。
  - 通过 `@Service` 和 `@Log4j2` 注解，说明该类是服务层组件，并用于日志记录。
  - 展示 `@Autowired` 注解自动装配 `TradeStockRepository`。

- **场景二：涨跌幅计算逻辑**
  - 讲师在 `calcPriceRate` 方法中，通过 `MathUtils.sub` 计算价格差值。
  - 根据差值的正负，使用 `MathUtils.divDouble` 计算百分比，并处理零值情况。
  - 展示了 `priceRate` 的计算逻辑和返回值。

- **场景三：第三方 API 调用与缓存**
  - 讲师调用 `JuheThirdApi.getReal(stock)` 方法获取行情数据。
  - 通过 `HttpUtil` 发起 HTTP 请求，并处理返回的 JSON 数据。
  - 将获取到的行情数据存入 Redis 缓存，使用 `GlobalConstants.STOCK_QUOTE_GENERATE_KLINE_KEY` 作为缓存键。

- **场景四：开盘价缓存管理**
  - 讲师演示 `updateOpenPrice` 方法，用于更新开盘价缓存。
  - 通过 `stockOpenCache` 和 `redisCacheManager` 管理开盘价缓存。
  - 展示了 `initOpenPriceCache` 方法的初始化逻辑和 `scheduleRestOpenPriceCache` 方法的定时刷新机制。

- **场景五：异常处理与日志记录**
  - 在多个方法中，讲师使用 `try-catch` 块捕获异常。
  - 使用 `Log.info` 和 `Log.error` 记录日志信息，便于调试和问题追踪。

---

以上是根据视频画面进行的结构化技术分析，涵盖了视频的主要内容和关键操作。
