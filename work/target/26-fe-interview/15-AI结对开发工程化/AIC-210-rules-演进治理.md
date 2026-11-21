---
title: [AIC-210] rules 库随团队发展会腐化，你如何设计 rules 的生命周期治理（新增/废弃/合并）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-210：rules 库随团队发展会腐化，你如何设计 rules 的生命周期治理（新增/废弃/合并）？
**答**：
- 入库即建档：记录动机（关联 PR/事故）、生效范围、负责人、创建日期。
- 定期巡检：季度跑一次评测集，通过率无提升或负提升的规则进入废弃流程。
- 合并同类：主题相近的规则合并，规则数控制上限（如 30 条）。
- 废弃不是删除：归档到 rules/archive 保留历史，方便回溯。

```javascript
# rule-metadata 示例（rules/base.mdc 的 front-matter 扩展字段）
# owner: fe-platform
# created: 2026-03-01
# motivation: PR#1243 硬编码色值导致暗色模式回归
# last-eval: 2026-10-15 passRate +14%
# status: active   # active | deprecated
globs: ["src/**/*.tsx"]
r
```
