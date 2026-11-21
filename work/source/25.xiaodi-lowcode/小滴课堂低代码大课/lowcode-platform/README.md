# LowCode Platform（低代码平台 · 自研工程）

基于「小滴课堂低代码大课」229 篇博客提炼的**可商用自研低代码平台**参考实现。
设计文档见 `工程实践-05-参考实现蓝图.md` 与 `工程实践-06-工作流模块设计（平台内）.md`（同目录上级）。

> **📘 接手本工程请先读 [`交接文档.md`](./交接文档.md)** —— 面向新 Agent / 新人的自包含说明书：目录地图、设计约定、运行与测试方式、已交付边界、本机环境坑位。

> 工作流（ComfyUI 式可视化编排）是**平台内模块**，与 page/component 等模块同级，主次分明，随平台一体部署。

## 目录结构

```
lowcode-platform/
├─ packages/shared/        # 平台级共享契约（PageSchema / WorkflowContract / 租户预留）
├─ apps/
│  ├─ server/              # 后端（NestJS）— 含 modules/workflow + modules/page-builder
│  └─ studio/              # 创作端（React + React Flow，M2 工作流画布 / M7 页面搭建）
├─ docker-compose.yml      # mysql + redis + server 一键起
├─ package.json             # npm workspaces（workspaces 字段）
└─ .env.example
```

## 技术栈

- 后端：NestJS 10 + TypeORM + MySQL 8 + Redis 7
- 前端：React 18 + Vite + React Flow（工作流画布）
- 契约：`@lowcode/shared`（跨端共用类型）
- 部署：Docker / docker-compose

## 快速开始

```bash
npm install                 # npm workspaces（本机用 npm，pnpm 在本机缺原生二进制）
cp .env.example .env        # 按需填写 OSS/DB 等
# 起基础设施（需先启动 Docker Desktop / 具备管理员权限拉起 docker daemon）
docker compose up -d mysql redis
npm run dev --workspace=@lowcode/server
npm run dev --workspace=@lowcode/studio
```

## 验证（编译校验，无需数据库）

```bash
npm run build               # 按依赖序：shared → server(nest build) → studio(vite build)
```
- server：`nest build` 通过 = 后端类型与 DI 全部闭合。
- studio：`tsc --noEmit` 0 错误 + `vite build` 打包通过 = 前端可编译可发布。
- 后端 DAG 引擎已通过纯函数冒烟（拓扑序/环检测/节点输出传播）。
- **运行时 E2E 已真实跑通**（连 MySQL，docker compose 起 mysql 后本地起 server）：建图（formSubmit→map→composePage→sendSms）→ 运行 → 模板注入生效（标题/文本动态生成）→ 页面持久化为 `wf_generated_page` → `/pages/:id/render` 返回完整 HTML。验证脚本与结果见本仓库验证记录。

## 商业化就绪（设计硬约束，见 06 §8）

- 依赖仅 MIT/Apache/BSD 等商业友好协议；自研默认 MIT。
- 全表预留 `tenant_id`，后续 SaaS 化零结构改动。
- 个人信息（手机号/短信）走脱敏与最小化采集，预留审计。
- 密钥仅存服务端配置/密钥库，永不进前端、不进图 JSON、不进沙箱。
- OSS region / 短信通道 / 限流阈值等全配置外置。
- 执行埋点统一可观测，预留计量钩子（后续计费）。
- 品牌去课程化，可独立售卖。

## 当前进度（M 系列 = 工作流模块增量）

