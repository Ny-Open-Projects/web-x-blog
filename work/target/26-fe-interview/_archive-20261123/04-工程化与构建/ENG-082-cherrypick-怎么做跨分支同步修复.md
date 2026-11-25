---
title: [ENG-082] cherry-pick 怎么做跨分支同步修复？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-082：cherry-pick 怎么做跨分支同步修复？
**答**：
- 场景：热修先落在 release 分支，需要原样同步到 main 与其他维护分支。
- 单个提交直接 cherry-pick <sha>；一段连续提交用 ^..范围语法（含起点）。
- 冲突解决后 git cherry-pick --continue；想放弃本次摘取用 --abort。
- 提交信息按惯例追加 origin 标注，GitHub 能据此标记"已同步"，避免重复摘取。

```bash
# 把热修提交摘到当前分支
git checkout release/1.8
git cherry-pick 3f8d2c1

# 摘取一段连续提交（含起点）
git cherry-pick 3f8d2c1^..9a1b4e2

# 冲突解决后继续 / 放弃
git cherry-pick --continue
git cherry-pick --abort

# 提交信息保留来源，便于回溯与去重
git log -1 --format=%B
```
