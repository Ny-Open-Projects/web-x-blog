---
title: "XXL-JOB 落地：交易调度服务、交割单生成与持仓利息计算、接口链路与验证"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, XXL-JOB]
---

# XXL-JOB 落地：交易调度服务、交割单生成与持仓利息计算、接口链路与验证

第 3 章分布式任务调度从选型进入落地：新建交易调度服务 bulls-stock-task 接入 XXL-JOB 执行器，实现账户交割单与持仓利息两个调度任务并接入管理端，补齐"获取账户交割单"的完整接口链路（Netty 对外、gRPC 对内、资金服务实现、代理服务转发），最后在管理端用"执行"操作逐项验证。

## 先给结论

- 交易调度服务 bulls-stock-task：新建模块，在常规依赖（Spring Boot、Nacos、MyBatis 双数据源、Redis、gRPC）之外引入 com.xuxueli:xxl-job-core 2.1.0；XXL-JOB 是分离式设计，admin 调度管理后台与 executor 执行器两部分独立、相互注册。
- 执行器接入三件套：bootstrap-dev.yml 的 xxl.job 配置（admin 地址、appname 取服务名、logretentiondays 为 -1 不清日志、access_token 权限控制）、XxlJobConfig 里 @Bean(initMethod = "start", destroyMethod = "destroy") 初始化 XxlJobSpringExecutor、启动类开启服务注册/事务/Spring 调度。
- 交割单记录股票与资金变动（成交记录侧重成交数据），含交割日期、证券代码、成交价格等 19 项；AccountSettlementJob 继承 IJobHandler，参数是精确到天的日期，某天生成失败可次日带参重跑修复；按成交记录 ID 防止重复生成。
- 双数据源事务是最容易踩的坑：交割单任务 @Transactional 必须指定 transactionManager = "bizSystemTransactionManager"（报表数据在业务库，双数据源默认指向交易数据源）；不用并行流，异步执行会让事务不能真正生效。
- 持仓利息对应融资融券、外汇的隔夜利息场景：市值 = 持仓数量 × 最新价，利息 = 市值 × 利息率 ÷ 10000（利率万分比，配置 2 即万分之二）；靠 interestTime 为空或小于执行日的查询条件天然防重，算完写入当天日期。
- 接口链路：Netty 对外传起止时间，gRPC 对内多带 accountId；资金服务把时间戳转格式化日期后查库，代理服务 switch 增加 GET_ACCOUNT_SETTLEMENTS 分支转发。验证全部通过：交割单生成 4 条、利息与更新时间写入、接口返回 4 条数据 ID 285 到 288 与库中一致。

## 交易调度服务：XXL-JOB 执行器接入

新建模块 bulls-stock-task，依赖从讲义拷贝：Spring Boot、Nacos 服务注册发现、公用的数据层/服务层/工具/实体依赖、缓存依赖、gRPC 依赖，最后是 XXL-JOB 核心依赖，2.1.0 为当前最新版本：

```xml
<dependency>
    <groupId>com.xuxueli</groupId>
    <artifactId>xxl-job-core</artifactId>
    <version>${xxl.job.version}</version>
</dependency>
```

配置文件两个：基准的 bootstrap.yml 指定读取哪一套环境（package.environment 变量），开发环境的 bootstrap-dev.yml 里放服务基本配置、RocketMQ 消息配置（主题 stocktask-1，每个服务的主题名称保持唯一）、双数据源配置，以及最关键的分布式调度任务配置：

```yaml
xxl:
  job:
    admin:
      addresses: http://127.0.0.1:8080/xxl-job-admin
    executor:
      appname: ${spring.application.name}
      ip: ${xxl.job.executor.ip}
      port: ${xxl.job.executor.port}
      logpath: /data/aplogs/xxl-job/jobhandler
      logretentiondays: -1
      access_token: ${xxl.job.executor.accessToken}
```

