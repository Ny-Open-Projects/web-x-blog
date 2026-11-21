# 扫描4：顶层工程文档 + 资源提炼（课程25 小滴课堂低代码大课）

> 源目录：`work/source/25.xiaodi-lowcode/小滴课堂低代码大课`（只读）
> 扫描范围：工程实践-00~07（8 篇）、图谱总览.md、资料关联索引.md、低代码平台工程实践手册.md、低代码博客审核与落地建议.md、第3项方案与实施记录.md、工程实践门户.html、blog_jobs/、blog_progress.json、blog_brief.md
> 扫描日期：2026-11-17

---

## 一、工程实践手册 8 篇逐篇要点提炼

### 工程实践-00 · 总览与定位（5.4KB）

- **资产盘点**：229 篇视频转写博客（约 55.2 万字，9 期：预先课 40 + 第一至八期 189）、知识图谱 `graph.json`（229 节点）、17146 个关联物料（代码 13724 / 图片 1102 / 数据配置 1323 等，100% 挂接）。`graph.json` 终检未改动（sha256 锚定），229 篇通过六点校验。
- **定位边界（最重要的一节）**：这是"研发侧自研低代码平台实战资产"——适合做自研平台技术底座、团队 onboarding 教材、踩坑复盘库；**不适合**做对外选型/售前材料（缺横向对比、ROI），也不面向公民开发者（缺零代码范式）。
- **低代码 vs 零代码四维边界**：是否需研发介入 / 灵活度 / 适用人群 / 典型产物（自研平台 vs 表单工厂类）。
- 8 篇文档的分工地图：00 定边界 → 01/02 补能力（原理）→ 03 立规矩（治理）→ 04 结构化（生命周期）→ 05/06 落地（蓝图+工作流）→ 07 交接。

### 工程实践-01 · 原理综述（上）：Schema/DSL 驱动渲染（6.0KB）

- **核心命题：低代码 ≠ 少写代码，而是"配置即 UI"**。页面不是写出来的，是用 Schema 描述、交给通用渲染器解释执行的。
- **活样本 = 课程 20-6 发布页渲染**。Schema 驱动四要素：
  1. Schema 数据：`{id, type, options}` 组件数组；
  2. 渲染器：`ComponentRender` + `getComponentByType(type)`，`<Comp {...props}/>` 摊开属性；
  3. 组件注册表：share 包里的 type→组件映射，新增组件即登记；
  4. 数据回写：`onChange→onUpdate→useImmer` 保持视图与 Schema 同步。
- **编辑器编辑的是数据不是画面**（18-4）：拖拽 = `arrayMove(oldIndex,newIndex)` 数组索引交换；画布是数组投影；发布 = 数组写库；渲染 = 再投影。编辑端与发布页共享同一份数据契约，一端可写一端只读（20-2 复用同一服务层）。
- **Schema 与 DSL 的关系**：课程用 JSON Schema 直驱（未另起 DSL）。当配置超出"表单填属性"承载力（条件显隐、跨页联动、循环分支表达式）时才需要 DSL/逻辑编排层。业界对照：LowCodeEngine 协议式、Amis JSON 直驱、Retool 数据绑定 DSL。
- **落地铁律 4 条**：先固化 Schema 协议（type 枚举 + props 规范 + 版本号）；两端共享契约；UI 是数据投影；预留逻辑表达式字段。

### 工程实践-02 · 原理综述（下）：引擎、权限与边界（6.3KB）

- **表单/页面引擎雏形已在**：组件注册表 + 属性面板 Schema（14-x 每个组件"展示视图+配置属性"成对开发）+ 数据回写 + 拖拽编排 = 最小可行表单引擎；商用化只需抽象组件市场 + 引擎配置协议。
- **流程引擎课程未做**：只有草稿/预览/发布三态、提交状态等雏形；建议引入 BPMN/状态机并与表单引擎解耦（表单产数据、流程定流转）。
- **RBAC 多端落地**：三端模型（6-2）——编辑端需登录（token 解析 user）、发布页免登录（凭 pageId）、统计端登录+数据权限。已有零件：11-1 用户信息装饰器、14-2 发布鉴权、20-2 访客 `user?.id` 兜底。商用化公式：角色(管理员/编辑/访客) × 资源(页面/组件/问卷数据) × 操作(读/写/发布)；NestJS Guard 统一鉴权；数据权限与菜单权限分层；前端路由级 + 接口级双拦截。
- **自研 vs 采购决策树**：业务高度差异化/需深度集成/长期演进 → 自研；否则采购（要 JSON 配置出页面 → LowCodeEngine/Amis；数据后台+流程 → aPaaS；标准后台 → Admin 框架）。ROI 提示：自研真正价值是"业务差异化能力沉淀为可复用资产"。
- **方法论缺口清单**：课程缺的 5 项已在综述补齐；组件市场/协议版本化、DSL 逻辑编排、监控告警/灰度发布仅停留在"建议"层。