| 阶段 | 内容 | 状态 |
|---|---|---|
| P0 | 主工程 Monorepo 脚手架 | ✅ 完成 |
| M0 | 节点注册表 + Graph DSL + wf_* 表 + 图 CRUD | ✅ 完成 |
| M1 | DAG 执行引擎（拓扑/执行/节点级追踪） | ✅ 完成（纯函数可单测） |
| M2 | studio 内 workflow-canvas（React Flow） | ✅ 完成 |
| M3 | 预置节点端到端打通（form/oss/短信/ui 发射 → render） | ✅ 完成（真实运行时 E2E 已通过） |
| M4 | 沙箱隔离（脚本/LLM 节点，软隔离 + 配额 + 审计） | ✅ 完成（三层验证通过） |
| M5 | studio 前端参数编辑器（script/llm 专用面板 + 全节点结构化输入） | ✅ 完成（tsc 0 错 + vite build 通过） |
| M6 | 商业化闭环（真实表单持久化 + 租户隔离守卫 + 统计/审计端点 + 真实运行时 E2E） | ✅ 完成（12/12 运行时 E2E 通过） |
| M7 | 可视化 Page Builder（独立平台模块，复用 renderPageToHtml，CRUD + HTML 渲染 + 租户隔离） | ✅ 完成（11/11 运行时 E2E 通过） |
| M8 | 容器级硬隔离（一次性容器 + 禁网 + 只读根 + 资源限额 + 自动回退 + 审计记层） | ✅ 完成（见 M8 章节） |
| M9 | 嵌套组件可视化（容器/栅格/表单可嵌子组件，树形编辑） | ✅ 完成（18/18 运行时 E2E 通过） |

全部 M 系列（P0 → M9）已交付并验证。剩余升级路线：**SMS/OSS Provider 接入真实云厂商**（架构已支持，仅替换 `WorkflowModule` 内 Provider 实现 + 填 env 密钥；节点代码零改动）。

## M8 容器级硬隔离（已交付 · 多租户安全底线）

M4 的 vm 软隔离**不是安全边界**（Node `vm` 只是上下文隔离，可被构造漏洞绕过）。M8 把 `script.eval` 的执行从「同进程 vm」升级为**独立一次性容器**：不可信脚本与主进程在 PID / 内核能力 / 文件系统 / 网络层面彻底分开。

### 交付内容
- `nodes/container-sandbox.ts`（新增）
  - `runInContainer()`：每次执行创建**一次性容器**（`AutoRemove`，用完即焚），宿主侧超时到点 `kill` 强杀（死循环也无法拖垮主进程）。
  - 容器加固：`NetworkDisabled`（禁网）+ `CapDrop: ALL` + `SecurityOpt: no-new-privileges` + `ReadonlyRootfs`（只读根）+ `User: 10001`（非 root）+ `Memory/MemorySwap/NanoCpus/PidsLimit` 限额（防 OOM / fork 炸弹）+ `/tmp` tmpfs（noexec,nosuid,1m）。
  - 用户脚本经 `new Function` 执行，**拿不到 runner 作用域的 `require`** —— 容器内也无法读写文件或联网。
  - runner 自检 `probe`（uid / 根文件系统可写性 / 网络接口列表），用于验证隔离真的生效。
  - `executeWithFallback()`：容器不可用（Docker 未启动 / 镜像缺失 / 权限不足）时**自动回退 vm 软隔离**，并在 `fallbackReason` 中如实标注——**不假装硬隔离**。
- `registry.ts`：`script.eval` 改走 `executeWithFallback`，审计新增 `isolation` 字段（`vm` / `container`）与回退原因。
- `entities/wf-audit.entity.ts`：`wf_audit` 增 `isolation` 列，事后可查"这条脚本当时跑在哪层隔离里"。
- 配置外置（`.env.example`）：`WF_SANDBOX_MODE`（`vm` / `container`）、`WF_SANDBOX_IMAGE`、`WF_SANDBOX_MEMORY_BYTES`、`WF_SANDBOX_NANO_CPUS`、`WF_SANDBOX_PIDS_LIMIT`、`WF_DOCKER_SOCKET`。

### 隔离层级对照（选用规则）
| 模式 | 隔离强度 | 适用场景 | 依赖 |
|---|---|---|---|
| `vm`（软隔离） | 上下文隔离，非安全边界 | 自托管单租户、可信运维 | 无 |
| `container`（硬隔离） | 进程/能力/文件系统/网络全隔离 | **多租户 SaaS、对外开放脚本编辑** | Docker + 运行时镜像 |

