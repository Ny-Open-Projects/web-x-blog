# 课程总编号表（唯一事实源）

> **本表是全工作区唯一的课程编号依据。** 任何目录改名、新课程入库、发布 hookup 之前先查这里。
> 三段目录（`source` 素材 → `target` 卡片 → `blog` 成品）共用**同一套连续编号 1–29**，不再各自编号。
> 建立日期：2026-11-13 · 依据：实盘磁盘计数，非陈旧进度文档。

## 编号规则

1. **1–20**：来自 `work/source/NN.课程名` 的素材序号，一门课一个号，跨三段不变。
2. **21–22**：外部移入的**成品课**（无 source 素材），接续 20 之后编号。
3. **`work/blog/source/_posts/` 下 23 个物理目录保持纯 slug**（`es` / `campus` / …），
   **不**再加数字前缀 —— 改 3282 篇文章路径会破坏发布流水线与已有链接，编号统一由本表承担。
4. `code`（代码片段，2 篇）是**辅助目录、不占课程号**；它是 blog 总览页第 19 张卡片，但不是独立课程。
5. 已删除的编号**不复用**：原 21（渡一前端大师课）由用户裁定清掉，21 号顺延给 DSA 成品课，
   这是本次「做成一套」后的新分配，**不是**历史编号。

## 全表（1–29）

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
| 11 | Go面试题集 | `11. go interview` (398) | `work/go-interview` (1405) | `_posts/go-interview` | 1413 | ✅ 已发布 |
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
| 23 | Go微服务精讲：Go-Zero全流程实战即时通讯 | —（成品课，外部交付） | `target/mksz826` (138) | `_posts/mksz826` | 138 | ✅ 已生成 |
| 24 | 真实高质量低代码商业项目，前端/后端/运维/管理系统 | `24.真实高质量低代码商业项目-前端后端运维管理系统` (547 md + 547 srt) | `target/mksz824` (512) | `_posts/mksz824` | 512 | ✅ 已生成（18 波润色收口，hexo 14021 files 构建通过） |
| 25 | 小滴课堂 全栈多端低代码平台项目大课（React+NestJS，8期+预先课） | `25.xiaodi-lowcode` (1253 文件，只读) | `target/25-lowcode`（229 篇 + 35 卡 + scan1~10 + review-b1~b10 + apply-* + eng-a/b 终审） | `_posts/xiaodi-lowcode{,-cards}` | 229+35 | ✅ 已发布（专家终审 264 成品全过，hexo 13384 files 构建通过） |

