# 16-第三方行情源-第三方行情源外层调用处理逻辑 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话咱们来实现行情处理的外层业务逻辑

行情员对接完成之后

咱们是应该还在提供一个路口进行相应的调用和触发

这个调用处理环节就在咱们容器启动后开始执行

咱们就来做一个具体实现

首先创建一个Global System Configuration配置内

这个放在Configure目录下面

New JAL Class

点击OK

咱们先将它的周边代码copy进来

然后再copy下它的辅助方法

接着JAL实现这个接口所定义的Run方法

在这里面咱们就要处理它的核心业务逻辑

这方法是在容器启动后会进入执行

读容器启动完成后调用执行

咱们来实现它的核心逻辑

首先加上日志打印

咱们通过一个后台线程去调用了第三方行权

实现一格处理

那么这个调用是一个循环调用

内部的话加上Check Catch

防止因为出现异常

整个调用就产生终止

接下来是获取有效的股票产品行情数据

我们给它定义一个方法

Get Stock

Borders

这个方法咱们接下来去做实现

调用完这个方法之后

还给它一个间隔时间

外层是一个无限循环

在这里我们每次获取到股票产品行情数据之后

让它休息一段时间

一般设置为一秒

如果适合第三方行情源

通过Soci的长连接

或者订阅MQ

那么服务端可以将频率改快一点

一秒钟推送多口报价都没有问题

这种ATTB主动拉取方式

一般设置为一秒拔取一到两次行情数据就可以了

由于是教学测试

这里时间可以适当放长一点

这里咱们设定为30秒

因为是受限免费账号的限制

在这里Slide点Sleep

单位是毫秒

30秒的话就是3万

Slide完成之后要用Start方法

接着咱们就来实现获取有效的股票产品行情数据方法处理

加上对应的注册

获取股票的产品行情数据

这里该怎么去做呢

首先第一步要获取所有的有效产品

之前咱们在service里面定义了相应的方法

Check stock

拿到的是一个list

stock, quote, service, fund

所有的有效股票产品

然后咱们打一个日志

这个日志我们将它的获取的股票总数量打出来

stock, list, size

接下来做一个唯空判断

if now不等于stock list

并且这个大小要大于0

然后咱们怎么去获取股票的产品行情数据呢

咱们的股票是支持多个市场

所以在这里为了提升股票的成本

提升它的处理效率

咱们就要按市场去做一个分组汇总

通过不同的市场并行处理

提升整个行情数据的获取效率

虽然咱们在这里只是实现了附身的股票市场

并没有实现行股或者美股

但是咱们可以按照多种股票市场的逻辑去做

提升它的一个扩展性

根据股票产品的市场电号进行分组汇总处理

这样可以拉开股票的市场的规模

让每个市场的股票信息处理步步干道

股票市场是一个整形

然后Chadstock是对应的股票产品数据

Bluetooth by Stock List

Streams,Bluetooth by

这里参数就是Chadstock根据它的市场电号

这样就根据市场电号完成了对应的分组

好

拿到分组之后咱们就要做一个循环迭代处理

Market Number

然后是它具体的值

拿到股票市场之后

咱们要去根据股票市场去获取对应的市场分类

因为股票市场分类里面会包含股票产品的一些设置信息

比如说它的交易时间等等

所以咱们在这里要去校验股票产品的分类是否存在

股票分类和股票市场是对应关系

分类信息里面包含交易时间等设置信息

所以咱们要在这里对分类做一个获取和判断

叫做Stock Calibrate

然后通过数据审解口根据编号来查找

在这里咱们要通过一个枚举做转换

将它的市场编号转换为股票市场的标识

获取股票市场的标识

那么通过这个标识就可以找到对应的分类

咱们可以看一下这个枚举

之前也做了讲解

也就是说咱们在这里有支持多少个股票交易市场

那么在数据库当中股票分类表里面就会做相应的配置

比如说有上交所、升交所

那么它的编号就是在这里面的市场标识

马上就会看到了

根据这个市场标识就能够找到市场分类

