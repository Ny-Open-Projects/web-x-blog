---
title: [ENG-080] rebase 与 merge 的工程决策怎么做？团队策略怎么定？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-080：rebase 与 merge 的工程决策怎么做？团队策略怎么定？
**答**：
- 核心红线：已推送到共享分支的提交禁止 rebase，重写历史会让协作者本地仓库错乱。
- 推荐策略：本地未推送的零散提交用 rebase 收拾干净；合并回主干用 merge --no-ff 保留合并节点可回溯。
- 团队可选两种风格之一并写进规范：线性历史（PR squash merge）或保留拓扑（merge commit），混用最糟。
- 工具配套：git pull 默认配 --rebase 减少无意义合并提交；冲突在 rebase 中逐个解决，范围更小。

```bash
# 团队策略落地示例
# 1. 本地同步主干：变基拉取，避免产生 merge commit
git config pull.rebase true

# 2. feature 分支整理：只对未推送的提交做交互式变基
git rebase -i origin/main

# 3. 合入主干：保留合并节点，方便整体回滚一个特性
git checkout main
git merge --no-ff feature/login -m "Merge feature/login"

# 4. PR 平台配置：squash merge 保持线性历史
gh repo edit --merge=false --squash=true
```