### 工程实践-03 · 内容治理规范（6.1KB）

- **内容门禁 6 条硬约束**：①转写纠错括号残留（"口播误读为X"）→删；②口播语气词（"视频里/听起来"）→书面化；③广告后缀 `【网盘分享wpfx.org.cn】`→全局删；④HTML 实体（`&ldquo;` 等）→还原；⑤编造互链（引用 titles.txt 白名单 229 条之外的标题）→禁止；⑥六段结构（导语/前置/正文/小结/下一步）缺失→补全。终检脚本 `tools/verify_xiaodi_6point.py` 六点校验全绿方可交付。
- **术语表**：中文核心词（低代码/零代码/Schema/DSL/RBAC/拖拽/组件库）全文一致；英文专名大小写严格对齐代码（React、Next.js、NestJS、TypeORM、Ant Design、Tailwind CSS、dnd-kit、pnpm 等），代码块内按库本身写法。
- **技术准确性双人复核**：接口名/类名/版本号/配置项以关联代码 materials 为准，禁止凭口播记忆；"关联物料注入机制必须延续"。
- **密钥安全红线**：课程 17-1/27-7 的 OSS AccessKey 是教学占位符；生产必须环境变量/KMS 注入、最小权限（仅授予所需 Bucket Put/Get/Delete）、安全评审、定期轮换、附上线前 6 项自查清单（grep 无明文密钥、公网接口鉴权、白名单/VPC 隔离等）。

### 工程实践-04 · 生命周期导航（31.9KB）

- 把 229 篇按"落地生命周期"重排（而非按集数平铺），主线：
  `需求分析 → 系统架构 → 后端接口(NestJS) → 前端框架(React) → 编辑器(拖拽配置) → 发布页渲染(Schema) → 资源(OSS) → 数据统计 → 部署DevOps → 压测运维`
- 各阶段篇数：后端服务 50 / 需求分析与架构 39 / 编辑器 35 / 部署 DevOps 26 / 前端框架 23 / 性能压测 15 / 数据统计后台 14 / 发布页与 Schema 渲染 14 / OSS 9 / 职业面试 4。
- 全表给出每篇的标题、原期目录、关联物料数、图片数、正文字数，是"按需查实现"的检索目录。

### 工程实践-05 · 参考实现蓝图（11.5KB，状态"待审阅"）

- 定位：把博客里的平台变成**可 clone、可 `docker compose up` 的最小参考实现**的技术方案（不是代码）。边界：打通"定义页面→拖拽配置→发布→Schema 渲染→提交数据→后台统计"主线闭环；不含工作流引擎/多租户/插件市场/AI。
- **架构核心 = "Schema 即产物"**：创作端只产 JSON；渲染端读同一份 Schema 按 type 映射组件；服务端存 Schema、鉴权、存提交数据、对接 OSS。
- pnpm Monorepo 结构：`packages/shared`（Schema 类型/组件注册表）+ `apps/server`（NestJS，auth/page/component/form/oss/stats/rbac 7 模块）+ `apps/editor`（React 18+dnd-kit+MobX）+ `apps/render`（Next.js 14）+ `apps/admin` + docker-compose。
- 技术栈基线：Node 18、NestJS 10 + TypeORM 0.3、MySQL 8、Redis 7、React 18 + Vite + AntD 5、Next.js 14、OSS、云效、JMeter 5。
- 核心数据模型：`ComponentNode = {id, type, options}`，页面 = 数组；MVP 6 张表（user / role+user_role / page / page_component / form_submission / oss_file）；关键 API 面 6 域（账户/微信/页面/组件/表单/OSS/统计），全部标注课程篇目出处。
- 实施分期 P0–P4 约 19–26 人日；MVP 外预留：流程引擎、多租户、组件市场、AI 生成、源码导出。
- 上线前商用化缺口：真实基础设施、密钥管理、限流防刷审计监控、**Schema 版本兼容**（type 一旦发布改名即破坏已发布页面，需版本化注册表）。

### 工程实践-06 · 工作流模块设计（11.1KB，平台内模块）

