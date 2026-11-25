---
title: [MFW-613] Server Components 的 Tree Shaking：跨边界摇树的边界
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-613：RSC 的跨边界 Tree Shaking

**答**:
- RSC 的双 bundle 摇树：server bundle（server 组件 + 数据层）与 client bundle（client 组件）**分别摇树**——同一模块在两 bundle 的使用面不同（server 只用 fetchData、client 只用 UI 渲染——模块按边界拆分摇树）。
- 边界的摇树陷阱：1) **'use client' 的导出面**（client 组件 export 的所有东西都进 client bundle——server-only 的 helper 放 client 组件文件 = 泄漏 RBL-780）；2) **共享模块的分裂**（utils.ts 被 server+client 都 import → 两份编译（可能两份代码——sideEffect 的处理））；3) **barrel 文件的摇树失效**（index.ts re-export 全家桶——跨边界 barrel = 双 bundle 都打全 RBL-594 的边界版）。
- 优化：server-only/client-only 包（显式边界标记——import 错误即抛）；「模块的环境归一」（utils 拆 server/client 两文件）。
- 追问钩子：为什么「barrel 文件」在 RSC 双 bundle 下比单 bundle 更伤？——单 bundle：摇树至少还有 sideEffects 标记兜底；双 bundle：server bundle 摇掉 client 部分、client bundle 摇掉 server 部分——但 barrel 的 re-export 让「两个 bundle 都解析全模块」——parse 成本 ×2 + sideEffect 探测 ×2；且 server 部分（db 连接）漏进 client bundle 的风险 ↑（barrel 逃逸 RBL-780 的摇树维度）；「边界与摇树的交互」：拆 barrel = 拆摇树边界（子路径 import RBL-602 的封装语义）。

```typescript
// 反模式：barrel 跨边界
// index.ts: export * from './db'; export * from './ui';  ← 双 bundle 都打全
// 修正：环境归一
// server.ts: export * from './db'      → server-only
// client.tsx: export * from './ui'     → 'use client'
// server 组件：import { getProduct } from '@org/db/server'   ← 子路径直引
// 'use client' 组件：import { Button } from '@org/ui/client'
// 构建器验证：client bundle 内不得出现 db 模块（RBL-780）
const auditClientBundle = (bundleModules: string[]) =>
  bundleModules.filter(m => /\/db\.|prisma|server-only/.test(m))
    .map(m => `client bundle 泄漏: ${m}`);
```
