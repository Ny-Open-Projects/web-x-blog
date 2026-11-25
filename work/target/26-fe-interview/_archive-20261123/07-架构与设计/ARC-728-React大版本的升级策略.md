---
title: [ARC-728] React 大版本升级策略
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 面试题, 迁移]
type: 面试题
---

## ARC-728：React 大版本升级

**答**：
- 升级评估先行：官方 codemod 清单 + 生态兼容矩阵（路由/状态库/测试库的 peer 支持）——生态不齐不启动
- 渐进开关策略：React 18 的并发特性是 opt-in（createRoot 才启用）——「先升级依赖后开并发」的两段式：段1 API 兼容迁移（legacy root）、段2 createRoot 切换（并发生效）
- 行为变化的回归面：自动批处理（跨 promise 的 setState 合并）/Suspense 语义——「静默行为变化」靠回归测试集 + 灰度指标
- 升级的时机选择：新版本发布后等 2~3 个 minor（生态适配成熟）——追最新版本的团队是生态小白鼠
- 深水点：升级的「依赖锁定策略」——lockfile 精确锁定升级范围（只升 react 系——其他依赖不动）——一次只动一个变量

```text
React 升级:
  两段式: API 迁移(legacy root) → createRoot(并发生效)
  前置: codemod + 生态兼容矩阵
  回归: 批处理/Suspense 行为变化 → 测试集+灰度
  时机: 发布后等 2~3 minor (生态成熟)
  锁定: lockfile 只升 react 系 (一次一个变量)
```
