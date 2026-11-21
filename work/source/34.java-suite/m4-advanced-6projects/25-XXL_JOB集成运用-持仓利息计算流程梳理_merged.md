# 25-XXL_JOB集成运用-持仓利息计算流程梳理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来这一讲咱们去学习账户时长利息调度任务的处理实现

这个在股票产品下面一般不会出现

除非是做了融资融券或者是外汇产品交易会存在隔夜利息计算的情况

在这里咱们来学习它的实现处理逻辑

首先我们要去创建任务调度器回到工程当中

咱们在Job的包下面创建一个新的任务

这里先创建一个新的纸包

Open in terminal

可以点点Make DIR

这个纸包就叫Position

专门负责持仓的调度处理任务

我们创建一个新的类New Job Class

名称就叫Account Position Interest Job

Job的配置之前我们实现交个单的时候已经做了讲解

我们从讲习当中直接copy进来

这里要定义一个Job Handle

给它一个名称

然后增加Service租捡

这个是Job Handle

这是日子插件的租捡

让它导入进来

然后这个是持仓利息的业务实现接口

这个业务接口稍后咱们再做实现

接着的话是Execute的方法

这里会去调用业务接口

生成账户的持仓利息

接下来我们去创建业务接口

在Service下面

右键New

定义名称

Position

Interest

Service

Implement

添加Service租捡

添加日子插件的租捡

接下来我们从讲习当中

将必要的接口属性

以及辅助方法copy进来

然后我们去定义一个

生成账户仓位利息的方法

Generate

Account

Position

Interest

设置参数

这里要开启事务环

Consectional

配置No Backflow

针对于所有的异常

这里咱们就不需要去指定

Consectional Manage

因为它要去修改仓位的利息

这里采用的是交易数据源

修改的是仓位里面的利息属性

并不需要生成统计报表

所以咱们在这里不需要去指定业务数据源

采用默认的交易数据源就可以

然后添加注释

这是生成账户的仓位利息

将接口抽取出来

右键Refact

Extract

这里选择Innovate

Package呢

放在Service下面

Innovate名称以I开头

去掉Implement

点击Refact

这里要勾选Generate Account Position

然后点击Refact

好 咱们可以看到

已经生成了账户持仓利息的业务接口

那咱们就来对这个接口做具体的实现

进入到实现内容里面

在这里当中

增加日日Process In

加内名Copy

方法名Copy

首先我们去获取当天的格式化日期

具体格式呢

就是年月再加上日

通过日期我们是要获取指定仓位的数据

Date

Utils

Get

Command Date

然后第一步

我们要根据日期去获取有效的持仓数据

获取所有有效的持仓数据

这里要注意一下

持仓利息的调度任务

它只会更新当天和之前的仓位数据

并且不能重复更新计算利息

在这里要定义一个集合

CAD Positions

CAD Positions

传递Command Date

当天的格式化日期

那咱们来结合这个数据层接口来看一下

这里是获取所有有效的持仓数据

而且每次抓取是限制2000条

我们看一下它的具体伺候

在Cosmab上面找寻一下

可以看到它伺候的直线逻辑

它会根据持仓利息的更新时间去获取所有有效的仓位记录

这里我们给大家画一个图

便于大家理解

比如说这个呢是仓位记录员的项目

这里我们会有一个时间

这个时间呢就是Interest Time

它是利息更新时间

那比如今天是5月2号

这里有不同的日期持仓数据

比如说是有5月1日的持仓

还有5月2号的持仓

每条仓位数据它生成的时候

利息更新时间默认是为NOW的

也就是

Interest Time了

它默认是为NOW

5月2号它的利息更新时间呢

也是为NOW

这里扣一下

那么咱们在5月2号去执行

仓位利息更新的调度任务

根据这个Circle的查询

它会找到Time为NOW

或者利息更新时间要小于咱们指定的日期

为什么条件要这么去限定

那大家结合这个流程

