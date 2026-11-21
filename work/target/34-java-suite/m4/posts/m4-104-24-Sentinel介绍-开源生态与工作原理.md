---
title: "Sentinel 工作原理与 Dashboard 实战：Slot Chain 插槽链、RT/异常比例降级与 QPS/线程数限流"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, Sentinel]
---

# Sentinel 工作原理与 Dashboard 实战：Slot Chain 插槽链、RT/异常比例降级与 QPS/线程数限流

上一篇读完 Sentinel 的身世与特性，本篇把剩下两块补齐：一是开源生态与工作原理——它靠什么接入 Dubbo、Spring Cloud 这些主流框架，请求进来又沿着怎样一条插槽链流转；二是上手实操——把 Dashboard 1.6.2 控制台拉起来，用阿里官方的四个 demo 依次演示平均响应时间降级、异常比例降级、QPS 限流与并发线程数限流，再到控制台里看每一组规则的实时曲线。

## 先给结论

- 开源生态四向覆盖：适配层有 Sentinel Dubbo Adapter（限流降级）、gRPC Adapter、Spring Cloud 全家（Web MVC、Cloud Netflix、Spring Cloud Gateway）与 RocketMQ；网格侧对接 Istio；动态规则支持 Nacos、Redis、ZooKeeper、Apollo。
- 节点规模决定方案：十几个到几十个微服务，Spring Cloud 一套就足够；节点数量特别巨大再考虑 Istio 的网格治理方案。
- 工作原理一句话：资源对应 Entry，Entry 创建时生成 Slot Chain 插槽链——NodeSelectorSlot 收调用路径、ClusterBuilderSlot 存统计、StatisticSlot 记运行时指标、FlowSlot 限流、DegradeSlot 熔断、AuthoritySlot 黑白名单、SystemSlot 控总入口流量；SlotChainBuilder 走 SPI 扩展，插槽可插拔、可自定义。
- Dashboard 1.6.2 一条命令拉起，还能把自己也监控进来；默认账号密码都是 sentinel，可用 -Dsentinel.dashboard.auth.* 修改；四大功能：机器列表与健康、秒级实时监控（单机加集群聚合）、规则统一管理与推送、鉴权。
- RT 降级：平均响应时间超阈值（count，毫秒）进入准降级，接下来 1s 内持续 5 个请求（QPS >= 5）且 RT 都超阈值，timeWindow（秒）内调用自动熔断抛 DegradeException；RT 统计上限默认 4900ms，用 -Dcsp.sentinel.statistic.max.rt 调整。
- 限流两策略数字差异巨大：QPS 限 20，通过 QPS 就稳定在 20 左右；并发线程限 20，通过 QPS 实测可到 957——QPS 是查询速率维度，线程数是实际工作线程维度，不要混用。

## 生态全景与 Slot Chain：请求进来走哪条链

Sentinel 的生态图分三块看。左侧与顶部是适配层：gRPC 有专门的 adapter；Dubbo 通过 Sentinel Dubbo Adapter 获得限流与降级能力；Service Mesh 一侧对接的是服务网格治理，Istio 是专业化服务治理组件，自带一系列工具，微服务节点特别多时可以考虑；右侧是 Spring Cloud 体系——Web MVC、Cloud Netflix、Spring Cloud Gateway，再加上 RocketMQ 消息队列；最底层是动态规则数据源，Nacos、Redis、ZooKeeper、Apollo 都能对接。支持面铺得宽，大多数场景都能拿 Sentinel 做熔断降级。

工作原理的核心是 Entry 与 Slot Chain：每个资源对应一个资源名和一个 Entry，Entry 可以通过对主流框架的适配自动创建，也可以通过注解或 API 显式创建；Entry 创建的同时会生成一条插槽链，链上插槽各司其职：

```mermaid
flowchart LR
    E[Entry<br/>资源进入] --> N[NodeSelectorSlot<br/>收集调用路径]
    N --> C[ClusterBuilderSlot<br/>存储资源统计信息]
    C --> S[StatisticSlot<br/>记录 runtime 指标]
    S --> F[FlowSlot<br/>流量控制]
    F --> D[DegradeSlot<br/>熔断降级]
    D --> A[AuthoritySlot<br/>黑白名单]
    A --> Y[SystemSlot<br/>控制总入口流量]
```

