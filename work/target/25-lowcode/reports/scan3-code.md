# 扫描3：代码技术点核实报告

数据源（均只读，忽略 node_modules/dist/.next）：
- 工程 A：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/lowcode-platform`（自研参考实现）
- 工程 B：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课/course-reference/lowcode-platform-full`（课程完整参考实现）

---

## 1. 工程架构与技术栈版本（逐个核实自 package.json）

### 工程结构

**A（lowcode-platform）**：npm workspaces（`workspaces: ["packages/*", "apps/*"]`），packageManager=npm@10.9.7，Node ≥18。
- `packages/shared`：平台级契约（`@lowcode/shared`）—— PageSchema / WorkflowContract / TenantScoped 纯类型，无组件
- `apps/server`：NestJS 后端（`@lowcode/server`），模块仅两个：`workflow` + `page-builder`
- `apps/studio`：创作端前端（`@lowcode/studio`）
- `docker-compose.yml`：mysql + redis + server 三服务
- 定位：工作流编排（ComfyUI 式 DAG）+ 页面搭建，服务端渲染 HTML；自述 M0~M9 全部交付

**B（lowcode-platform-full）**：pnpm workspace（pnpm-workspace.yaml + pnpm-lock.yaml），Node ≥18。
- `packages/share`：共享包（`@lowcode/share`）——15 种低代码 React 组件 + 全部类型 + 工具函数，unbuild 打包（ESM/CJS 双格式），依赖 dompurify
- `packages/server`：NestJS 后端 API
- `packages/client`：B 端编辑器 + 数据统计（React + Vite + AntD5 + Tailwind + MobX + dnd-kit）
- `packages/release`：C 端发布页（Next.js 14 App Router + SSR）
- `nginx/` + 4 个 Dockerfile + docker-compose + `docs/API.md` + `docs/schema.sql`
- 定位：H5 拖拽搭建 → 发布 → C 端访问 → 问卷收集 → 数据统计 的完整业务闭环

### 版本核实表（直接抄自各 package.json，非编造）

| 依赖 | A-server | B-server | A-studio | B-client | B-release |
|---|---|---|---|---|---|
| @nestjs/common | ^10.3.0 | ^10.0.0 | — | — | — |
| @nestjs/typeorm | ^10.0.0 | ^10.0.1 | — | — | — |
| typeorm | ^0.3.20 | ^0.3.17 | — | — | — |
| mysql2 | ^3.9.0 | ^3.6.3 | — | — | — |
| @nestjs/jwt + passport-jwt | 无 | ^10.2.0 / ^4.0.1 | — | — | — |
| react | — | — | ^18.2.0 | ^18.2.0 | ^18 |
| vite | — | — | ^5.1.0 | ^5.0.0 | — |
| next | — | — | — | — | 14.0.4 |
| antd / @ant-design/icons | — | — | 无（无 AntD） | ^5.11.2 | ^5.11.2 |
| mobx / mobx-react-lite | — | — | 无 | ^6.12.0 / ^4.0.5 | — |
| @dnd-kit/core/sortable | — | — | 无 | ^6.1.0 / ^8.0.0 | — |
| reactflow（React Flow） | — | — | ^11.10.0 | 无 | — |
| typescript | ^5.4.0 | ^5.2.2（根） | ^5.4.0 | — | ^5 |
| echarts | — | — | — | ^5.4.3 | — |
| ioredis / svg-captcha / ali-oss | redis 依赖有 host 但 server 未用 | ioredis ^5.3.2 / svg-captcha ^1.4.0 / ali-oss ^6.19.0 | — | — | — |
| dockerode | ^4.0.2（容器沙箱） | 无 | — | — | — |

A 的 docker-compose 里 redis 已起、.env 也配了 REDIS_HOST，但 server 源码实际没 import ioredis/redis 模块（无 RedisModule）——Redis 对 A 是预留，未真实使用。
B 的 server 确有 RedisModule（`src/utils/modules/redis.module.ts`），用于验证码防刷、微信扫码状态等。

---

## 2. 后端核心设计

### A（apps/server）

- **模块**：`WorkflowModule` + `PageBuilderModule`，全局 `ConfigModule` + `TypeOrmModule`（MySQL，`synchronize: true` 仅开发期）。全局前缀 `/api`，启用 ValidationPipe(transform+whitelist)，CORS 可由 `CORS_ORIGINS` 锁域名。
- **实体/表（7 张 wf_* + 1 张 page_def）**：
  - `wf_graph`（name/version/graphJson JSON/status draft/tenantId）
  - `wf_node_def`、`wf_run`、`wf_run_node`（节点级追踪 inputMd/outputMd/durationMs）
  - `wf_generated_page`（工作流产出的页面持久化）、`wf_submission`（表单提交落库）、`wf_audit`（脚本/LLM 审计：codeHash、isolation 'vm'|'container'、outputBytes）
  - `page_def`（页面定义：tenantId/name/schemaJson text）
