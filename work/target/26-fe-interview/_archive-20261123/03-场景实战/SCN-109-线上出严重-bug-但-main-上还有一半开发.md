---
title: [SCN-109] 线上出严重 bug，但 main 上还有一半开发完的未发布功能，hotfix 流程怎么走？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-109：线上出严重 bug，但 main 上还有一半开发完的未发布功能，hotfix 流程怎么走？
**答**：
- 正确姿势：从"线上正在运行的 release tag"拉 hotfix 分支修复并单独发版，未完成功能不受影响；前提是发布物来自 release 分支/tag 而非 main HEAD。
- 若平时就直接从 main 发布，则用 revert 法或 Feature Flag 关闭半成品功能。
- 最易漏的一步：hotfix 必须回合 main，否则下个版本会把补丁丢掉。

```bash
# hotfix 流程：基于上个发布 tag 修复，修完双回合
git fetch --tags
git checkout -b hotfix/login-crash v2.3.0     # 1. 基于线上运行的 tag
# ... 修复并补测试 ...
git commit -am "fix: guard null user on login page"
git tag v2.3.1 && git push origin v2.3.1      # 2. 单独发版，不含 main 半成品

# 3. 回合 main：防止下个版本丢补丁（最容易漏的一步）
git checkout main && git cherry-pick v2.3.1
git push origin main

# 4. 线上验证错误率回落后关闭事故单，写复盘
```
