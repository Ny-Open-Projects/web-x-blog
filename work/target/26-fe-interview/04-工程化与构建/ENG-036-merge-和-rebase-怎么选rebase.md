---
title: [ENG-036] merge 和 rebase 怎么选？rebase 的黄金法则是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-036：merge 和 rebase 怎么选？rebase 的黄金法则是什么？
**答**：
- merge 保留真实分叉历史，产生合并提交，适合合入主干或公共分支。
- rebase 把自己的提交摘下来重放到目标分支顶端，历史线性干净，适合更新 feature 分支。
- 黄金法则：不要对已经推送到公共分支的提交做 rebase，会打乱他人的历史。
- rebase 冲突时逐个解决，git rebase --continue 继续，--abort 撤销整次操作。

```bash
# merge：保留分叉历史
git checkout feature && git merge main

# rebase：线性历史
git checkout feature && git rebase main

# 冲突解决后继续
git add . && git rebase --continue

# 放弃本次 rebase
git rebase --abort
```