### 容器运行时镜像
默认镜像 `node:20-alpine`（需可拉取）。**国内网络拉不动 Docker Hub 时**，用随工程附带的 `apps/server/Dockerfile.sandbox` 本地构建最小镜像（Debian 底包 + Node 运行时，无需外网）：

```bash
# 准备 node 运行时包（npmmirror 镜像，国内可用）
curl -sL -o node.tar.gz https://registry.npmmirror.com/-/binary/node/v20.18.1/node-v20.18.1-linux-x64.tar.gz
cp apps/server/Dockerfile.sandbox ./Dockerfile
docker build -t lowcode-node-sandbox:20 .
# 指向本地镜像
export WF_SANDBOX_IMAGE=lowcode-node-sandbox:20
```

### M8 验证
```bash
# 1) 隔离层验证（基于 nest build 产物，含容器安全属性自检）
WF_SANDBOX_IMAGE=lowcode-node-sandbox:20 node apps/server/test/m8-verify.cjs     # 18/18
# 2) 运行时 E2E（需起 server 连 MySQL，server 以 container 模式启动）
WF_SANDBOX_MODE=container WF_SANDBOX_IMAGE=lowcode-node-sandbox:20 node dist/main.js &
node test/m8-runtime-e2e.cjs                                                    # 11/11
```
覆盖：vm 回归不破、容器内正常执行、死循环被中断、**容器内非 root（uid=10001）**、**根文件系统只读（EROFS）**、**禁网（仅 lo 网卡）**、**用户脚本拿不到 require**、镜像缺失自动回退并标注；运行时验证审计落库 `isolation=container` 且脚本明文不落库。

## M9 嵌套组件可视化（已交付并真实 E2E 验证）

M7 的建页器只能搭「扁平区块」，做不出真实业务表单。M9 把结构升级为**树形**：容器 / 栅格 / 表单可承载子组件，任意层级嵌套。

- **前端 `PageBuilder.tsx` 重写为树结构**：组件面板分「基础 / 容器」两组；容器节点支持**向内添加子组件**（`＋子组件` 按钮设定插入目标，左侧面板实时提示"插入到 xxx 内"，可一键改回根级）；结构树递归渲染并按层级缩进，容器可折叠；属性面板新增容器标题、栅格列数（0=自适应）、表单提交按钮文字与 `formId`。
  - 树操作（增/删/改/同级移位）全部走路径索引，嵌套层级下定位准确，不误伤兄弟节点。
- **渲染管线 `render-page.ts`**：`grid` 支持 `columns` 固定列数；`form` 渲染 `data-form-id`；`container`/`form` 补齐样式；`children` 递归下钻（本就支持，本轮打通可视化入口）。
- **契约不变**：`PageSchema.nodes` 仍是 `ComponentNode[]`，`children` 为可选树字段——存量扁平页面**无需迁移**即可继续用。

### M9 验证（真实运行时 E2E · 连 MySQL）
`node apps/server/test/m9-e2e.cjs`（需先起 server 连 MySQL）— **18/18 通过**：
1. 创建含 `form → input/select`、`grid → container → text` 三层嵌套的页面 `201`；2. 渲染 HTML 真实体现嵌套层级；
3. 栅格列数生效（`grid-template-columns:repeat(2,1fr)`）；4. 提交按钮文字 / 下拉选项 / 必填标记均生效；
5. 落库保留 `children` 层级与三层嵌套；6. 删除子组件后持久化一致、重新渲染不再出现。

## M6 商业化闭环（已交付并真实 E2E 验证）

把工作流从「演示链路」补成「可商用闭环」：