- **定位硬约束**：workflow 是 `apps/server/src/modules/` 下与 auth/page 平级的**平台内模块**（不单建仓库/服务/DB/CI），画布是 studio 内与 page-builder 并列的 Tab。历史教训：初版被批评"主次不分"画成独立系统，已修正。
- **节点词汇表**：节点 = 平台既有 module service 的可编排封装（trigger.webhook/schedule/formSubmit、source.formSubmission/mysqlQuery/apiGet/ossRead、transform.map/filter/aggregate/script、logic.branch/merge/loop/delay、**ui.emitComponent/ui.composePage 复用 PageSchema**、action.sendSms/callApi/writeDb/webhook、ai.generatePage）。统一 `NodeContract {type, ports, execute}`，前后端共用注册表。
- **Graph DSL**：与 ComfyUI prompt 同构的 JSON（nodes[].params + edges 带端口），入库存 `wf_graph`，版本单调递增。
- **DAG 执行引擎**（纯 TS 可单测）：解析→校验（端口类型/必填参数/注册表命中）→Kahn 拓扑排序检环→逐节点执行（无依赖兄弟并行）→ctx 携带 tenantId/runId/配额/审计→每次执行落 wf_run/wf_run_node 支持重放→单节点失败按配置决定回滚/跳过/告警。
- **沙箱方案**：脚本/LLM 节点是商用安全硬门槛——默认关闭、容器/WASM 隔离、资源配额、输入白名单（不触密钥）、全量审计；轻量可商用版不含脚本节点。
- **商业化就绪 11 项设计**：MIT/Apache 协议（禁 GPL 传染）、全表预留 tenant_id、PIPL 合规脱敏、密钥不进前端/图 JSON/沙箱、可观测、计量钩子、配置外置、契约版本化、品牌去课程化、节点 SDK 开放注册。
- 排期 M0–M4 约 20–22 人日（轻量版 M0–M3 ≈16 人日）。

### 工程实践-07 · 工程交接文档（18.1KB，面向新 Agent/新人）

- **状态**：参考实现 `lowcode-platform/` 已实际建成——**P0 + M0–M9 全部交付**（3 构建 + 7 测试套件全绿，2026-11-15）。技术栈实际落地为 NestJS 10 + TypeORM + MySQL 8、React 18 + Vite + React Flow、**npm workspaces**（非 pnpm）。唯一待办：SMS/OSS Provider 接真实云厂商（缺密钥）。
- **协作铁律**：讨论 ≠ 授权开工（历史教训：误把需求输入当授权写代码）；指令极简风格；交付须带可复现验证证据。
- **核心设计约定**：契约唯一真源在 `packages/shared`（PageSchema/WorkflowContract/tenant），任何端不得私自加字段，破坏性变更走 schema.version；工作流是平台内模块不是独立系统；端口三类 data/schema/trigger 前端校验；副作用全走 Provider（Sms/Oss/Form 可替换，接云厂商=换 Provider 实现+填 env，节点零改动）；密钥纪律（只从 env 读，不进前端/图 JSON/沙箱）。
- **已交付能力**：DAG 引擎（拓扑+环检测+节点级追踪）、React Flow 画布+结构化参数编辑器、预置节点端到端、vm 软隔离（M4）、租户守卫跨租户 403（M6）、可视化 Page Builder（M7）、**容器硬隔离**（M8：一次性容器+禁网+只读根+非root+资源限额+容器内再套 JS 沙箱+自动回退 vm）、**嵌套组件树形建页**（M9，PageSchema 契约不变存量零迁移）。
- **未做边界（勿夸大）**：完整 RBAC/SSO（只有 x-tenant-id 头级过滤）、真实云厂商 Provider、计量计费/MQ/限流、前端登录态、组件市场、DB 迁移脚本（现 synchronize:true）、Jest 框架化测试。
- **Windows/exFAT 环境坑位 12 条**：exFAT 不支持原地覆盖（tmpnew+remove+replace 三步写法）、node_modules 别放外接盘、pnpm 缺二进制卡死、NTFS 存不住 exec 位（node 二进制必须在 Dockerfile 内解压）、Git Bash 管道改写二进制、MSYS_NO_PATHCONV、ValidationPipe whitelist 会剥掉无装饰器字段、--experimental-strip-types 不解析无扩展名导入、.cjs 顶层 await 等——对后续在本机跑这套工程极有价值。
- 接手优先级：①接真实云厂商 ②RBAC 第二层 ③TypeORM migration ④前端租户头/登录态 ⑤组件资产市场。