| 26 | 前端面试工程（27 专题大厂题库） | `26.前端面试工程` (30 md / 8.9M，外置盘成品题库入库，只读) | `target/26-fe-interview` (11 大类 / 4917 卡，面试题+笔试题双标签) | 待定（`_posts/fe-interview`） | 0 | 🟡 已拆题入库，扩量生成中（目标每类 5000 题） |
| 27 | Python面试3000（工程向原理+追问链题库，前作13号） | `27.python-interview-3000` (3086 文件：72 章节 md + 3000 代码 + 脚本，外置盘成品题库入库，只读) | `target/27-python-interview` (8 大类 / 3015 卡：Q 系面试题 3000 + A 系笔试题 15) | 待定（`_posts/py-interview-3000`） | 0 | 🟡 已拆题入库，扩量生成中（目标总量 5000+） |
| 30 | 生产级AI Agent开发 | —（成品课，外部交付） | `target/mksz980` (116) | `_posts/mksz980` | 116 | ✅ 已生成（原编 27，2026-11-18 因与 27 号 Python面试3000 撞号顺延，物理目录名不变） |
| 31 | 多Agent+Skills+SpringAI | —（成品课，外部交付） | `target/mksz981` (125) | `_posts/mksz981` | 125 | ✅ 已生成（原编 28，同上顺延） |
| 32 | 股票异动风控机器人 | —（成品课，外部交付） | `target/mksz982` (62) | `_posts/mksz982` | 62 | ✅ 已生成（原编 29，同上顺延） |
| 33 | Java后端面试全库（对标阿里P10） | `33.java-interview` (160 文件 / 45.4M：体系 25 册 + 13 域事实矩阵 + 双 2 万题库 + 自测三件套，win1 交付成品入库，只读) | `target/33-java-interview` (5463 卡：体系精讲 12 章 + 实战演练 9 类 + 导览 3 + 背诵卡 13 域 2550 + 话术卡 13 域 2550) | `_posts/java-interview` (363) + `_posts/java-interview-cards` (2550) + `_posts/java-interview-talk` (2550) | 5463 | ✅ 已进站（hexo 11101 files 构建通过） |
| 34 | Java后端进阶全套（四模块：面试专题·就业指导·十大中级项目·六大进阶项目） | `34.java-suite` (外置盘 ai-done 07/08/09/10 四目录归档，161M / 11726 md / 376 png；排除 wav/audio_line 19G/vision_line/materials-code 1.1G，只读锁) | `target/34-java-suite` (M1 257 + M2 12 + M3 1629 + M4 214 单元重写稿 = 2112 篇带 front-matter；QC 门禁全过) | `_posts/java-suite` (2112 篇单目录，categories 分四模块) + `source/images/java-suite/m1` (188 png) + `source/demos/java-suite` (8 交互 demo) | 2112 | ✅ 已进站（hexo 14302 files 构建通过，node 22） |

**辅助（不占号）**：`code` — `target/code` (2 md) → `_posts/code` (2 篇)。

## 计数基线（2026-11-20 实盘）

| 段 | 数量 | 说明 |
|---|---|---|
| `work/source/` | 25 目录 | 26/27 号入库后 23 个；33 号 java-interview 入库后 24 个；34 号 java-suite 入库后 25 个 |
| `work/target/` | 27 目录 | 26 门旧课 + 34-java-suite（2112 篇） |
| `work/blog/source/_posts/` | 29 物理目录 / **11574 篇** | 导航页 26 门卡（已补 java 34） |
| `work/blog/courses/` | 2 门成品 | 在 hexo `source/` 之外，不进渲染链（暂不发布） |
| 全局课程实体 | **27 门** | 含 2 门成品 + 1 独立站 + 素材/产出中课程 |

## 素材完整性（19 / 20 专项，2026-11-13 审计）

| # | 结构 | 空文件 | 缺口 | 判定 |
|---|---|---|---|---|
| 19 量化 | 58 篇 / 11 章 | 2 | 章节 **02 缺**；课时号 1–64 缺 8 个（7,9,10,12,13,56–58）；**「第十课 选币策略」整章仅 1 个 0 字节文件** | ❌ **不完整**，但 `quant-site` 已产出 11 章（含 `09-选币策略.md`），内容由独立站补齐 |
| 20 数据分析 | 208 篇 / **16 周齐全** | 1（第5周 `1-2 什么是Python`） | 周编号无缺口；14 篇 <2KB 多为「本章小结」，属正常 | ✅ **基本完整**（1 篇空稿，99.5%） |
| ~~21 渡一前端~~ | 131 篇 / 单模块「01 技术提升」/ 11 子模块 | 0 | 只有整门课的一个模块 | 用户裁定不需要，已清掉；**原始转写产出仍在 Desktop，可恢复**（见下） |

## 变更记录

