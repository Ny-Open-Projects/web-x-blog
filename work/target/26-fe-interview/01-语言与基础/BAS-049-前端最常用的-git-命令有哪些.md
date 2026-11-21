---
title: [BAS-049] 前端最常用的 git 命令有哪些？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-049：前端最常用的 git 命令有哪些？
**答**：
- 日常六件套：status、diff、add、commit、push、pull。
- 分支：`switch -c` 新建切换、merge/rebase 合并（rebase 黄金法则：不 rebase 已推送的公共分支）。
- 补救：restore 丢弃工作区改动、revert 生成反向提交（线上分支用）、reset 本地回退、stash 临时暂存。

```bash
git status && git diff            # 先看改了什么
git switch -c feat/login          # 新建并切换分支
git add -p                        # 交互式分块暂存
git commit -m "feat: add login page"
git pull --rebase origin main     # 变基拉取，减少 merge commit
git restore src/a.js              # 丢弃某文件的未暂存改动
git stash && git stash pop        # 临时存取当前改动
git log --oneline -10
```
