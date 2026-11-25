---
title: [ENG-083] git 回滚全家桶：reset、revert、reflog 分别什么时候用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-083：git 回滚全家桶：reset、revert、reflog 分别什么时候用？
**答**：
- 未推送的本地提交：git reset --soft 保留改动在暂存区，--hard 连工作区一起丢（谨慎）。
- 已推送的共享提交：git revert 生成反向提交，不改写历史，是协作分支唯一安全的回滚。
- 任何"丢失"的提交：git reflog 记录了 HEAD 的全部移动，git reset --hard HEAD@{n} 找回。
- 精细化撤销：git restore 管工作区/暂存区的文件级撤销，比 checkout 语义更清晰。

```bash
# 1. 未推送：软回滚，改动退回暂存区
git reset --soft HEAD~1

# 2. 已推送：反向提交，不改写历史
git revert --no-edit 3f8d2c1

# 3. 误删/误 reset：reflog 找回所有 HEAD 移动记录
git reflog
git reset --hard HEAD@{3}

# 4. 文件级撤销：暂存区与工作区分别处理
git restore --staged src/app.ts
git restore src/app.ts
```
