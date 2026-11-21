# 23-XXL_JOB集成运用-交割单任务job编写 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,这一讲我们开始学习账户股票交割单调度任务的处理实现

交割单它是用来记录交割的具体交易情况的单据

交割的概念来源于期货

分为实物交割和现金交割

交割单的查询我们一般是以电子表格的形式输出

这样也比较容易看清楚

操作起来也比较简单

交割单的表格内容主要包含交割的日期

证券代码

成交价格等19项内容

覆盖的数据信息比较多

是股民的交割依据

一般以交割单作为依据来计算成本

核对并计算实际的盈亏情况

那交割单和成交记录有什么样的差别呢

它和成交记录是不一样的

成交记录侧重的是股票成交的数据

而交割单呢

它侧重的是股票和资金变动的数据

为了便于计算

我们在成交记录生成的时候

要去计算并保存佣金等相关信息

这样在处理交割单的时候就不用再去追溯

实现起来就会比较简单

因为成交记录里面具备了佣金计算相关的条件

所以呢

在成交记录做好相应处理的时候呢

来的更为简单一些

好那咱们来了解一下账户交割单的实体

主要包括哪些数据信息

首先我们可以看到有优质ID

Account ID

这些呢是用户信息

下面是成交记录的ID

每一笔交割单呢

对应会有一笔成交记录

下面是交易时间

然后是股票ID

股票代码

币种

买卖方向

然后是交易相关的数据信息

比如交易金额

数量

价格

税费

这里面的税费呢

全部累加计算在一起

包括印花税

过户费

交易规费等等

如果是在实际的券商当中进行交易

那么券商会将这些不同的税费分开来做记录

下面是佣金

然后是状态

如果是无效的交割单

在这里面呢

标示为一

接下来我们就去实现交割单的调度任务

首先我们要创建对应的旧宝

回到工程代码当中

咱们在

Job的目录下面

再创建一个指导

这里面是处理资金服务相关的调度任务

然后右键New Java Class

这里创建Account Settlement的Job

这个Job是生成账户交割单数据信息

一般执行时间呢

是要放在修饰之后

比如说每天晚上的十点

这个通过Clone表达师

做相应的配置就可以

要创建一个XSL Job的调度任务

我们要去继承XSL Job提供的抽象类

iJobHandle

实现他的抽象方法

JobHandle这个副类

我们可以点进去看一下

在这里呢

主要就提供三个方法

一个是初始化

一个是销毁

还有一个就是抽象方法

需要执行的具体任务

然后要去添加Job任务的注写

JobHandle了

给他配置一个名称

这个名称就采用内的名称保持一致

然后要标示为他是一个Service

LogProject2日子查鉴

接下来我们要去定一个Service

去负责任务的处理和实现

Account Settlement Service

稍后咱们再去实现业务层的接口

这里呢

先将他定义好

添加注册

这个是

账户交个单任务的实现接口

然后我们再去完成方法的调度处理

首先添加日志

log.info

提示已经进入方法

开始执行调度任务

加名称copy

点一个是JobHandle

Cute

Message

Admin

将传递的参数信息呢可以打印出来

进行调度任务的时候呢

有可能会出现失败

在外围咱们增加异常的补货处理

Catch

Exception

增加异常的输出

然后调用业务层接口

生成账户的交个单信息

Account Settlement Service

这里给他定义一个方法

Generate

OK

Convert to Account

Settlement

传递参数

处理执行完成之后

回处理结果

这里呢

标示为Success

好

这样呢

咱们就完成了一个插在了Job

调度任务的实现

接下来我们将service做一个创建

这个接口是放在service目录下面

OK

咱们再去定义一个接口

Void

Generate

Settlement

String

TitleMate

这个要改成接口

Inface

添加注释

他是生成账户的交个单数据

接下来我们再去创建他的实现内

在service下面创建新的保有

Implement

然后我们创建他的实现内

Account Settlement Service Implement

他要去实现刚才定义的接口

