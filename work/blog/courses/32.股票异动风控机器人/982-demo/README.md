# 982-demo · 股票异动风控 Bot（生产级工程示例）

> 配套课程：**mksz982《AI Agent 股票异动风控机器人实战（支持美股+A股）》**
> 技术栈：**Java 21 + Spring Boot 4.1.1 + Spring AI 2.0.1**（2026-10 最新稳定线）
> 链路追踪：W3C `traceparent`（手写 `TraceIdFilter`，零新增依赖，与 980/981 统一实现）
> 定位：课程「感知→决策→执行」风控闭环的**可部署最小实现**，不是玩具 demo。

**部署到其他机器**：见 [DEPLOY.md](DEPLOY.md)（配置全表 / jar 直跑 / compose / Nacos 脚手架 / 验证清单 / 回滚）。

---

## 1. 它实现了什么（对应博客篇章）

| 博客主题 | 工程模块 |
|---|---|
| 行情接入 | `provider/QuoteProvider` + `MockQuoteProvider`(离线) / `RealQuoteProvider`(prod 可切真实 API) |
| 风控规则引擎设计 | `engine/RiskRule` + `PriceVolatilityRule` / `VolumeSpikeRule` + `RuleEngine`（可插拔） |
| 异动判定与告警 | `service/RiskEvaluationService`（熔断保护）+ `domain/RiskAlert` |
| Agent 问答（查某票风险） | `agent/RiskQueryAgent`：`ChatClient` + `@Tool`（`ToolCallingAdvisor` 驱动工具循环） |
| 周期扫描 | `scheduler/RiskScanScheduler`（Java 21 虚拟线程） |
| 对外接口 / 健康 | `controller/RiskController` + Actuator `/actuator/health`、`/actuator/metrics`、`/actuator/prometheus` |

行情源按 profile 切换：default(离线) 用 `MockQuoteProvider`，prod 用 `RealQuoteProvider`（真实端点 `risk.quote.api-url`，prod 配置）。每个 tick 自带 market 字段（A= A股 / US= 美股）。

---

## 2. 环境要求

- **JDK 21**（LTS，Spring AI 2.0 基线）
- **Maven 3.9+**
- 真实模型（可选）：`SPRING_AI_OPENAI_API_KEY`（或通义/DeepSeek 端点，改 `application.yml` 的 starter 即可）

---

## 3. 构建与运行

### 3.1 离线 mock 模式（默认，不联网、不填 Key）
```bash
mvn -q clean package
java -jar target/982-demo-1.0.0.jar
# 或： mvn -q spring-boot:run -Dspring-boot.run.profiles=default
```
启动后验证：
```bash
curl -s -X POST "localhost:8080/api/risk/evaluate?symbol=600519"   # 命中涨跌幅异动（POST）
curl -s localhost:8080/api/risk/scan                        # 全市场扫描
curl -s localhost:8080/actuator/health                      # {"status":"UP"}
```

### 3.2 真实模型模式（prod profile）
```bash
export SPRING_PROFILES_ACTIVE=prod
export SPRING_AI_OPENAI_API_KEY=sk-xxx
mvn -q spring-boot:run
# Agent 问答： curl -s "localhost:8080/api/risk/query?q=600519 现在风险高吗"
```

### 3.3 容器化部署
```bash
docker compose up --build          # prod profile，需注入 SPRING_AI_OPENAI_API_KEY
docker compose up --build -e SPRING_PROFILES_ACTIVE=default   # 离线演示
```
镜像基于 `eclipse-temurin:21-jre`、非 root 运行、内置 `HEALTHCHECK`。

---

## 4. 测试
```bash
mvn -q test      # RuleEngineTest / RiskEvaluationServiceTest / RiskQueryAgentMockTest
                 # / RiskControllerTest / RiskBotApplicationTest / RiskBotProdProfileTest
                 # / LlmTokenBudgetTest / ActuatorSecurityTest
                 # / RealQuoteProviderTest(2) / TraceIdFilterTest(6)，共 38 例，离线可跑
```
其中 `RiskBotProdProfileTest` 以 prod profile 拉起完整上下文，守护「Mock/Real 双 bean 歧义」这类
只在真实 profile 下暴露的启动级故障。`mvn verify` 另跑 GitHub Actions CI（`.github/workflows/ci.yml`）。

---

## 5. 生产加固点（已落地 / 建议）

- ✅ **多 profile 配置**：密钥走环境变量，不落库。
- ✅ **可观测**：Actuator + Micrometer（Prometheus 抓取 `/actuator/prometheus`）。
- ✅ **弹性**：`RiskEvaluationService` 规则引擎评估用 resilience4j 熔断降级（异常带完整堆栈入日志，风控场景不静默漏报）。
- ✅ **输入防线**：`StockTick` 紧凑构造器 fail-fast；symbol 语义化校验（A股 6 位数字 / 美股代码）；`VolumeSpikeRule` 启动期校验 ratio 非 NaN 非负。
- ✅ **外部调用超时**：`RealQuoteProvider` 的 `RestClient` 显式配置连接 3s / 读取 5s，失败降级为空不影响扫描链。
- ✅ **行情网关重试 + 配置外置**：`RealQuoteProvider` 真实拉取套 resilience4j 重试（指数退避，`risk.quote.retry.max-attempts`/`wait-ms`），
  瞬时抖动自愈、重试耗尽降级为空不影响扫描链；地址与超时全部外置为 `risk.quote.api-url` / `connect-timeout-ms` / `read-timeout-ms`（均 env 驱动）。
