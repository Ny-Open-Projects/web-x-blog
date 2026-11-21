# 980-demo 部署文档（transfer-demo）

> 本文面向**运维/部署人员**：目标是在任意一台机器上把本工程跑起来，不需要读源码。
> 开发与加固细节见 `README.md`；三工程统一编排见 `../../07-部署编排/README.md`。

## 1. 工程概览

| 项 | 值 |
|---|---|
| 工程 | transfer-demo（AI Agent 库存调拨示例） |
| 技术栈 | Java 21 + Spring Boot 4.1.1 + Spring AI 2.0.1 + JPA/H2 |
| 产物 | `target/transfer-demo-1.0.0.jar`（可执行 fat jar） |
| 默认端口 | 8080 |
| 默认模式 | 离线（`transfer.offline=true`，不联网、不需要任何 Key 即可跑通全流程） |
| 生产模式 | `prod` profile（真实 LLM + 可选 MySQL） |

## 2. 前置要求

| 场景 | 要求 |
|---|---|
| jar 直跑 | JDK/JRE **21+**（`java -version` 确认） |
| Maven 构建 | JDK 21 + Maven 3.9+（离线构建需本地仓库已缓存依赖） |
| Docker | Docker 24+ 与 compose v2 |

## 3. 快速开始（离线演示，5 分钟）

```bash
# 1) 构建（有 Maven + JDK21）
mvn clean package -DskipTests          # 首次构建；后续增量即可

# 2) 启动（离线模式：无需任何 Key）
java -jar target/transfer-demo-1.0.0.jar

# 3) 验证
curl http://localhost:8080/api/transfer/health-demo
# 期望：transfer-demo ok

curl -X POST http://localhost:8080/api/transfer/create \
  -H 'Content-Type: application/json' \
  -d '"把华北仓的 10 件 SKU-A 调拨到华东仓，日期 2026-10-20"'
# 期望：调拨单已创建：orderId=1
```

> POST body 是**纯 JSON 字符串**（自然语言需求），不是对象。中文需求请用 UTF-8 文件传：
> `curl --data-binary @req.json -H 'Content-Type: application/json'`

## 4. 构建

### 4.1 Maven

```bash
# 在线构建
mvn clean package

# 离线构建（CI / 内网，依赖已在本地仓库）
mvn -o clean package

# 跳过测试（仅打包，不推荐用于发布前验证）
mvn clean package -DskipTests
```

产物：`target/transfer-demo-1.0.0.jar`。发布时随包附带本目录 `DEPLOY.md` 与 `application*.yml` 便于运维核对。

### 4.2 Docker

```bash
docker build -t transfer-demo:1.0.0 .
docker run -d --name transfer-demo -p 8080:8080 transfer-demo:1.0.0
```

或 compose（单工程）：

```bash
docker compose up -d            # 默认不带 tracing profile
docker compose --profile tracing up -d   # 附带 Jaeger（可选）
```

## 5. 配置项全表

所有配置均可通过**环境变量**覆盖（格式 `${ENV:默认值}`），无需改 yml。

### 5.1 服务与模式

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `SERVER_PORT` | `server.port` | `8080` | HTTP 端口 |
| `SPRING_PROFILES_ACTIVE` | `spring.profiles.active` | `default` | `default`=离线演示；`prod`=真实模型+可换数据库 |
| `TRANSFER_OFFLINE` | `transfer.offline` | `true` | 离线规则模型开关（prod profile 内被强制为 false） |

### 5.2 LLM 通道（仅 prod 生效）

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `TRANSFER_LLM_BASE_URL` | `transfer.llm.base-url` | 空 | OpenAI 兼容端点（通义/DeepSeek/本地 vLLM 均可） |
| `TRANSFER_LLM_MODEL` | `transfer.llm.model` | 空 | 模型名，如 `qwen-plus` |
| `OPENAI_API_KEY` | `transfer.llm.api-key` | 空 | **必填（prod）**。严禁写进 yml/镜像/日志 |
| `TRANSFER_LLM_MAX_TOKEN_BUDGET` | `transfer.llm.max-token-budget` | `200000` | 进程内 token 成本上限，超限后创建请求直接 400 |
| `TRANSFER_LLM_RETRY_MAX_ATTEMPTS` | `transfer.llm.retry.max-attempts` | `3` | LLM 调用重试次数 |
| `TRANSFER_LLM_RETRY_WAIT_MS` | `transfer.llm.retry.wait-ms` | `500` | 重试初始间隔（指数退避 ×2） |

