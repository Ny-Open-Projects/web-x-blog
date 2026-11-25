---
title: [WCN-624] 在 Next.js App Router 中集成 Web Components 有哪些水合（hydration）坑？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-624：在 Next.js App Router 中集成 Web Components 有哪些水合（hydration）坑？

**答**：
- 结论：核心矛盾是「WC 在客户端自定义元素升级」与「RSC 服务端只输出 HTML」的时序差——服务端打印的 shadow 内容到客户端会被重新处理导致不一致。
- 做法：用 DSD（Declarative Shadow DOM）让服务端输出 shadow 结构；客户端组件中用 useEffect 后再操作 DOM；WC 注册用动态 import 且 ssr:false。
- 追问钩子：为什么不能直接 'use client' 了事？因为 use client 组件仍会在服务端预渲染，首次 HTML 与客户端 WC 升级后的 DOM 不同仍会告警——考察对 RSC 模型的理解。

```javascript
// app/page.tsx (Server Component) 输出 DSD 标记
export default function Page() {
  return (
    <ds-goods name="商品A">
      <template shadowrootmode="open">
        <style>{'.name{font-weight:bold}'}</style>
        <div class="name">商品A</div>
      </template>
    </ds-goods>
  );
}
// 客户端注册（client-only，避免 SSR 期访问 window）
'use client';
useEffect(() => { import('@/components/ds-goods'); }, []);
// 服务端 HTML 已含 shadow 结构，客户端 connect 时不重建 DOM → 无水合告警
```
