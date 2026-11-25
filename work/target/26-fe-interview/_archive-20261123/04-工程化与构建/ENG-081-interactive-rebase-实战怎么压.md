---
title: [ENG-081] interactive rebase 实战：怎么压缩提交、修改历史？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-081：interactive rebase 实战：怎么压缩提交、修改历史？
**答**：
- git rebase -i HEAD~N 打开待办清单：pick 保留、squash/s 合并进上一个、reword 改信息、drop 丢弃。
- 典型场景：功能分支上的 WIP、fixup 提交在合并前压成一个干净提交。
- 改的是分支上未推送的提交；如果必须改已推送的私有分支，force push 要加 --force-with-lease。
- 出问题先 git rebase --abort 整体撤销；rebase 前记录一次 ORIG_HEAD/reflog 可找回。

```bash
# 把最近 3 个提交压缩成一个
git rebase -i HEAD~3
# 编辑器中的待办清单，第一个保持 pick，其余改 squash：
#   pick a1b2c3 feat: 登录页
#   squash d4e5f6 fix: 修正样式
#   squash f7g8h9 chore: 调整依赖

# 更省事的写法：最后一个提交直接并入前一个
git commit --amend --no-edit

# 中途出错：整体撤销回到 rebase 前
git rebase --abort

# 解决冲突后继续变基
git add -A && git rebase --continue

# 必须覆盖已推送的私有分支时，用安全强推
git push --force-with-lease
```