应该可以看到

大家应该能理解清楚

调度任务在5月2号执行的时候

它会将5月2号的持仓记录做一个更新

因为它的Interest Time为NOW

也会将之前如果没有更新的仓位记录呢

统一做一个更新

如果之前没有更新的

它的Interest Time也是为NOW

那么一并会将所有的持仓记录都找出来

那更新完成之后呢

这里Interest Time它就会产生变化

就会变成5月2号的日期

5月2日

那同样之前5月1日的持仓做了更新之后

它的时间也会变成5月2号

这样即便仓位利息更新的调度任务多次执行

因为它们的时间已经产生了变化

根据这个Circle做判断的时候呢

它必须要小于或者是为空

这两个条件呢

都不符合

所以呢就不会再次更新已经计算过利息的仓位

那如果是5月3号呢

这些持仓记录又会再次

找寻出来

我们知道利息呢

每天都要产生并且进行累加的

所以在5月3号的时候呢

它们会将原有的持仓记录找寻出来

然后再做一个累加更新

好这一块呢就是仓位利息更新调度任务的处理实现流程

大家要理解清楚

那回到代码当中

回到刚才的实现内

咱们再梳理一下下面的处理流程

第二步呢

根据

股票ID

对数据

做汇总处理

目的是要减少

Circle

查询次数

提升处理效率

第三步

根据股票ID

建立所有的

持仓数据

第四步

要获取最新的股票

行情报价

拿到行情报价之后

要去计算

仓位市值

仓位市值等于持仓数量

再乘以股票

最新价

接着的话呢要去计算

仓位利息

这个利息呢等于

市值

再乘以利息率

接着的话呢要去累加

持仓

利息

然后第八步

要去写入

持仓

利息的

更新时间

防止

重复计算

这个时间呢就是

领取STAND

咱们在流程当中所讲的利息更新时间

最后

就是要对数据做一个更新

更新

利息的

计算结果

以及

利息的

更新时间

好那这一讲咱们对持仓利息的更新整个流程做了梳理和讲解

这一讲的内容

咱们就先讲到这里

下一讲咱们再来做具体的实现

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个金融交易系统中“账户持仓利息调度任务”的实现过程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何使用 XXL-JOB 定时任务框架，结合 Spring Boot 和 MyBatis，来实现一个核心的业务逻辑：根据指定日期，计算并更新所有符合条件的持仓账户的利息。整个过程包括创建任务调度器、定义服务接口、实现服务层逻辑、编写数据访问层的 SQL 映射文件，并最终在服务层中整合调用。视频重点在于展示代码结构、关键方法的实现以及数据流的处理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 编辑器中展示课程大纲，定位到当前章节“3.5 实现账户持仓利息调度任务”，并说明本节将讲解整体实现逻辑。
*   **00:00:05 - 00:00:15**：讲师切换到 IntelliJ IDEA，打开项目 `bulls-stock`，并导航至 `AccountPositionInterestJob` 类，展示任务调度器的定义。
*   **00:00:15 - 00:00:30**：讲师在 `AccountPositionInterestJob` 类中，展示其继承自 `IJobHandler` 并被 `@JobHandler` 注解，以及通过 `@Autowired` 注入 `IaccountPositionInterestService` 服务接口。
*   **00:00:30 - 00:00:45**：讲师将光标移动到 `execute` 方法，展示其核心逻辑：调用服务层方法 `generateAccountPositionInterest`，并根据执行结果返回 `SUCCESS` 或 `FAIL`。
*   **00:00:45 - 00:01:00**：讲师切换到服务实现类 `AccountPositionInterestServiceImpl`，并展示其 `@Service` 和 `@Log4j2` 注解。
*   **00:01:00 - 00:01:15**：讲师在 `generateAccountPositionInterest` 方法中，首先添加日志记录，并获取当前日期的格式化字符串 `fmtDay`。
*   **00:01:15 - 00:01:30**：讲师调用 `tradePositionDao.findAllValidPositionsByInterestTime(fmtDay)` 方法，获取所有符合条件的持仓记录。
*   **00:01:30 - 00:01:45**：讲师对获取到的持仓列表进行分组，按股票 ID (`stockId`) 分组，以便后续按股票进行利息计算。
*   **00:01:45 - 00:02:00**：讲师展示 `TradePositionMapper.xml` 文件中的 SQL 映射语句，该语句用于查询符合条件的持仓记录，并限制返回数量为 2000 条。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **课程大纲**：在 Typora 中显示，包含章节 3.5 “实现账户持仓利息调度任务”。
    *   **代码注释**：在 `AccountPositionInterestServiceImpl` 类中，有清晰的中文注释，如“// 获取当天的格式化日期，yyyyMMdd”、“// 1. 获取所有有效的持仓数据”、“// 2. 根据股票ID做汇总”、“// 3. 根据股票ID，遍历所有仓位数据”。

