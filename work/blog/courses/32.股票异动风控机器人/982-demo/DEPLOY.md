# 982-demo 部署文档（982-demo）

> 本文面向**运维/部署人员**：目标是在任意一台机器上把本工程跑起来，不需要读源码。
> 开发与加固细节见 `README.md`；三工程统一编排见 `../../07-部署编排/README.md`。

## 1. 工程概览

| 项 | 值 |
|---|---|
| 工程 | 982-demo（AI Agent 股票异动风控机器人，支持 A 股 + 美股） |
| 技术栈 | Java 21 + Spring Boot 4.1.1 + Spring AI 2.0.1 + resilience4j |
| 产物 | `target/982-demo-1.0.0.jar`（可执行 fat jar） |
| 默认端口 | 8080 |
| 默认模式 | 离线 mock 行情（`SPRING_PROFILES_ACTIVE=default`，不联网、不需要 Key 跑通规则引擎 + 问答） |
| 生产模式 | `prod` profile（真实 LLM + 真实行情网关） |

## 2. 前置要求

| 场景 | 要求 |
|---|---|
| jar 直跑 | JDK/JRE **21+** |
| Maven 构建 | JDK 21 + Maven 3.9+ |
| Docker | Docker 24+ 与 compose v2 |

## 3. 快速开始（离线演示，5 分钟）

```bash
# 1) 构建
mvn clean package

# 2) 启动（默认离线 mock 行情）
java -jar target/982-demo-1.0.0.jar

# 3) 验证
curl http://localhost:8080/actuator/health          # 期望 200 + UP
curl -X POST 'http://localhost:8080/api/risk/evaluate?symbol=600519'   # 规则评估
curl http://localhost:8080/api/risk/scan             # 手动触发一轮扫描
curl 'http://localhost:8080/api/risk/query?q=600519%20现在风险高吗'     # 自然语言问答
```

> 中文 query 参数请 URL 编码或使用 UTF-8 文件，避免终端编码问题。

## 4. 构建

```bash
mvn clean package          # 在线
mvn -o clean package       # 离线（依赖已在本地仓库）
```

Docker：

```bash
docker build -t 982-demo:1.0.0 .
docker run -d --name 982-demo -p 8080:8080 982-demo:1.0.0
docker compose up -d                        # 或 compose
docker compose --profile tracing up -d      # 附带 Jaeger（可选）
```

## 5. 配置项全表

### 5.1 服务与 LLM

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `SERVER_PORT` | `server.port` | `8080` | HTTP 端口 |
| `SPRING_PROFILES_ACTIVE` | `spring.profiles.active` | `default` | `default`=离线 mock；`prod`=真实模型/行情 |
| `SPRING_AI_OPENAI_API_KEY` | `spring.ai.openai.api-key` | `dummy` | **prod 必填**，严禁硬编码 |
| `SPRING_AI_OPENAI_BASE_URL` | `spring.ai.openai.base-url` | `https://api.openai.com/v1` | OpenAI 兼容端点（通义/vLLM 均可） |
| `SPRING_AI_OPENAI_CHAT_MODEL` | `spring.ai.openai.chat.options.model` | `gpt-4o` | 模型名 |
| `RISK_LLM_MAX_TOKEN_BUDGET` | `risk.llm.max-token-budget` | `200000` | 问答链路 token 上限，超限返回降级文案 |
| `RISK_LLM_RETRY_MAX_ATTEMPTS` | `risk.llm.retry.max-attempts` | `3` | LLM 重试次数（指数退避） |
| `RISK_LLM_RETRY_WAIT_MS` | `risk.llm.retry.wait-ms` | `500` | 重试初始间隔 |

### 5.2 行情网关（prod 生效）

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `RISK_QUOTE_API_URL` | `risk.quote.api-url` | 空 | 真实行情端点；**留空则仅 mock 源** |
| `RISK_QUOTE_CONNECT_TIMEOUT_MS` | `risk.quote.connect-timeout-ms` | `3000` | 连接超时 |
| `RISK_QUOTE_READ_TIMEOUT_MS` | `risk.quote.read-timeout-ms` | `5000` | 读取超时 |
| `RISK_QUOTE_RETRY_MAX_ATTEMPTS` | `risk.quote.retry.max-attempts` | `3` | 行情拉取重试次数 |
| `RISK_QUOTE_RETRY_WAIT_MS` | `risk.quote.retry.wait-ms` | `500` | 重试初始间隔 |