- 2026-11-20（凌晨收官）：**java-suite 四模块入库为 34 号**（用户指令：扫描外置盘 ai-done 07/08/09/10 四目录生成一门新课分四模块，每模块润色深化，夜间无人值守持续推进）。
  - 素材：`/Volumes/SAMSUNG/ai-done/` 的 07 面试专题（house style 成品 260 md + 188 png）、08 就业指导（成品 12 篇）、09 JavaEE 十大中级项目（blog 1629 + raw 双线 5198）、10 精英进阶（1671 份 merged 口播原稿）。归档 `work/source/34.java-suite`（161M，排除 wav/audio_line 19G/vision_line 418M/materials-code 1.1G，rsync 尾斜杠语义坑与先锁只读坑已修，chmod a-w 只读锁）。
  - M1/M2/M3：`ai/scripts/ingest_java_suite.py` 机械处理（front-matter + 图片/demos 绝对路径改写 + 坏图剔除 + m3 重命名防冲突），M1 补 INDEX 漏收 5 篇章名、剔 2 篇管线元文档；M3 的 12 处 TODO 为教学占位豁免、15 篇坏图剔除、相对内链降级。
  - M4 重写：`m4_build_units.py` 按 manifest 聚合 **214 写作单元**（重名 video_id 23 条记 _dup_report.json 不编造），子 agent 逐单元重写为 house style 深稿（去口播腔、画面线纠错、双 agent 会话分头推进避免撞车），`m4_qc.py` 门禁（front-matter/title 双引号/CJK 分级门槛/口播腔/围栏），**214/214 PASS**。脚本四件套：m4_build_units / m4_next_prompt / m4_mark_done（含 34.java-suite 点号误写自愈 recover_stray）/ m4_qc。
  - 进站：`_posts/java-suite` **2112 篇**（M1 257 + M2 12 + M3 1629 + M4 214），188 png → `source/images/java-suite/m1`，8 demos → `source/demos/java-suite`。导航页（source/courses/index.md + 根 index.md）补 34 号卡，26 门课 / 11574 篇。hexo 全量构建 **14302 files 通过**（node 22；系统 node16 报 strip-ansi ESM 错）。
  - 已知豁免：M4 QC 对 <40KB 小源料单元字数门槛降至 1200；M1 INDEX 声称 256 篇实为 257（含术语注解卡）；09 交接文档 INDEX「2085 篇」为陈旧数字未采信，以实盘 1629 为准。
