---
title: [MFW-664] 产物审计：Forbidden API 扫描
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-664：Forbidden API 扫描

**答**:
- server bundle 的禁止 API：1) **client bundle 禁止 Node API**（fs/net/process——client 运行时不存在：引用 = 运行时崩溃 RBL-780）；2) **server bundle 禁止 browser API**（window/document——RSC 渲染环境无 DOM RBL-914）；3) **edge 运行时禁止**（Node 完整 API——RBL-787 支持表）；「per-运行时的 API 白名单」是 forbidden 扫描的依据。
- 扫描的实现：产物扫描（bundle 内的 API 引用 AST/字符串匹配——压缩后仍可识别（全局引用 RBL-762 的安全扫描模式））；「编译器内建 vs 独立审计」（Next 内建部分检查 + 独立扫描兜底——两层）。
- 误报的处理：polyfill 引用（条件 polyfill——typeof fs === 'undefined' 守卫的合法引用——扫描器的守卫识别）；动态引用（间接调用——扫描不到：诚实标注局限）。
- 追问钩子：为什么「Forbidden API 扫描」要在产物层做而不是源码 lint？——源码 lint 只看「显式引用」（import fs from 'fs'）；产物层的引用包括「依赖间接引入」（依赖包用了 fs——源码看不到）；产物 = 运行时的真实 API 面（RBL-762 产物审计的 API 维度）：依赖的间接 API 引用只有产物扫描才能发现。

```typescript
// Forbidden API 扫描器（产物层）
const FORBIDDEN = {
  client: ['require("fs")', 'require("net")', 'process.binding', '__dirname',
    'window.', 'document.', 'localStorage.'],
  server: ['window.', 'document.', 'localStorage.', 'navigator.'],
  edge: ['require("fs")', 'child_process', 'fs.writeFileSync'],
};
function scanForbidden(bundles: { name: string, target: 'client' | 'server' | 'edge', code: string }[]) {
  const findings = [];
  for (const b of bundles) {
    for (const api of FORBIDDEN[b.target] ?? []) {
      if (b.code.includes(api)) {
        // 守卫识别：typeof 检查的合法引用
        const guarded = b.code.includes(`typeof ${api.split('.')[0]} === 'undefined'`);
        findings.push({ bundle: b.name, api,
          severity: guarded ? 'warn-guarded' : 'error' });
      }
    }
  }
  return findings.filter(f => f.severity === 'error');   // 仅 error 阻断；guarded 告警
}
// client bundle 的 Node API 引用 = 运行时崩溃（client 无 fs）
// server bundle 的 window 引用 = SSR 崩溃（无 DOM）
```