- ✅ **高并发**：虚拟线程调度扫描，单轮异常不中断后续轮次。
- ✅ **周期调度真正生效**：`@EnableScheduling` + 虚拟线程 `TaskScheduler`。曾因缺 `@EnableScheduling`
  导致 `@Scheduled` 静默失效（启动预扫正常、周期扫描从未触发，只有冒烟实测才暴露）；修复后实测
  30s 周期告警两轮、virtual 线程承载、零 ERROR。
- ✅ **容器化 + CI**：Dockerfile / compose / GitHub Actions。
- ✅ **管理端点安全管控**：Spring Security 对 `/actuator/**`（含 prometheus/metrics）做 Basic Auth，仅 `/actuator/health` 放行；消除裸暴露风险（冒烟实测 prometheus=401、health=200）。
- ✅ **LLM 问答重试**：`RiskQueryAgent` 的模型调用套 resilience4j 重试（指数退避），瞬时抖动自愈；异常仍降级返回离线文案不崩。
- ✅ **Token 成本上限**：进程内 `LlmTokenBudget`（默认 20 万 token）调用前拦截、调用后记账，离线模型 `usage=null` 安全记 0，超限抛 `TokenBudgetExceededException`，问答链路捕获后返回降级文案（HTTP 200，不中断服务）。
- ✅ **链路日志关联**：`TraceIdFilter` 为每次请求注入 traceId/spanId 到 MDC 并回写 `X-Trace-Id` 响应头；日志格式 `[app,traceId,spanId]`，一次请求全链路可串。
- ✅ **分布式链路追踪就绪**：`TraceIdFilter` 解析 W3C `traceparent` 头，上游 traceId 直接继承、本服务续接新 span；
  响应回写 `traceparent` / `X-Trace-Span-Id`，调用方可继续向下游传播（`TraceIdFilterTest` 6 例守护）。
  compose 内置 `tracing` profile 的 Jaeger 后端，见下方「链路追踪」。
- 🔧 建议生产再加：配置中心接入脚手架已写入 `DEPLOY.md` 第 8 节（nacos-config-spring-boot-starter + bootstrap.yml + dataId 规划），按需执行；公网暴露时的前置网关限流。

---

## 6. 链路追踪

**当前已就绪（开箱可用，零新增依赖）**

- 入站：请求带 `traceparent`（`00-{trace-id}-{parent-id}-{flags}`）且合法时，本服务**沿用上游 traceId**、
  生成新 spanId 续接链路；头部缺失或非法（全零、长度错、字段数错）时自建新链路。
- 出站：响应头回写 `traceparent`（本服务当前 span）、`X-Trace-Id`、`X-Trace-Span-Id`；`tracestate` 原样透传。
- 日志：traceId / spanId 进 MDC，日志格式 `[app,traceId,spanId]`，一次请求的所有日志行可串联。
- 主动调外部行情接口时，可用 `TraceIdFilter.currentTraceParent()` 取当前上下文加到出站请求头。

**启动 Jaeger（opt-in）**

```bash
docker compose --profile tracing up -d      # Jaeger UI: http://localhost:16686
docker compose --profile tracing down       # 停止
```

默认 `docker compose up` **不会**启动 Jaeger（`profiles` 隔离），不影响既有部署。

**要真正把 span 导出到 Jaeger，还差两步**（本工程为保持离线构建可复现，刻意没把 exporter 放进依赖里）：

```xml
<dependency>
  <groupId>io.micrometer</groupId>
  <artifactId>micrometer-tracing-bridge-otel</artifactId>
</dependency>
<dependency>
  <groupId>io.opentelemetry</groupId>
  <artifactId>opentelemetry-exporter-otlp</artifactId>
</dependency>
```

```yaml
management:
  tracing:
    sampling:
      probability: 1.0
  otlp:
    tracing:
      endpoint: http://localhost:4318/v1/traces
```

> Boot 4.1.1 已移除 tracing 自动配置，接入上述依赖后还需按官方文档补 `ObservationRegistry` + `Tracer` 装配，
> 或直接改用 Spring Boot 3.x（981 用的 3.5.7 仍自带自动配置）。

---

## 7. 与课程/博客的衔接
润色后的 mksz982 博客相关篇章在【小结】处引用本工程模块（如 `RiskEvaluationService`、
`RiskQueryAgent`），形成「读博客 → 跑工程」闭环。工程 API 名（`ChatClient` / `@Tool` /
`ToolCallingAdvisor` / `MessageChatMemoryAdvisor`）与博客所述 Spring AI 2.0 一致。
