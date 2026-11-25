---
title: [AIC-021] AI 一次改了十几个文件，diff 太大看不过来怎么办？大 diff 的拆解审查法？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-021：AI 一次改了十几个文件，diff 太大看不过来怎么办？大 diff 的拆解审查法？
**答**：
- 先分层缩小范围：`git diff --stat` 看每个文件的变更量，只细读高变更量的核心文件；纯机械改动（import 排序、重命名）靠 rename/lint 工具确认，不逐行看。
- 按依赖序审：类型定义 → 工具函数 → 业务逻辑 → UI，上层依赖下层，先把底层审对上层才有意义。
- 用「意图对照」：拿任务描述列出预期的改动点清单，diff 里每处改动都对应到清单，多出来的就是越界改动，缺失的就是没做完。
- 对 Agent 的预防措施：任务里就要求「分步提交」，每步一个 commit，审查粒度自然变小。
- 追问钩子：可提「让另一个 AI 审 AI 的 diff 不可全信，但适合做第一遍漏斗」。

```bash
# 大 diff 三步审查法
git diff --stat                                # ① 范围与体量，找重灾区
git diff -- src/types src/utils                # ② 按依赖序：先底层
git diff -- src/hooks/useCart.ts               # ③ 核心业务逻辑逐行

# 意图对照：预期改动点逐条核对
grep -n "setQuantity" src/hooks/useCart.ts     # 预期点 1：数量修改
grep -n "coupon" src/                          # 预期点 2：优惠码
git diff --diff-filter=D --name-only           # 越界检查：谁被删了？
```
