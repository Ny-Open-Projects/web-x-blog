# 980-demo · 生产级 AI Agent 库存调拨示例

> 配套 **mksz980《Java 转 AI 高薪领域必备：从 0 到 1 打通生产级 AI Agent 开发》** 第 5 章。
> 复刻课程「LLM 生成 → 结构化抽取 → MapStruct 转换 → 入库」的完整闭环，可 `mvn` 真跑、可 `docker` 部署。

**部署到其他机器**：见 [DEPLOY.md](DEPLOY.md)（配置全表 / jar 直跑 / compose / MySQL 迁移 / Nacos 脚手架 / 验证清单 / 回滚）。

## 技术栈

| 项 | 版本 | 说明 |
|---|---|---|
| Java | **21 LTS** | 虚拟线程 / Record / 分代 ZGC |
| Spring Boot | **4.1.1** | |
| Spring AI | **2.0.1** | `ChatClient` / `call().entity()`(BeanOutputConverter) / Advisor 链 |
| MapStruct | 1.6.3 | POJO 转换层（复刻 5-15） |
| 持久化 | H2（默认）/ MySQL（prod） | 课程用 MyBatis Plus + MySQL，demo 用 H2+JPA 以便**离线可跑**，字段/转换规则一致 |
| 弹性 | resilience4j | 包裹 LLM 调用（熔断/降级） |
| 可观测 | Actuator + Micrometer | `/actuator/health`、`/actuator/metrics` |
| 链路追踪 | W3C `traceparent`（手写，零新增依赖） | `TraceIdFilter`，与 981/982 统一实现 |

## 模块与博客篇章对应

| 工程模块 | 对应博客 |
|---|---|
| `domain/param/TransferOrderParam` | 5-15 / 5-16（含 LocalDate 坑） |
| `convert/TransferOrderConvert`（MapStruct） | 5-15 |
| `extract/TransferOrderExtractor`（`call().entity()` 抽取） | 5-16「状态机 JSON 数据解析与入库」 |
| `service/TransferOrderServiceImpl` | 5-15 / 5-16 入库节点 |
| `agent/TransferAgent`（工具节点动作） | 5-1 全局状态机 / CreateInventoryTransferNode |
| `controller/TransferController` | 5-14 入库接口业务逻辑 |
| `config/OfflineChatModel` | 离线 Mock（default profile 不联网） |

## 核心坑（必读）

**MapStruct + LocalDate（5-16）**：`param` 与 `model` 的日期**不能都用 `LocalDate`**。
大模型返回的 JSON 日期是字符串，MapStruct 转 `LocalDate` 时会调用 `LocalDate.parse(String)`；
若 `param` 也定义成 `LocalDate`，parse 收到的就是 `LocalDate` 对象而非字符串，直接抛异常。
正确写法：`param.transferDate` 用 `String` 接收，`model.transferDate` 用 `LocalDate`，由 MapStruct 自动转换（见 `TransferOrderConvertTest`）。

## 构建与运行

```bash
# 1. 离线跑通（default profile，MockChatModel 返回固定 JSON，不联网不填 Key）
mvn -q clean verify            # 编译 + 跑抽取/转换单测（离线）
mvn -q spring-boot:run         # 启动，控制台打印「【离线演示闭环】调拨单已创建：1 -> 2」
# 访问 http://localhost:8080/actuator/health  →  {"status":"UP"}
# H2 控制台：http://localhost:8080/h2-console

# 2. 接真实模型（prod profile）
export OPENAI_API_KEY=sk-xxx
export TRANSFER_LLM_BASE_URL=https://api.openai.com/v1   # 或通义 / 本地 vLLM 端点
export TRANSFER_LLM_MODEL=gpt-4o
mvn -q spring-boot:run -Dspring-boot.run.profiles=prod
```

## 容器化

```bash
docker compose up --build      # 默认 default profile（离线），健康检查 http://localhost:8080/actuator/health
# 接真实模型：export OPENAI_API_KEY=... 后再 up
```

## 预期输出（离线）

启动日志：
```
【离线演示闭环】调拨单已创建：1 -> 2
```
H2 中 `bb_transfer_order` / `bb_transfer_order_item` 各插入 1 条。

