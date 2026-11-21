# 981-demo 部署文档（981-demo）

> 本文面向**运维/部署人员**：目标是在任意一台机器上把本工程跑起来，不需要读源码。
> 开发与加固细节见 `README.md`；三工程统一编排见 `../../07-部署编排/README.md`。

## 1. 工程概览

| 项 | 值 |
|---|---|
| 工程 | 981-demo（多 Agent + Skills + A2A 自主决策旅游规划智能体） |
| 技术栈 | Java 21 + Spring Boot 3.5.7 + AgentScope 2.0.3（Boot 4 不被 AgentScope 支持，硬约束） |
| 产物 | `target/981-demo-1.0.0.jar`（可执行 fat jar） |
| 默认端口 | 8080 |
| 默认模式 | 离线（`app.agent.model-mode=offline`，规则模型，不联网、不需要 Key 跑通主管→成员全链路） |
| 生产模式 | `prod` profile（真实模型 dashscope + Nacos 注册中心可选） |

## 2. 前置要求

| 场景 | 要求 |
|---|---|
| jar 直跑 | JDK/JRE **21+** |
| Maven 构建 | JDK 21 + Maven 3.9+ |
| Docker | Docker 24+ 与 compose v2 |
| Nacos（可选） | Nacos 3.x 服务端（仅 `discovery=nacos` 模式需要） |

## 3. 快速开始（离线演示，5 分钟）

```bash
# 1) 构建
mvn clean package

# 2) 启动（离线模式：无需任何 Key）
java -jar target/981-demo-1.0.0.jar

# 3) 验证
curl http://localhost:8080/api/travel/members
# 期望：返回团队成员 JSON 数组

curl -X POST http://localhost:8080/api/travel/plan \
  -H 'Content-Type: application/json' \
  --data-binary @req.json
# req.json 内容：{"requirement":"3天2晚，上海出发，想去杭州西湖和乌镇，预算3000元"}
# 期望：返回完整行程规划 JSON
```

> 中文 body 必须用 UTF-8 文件传（`--data-binary @file`）；内联中文可能因终端编码不是 UTF-8 导致服务端 400。
> 字段名是 `requirement`（不是 `request`）。

## 4. 构建

```bash
mvn clean package          # 在线
mvn -o clean package       # 离线（依赖已在本地仓库）
```

Docker：

```bash
docker build -t 981-demo:1.0.0 .
docker run -d --name 981-demo -p 8080:8080 981-demo:1.0.0
docker compose up -d                        # 或 compose（含 nacos 服务）
docker compose --profile tracing up -d      # 附带 Jaeger（可选）
```

## 5. 配置项全表

### 5.1 服务与 Agent 行为

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `SERVER_PORT` | `server.port` | `8080` | HTTP 端口 |
| `SPRING_PROFILES_ACTIVE` | `spring.profiles.active` | `default` | `default`=离线；`prod`=真实模型 |
| `APP_AGENT_MODEL_MODE` | `app.agent.model-mode` | `offline` | `offline`=规则模型；`dashscope`=真实模型 |
| `APP_AGENT_MODEL_NAME` | `app.agent.model-name` | `offline-plan` | 非 offline 时生效，如 `dashscope:qwen-plus` |
| `DASHSCOPE_API_KEY` | （模型 SDK 读取） | 空 | **prod 必填**，严禁硬编码 |
| `APP_AGENT_DISCOVERY` | `app.agent.discovery` | `in-process` | `in-process`=进程内注册表；`nacos`=Nacos 注册中心 |
| `APP_AGENT_NACOS_SERVER_ADDR` | `app.agent.nacos-server-addr` | `127.0.0.1:8848` | discovery=nacos 时生效 |
| `APP_AGENT_ADVERTISE_IP` | `app.agent.advertise-ip` | 空 | 注册到 Nacos 的对外 IP；**容器/多网卡必须显式设**，为空回退本机 IP |
| `APP_AGENT_MAX_ITERS` | `app.agent.max-iters` | `10` | ReAct 循环最大迭代轮数（有界自主，防跑飞） |
| `APP_AGENT_MAX_TOKEN_BUDGET` | `app.agent.max-token-budget` | `200000` | 进程内 token 成本上限，超限 → HTTP 400 `TOKEN_BUDGET_EXCEEDED` |

### 5.2 远程成员调用（熔断）

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `APP_RISK_FAILURE_RATE_THRESHOLD` | `app.risk.failure-rate-threshold` | `50` | 熔断失败率阈值（%） |
| `APP_RISK_WAIT_DURATION_IN_OPEN_STATE` | `app.risk.wait-duration-in-open-state` | `10s` | 熔断器打开持续时间 |
| `APP_RISK_SLIDING_WINDOW_SIZE` | `app.risk.sliding-window-size` | `10` | 统计滑窗大小 |