> 行情拉取失败（含重试耗尽）降级为空列表，不影响扫描主链与规则评估。

### 5.3 规则与调度

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `RISK_RULES_PRICE_CHANGE_THRESHOLD` | `risk.rules.price-change-threshold` | `5.0` | 涨跌幅异动阈值（%） |
| `RISK_RULES_VOLUME_SPIKE_RATIO` | `risk.rules.volume-spike-ratio` | `2.0` | 成交量相对基准倍数 |
| `RISK_RULES_VOLUME_SPIKE_BASE` | `risk.rules.volume-spike-base` | `8000000` | 成交量基准量（生产改滚动均值） |
| `RISK_SCAN_ENABLED` | `risk.scan.enabled` | `true` | 周期扫描开关 |
| `RISK_SCAN_FIXED_DELAY_MS` | `risk.scan.fixed-delay-ms` | `30000` | 扫描间隔（演示 30s，生产按需） |

### 5.4 安全与可观测

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `ACTUATOR_USER` | actuator 内存用户 | `admin` | **生产必须覆盖** |
| `ACTUATOR_PASSWORD` | actuator 内存用户 | `riskbot-actuator` | **生产必须覆盖** |

## 6. 端点清单

| 端点 | 方法 | 认证 | 说明 |
|---|---|---|---|
| `/api/risk/evaluate` | POST | 匿名 | 单票规则评估（`?symbol=600519`） |
| `/api/risk/scan` | GET | 匿名 | 手动触发一轮全量扫描 |
| `/api/risk/query` | GET | 匿名 | 自然语言风险问答（`?q=...`） |
| `/actuator/health`、`/actuator/health/**` | GET | 匿名 | 健康检查 |
| `/actuator/prometheus`、`/actuator/metrics`、`/actuator/info` | GET | Basic Auth | 指标端点 |

## 7. 部署方式 A：jar 直跑

### 7.1 Windows

```bat
:: deploy-run.bat（jar 同级目录）
@echo off
cd /d %~dp0
set JAVA_OPTS=-Xms256m -Xmx512m -Dfile.encoding=UTF-8
java %JAVA_OPTS% -jar 982-demo-1.0.0.jar --server.port=8080 >> logs\app.log 2>&1
```

```powershell
schtasks /Create /TN "982-demo" /TR "D:\deploy\982-demo\deploy-run.bat" /SC ONSTART /RL HIGHEST /F
schtasks /Run /TN "982-demo"
```

> 防火墙/360 需放行 `java.exe` 与端口，否则同网段访问超时。

### 7.2 Linux（systemd）

```ini
# /etc/systemd/system/982-demo.service
[Unit]
Description=982-demo
After=network.target

[Service]
Type=simple
User=app
WorkingDirectory=/opt/982-demo
Environment=SERVER_PORT=8080
Environment=ACTUATOR_USER=ops
Environment=ACTUATOR_PASSWORD=<从密钥服务读取>
Environment=SPRING_PROFILES_ACTIVE=prod
Environment=SPRING_AI_OPENAI_API_KEY=<从密钥服务读取>
Environment=RISK_QUOTE_API_URL=<行情网关地址>
ExecStart=/usr/bin/java -Xms256m -Xmx512m -Dfile.encoding=UTF-8 -jar 982-demo-1.0.0.jar --server.port=8080
Restart=on-failure
RestartSec=5
StandardOutput=append:/opt/982-demo/logs/app.log
StandardError=append:/opt/982-demo/logs/app.log

[Install]
WantedBy=multi-user.target
```

## 8. Nacos 配置中心接入（脚手架）

> 本工程默认配置即 env 驱动，不接 Nacos 也可生产运行。需要集中管理/动态刷新时按官方 starter 接入：
> 本仓库未引入 `nacos-config-spring-boot-starter`（离线构建仓库无此依赖、Boot 4.1.1 兼容性未实测）。

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>nacos-config-spring-boot-starter</artifactId>
    <version>0.3.2</version> <!-- [待核实: 与 Spring Boot 4.1.1 兼容性需目标环境实测] -->
</dependency>
```

```yaml
# src/main/resources/bootstrap.yml（新建）
spring:
  application:
    name: stock-risk-bot
  cloud:
    nacos:
      config:
        server-addr: ${NACOS_SERVER_ADDR:127.0.0.1:8848}
        namespace: ${NACOS_NAMESPACE:}
        group: DEFAULT_GROUP
        file-extension: yml
        refresh-enabled: true
  config:
    import: "nacos:stock-risk-bot.yml"
