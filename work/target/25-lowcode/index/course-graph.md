# 课程25 总图谱：小滴课堂低代码大课（扫描9）

> 数据源：scan1-structure / scan1-tree（结构）、scan2-knowledge（知识点总账）、scan3-code（代码实况）、scan4-docs（图谱骨架）、scan4-lowcode-domain（领域体系）、scan7-materials（物料增量）。229 篇博客 + 35 张知识卡 + 17146 条物料。
> 本文件是课程25 的"一张图"：结构、概念关系、卡↔篇映射、缺口与红线。进站导航版见同目录 `index.md`。

## 1. 课程结构：9 阶段 / 18 章 / 229 篇

| 阶段（博客目录） | 篇数 | 课时号 | 内容主线 |
|---|---|---|---|
| 00.预先课 | 40 | 章 1–6 | NestJS/TypeORM/React 预备：用"课程管理"小项目把三件套各过一遍（10 个章组） |
| 01.第一期【1.1–5.3】 | 24 | 1-1~5-3 | 导学 + 技术选型（Vue/React、Express/Koa/Nest、Next/Nuxt）+ Next.js 基础 + 需求分析 + 需求文档 |
| 02.第二期【6.1–10.8】 | 26 | 6-1~10-8 | 系统架构 + 数据库设计（ER 图）+ 云服务器/Docker 装 MySQL/Redis + pnpm Monorepo 初始化 + TypeORM 全套 |
| 03.第三期【11.1–13.10】 | 23 | 11-1~13-10 | 账户体系：验证码/短信/注册登录 + 微信扫码登录 + 前端登录模块联调（**13-4 缺集**） |
| 04.第四期【14.1–16.7】 | 24 | 14-1~16-7 | 编辑器：发布接口（事务）+ 画布布局 + 组件成对开发（展示视图+属性配置） |
| 05.第五期【17.1–20.8】 | 26 | 17-1~20-8 | OSS 资源体系 + 拖拽排序/工具栏/撤销重做 + 草稿预览发布 + Next.js 发布页渲染与问卷提交 |
| 06.第六期【21.1–24.4】 | 25 | 21-1~24-4 | 数据统计后台（Excel 导出/动态图表）+ Dockerfile×4 + Compose + DevOps/云效 |
| 07.第七期【25.1–28.3】 | 22 | 25-1~28-3 | 云效流水线全链路 + 上线确认/BUG 修复 + JMeter 入门 |
| 08.第八期【28.4–31.4】 | 19 | 28-4~31-4 | JMeter 压测实战（含 30-6 压测驱动优化）+ 简历/面试收尾 |

预先课 40 篇按章容器（pre_chapter）挂链代码演进链；主课 189 篇按 lesson_no（x-y ↔ 代码包目录）硬锚点挂链，115 篇有 code_dir，17146 物料 100% 关联。

## 2. 核心概念关系（Schema / 物料 / 渲染 / 发布 / 工作流）

```
需求分析(1-1~5-3) ──▶ 系统架构三端分层(6-2) ──▶ Monorepo 三包(8-x, share=契约包)
                                                        │
   Schema 数据契约 {id,type,options}（concept-02/05）     ▼
        │                                    后端 NestJS(9-x~13-x: JWT/验证码/微信)
        ▼                                              │ 提供 page/component 接口
   物料·组件注册表 type→组件（concept-03）              ▼
        │                                    编辑器 React(14-x~19-x)
        ▼                                    拖拽=arrayMove 索引交换(principle-02)
   渲染引擎 getComponentByType 摊开 props（concept-04/principle-01）
        │
        ▼
   发布链路 草稿→预览→发布（concept-08/principle-03 事务三段式）
        │ Schema 写库
        ▼
   发布页 Next.js(20-x) 免登录凭 pageId ──▶ 访客问卷提交 ──▶ 统计后台(21~22-x: ECharts/Excel)
        │
        ▼
   部署 DevOps(23~27-x: 4 Dockerfile→Compose→云效流水线→双 Nginx 网关) ──▶ JMeter 压测(28~30-x) ──▶ 面试收尾(31-x)

【横向贯穿】权限（编辑端登录 vs 发布页免登录，concept-07/principle-05）｜密钥安全（OSS 占位符纪律）｜工作流/沙箱（参考实现扩展，concept-09/10）
```

一句话主干：**编辑器编辑的是数据不是画面**——一切围绕 Schema 数组的写（编辑端）、存（事务发布）、读（渲染引擎）展开；工作流与沙箱是课程之外的参考实现增量，引用时必须注明来源（见 §5 红线）。

## 3. 35 张知识卡 ↔ 229 篇映射

完整出处表见 `cards/README.md`，此处按阶段给落点（卡 → 代表性博客篇，互链方案见 reports/scan9-index.md）：

