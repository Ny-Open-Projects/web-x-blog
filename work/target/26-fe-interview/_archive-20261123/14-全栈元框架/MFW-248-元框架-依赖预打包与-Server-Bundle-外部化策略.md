---
title: [MFW-248] Server Bundle 的依赖外部化策略
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-248：Server Bundle 依赖外部化策略

**答**:
- 决策维度：serverExternalPackages（不打包走 node_modules require）vs 全打包（单文件部署）——外部化赢冷启动（少求值代码）与 native 模块兼容（sharp/better-sqlite3 无法打包），打包赢部署简洁（无 node_modules 拷贝）
- 默认建议：native/二进制依赖必外部化（打包必炸）、框架自身外部化（共享实例/热更新语义）、业务代码打包
- 体积监控：server bundle 尺寸进预算（冷启动线性相关）——依赖膨胀告警（新引入 5MB 包进 server bundle）
- 一致性风险：外部化后运行时解析 node_modules——CI 与运行环境依赖树必须一致（frozen-lockfile + 镜像同 lock）

```javascript
// next.config
serverExternalPackages: ['sharp', 'better-sqlite3', '@prisma/client'],
// 判定：native→必外置；框架→外置；业务→打包
// 监控：server chunk 总字节 P95 预算（如 20MB）告警
```