### 配套：低代码平台工程实践手册（8.5KB，Playbook）

- 技术栈总表（从各期 package.json 提炼）：pnpm Monorepo / React18+Vite+TS / Next.js / AntD5+Tailwind3 / MobX / dnd-kit / NestJS / TypeORM+MySQL / Redis / 阿里云 OSS / Nginx / Docker+Compose / 云效 / JMeter 5。
- 架构决策（6-2）：访问层（编辑端+发布页 H5）→ Nginx 网关 → NestJS → MySQL+Redis+OSS → ECS/CDN；编辑端与发布页共享同一服务层仅鉴权不同。
- 8 个关键代码模式（带课程锚点）：Monorepo 分包、NestJS 装饰器（@User/验证码装饰器/拦截器）、TypeORM 实体关系与事务、Schema 驱动渲染、dnd-kit+MobX 拖拽（transform Y 轴清空避坑）、OSS 动态模块+multer（AliOssModule @Global 注入、latin1→utf8 文件名）、容器化 DevOps（4 个 Dockerfile）、JMeter 压测闭环。
- Do/Don't 与上线 Checklist、**商用化补齐清单 7 项**：版本化 Schema 协议+组件市场、DSL 逻辑编排、BPMN 流程引擎、统一 RBAC、可插拔组件市场、监控告警/灰度/回滚、多租户。

### 配套：低代码博客审核与落地建议（6.8KB）

- 修复清单：13 处转写痕迹、2 处 engines 残留、1 处纠错尾巴、3 处口播语气词，全部已清。终检：229/229 落盘、六段结构 0 不全、广告/实体/编造互链/转写痕迹均 0，单篇 964–4740 字（均值 2412）。
- **术语覆盖度分析（关键洞察）**："表单"113 次、"流程"122 次、"拖拽"74 次、"权限"46 次，但"低代码引擎"仅 1 次、"Schema 驱动"0 次、"表单引擎/流程引擎"0 次、"DSL"2 次 → **实现层极扎实、方法论层缺失**：读者能照敲出一套系统，却理解不了"为什么拖一下就能生成页面"。
- 场景适配评分：踩坑复盘库 ★★★★★、onboarding ★★★★☆、自研参考 ★★★★☆、选型决策 ★☆☆☆☆、售前 ★☆☆☆☆、公民开发者 ☆☆☆☆☆。
- 落地建议工作流："收场景→定边界→选平台→立规矩"，即 00–04 篇的由来。

### 配套：第3项方案与实施记录.md（5.7KB）

- 资料关联工程实施记录（已完成验收）：17146 文件 100% 挂接，9 类资料、104 种扩展名、0 篇零关联（中位数 75 条/课）。
- **关键破译：三方同构锚点**——视频 `x-y` 编号 ≡ 总纲"第 x 章第 y 集" ≡ 代码包 `<x-y>/` 目录；代码包是**累积快照**（8-2 起步 3 文件 → 30-6 完整工程），由此推出预先课章节 → 代码演进链目录映射。
- 三个精细处理：孤儿图片 213/213 三级归位（md5 → dHash 感知哈希 → mtime 最近邻）；公共资料按双向主题规则挂载（资料侧强特征 + 文章侧标题/子目录强特征双命中）；工具包 vs 教学资料区分（jmeter 软件本体 2620 文件整包挂 toolkit 维度）。
- 排除规则：node_modules（5.1 万项）不入图、dist/.git/.next 等构建产物排除，其余全入图（含 .mwb/.drawio/.sql/.jmx/.dmg）。
- 复现脚本清单：scan_xiaodi_videos / map_orphan_images / build_xiaodi_graph / export_xiaodi_index_md / zh_en_map。

### 工程实践门户.html（247KB）

- 自包含单文件门户（标题"低代码平台工程实践门户"），读 `graph.json` 数据，支持对 229 篇按关键词检索直达（如 dnd-kit、TypeORM、OSS、Dockerfile）。

---

## 二、图谱总览 + 资料关联索引：知识图谱骨架

**规模**：229 节点（博客篇目）× 17146 资料文件，总纲 31 章/190 集，代码包课号目录 116 个，100% 覆盖（中位数 75 关联/篇）。

**骨架（三层结构）**：

