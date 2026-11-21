# 深度工程审计 A：lowcode-platform（自研参考实现）

> 审计对象（只读）：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/lowcode-platform`
> 前置阅读：`reports/scan3-code.md`（架构结论，本文不重复）、`reports/review-eng-b.md`（B 工程审计，格式对齐）
> 本文路径均相对工程根（下称 `PROJ`）。所有行号取自当前工作区文件实际内容。
> 审计方法：逐文件通读 server 全部源码（main/app.module + workflow 模块 24 文件 + page-builder 模块 4 文件）+ `packages/shared` 4 文件 + `apps/studio` 10 文件 + 全部部署文件（docker-compose / Dockerfile×2 / .env.example / .npmrc / .gitignore / 各 package.json）+ 7 个测试脚本逐断言核对 + README.md 与 交接文档.md 的声明逐条对照代码。共核对了 85 条测试断言、19 处 `process.env` 读取点、全部 12 个 REST 端点。

---

## 0. 结论速览

- **引擎骨架质量高于课程原版 B**：Kahn 拓扑排序/环检测正确、DTO 全局 whitelist、渲染链转义扎实、未发现 N+1 与 mass assignment。交接文档 §7 的"未做边界"清单（多租户 RBAC/云厂商/限流/迁移/Jest）与代码基本对得上，工程自述诚实度高。
- **但 P0 三条成立**：① 全接口无鉴权 + 沙箱默认 vm 模式（硬化可被经典 constructor 链绕过）= 公网部署即未鉴权远程代码执行面；② 租户隔离在 PUT/DELETE 与工作流生成页读取上失效，而 README 明文声称"全面按 tenantId 隔离"（声明与实现不符）；③ server 镜像 Dockerfile 引用不存在的 `pnpm-workspace.yaml`，`docker compose up --build` 必失败，README 的 compose 三服务"一键起"是断的。
- **死循环防护总评**（任务项 1）：图级环检测（Kahn）+ 脚本同步 timeout + 容器宿主强杀三层真实存在；但 `ai.llm`/Provider 无超时可挂死整次 run、vm 模式有内存炸弹窗口、容器模式失败时 fail-open 回退 vm，三个洞使防护不闭环。

## 分级总览

- **P0（安全/正确性/部署硬伤）3 条**：默认 vm 沙箱 + 零鉴权的 RCE 暴露面；租户隔离 PUT/DELETE/生成页读取失效且与 README 声明矛盾；server Dockerfile 构建必失败（pnpm 残留）。
- **P1（质量/可观测/部署）10 条**：容器模式 fail-open 回退、失败原因无处可查（run 无 error 列 + 失败节点无 trace + 异常吞成 500）、LLM/Provider 无超时且 run 无并发控制、vm 模式内存炸弹、compose 关键 env 缺失 + 健康检查未接线、`npm test` 必失败、页面表单→工作流链路实际断开、synchronize:true 无迁移方案、studio 保存永远新建、浅拷贝跨节点可变共享。
- **P2（建议/一致性）16 条**：DTO 无长度限制、ai.llm 失败不审计、死表死字段、body tenantId 可污染归属、沙箱镜像含 redis、.npmrc 是 pnpm 残留、README "new Function" 描述错误等。

---

## P0 —— 安全 / 正确性 / 部署硬伤

### P0-1 全接口零鉴权 × 沙箱默认 vm 模式：公网部署即"未鉴权脚本执行服务"，且 vm 硬化可被绕过

- 暴露面证据：
  - 全服务无任何用户体系/JWT/API Key（scan3 已核）。`apps/server/src/modules/workflow/guards/tenant.guard.ts:13-18`：`TenantGuard` 直接把请求头 `x-tenant-id` 当作可信租户，**任何人可自称任意租户**。
  - `POST /api/workflow/:id/run`（workflow.controller.ts:79-86）同步执行图内任意 `script.eval` 脚本与 `ai.llm` 调用，无并发限制、无频控（`.env.example:22` 的 `RATE_LIMIT_PER_TENANT` 在源码中零引用，grep 验证）。
- vm 硬化可绕过证据：
  - `nodes/sandbox.ts:87-97` 的"尽力移除可逃逸入口"只对 **context 全局对象** `defineProperty(this,'Function'/'globalThis'/'global',undefined)`。
  - 但 `data` 是宿主 realm 里的 `JSON.parse(JSON.stringify(...))` 产物（sandbox.ts:27-33, 76），传入 context 后，`data.constructor.constructor`（即宿主 realm 的 `Function`）不受上述 defineProperty 影响——经典 Node vm 逃逸：`data.constructor.constructor('return process')()` 可拿宿主 `process`，进而 `process.mainModule.require('fs')` 全盘接管主进程。`setOutput`（宿主函数，sandbox.ts:78-80）同样经 `.constructor.constructor` 泄漏宿主 Function。
  - `m4-verify.mts:40-42` 的"危险 API(process)不可达 ✅"只测了裸标识符 `process` 未定义，**测不出 constructor 链逃逸**，给出口径过强的假信心。
- 默认值证据：`nodes/container-sandbox.ts:35` `mode: (process.env.WF_SANDBOX_MODE) || 'vm'`；`.env.example:33` `WF_SANDBOX_MODE=vm`；README 快速开始（README.md:30-39）与 compose server env（docker-compose.yml:24-31）均未设置 container。
- 定性：工程注释/README 自己承认"vm 不是安全边界"（sandbox.ts:61-64、README.md:81），自托管单租户定位下不算秘密武器；但**默认配置 + 零鉴权 + 零频控**的组合，使任何把它跑在可达网络上的部署都是 RCE 服务（vm 逃逸）+ LLM API Key 盗刷面（`ai.llm` 密钥来自 env，llm.ts:85-92）。修复：默认改 container、无鉴权时拒绝 script.eval/ai.llm、加全局限流；博客严禁出现"vm 沙箱防逃逸"表述。

### P0-2 租户隔离在 PUT / DELETE / 工作流生成页读取上失效，与 README"全面隔离"声明直接矛盾

- 证据：
  - `workflow.service.ts:67-75` `update(id, dto)` 内 `await this.get(id)` **不传 tenantId**；`:77-81` `remove(id)` 同样裸查。Controller 侧（workflow.controller.ts:69-72、74-77）根本不取 `@CurrentTenant()`。
  - 对照：`get`（service:57-64）与 `run`（service:87-88）做了跨租户 403，m6-e2e.cjs:63-64 也只测了 **GET** 的 403——写/删路径的洞恰好落在测试盲区。
  - 工作流产出的页面：`workflow.controller.ts:53-62` `GET /workflow/pages/:id` 与 `/:id/render` 不接收 tenant，`workflow.service.ts:156-166` 裸查 → 任意生成页任何人可读可渲染（uuid 可经 `GET /workflow/pages` 列表枚举，service:149-154 带租户过滤，但无租户时返回全部）。
  - page-builder 侧反而是对的：page-builder.controller.ts:51-58 PUT 传了 tenant，page-builder.service.ts:34-39 经 `get(id, tenantId)` 校验——**同一套守卫两个模块行为不一致**，更说明 workflow 侧是遗漏而非设计。
- 矛盾声明：README.md:142「`WorkflowService` 对 图定义/运行/页面/审计/统计 全面按 tenantId 隔离，跨租户访问返回 403」——"图定义（改/删）"与"页面（读/渲染）"不成立。交接文档.md:229 自认"只有 x-tenant-id 头级别的租户过滤"，但那是说无 RBAC，没承认连自家过滤都漏了两条写路径。
- 修复：update/remove 补 `this.get(id, tenantId)` 并透传；工作流生成页读取接入租户校验；补 PUT/DELETE 跨租户负向测试。

### P0-3 server 镜像构建必失败：Dockerfile 引用不存在的 pnpm-workspace.yaml，README"一键起"是断的

- 证据：
  - `apps/server/Dockerfile:4`：`COPY pnpm-workspace.yaml package.json tsconfig.base.json ./` —— 工程根**没有** `pnpm-workspace.yaml`（实测 `ls` 不存在；根 package.json:8 是 `npm workspaces`，配套 `package-lock.json`）。Docker COPY 任一源缺失即整层失败 → `docker compose up --build`（docker-compose.yml:22 `build: { context: ., dockerfile: apps/server/Dockerfile }`）第一步就挂。
  - 第二层断裂：Dockerfile:3 `corepack enable` + `:9` `pnpm install`，而根 package.json:6 `"packageManager": "npm@10.9.7"` —— corepack 会按该字段拒绝运行 pnpm（"This project is configured to use npm"）。即使补上 yaml 也过不去。
  - 工程自身已承认 pnpm 不可用：README.md:33「本机用 npm，pnpm 在本机缺原生二进制」、交接文档.md:137「**不要用 pnpm**」。Dockerfile 是 pnpm 时代残留，与 README/交接文档互相矛盾。
- 连带：`.npmrc:1-2` `node-linker=hoisted` + `package-import-method=copy` 是 **pnpm 专属配置**，npm 不识别——又一个迁移残留物（无害但佐证漂移）。
- 后果：README.md:18「docker-compose.yml # mysql + redis + server 一键起」与交接文档.md:57 的三服务描述不成立；可用路径只有 README.md:36 的 `docker compose up -d mysql redis`（纯基础设施）+ 本地 node 起 server。
- 修复：Dockerfile 改 npm（`COPY package.json package-lock.json` + `npm ci -ws --include-workspace-root`，构建序 shared→server），或恢复 pnpm 工作区并补齐 yaml/lockfile 二选一。

---

## P1 —— 质量问题

### P1-1 容器模式 fail-open：Docker 不可用自动回退 vm 继续执行不可信脚本

- `nodes/container-sandbox.ts:231-237`：`executeWithFallback` 在容器创建/启动失败后 `catch` → 直接 `runSandboxed`（vm 软隔离）返回，仅附 `fallbackReason` 文案。
- 危害：交接文档.md:238 要求多租户"**必须** WF_SANDBOX_MODE=container"——但 Docker 重启/镜像被删/socket 权限变更的瞬间，多租户模式会**静默降级到可逃逸的 vm**（P0-1），审计里虽有 fallbackReason，执行照样发生。安全模式应当 fail-closed：容器不可用即拒绝 script.eval 并告警，而不是退回弱隔离。
- m8-verify.cjs:83-95 还把这个回退当特性测（"业务不中断"）——可用性优先于安全性的取舍被写进了测试。

### P1-2 失败原因三处断链：run 无 error 列、失败节点无 trace、异常对外吞成 500

- `entities/wf-run.entity.ts:5-29`：无 error/errorMessage 字段，失败原因不落库。
- `engine/dag.ts:116`：trace 回调只在节点成功后调用（`await onNode?.(nodeId,'success',...)`），节点抛错直接冒泡 → `wf_run_node` 对失败节点**一行都不写**；`:16` 状态枚举的 `'running' | 'failed' | 'skipped'` 三值从未被写入（grep 全仓只有 'success'）。
- `workflow.service.ts:141-144`：`catch (e) { update status failed; throw e }` —— 普通 `Error` 经 Nest 默认过滤器变成 `{"statusCode":500,"message":"Internal server error"}`，`runDag` 抛出的"检测到环/未知节点类型/脚本节点失败[timeout]"等真实原因**既不进响应也不进库**；studio 端只见"运行失败: POST ... -> 500"（api.ts:16）。
- 修复：wf_run 加 errorMessage 列；失败节点补写 trace（status='failed'）；抛 `HttpException` 携带原始信息。

### P1-3 ai.llm / 副作用 Provider 无超时，run 端点同步等待且无并发控制

- `nodes/llm.ts:61-65`：`fetch(url, {...})` **无 AbortSignal.timeout**——LLM 网关挂起时节点级无限等待（undici 默认 headers timeout ~300s 兜底），整条 run 卡住；`POST /:id/run` 是同步 HTTP（workflow.controller.ts:79-86），请求挂着、`wf_run` 永远 `'running'`（进程重启后成僵尸记录，无清扫机制）。
- `ConsoleSmsProvider`/`LocalOssProvider` 是本地实现不会挂，但 Provider 接口（providers.ts:20-35）没有超时约定，接真实云厂商后同样裸奔。
- 结合 P0-1 的零频控：循环 POST run = 免费把配置好的 LLM API Key 打爆 + DB 堆垃圾 run/audit 行。
- 修复：`AbortSignal.timeout(30000)`；run 改异步任务 + 状态轮询（工程自己预留了 Redis 却没用，见 P2-7）；接口级 throttler。

### P1-4 vm 模式内存炸弹：输出配额不防"执行中"分配，watchdog 是死代码

- `nodes/sandbox.ts:109-118`：`maxOutputBytes` 只在**脚本跑完后**对序列化结果计量；`setOutput("x".repeat(1e9))` 这类 2 秒内分配 GB 级内存的脚本（分配本身远快于 2000ms timeout）会在主进程内 OOM——vm 模式与 Node 主进程同内存，**炸的是 server 本体**。容器模式才受 128MB + MemorySwap=Memory 保护（container-sandbox.ts:130-131）。
- `sandbox.ts:35-49` `withWatchdog` 包裹的是 `Promise.resolve().then(() => vm.runInContext(...))` —— 脚本是同步执行，watchdog 的异步超时永远跑不赢 vm 同步 timeout（sandbox.ts:104），注释"异步滥用由 watchdog 兜底"（sandbox.ts:58）与实现不符，纯装饰。
- 修复：文档明示 vm 模式内存风险；或加 `resourceLimits`（`vm.runInContext` 支持 `maxOldGenerationSizeMb` 等选项，当前未用）。

### P1-5 docker-compose：server 缺全部业务 env、depends_on 不等健康、Redis 纯空跑

- `docker-compose.yml:24-31`：server 环境变量只有 DB/REDIS——`WF_SANDBOX_MODE/IMAGE/*`、`LLM_*`、`CORS_ORIGINS`、`SERVER_PORT` 全未传 → 容器化部署永远是 vm 模式 + mock LLM + CORS 全开（main.ts:14-15 未配即全开），与交接文档对 container 模式的要求脱节。
- `:23` `depends_on: [mysql, redis]` 短格式只等容器启动不等健康（mysql 的 healthcheck 在 `:12-15` 定义了却没人消费）；`synchronize:true` 启动即连库，MySQL 未就绪时 server 直接崩，且无 `restart` 策略。
- redis 服务（`:17-19`）无密码、端口映射宿主，而 server 源码零引用 Redis（grep 验证，scan3 结论维持）——纯占位还开了攻击面。
- 修复：`depends_on: {mysql: {condition: service_healthy}}`；补 env；redis 加密码或干脆从 compose 移除。

### P1-6 `npm test` 必失败：package.json 声称 Jest，仓库里 0 个 spec

- 根 package.json:13 `"test": "npm run test --workspaces --if-present"` → server package.json:10 `"test": "jest"`；但全仓无 jest.config、server package.json 无 jest 配置段、无任何 `*.spec.ts`（find 验证），jest 依赖（server package.json:34-37 `jest/ts-jest/@types/jest/@nestjs/testing`）纯闲置。`npx jest` = "No tests found" **exit 1** → 根 `npm test` 直接报错。
- 真实测试是 7 个手写脚本（见下文测试矩阵），交接文档.md:234 自认"非 Jest"，但 package.json 的口径会误导任何 CI/接手者按 `npm test` 跑。
- 修复：`"test"` 改为按套件逐个执行脚本的编排（或补 `--passWithNoTests` 的真实 jest 配置），删除闲置依赖。

### P1-7 "页面表单 → 工作流"链路实际是断的：渲染页表单无处提交，formSubmit 数据只来自图参数

- `engine/render-page.ts:26`：`<form class="lc-form" data-form-id="...">` **没有 action、没有任何提交端点、没有一段 JS**；渲染 HTML 是纯静态（README.md:122 自述"无交互逻辑"）。
- `nodes/registry.ts:79-85`：`trigger.formSubmit` 的数据来源是 `inputs['out'] ?? params['data']` —— 即**图参数里手填的 JSON**，不是真实页面提交。全服务无任何接收渲染页表单提交的端点（交接文档.md:169-183 API 表可证）。
- 后果：`page_def` 页面的 `formId` 与 `wf_submission` 之间没有数据通路；"搭建表单页 → 用户提交 → 触发工作流"的故事线只存在于参数模拟。README.md:69 M3"预置节点端到端打通（form/…→ render）"是各自成环，不是业务闭环。
- 博客红线：不可写"页面表单提交自动触发工作流"。

### P1-8 `synchronize: true` 无迁移方案，注释指向不存在的文档

- `app.module.ts:18`：`synchronize: true` 注释"仅开发期；生产用迁移脚本（见 README）"——README 全文（215 行）**没有一处迁移内容**（grep '迁移/migration' 仅命中"无需迁移"的 schema 兼容表述）；全仓无 migrations 目录、TypeORM 配置无 migrations 路径。交接文档.md:233 自认未做，但代码注释把读者指去了不存在的地方。
- 连带：`app.module.ts:9` 引入 `ConfigModule.forRoot({isGlobal:true})` 但全部 19 处配置读取都是裸 `process.env`（grep 验证），ConfigService 从未被注入——装了闸门没人用，新人对"配置体系"的认知会被误导。
- 修复：接手者落地 TypeORM migration 前后改掉注释；ConfigModule 要么真用（ConfigService 注入）要么删。

### P1-9 studio 保存永远新建图：图表只增不减，PUT 端点前端不用

- `apps/studio/src/workflow/WorkflowCanvas.tsx:145-160`：`onSave` 每次都调 `api.create(toGraph())`（api.ts:24-25 POST），`currentId` 只用于运行，不回写更新；后端 `PUT /api/workflow/:id`（controller:69-72）**前端零调用**（grep studio 无 `api.update`/PUT workflow）。
- 后果：编辑→保存 N 次 = N 行 `wf_graph` 垃圾，列表下拉越来越长且无删除入口（`DELETE` 前端同样零调用）。页面搭建侧反而正确（PageBuilder.tsx:220-236 savedId 有则 update）。
- 修复：onSave 按 currentId 分流 create/update；列表项加删除。

### P1-10 transform.map 浅拷贝 + setPath 深写：跨节点可变共享，破坏"纯函数"引擎设定

- `nodes/registry.ts:91-95`（setField）：`const cp = { ...src }` 浅拷贝后 `setPath(cp, ...)`（`:68-76`）沿路径深写——路径穿过嵌套对象时写的是 `src` 的子对象引用；`:102-106`（pickTo）同构。
- `dag.ts:115` `outputs[nodeId] = out` 按引用共享：下游 transform 改了嵌套字段，上游节点已记录的 `outputMd` trace（workflow.service.ts:119-121 存的是同一引用的序列化结果）与下游实际消费的数据产生**时间线不一致**；同一上游输出被多条边共享时，一条支路的 setField 会污染另一条支路的输入。dag.ts:89 注释"纯函数、无 HTTP 依赖"被执行器打破。
- 修复：setField/pickTo 改结构化深拷贝（`structuredClone`）或写时复制。

---

## P2 —— 建议

1. **DTO 无长度/格式约束**：`create-workflow.dto.ts:20` name 仅 `@IsString()`（DB varchar(255)，超长 → MySQL 1406 → 500）；page-builder.controller.ts:18 同（varchar(128)，page-def.entity.ts:22-23）。建议 `@MaxLength` + `@Matches`。
2. **ai.llm 失败不审计**：registry.ts:174-179 审计写在 `llm.complete` 成功返回之后，异常直接冒泡——与 script.eval 的 success/error/timeout 三态审计（:145-161）不对称，LLM 网关故障在 `wf_audit` 无痕。
3. **审计写失败会拖垮节点执行**：registry.ts:26-33 `await ctx.audit(...)` 在执行器内，audit 落库异常 = 节点失败 = run 失败。审计 sink 应自吞异常降级。
4. **render 健壮性**：render-page.ts:17 `opts.options as 数组` 直接 `.map`，PageBuilder 下拉选项经 JSON 文本框可被改成对象/字符串（PageBuilder.tsx:573-585）→ `GET /render` 500；workflow.service.ts:164、page-builder.service.ts:57 `JSON.parse(schemaJson)` 无兜底（当前写入端恒 stringify，属埋雷）。
5. **死表死字段**：`wf_node_def` 实体注册了 forFeature、service 注入了 repo（workflow.service.ts:22, workflow.module.ts:22）但**零使用零种子**——节点目录实际来自内存 `NODE_CONTRACTS`（service:53-55）；`wf_graph.status`（'published' 分支无人写，service:34-43,67-75）与 `ownerId`（wf-graph.entity.ts:26）从未赋值。
6. **RunWorkflowDto.tenantId 客户端可控**（run-workflow.dto.ts:6）：无 header 时 `effectiveTenant = tenantId ?? dto.tenantId`（workflow.service.ts:89），body 里的 tenantId 会成为 run/audit/submission 行的归属标注（不能借它过 `get` 校验，但可伪造计量与审计归属）。建议删掉 body 侧来源。
7. **compose 细节**：`version: '3.8'` 已废弃；3306/6379 映射宿主（`:10,19`）暴露面；无 `.dockerignore`（构建上下文 = 整个仓库含 .git/package-lock）；redis 无数据卷也无密码。
8. **Dockerfile.sandbox 基于 `redis:7`**（Dockerfile.sandbox:4）：沙箱镜像内自带 redis 服务端二进制——NetworkDisabled 下不可达，但属多余攻击面与体积；且构建需手动预下载 node.tar.gz（README:101-110 已说明，属门槛非 bug）。
9. **README 与代码不符一处**：README.md:87「用户脚本经 `new Function` 执行」——实际 RUNNER 用 `vm.createContext` + `vm.runInContext`（container-sandbox.ts:66-73）。结论方向没错（脚本拿不到 runner 的 require），实现描述错了。
10. **日志体系为零**：全服务仅 main.ts:20 一处启动 console.log；无 Nest Logger、无请求日志、无错误堆栈落盘；`ConsoleSmsProvider` 把手机号明文打进 stdout（providers.ts:83，接真实网关前是隐私雷）。
11. **studio 全程无租户头**：api.ts:11-18 与 pageApi.ts:14-21 都不注入 `x-tenant-id` → 前端永远无租户身份：建页 tenantId=null、列表看全部（交接文档.md:163 自认）。租户功能在 UI 层完全不可见，演示价值打折。
12. **快速开始缺前置构建**：README.md:30-39 直接 `npm run dev --workspace=@lowcode/server`——`@lowcode/shared` 的 main 指向 `dist/index.js`（packages/shared/package.json:5-6），fresh clone 未先 `npm run build -w @lowcode/shared` 时 server/studio 均因模块解析失败起不来（根 build 脚本有依赖序，dev 没有）。交接文档 §4.3 有正确姿势，README 缺。
13. **getStats 细节**：workflow.service.ts:173-174 `'1=1'` 分支仍传 `{t: tenantId}` 冗余参数；`listAudit` limit 固定 50 不可配（controller:48-51）。
14. **MemoryFormStore 无上限**（providers.ts:61-76）：仅在 ctx.services 缺失时启用（registry.ts:82 等三处 `?? DEFAULT_SERVICES`），生产路径恒走 DbFormStore，风险低但建议加容量上限防误用。
15. **前端循环检测重复实现**：WorkflowCanvas.tsx:109-123 手写 DFS 与 dag.ts:62-85 的 Kahn 并存，两套判定（DFS 递归深图有栈溢出理论风险）——建议复用 shared 包抽出单一实现。
16. **`PageSchema.version` 声明了版本化纪律却无人校验**：shared/page-schema.ts:28-33，写入恒 1，读取端（render/load）从不检查——契约注释（page-schema.ts:4 "破坏性变更走版本化"）目前是空头支票。

---

## 附：7 个测试套件覆盖矩阵（任务项 4）

全部为**手写自包含脚本**（.cjs/.mts），非 Jest 框架（交接文档.md:234 自认）。共 85 条断言，逐条与脚本核对一致（README/交接文档标注的 8/7/18/12/11/11/18 均吻合）：

| 脚本 | 断言数 | 前置 | 覆盖内容 | 盲区 |
|---|---|---|---|---|
| test/m4-verify.mts | 8 | 无 | vm 沙箱单元行为：正常执行、输入深拷贝隔离、裸 `process` 不可达、同步死循环 timeout、输出配额、LLM mock | **测不出 constructor 链 vm 逃逸**（P0-1）；内存炸弹 |
| test/e2e-m4.cjs | 7 | nest build | DAG 引擎集成冒烟（formSubmit→script→(llm,composePage)）、审计回调、模板注入 | 无 DB、无环图负例、无边引用不存在节点负例 |
| test/m6-e2e.cjs | 12 | 活 server+MySQL | REST 建图/运行、wf_submission 直查落库、审计/统计端点、GET 跨租户 403、页面渲染 | **PUT/DELETE 跨租户负例缺失**（恰是 P0-2 的洞） |
| test/m7-e2e.cjs | 11 | 同上 | page CRUD、render HTML 内容、page 跨租户 403、无租户列表 | 无 schema 超长/非法 options 负例 |
| test/m8-verify.cjs | 18 | nest build+Docker | 容器硬隔离全项：正常执行、死循环强杀、uid≠0、只读根 EROFS、禁网仅 lo、脚本拿不到 require、回退语义+标注 | 把 fail-open 回退当特性测（P1-1） |
| test/m8-runtime-e2e.cjs | 11 | server 以 container 模式跑 | 业务链路经容器：审计 isolation=container、codeHash 64 位、**脚本明文不落库**、生成页渲染 | 无回退触发时的审计断言 |
| test/m9-e2e.cjs | 18 | 活 server+MySQL | 嵌套渲染三层（form>input/select、grid>container>text）、columns 生效、增删子组件落库一致性 | 无深层嵌套（>3 层）与环形 children 防御 |

- 覆盖强项：沙箱行为矩阵、容器安全属性自检（probe）、租户隔离正向、嵌套渲染回归——远好于 B 工程（0 测试）。
- 结构性盲区：全部负向安全测试只有"GET 跨租户"一条；DTO/校验层零测试；并发零测试；前端（studio）零测试；无 CI 配置（仓库内无 .github/ 云效文件）。

---

## 博客表述风险清单（cards/blog 成稿修正依据）

| # | 博客/cards 可能的说法 | 风险 | 建议表述 |
|---|---|---|---|
| 1 | "ComfyUI 式 DAG 工作流引擎（Kahn 拓扑排序+环检测）" | 无风险，代码支撑扎实（dag.ts:62-85 环检测+边引用校验） | 可放心展开；可补一句"按拓扑序串行执行，无并行调度"避免读者以为有并行 |
| 2 | "vm/容器双沙箱" | 双沙箱存在属实；但 vm 硬化（Function/globalThis 置空）可被 `data.constructor.constructor` 经典链绕过（sandbox.ts:87-97），m4 测试给的是假信心；容器模式失败静默回退 vm（container-sandbox.ts:231-237） | 写"vm 软隔离**不是安全边界**（工程注释原文 sandbox.ts:61-64，可直接引用）+ 容器硬隔离（CapDrop ALL/禁网/只读根/非 root/限额/probe 自检）"；点破"容器不可用自动回退 vm 是 fail-open 设计"——这本身就是好素材 |
| 3 | "AI 卡（LLM 节点）密钥安全：仅 env、不进图 JSON、不下发前端" | **属实**（llm.ts:85-92 工厂仅读 env；图 JSON 只存 prompt/model；grep 验证无泄漏路径） | 可放心写；但注明默认 MockLlmProvider（占位输出），真实网关无超时无重试（llm.ts:61-65），不是生产级接入 |
| 4 | "多租户隔离已实现" | **与实现不符**：update/delete 不校验租户（workflow.service.ts:67-81）、工作流生成页读取不校验（controller:53-62）；且租户身份=自报 header（tenant.guard.ts:13-18）；README:142"全面隔离"说法过强 | 降格为"tenantId 预留 + 头级过滤（读路径）"；如实写"写路径（改/删）漏了校验"作为案例；交接文档.md:229 的自认原文可引用 |
| 5 | "技术栈含 Redis 7" | Redis 在 compose 里空跑，server 源码零引用（grep 验证，README.md:25 自己都写进技术栈了） | 从"实际使用的技术栈"里删掉；可写"预留了 Redis 位未接线" |
| 6 | "docker-compose 一键起三服务" | server 镜像构建必失败（Dockerfile:4 引用不存在的 pnpm-workspace.yaml + corepack/packageManager 冲突） | 改为"compose 起 mysql+redis，server 本地 node 跑"；或把 Dockerfile 修复后再写 |
| 7 | "3 构建 + 7 测试套件全绿 / 12/12、11/11、18/18" | 断言数与脚本一致（本次逐条核对无误），但全部是**手写冒烟脚本**，`npm test`（jest）实为 0 测试且 exit 1；无 CI | 可引用具体通过数并注明"脚本化冒烟、需活库活服"；严禁写成"Jest 测试保障/CI 门禁" |
| 8 | "表单页提交触发工作流" | **链路不存在**：渲染页 form 无 action 无端点（render-page.ts:26），formSubmit 数据只来自图参数（registry.ts:79-85） | 删除该表述；或写"表单触发目前是 run 参数模拟，页面→工作流的数据通路是留白" |
| 9 | "审计计量：codeHash 不存明文" | script.eval 侧属实且被测试断言（m8-runtime-e2e.cjs:68）；但 ai.llm 失败路径不审计（registry.ts:174） | 可写，补一句"LLM 失败路径审计是缺口" |
| 10 | "服务端渲染 + 全量转义防注入" | **正面项，核实通过**：render-page.ts:3-5 esc 覆盖文本/属性/标题，grid 列数走 Number 强转，本次审计未发现注入点 | 可放心写（本工程稀缺的纯正面项）；可对比 B 工程 SSR 跳过消毒的翻车点 |
| 11 | "可商用 / 生产就绪 / M0-M9 全部交付" | P0×3 + 限流/迁移/JWT 全未做；交接文档.md:22 自认"参考实现，不是成品 SaaS" | 统一降格为"教学级生产化参考实现"；README 的"商业化就绪"章节（README.md:51-59）逐条都要打对折引用 |
| 12 | "限流/计量已配置外置" | `.env.example:22` `RATE_LIMIT_PER_TENANT`、`:25` `SANDBOX_ENABLED` 源码零引用（grep 验证）——死配置 | 写"预留 env 钩子，未实现"（交接文档.md:231 口径正确） |
| 13 | "9 种组件物料、前后端共用契约" | 属实：PALETTE 9 类（PageBuilder.tsx:24-34），render-page 9 分支，契约在 shared（page-schema.ts） | 无风险；注意组件是 HTML 拼装不是 React 组件库（对比 B 的 15 种真组件） |
| 14 | 出处红线总核对 | **「出自自研参考实现」标注是正确且必要的**：工作流/DAG/沙箱/AI 卡/审计/容器隔离/租户预留全部只存在于工程 A；课程原版 B 无任何此类内容（scan3 §6 已核）。反向红线：A 无用户体系/JWT/验证码/微信登录/OSS 真传/统计图表——不要把 B 的鉴权事迹写进 A 的故事 | 涉工作流、沙箱、AI 卡的 cards 一律带「出自自研参考实现 lowcode-platform，非课程原始配套代码」；涉鉴权/验证码/OSS 的 cards 归 B，勿混 |

---

### 修正优先级建议（落地顺序）

1. **成稿即改口径（无需改代码）**：#4、#5、#6、#7、#8、#11、#12——尤其 #8（表单触发）与 #4（多租户）是本次新发现的与 README 直接矛盾的点。
2. **低成本修代码再成稿（半天）**：P0-2（update/remove 补 tenantId 三行 + 补负向测试）、P0-3（Dockerfile 换 npm 化重写）、P1-9（onSave 分流 update）、P1-6（test 脚本编排化）。
3. **高价值但需设计（可开续篇）**：P0-1/P1-1（默认 container + fail-closed + 鉴权/限流）、P1-2（失败可观测闭环）、P1-3（run 异步化 + LLM 超时）、P1-8（TypeORM migration）。

---

## 附：本次审计引用文件索引（相对 PROJ）

```
PROJ=/Users/Wang/Code/github/web-x-blog/work/source/25.xiaodi-lowcode/小滴课堂低代码大课/lowcode-platform
package.json · .npmrc · .gitignore · .env.example · docker-compose.yml · README.md · 交接文档.md
apps/server/package.json · apps/server/Dockerfile · apps/server/Dockerfile.sandbox
apps/server/src/main.ts · src/app.module.ts
apps/server/src/modules/workflow/workflow.{module,controller,service}.ts
apps/server/src/modules/workflow/engine/{dag.ts, render-page.ts}
apps/server/src/modules/workflow/nodes/{registry.ts, sandbox.ts, container-sandbox.ts, llm.ts, providers.ts}
apps/server/src/modules/workflow/guards/tenant.guard.ts · decorators/current-tenant.decorator.ts
apps/server/src/modules/workflow/dto/{create-workflow.dto.ts, run-workflow.dto.ts}
apps/server/src/modules/workflow/entities/{wf-graph, wf-node-def, wf-run, wf-run-node, wf-generated-page, wf-submission, wf-audit}.entity.ts
apps/server/src/modules/page-builder/{page-builder.controller.ts, page-builder.service.ts, page-builder.module.ts, entities/page-def.entity.ts}
apps/server/test/{m4-verify.mts, e2e-m4.cjs, m6-e2e.cjs, m7-e2e.cjs, m8-verify.cjs, m8-runtime-e2e.cjs, m9-e2e.cjs}
packages/shared/src/{page-schema.ts, workflow-contract.ts, tenant.ts, index.ts} · packages/shared/package.json
apps/studio/src/App.tsx · src/main.tsx · vite.config.ts
apps/studio/src/workflow/{WorkflowCanvas.tsx, WorkflowNode.tsx, Palette.tsx, ParamEditor.tsx, api.ts, types.ts}
apps/studio/src/page-builder/{PageBuilder.tsx, pageApi.ts}
```