- **鉴权**：没有用户体系/JWT/RBAC。只有 `TenantGuard`：读 `x-tenant-id` 请求头注入 `req.tenantId`，Service 做跨租户 Forbidden 拦截。注释明确"生产应校验 API Key/JWT 映射为可信 tenantId"——即多租户是预留层，不是完整鉴权。
- **低代码 schema 存储**：页面 = 一份 `PageSchema` JSON（version/title/nodes，节点含 type/options/children 递归嵌套），序列化存 `schemaJson` text。契约在 `packages/shared/src/page-schema.ts`，前后端共用。
- **工作流引擎**（核心亮点）：
  - `engine/dag.ts`：Kahn 拓扑排序（检测环抛错）→ 按序执行 → 沿边注入下游输入端口 → 节点级 trace 回调。纯函数无 HTTP 依赖。
  - `nodes/registry.ts`：7 类节点契约与执行器：`trigger.formSubmit`、`transform.map`（setField/pick/pickTo/concat）、`ui.composePage`（支持 `{{data.x}}` 模板注入生成 PageSchema）、`action.sendSms`、`action.ossUpload`、`script.eval`、`ai.llm`。契约（NODE_CONTRACTS）前后端同源，前端画布直接消费。
  - `nodes/sandbox.ts`：Node vm 软隔离执行用户脚本——严格模式 IIFE、封 `Function/globalThis/global`、静默 console、同步 timeout + 异步 watchdog、输出 256KB 配额，结果标注 `isolation:'vm'`。
  - `nodes/container-sandbox.ts`：M8 容器硬隔离——dockerode 起一次性容器（CapDrop ALL / no-new-privileges / 非 root / 只读根 / 禁网 / 128MB / 0.5 核 / pids 64），容器内再套一层 vm；失败自动回退 vm 并如实标注 `fallbackReason`。
  - `nodes/llm.ts`：LLM Provider 工厂——有 `LLM_BASE_URL + LLM_API_KEY` 走 OpenAI 兼容网关（通义/DeepSeek/Ollama），否则 Mock；密钥只来自 env，不进图 JSON、不下发前端。
  - `nodes/providers.ts`：副作用可替换 Provider 接口（SmsProvider/OssProvider/FormStore），默认 console/local/memory 实现，表单存储已落库 `wf_submission`（DbFormStore）。
- **发布/渲染**：`render-page.ts` 把 PageSchema 服务端渲染成自包含 HTML（转义处理，支持 text/input/textarea/select/button/image/form/grid/container 嵌套），接口 `GET /api/pages/:id/render` 返回 `text/html`。
- **关键接口清单（A）**：
  - pages：`POST/GET /api/pages`、`GET/PUT /api/pages/:id`、`GET /api/pages/:id/render`
  - workflow：`POST/GET /api/workflow`、`GET /api/workflow/nodes`（节点目录）、`GET /api/workflow/stats`、`GET /api/workflow/audit`、`GET /api/workflow/pages`、`GET /api/workflow/pages/:id/render`、`GET/PUT/DELETE /api/workflow/:id`、`POST /api/workflow/:id/run`

### B（packages/server）

- **模块**：`UserModule`、`LowCodeModule`、`ResourcesModule`、`WechatLoginModule` + 全局 RedisModule/JwtModule；`config.ts` 全 env 化且启动强校验（required() 缺配置直接抛错）。
- **实体/表（5 张，docs/schema.sql 可直接建库）**：
  - `user`（username/head_img/phone/password/open_id）
  - `page`（account_id/page_name/components simple-array=组件 id 顺序串/tdk/desc）
  - `component`（type/page_id/account_id/options simple-json）
  - `component_data`（page_id/user=MD5(ip+ua) 匿名标识/props simple-json 问卷答案）
  - `resources`（url/account_id/type image|video/name）
