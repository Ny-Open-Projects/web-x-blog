# 课程总编号表（唯一事实源）

> **本表是全工作区唯一的课程编号依据。** 任何目录改名、新课程入库、发布 hookup 之前先查这里。
> 三段目录（`source` 素材 → `target` 卡片 → `blog` 成品）共用**同一套连续编号 1–22**，不再各自编号。
> 建立日期：2026-11-13 · 依据：实盘磁盘计数，非陈旧进度文档。

## 编号规则

1. **1–20**：来自 `work/source/NN.课程名` 的素材序号，一门课一个号，跨三段不变。
2. **21–22**：外部移入的**成品课**（无 source 素材），接续 20 之后编号。
3. **`work/blog/source/_posts/` 下 19 个物理目录保持纯 slug**（`es` / `campus` / …），
   **不**再加数字前缀 —— 改 3282 篇文章路径会破坏发布流水线与已有链接，编号统一由本表承担。
4. `code`（代码片段，2 篇）是**辅助目录、不占课程号**；它是 blog 总览页第 19 张卡片，但不是独立课程。
5. 已删除的编号**不复用**：原 21（渡一前端大师课）由用户裁定清掉，21 号顺延给 DSA 成品课，
   这是本次「做成一套」后的新分配，**不是**历史编号。

## 全表（1–22）

| # | 课程 | source 素材（文件数） | target 卡片 | blog 落点 | 已发布篇数 | 状态 |
|---|---|---|---|---|---|---|
| 1 | Elasticsearch与Go实战 | `1.es-go` (132) | `target/es` (134) | `_posts/es` | 134 | ✅ 已发布 |
| 2 | Kubernetes与云原生KCNA | `2.k8s2-KCNA` (122) | `target/kcna` (123) | `_posts/kcna` | 123 | ✅ 已发布 |
| 3 | Kubernetes集群部署 | `3.k8s3-top` (205) | `target/k8stop` (207) | `_posts/k8stop` | 207 | ✅ 已发布 |
| 4 | Kubernetes认证CKA | `4.k8s4-cka` (88) | `target/cka` (89) | `_posts/cka` | 89 | ✅ 已发布 |
| 5 | Kubernetes生产实践 | `5.k8s5-prod` (74) | `target/k8sprod` (71) | `_posts/k8sprod` | 71 | ✅ 已发布 |
| 6 | Go高并发抽奖项目 | `6.mksz295` (7065) | `target/lottery` (107) | `_posts/lottery` | 107 | ✅ 已发布 |
| 7 | 自主开发PaaS平台 | `7.mksz535` (4223) | `target/paas` (143) | `_posts/paas` | 143 | ✅ 已发布 |
| 8 | 后端校招面试 | `8.mksz540` (124) | `target/campus` (80) | `_posts/campus` | 80 | ✅ 已发布 |
| 9 | 六大数据库存储实战 | `9.mksz615` (496) | `target/storage` (113) | `_posts/storage` | 113 | ✅ 已发布 |
| 10 | APM监控系统实战 | `10.mksz883` (111) | `target/apm` (112) | `_posts/apm` | 112 | ✅ 已发布 |
| 11 | Go面试题集 | `11. go interview` (398) | `work/go-interview` (1402) | `_posts/go-interview` | 1402 | ✅ 已发布 |
| 12 | MySQL面试题集 | `12.MySQL面试指南` (13) | `work/mysql-interview` (154) | `_posts/mysql-interview` | 154 | ✅ 已发布 |
| 13 | Python服务端面试题集 | `13.Python服务端工程师指导面试教程` (56) | `work/py-interview` (238) | `_posts/py-interview` | 238 | ✅ 已发布 |
| 14 | 云原生CI/CD实战 | `14.mksz892` (176) | `target/mksz892` (98) | `_posts/mksz892` | 98 | ✅ 已发布 |
| 15 | 提示词工程与大模型实战 | `15.mksz737` (99) | `target/mksz737` (86) | `_posts/mksz737` | 86 | ✅ 已发布 |
| 16 | RAG全栈技术 | `16.mksz920` (89) | `target/mksz920` (36) | `_posts/mksz920` | 36 | ✅ 已发布 |
| 17 | SpringAI与RAG实战 | `17.mksz948` (79) | `target/mksz948` (31) | `_posts/mksz948` | 31 | ✅ 已发布 |
| 18 | LangChain4j实战 | `18.mksz952` (100) | `target/mksz952` (56) | `_posts/mksz952` | 56 | ✅ 已发布 |
| 19 | 数字货币Python量化投资 | `19.wyy0008` (58) | — | **`work/quant-site`** (27 content md) + `quant-site-static` | — | 🟡 **独立 Next.js 站，不进 hexo** |
| 20 | 人人都能学会数据分析 | `20.体系课` (208) | — | — | 0 | 🔴 **仅素材，未产出** |
| 21 | DSA 多语言算法题库 | — | — | `blog/courses/21.dsa` | — | 🟦 成品课 · 254 题解 / 11 语言 / 15287 文件 |
| 22 | 股市入门实操课 | — | — | `blog/courses/22.股市入门实操课` | — | 🟦 成品课 · 20 章 + 4 附录 / 25 篇 |