逐个看职责：NodeSelectorSlot 把资源调用路径以树状结构存储起来，用于按调用路径做限流降级——比如用户服务和交易服务各有限流保护策略，路径不同规则不同；ClusterBuilderSlot 存储资源统计信息与调用者信息，像 RT 响应时间、QPS、线程数，这些是多维度限流和降级的依据；StatisticSlot 记录统计不同维度的运行时指标监控信息；FlowSlot 根据预设的限流规则结合前面的统计状态做流控；DegradeSlot 按统计信息与预设规则做熔断降级；AuthoritySlot 按配置的黑白名单与调用来源做控制；SystemSlot 根据系统状态（如 load1）控制总入口流量。

这套设计是典型的插槽式：每个组件只负责具体功能，统计的归统计、限流的归限流，彼此独立、支持可插拔——不需要的插槽移除即可，不影响系统原有运行的稳定性。想加自定义能力，比如认证环节要按 VIP 设定不同权限，写一个 MyCustomSlot 认证插槽，通过 SlotChainBuilder 这个 SPI 接口扩展，编排进链路就能生效，对原有系统冲击很小。本章最后归纳的三件事也值得记住：了解 Sentinel 的基本知识与功能作用；了解它的功能特性、相比 Hystrix 这类限流熔断组件的特点；了解工作原理与请求处理流程——配置规则、排查线上问题都靠它。

## Dashboard 控制台：一条命令拉起的监控中枢

Sentinel 控制台包含四项功能：查看机器列表以及健康情况——收集客户端发来的心跳包，判断机器是否在线；监控——通过客户端暴露的监控 API 定期拉取并聚合应用监控信息，支持单机和集群聚合，能做到秒级实时监控；规则管理和推送——多个节点接入后由控制台统一管理、统一推送规则；鉴权——生产环境的必备项，每个团队按实际情况定制。

从 GitHub 下载控制台，课程沿用讲义当时的最新版本 1.6.2。启动只需要一条命令：

```bash
java -Dserver.port=8090 -Dcsp.sentinel.dashboard.server=localhost:8090 \
     -jar sentinel-dashboard-1.6.2.jar
```

两个参数各有含义：-Dserver.port 指定控制台端口 8090；-Dcsp.sentinel.dashboard.server 指向自己，也就是把控制台自身也注册进 Dashboard——自己把自己监控起来。启动完成后直接访问 http://127.0.0.1:8090，不需要附带 context path。默认登录账号和密码都是 sentinel，想修改通过参数变量调整即可：

```bash
-Dsentinel.dashboard.auth.username=sentinel
-Dsentinel.dashboard.auth.password=123456
```

登录进去，首页已经有一个应用在报心跳——正是 sentinel 自己；点开实时监控，能看到通过 QPS、拒绝 QPS 两条曲线和响应时间表格。左侧菜单包括簇点链路、流控规则、降级规则、热点规则等，后面的演示就逐个落到这些菜单上。业务应用接入控制台有两种方式：启动时通过 -D 变量传参，或者直接在代码里设置属性——官方 demo 里用的是后者：

```java
System.setProperty("csp.sentinel.dashboard.server", "127.0.0.1:8090");
```

## 降级演示：平均响应时间与异常比例

降级有两个策略：平均响应时间与异常比例。先看平均响应时间：当资源的平均响应时间超过阈值（DegradeRule 的 count，毫秒为单位），资源进入准降级状态——注意不是立刻降级，而是准备降级；如果接下来 1s 内持续进入 5 个请求（QPS >= 5），它们的 RT 都持续超过阈值，那么在接下来的时间窗口（timeWindow，秒为单位）内，对这个方法的调用都会自动熔断，抛出 DegradeException。QPS >= 5 是基准下限——一个系统连这个量级都撑不住，本来就谈不上保护价值。另外 Sentinel 默认统计的 RT 上限是 4900ms：不到 5 秒是因为预留了传输、网络这类开销的时间差，超出部分一律按 4900ms 计，需要变更时通过 -Dcsp.sentinel.statistic.max.rt=xxx 修改。