- 2026-11-18（夜间）：**java-interview 入库为 33 号**（用户指令：分析 win1 的 3 个备份 zip、按本项目约束生成新课程、可背诵快速入职、细节深挖、夜间无人值守持续推进）。
  - 素材：`/Volumes/SAMSUNG/ai-done/win1/java-interview`（Windows 侧交付的「阿里 P10 面试准备全库」成品题库，JDK 21 实测 + 官方核对背书）。三 zip 审计：11-14（体系快照，31 文件，Windows 反斜杠打包）、11-16（142 文件，+追问地图/对话剧/闭卷笔试/11 域题库/arthas 沙盘）、11-17（164 文件，+agent 手写笔试/agent-dev 与 java-ai 双域/闪卡三件套）；**live 目录比 z17 还新 8 个文件**（exams 面板与双域 banks 重建于 11-17 01:52），以 live 为准入库。
  - source 归档：`work/source/33.java-interview`（160 文件 / 45.4M，排除 maven target/ 与 ._*，逐文件 cmp 与 live 全一致，chmod a-w 锁只读）。
  - 拆题：`ai/scripts/split_java_interview.py` → `target/33-java-interview` **2913 卡**：体系精讲 12 章（###题/###卡片/章节段，156 题 + 概念卡/追问链/速记卡）、实战演练 9 类（手写代码 12 / Agent 手写笔试 10 / 对话剧 10 / 闭卷笔试 9 / 模拟卷 20 / 快问快答 9 / 追问地图 26 / 方法论实录 8 / 全卷速记卡 18）、导览 3、**背诵卡 13 域 2550**（事实矩阵一条一卡：事实/原理/误区×3/用法/锚点）。质检 `ai/scripts/qc_java_interview.py` 机检 0 问题。
  - 源缺陷处置：agent-dev.txt 第 37 行 ID 笔误 JA-033→AD-033（拆题时归一化，source 未动）；源 INDEX.md 统计为陈旧版 6145 题，未采信，以 DELIVERY.md（20908 条）为准；quiz 题库（笔试 22921 + 面试 18006）不拆卡进站——系矩阵模板生成、重复度高，留在 source 供 grep/刷题面板用，站点进精选背诵层。
  - 进站：`_posts/java-interview`（363）+ `_posts/java-interview-cards`（2550），categories=[Java面试, 子类]，全卡带 disableNunjucks 防模板注入；hexo clean+generate **8096 files 通过**。发布脚本 `ai/scripts/publish_java_interview.py`（幂等，以 target 为真源）。
  - 夜间扩量（同日续）：**话术卡 2550** 进站 `_posts/java-interview-talk`。分组规则：题型规范序（概念<误用<原理<工程<结论<边界<追问，版本演进通配）回退即切组，13 域 cycles==facts 行数全等校验通过（`ai/scripts/split_java_talk.py`）；一知识点一卡 n 问打包（问法+标准话术+评分点）。源缺陷机械归一：java-banks java-basics 域 769 处「。。」→「。」（模拟卷零星同修，归一化下沉在 write_card 单一漏斗）。hexo 重建 **11101 files 通过**；抽样事实核对（RD-001/002/003、JV-001/002）无事实错误。
  - 外置盘源删除（用户指令「做完之后可以把拖给你的删除」）：删前把 live 的 maven target/（4 文件）补入归档升为 164 文件全量超集（164/164 cmp 一致），三 zip 哈希审计证明均为 live 子集无独有数据；live 目录 + 3 zip `mv` 进废纸篓 `~/.Trash/java-interview-win1_20261118_003256/`（未用 rm），废纸篓副本复核 164/164 一致、zip 字节数与原件相同。唯一留存 `work/source/33.java-interview`。
  - 编号冲突修正：27 号双重占用（mksz980 成品课 vs python-interview-3000，后者有物理目录与用户指令背书），mksz980/981/982 顺延为 **30/31/32**（物理目录名 mksz-* 不变，卡片未写死编号，波及面为零）；本课顺延取 **33**。
  - 导航页 `courses/index.md` 20→25 门（补 mksz826/980/981/982 三课漏登记 + 本课）/ 3555→6912 篇。
- 2026-11-17：**python-interview-3000 入库为 27 号**（用户指令：纳入 target、参考前作 13 号 Python 服务端面试题集、扩展到 5000 题以上冲大厂资深、可背诵可复盘、含笔试题）。
  - 外置盘 `/Volumes/SAMSUNG/ai-done/mac1/python-interview-3000`（1.1G，大头为 site/backups/db）→ 归档 `work/source/27.python-interview-3000`（22M / 3086 文件，排除 site、backups、*.db、node_modules、._*，只读锁定）。
  - 源为 2026-11-13 审核过的成品题库：Q001–Q3000 六大类 + A 系算法专题，每题「问→答→可运行代码→追问链」，docs 与 code 一一对应，审核报告全量机检通过。
  - 拆题脚本 `ai/scripts/split_py_interview.py`（坑：扩产批次是 4 位题号，正则须 `\d{3,4}`），落 `target/27-python-interview/01..08-*` 共 **3015 卡**；A 系与后续场景/编程题标 `type: 笔试题`。
  - 与前作 13 号（`work/py-interview`，238 卡，速查向）互补：13 号是背诵速查，27 号是原理深挖+追问链，题号体系独立（Q/A）。
  - 外置盘原目录已按用户指令删除：删前 3086/3086 文件逐个 cmp 校验与归档一致（site/backups/db 按排除项豁免），`mv` 进废纸篓 `~/.Trash/python-interview-3000_20261117_234706`，未用 `rm`。