admin 是管理后台地址，多节点时把所有地址逗号分隔全部加入；课程侧重集成运用，指向单个后台节点即可。executor 里 appname 就是服务名称，ip 可以不配（默认读本机 IP），port 是执行器监听端口，logpath 是日志路径，logretentiondays 为 -1 表示日志不清除，要做权限控制时配置 access_token。

配置类 XxlJobConfig 负责把属性注入执行器：

```java
@Configuration
public class XxlJobConfig {

    @Bean(initMethod = "start", destroyMethod = "destroy")
    public XxlJobSpringExecutor xxlJobExecutor() {
        XxlJobSpringExecutor xxlJobSpringExecutor = new XxlJobSpringExecutor();
        xxlJobSpringExecutor.setAdminAddresses(adminAddresses);
        xxlJobSpringExecutor.setAppName(appName);
        xxlJobSpringExecutor.setIp(ip);
        xxlJobSpringExecutor.setPort(port);
        xxlJobSpringExecutor.setAccessToken(accessToken);
        xxlJobSpringExecutor.setLogPath(logPath);
        xxlJobSpringExecutor.setLogRetentionDays(logRetentionDays);
        return xxlJobSpringExecutor;
    }
}
```

initMethod 与 destroyMethod 是关键：bean 初始化时调用执行器的 start，销毁时调用 destroy；执行器通过异步线程处理任务，服务关闭时要关闭任务、释放资源。日志用 Lombok 的 @Log4j2 插件，配置类里加一条打印便于确认初始化正常。其余组件快速补齐：双数据源（基于 MyBatis）、Redis、线程池的配置类从已实现代码引入，DAO 数据层接口（biz 与 trade）和 mapper 文件一并拷入。启动类上加 @EnableDiscoveryClient、@EnableTransactionManagement、@EnableScheduling，@ComponentScan 指向基础包。

## 交割单与持仓利息：两个调度任务的实现

先分清交割单和成交记录：交割单用来记录交割的具体交易情况，交割概念来源于期货，分实物交割和现金交割；查询一般以电子表格输出，内容含交割日期、证券代码、成交价格等 19 项，是股民的交割依据，一般以它计算成本、核对盈亏。成交记录侧重股票成交的数据，交割单侧重股票和资金变动的数据；成交记录生成时就保存了佣金，交割单处理时不用再追溯。交割单实体里有用户信息、成交记录 ID（每笔交割单对应一笔成交记录）、交易时间、股票 ID 与代码、币种、买卖方向、交易金额、数量、价格、税费、佣金、状态：税费是印花税、过户费、交易规费累加在一起（实际券商分开记录），无效状态标示为 1。

交割单任务 AccountSettlementJob 放在 job 包下的 finance 子包（处理资金服务相关调度任务），执行时间一般放在收盘之后，比如每晚十点，用 Cron 配置。创建 XXL-JOB 调度任务要继承抽象类 IJobHandler 并实现抽象方法 execute（父类主要提供初始化、销毁、execute 三个方法）：

