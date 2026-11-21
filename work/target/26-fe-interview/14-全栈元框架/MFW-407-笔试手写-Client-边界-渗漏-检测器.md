---
title: [MFW-407] 笔试：手写 'use client' 渗漏检测器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-407：边界渗漏检测
**需求**：实现 `detectLeak(files)`：1) files：`{ path, isClient, imports: string[], exports: string[] }[]`；2) 规则一：无 'use client' 模块从 client 模块 import（RSC 引 client 内部 = 服务端执行客户端代码——序列化断裂）；3) 规则二：client 模块从 server-only 包 import（DB 驱动进浏览器包）；4) 规则三：client→client 传函数 props 的模块对（跨客户端边界不可序列化——父 RSC 传 fn 是合法，client 父传 client 子 fn 也断裂）；5) 输出违规对与建议（边界组件下移/类型改 DTO）。

```javascript
export function detectLeak(files) {
  const byP = new Map(files.map((f) => [f.path, f]))
  const errs = []
  for (const f of files) {
    for (const imp of f.imports) {
      const t = byP.get(imp)
      if (!t) continue                                        // 外部包走规则二单独清单
      if (!f.isClient && t.isClient)
        errs.push({ type: 'RSC_IMPORTS_CLIENT', from: f.path, to: imp,
          fix: '把共享逻辑抽到无端模块，或给目标加 RSC 入口包装' })
      if (f.isClient && t.serverOnly)
        errs.push({ type: 'CLIENT_IMPORTS_SERVER', from: f.path, to: imp,
          fix: '通过 Route Handler/Action 暴露能力' })
    }
  }
  // fn-prop：调用方掌握组件树信息（简化：由框架 build 告警回填）
  return { violations: errs, note: 'fn-props 由编译器告警合并到此报告' }
}
```
**评分点**：
- 三类渗漏全覆盖（RSC←client / client←server / fn-prop 跨界）
- 修复建议带方向（抽无端模块 vs 赽 Action——不是只报错）
- 诚实边界：fn-prop 静态难全查（合并编译器告警——工具互补声明）
