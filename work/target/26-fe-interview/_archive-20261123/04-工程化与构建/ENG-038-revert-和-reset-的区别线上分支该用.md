---
title: [ENG-038] revert 和 reset 的区别？线上分支该用哪个？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-038：revert 和 reset 的区别？线上分支该用哪个？
**答**：
- revert 生成一条"反向提交"撤销指定提交，历史完整保留，安全可推送，公共分支必用它。
- reset 移动分支指针：--soft 保留改动到暂存区、--mixed 到工作区、--hard 彻底丢弃。
- 已 push 的提交用 reset 强推会破坏协作，属于高危操作。
- 本地未推送的提交想整理，用 reset；线上回滚，用 revert。

```bash
# revert：生成反向提交，适合公共分支
git revert 7a1b2c3
git revert HEAD~2..HEAD   # 批量撤销区间提交

# reset：本地整理未推送提交
git reset --soft HEAD~1   # 改动保留在暂存区
git reset --mixed HEAD~1  # 改动保留在工作区（默认）
git reset --hard HEAD~1   # 彻底丢弃，慎用
```