**辅助（不占号）**：`code` — `target/code` (2 md) → `_posts/code` (2 篇)。

## 计数基线（2026-11-13 实盘）

| 段 | 数量 | 说明 |
|---|---|---|
| `work/source/` | 20 目录 / 13917 文件 | 原 21 个，渡一清掉后 20 个；全部为 .txt 逐字稿 |
| `work/target/` | 16 目录 / 1490 md | agent 卡片工作区 |
| `work/blog/source/_posts/` | 19 物理目录 / **3282 篇** | 与 `source/courses/index.md` 写死的「19 门课 / 3282 篇」一致 |
| `work/blog/courses/` | 2 门成品 | 在 hexo `source/` 之外，不进渲染链（暂不发布） |
| 全局课程实体 | **22 门** | 18 已发布 + 1 独立站 + 1 仅素材 + 2 成品 |

## 素材完整性（19 / 20 专项，2026-11-13 审计）

| # | 结构 | 空文件 | 缺口 | 判定 |
|---|---|---|---|---|
| 19 量化 | 58 篇 / 11 章 | 2 | 章节 **02 缺**；课时号 1–64 缺 8 个（7,9,10,12,13,56–58）；**「第十课 选币策略」整章仅 1 个 0 字节文件** | ❌ **不完整**，但 `quant-site` 已产出 11 章（含 `09-选币策略.md`），内容由独立站补齐 |
| 20 数据分析 | 208 篇 / **16 周齐全** | 1（第5周 `1-2 什么是Python`） | 周编号无缺口；14 篇 <2KB 多为「本章小结」，属正常 | ✅ **基本完整**（1 篇空稿，99.5%） |
| ~~21 渡一前端~~ | 131 篇 / 单模块「01 技术提升」/ 11 子模块 | 0 | 只有整门课的一个模块 | 用户裁定不需要，已清掉 |

## 变更记录

- 2026-11-13：DSA 与股市课从 `work/target/` 纠正到 `work/blog/courses/`，初编 20/21。
- 2026-11-13：用户裁定「做成一套」→ 删除 `work/source/21.渡一前端大师课`（131 文件，
  移入 `~/.Trash/21.渡一前端大师课_20261113_172755`，清单 `/tmp/duyi_delete_manifest.txt`），
  成品课顺延为 **21 / 22**，与 source 1–20 合并成一套连续编号。
- 2026-11-13：DSA 工具链三次重定向完成，最终指向
  `/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa`；三代旧路径文本残留全 0。

> 注意：`ai/AGENTS.md` 第 2 节规定 **`work/source/` 只读、不删除**。清理渡一为用户明确裁定覆盖该红线，
> 且采用废纸篓可逆方式，未用 `rm`。
