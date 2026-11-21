# 扫描9 · 课程总图谱 + 索引 + 互链方案（25 小滴课堂低代码大课）

- 生成：2026-11-17。产出：`index/course-graph.md`（总图谱）、`index/index.md`（进站导航页草案）、本文件（互链方案）。
- 依赖：scan1-structure / scan1-tree（9 阶段 18 章 229 篇）、scan4-docs（概念关系骨架）、scan7-materials（13-4 缺集与红线）、cards/README.md（35 卡出处表）、`blog/source/courses/index.md`（19 门课卡片格式）。

## 1. 卡片 → 博客篇互链怎么落

### 1.1 链接形态与 URL 规律

- 站点为 Hexo，课程25 博客全部落在 `_posts/xiaodi-lowcode/`，渲染后 URL 形如 `/2026/11/17/xiaodi-lowcode/<期目录>/<文件名去.md>/`（229 篇 date 均为 2026-11-17，日期段统一）。预先生成的 public 已验证该模式。
- **推荐做法**：卡片进站时用相对站内路径（`/2026/11/17/xiaodi-lowcode/05.第五期/20-6.低代码项目发布页面—获取页面渲染/`）或 Hexo 的 post 引用；**不要用带当天日期的绝对永久链接做长期外发**——若 permalink 配置日后变更会全量失效。更稳的口径：卡片正文引用"篇目名 + 期目录"，站内跳转交给分类聚合页。
- 分类聚合页（稳定入口）：每篇已挂 `categories: [低代码大课, 低代码第N期]`预先课为 `低代码预备`，第一期起为 `低代码第N期`），卡片可直接链 `/categories/低代码大课/`。

### 1.2 互链策略：每卡 1~3 个代表性篇目，不追求全量

35 卡对 229 篇全量互链（35×N 链接）会稀释导航价值且维护成本高。原则：**每张卡链"最能当活样本"的 1–3 篇**，其余靠期目录聚合页承接。代表篇选择标准：① 代码可读（有 code_dir）；② 是该知识点的首次完整实现；③ 标题自解释。具体映射（卡 → 代表篇）：

| 卡 | 代表篇（期目录/文件） |
|---|---|
| concept-01-meta-driven | 04/14-2（发布接口·上，Schema 写库入口） |
| concept-02-schema-dsl | 02/8-5（share 契约包）、04/14-2 |
| concept-03-material-registry | 04/14-7（左栏组件列表） |
| concept-04-render-engine | 05/20-6（发布页获取页面渲染，全课程最佳活样本） |
| concept-05-data-model | 02/6-4（数据库设计） |
| concept-06-protocol | 无课程篇目（源自工程实践文档），卡内注明，链 `/categories/低代码大课/` |
| concept-07-permission-model | 05/20-3（发布页免登录问卷查询） |
| concept-08-release-pipeline | 05/19-2~19-4（草稿/预览/发布三篇） |
| concept-09-sandbox | 无课程篇目（参考实现），注明来源 |
| concept-10-workflow-dag | 无课程篇目（参考实现），注明来源 |
| concept-11-lowcode-vs-nocode | 01/1-2（项目亮点+疑惑） |
| principle-01-schema-to-ui | 04/14-8、04/14-9（视频组件成对开发） |
| principle-02-drag-index-swap | 05/18-4（拖拽排序） |
| principle-03-transaction-release | 04/14-4（发布接口·下 QueryRunner 事务） |
| principle-04-cache-qps | 08/30-6（压测驱动优化） |
| principle-05-jwt-chain | 03/11-8（登录接口）、04/14-3（发布鉴权） |
| principle-06-undo-redo | 05/18-5（键盘操作） |
| practice-01-nestjs-core | 00 预先课（控制器/模块/拦截器三篇） |
| practice-02-typeorm-pitfalls | 02/10-8（事务） |
| practice-03-captcha-antifraud | 03/11-3、03/11-6（图形/手机验证码） |
| practice-04-wechat-scan | 03/12-2（扫码时序图）、03/12-6（轮询） |
| practice-05-oss-resource | 05/17-1~17-3（上传配置/上传接口/删除配置） |
| practice-06-excel-export | 06/21-9、06/22-1（导出 Excel/压缩包） |
| practice-07-docker-deploy | 06/23-3、06/24-2（后端镜像/Compose） |
| practice-08-jmeter | 08/28-7（发布页压测） |
| practice-09-redis-cache-pattern | 03/11-2（Redis 模块配置） |
| practice-10-editor-interactions | 05/18-6~18-8（工具栏三篇） |
| practice-11-stat-frontend | 06/22-4（动态饼图） |
| practice-12-component-recipe | 04/15-4（轮播图配置属性，五步范式样板） |
| interview-01-tech-choice | 01/2-3、01/2-9（技术选型/技术栈选择） |
| interview-02-security | 03/11-6、04/14-3 |
| interview-03-performance | 08/29-1、08/30-6 |
| interview-04-lowcode-highlights | 01/1-2、08/31-4（低代码简历讲解） |
| interview-05-resume-rules | 08/31-1~31-4 |
| interview-06-pitfall-talk | 02/10-8、07/27-2（镜像名称 BUG） |