- **鉴权（JWT + 全局守卫 + @Public 白名单）**：passport-jwt Strategy（Bearer token），`JwtAuthGuard` 以 `APP_GUARD` 全局注册，默认拦截一切、`@Public()` 显式豁免——注释明言"杜绝新接口忘加守卫"。validate 里二次查库、抹除 password。登录方式：密码登录、手机验证码登录、微信扫码登录（公众号 XML 回调 + Redis 存扫码状态 + 前端轮询 check_scan）+ 验证码防刷体系（svg-captcha 图形码 Redis 60s、短信码 60s 防重、key=MD5(ip+ua)）。
- **schema 存储/发布流程**：与 A 的"整页 JSON"不同，B 是关系化存储——页面一行 + 每个组件一行（options JSON），page.components 存组件 id 顺序。发布走事务（QueryRunner）：查该用户页面 → 存在则"先置空 components、删旧组件行、插新组件行"（保留 component_data 问卷数据，注释注明是对原课程实现的修正），不存在则新建。
- **关键接口清单（B，docs/API.md 共 20 个）**：`/user/captcha|send_code|register|password_login|phone_login`；`/wechat_login/login|callback(GET+POST)|check_scan`；`/low_code/release(POST 🔒)|release_with_user 🔒|release?id= 公开|is_question_data_posted|question_data(GET 提交 POST)|question_components|get_question_data_by_id`；`/resources/upload 🔒|DELETE 🔒|GET 🔒`。统计侧配套 ECharts 饼图/柱状图、ExcelJS 导出 + JSZip 压缩包（前端做）。
- **统一响应**：`{code, data, msg}`，全局异常过滤器 + 响应拦截器（AbnormalFilter/ResponseIntercept）。

---

## 3. 前端核心设计

### A studio（apps/studio，~1000 行，极简）

- 无状态管理库、无 AntD、无路由库：App.tsx 两个 tab 按钮（工作流编排 / 页面搭建）useState 切换。
- **工作流画布**（WorkflowCanvas.tsx，332 行）：React Flow 11（`useNodesState/useEdgesState/addEdge`，Background/Controls/MiniMap），自定义节点类型 `WorkflowNode`，按节点契约渲染端口（portType 按类型着色），Palette 拖入节点，ParamEditor 编辑参数（script/llm 专用面板），运行后展示日志与生成页面链接。
- **页面搭建**（PageBuilder.tsx，662 行）：物料面板（基础：文本/图片/按钮/输入框/多行/下拉；容器：container/grid/form）+ 组件树编辑（容器可嵌子组件，树形增删/移动）+ 选中编辑 options；数据存本地 state，通过 `pageApi`（fetch 封装）CRUD 到 `/api/pages`，渲染直接用 `GET /api/pages/:id/render` 的服务端 HTML（iframe/链接方式）。
- schema→UI 流程：PageSchema JSON → 后端 renderPageToHtml → 静态 HTML。前端不做渲染引擎，渲染闭环在服务端。

### B client（packages/client，完整编辑器）

- **状态管理 MobX**（`makeAutoObservable`）：`store/components.ts`（compConfigs 组件属性表 + sortableCompConfig 顺序数组 + currentCompConfig 选中项 + copyedCompConig 复制缓冲 + 撤销/重做经 `mobx-shallow-undo`），`store/page.ts`（title/desc/tdk），`store/auth.ts`。mobx-react-lite observer 订阅。
- **编辑器三栏**：左 `EditorLeftPanel/ComponentList`（物料列表）→ 中 `EditorCanvas`（`SortableContainer` dnd-kit：MouseSensor 2px 激活 + closestCenter 碰撞 + verticalListSortingStrategy 排序；选中包蓝框、hover 提示、上下移动/删除工具栏）→ 右 `EditorRightPanel`（ComponentFields 组件属性 + GlobalFields 页面级 TDK）。快捷键 `useComponentKeypress`（复制/粘贴/删除/撤销/重做）。
- **schema→UI**：`@lowcode/share` 导出 `getComponentByType(type)` 工厂，编辑器画布与 C 端渲染端共用同一套 15 种组件（text/swiper/list/image/video/card/split/richText/qrcode/alert/input/textArea/radio/checkbox/empty），组件与 Props 编辑面板一一配对（`LowCodeXxx/XxxComponentProps.tsx`）。dompurify 用于富文本消毒。
- **页面级操作**：草稿（localStorage）、预览页、一键发布（调 `/low_code/release`）、资源中心（OSS 上传/复用）、数据统计页（ECharts + Excel 导出）。
- 工程化：vite manualChunks 拆 vendor-react/vendor-antd/vendor-charts/vendor-editor 四组缓存。
- **release 包**：Next.js 14 App Router，`src/app/[id]/page.tsx` Server Component 直接 fetch `/low_code/release?id=`（SSR、cache:no-cache），`ComponentRender`（client）渲染 + 输入类组件受控收集答案 + 问卷提交/防重复（useImmer 局部状态）。