- **真实表单持久化**：新增 `entities/wf-submission.entity.ts`（`wf_submission` 表）+ `providers.ts` 的 `DbFormStore`（TypeORM）。`trigger.formSubmit` 节点由内存 mock 改为真实落库，业务数据可追溯。
- **租户隔离守卫（rbac 第一层）**：`guards/tenant.guard.ts` + `decorators/current-tenant.decorator.ts`。`TenantGuard` 从 `x-tenant-id` 头解析租户并挂载到请求；`WorkflowService` 对 图定义/运行/页面/审计/统计 全面按 tenantId 隔离，跨租户访问返回 403。生产可将身份来源替换为 API Key / JWT 网关注入。
- **运营视图**：`GET /workflow/stats`（按租户统计运行总数与成功失败分布）、`GET /workflow/audit`（按租户查高风险节点审计）。
- **真实副作用装配**：`WorkflowModule` 通过 `WORKFLOW_SERVICES` provider 注入 DB-backed 表单存储；SMS/OSS 仍保留 console/local 默认实现（生产替换即可，节点代码不动）。

### M6 验证（真实运行时 E2E · 连 MySQL）
`node apps/server/test/m6-e2e.cjs`（需先起 server 连 MySQL）— **12/12 通过**：
1. 创建/运行工作流；2. 脚本产出 `level=HIGH`；3. LLM 返回文本；4. 页面持久化；
5. 审计落库含 `script.eval`+`ai.llm` 且均带 tenantId；6. 统计 `total=1`；
7. 页面 HTML 含动态标题；8. **`wf_submission` 直查 count=1（表单真实落库）**；9. 跨租户访问返回 403。

```bash
# 起基础设施（Docker 已就绪则可跳过）
docker compose up -d mysql redis
# 本地起 server（连本机 MySQL）
cd apps/server && DB_HOST=127.0.0.1 DB_PORT=3306 DB_USER=lowcode DB_PASSWORD=change_me DB_DATABASE=lowcode node dist/main.js
# 另开终端跑 E2E
node apps/server/test/m6-e2e.cjs
```

## M7 可视化 Page Builder（已交付并真实 E2E 验证）

把「连线即生成页面」升级为**独立的可视化建页器**——这是平台级能力，与 workflow 模块同级（见 06 §架构），复用同一份 `PageSchema` 契约与 `renderPageToHtml` 渲染器。

- **后端 `modules/page-builder`**：`PageDef` 实体（`page_def` 表，含 tenantId）+ `PageBuilderService`（CRUD + render）+ `PageBuilderController`（`/api/pages` 的 POST/GET/PUT/`:id/render`）。复用 workflow 引擎的 `renderPageToHtml`，零重复渲染代码。
  - 租户隔离沿用 `TenantGuard`：跨租户读取返回 403，与 workflow 一致。
- **前端 studio `page-builder/`**：`PageBuilder.tsx` 三栏布局——左侧组件面板（文本/图片/按钮/输入框/多行文本/下拉框）、中间结构化列表（选中/上移/下移/删除）、右侧属性编辑器（按组件类型动态字段，下拉选项支持 JSON 编辑）；顶栏含页面名、保存、新建、预览（打开 `/api/pages/:id/render`）、加载已有页。`pageApi.ts` 为对应客户端。App.tsx 原 `页面搭建 (P3)` 占位已替换为真实组件。

### M7 验证（真实运行时 E2E · 连 MySQL）
`node apps/server/test/m7-e2e.cjs`（需先起 server 连 MySQL）— **11/11 通过**：
1. 创建页面 `201` 并返回 ID；2. `/:id/render` 返回 `text/html`；3. HTML 含页面标题与文本/输入框/按钮组件；
4. 同租户可读取（`200`）；5. 跨租户访问返回 `403`；6. 列表接口可用且含刚建页面。

## M5 前端参数编辑器（已交付）

后端 M4 新增的 `script.eval` / `ai.llm` 节点在画布中已可拖入，但原前端只用「整段 JSON 文本框」编辑参数。M5 补齐**按节点类型的结构化编辑器**：

