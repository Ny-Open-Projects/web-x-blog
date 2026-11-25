---
title: [MFW-231] App Router 性能反模式清单（高频踩坑）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-231：App Router 性能反模式清单

**答**:
- 七大反模式：①把整页标 'use client'（放弃 RSC 收益）②RSC 内 await 串行瀑布（该 Promise.all 并行）③未用 Suspense 分段（慢数据阻塞整树流式）④layout 顶层做重 DB 查询（每页都跑）⑤ huge client bundle 进首屏（第三方库应懒加载）⑥middleware 里做 DB 查询（毫秒预算内塞重活）⑦滥用 router.refresh() 全树刷新（应精准 revalidateTag）
- 定位方法：TTFB 分解（RSC payload 大小/DB 时间）、React DevTools Profiler 找 client 边界过大、next build 输出的 First Load JS 预算
- 修复优先级：串行→并行（零风险）> Suspense 分段 > 边界收缩（client 下沉）> 缓存策略修正

```text
自查清单：
□ 有无整页 'use client'？      □ RSC 是否 Promise.all？
□ 慢段有无 Suspense？          □ layout 是否轻？
□ First Load JS 预算？         □ middleware <10ms？
□ 失效用 tag 还是 refresh()？
```
