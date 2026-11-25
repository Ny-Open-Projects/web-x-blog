---
title: [ARC-025] 什么是幽灵依赖？pnpm 如何从机制上治理它？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-025：什么是幽灵依赖？pnpm 如何从机制上治理它？
**答**：
- 幽灵依赖：代码 import 了"没有声明在 package.json 里"的包，只是因为 npm/yarn 扁平化 hoist 到根 node_modules 才碰巧能用。
- 危害：上游某天不再传递依赖它，构建直接崩；版本也不受你控制。
- pnpm 默认符号链接结构让未声明依赖不可见，从机制上修复，而不是靠 lint 提醒。

```ini
# .npmrc —— pnpm 幽灵依赖治理配置
hoist=false                     # 关键：不把依赖偷偷提升到根，未声明的包 import 不到了
shallow-install=false
strict-peer-dependencies=true   # peer 依赖缺失直接报错，避免版本错配上线
auto-install-peers=true
# 配合命令检查：pnpm dlx depcheck  扫出"用了但没声明"的包
```