然后就读取了股票产品分类里面的配置信息

像这里面的交易时间、交易佣金比例等等

咱们再回到刚才的处理逻辑

接下来咱们做一个围攻判断

给它一个日子打印

没找到对应的股票产品分类信息

防保可以打印出来

这个咱们就采用站位符的方式

然后退出方法

接下来就要去判断是否处于开盘时间

咱们同样通过一个方法做判断处理

以时Open Time

在这里咱们就传入分类产品分类信息

以时Open Time它的判断也比较简单

通过当前时间和开始时间做一个判断比较

判断完成之后

在这里还做一个判断

要去计算距离收盘的时间分钟差

这个是用于后面对收盘价的处理

咱们之前做了假检

收盘价是在收盘后五分钟内进行更新处理

那么在这里我们做一个计算

通过以时Open Time的方法做判断处理

同样也是传入产品分类信息

它的判断也是和它的交易结束时间做一个对比

然后计算出它所剩余的时间

通过DataUtils这个工具去做具体的处理

咱们再回到刚才的处理逻辑

接下来就在交易时间内

获取股票产品的实时行情数据

这里咱们是做测试

就不做交易处理了

我们先来看看交易时间的限定

因为如果是做了交易时间的限定

那么在交易时间之外

咱们就没法获取行情的数据信息

要做交易时间判定其实很简单

根据以时Open Time如果等于2

并且当前的时间要小于等于具体收盘价的五分钟

那么就可以得出它是在交易时间范围之内

这里将它放行

为了提升处理效率

在这里就采用现成式方式

Task XKey

Cute is cute

在这里面开启一个Ulanobu接口

然后我们要去建立股票产品

这里我们就采用并发流方式

建立获取每个股票市场的所有产品行情数据

在上面分组汇总的值做一个转换处理

Chad Stock Market Stock List

做强转

然后采用流逝方式

Market Stock List

点

并行流方式

For each

这里就是stock

然后调用stock for the service

之前所通过的方法

去抓取股票行情数据

好

为了避免某只产品产生的异常

咱们在外层加入一个异常补货的处理

将异常信息反映出来

好

在这里咱们就完成了外层对行情源获取的逻辑处理

咱们回到讲习当中

再来回顾一下整体的处理流程

在这里咱们首先是通过Application Runner的乱放吧

在服务初始化的时候

调用行情处理逻辑

在内部咱们是开启一个新的线程

由Get Stock Call的方法去处理具体的逻辑

通过

Stock Call的Service

这里面提供一个获取所有有效股票产品的业务接口

然后拿到有效的股票产品信息

先做一个非空判断

接着的话咱们就要遍历所有的产品

要用第三方行情源接口去获取报价信息

在遍历之前做了一个分组汇总

根据不同的股票市场进行相应的分组汇总

这样的话

不同市场之间的股票产品

互不干扰不会产生影响

也能提升股票行情的定发处理速度

内部调用处理线程

它需要一直执行

间隔时间是30秒更新一次

咱们在这个代码当中也做了一个讲解

这个线程会一直进行一个循环调用

外层的话要一个Track Catch一场的捕获

避免整个处理过程当中出现异常

导致整个线程出现中断

在实际生产环境当中可以加快它的频率

一般一秒更新一次

因为是后台线程处理

为了防止中断

就需要加入Track Catch的捕获一场

无论是在这个最外层

还是在内部的通过线程式方法的调用

注意要加上Track Catch一场的捕获

行情获取的具体调用

就是通过咱们上面章节当中

对行情第三方行情员调用的封装做了处理

通过Get Store Course方法

获取股票产品的行情数据

最后咱们要注意

在不同市场的股票行情

处理逻辑当中

我们加入了线程式的处理

每个线程对应处理的是每个市场的所有股票信息

咱们从代码图中可以看到

外层做了一个便利

内部拿到的是进行了分组汇总的股票产品信息

然后将它通过线程式方式进行调用

这样每个市场的股票产品数据

它都是得力处理了

那么在这个线程内部