数一下这笔账就更直观：一段业务自身处理 3 秒、远程调用 2 秒，单个请求总耗时 5 秒；阈值配 5 秒，请求能正常通过；阈值配 3 秒，请求必然超标，叠加 QPS 条件就触发平均响应时间降级。

演示模块 sentinel-demo 建在 bulls-stock 下面，pom 里加 Sentinel 依赖不用写版本——dependencyManagement 已统一管理。规则初始化是官方 demo 的写法：

```java
private static void initDegradeRule() {
    List<DegradeRule> rules = new ArrayList<>();
    DegradeRule rule = new DegradeRule();
    rule.setResource(KEY);
    rule.setCount(100);                              // 平均响应时间阈值 100ms，便于触发
    rule.setGrade(RuleConstant.DEGRADE_GRADE_RT);    // 降级策略：按平均响应时间
    rule.setTimeWindow(10);                          // 触发熔断后 10 秒恢复
    rules.add(rule);
    DegradeRuleManager.loadRules(rules);
}
```

策略常量要标清楚：RuleConstant 里 DEGRADE_GRADE_RT、DEGRADE_GRADE_EXCEPTION_RATIO、DEGRADE_GRADE_EXCEPTION_COUNT 对应 0、1、2 三种降级维度，DEGRADE_DEFAULT_MIN_REQUEST_AMOUNT 的 5 就是那个基准请求数。RtDegradeDemo 的主流程：tick 线程负责打印耗时与监控日志；100 个线程循环模拟调用——先 sleep 5ms 保持处理有序，再 SphU.entry(KEY) 获取令牌，pass 计数加一，然后 sleep 600ms 模拟业务耗时（远超 100ms 阈值），拿到异常就 block 计数，最后 total 加一并 entry.exit() 释放；计数用 AtomicInteger，不会出线程安全问题。

运行结果与规则严丝合缝：一开始放行了 104 个请求，随后触发降级开始阻断；等 10 秒时间窗过后恢复，放行一批（约 100 QPS），又因为每个线程都要睡 600ms、远超 100ms 上限再次降级——降级与恢复随时间窗交替进行。切到 Dashboard 实时监控，这个节奏看得非常直观；簇点链路里也能看到资源的调用情况。这组 demo 是手工方式接入 Sentinel，并没有与 Spring Boot 集成，后面项目学习中再讲整合方案。

异常比例的规则条件：当资源的每秒请求量 >= 5（与上面一致），并且每秒异常总数占通过量的比值超过阈值，资源进入降级状态，在接下来的时间窗口（秒为单位）内对该方法的调用都会自动返回。异常比例阈值范围 0.0 到 1.0，代表 0% 到 100%。举例：5 个请求里出现 2 个超时异常，错误率 40%；阈值配 30% 就触发降级，调大到 50% 则安然无恙。

ExceptionRatioDegradeDemo 与 RT demo 结构一致，区别只在策略与阈值：setGrade(DEGRADE_GRADE_EXCEPTION_RATIO)、setCount(0.1)（10%，特意配小方便触发，配太大要么等很久要么制造很多异常）、setTimeWindow(10)。业务逻辑更有意思：单线程 while(true) 死循环不停调资源，count 累加到偶数位就抛 RuntimeException——每两次请求抛一次异常，异常率轻松越过比例上限。控制台按秒打印 oneSecondTotal、oneSecondBlock、oneSecondBizException 三个指标：先放行 5 个（正好是基准数），异常一出现立刻降级、全部阻断；10 秒后恢复，恢复的瞬间又触发、再降级。演示中还遇到一个小插曲：Dashboard 上刷不到应用，提示没有找到存活的节点——把 demo 进程重启、重新登录就能看到 com.itcast.bulls.sentinel.demo.ExceptionRatioDegradeDemo；实时监控的波线图里，10 秒放行两个请求，第二个偶数位触发异常，达到 10% 上限又降级，列表里每一秒的通过、拒绝、异常数据都有明细。

## 限流演示：QPS 与并发线程数的数字差异

流量控制的原理：监控应用流量的 QPS 或并发线程数等指标，达到指定阈值时对流量进行控制，避免被瞬时的流量高峰冲垮——峰值请求往往是平常的数倍，控制不住就容易崩溃，限流功能由此保障应用的高可用性。

QPS 策略的官方 demo 是 FlowQpsDemo，规则写法与降级同构：