```java
@JobHandler(value = "accountSettlementJob")
@Service
@Log4j2
public class AccountSettlementJob extends IJobHandler {

    @Autowired
    private IAccountSettlementService accountSettlementService;

    @Override
    public ReturnT<String> execute(String params) throws Exception {
        log.info("Process in AccountSettlementJob.execute method, param: " + params);
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

@JobHandler 的名称与类名保持一致；调度可能出现失败，外围 try-catch 兜底，正常返回 SUCCESS、异常返回 FAIL。业务实现 AccountSettlementServiceImpl 注入成交记录 DAO、账户交割单 DAO 和两个缓存（AccountsCache、StocksCache，减少数据库查询次数）。缓存继承同一个抽象缓存父类：@PostConstruct 在 bean 初始化时执行加载缓存，DataCache 是线程安全的 ConcurrentHashMap，定义在父类中；股票缓存按股票 ID 缓存编号，账户缓存按账户 ID 缓存用户 ID，读取时直接从 HashMap 取值不再查库；为避免与数据库不一致，每 10 分钟定时刷新。

业务方法三步走。第一步按日期取成交记录：param 传日期（如 2020-05-01，精确到天），参数为空默认取当天记录；不为空则把日期拆成两个时间点（开始拼零点、结束拼 23 点 59 分 59 秒），交给数据层按时间范围查询。第二步流式遍历，每条成交记录生成一条交割单：

```java
@Override
@Transactional(rollbackFor = Exception.class, transactionManager = "bizSystemTransactionManager")
public void generateAccountSettlement(String param) {
    List<TradeDeal> tradeDeals = getTradeDeals(param);
    if (null != tradeDeals && !tradeDeals.isEmpty()) {
        log.info("get trade deal size: " + tradeDeals.size());
        tradeDeals.stream().forEach(tradeDeal -> processTradeDeal(tradeDeal));
    }
}
```

第三步 processTradeDeal 单条处理：先按成交记录 ID 查交割单是否已存在，存在则输出错误日志返回（防重复生成）；然后创建交割单对象，设置交易行为信息（股票、买卖方向、币种，用户 ID 与股票代码从缓存取）和交易资金信息（佣金、税费、成交价格、成交数量、成交金额），插入交割单表。

两个容易踩的坑值得强调。一是事务管理器：内部遍历有大量数据库写入，加事务提升处理效率，但调度服务是双数据源，默认指向交易数据源，报表数据统一放在业务库，必须显式指定业务数据源的事务管理器防止错乱。二是不用并行流：并行流异步执行，事务不能真正生效。另外 param 只传具体某一天、不会跨天，由维护人员在管理后台控制；某天生成失败，第二天可通过参数触发上一天的交割单生成，做修复处理。

持仓利息任务是另一个场景：股票产品一般不涉及，除非做了融资融券或外汇交易，才有隔夜利息计算。结构上与交割单任务同构：AccountPositionInterestJob 放在 position 子包，继承 IJobHandler、@JobHandler(value = "accountPositionInterestJob")，调用业务接口 generateAccountPositionInterest，SUCCESS/FAIL 收尾。业务方法的 @Transactional 不需要指定事务管理器：它修改的是仓位利息属性，走默认的交易数据源，不生成统计报表。

实现流程九步：取当天格式化日期（yyyyMMdd）→ 按日期取所有有效持仓 → 按股票 ID 分组汇总（减少 SQL 查询次数）→ 遍历持仓 → 获取最新行情报价 → 算仓位市值（数量 × 最新价）→ 计算并累加利息 → 写入利息更新时间 → 更新计算结果与更新时间。核心代码：

```java
@Override
@Transactional(rollbackFor = Exception.class)
public void generateAccountPositionInterest(String param) {
    String fmtDay = DateUtils.getFmtDay();
    List<TradePosition> tradePositions = tradePositionDao.findAllValidPositionsByInterestTime(fmtDay);
    Map<Long, List<TradePosition>> groupByPositions = tradePositions.stream()
            .collect(Collectors.groupingBy(TradePosition::getStockId));
    groupByPositions.forEach((stockId, positions) -> {
        if (null != positions && positions.size() > 0) {
            TradeStockQuoteLast quoteLast = getTradeStockQuoteLast(stockId);
            if (null != quoteLast) {
                positions.forEach(pos -> {
                    Long totalMarketValue = MathUtils.mul(pos.getVolume(), quoteLast.getLastClosePrice());
                    Long posInterest = MathUtils.divLong(MathUtils.mul(totalMarketValue, interest), 10000);
                    pos.setInterest(isNullToZero(pos.getInterest()) + posInterest);
                    pos.setInterestTime(fmtDay);
                    tradePositionDao.updateInterest(pos);
                });
            }
        }
    });
}
```

行情报价必须存在，否则无法计算市值和利息；累加时用 isNullToZero 把已有利息的 null 转 0，防止空指针异常。除以 10000 是因为利息率是万分比：利率设置为 2 代表万分之二，市值乘利率后再除以一万才是正确利息。查询条件是防重复计算的核心：

```xml
<select id="findAllValidPositionsByInterestTime" resultMap="BaseResultMap">
    select ... from t_trade_position
    where status = 0
      and (interest_time is null or interest_time &lt; #{interestTime})
    limit 2000
</select>
```

持仓数据生成时利息更新时间（interestTime）默认为空。假设 5 月 2 号执行任务：利息更新时间为空或小于 5 月 2 号的持仓都会被查出来（含当天新建和历史未更新的），更新后 interestTime 写成 5 月 2 号；再次执行时这些记录既不为空也不小于当天，不会重复计算利息。到 5 月 3 号执行日期后移，这批记录又满足条件，被再次查出累加利息，利息每天产生、逐日累加。每次抓取限制 2000 条。

## 管理端接入与获取交割单接口链路

任务要接入管理端才能被调度。先把工程配置里的管理后台地址端口改成 8080，启动任务调度服务，确认日志无异常。执行器管理里配置执行器：名称"交易平台调度任务"，注册方式勾选自动，AppName 必须与工程配置一致（appname 取的是 spring.application.name），否则无法正常注册；注册成功且服务在线后，机器地址显示为绿色。默认执行器无法删除，系统必须保留一个执行器。

任务管理里新增两个任务，配置差异如下：

| 配置项 | 交割单任务 | 持仓利息任务 |
| --- | --- | --- |
| 任务描述 | 生成账户交割单信息 | 生成账户持仓利息 |
| JobHandler | accountSettlementJob | accountPositionInterestJob |
| 运行模式 | BEAN（与 Spring Boot 集成，以 bean 方式注入运行） | BEAN |
| 阻塞处理策略 | 单机串行 | 丢弃后续调度（防止对当前任务执行产生影响） |
| Cron | 每分钟一次（便于测试验证） | 每天凌晨两到三点间每五分钟一次（结算时间之后调度） |

路由策略决定多节点时任务落在哪台机器：第一个、最后一个、轮询、随机、故障转移、忙碌转移，按场景选择。阻塞处理策略处理"任务未执行完又再次触发"：单机串行继续等待，丢弃后续调度放弃之后的触发，覆盖之前调度终止之前的任务、执行新的调度。

接着打通"获取账户交割单"接口。数据结构分两层定义：Netty 对外的 StockMessage.proto 增加 GetAccountSettlementData（开始时间 timeStart、结束时间 timeEnd）与 GetAccountSettlementRespData（status、message 加 repeated 交割单集合）；StockMessage 的请求数据包占序号 7，ResponseMessage 的返回数据包列表占序号 9。gRPC 对内的 StockFinanceService.proto 返回信息与 Netty 基本一致，请求多带交易账户 ID：

```protobuf
// 获取账户交割单数据接口
rpc getAccountSettlement(GetAccountSettlementRequest) returns (GetAccountSettlementResponse);

message GetAccountSettlementRequest {
    int64 accountId = 1;   // 交易账户 ID
    int64 timeStart = 2;
    int64 timeEnd = 3;
}
```

通过 proto-grpc.bat 脚本生成 gRPC 代码，再生成 Netty 代码，两边 GetAccountSettlementRequest 均成功生成（gRPC 侧继承 GeneratedMessageV3）。

资金服务实现两层。gRPC 层 GrpcStockFinanceService#getAccountSettlement：调业务层拿交割单数据，判空后遍历复制、包装成传输结构输出。数据复制用自定义的 BeanAssistant.copyNotNullProps 而非 proto 自带复制，避免 proto 属性复制时空指针异常；日期字段复制时排除，转为 long 长整型传递。业务层 getTradeAccountSettlements 把时间戳转成格式化日期再查库，两层方法都要声明抛出 ComponentException：

```java
public List<TradeAccountSettlement> getTradeAccountSettlements(long accountId, long timeStart, long timeEnd) throws ComponentException {
    String strTimeStart = DateUtils.getFmtDateByTime(timeStart);   // 时间戳转 yyyy-MM-dd HH:mm:ss
    String strTimeEnd = DateUtils.getFmtDateByTime(timeEnd);
    return tradeAccountSettlementDao.getSettlementsByTimeRange(accountId, strTimeStart, strTimeEnd);
}
```

代理服务侧与之前交易服务处理器的改造思路一样：StockFinanceProcessor 是资金服务处理器，@GrpcClient 注入资金服务 stub，processRequest 按请求类型分发，支持多个接口转发（获取账户资金总览、获取账户交割单）。PB 结构文件 StockHead 的 RequestType 枚举增加 GET_ACCOUNT_SETTLEMENTS：

```java
switch (stockMessage.getStockHead().getRequestType()) {
    case GET_FINANCE_OVERVIEW:
        getFinanceOverview(channelHandlerContext, stockMessage);
        break;
    case GET_ACCOUNT_SETTLEMENTS:
        getAccountSettlements(channelHandlerContext, stockMessage);
        break;
    default:
        log.error("Process in StockFinanceProcessor.processRequest method => Not Match RequestType!");
}
```

getAccountSettlements 方法里：从报文取出起止时间，构造 gRPC 请求（accountId 由 getUserAccountId 从上下文获取），调用资金服务，遍历返回集合复制属性，组装 ResponseMessage 写回客户端。

## 功能验证：管理端执行与接口调用

管理后台任务列表的操作栏提供三个操作：执行（只执行一次）、启动（按 Cron 配置的时间定时执行）、日志。

**交割单任务验证。** 先查后台数据做比对：5 月 27 号的成交记录共 4 条，交割单表此时还是空的。任务管理里点"执行"，输入任务参数日期 2020-05-27，点击保存。执行完成后查库：生成 4 条交割单数据，关联的 dealId 是 2672 到 2675，与成交记录 ID 一致。

**持仓利息任务验证。** 先看仓位数据：两条仓位记录，最新一条 5 月 22 号生成，持仓利息与利息更新时间都是空的。点"执行"，输入日期 2020-05-27，提示执行成功。刷新数据库：持仓利息成功生成，利息更新时间也成功写入，防重机制与计算逻辑同时得到确认。

**交割单接口验证。** 模拟客户端先加接口调用：Test 目录下 BusinessHandler 末尾增加获取账户交割单的调用，传时间范围；交割单创建时间是 5 月 28 号，时间范围就调整为 5 月 28 号。再改交互菜单：ClientBoundHandler 的 showMenu 方法增加输出指令 8（Get Account Settlement，获取账户交割单），指令处理同步补上。启动代理服务、资金服务、交易服务并登录，调用指令 8：客户端收到服务端数据共 4 条，详情打印 ID 285 到 288；数据库交割单表同样 4 条、ID 285 到 288，两边一致，接口链路处理成功。三个验证分别覆盖了调度任务的单次触发与参数化重跑、利息计算与防重、以及客户端报文到资金服务查询的完整链路。

## 小结

这一章把 XXL-JOB 从选型推进到全链路落地：交易调度服务以执行器身份接入调度中心，交割单任务按天生成股票与资金变动的单据、持仓利息任务按万分比利率逐日累加隔夜利息，两个任务通过执行器注册与任务配置纳入统一调度；接口侧 Netty 与 gRPC 双结构定义、资金服务按时间范围查询、代理服务按 RequestType 分发转发，客户端也能拿到交割单数据。最有价值的两个细节是双数据源下显式指定事务管理器、用利息更新时间做查询条件天然防重：前者保证报表数据正确落库，后者让任务放心按 Cron 反复触发。至此调度任务、接入配置、接口链路与功能验证全部走通。
