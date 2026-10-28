---
disableNunjucks: true
title: "course11 面试卡 · 夜间无人值守 SOP"
date: 2026-10-07 23:55:47
categories: [Go面试题集]
tags: [Go面试题集]
---

> 交接文档。**任何 agent / 自动化接手本流水线前必读，并严格遵守其中红线。**
> 最后更新：2026-10-06 23:05（批次 36 收口，72/369）

## 0. 目标与当前断点

- **最终目标**：`source/11. go interview`（course11）全部 **369 篇**机翻稿 → 高质量面试卡，与已完成的课程 8/9/10 共同达成全量覆盖。
- **当前断点（接手时先跑 `queue.py status` 复核，勿信本文档数字）**：
  - 72 done / 297 pending / 414 张卡落盘；XL 72/114，之后 L 124 / M 100 / S 31。
  - `validate.py --strict` → **414/414 PASS、0 error、warn 44**。
  - 本地 commit 已 ahead 41，**未 push**。

## 1. 硬性红线（违反即视为事故）

1. **质量优先于速度**。宁可少产一波，不可出一张错卡。
2. **`source/` 只读**，绝不修改、绝不移动、绝不 commit（每次 `git add` 必须显式列文件，且 `git diff --cached --name-only | grep "go-interview/source/"` 必须为空）。
3. **只本地 commit，禁止 push**。用户明确要求「不 push、不烦用户」。
4. **门禁 0 error 才 done**：`validate.py --strict` 有 error 必须修完，禁止带 error 标记完成。
5. **`MAX_PARALLEL = 1`（串行）**，已在 `queue.py:52` 硬编码。禁止任何形式的并行子 agent。
6. **不新增依赖、不改 `validate.py` 放宽规则**（要改规则须用户拍板）。

## 2. 429 / 额度防护（基于实测，勿拍脑袋调整）

**实测依据**（写死在 `queue.py:52` 注释）：2026-10-03 凌晨 **3 个并行 worker 同时 429 额度耗尽全部失败** → 降为串行后，`metrics.jsonl` 中 **429 计数 = 0**、每任务 `attempts=1`。

因此防 429 的**唯一有效手段就是「不并发」**，配上下面四条闸门：

| 闸门 | 阈值 | 动作 |
|------|------|------|
| 并行度 | `MAX_PARALLEL=1`、`MAX_FILES_PER_AGENT=2` | 单波只派 2 篇，串行执行 |
| ~~波间冷却 `sleep 600`~~ **（2026-10-07 取消）** | **不再休息** | **用户拍板：一项 done 立刻接下一项，串行连续推进** |
| ~~单会话波数上限 4 波~~ **（2026-10-07 取消）** | 不设上限 | 持续串行推进，直到用户叫停或额度异常 |
| 指数退避 | 遇 429：2/4/8/16/30 min 上限 | 退避后重试，不立即重试 |
| 熔断 | `consec_fail ≥ 3` 或 watchdog 命中 429 | **立即停手写快照，不硬抗**，等额度恢复 |

> **节奏口径（用户 2026-10-07 拍板，覆盖 2026-10-06 版本）**：
> 「**一项任务完成，立刻接着做下一项**」——**不休息、不 sleep、不要定时任务**。
> 上文表格里的「`sleep 600` 波间冷却」与「单会话 4 波上限」**均已作废**。
> **重要**：防 429 的唯一有效手段仍是「**不并发**」（`MAX_PARALLEL=1`、不开并行子 agent）。
> 节奏快慢本身不触发 429，只有并发才会——所以可放心串行连续推进。

- **守护进程**：`python3 _pipeline/watchdog.py`（轮询 120s，命中 429 自动写 `.paused` 暂停标记并解冻任务）。恢复后 `python3 _pipeline/watchdog.py --resume`。
- **`--once` / `--status`** 用于单次扫描与查看守护状态。
- **卡死回收器**：`python3 _pipeline/reclaim-stale.py [--minutes 30] [--dry-run]`
  - 背景：`state.json` **不记录任务领取时间戳**，若某会话中途死掉，它占的 2 个任务会永久停在 `running`，
    导致后续所有会话都因「running > 0 → 避让」而**整夜空跑**（2026-10-06 夜发现此隐患）。
  - 判定：以「最新卡片 mtime」与「最新 git commit」为活跃度代理，**两者都**超阈值（默认 30 分钟）才回收。
  - 动作：用 `queue.py reset` 放回 pending——**不用 `fail`**（fail 会累加 `consec_fail` 并施加指数退避惩罚）。
  - **每波开工前都要先跑一次**，放在 `running > 0 → 避让` 判定**之前**。
- **阈值调优纪律**：任何并行度上调，必须**先有 ≥3 批次零 429 的实测数据**才允许 1→2，禁止凭直觉改。