| 阶段 | 对应卡片 | 代表篇（anchor） |
|---|---|---|
| 00 预先课 | practice-01-nestjs-core | 第_2_集__详解Nestjs控制器《上》、第_3_集__TypeORM配置实体和操作数据库 |
| 01 导学/选型/需求 | interview-01-tech-choice、interview-04-lowcode-highlights | 1-2.低代码平台项目亮点+疑惑、2-9.技术栈选择、5-2/5-3.需求文档 |
| 02 架构/数据库/Monorepo | concept-02、concept-05、practice-02-typeorm-pitfalls | 6-2.规划系统架构、6-4.数据库设计、8-5.share 包、10-8.TypeORM 事务 |
| 03 账户/微信登录 | practice-03-captcha-antifraud、practice-04-wechat-scan、principle-05-jwt-chain、interview-02-security | 11-1.用户信息装饰器、11-6.手机验证码、12-2.扫码时序图、11-8.登录接口 |
| 04 编辑器/组件 | concept-01、concept-03、practice-12-component-recipe、principle-03-transaction-release | 14-2~14-4.发布接口、14-8/14-9.视频组件成对开发、15-4.轮播图属性配置 |
| 05 OSS/拖拽/发布渲染 | practice-05-oss-resource、principle-02-drag-index-swap、principle-06-undo-redo、practice-10-editor-interactions、concept-04、principle-01-schema-to-ui、concept-08 | 17-1.OSS 配置、18-4.拖拽排序、18-5.键盘操作、19-4.发布功能、20-6.获取页面渲染 |
| 06 统计/部署 | practice-06-excel-export、practice-11-stat-frontend、practice-07-docker-deploy | 21-9.Excel 导出、22-4.动态饼图、23-3.后端镜像、24-2.Compose |
| 07/08 流水线/压测 | practice-07、practice-08-jmeter、practice-09-redis-cache-pattern、principle-04-cache-qps、interview-03-performance、interview-05-resume-rules、interview-06-pitfall-talk | 25-1.流水线关联代码源、27-2.镜像名称 BUG、28-7.发布页压测、29-1.聚合报告、30-6.压测优化、31-4.低代码简历 |

概念卡中 concept-06（协议）、concept-09（沙箱）、concept-10（工作流）、concept-11（选型边界）无课程原始篇目直接对应：06/11 出自工程实践文档（scan4），09/10 出自参考实现 lowcode-platform（scan3 §2-A），互链指向工程实践/参考实现语境，不编造课程篇目。

## 4. 缺口与注意事项标注

### 4.1 13-4 缺集（唯一内容缺口）
- 13-4 课无视频、无博客（第三期目录从 13-3 直接跳 13-5），其代码快照以 orphan_code 锚点挂在 13-3 名下。成稿若引用 13-4 代码需注明"该集未录制，内容并入 13-3"。除此之外 229↔229 音频转写零缺口，各期课时号覆盖完整（num 断档是编码规则非缺集）。

### 4.2 方法论缺口（课程只做没讲，成稿增量点）
- "Schema 驱动""低代码引擎""表单/流程引擎"在 229 篇正文几乎零提及——实现层极扎实、方法论层缺失；原理卡 6 张 + 概念卡 01/02/04/06 就是补这一层的成稿素材。
- 流程引擎课程未做（只有三态雏形）；组件市场/协议版本化/监控灰度停留在"建议"层。

### 4.3 红线（写博客/互链必守）
1. **Navicat 破解教程物料**（安装包随附步骤.docx/pdf）绝不可引用、复述或链接；替代口径用官方试用版/DBeaver。
2. 工作流/沙箱/AI 节点内容来自**自研参考实现**（lowcode-platform），不是课程原始代码，引用必须说清来源。
3. 两套工程均无真正 RBAC 角色模型，禁止写"RBAC 权限体系"（只有三端差异化鉴权）。
4. 课程原版（B 工程）无工作流模块；参考实现（A）的 Redis 未实际使用。
5. 事务化发布"保留问卷数据"是参考实现修正，原课程实现会重置问卷数据。
6. 课程 17-1/27-7 的 OSS AccessKey 是教学占位符；成稿须按"密钥不进代码、env/KMS 注入"口径表述。
7. 禁止编造互链：引用篇目标题必须在 titles.txt 229 条白名单内；1102 张截图物料含网盘水印，不直接用，配图走 drawio 重导出或自绘。
8. 物料实体（笔记 PDF、drawio、mwb、sql 等）在外部盘，本工作区不可读；引用原文需先补取。

## 5. 阅读动线（对应 index.md 的前置/后续）

1. **预先课**（practice-01/02 打底）→ **第一期**（选型与需求，interview-01/04）→ **第二期**（架构与 TypeORM，concept-02/05）→ **第三期**（账户与微信登录，principle-05）→ **第四期**（编辑器与组件范式，practice-12）→ **第五期**（拖拽/发布/渲染，principle-02、concept-04/08）→ **第六期**（统计与部署，practice-06/07）→ **第七期**（流水线与上线）→ **第八期**（压测与面试，principle-04、interview-02/03/05/06）。
2. 快速通道：只想要"低代码本质"→ concept-01 → concept-04 → principle-01/principle-02 → 20-6 篇；只想要面试 → interview 六卡 + 31-x 四篇。