```java
private static void initFlowQpsRule() {
    List<FlowRule> rules = new ArrayList<>();
    FlowRule rule = new FlowRule();
    rule.setResource(KEY);
    rule.setCount(20);    // set limit qps to 20
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);   // 选定限流策略，基于 QPS
    rule.setLimitApp("default");
    rules.add(rule);
    FlowRuleManager.loadRules(rules);
}
```

demo 循环建立 32 个线程跑长任务，验证 QPS 峰值能否被压在 20 以内。运行下来，初期因为规则加载有延迟，控制得不算严格，之后基本稳定在 20 QPS 之内；CPU 计算、线程切换会带来 1 到 2 个的波动，属正常范围。Dashboard 实时监控里通过 QPS 稳定在 20 左右，拒绝 QPS 单独一条曲线，响应时间很快——资源内部没有做重逻辑。

讲并发线程数限流之前，先把 QPS 与 TPS 分清：QPS（Queries Per Second）是单个接口一次查询的交付时间；TPS（Transactions Per Second）是一笔事务的处理时间。一个页面请求包含用户查询、订单查询、库存查询三个接口——三个接口全部完成的总时间记入 TPS，单个接口的耗时记入 QPS。所以 TPS 的概念大于 QPS：一个 TPS 可能包含多个 QPS，反过来一个 QPS 不会包含多个 TPS，被问到时别搞错包含关系。

再看并发线程数：服务里开线程池接收请求，开 6 个线程不代表只能处理 6 个请求——线程池提升的是吞吐能力，6 个线程可能同时处理 10 个请求；线程数少了吞吐能力随之下降。QPS 的数量可以远大于并发线程数，因为并发线程数是实际干活的线程。线程也不能滥开：CPU 上下文切换有开销，一般 CPU 有超线程机制，4 个核心开 8 到 10 个线程左右就足够，再多没有明显提升，反而加重 CPU 负担。

并发线程数限流的官方 demo 是 FlowThreadDemo，规则把 grade 换成线程维度：

```java
rule.setResource("methodA");
// set limit concurrent thread for 'methodA' to 20
rule.setCount(20);
rule.setGrade(RuleConstant.FLOW_GRADE_THREAD);
rule.setLimitApp("default");
```

也就是 methodA 这个资源最多允许 20 个线程同时处理，超出的被限制。simulateTraffic 起 threadCount 个线程死循环调 methodA；业务逻辑里 methodA 埋点进入后还嵌套调用了 methodB，两个资源都做了记录。运行结果：通过的线程数稳定控制在 20 左右，符合规则要求。但 Dashboard 上的数字很有说服力——FlowThreadDemo 的通过 QPS 达到 957，拒绝 QPS 也不少：虽然只有 20 个线程，处理能力却远超 20 QPS，视机器性能可以到上千。同样是 20 这个数，QPS 维度最多放行 20 个/秒，线程维度可能放行上千——两套策略的差别在实际应用里一定要分清，把 QPS 当线程数去控制，数字上会差出一个量级。

## 小结

本篇把 Sentinel 的「是什么」补成了「怎么跑、怎么用」：生态上，Dubbo/gRPC/Spring Cloud/RocketMQ 的适配层加 Istio 的网格方案加四大配置中心的动态规则，决定了选型路径——小规模集群 Spring Cloud 一套够用；原理上，Entry 与 Slot Chain 是核心，七个插槽从收路径、存统计、记指标到限流、熔断、黑白名单、系统保护各管一段，SPI 扩展让自定义插槽即插即用；实操上，Dashboard 1.6.2 一条命令拉起并自带自我监控，sentinel/sentinel 登录后即可看到秒级实时曲线。四组官方 demo 两两成对：降级的平均响应时间（100ms 阈值触发准降级，1s 内 5 个请求超标熔断 10 秒）与异常比例（每秒 5 个请求且异常占比超 10% 降级），限流的 QPS（限 20 稳在 20）与并发线程（限 20 线程跑出 957 QPS）——后面这组数字对比是全篇最值得记住的一笔，它提醒你规则维度必须与业务语义对齐。课程给的延伸路径是官方 wiki 文档，而真正的整合姿势（Spring Boot 集成、注解式埋点）留到后续项目实战里展开。
