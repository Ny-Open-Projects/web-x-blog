# 32-XXL_JOB集成运用-总结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们对本章内容做个回顾和总结

首先咱们回顾下本章的学习目标

这里我们需要完成四点目标

首先的话呢

要创建和配置好交易调度服务工程

接着的话呢

要实现交购单

持仓利息任务的生成处理

然后咱们要侧重掌握插载的Job

分布式任务调度框架的集成使用

最后要实现获取账户交购单的功能接口

那咱们回顾一下

本章所讲解的具体内容

首先咱们介绍了插载的Job

和主流的分布式任务调度框架

做了一个对比

接着的话呢

咱们实现了插载的Job

管理端的配置和使用

对管理端做了一个启动和验证

下面呢

我们就创建和配置了交易调度服务工程

然后咱们实现了账户股票交购单的调度任务处理

账户股票交购单的调度任务处理

数据量会比较大

大家要注意它的处理效率

在处理方式上要做相应的优化

比如在这里

比如咱们加入了事务

然后应用了缓存功能

减少社口的查询次数

接下来咱们实现了账户持仓利息的调度任务

在融资融券或者是外汇产品交易场景下面

会存在隔夜利息的计算情况

这里我们通过学习

要知道呢

它是如何去

生成处理的

然后咱们对交购单调度任务

还有账户持仓利息的调度任务

进行了揭露配置

XZLJob提供的配置策略也是比较丰富的

大家可以根据自己的业务场景需要

选择不同的运行处理模式

接下来我们是提供了获取交购单的接口数据结构

这里我们定义了相应的PB文件

然后在资金服务里面

我们可以看到

实现了获取账户交购单接口

接着的话呢

在代理服务里面增加了账户交购单接口的转发处理

最后咱们对整体功能做了一个测试和验证

通过XZLJob的管理团

能够比较方便的去管理和维护调度任务

最后咱们再来做一个总结

在实际生产环境当中

往往会存在大量的调度任务

如果是通过Spring或是Spring

它不能够完全满足各种场景的需要

比如说任务执行失败了

咱们想去再次重复执行

或者咱们想去动态修改它的Clone定时任务运行时间

Spring Quartz都是存在比较大的局限

所以我们就采用了分布式的开用框架XZLJob

它是一款比较优秀的开用任务调度处理工具

掌握XZLJob的运用

能够便于我们去管理和维护复杂的调度任务

XZLJob的功能也比较强大

管理端可以支持集群模式的部署

交易调度服务也可以部署多个节点

交易调度服务作为任务的执行器

也可以部署支持多个节点

同时处理不同的任务

咱们之前做配置的时候

对路由策略也做了讲解

这里面的策略选项也是比较灵活的

有兴趣大家可以再做深入的研究

最后咱们是提供了获取账户的交货单接口

整体实现起来交易简单

但是交货单的业务作用来讲却是比较重要的

客户会经常查看交货单

关注自己股票的投资以及资金变化情况

那么交货单成交记录还有资金流水

这三个信息都是重要的数据

并且存有一定的关联性

任何一条数据的计算错误

都会影响整个数据的核对

作为交易平台

所以咱们要充分去考虑和保障好数据的准确性

不能出现误差

这三个核心数据一定要做到统一一致

好

这一讲就是对本章内容的回复和总结

那这一讲的内容咱们就到此结束

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程是关于在金融交易系统中，如何使用 **XXL-JOB** 分布式任务调度框架来实现“账户持仓利息”等核心业务的定时计算任务。课程内容从介绍 XXL-JOB 框架开始，逐步深入到具体的开发实现，包括创建调度任务、定义数据结构、编写服务逻辑、接入管理端以及最终的功能验证。课程强调了在金融系统中数据准确性的重要性，并通过代码演示了如何将业务逻辑封装到 XXL-JOB 任务中，以及如何通过缓存机制优化性能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中精确获取视频的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:30**：**课程总览与目标**。讲师介绍了本章的核心目标：实现一个基于 XXL-JOB 的“账户持仓利息”定时计算任务，并强调了数据准确性的重要性。
*   **00:30 - 01:00**：**XXL-JOB 框架介绍**。讲师对比了主流的分布式任务调度框架（如 Quartz、Elastic-Job），并重点介绍了 XXL-JOB 的特点，如管理端支持集群部署、任务路由策略灵活等。
*   **01:00 - 02:00**：**创建配置与服务工程**。讲师演示了如何创建一个用于调度任务的 Spring Boot 项目，并配置 XXL-JOB 的管理端和执行器。
*   **02:00 - 03:30**：**实现核心业务逻辑**。
    *   **02:00 - 02:30**：**定义数据结构**。讲师展示了 `TradeAccountSettlement` 实体类，用于存储交割单数据。
    *   **02:30 - 03:00**：**创建服务类**。讲师编写了 `AccountSettlementServiceImpl` 服务类，用于处理具体的业务逻辑。
    *   **03:00 - 03:30**：**实现持仓利息计算**。讲师编写了 `AccountPositionInterestServiceImpl` 服务类，其中包含了核心的利息计算逻辑。