咱们可以看到采用了B型流的方式

通过B型流的方式

进行调用的目的也是为了提升它的处理效率

因为这一块咱们可以不用保持它的有序性

大家注意这个B型流的调用

虽然能够提升并发处理速度

但是正因为它提升的并发处理速度

所以就不能保证处理的有序性

如果是对一些逻辑性比较强的业务

这个B发流的处理要慎重

好在这里就是对外层第三方行权对接逻辑处理的实现

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据处理系统的实现讲解，核心内容是展示如何在 Spring Boot 应用中，通过 `@Configuration` 和 `ApplicationRunner` 接口，启动一个后台线程来持续、并行地从第三方行情服务获取多个市场的实时行情数据。视频重点演示了如何利用 Java 8 的 Stream API 对数据进行分组聚合，并使用 `TaskExecutor` 来并发处理不同市场的行情请求，以提升系统性能。整个过程结合了 Spring 的依赖注入、流式处理和异步任务执行机制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:03**: 视频开始，展示课程大纲，定位到“3.1 行情服务与MQ集成配置”章节。
*   **00:00:03 - 00:00:08**: 展示 `GlobalSystemConfiguration` 类的代码结构，说明其作用是监听服务启动并调用业务逻辑。
*   **00:00:08 - 00:00:12**: 代码编辑器中，光标位于 `while(true)` 循环的起始位置，准备讲解主线程的无限循环。
*   **00:00:12 - 00:00:18**: 代码编辑器中，光标位于 `getStockQuotes()` 方法的定义处，准备讲解获取行情数据的核心逻辑。
*   **00:00:18 - 00:00:24**: 代码编辑器中，光标位于 `Map<Integer, List<TradeStock>> groupBy` 语句，讲解如何对股票产品按市场进行分组。
*   **00:00:24 - 00:00:30**: 代码编辑器中，光标位于 `tradeStockCategoryRepository.findByCode(...)` 语句，讲解如何根据市场编号查询对应的分类信息。
*   **00:00:30 - 00:00:36**: 代码编辑器中，光标位于 `taskExecutor.execute(new Runnable()` 语句，讲解如何将每个市场的行情处理任务提交给线程池。
*   **00:00:36 - 00:00:42**: 代码编辑器中，光标位于 `marketStockList.parallelStream().forEach(...)` 语句，讲解如何使用并行流对不同市场的行情数据进行并发处理。
*   **00:00:42 - 00:00:48**: 代码编辑器中，光标位于 `run()` 方法的 `try-catch` 块，讲解如何处理线程中断异常。
*   **00:00:48 - 00:00:54**: 展示课程大纲，总结本节内容，强调了线程、分组、并行处理和异常处理等关键点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

**关键代码片段：**

*   **`GlobalSystemConfiguration` 类定义：**
    ```java
    @Configuration
    @Log4j2
    public class GlobalSystemConfiguration implements ApplicationRunner {
        @Autowired
        private IStockQuoteService stockQuoteService;
        @Autowired
        private TaskExecutor taskExecutor;
        @Autowired
        private TradeStockCategoryRepository tradeStockCategoryRepository;
    }
    ```

*   **`getStockQuotes()` 方法核心逻辑：**
    ```java
    private void getStockQuotes() {
        // 1. 获取所有的有效产品
        List<TradeStock> stockList = stockQuoteService.findAllValidStocks();
        if (null != stockList && stockList.size() > 0) {
            // 2. 根据股票产品的市场编号，进行分组汇总处理
            Map<Integer, List<TradeStock>> groupBy = stockList.stream()
                    .collect(Collectors.groupingBy(TradeStock::getMarketNo));
            // 3. 校验股票产品的分类是否存在
            for (Map.Entry<Integer, List<TradeStock>> entry : groupBy.entrySet()) {
                TradeStockCategory category = tradeStockCategoryRepository.findByCode(
                        StockMarketEnum.parseByMarketNo(entry.getKey()).getCategoryCode());
                // 4. 校验市场是否开放
                if (!category.isOpenTime()) {
                    continue;
                }
                // 5. 获取每个市场的行情数据
                List<TradeStock> marketStockList = entry.getValue();
                // 6. 并发处理
                taskExecutor.execute(new Runnable() {
                    @Override
                    public void run() {
                        marketStockList.parallelStream().forEach(stock -> stockQuoteService.fetchStockQuote(stock, stockDiffMins));
                    }
                });
            }
        }
    }
    ```