- 新增 `apps/studio/src/workflow/ParamEditor.tsx`：`PARAM_SCHEMAS` 声明各节点字段（text/textarea/number/json）。`script.eval` → 代码多行编辑器；`ai.llm` → 提示词多行编辑器 + 模型/温度/最大Token 字段；其余节点也改为单字段输入（表单ID、标题、组件JSON、手机号、OSS Key 等）。
- `WorkflowNode.tsx`：命中 schema 时渲染 `ParamEditor`（字段即时提交），未命中才回退到 JSON 文本框。
- `WorkflowCanvas.tsx`：`defaultParams` 为 `script.eval`（`setOutput({ ...data })`）与 `ai.llm`（提示词/模型/温度/Token）预填合理默认值。
- **可扩展**：后端新增节点类型，仅需在 `PARAM_SCHEMAS` 登记字段，前端即自动出现对应编辑器，零渲染逻辑改动。

### M5 验证
- `npx tsc --noEmit -p apps/studio/tsconfig.json`：0 错误。
- `npx vite build`：打包成功（`dist/assets/index-*.js` ~307KB）。

## M4 工作流沙箱隔离（已交付 · 商业化安全硬门槛）

工作流的 `script.eval`（用户自定义 JS）与 `ai.llm`（大模型调用）是**高风险节点**，必须经隔离执行 + 配额 + 审计三件套方可商用。

### 交付内容
- `nodes/sandbox.ts`：`runSandboxed(code, bag, opts)` 用 Node `vm` 受限上下文执行——
  - 严格模式 IIFE 包裹，阻断 `this` 逃逸；不暴露 `require/process/fs/Function/Object` 等危险 API；
  - 输入 `data` 深拷贝隔离，仅暴露 `data` 与 `setOutput(v)`；
  - `vm` 同步超时中断死循环 + watchdog 兜底；输出体积 `maxOutputBytes` 配额防内存爆炸；
  - `sha256` 对脚本/提示词取哈希，审计仅存哈希不存明文。
- `nodes/llm.ts`：`LlmProvider` 接口 + `MockLlmProvider`（不连网跑通链路）+ `OpenAiCompatibleLlmProvider`（通义/DeepSeek/Ollama 等）。**密钥仅来自 env（`LLM_API_KEY`），绝不进图 JSON / 前端**。
- `entities/wf-audit.entity.ts`：审计表 `wf_audit`（tenantId / runId / nodeId / nodeType / codeHash / durationMs / status / errorMessage / outputBytes），合规追责依据。
- `registry.ts`：新增 `script.eval`、`ai.llm` 两类节点，执行后回调 `ExecCtx.audit` 写审计；`dag.ts` 注入 `currentNodeId` 定位审计。
- 配置外置：`.env.example` 增 `WF_SANDBOX_TIMEOUT_MS` / `WF_SANDBOX_MAX_OUTPUT_BYTES` / `LLM_BASE_URL` / `LLM_API_KEY` / `LLM_MODEL`。

### 隔离层级与升级路线
- **本层 = 软隔离（vm + 超时 + 配额 + 审计）**：适用于**自托管单租户 / 可信运维**场景。Node `vm` 本身不是安全边界，多租户对外开放脚本编辑时**必须**升级。
- **下一层 = 硬隔离（商业化多租户）**：容器（每租户独立进程 + cgroup 资源限制）/ WebAssembly（WASM 沙箱，如 Wasmer/Wasmtime）+ 配额 + 审计，见 `工程实践-06 §M4`。

### M4 验证（三层全绿）
1. 核心隔离单测 `test/m4-verify.mts`（8/8）：正常脚本、输入隔离、危险 API 不可达、死循环超时、输出配额、LLM mock。
2. server 全量 `tsc --noEmit` + `nest build`：零错误。
3. 整链集成 `test/e2e-m4.cjs`（7/7）：`formSubmit→script.eval→(ai.llm,composePage)`，脚本输出正确、LLM 返回文本、模板注入生效、审计含 script/llm 且带 nodeId/tenantId。

```bash
node --experimental-strip-types apps/server/test/m4-verify.mts   # 核心隔离单测
node apps/server/test/e2e-m4.cjs                                 # 整链集成（需先 nest build）
```