*   **关键代码**：

    *   **任务调度器 (`AccountPositionInterestJob`)**
        ```java
        @JobHandler(value="accountPositionInterestJob")
        @Service
        @Log4j2
        public class AccountPositionInterestJob extends IJobHandler {
            @Autowired
            private IAccountPositionInterestService accountPositionInterestService;
            
            @Override
            public Return<String> execute(String param) throws Exception {
                log.info("Process in AccountPositionInterestJob.execute method, param: " + param);
                try {
                    // 生成账户持仓利息
                    accountPositionInterestService.generateAccountPositionInterest(param);
                    return SUCCESS;
                } catch (Exception e) {
                    log.error(e.getMessage(), e);
                    return FAIL;
                }
            }
        }
        ```

    *   **服务接口 (`IaccountPositionInterestService`)**
        ```java
        @Service
        @Log4j2
        public class AccountPositionInterestServiceImpl {
            // ... 其他注解和成员变量 ...
            
            @Transactional(rollbackFor = Exception.class)
            public void generateAccountPositionInterest(String param) {
                log.info("Process in AccountPositionInterestServiceImpl.generateAccountPositionInterest method.");
                // ... 业务逻辑 ...
            }
        }
        ```

    *   **数据访问层 SQL (`TradePositionMapper.xml`)**
        ```xml
        <select id="findAllValidPositionsByInterestTime" resultMap="BaseResultMap">
            select
            from t_trade_position
            where status = 0
              and interestTime is null
              or interestTime = #{interestTime}
            limit 2000
        </select>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：任务调度器的创建与配置**
    *   **描述**：讲师首先在 `AccountPositionInterestJob` 类中，通过 `@JobHandler` 注解指定任务名称，并通过 `@Autowired` 注入服务接口。这表明该类是一个 XXL-JOB 的任务处理器，负责调用具体的业务逻辑。

*   **场景二：服务层的实现与事务管理**
    *   **描述**：讲师在 `AccountPositionInterestServiceImpl` 类中，使用 `@Transactional` 注解对 `generateAccountPositionInterest` 方法进行事务管理，确保在发生异常时能够回滚数据库操作。这体现了对数据一致性的重视。

*   **场景三：数据查询与分组处理**
    *   **描述**：讲师在服务层中，首先通过 `tradePositionDao.findAllValidPositionsByInterestTime(fmtDay)` 查询符合条件的持仓数据。然后，使用 Java 8 的 Stream API 对数据进行分组，按 `stockId` 分组，以便后续对每个股票的持仓进行独立处理。

*   **场景四：SQL 映射文件的编写**
    *   **描述**：讲师展示了 `TradePositionMapper.xml` 文件中的 SQL 语句。该语句查询 `t_trade_position` 表中 `status` 为 0 且 `interestTime` 为空或等于传入参数的记录，并限制返回 2000 条。这确保了查询的效率和数据量的可控性。

---

以上是根据视频画面进行的详细技术分析。
