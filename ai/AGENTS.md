# ai/AGENTS.md —— 接手事实源

> 本仓库的**交接事实源**。任何 agent 接手前必读，读完再动手。
> 根目录的 `AGENTS.md` 只是指针，一切以本文件为准。

## 1. 这是什么

**个人创作者工作空间。** 三个目录各司其职，位置与职责不可混：

- **输入 `work/source/` —— 机器翻译的结果（MT output）。** 622+ 个 .txt，来自 ES / K8s 等面试课程的**机翻稿**。不是人工转写，**也不是 agent 产出的**，只进不出。
- **工作区 `work/target/` —— agent 转换后的目录，也是 agent 的主工作目录。** 拆题 / 纠错 / 上 front-matter / 质检，全在这里落盘，所有转换结果最终归位到这里。
- **出口 `work/blog/` —— hexo 初始化过的站点目录。** 把 target 里的东西**分类**（categories / tags）后生成静态站，本地起服务预览、对外发布。

- 输入：`work/source/`（622+ 个 .txt 转写稿，来自 ES / K8s 等面试课程）
- 产出：`work/target/`（题目卡片、索引、结构化文档）
- 终点：`work/blog/`（对外成稿）

## 2. 红线（不可协商）

- **`work/source/` 只读。** 原始素材锁死，只读取、不改写、不删除、不归集。
- **业务文件不进仓库根。** 根只有 `README.md` / `AGENTS.md` / `.gitignore` 三个文件。
- **agent 相关一律进 `ai/`。** 新增 prompt / 模板 / 记忆 / 技能先问一遍"是不是该放 `ai/`"。
- **卡片必须过质检再落 target。** 机翻残留、事实错误、重复题，任一命中即打回，不许带病入库。
- **质量优先于速度。** 慢可以，糊不行。宁可少产出，不许错产出。

## 3. 目录约定

```
work/
├── source/    机器翻译的结果（只读取，不进站）  按「数字.科目」分目录，如 4.es-go
├── target/    agent 转换后的目录 = agent 的主工作目录  按科目归档，如 es/ k8s/
├── blog/      hexo 站点（已初始化）  把 target 内容分类后生成静态站
ai/            agent 层
├── AGENTS.md      本文件（事实源）
├── prompts/       prompt 模板
├── templates/     产出模板（选题卡 / 题目卡）
├── memory/        项目长期记忆、已定约定
└── skills/        项目级技能
```

## 4. 标准流水线

```
source（机翻结果）
   ↓ 解码 → 切分 → 拆题 → 写卡片 → 上 front-matter → 质检
target（agent 主工作目录）
   ↓ 按 categories/tags 分类
blog（hexo 站点，本地起服务预览 / 发布）
```

三段式拆解（按内容类型选）：**概念题**（是什么）、**原理题**（为什么）、**实战题**（怎么做 / 怎么排）。

### target → blog 怎么进站

卡片模板（`ai/templates/CARD.md`）自带 **hexo front-matter**，所以链路极短：

```
work/target/{科目}/{卡片}.md  --拷-->  work/blog/source/_posts/{卡片}.md  → hexo 分类 → 静态站
```

- **分类靠 `categories` / `tags` 两个字段**，站上归档、标签页全靠它
- 不许在 `blog/source/_posts/` 里二次改写内容 —— 站上内容以 `target/` 为准，`target` 改完重新拷过去
- `blog/` 是生成侧（`public/` 产物、node_modules 不入库，已 gitignore）

## 5. 复用，别重造

用户级已有 skill，命中就直接用，不要在 `ai/skills/` 里复制一份：

- `interview-card-pipeline` —— 转写稿 → 面试题卡片的**主流水线**（机翻解码、去重、格式质检、索引生成都在它里面）
- `humanizer` —— 成稿去 AI 味
- `webfault-night-shift` / `volcano-pipeline` —— 同类跨会话流水线的**断点续跑范式**（照它的写法抄）

只有流水线覆盖不到的环节，才在 `ai/skills/` 里补项目级技能。

## 6. 断点续跑

- 长任务分批推进，**每批结束留状态**：`ai/memory/` 里记「已处理到哪个文件 / 哪张卡」。
- 中断后接手，先读 `ai/memory/MEMORY.md`，再读 `work/target/` 的现有索引，从断点继续。
- **别用"重新全跑一遍"兜底** —— source 有 622 个文件，全量重跑成本不可接受。

## 7. git 规矩

- 本地 commit 由人决定，agent **不主动 push**。
- 大批量产出的 commit 单独提、信息写清批次与条数。

## 8. 当前状态

- `work/source/`：5 个科目目录（4.es-go、6.k8s2-KCNA、7.k8s3-top、8.k8s4-cka、9.k8s5-prod），共 622 个文件
- `work/target/`：空，尚未产出（**agent 的主工作目录，活都砸在这**
- `work/blog/`：hexo **8.1.2** 已初始化，主题 landscape 1.1.0，渲染器 ejs + markdown-it
  - 起本地服务：`cd work/blog && ./node_modules/.bin/hexo server -p 4000`
  - 重新生成：`./node_modules/.bin/hexo generate`
- 最近动作：工作空间初始化（骨架 + 交接文档 + hexo 站点）