```

dataId 规划：`stock-risk-bot.yml`（第 5 节全部配置项）、`stock-risk-bot-prod.yml`（prod 覆盖：llm/quote 凭据类项建议仍走 env + Nacos 只放非敏感项）。
灰度/回滚：先非关键项（日志级别）→ 灰度一台 → 全量；回滚用控制台版本历史。
**Nacos 故障不影响启动**：本地 `application.yml` 的 env 默认值兜底。

## 9. 验证清单（部署后逐项过）

```bash
BASE=http://localhost:8080

# 1 健康（期望 200 + UP）
curl -s $BASE/actuator/health

# 2 规则评估（期望 200 + JSON）
curl -s -o /dev/null -w '%{http_code}\n' -X POST "$BASE/api/risk/evaluate?symbol=600519"

# 3 扫描（期望 200 + JSON）
curl -s -o /dev/null -w '%{http_code}\n' $BASE/api/risk/scan

# 4 问答（期望 200 + 文本）
curl -s -o /dev/null -w '%{http_code}\n' "$BASE/api/risk/query?q=600519"

# 5 周期调度生效（关键！不能只看 Started）：启动 90s 后日志应出现 >= 3 轮扫描
#    grep -c "扫描" logs/app.log     （默认 fixed-delay=30s）

# 6 指标端点（期望匿名 401，带凭据 200）
curl -s -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus
curl -s -u "$ACTUATOR_USER:$ACTUATOR_PASSWORD" -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus

# 7 链路追踪头（期望继承上游 traceId）
curl -s -D - -o /dev/null -H 'traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01' \
  $BASE/api/risk/scan | grep -iE '^(x-trace-id|traceparent):'
```

通过线：1-4、6、7 全过，且第 5 项**日志中扫描轮次数 ≥ 3**（调度类功能必须数周期日志，不能只看进程 Started）。

## 10. 回滚

| 场景 | 动作 |
|---|---|
| 应用版本回退 | 保留上一个 jar，改计划任务/服务/systemd 指向旧包 |
| 配置回退 | env 方式改回；Nacos 方式用控制台版本历史 |
| 行情网关异常 | `RISK_QUOTE_API_URL` 置空后 RealQuoteProvider 返回空行情（不切回 mock；要回离线 mock 需把 `SPRING_PROFILES_ACTIVE` 改回 default） |

## 11. 生产检查清单（八项对照）

| 项 | 本工程状态 | 部署时确认 |
|---|---|---|
| 幂等 | ✅ 扫描/评估为只读计算，无写副作用 | — |
| 超时 | ✅ LLM/行情网关显式超时（连接 3s/读取 5s，env 可调） | — |
| 重试 | ✅ LLM + 行情网关双通道指数退避限次 | — |
| 限流 | ⚠️ 未做（公网暴露需前置网关限流） | 按暴露面决定 |
| 审计日志 | ✅ traceId 贯穿 + MDC + 告警记录 | 确认日志采集 |
| 成本上限 | ✅ token 预算（问答链路，超限降级文案而非 500） | 设 `RISK_LLM_MAX_TOKEN_BUDGET` |
| 灰度回滚 | ✅ jar + 配置版本化 | 按第 10 节 |
| 评测集回归 | ✅ 38 例（`mvn test`），CI 已接入 | — |

## 12. 故障排查

| 现象 | 定位 |
|---|---|
| 周期扫描不跑 | 确认 `RISK_SCAN_ENABLED=true`；**必须数日志轮次**（只看到 Started 不算） |
| 问答返回降级文案 | token 预算耗尽（调大 `RISK_LLM_MAX_TOKEN_BUDGET`）或 LLM 通道重试耗尽 |
| evaluate 大量告警/无告警 | 核对 `risk.rules.*` 阈值与行情源字段（mock 源为固定样本） |
| prod 模式问答降级（非启动失败） | `SPRING_AI_OPENAI_API_KEY` 未配时占位符可解析、应用正常启动，问答走 FALLBACK_ANSWER；想保持离线就留在 default profile |
| 同网段访问超时 | 防火墙/360 拦截，放行 java.exe + 端口 |

---

## 待确认清单（部署侧）

- `[待核实]` nacos-config-spring-boot-starter 与 Spring Boot 4.1.1 兼容性：接入前目标环境实测启动 + 配置刷新。
- `[待核实]` 真实行情网关的接口契约（字段/限流）：`RealQuoteProvider` 当前为通用 JSON 适配，接真实源前需按源站文档校准解析。
