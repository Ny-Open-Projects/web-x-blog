---
title: [ENG-037] cherry-pick 的典型使用场景？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-037：cherry-pick 的典型使用场景？
**答**：
- 把某个具体提交"摘"到另一个分支，最典型是把 bugfix 从 main 摘到 release 分支。
- 产生一个新的提交，内容相同但 hash 不同；带冲突时解决后 --continue。
- -n 只应用改动不自动提交，方便把多个提交内容合并处理。
- 多个提交可以批量摘取：git cherry-pick A^..B。

```bash
# 把 main 上的 bugfix 提交摘到发布分支
git checkout release/1.2
git cherry-pick abc1234

# 冲突解决后继续
git cherry-pick --continue

# 只取改动不自动提交
git cherry-pick -n abc1234
```