### 5.3 第三方凭证

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `BAIDU_MAP_API_KEY` | `baidu.map.api-key` | 空 | 百度地图 AK；缺失时启动告警并自动走离线桩，不阻断启动 |

### 5.4 安全与可观测

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `ACTUATOR_USER` | actuator 内存用户 | `admin` | **生产必须覆盖** |
| `ACTUATOR_PASSWORD` | actuator 内存用户 | `travel-actuator` | **生产必须覆盖** |

## 6. 端点清单

| 端点 | 方法 | 认证 | 说明 |
|---|---|---|---|
| `/api/travel/members` | GET | 匿名 | 团队成员清单 |
| `/api/travel/plan` | POST | 匿名 | 旅游规划全链路（主管 Agent 编排） |
| `/a2a/{agent}/.well-known/agent.json` | GET | 匿名 | A2A AgentCard 发现 |
| `/a2a/{agent}` | POST | 匿名 | A2A JSON-RPC 调用入口 |
| `/actuator/health`、`/actuator/health/**` | GET | 匿名 | 健康检查 |
| `/actuator/prometheus`、`/actuator/metrics`、`/actuator/info` | GET | Basic Auth | 指标端点 |

## 7. 部署方式 A：jar 直跑

### 7.1 Windows

```bat
:: deploy-run.bat（jar 同级目录）
@echo off
cd /d %~dp0
set JAVA_OPTS=-Xms256m -Xmx512m -Dfile.encoding=UTF-8
java %JAVA_OPTS% -jar 981-demo-1.0.0.jar --server.port=8080 >> logs\app.log 2>&1
```

```powershell
schtasks /Create /TN "981-demo" /TR "D:\deploy\981-demo\deploy-run.bat" /SC ONSTART /RL HIGHEST /F
schtasks /Run /TN "981-demo"
```

> 防火墙/360 需放行 `java.exe` 与端口，否则同网段访问超时。

### 7.2 Linux（systemd）

```ini
# /etc/systemd/system/981-demo.service
[Unit]
Description=981-demo
After=network.target

[Service]
Type=simple
User=app
WorkingDirectory=/opt/981-demo
Environment=SERVER_PORT=8080
Environment=ACTUATOR_USER=ops
Environment=ACTUATOR_PASSWORD=<从密钥服务读取>
Environment=DASHSCOPE_API_KEY=<从密钥服务读取，仅 prod>
ExecStart=/usr/bin/java -Xms256m -Xmx512m -Dfile.encoding=UTF-8 -jar 981-demo-1.0.0.jar --server.port=8080
Restart=on-failure
RestartSec=5
StandardOutput=append:/opt/981-demo/logs/app.log
StandardError=append:/opt/981-demo/logs/app.log

[Install]
WantedBy=multi-user.target
```

## 8. Nacos 双模式说明

本工程对 Nacos 有两种用法，按需选择：

### 8.1 服务注册（已内置，`discovery=nacos`）

课程 11-2/11-3 的 A2A 注册中心场景：团队成员互相发现走 Nacos。

```bash
# 1) 起 Nacos（docker 或已有实例）
docker run -d --name nacos -p 8848:8848 -p 9848:9848 -e MODE=standalone nacos/nacos-server:v3.1.0

# 2) 应用侧切模式
APP_AGENT_DISCOVERY=nacos APP_AGENT_NACOS_SERVER_ADDR=<nacos-host>:8848 APP_AGENT_ADVERTISE_IP=<本机对外IP>
```

验证：启动日志出现注册成功；Nacos 控制台服务列表可见 `981-demo` 及成员。

### 8.2 配置中心（脚手架，按需接入）

> 本仓库未引入 `nacos-config-spring-boot-starter`（离线构建仓库无此依赖、Boot 3.5.7 兼容性未实测）。
> 需要配置集中管理时按官方 starter 接入：

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>nacos-config-spring-boot-starter</artifactId>
    <version>0.3.2</version> <!-- [待核实: 与 Boot 3.5.7 兼容性需目标环境实测] -->
</dependency>
```

```yaml
# src/main/resources/bootstrap.yml（新建）
spring:
  application:
    name: 981-demo
  cloud:
    nacos:
      config:
        server-addr: ${NACOS_SERVER_ADDR:127.0.0.1:8848}
        namespace: ${NACOS_NAMESPACE:}
        group: DEFAULT_GROUP
        file-extension: yml
        refresh-enabled: true
  config:
    import: "nacos:981-demo.yml"