- 2026-11-13：DSA 与股市课从 `work/target/` 纠正到 `work/blog/courses/`，初编 20/21。
- 2026-11-13：用户裁定「做成一套」→ 清掉 `work/source/21.渡一前端大师课`（131 文件 / 4.3M），
  成品课顺延为 **21 / 22**，与 source 1–20 合并成一套连续编号。
  - 操作方式：`mv` 到 `~/.Trash/21.渡一前端大师课_20261113_172755`，**未用 `rm`**。
  - **实测修正**：废纸篓副本随后被系统清空（`~/.Trash` 于 17:28 后为空），该恢复路径已失效。
  - **真实恢复源**：原始转写产出 `~/Desktop/dy-transfer-2026-11-02/outputs/21.渡一前端大师课`
    完整保留 —— 131/131 文件名与删除清单一致、0 空文件、总字节 **4,202,082** 与删除前实测一致、
    内容特征匹配，SHA256 基线 `3e4a2e16ba06597ef0bcf9ec67121bda605156a088744e122c2dffa1da1ecd97`。
    删除清单：`/tmp/duyi_delete_manifest.txt`（131 条）。
- 2026-11-13：DSA 工具链三次重定向完成，最终指向
  `/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa`；三代旧路径文本残留全 0。

- 2026-11-17：课程 11 吸收 Desktop 材料 `~/Desktop/go-interview`（go 面试卡流水线的**原始工作区**，2026-10-02~10-07；
  项目侧 `work/go-interview` 由它 fork 续跑并重编号扩充到 1394 卡）。三遍扫描结论：与本项目**高度同源**——
  source 逐目录一致（21 章 398 文件）；材料 378 张旧卡 ≈97% 已被项目覆盖或超越（0 文件名重叠、内容级比对确认）。
  补入真缺口 **9 张卡**（target 1394→1405，blog 1402→1411）：
  ch20 求职 5 张（**2001–2005**：录用条件三层拆解 / 岗位画像与单源孤证 / 谈薪与年包到手测算 / 大小公司决策矩阵 / 试用期法定红线，各带可重跑实测脚本）、
  ch18 Linux 实操 2 张（**1854** 取 tmp 权限与打印偶数、**1855** 求和五法与权限三层扩展，BSD/GNU 差异实测）、
  ch08 runtime 细节 2 张（**821** 静态锁分级与 m 持锁上限、**822** 调度延迟抽样 /sched/latencies，各带 .deep）；
  并解除 **815 卡**「上限 10」[存疑]（真相：locksHeld[10] 仅在 GOEXPERIMENT=staticlockranking 下维护，默认构建无此限制，指向 821）。
  材料独有交付物 读物 3 册 / 背诵清单 / 复习路线为旧 378 卡库上的生成产物（内容=卡片聚合、卡号已过时），格式能力由
  `_pipeline/gen-*.py` 保存（补齐了缺失的 `gen-review-path.py`），过时内容不搬。
  删除方式：`mv` 到 `~/.Trash/go-interview_20261117_*`（未用 `rm`）。
- 2026-11-17：**mksz824 低代码商业项目入库为 24 号**。用户裁定统一命名「真实高质量低代码商业项目，前端/后端/运维/管理系统」。
  - 外接盘原目录 `mksz824-低代码商业项目` → `24.真实高质量低代码商业项目-前端后端运维管理系统`（827M，含 graph/blog/platform 历史产出）。
  - source 复制入库：`work/source/24.真实高质量低代码商业项目-前端后端运维管理系统`，547 md + 547 srt / 23 章 / 0 空文件，完整性 ✅。
  - 素材为视频转文字稿（含 `_` 后缀文件名与全角空格），产出线：target `mksz824` → blog `_posts/mksz824`。
  - 外接盘旧 HANDOFF.md 描述的是 Windows 侧平行工程（platform/），其硬约束仅约束当时会话；本轮按用户指令重扫并产出。