### 5.3 数据库（prod 生效；default 固定 H2 内存库）

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `TRANSFER_DB_URL` | `spring.datasource.url` | `jdbc:h2:mem:transfer` | 生产换 MySQL：`jdbc:mysql:<SECRET_4553d142> |
| `TRANSFER_DB_USER` | `spring.datasource.username` | `sa` | |
| `TRANSFER_DB_PASSWORD` | `spring.datasource.password` | 空 | 从密钥服务/环境变量注入 |

> **ddl-auto 差异**：default=`create-drop`（每次启动重建，适合演示）；prod=`update`（保留数据）。
> 换 MySQL 必须做第 8 节的一次性迁移。

### 5.4 安全与可观测

| 环境变量 | yml 键 | 默认 | 说明 |
|---|---|---|---|
| `ACTUATOR_USER` | actuator 内存用户 | `admin` | **生产必须覆盖** |
| `ACTUATOR_PASSWORD` | actuator 内存用户 | `transfer-actuator` | **生产必须覆盖** |
| `H2_CONSOLE_ENABLED` | `spring.h2.console.enabled` | `false` | 仅本地调试开启；开启会暴露整库 |

## 6. 端点清单

| 端点 | 方法 | 认证 | 说明 |
|---|---|---|---|
| `/api/transfer/health-demo` | GET | 匿名 | 存活探针 |
| `/api/transfer/create` | POST | 匿名 | 自然语言 → 调拨单入库。**幂等头 `Idempotency-Key` 可选** |
| `/actuator/health`、`/actuator/health/**` | GET | 匿名 | 健康检查（K8s 探针/负载均衡用） |
| `/actuator/info`、`/actuator/metrics`、`/actuator/prometheus` | GET | Basic Auth | 指标端点，生产不裸奔 |

### 幂等语义（`/api/transfer/create`）

- 带 `Idempotency-Key: <键>` 头：同键重复请求返回**首次**结果（`调拨单已存在（幂等命中）：orderId=N`），不会重复入库、不会重复调 LLM；
- 不带该头：按需求文本哈希派生键，同一句需求重复提交同样去重；
- 库层有 `request_id` 唯一索引兜底并发双写。

```bash
# 第一次
curl -X POST localhost:8080/api/transfer/create -H 'Idempotency-Key: order-2026-1023-001' ...
# 第二次（同键）：调拨单已存在（幂等命中）：orderId=1
```

## 7. 部署方式 A：jar 直跑（生产推荐先跑通再容器化）

### 7.1 Windows

方式一：计划任务常驻（重启自愈）

```bat
:: deploy-run.bat（放在 jar 同级目录）
@echo off
cd /d %~dp0
set JAVA_OPTS=-Xms256m -Xmx512m -Dfile.encoding=UTF-8
java %JAVA_OPTS% -jar transfer-demo-1.0.0.jar --server.port=8080 >> logs\app.log 2>&1
```

```powershell
# 注册计划任务（开机启动 + 失败重启，需管理员 PowerShell）
schtasks /Create /TN "transfer-demo" /TR "D:\deploy\transfer-demo\deploy-run.bat" /SC ONSTART /RL HIGHEST /F
schtasks /Run /TN "transfer-demo"
```

方式二：注册为 Windows 服务（用 WinSW 或 NSSM，二选一，均为第三方工具）：

```powershell
# NSSM 示例
nssm install transfer-demo "C:\Program Files\Java\jdk-21\bin\java.exe"
nssm set transfer-demo AppParameters "-jar D:\deploy\transfer-demo\transfer-demo-1.0.0.jar --server.port=8080"
nssm set transfer-demo AppDirectory D:\deploy\transfer-demo
nssm set transfer-demo AppStdout D:\deploy\transfer-demo\logs\app.log
nssm set transfer-demo AppStderr D:\deploy\transfer-demo\logs\app.log
nssm start transfer-demo
```

> 注意：本机若装有 360 等安全软件，放行 `java.exe` 与 8080 端口，否则同网段访问超时。

### 7.2 Linux（systemd）

```ini
# /etc/systemd/system/transfer-demo.service
[Unit]
Description=transfer-demo
After=network.target

[Service]
Type=simple
User=app
WorkingDirectory=/opt/transfer-demo
Environment=SERVER_PORT=8080
Environment=ACTUATOR_USER=ops
Environment=ACTUATOR_PASSWORD=<从密钥服务读取>
ExecStart=/usr/bin/java -Xms256m -Xmx512m -Dfile.encoding=UTF-8 -jar transfer-demo-1.0.0.jar --server.port=8080
Restart=on-failure
RestartSec=5
StandardOutput=append:/opt/transfer-demo/logs/app.log
StandardError=append:/opt/transfer-demo/logs/app.log

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload && systemctl enable --now transfer-demo
systemctl status transfer-demo
```

## 8. MySQL 迁移（prod 一次性操作）

prod profile 用 `ddl-auto=update`：新列会自动加，但**唯一约束不会补**。按序执行：

```sql
-- 1) 建库（如未建）
CREATE DATABASE transfer_demo DEFAULT CHARACTER SET utf8mb4;

-- 2) 应用启动一次，让 Hibernate 建出基础表后，补幂等唯一索引：
--    （幂等列 request_id 会由 update 模式自动添加；索引需手工/启动器补）
CREATE UNIQUE INDEX uk_bb_transfer_order_request_id ON bb_transfer_order(request_id);

-- 3) 如历史数据已有重复 requestId（新部署无此问题），先清理再建索引：
--    SELECT request_id, COUNT(*) FROM bb_transfer_order GROUP BY request_id HAVING COUNT(*) > 1;
```

应用启动时 `IdempotencyIndexInitializer` 会 best-effort 再执行一次 `CREATE UNIQUE INDEX IF NOT EXISTS`（MySQL 报「索引已存在」时忽略），双保险。

## 9. Nacos 配置中心接入（脚手架）

> **现状说明**：本工程默认配置即 env 驱动，不接 Nacos 也可生产运行。
> 以下为需要「配置集中管理/动态刷新」时的接入步骤，按需执行。
> 本仓库未引入 `nacos-config-spring-boot-starter`（离线构建仓库无此依赖，Boot 4 兼容性未经实测），
> 故以官方 starter 方式接入，步骤如下（`[待核实]` 项见文末清单）。

### 9.1 Nacos 服务端

```bash
# docker 方式（与 agent-demos 聚合编排中的 nacos 服务同款）
docker run -d --name nacos -p 8848:8848 -p 9848:9848 \
  -e MODE=standalone nacos/nacos-server:v3.1.0
```

控制台：`http://<nacos-host>:8848/nacos`（默认账号 nacos/nacos，生产立即改密并开鉴权）。

### 9.2 配置dataId 规划

| dataId | group | 内容 |
|---|---|---|
| `transfer-demo.yml` | DEFAULT_GROUP | 本文第 5 节全部配置项 |
| `transfer-demo-prod.yml` | DEFAULT_GROUP | prod 覆盖（db、llm、凭据） |

### 9.3 客户端接入（pom + bootstrap）

```xml
<!-- pom.xml：nacos 配置中心 starter（版本与 Nacos 服务端 3.x 对齐，以官方发布为准） -->
<dependency>
    <groupId>com.alibaba.boot</groupId>
    <artifactId>nacos-config-spring-boot-starter</artifactId>
    <version>0.3.2</version> <!-- [待核实: 该版本与 Spring Boot 4.1.1 的兼容性，需在目标环境实测] -->
</dependency>
```

```yaml
# src/main/resources/bootstrap.yml（新建）
spring:
  application:
    name: transfer-demo
  cloud:
    nacos:
      config:
        server-addr: ${NACOS_SERVER_ADDR:127.0.0.1:8848}
        namespace: ${NACOS_NAMESPACE:}
        group: DEFAULT_GROUP
        file-extension: yml
        refresh-enabled: true
  config:
    import: "nacos:transfer-demo.yml"   # 缺失时本地 application.yml 兜底，不阻断启动
```

### 9.4 灰度与回滚

1. Nacos 控制台先改**一个非关键项**（如日志级别），确认动态刷新生效（`/actuator/env` 或行为变化）；
2. 关键项（db/llm）变更遵循「先灰度一台 → 观察 15 分钟 → 全量」；
3. 回滚 = Nacos 控制台改回上一版本（配置带版本历史，一键回滚）；
4. Nacos 整体故障时：本地 `application.yml` 的 env 默认值兜底，服务不中断。

## 10. 验证清单（部署后逐项过）

```bash
BASE=http://localhost:8080

# 1 健康（匿名，期望 200 + {"status":"UP"}）
curl -s $BASE/actuator/health

# 2 业务冒烟（期望 200，返回创建/幂等文案）
curl -s -X POST $BASE/api/transfer/create -H 'Content-Type: application/json' \
  -d '"把华北仓的 10 件 SKU-A 调拨到华东仓，日期 2026-10-20"'

# 3 幂等（带同键再来一次，期望「已存在（幂等命中）」）
curl -s -X POST $BASE/api/transfer/create -H 'Idempotency-Key: smoke-001' \
  -H 'Content-Type: application/json' -d '"冒烟测试单"'

# 4 指标端点（期望 401 匿名被拦；带凭据 200）
curl -s -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus
curl -s -u "$ACTUATOR_USER:$ACTUATOR_PASSWORD" -o /dev/null -w '%{http_code}\n' $BASE/actuator/prometheus

# 5 链路追踪头（期望继承上游 traceId，spanId 为新 16 位 hex）
curl -s -D - -o /dev/null -H 'traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01' \
  $BASE/api/transfer/health-demo | grep -iE '^(x-trace-id|traceparent):'
```

通过线：1-5 全过；日志行含 `[transfer-demo,<traceId>,<spanId>]`。

## 11. 回滚

| 场景 | 动作 |
|---|---|
| 应用版本回退 | 保留上一个 jar，`java -jar transfer-demo-1.0.0.jar.bak` 或改计划任务/服务指向旧包；配置未变即可回退 |
| 数据库变更 | `request_id` 列为新增可空列，旧代码不感知；唯一索引删除即回退：`DROP INDEX uk_bb_transfer_order_request_id ON bb_transfer_order;` |
| 配置回退 | env/系统属性方式改回；Nacos 方式用控制台版本历史一键回滚 |

## 12. 生产检查清单（八项对照）

| 项 | 本工程状态 | 部署时确认 |
|---|---|---|
| 幂等 | ✅ requestId + 唯一索引 + 预查 | 已跑第 10 节验证 3 |
| 超时 | ✅ LLM/HTTP 通道显式超时 | — |
| 重试 | ✅ 指数退避限次（LLM） | — |
| 限流 | ⚠️ 未做（内网/低并发可接受；公网部署需前置网关限流） | 按暴露面决定 |
| 审计日志 | ✅ traceId 贯穿 + 关键操作日志 | 确认日志采集到位 |
| 成本上限 | ✅ token 预算（默认 20 万，按成本调） | 设 `TRANSFER_LLM_MAX_TOKEN_BUDGET` |
| 灰度回滚 | ✅ 配置版本化 + jar 版本化 | 按第 11 节执行 |
| 评测集回归 | ✅ 42 例单测/集成测试（`mvn test`） | CI 已接入（`.github/workflows/ci.yml`） |

## 13. 故障排查

| 现象 | 定位 |
|---|---|
| 启动报 `OpenAiChatAutoConfiguration` 相关错误 | 用了 prod profile 但没填 `OPENAI_API_KEY`；或应保持 default 离线 |
| POST create 返回 400 `requirement 不能为空` | body 不是纯 JSON 字符串；中文请用 UTF-8 文件 `--data-binary @file` |
| 返回 400 `TOKEN_BUDGET_EXCEEDED` | 进程内 token 预算耗尽，调大 `TRANSFER_LLM_MAX_TOKEN_BUDGET` 或重启（预算为进程内累计） |
| 同网段访问超时（ping 通） | Windows 防火墙 Block 规则或 360 拦截，放行 java.exe + 端口 |
| 指标端点 200（匿名可达） | `ACTUATOR_*` 未覆盖默认值且部署在可信内网；公网必须改密 |
| H2 数据重启丢失 | default 模式内存库预期行为；要持久化走 prod + MySQL（第 8 节） |

---

## 待确认清单（部署侧）

- `[待核实]` nacos-config-spring-boot-starter 版本与 Spring Boot 4.1.1 的兼容性：接入前在目标环境跑一次 `mvn dependency:tree` + 启动冒烟；不兼容则退回 env 驱动方案（本文第 5 节已覆盖）。
- `[待核实]` Nacos 服务端 v3.1.0 镜像与规划版本一致性：以运维侧 Nacos 实际版本为准。