反向互链（博客篇 → 卡）：不在 229 篇正文里补链接（正文已终检锁定，改动需走审核流程）；用**期目录聚合页 + 卡片分类**承接——卡片 front-matter 已带 `categories: [课程, 低代码]`、`tags: [25-lowcode, ...]`，站内 tag 页 `/tags/25-lowcode/` 天然聚合 35 卡 + 229 篇，即"反向互链"由标签体系完成，正文零改动。

### 1.3 链接安全约束

- 只链 titles.txt 白名单内的篇目（229 条），禁止编造篇名（工程实践-03 门禁第⑤条，继续执行）。
- concept-06/09/10 与面试卡里涉及参考实现的表述，须按 cards/README.md 红线注明"来自自研参考实现，非课程原始代码"。

## 2. courses/index.md 如何接 25 号课

现有 19 门课卡片格式：单行 `<a href='/categories/XXX/'>` 网格卡，含课程名 + "N 篇 · 目录 xxx"。25 号课对齐方案（**仅建议 diff，最终修改由主 agent 执行**）：

```diff
--- a/work/blog/source/courses/index.md
+++ b/work/blog/source/courses/index.md
@@
-<p style='color:#666'>共 <b>19</b> 门课 / <b>3291</b> 篇笔记。点课程进入，再点单篇看细节。</p>
+<p style='color:#666'>共 <b>20</b> 门课 / <b>3520</b> 篇笔记。点课程进入，再点单篇看细节。</p>
@@
 （网格末尾追加一张卡）
+  <a href='/categories/低代码大课/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>全栈低代码平台大课</div><div style='color:#888;font-size:13px;margin-top:6px'>229 篇 · 目录 xiaodi-lowcode</div></a>
```

- 课程入口统一指向父分类 `/categories/低代码大课/`（229 篇都挂了该父分类），进站后的分期导航由 `index/index.md` 草案承接（其 9 张期目录卡与各期分类一一对应）。
- 计数修正：3291 + 229 = 3520；门数 19 → 20。**主 agent 落地前请核对**两处计数与站点实际（以 hexo categories 页生成为准）。
- 卡片 hover 行为、样式类均沿用现有格式，不新造样式。

## 3. 本扫描产出清单与遗留

- 已产出：`index/course-graph.md`（9 阶段 18 章、概念关系图、35 卡↔229 篇映射、13-4 缺集 + 8 条红线、阅读动线）、`index/index.md`（进站导航草案，含前置/后续阅读与快速通道）。
- 遗留（主 agent）：① courses/index.md 按 §2 diff 落地并核对计数；② 35 卡进站时按 §1.2 表补 1–3 条站内链接；③ 确认 hexo 侧 `低代码预先课/低代码第一期…` 各子分类页已生成（index.md 草案的期卡依赖这些分类路径；若分类 slug 与草案不符需回改）。