1. **节点层**：每篇博客一个节点，属性含 stage（期目录）/ subdir / title / num / transcript / materials / containers。
2. **关联层（锚点体系，零歧义硬锚点为核心）**：
   - `lesson_no`（115 篇）：视频 x-y ↔ 代码包 x-y 目录，最强锚点；
   - `pre_chapter`（40 篇）：预先课章节 → 代码演进链课号目录（因为代码包是累积快照，预先课没有自己的 x-y）；
   - `code_feature`（7 篇）：中文标题 → 英文源码文件名技术词映射；
   - `orphan_code`（1）：13-4 有代码无视频 → 挂 13-3；
   - `toolkit`（41 篇）：jmeter/Navicat/jdk8 整包；
   - `public`：总纲/需求文档/流程图/简历模板按主题语义挂载。
3. **语义层（工程实践 04 补上）**：229 节点按"低代码平台落地生命周期"重编为 10 阶段——这正是这门课知识图谱的概念主干。

**核心概念关系图（文字版）**：

```
需求分析(4-x/5-x) ──产出──▶ 需求文档+原型 ──决定──▶ 系统架构(6-2 三端分层)
     │                                              │
     ▼                                              ▼
 后端 NestJS(8-4~13-x: 模块/装饰器/TypeORM/Redis/验证码/OSS)
     │ 提供 page/component 接口(14-x, 20-2)          │
     ▼                                              ▼
 编辑器 React(14-6 画布+左栏+属性面板; 18-4 dnd-kit)
     │ 编辑的只是 Schema 数组 {id,type,options}
     ▼
 发布(14-2/14-3: 草稿→发布, Schema 写库)
     │
     ▼
 发布页 Next.js(20-5/20-6: getComponentByType 摊开 props 渲染) ──免登录凭 pageId──▶ 访客提交问卷(20-7)
     │
     ▼
 数据统计后台(21-x: ECharts 动态图表 + Excel 导出)
     │
     ▼
 部署 DevOps(23-x Dockerfile ×4 → 24-x Compose → 25/26-x 云效流水线 → 27-x 上线确认)
     │
     ▼
 压测 JMeter(28-30-x: 线程组/聚合报告/断言 → 30-6 据压测优化获取组件接口)
     +
 职业收尾(31-x 简历/面试)
```

横向贯穿：权限（编辑端登录 vs 发布页免登录）、密钥安全（OSS 占位符）、物料挂接（每篇博客的 materials 字段，技术细节以代码为准）。

**资料关联索引.md**（942KB）是 graph.json 的人读版：分期分课表格 + 每课折叠课件正文 + 全部关联资料清单，可直接作为"博客引用素材"的查找入口。

---

## 三、blog_jobs / blog_progress：处理流水线状态

### blog_progress.json（权威状态）

- **total 229，done 229，failed []，missing []，status = COMPLETED**（2026-11-12 22:25:01）。
- 生成方式：Hy3 自身并行子 agent 分批生成，无外部模型调用。
- 质量指标：六段结构 ✓、广告后缀 0、HTML 实体 0、编造互链 0、重复副本 0。

### blog_jobs/（229 个任务包）

- 每个任务包 `job_NNN.json` 结构：`{idx, rel, title, stage, materials{code[], notes[]}, transcript_path, out_path}`——含 ASR 转写稿路径、输出路径、关联代码物料（带 snippet 片段，如 package.json/pnpm-lock 等）。
- 另有 `remaining_group_1~3.json`（各 16 项 = 48 项）与 `titles.txt`（229 条标题白名单）。remaining_group 从 idx 覆盖看是分批重跑/补处理用的中间产物；由于 progress 已 COMPLETED 且 blog/ 目录 9 期齐全，它们属于历史批次拆分，**不构成未完成项**。

### 已完成 / 未完成

**已完成**：①229 篇转录稿→博客全量转换（六段结构、质量门禁全过）；②17146 物料 100% 挂接（第3项）；③审核修复 + 终检全绿；④工程实践 00–07 + 手册 + 门户 + 参考实现 lowcode-platform（P0+M0–M9 全交付、7 测试套件全绿）。

**未完成 / 遗留**（按文档自述）：
1. 参考实现唯一明确待办：**SMS/OSS Provider 接真实云厂商**（缺用户 API 密钥）；
2. 参考实现未做：完整 RBAC/SSO、计量计费、MQ/限流、前端登录态、组件市场、DB migration；
3. 工程蓝图 05 仍标"待审阅"（是否按 P0–P4 正式写完整版参考实现的授权决策点）；
4. 方法论层仅综述级：组件市场/协议版本化、DSL 逻辑编排、监控告警/灰度发布三处均停在"建议"；
5. 面向博客成稿侧：工程实践文档已就绪，但**尚无面向读者的博客化改写**（这正是本工作空间 blog 目录之外可做的增量）。

