# 981-demo：多 Agent 自主决策旅游规划（可生产部署）

复刻慕课实战课程《多 Agent + Skills + SpringAI 构建自主决策智能体》第 10–13 章的核心形态：
**主管 Agent 通过 A2A 协议发现并调度远程团队成员 Agent，成员 Agent 通过 Toolkit 挂载 MCP 风格工具**。
这不是玩具：默认离线可跑（不联网、不填 Key），prod 模式切真实模型与 Nacos，带熔断、Actuator、容器化与 CI。

**部署到其他机器**：见 [DEPLOY.md](DEPLOY.md)（配置全表 / jar 直跑 / compose / Nacos 双模式 / 验证清单 / 回滚）。

## 技术栈

| 层 | 选型 | 说明 |
|---|---|---|
| 语言/运行时 | **Java 21**（LTS，2026 生产使用率第一） | 课程要求 JDK 17+ |
| Agent 框架 | **AgentScope Java 2.0.3**（阿里开源，Maven Central） | 课程同款框架（Jmanus 架构） |
| 模型 | `agentscope-extensions-model-dashscope`（qwen-plus） | default 用离线规则模型，不调 API |
| 注册中心 | Nacos 3.1（prod） | 课程 11-2/11-3 的 `NacosAgentCardResolver` 同角色 |
| Web/运维 | Spring Boot 3.5 + Actuator + Micrometer + resilience4j | 课程 13-2/13-3 |
| 链路追踪 | W3C `traceparent`（手写，零新增依赖） | `TraceIdFilter`，与 980/982 统一实现 |

> 课程录制时用的是 AgentScope 1.x API（`ReActAgent`/`A2aAgent`/`Toolkit`/`Msg`/`TextBlock`）。
> 本工程按 **2.0.3 当前稳定版** 实现（`ReActAgent.builder()`、`Toolkit.registerTool()`、
> `ModelRegistry` 字符串 id 如 `dashscope:qwen-plus`），概念与博客一一对应。

## 快速开始

```bash
# 离线演示：不需要任何 API Key
mvn spring-boot:run
```

```bash
# 触发主管 Agent 统筹成员（景点路由 / 路线路由均有规则决策）
curl -X POST http://localhost:8080/api/travel/plan \
  -H 'Content-Type: application/json' \
  -d '{"requirement":"帮我规划杭州三天行程，含景点和路线"}'

# 查看当前发现的团队成员（课程 11-3）
curl http://localhost:8080/api/travel/members

# 成员 A2A 能力发现（课程 11-2）
curl http://localhost:8080/a2a/RouteMakingAgent/.well-known/agent.json

# 以 A2A JSON-RPC 远程调用成员（课程 11-4）
curl -X POST http://localhost:8080/a2a/RouteMakingAgent \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":"1","method":"message/send","params":{"message":{"role":"user","parts":[{"type":"text","text":"西湖到灵隐寺怎么走"}]}}}'

# 健康检查与指标
curl http://localhost:8080/actuator/health
curl http://localhost:8080/actuator/prometheus
```

验证全部离线逻辑（CI 同款，不需 Key）：

```bash
mvn test
```

## 架构

```
用户 ──POST /api/travel/plan──▶ TravelManagerAgent（主管，ReActAgent）
                                   │ 第一轮：按需求选择成员工具（离线规则 / 真实 LLM 决策）
                                   ▼
                    ┌──────── ask_route_making_agent ────────┐
                    │                                        ▼
                    │              ask_attraction_agent   RouteMakingAgent（远程成员）
                    │                      │                · Toolkit 挂载百度地图 MCP 风格工具
                    │                      ▼                · map_directions / map_weather / map_geocode
                    │           AttractionAgent           A2A HTTP 端点（默认进程内通道）
                    │           · search_attractions        · GET /.well-known/agent.json
                    ▼                                      · POST JSON-RPC message/send
          SupervisorTools（resilience4j 熔断兜底）                ▲
                    │         Nacos 注册/发现（prod）───────────┘
                    ▼
         第二轮：汇总成员结果 → 返回行程规划
```

关键类：

