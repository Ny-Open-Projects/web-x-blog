---
title: [BAS-189] semver 的完整规则是什么？^ 和 ~ 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-189：semver 的完整规则是什么？^ 和 ~ 有什么区别？
**答**：
- 三段式 MAJOR.MINOR.PATCH：不兼容的 API 变更升 MAJOR，向后兼容的新功能升 MINOR，向后兼容的修 bug 升 PATCH。
- ^1.2.3 允许升到 <2.0.0（锁 MAJOR）；~1.2.3 只允许 <1.3.0（锁 MINOR）。
- 特殊陷阱：0.x 阶段不稳定，^0.2.3 只允许 <0.3.0（等价锁 MINOR），所以依赖 0.x 包时锁得非常死。

```bash
# MAJOR.MINOR.PATCH
# MAJOR 不兼容改动 / MINOR 向后兼容新功能 / PATCH 向后兼容修 bug
^1.2.3   # 允许 1.2.3 到 <2.0.0，锁定 MAJOR
~1.2.3   # 允许 1.2.3 到 <1.3.0，锁定 MINOR
^0.2.3   # 0.x 阶段：只允许到 <0.3.0，等价锁 MINOR
1.x      # 通配：任意 1.y.z
```