```

dataId 规划：`981-demo.yml`（第 5 节全部配置项）、`981-demo-prod.yml`（prod 覆盖）。
灰度/回滚同 980 文档第 9.4 节：先非关键项 → 灰度一台 → 全量；回滚用控制台版本历史。
**Nacos 故障不影响启动**：`spring.config.import` 中的 nacos 源缺失时本地 `application.yml` 的 env 默认值兜底。

## 9. 验证清单（部署后逐项过）

```bash
BASE=http://localhost:8080

# 1 健康（期望 200 + UP）
curl -s $BASE/actuator/health

# 2 成员清单（期望 200 + JSON 数组）
curl -s $BASE/api/travel/members

# 3 规划全链路（期望 200 + 行程 JSON；中文用 UTF-8 文件）
printf '{"requirement":"3天2晚 上海出发 杭州西湖 乌镇 预算3000元"}' > /tmp/req981.json
curl -s -o /dev/null -w '%{http_code}\n' -X POST $BASE/api/travel/plan \
  -H 'Content-Type: application/json' --data-binary @/tmp/req981.json

# 4 指标端点（期望匿名 401，带凭据 200）
curl -s -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus
curl -s -u "$ACTUATOR_USER:$ACTUATOR_PASSWORD" -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus

# 5 链路追踪头（期望继承上游 traceId）
curl -s -D - -o /dev/null -H 'traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01' \
  $BASE/api/travel/members | grep -iE '^(x-trace-id|traceparent):'

# 6 Token 预算（可选：上限调到 1 后首次 plan 应 400 TOKEN_BUDGET_EXCEEDED）
#    java -jar 981-demo-1.0.0.jar --app.agent.max-token-budget=1
```

通过线：1-5 全过；日志行含 `[981-demo,<traceId>,<spanId>]`。

## 10. 回滚

| 场景 | 动作 |
|---|---|
| 应用版本回退 | 保留上一个 jar，改计划任务/服务/systemd 指向旧包 |
| 配置回退 | env 方式改回；Nacos 方式用控制台版本历史 |
| 注册中心回退 | `APP_AGENT_DISCOVERY=in-process` 即退回进程内注册表，不依赖 Nacos |

## 11. 生产检查清单（八项对照）

| 项 | 本工程状态 | 部署时确认 |
|---|---|---|
| 幂等 | ⚠️ plan 为非幂等写操作（Agent 编排无副作用写库）；如接入订单类写操作需补 requestId | 按业务演进 |
| 超时 | ✅ 远程成员调用 + 模型调用显式超时 | — |
| 重试 | ✅ A2A HTTP 传输指数退避（协议层 JSON-RPC error 不重试） | — |
| 限流 | ⚠️ 未做（公网暴露需前置网关限流） | 按暴露面决定 |
| 审计日志 | ✅ traceId 贯穿 + MDC | 确认日志采集 |
| 成本上限 | ✅ Token 预算装饰器位于 ReAct 循环内逐轮记账（实测上限=1 首次 plan 即 400） | 设 `APP_AGENT_MAX_TOKEN_BUDGET` |
| 灰度回滚 | ✅ jar + 配置版本化 | 按第 10 节 |
| 评测集回归 | ✅ 39 例（`mvn test`），CI 已接入 | — |

## 12. 故障排查

| 现象 | 定位 |
|---|---|
| POST plan 返回 400 且服务端日志 `Invalid UTF-8 middle byte` | 客户端内联中文非 UTF-8；改用 `--data-binary @file`（UTF-8 文件） |
| 400 `TOKEN_BUDGET_EXCEEDED` | 预算耗尽；调大 `APP_AGENT_MAX_TOKEN_BUDGET` 或重启（进程内累计） |
| 启动告警「百度地图 Key 未配置」 | 预期行为（离线桩兜底）；需要真实路径规划时设 `BAIDU_MAP_API_KEY` |
| discovery=nacos 起不来 | 确认 `APP_AGENT_NACOS_SERVER_ADDR` 可达 + `APP_AGENT_ADVERTISE_IP` 已设（容器必设） |
| A2A card 404 | 确认 URL 为 `/a2a/{agent}/.well-known/agent.json`，`{agent}` 为成员名 |
| 同网段访问超时 | 防火墙/360 拦截，放行 java.exe + 端口 |

---

## 待确认清单（部署侧）

- `[待核实]` nacos-config-spring-boot-starter 与 Spring Boot 3.5.7 兼容性：接入前目标环境实测启动 + 配置刷新。
- `[待核实]` Nacos 服务端版本与镜像一致性（v3.1.0）：以运维侧实际版本为准。