---

## 4. A 与 B 差异对比

| 维度 | A lowcode-platform | B lowcode-platform-full |
|---|---|---|
| 定位 | 工作流编排平台 + 轻量 Page Builder（自研复刻，面向可商用/SaaS 化） | 面向课程完整业务的 H5 搭建平台（编辑器→发布→C端→问卷→统计） |
| 新旧/完成度 | 版本号 0.1.0，README 自述 P0→M9 全部交付（含运行时 E2E 记录），设计更"新"（2024+ 风格：AI 节点、容器沙箱、多租户预留、审计计量） | 课程原始实现（schema.sql 数据日期 2023-11，Next 14.0.4/antd 5.11），但含 README/docs/API.md/schema.sql/CI 配套，文档完整度高 |
| 鉴权 | 无用户体系，仅 x-tenant-id 头（预留） | JWT 全局守卫 + 三种登录 + 验证码防刷 + 微信扫码，完整 RBAC 前置 |
| schema 模型 | 整页 PageSchema JSON 递归树（shared 契约） | 关系化三表（page/component/component_data）+ 组件顺序数组 |
| 渲染 | 服务端 renderPageToHtml 输出静态 HTML（无交互逻辑，仅表单结构） | C 端 Next.js SSR + React 组件渲染（问卷可交互提交） |
| 组件物料 | 9 种（无真实组件库，HTML 拼装） | 15 种真实 React 组件（share 包双格式分发） |
| 独有能力 | DAG 工作流引擎、vm/容器双沙箱、LLM 节点、审计/统计端点、租户隔离、共享契约包 | 完整用户/资源/统计/微信登录、Nginx 网关部署、docs 文档、事务化发布 |
| 互相缺什么 | A 缺：用户/JWT、真实组件库、C 端发布页、资源中心、问卷统计、Redis 实际使用 | B 缺：工作流引擎、沙箱、AI 能力、多租户、共享渲染契约（share 有组件但无 PageSchema DSL） |
| 包管理 | npm workspaces + package-lock.json | pnpm workspace + pnpm-lock.yaml |

结论：两者不是新旧替代关系而是互补关系。B 更"旧"（2023 年课程原版）但业务闭环与部署文档更完整；A 更"新"（自研增强版）但只覆盖工作流+页面搭建，无用户体系。

---

## 5. 部署链路

### A
- `docker-compose.yml`：mysql:8.0（healthcheck、卷持久化）+ redis:7-alpine + server（构建自 `apps/server/Dockerfile`，node:18-alpine 多阶段：deps→build→runtime，暴露 3000）。studio 无独立镜像（本地 vite dev）。
- `apps/server/Dockerfile.sandbox`：容器沙箱专用镜像——基于 redis:7 底包解包 node.tar.gz、精简文档，作为 WF_SANDBOX_IMAGE 的国内替代（默认 node:20-alpine）。
- 沙箱配置全 env 化（WF_SANDBOX_MODE=vm|container、内存/CPU/PID 限额、docker socket 路径，Windows 走命名管道）。
- 无 nginx；CORS 由服务端直接控制。

### B（四镜像 + 双 Nginx 网关）
- `server.Dockerfile` / `release.Dockerfile`：node:18-alpine 单阶段，pnpm 全局装 → pnpm install → build:share → build:server/release → `pnpm start:server/start:release`（注意是运行时 pnpm start，非多阶段精简镜像；用了 npmmirror）。
- `server.nginx.Dockerfile` / `release.nginx.Dockerfile`：nginx:1.25.0-alpine 内嵌 conf。
- `docker-compose.yml`：backend(5001→3000)、backend_nginx(5000→80)、frontend(4001→3000)、frontend_nginx(4000→80)；nginx 用 `extra_hosts: host.docker.internal:host-gateway` 反代宿主机端口，支持 WebSocket Upgrade 头。
- 端口链：API 网关 5000→5001→NestJS 3000；发布页网关 4000→4001→Next 3000。镜像 tag 由 `${backend_tag}` 等变量注入，配合云效 CI/CD。

---

## 6. 课程博客常见技术说法核实结论

