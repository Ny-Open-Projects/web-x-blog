---
title: [ENG-035] Git Flow 与 Trunk-based 两种分支模型怎么选？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-035：Git Flow 与 Trunk-based 两种分支模型怎么选？
**答**：
- Git Flow：master/develop 双长期分支 + feature/release/hotfix，发布节奏重，适合版本化交付。
- Trunk-based：所有人高频小步合入 main，短生命周期分支 + 功能开关，适合持续部署。
- 现代前端团队多用 Trunk-based + PR review + CI 卡点，减少合并冲突与分支漂移。
- 关键是分支存活时间越短，集成风险越小。

```bash
# Git Flow 示例
git checkout -b feature/login develop
git commit -m "feat: add login form"
git checkout develop && git merge --no-ff feature/login

# Trunk-based 示例
git checkout -b fix/typo main
git push origin fix/typo
# PR review 通过后 squash merge 到 main，分支存活通常不超过两天
```