---

## 四、值得进博客成稿的高价值内容清单（去重后）

按主题合并自多份文档（出处标注一次），按可读性/独立性排序：

### A. 原理洞察类（最稀缺，课程正文里没有）

1. **"为什么拖一下就能生成页面"——Schema 驱动渲染四要素**（工程实践-01）：Schema 数据 / 渲染器 / 组件注册表 / 数据回写，用课程 20-6 真实代码做活样本。★最高价值，全课程唯一讲透本质的内容。
2. **"编辑器编辑的是数据不是画面"**（01 + 18-4）：拖拽 = arrayMove 索引交换，画布只是数组投影；编辑端可写、发布端只读共享同一契约。
3. **Schema vs DSL：什么时候 JSON 不够用**（01）：条件显隐/跨页联动/表达式需要 DSL 或逻辑编排层；业界三方对照（LowCodeEngine 协议式 / Amis JSON 直驱 / Retool DSL）。
4. **低代码 vs 零代码 vs 自研 vs 采购的边界决策**（00/02）：四维对比表 + 自研决策树 + "自研真正价值是差异化能力沉淀为资产"的 ROI 论断。
5. **表单引擎/流程引擎职责切分**（02）：课程有表单引擎雏形、无流程引擎；二者应通过事件/接口解耦。
6. **RBAC 三端落地公式**（02）：角色×资源×操作；NestJS Guard 统一鉴权；数据权限与菜单权限分层；前端藏按钮接口不能裸奔。

### B. 实战踩坑类（课程强项，可做系列）

7. dnd-kit 拖拽排序完整实现与三个坑（18-4）：transform Y 轴清空、isDraggable、over 为 null；碰撞检测 closestCenter。
8. NestJS 用户信息装饰器模式（11-1）：token→user 全局复用，替代散写的 if(!user)。
9. 阿里云 OSS 动态模块（17-1）：@Global + ALI_OSS 注入、multer、latin1→utf8 文件名、CNAME 替换；密钥占位符纪律。
10. Schema 渲染发布页（20-2/20-6）：getComponentByType + 摊开 props + useImmer 回写；发布页免登录设计。
11. Docker 化 + 云效流水线全链路（23~27-x）：4 个 Dockerfile、Compose 编排、流水线、Bucket 绑域名、上线功能确认。
12. JMeter 压测闭环（28~30-x）：线程组/聚合报告/断言，30-6 据压测结果优化获取组件接口性能（压测驱动的性能优化案例）。

### C. 架构与工程化类

13. Monorepo 三包结构与"页面专属 vs 公共复用"组件划分原则（8-x/14-6）。
14. 参考实现蓝图的工程结构（05）：shared 契约包 + 7 后端模块 + 3 前端 app + docker-compose 一键起；MVP 表设计与 API 面。
15. 工作流模块设计（06）：节点 = 平台能力的可编排封装、Graph DSL、DAG 引擎（Kahn 检环/并行/追踪重放）、ui.composePage 连线生成可运行页面。
16. 沙箱分级路线（06/07）：vm 软隔离 → 容器硬隔离（一次性容器+禁网+只读根+非root+资源限额）+ 自动回退——自研平台执行用户代码的安全方案。
17. 商用化补齐清单 7 项（手册六）：从"能跑"到"可商用"的差距表，本身就是一篇好文章的骨架。
18. 密钥安全红线与上线自查清单（03）：占位符教育、环境变量/KMS、最小权限、轮换。

### D. 内容工程/知识管理类（面向本工作空间读者）

19. 三方同构锚点 + 累积快照破译（第3项记录）：如何给 229 篇视频课建零歧义的资料关联，孤儿图片 md5/dHash/mtime 三级归位——数据工程方法论。
20. 六点终检门禁 + 术语表 + 双人复核（03）：视频转写内容的质量治理流水线，可复用于本工作空间其他课程。

**去重说明**：00/审核建议/手册三份文档重复论述"低代码 vs 零代码、定位边界、方法论缺口"，已合并为 A4/A5；02 与手册重复的 RBAC 内容并入 A6；05/07 重复的工程结构并入 C14；06 与 07 重复的沙箱内容并入 C16。

**建议成稿优先级**：A1、A2（原理层，全网稀缺）→ B 系列选 3–4 篇（实战搜索流量）→ A4/C17（决策层，面向管理者）→ D19/20（面向内容工程读者）。