## 测试

```bash
mvn -q test      # TransferOrderServiceImplTest(10) / TransferAgentTest(5) / TransferControllerTest(5)
                 # / TransferOrderConvertTest / TransferOrderExtractorTest / LlmTokenBudgetTest(4)
                 # / ActuatorSecurityTest(3) / TraceIdFilterTest(6)
                 # / TransferIdempotencyIntegrationTest(4)，共 42 例，离线可跑
```

覆盖重点：LLM 抽取结果非法（明细为空/缺仓库/数量非法/日期坏格式/超长 comment）一律收敛为业务异常
而非 500；抽取服务降级返回 null 时上层判空；控制器入参边界（空 body、超长 body）；W3C `traceparent`
解析与回写（上游链路继承、非法头回退、MDC 清理）；幂等三防线（预查短路 / 唯一索引 / 并发兜底，含 16 线程同键竞态）。

## 生产加固点（已落地）

- ✅ **LLM 结果零信任**：抽取参数全量校验（源/目标仓库非空且不相同、明细非空、qty>0、SKU 非空、
  日期格式 yyyy-MM-dd、超长 comment 截断）——原实现明细为 null 时直接 NPE 变 500。
- ✅ **降级链路判空**：抽取失败返回 null 时上层不 NPE，日志带完整堆栈。
- ✅ **输入防线**：requirement 非空 + 长度 ≤2000；空 body 统一收敛 400。
- ✅ **异常处理**：清理永不触发的死 handler。
- ✅ **依赖清理**：删除零使用的 lombok。
- ✅ **LLM 抽取重试 + 成本上限**：`TransferOrderExtractor` 套 resilience4j 重试（指数退避）+ 熔断；`LlmTokenBudget` 进程内 token 上限（默认 20 万）调用前拦截 / 调用后记账，超限抛 `TokenBudgetExceededException` → 400。
- ✅ **管理端点安全管控**：Spring Security 对 `/actuator/**` 做 Basic Auth，仅 `/actuator/health` 放行（冒烟实测 prometheus=401、health=200）。
- ✅ **链路日志关联**：`TraceIdFilter` 注入 traceId/spanId（MDC + `X-Trace-Id` 响应头），日志格式 `[app,traceId,spanId]`。
- ✅ **分布式链路追踪就绪**：`TraceIdFilter` 解析 W3C `traceparent` 头，上游 traceId 直接继承、本服务续接新 span；
  响应回写 `traceparent` / `X-Trace-Span-Id`，调用方可继续向下游传播（`TraceIdFilterTest` 6 例守护）。
  compose 内置 `tracing` profile 的 Jaeger 后端，见下方「链路追踪」。
- ✅ **幂等控制（重复提交防护）**：`POST /api/transfer/create` 支持 `Idempotency-Key` 头（不传则按需求文本哈希派生键）。
  三道防线：Agent 层**抽取前短路**（命中不调 LLM，省 token 成本）→ Service 层预查 → `request_id` 唯一索引
  兜底并发双写（`TransactionTemplate(REQUIRES_NEW)` 新事务回查既有单）。集成测试含 16 线程同键竞态，只落一单。
  MySQL 部署需按 `DEPLOY.md` 第 8 节补唯一索引。
- 🔧 建议生产再加：配置中心（Nacos 接入脚手架见 `DEPLOY.md` 第 9 节）、公网暴露时的前置网关限流。

## 链路追踪

**当前已就绪（开箱可用，零新增依赖）**

- 入站：请求带 `traceparent`（`00-{trace-id}-{parent-id}-{flags}`）且合法时，本服务**沿用上游 traceId**、
  生成新 spanId 续接链路；头部缺失或非法（全零、长度错、字段数错）时自建新链路。
- 出站：响应头回写 `traceparent`（本服务当前 span）、`X-Trace-Id`、`X-Trace-Span-Id`；`tracestate` 原样透传。
- 日志：traceId / spanId 进 MDC，日志格式 `[app,traceId,spanId]`，一次请求的所有日志行可串联。
- 主动调外部服务时，可用 `TraceIdFilter.currentTraceParent()` 取当前上下文加到出站请求头。

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