*   **`ApplicationRunner` 的 `run` 方法：**
    ```java
    @Override
    public void run(ApplicationArguments args) throws Exception {
        log.info("Process in GlobalSystemConfiguration.run method.");
        new Thread(() -> {
            while (true) {
                try {
                    getStockQuotes();
                    Thread.sleep(30000); // 30秒更新一次
                } catch (Exception e) {
                    log.error(e.getMessage(), e);
                }
            }
        }).start();
    }
    ```

**关键概念：**

*   **`@Configuration`**: 标识这是一个配置类，用于定义 Spring 容器中的 Bean。
*   **`ApplicationRunner`**: 一个接口，用于在 Spring Boot 应用启动后执行自定义逻辑。
*   **`@Autowired`**: Spring 的依赖注入注解，自动将匹配的 Bean 注入到字段中。
*   **`Stream API`**: Java 8 引入的函数式编程接口，用于对集合进行流式处理，如 `collect(Collectors.groupingBy(...))`。
*   **`TaskExecutor`**: Spring 提供的异步任务执行接口，用于管理线程池。
*   **`parallelStream()`**: 并行流，用于对集合进行并行处理，提高性能。
*   **`try-catch`**: 用于捕获和处理运行时异常，确保线程不会因异常而中断。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与核心类定位 (00:00:00-00:00:08)**
    *   **描述**: 视频开始时，画面展示了一个 Markdown 文档（`Days12.md`）的目录结构，其中包含了“3.1 行情服务与MQ集成配置”等章节。随后，画面切换到 IntelliJ IDEA 编辑器，显示了 `GlobalSystemConfiguration.java` 文件，这是本节的核心代码文件。演示者通过鼠标点击和滚动，引导观众关注 `@Configuration` 和 `ApplicationRunner` 接口的定义，说明了该类的作用是监听服务启动并调用业务逻辑。

*   **场景二：主线程循环与行情获取 (00:00:08-00:00:18)**
    *   **描述**: 演示者将光标移动到 `while(true)` 循环的起始位置，说明这是一个无限循环，用于持续执行行情数据的获取。接着，光标移动到 `getStockQuotes()` 方法，演示者开始讲解如何获取所有有效的股票产品。

*   **场景三：数据分组与分类校验 (00:00:18-00:00:30)**
    *   **描述**: 演示者将光标定位到 `Map<Integer, List<TradeStock>> groupBy` 语句，通过 `Stream API` 的 `collect(Collectors.groupingBy(...))` 方法，将股票产品按市场编号进行分组。随后，光标移动到 `tradeStockCategoryRepository.findByCode(...)` 语句，演示者讲解了如何根据市场编号查询对应的分类信息，并校验市场是否开放。

*   **场景四：并发处理与并行流 (00:00:30-00:00:42)**
    *   **描述**: 演示者将光标定位到 `taskExecutor.execute(new Runnable(...))` 语句，说明将每个市场的行情处理任务提交给线程池。接着，光标移动到 `marketStockList.parallelStream().forEach(...)` 语句，演示者讲解了如何使用并行流对不同市场的行情数据进行并发处理，以提升系统性能。

*   **场景五：异常处理与线程管理 (00:00:42-00:00:48)**
    *   **描述**: 演示者将光标定位到 `try-catch` 块，说明了如何捕获和处理运行时异常，确保线程不会因异常而中断。最后，演示者将光标定位到 `run()` 方法的 `while(true)` 循环，说明了该线程会持续运行，每隔30秒更新一次行情数据。

*   **场景六：课程总结 (00:00:48-00:00