将注释货币进来

生成账户的交个单数据

接下来我们要去注入业务实现所需要用到的属性

Private

Credit deal

将成交记录的数据层接口注入进来

添加AutoVide注册

下面我们再去定义

I Trade Account Settlement Deal

AutoVide

这个是账户交个单

数据层接口

下面我们还要去定义两个缓存接口

为什么要用到缓存

因为我们要去提升交个单的处理性能

减少数据库的查询次数

缓存的接口实现了

我们就直接从已经实现的原码当中扣币进来

一个是账户的缓存

另外一个是股票数据的缓存

放置Cache目录下面

这里修正一下

咱们来看一下这个缓存接口的具体实现

首先定义了这个缓存接口

用了一个InitCache的方法

通过POST的数解

在并初始化的时候会进行调用

调用它会执行加载缓存的方法

加载缓存我们可以看到

它从数据库里面获取所有有效的股票数据

然后将它进行转换

根据股票ID做转换处理

将结果赋予给DataCache

DataCache它其实是一个Conclude HashMap

现成安全的HashMap

它是定义在负类中

也提供了一些基础的方法

然后附类也提供了一些基础的方法

比如说获取缓存对象

获取所有的Key值

好那咱们再回到股票缓存的实现内

如果要获取缓存信息

这里提供了一个方法

是根据股票ID获取股票编号

这样它就从HashMap里面读取具体的值

不需要再查数据库

这个是股票缓存的实现

那么账户缓存的实现也是一样的

它们都是去继承AppStrike的Cache

然后是初始化缓存数据

这里为了避免缓存和数据库的数据不一致问题

做了一个定时刷新的处理

每10分钟会去刷新一次

接着是加载缓存的具体实现

然后是提供了获取缓存数据的接口

这里是根据账户ID来获取用户ID

好那在下面的章节讲解当中

咱们再去实现交个单业务接口的处理

这里还有一个错误

我们要将service加上助解

纳入是没有容积管理

回到Job

最后这里还要返回一个结果

如果是出现异常

没有正常指定要返回失败

这一讲咱们就完成了Job

调度任务的配置和实现

这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程聚焦于一个股票交易系统中“账户交割单调度任务”的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何使用 XXL-JOB 定时任务框架，结合 Spring Boot 和 MyBatis，完成一个核心业务逻辑：在交易结束后，根据交易数据自动生成交割单，并将数据持久化到数据库。课程内容涵盖了从创建实体类、编写调度任务类、实现业务服务接口，到加载缓存数据等完整开发流程，旨在教授学员如何将定时任务与核心业务逻辑相结合。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程引入，展示课程大纲，明确本节目标是“实现账户交割单调度任务”。
*   **00:16 - 00:30**：讲解交割单的概念，指出其用于记录交易详情，并展示交割单实体类 `TradeAccountSettlement` 的数据库表结构。
*   **00:31 - 00:45**：开始编写调度任务类 `AccountSettlementJob`，展示其继承自 `IJobHandler` 并添加 `@JobHandler` 注解。
*   **00:46 - 01:00**：在 `AccountSettlementJob` 中注入 `AccountSettlementService` 服务，并编写 `execute` 方法的骨架。
*   **01:01 - 01:15**：在 `execute` 方法中调用 `accountSettlementService.generateAccountSettlement(params)` 来生成交割单。
*   **01:16 - 01:30**：展示 `AccountSettlementService` 的实现类 `AccountSettlementServiceImpl`，并注入 `tradeAccountSettlementDao`。
*   **01:31 - 01:45**：在 `AccountSettlementServiceImpl` 中编写 `generateAccountSettlement` 方法，用于处理生成交割单的业务逻辑。
*   **01:46 - 02:00**：在 `AccountSettlementServiceImpl` 中，展示如何通过 `tradeAccountSettlementDao` 获取并处理账户数据。
*   **02:01 - 02:15**：在 `AccountSettlementJob` 中，展示如何处理异常并返回 `FAIL`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：包含章节 `3.4 实现账户股票交割单调度任务`，并列出后续小节。
*   **交割单定义**：交割单用于记录交易详情，分为实物交割和现金交割。
*   **交割单表结构**：包含字段如 `direction` (买卖方向), `tradeAmount` (交易金额), `tradePrice` (交易价格), `taxes` (税费), `commission` (佣金), `status` (状态), `createTime` (创建时间)。