- 2026-11-17：**小滴课堂低代码大课入库为 25 号**（用户夜间指令：全目录分析 + 多轮扫描榨干知识点后删除外置盘源目录）。
  - 外置盘 `/Volumes/SAMSUNG/ai-done/小滴课堂低代码大课`（460M，大头为 dist/.next/node_modules 构建产物）→ 归档 `work/source/25.xiaodi-lowcode`（正文 1253 文件 / 39M，排除构建产物，抽样 cmp 校验一致，只读锁定）。
  - 21/22 号已被 DSA / 股市课占用，24 号为 mksz824，故顺延编 25（初占 22 号已纠正改名）。
  - 产出线：target `25-lowcode` → blog 待定。
- 2026-11-17（同日后续）：**25 号完成十轮扫描 + 进站**，外置盘源目录已按用户夜间指令删除。
  - 十轮扫描（结构/正文/代码/文档/机械质检/口径核实/物料深挖/知识卡/图谱索引/终检）报告全在 `target/25-lowcode/reports/`（scan1~scan10），35 张知识卡在 `target/25-lowcode/cards/`，总图谱在 `target/25-lowcode/index/`。
  - 229 篇进站 `_posts/xiaodi-lowcode`（target/25-lowcode/posts 为真源，front-matter categories=[低代码大课, 各期]）+ 35 卡 `_posts/xiaodi-lowcode-cards`；hexo 4244 files 构建通过；courses/index.md 19→20 门 / 3291→3555 篇，加「全栈低代码平台大课」卡片。
  - 扫描6 修正 A1~A10 全部落地（RBAC 夸大、接口路径跨期不一致、缓存篇 5 处、函数/字段名等）；13-4 集为课程原始缺集（无视频无博客）。
  - 外置盘 `/Volumes/SAMSUNG/ai-done/小滴课堂低代码大课`（1691 文件）已 `rm -rf`（用户夜间指令明确授权），删除记录 `target/25-lowcode/reports/deleted-manifest.txt`；工作区归档 `work/source/25.xiaodi-lowcode`（1253 文件）为唯一留存。
- 2026-11-18~19：**25 号专家终审完成**。低代码专家视角逐篇审核 229 篇 + 35 卡 + 两个配套工程（review-b1~b10 + review-eng-a/b + review-final.md），累计发现问题 ~470 处并全部修正落地（apply-review-b1~b10 十份日志）；hexo 13384 files 构建通过。工程侧 P0×12（B：裸 MD5 密码/验证码爆破/IDOR/SSR XSS 等 9 项；A：未鉴权 RCE 面/租户写路径失效/镜像构建必失败 3 项）未改工程源码，博客侧全部按「教学级参考实现」口径加限定。
- 注意：`ai/AGENTS.md` 第 2 节规定 **`work/source/` 只读、不删除**。清理渡一为用户明确裁定覆盖该红线，
> 操作用 `mv` 到废纸篓、未用 `rm`；废纸篓副本虽被系统清空，但 Desktop 原始产出完整，数据未丢失。

- 2026-11-20 03:13：**课程 11 全库审核完成（轮 1 终）**。37 批 × ~40 张覆盖 target 全部 1405 卡，
  六维事实审核（技术事实/版本口径/引用断链/代码实跑核数/错别字机翻/数字自洽）+ 全库终扫
  （h1 重复 0、断链 0、Desktop 残留 0）。累计修复 22 处并全部同步 blog：
  编译/运行级 9 处（105 缺 import、1506 `_ = time.Sleep` 非法、144/186 参数守卫、506 双卡常量重复 key+常量折叠、420 var 未用、914 双返回值赋值、1840 族 4 卡 demo 崩溃）
  + 形态级 13 处（108/113/1113×2/1115/201/113?/1420/913?/513×2/605 片段误标与断链）。
  豁免规则 8 条固化于 _pipeline/AUDIT-LEDGER.md 待修模式区；心跳/游标/锁/台账机制随审核结束停用。
  游标 1 1405；blog 同步 1413 篇不变。