*   **03:30 - 04:30**：**接入管理端与功能验证**。
    *   **03:30 - 04:00**：**接入管理端**。讲师演示了如何将任务注册到 XXL-JOB 的管理界面（`http://127.0.0.1:8080/xxl-job-admin`），并展示了管理界面的运行报表。
    *   **04:00 - 04:30**：**功能验证**。讲师通过模拟调用，验证了任务是否能正常执行并返回预期结果。
*   **04:30 - 05:00**：**总结与展望**。讲师总结了 XXL-JOB 在金融系统中的优势，并指出在实际开发中需要特别关注数据的准确性和一致性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节列表**：清晰地列出了本章的各个小节，如“3.1 XXL-JOB介绍”、“3.4 实现账户股票交割单调度任务”等。
    *   **总结部分**：强调了 XXL-JOB 的强大功能和在金融系统中的应用价值。
    *   **数据结构定义**：在 `3.4` 节中，定义了 `TradeAccountSettlement` 实体类的属性，包括交割日期、证券代码、成交价格等。
    *   **服务类代码**：在 `3.5` 节中，展示了 `AccountPositionInterestServiceImpl` 类的代码，其中包含了一个关键的业务方法 `generateAccountPositionInterest`。
    *   **管理界面截图**：在 `3.3` 节中，展示了 XXL-JOB 管理界面的截图，包括“运行报表”、“日均分布图”和“成功比例图”等。

*   **代码关键内容**：
    *   **实体类 `TradeAccountSettlement`**：
        ```java
        // 属性包括：交割日期、证券代码、成交价格、成交数量等
        ```
    *   **服务类 `AccountSettlementServiceImpl`**：
        ```java
        @Service
        @Log4j2
        public class AccountSettlementServiceImpl implements IAccountSettlementService {
            @Autowired
            private ITradeDealDao tradeDealDao;
        }
        ```
    *   **核心服务类 `AccountPositionInterestServiceImpl`**：
        ```java
        @Service
        @Log4j2
        public class AccountPositionInterestServiceImpl implements IAccountPositionInterestService {
            @Autowired
            private ITradePositionDao tradePositionDao;
            private Integer interest = 2; // 持仓利息率（万分比）
        }
        ```
    *   **核心业务方法**：
        ```java
        try {
            // 生成账户持仓利息
            accountPositionInterestService.generateAccountPositionInterest(param);
            return SUCCESS;
        } catch (Exception e) {
            log.error(e.getMessage(), e);
        }
        return FAIL;
        ```
    *   **数据结构 `GetAccountSettlementRespData`**：
        ```java
        message GetAccountSettlementRespData {
            int64 id = 1;
            int64 userId = 2;
            int64 dealId = 3;
        }
        ```
    *   **服务端处理类 `StockFinanceProcessor`**：
        ```java
        public class StockFinanceProcessor extends AbstractStockProcessor implements IBaseStockProcessor {
            @GrpcClient("grpc-finance-server")
            private StockFinanceServiceGrpc.StockFinanceServiceBlockingStub stockFinanceServiceStub;
            
            @Override
            public void processRequest(ChannelHandlerContext channelHandlerContext, StockMessage stockMessage) {
                switch (stockMessage.getStockHead().getRequestType()) {
                    case GET_FINANCE_OVERVIEW:
                        getFinanceOverview(channelHandlerContext, stockMessage);
                }
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：XXL-JOB 管理界面演示**（时间点：约 03:30）
    *   **描述**：讲师在屏幕上展示了 XXL-JOB 的管理界面，地址为 `http://127.0.0.1:8080/xxl-job-admin`。界面中显示了“运行报表”、“日均分布图”和“成功比例图”等关键指标。讲师指出，这些数据是通过之前调试过的任务生成的，用于监控任务的执行情况和成功率。

*   **场景二：核心业务逻辑代码演示**（时间点：约 02:30 - 03:30）
    *   **描述**：讲师在代码编辑器中逐步演示了如何实现“账户持仓利息”计算任务。
        1.  首先，创建了 `AccountPositionInterestServiceImpl` 服务类，并注入了数据访问层接口 `ITradePositionDao`。
        2.  然后，在 `generateAccountPositionInterest` 方法中，编写了核心的业务逻辑，包括调用 `tradePositionDao` 获取数据，并计算利息。
        3.  最后，将该服务类注册为 XXL-JOB 任务，并在管理端配置好执行参数。

*   **场景三：功能验证与数据准确性强调**（时间点：约 04:00 - 04:30）
    *   **描述**：讲师通过模拟调用，验证了任务的执行结果。在“总结”部分，讲师特别强调了在金融系统中数据准确性的极端重要性。他指出，任何一条数据的计算错误，都可能影响整个数据的核对，因此在开发过程中必须充分考虑数据的准确性和一致性。

*   **场景四：缓存机制优化**（时间点：约 02:30）
    *   **描述**：在讲解“交割单”数据时，讲师提到为了提高效率，避免每次查询数据库，系统会使用缓存。他展示了 `AccountsCache` 类的代码，该类用于缓存账户数据，并设置了每十分钟刷新一次的策略。