| 类 | 职责 | 对应课程 |
|---|---|---|
| `agent/TeamMembers` | 成员 ReActAgent + Toolkit 工具挂载 | 11-6、12-5 |
| `agent/SupervisorTools` | 成员即工具（Agent as Tool）+ 熔断 | 11-4、11-7 |
| `agent/SupervisorAgent` | 主管决策（分发/汇总） | 11-1、11-7 |
| `a2a/A2aEndpointController` | 成员 A2A 端点（Card + JSON-RPC） | 11-2 |
| `a2a/NacosAgentRegistry` | Nacos 注册与解析 | 11-2、11-3 |
| `model/OfflineChatModel` | 离线规则模型（`Model` 接口实现） | ReAct 循环机制 |
| `web/TravelController` | 用户交互接口 | 13-2 |

## 离线 ↔ 真实切换

| 配置（`application.yml` / `application-prod.yml`） | default | prod |
|---|---|---|
| `app.agent.model-mode` | `offline`（规则模型） | `dashscope`（ModelRegistry 解析 id） |
| `app.agent.discovery` | `in-process`（进程内通道） | `nacos`（Nacos 注册中心） |
| Key | 不需要 | `DASHSCOPE_API_KEY` |

```bash
DASHSCOPE_API_KEY=sk-xxx mvn spring-boot:run -Dspring-boot.run.profiles=prod
```

## 生产部署

```bash
mvn clean package
docker build -t 981-demo:1.0.0 .

# 完整形态（含 Nacos）：主管与成员分容器部署，成员启动即注册到 Nacos
docker compose up -d
docker run -d --name nacos -p 8848:8848 -p 9848:9848 nacos/nacos-server:v3.1.0   # 9848 是 nacos-client 3.x 的 gRPC 端口，漏映射会注册失败 \
  -e MODE=standalone -e NACOS_AUTH_ENABLE=false
docker run -d --name 981-demo -p 8080:8080 \
  -e SPRING_PROFILES_ACTIVE=prod -e AGENTSCOPE_NACOS_SERVER_ADDR=nacos:8848 \
  -e DASHSCOPE_API_KEY=sk-xxx 981-demo:1.0.0
# 容器/多网卡场景：显式指定成员注册到 Nacos 的对外 IP（否则回退本机 IP，跨机不可达）
#   -e APP_AGENT_ADVERTISE_IP=192.168.1.11
# 完整编排（含 advertise-ip 透传）见 docker-compose.yml 的 agent-app.environment
```

- 健康检查：`GET /actuator/health`（Dockerfile 可加 HEALTHCHECK）
- 指标：`GET /actuator/prometheus`（团队调用次数、成员延迟，接 Prometheus/Grafana）
- CI：`.github/workflows/ci.yml`（JDK 21 + `mvn verify`，离线测试无需 Key）

## 测试

```bash
mvn -q test      # SupervisorToolsTest(5) / TravelControllerValidationTest(6) / TravelPlanningFlowTest(5)
                 # / ActuatorSecurityTest(3) / A2aHttpAgentTransportRetryTest(2)
                 # / LlmTokenBudgetTest(5) / TokenBudgetModelTest(2) / RouteMakingToolsTest(5)
                 # / TraceIdFilterTest(6)，共 39 例，离线可跑
```

覆盖重点：主管→成员链路（Nacos 回落 / 远程调用失败降级 / 成员未注册抛异常 / 本地优先不碰 Nacos）；
控制器入参校验；A2A 协议行为。

## 生产加固点（已落地）

- ✅ **Nacos 3.x 适配**：3.x 已移除 `NamingService.shutdown()`，优雅停机改为对注册实例逐条 deregister。
- ✅ **注册中心故障不杀死应用**：Nacos 客户端创建失败/注册异常均降级本地运行（`@PostConstruct`
  抛异常 = 上下文启动失败，曾让 prod 一启动就挂）。
- ✅ **prod 链路三重瘫痪修复**：注册表装配统一按 `app.agent.discovery`（不再看 profile），
  消除「prod profile + in-process discovery + Nacos bean 无人消费」的组合断层。
- ✅ **A2A 远程调用显式超时**：连接 3s / 读取 10s；card 失败不缓存 unknown；200 响应内嵌
  JSON-RPC error 也识别。