| 博客常见说法 | 核实结论 | 依据 |
|---|---|---|
| 技术栈 React18 + NestJS10 + Next.js14 + TypeORM + MySQL + Redis + 阿里云 OSS | **属实**（B） | B 各 package.json 与 config.ts/ali-oss 依赖完全对得上；但注意这是 B 工程的说法，A 无 Next/antd/Redis |
| 拖拽用 dnd-kit、状态管理 MobX、UI 库 AntD5 | **属实** | client 依赖 @dnd-kit/core/sortable/utilities、mobx 6.12、antd ^5.11.2 |
| C 端发布页是 Next.js SSR | **属实** | release 包 Next 14.0.4 App Router，`app/[id]/page.tsx` 服务端 fetch + ComponentRender client 补交互 |
| 15 种低代码组件、编辑器与 C 端共用组件物料 | **属实** | share 包 LowCode* 组件恰 15 个目录，`getComponentByType` 两端共用 |
| 撤销/重做、快捷键、草稿 | **属实** | mobx-shallow-undo、useComponentKeyPress、草稿逻辑在 client |
| JWT 鉴权 + 全局守卫 + @Public 白名单 | **属实** | JwtAuthGuard 以 APP_GUARD 全局注册，passport-jwt，validate 二次查库 |
| 图形验证码 + 短信验证码 + 60s 防刷（Redis） | **属实** | svg-captcha、sendCode 60s 防重、RedisModule、key=MD5(ip+ua) |
| 微信扫码登录全链路 | **属实** | wechat-login 模块：二维码 ticket、XML 回调解析 open_id、自动建号、check_scan 轮询 |
| 发布走数据库事务 | **属实** | low-code.service.ts QueryRunner startTransaction/rollback，且含"保留问卷数据"的修正注释 |
| 统一响应 {code,data,msg} + 全局过滤器 | **属实** | AbnormalFilter / ResponseIntercept |
| OSS 上传图片/视频、资源复用 | **属实** | resources 模块 + ali-oss；CDN 域名 OSS_DOMAIN env |
| ECharts 图表 + Excel 导出 | **属实** | echarts/echarts-for-react、exceljs + jszip（压缩包下载） |
| "低代码引擎/Schema 驱动渲染" | **部分属实，说法要分工程**：B 是"组件 JSON options 驱动 React 组件渲染"（关系表存储，非 DSL 引擎）；A 才有真正意义上的 PageSchema DSL + 服务端渲染引擎。博客若笼统说"Schema→UI"对 B 成立，若说"渲染引擎"需限定 | A page-schema.ts/render-page.ts；B share/getComponentByType |
| 工作流/DAG/沙箱/AI 节点 | **仅 A 属实**，课程原版 B 无此内容；博客讲"ComfyUI 式编排/容器隔离/LLM 节点"时素材只能对应 lowcode-platform（A），不能说成课程配套代码的原始功能 | A workflow 模块全套 |
| 多租户/RBAC | **有出入**：两工程都没有真正的 RBAC 角色权限模型。B 只有 account_id 数据归属；A 只有 tenantId 头部注入（预留）。博客如写"RBAC 权限体系"属夸大 | A tenant.guard.ts 注释、B 无 role 字段 |
| Docker + Nginx + CI/CD 部署 | **属实**（B）：四镜像 compose + 双 nginx 网关；CI/CD 文件本体不在工程内（README 提"云效流水线"），博客只宜说"配套云效 CI/CD"而非展示 pipeline 代码 | B docker-compose/nginx/Dockerfile |
| "生产级" | **有出入（需加限定）**：B 架构完整但 Dockerfile 单阶段、`pnpm start` 常驻包管理器，非精简生产镜像；A 明确自述沙箱 vm 层"不是安全边界"。可表述为"生产化参考实现/教学级生产化" | B server.Dockerfile；A sandbox.ts 注释 |

---

## 7. 供博客核对的要点速记

1. 写课程（B）相关博客：技术细节以 docs/API.md 20 个接口 + 5 张表为准；鉴权、验证码、微信扫码、事务发布、SSR、问卷统计全部有代码支撑，可放心展开。
2. 写工作流/沙箱/AI 博客：以工程 A 为准，注意它是自研参考实现不是课程原始代码；其中"vm 软隔离非安全边界、容器硬隔离必配"是代码注释原文，可直接引用。
3. 版本号统一写法：NestJS 10、TypeORM 0.3.x、React 18、Vite 5、Next.js 14、Ant Design 5、MobX 6、dnd-kit 6/8、React Flow 11、ECharts 5。
4. 避免的说法：A/B 均无 RBAC 角色模型；A 的 Redis 未实际使用；B 的 CI 流水线代码不在仓库内。
