---
title: [RBL-324] monorepo 内构建工具包（preset/插件）的发布策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-324：monorepo 内构建工具包的发布策略

**答**:
- 发布模式：workspace 内直接引用（src 引用，改了立即生效）vs 发内部 npm（版本化）——混合模式：preset 发版（稳定面），实验插件 workspace 引用
- 版本纪律：preset 内部包用 fixed 联动版本（一起升，避免兼容矩阵爆炸）；breaking 变更必须走 RFC + 迁移 codemod
- 消费端锁定：业务仓锁 preset minor（自动 patch 升级可接受，minor 需评估）；版本漂移监控（多仓 preset 版本分布）
- 发布流水线：受影响包增量构建 + 发布预检（schema 校验/回归快照）+ changelog 自动生成（changesets）

```text
策略：preset 发版 fixed 联动 / 实验插件 workspace 引用 / 消费端锁 minor
流水线：affected 构建 → 预检 → changesets 发布 → 漂移监控
```