## 3. 单波 SOP（6 步，逐步执行）

```bash
cd /Users/Wang/Code/github/web-x-blog/work/go-interview

# ① 拉一批（串行，2 篇）
python3 _pipeline/queue.py next --wave 1 --per-agent 2

# ② 读两源（source/ 只读），按 house 骨架产 12 张卡（5 主卡 + 1 深卡 × 2 源）

# ③ 全量门禁（必须 0 error）
python3 _pipeline/validate.py --strict

# ④ 标记完成（--cards 逗号无空格）
python3 _pipeline/queue.py done <task1> --cards a,b,c,d,e,f
python3 _pipeline/queue.py done <task2> --cards a,b,c,d,e,f

# ⑤ 更新断点日志 ai/memory/MEMORY.md（追加批次明细 + 进度概要行）

# ⑥ 本地提交（显式列文件，排除 source/ 与杂项 ERRORS.sample.md / TODO-worker.md）
git add <12 卡> ai/memory/MEMORY.md _pipeline/state.json _pipeline/metrics.jsonl
git commit -m "course11 waveN: ..."
```

## 4. 卡片骨架铁律（house format，缺一即 error）

主卡必须含下列 **`##` 独立标题**（绝不可用 `**加粗**` 内联冒充标题）：

```
# 标题
> 分类：... | 难度：... | 题型：... | 频率：... | 关键词：**...**
> 原文锚点：第 X~Y 段「...」          ← 规则 8 强制
## 一句话总述
## 面试官视角
## 主问答                              ← 含 **Q（面试官原话）：** + 1. **点**：编号加粗，≥3 条
## 追问链                              ← 5 列表格 L1~L5，含「答不出停在哪档」
## 版本与兼容性                        ← 表格，非空
## 关键代码
## 总结与追问预判
## ⚠️ 原文纠错                        ← 标题必须精确，见下
```

- **纠错节标题铁律**：必须精确为 `## ⚠️ 原文纠错`。写成「`## ⚠️ 原本纠错`」会触发规则 3b **error**（历史踩坑：批次 30 因此 10 张卡全 FAIL）。
- **纠错节必须含 `[经验]` 分级标记**，且 ≤250 汉字（超则 warn）。
- **主卡体量不设字数上限**（2026-10-07 用户拍板取消；原「≤700 汉字」已在 `validate.py` 规则 3 移除，现仅统计不阻断）。质量靠骨架完整性与信息密度保证，**一律禁止为凑字数砍追问链停档判据、版本栅栏或验证数据**。
- **深卡（`.deep.md`）**必须含 `## 思路与架构` / `## 方案取舍` / `## 答题技巧`；深卡 early-return，不校验体量与黑名单。

## 5. 文件名映射铁律

正则：`^\d{3,4}-[a-z0-9]+(-[a-z0-9]+)*(\.deep)?\.md$`（前缀必须 **3~4 位数字**）。

- **chapter < 10**：课次**补零成 3 位**。4-4→`404-`、4-11→`411-`、4-19→`419-`、6-9→`609-`。
- **chapter ≥ 10**：原章号**直接拼接、单课次不补零**。12-22→`1222-`、12-43→`1243-`、15-2→`152-`、10-25→`1025-`、18-14→`1814-`。

## 6. 崩坏词处理（机翻稿固有）

源稿是 ASR+机翻，`MySQL/InnoDB/B+树/索引/Redis/AOF/RDB/singleflight/goroutine/CyclicBarrier/LIKE/EXPLAIN/子查询/物化/聚簇索引` 等大量被音译为崩坏词。

- **正文与纠错节一律写规范术语。**
- **纠错节禁止字面出现黑名单词**（如 `引诺DB`/`妈妈引擎`/`护士锁`/`自选锁`/`CQ语句`/`构语言`/`派森` 等）。
- **统一泛述句式**：「源码将 X 音译为多组崩坏词，本卡统一为 X」——**不要举例写出崩坏词本身**，否则触发规则 11 error。

## 7. 分诊纪律（R1~R4）

纯非技术内容（闲聊/广告/无信息量）整篇剔除，并记入 `_pipeline/TRIAGE.md` 台账，不产卡。

## 8. 晨间交付（带具体数字）

停止前必须输出状态快照，便于次日验收：

```
批次 N 收口：X/369 done / Y pending / Z 卡落盘
validate.py --strict：Z/Z PASS、0 error、warn W
本批产出：<文件名清单>
本地 commit：ahead N（未 push）
429 情况：metrics 中 429 计数 = n，attempts 均值 = m
下一步：续跑 python3 _pipeline/queue.py next --wave 1 --per-agent 2
```

**要求：用具体数字（字节/md5/计数）说话，禁止含糊状态汇报。**