- ✅ **协议正确性**：JSON-RPC 响应 id 回带请求 id；未知方法 -32601；空 task -32602；
  AgentCard 委托 `TeamMembers` 单一数据源。
- ✅ **工具入参零信任**：`@ToolParam.required` 只生成 JSON Schema、调用时不强校验，入口一律判空。
- ✅ **熔断只护远程通道**：resilience4j 仅包裹 `A2aHttpAgentTransport`，进程内成员失败直接暴露
  （代码缺陷不伪装成网络抖动）。
- ✅ **Agent 循环预算显式化**：ReActAgent `maxIters` 显式配置（`app.agent.max-iters`），
  新增 `advertise-ip` 支持容器/多网卡注册（docker-compose 已透传 `APP_AGENT_ADVERTISE_IP`）。
- ✅ **A2A 远程调用重试**：`A2aHttpAgentTransport` 套 resilience4j 重试（指数退避），协议层业务错误（内嵌 JSON-RPC error）不重试、其余瞬时异常自愈。
- ✅ **管理端点安全管控**：Spring Security 对 `/actuator/**` 做 Basic Auth，仅 `/actuator/health` 放行（冒烟实测 prometheus=401、health=200）。
- ✅ **链路日志关联**：`TraceIdFilter` 注入 traceId/spanId（MDC + `X-Trace-Id` 响应头），日志格式 `[app,traceId,spanId]`。
- ✅ **百度地图 Key 凭证管理**：`baidu.map.api-key` 走环境变量 `BAIDU_MAP_API_KEY`，代码零硬编码；
  Key 缺失时启动告警并走离线桩，不因缺凭证启动失败（`RouteMakingToolsTest` 5 例守护）。
- ✅ **Token 成本上限**：`TokenBudgetModel` 装饰器包裹 AgentScope 模型——装饰器位于 `ReActAgent` 内部循环之中，
  因此能拿到每一轮 `ChatResponse.getUsage()` 自记账（默认 20 万 token），超限抛 `TokenBudgetExceededException` → 400。
  离线模型 `usage` 缺失时按 input+output 回退记账，真实模式经 `ModelRegistry.resolve` 解析后同样包裹。
- ✅ **分布式链路追踪就绪**：`TraceIdFilter` 解析 W3C `traceparent` 头，上游 traceId 直接继承、本服务续接新 span；
  响应回写 `traceparent` / `X-Trace-Span-Id`，调用方可继续向下游传播（`TraceIdFilterTest` 6 例守护）。
  compose 内置 `tracing` profile 的 Jaeger 后端，见下方「链路追踪」。

## 链路追踪

**当前已就绪（开箱可用，零新增依赖）**

- 入站：请求带 `traceparent`（`00-{trace-id}-{parent-id}-{flags}`）且合法时，本服务**沿用上游 traceId**、
  生成新 spanId 续接链路；头部缺失或非法（全零、长度错、字段数错）时自建新链路。
- 出站：响应头回写 `traceparent`（本服务当前 span）、`X-Trace-Id`、`X-Trace-Span-Id`；`tracestate` 原样透传。
- 日志：traceId / spanId 进 MDC，日志格式 `[app,traceId,spanId]`，一次请求的所有日志行可串联。
- 主动调外部服务（如 A2A 远程成员）时，可用 `TraceIdFilter.currentTraceParent()` 取当前上下文加到出站请求头。

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

> 本工程跑在 Boot 3.5.7，Micrometer Tracing 自动配置仍可用；但为与 980/982（Boot 4.1.1）保持完全一致的
> 实现与日志形态，三个工程统一用手写 `TraceIdFilter`，**未**启用自动配置，避免两套 traceId 语义并存。

## 与博客的对应

博客润色版（`../blog/`）在各篇【易错点/小结】处引用了本工程模块；重点篇：
`11-2`（A2A 注册）、`11-3`（获取成员）、`11-4`（调度成员）、`11-6`（MCP 挂载）、
`11-7`（自主分发）、`12-5`（景点 SubAgent）、`13-2`（用户接口）、`13-3`（跟踪与 Token 分析）。
