---
title: [RBL-235] monorepo 增量发布的版本联动怎么编排
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-235：monorepo 增量发布的版本联动怎么编排

**答**:
- 联动规则：包 B 依赖包 A，A 发版 → B 需要重发（内部依赖版本更新）；affected + 依赖闭包决定发布集
- 版本策略：fixed（统一版本号，简单但全量发）/ independent（独立版本，精确但联动复杂）；changesets 是主流实践（变更集驱动的版本与 changelog）
- 发布流水线：CI 检测 changeset → version PR（批量升级版本与 changelog）→ 合并后按依赖拓扑序发布（构建缓存加持下分钟级）
- 私有包：不发布的内部包不发版但参与 affected 计算——发布图与构建图是两张相关联的图

```text
changesets 流程：PR 带 changeset → merge → CI version PR → merge → 拓扑序 publish（仅受影响包）
```