#### 代码关键内容

*   **调度任务类 `AccountSettlementJob`**：
    ```java
    @JobHandler(value = "accountSettlementJob")
    public class AccountSettlementJob extends IJobHandler {
        @Autowired
        private IAccountSettlementService accountSettlementService;

        @Override
        public ReturnT<String> execute(String params) throws Exception {
            try {
                // 生成账户的交割单信息
                accountSettlementService.generateAccountSettlement(params);
                return SUCCESS;
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                return FAIL;
            }
        }
    }
    ```

*   **服务接口 `IAccountSettlementService`**：
    ```java
    public interface IAccountSettlementService {
        void generateAccountSettlement(String param);
    }
    ```

*   **服务实现类 `AccountSettlementServiceImpl`**：
    ```java
    @Service
    public class AccountSettlementServiceImpl implements IAccountSettlementService {
        @Autowired
        private ITradeAccountSettlementDao tradeAccountSettlementDao;

        @Override
        public void generateAccountSettlement(String param) {
            // 业务逻辑实现
        }
    }
    ```

*   **数据访问层 `TradeAccountSettlement` 实体类**：
    ```java
    // 表字段映射
    private String direction; // 买卖方向
    private BigDecimal tradeAmount; // 交易金额
    private BigDecimal tradePrice; // 交易价格
    private BigDecimal taxes; // 税费
    private BigDecimal commission; // 佣金
    private Integer status; // 状态
    private LocalDateTime createTime; // 创建时间
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建调度任务类**
    *   **描述**：讲师在 IDEA 中创建了一个名为 `AccountSettlementJob` 的 Java 类，并将其置于 `com.iteast.bulls.stock.task.finance` 包下。
    *   **演示**：通过 `@JobHandler` 注解将任务命名为 `accountSettlementJob`，并继承 `IJobHandler` 接口。接着，通过 `@Autowired` 注解注入 `IAccountSettlementService` 服务。

*   **场景二：编写调度任务的执行方法**
    *   **描述**：讲师在 `AccountSettlementJob` 类中编写 `execute` 方法，用于处理定时任务的执行逻辑。
    *   **演示**：在 `execute` 方法中，首先记录日志，然后调用 `accountSettlementService.generateAccountSettlement(params)` 方法来生成交割单。最后，根据执行结果返回 `SUCCESS` 或 `FAIL`。

*   **场景三：实现业务服务接口**
    *   **描述**：讲师创建了 `AccountSettlementServiceImpl` 类，用于实现 `IAccountSettlementService` 接口。
    *   **演示**：在 `AccountSettlementServiceImpl` 中，通过 `@Autowired` 注解注入 `ITradeAccountSettlementDao` 数据访问对象，并实现 `generateAccountSettlement` 方法。

*   **场景四：编写数据访问层代码**
    *   **描述**：讲师在 `AccountSettlementServiceImpl` 中编写了 `generateAccountSettlement` 方法，用于处理生成交割单的业务逻辑。
    *   **演示**：通过 `tradeAccountSettlementDao` 获取账户数据，并进行处理。讲师展示了如何使用 `@Autowired` 注解注入 DAO，并在方法中调用 DAO 的方法。

*   **场景五：异常处理**
    *   **描述**：讲师在 `AccountSettlementJob` 的 `execute` 方法中添加了 `try-catch` 块，用于捕获执行过程中可能出现的异常。
    *   **演示**：在 `catch` 块中，记录异常信息，并返回 `FAIL`，以确保任务在出错时能够被正确标记。
