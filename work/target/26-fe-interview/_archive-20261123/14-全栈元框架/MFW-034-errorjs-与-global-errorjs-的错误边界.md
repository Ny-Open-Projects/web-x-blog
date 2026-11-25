---
title: [MFW-034] error.js 的错误边界机制是什么？和 global-error.js 怎么分工？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-034：error.js 的错误边界机制是什么？和 global-error.js 怎么分工？
**答**：
- `error.js` 自动包成**路由段的 Error Boundary**（'use client' 强制）：渲染/数据获取抛错时，只替换该段内容为降级 UI，兄弟段和父级 layout 不受影响。
- 接收两个 prop：`error`（错误对象，生产环境被脱敏，只有 digest）与 `reset()`（重置边界、重试渲染——服务端重新执行该段）。
- `global-error.js` 是**根级兜底**：替换整个 `<html>`（必须自己写 html/body 标签），处理 layout 也炸了的极端情况；生产上报错误时先看 digest 对照服务端日志。
- 注意分工：error.js 捕获子段的渲染错误，**不捕获事件回调里的错误**（那是普通 try/catch 的活）也不捕获 async 的 Server Action 错误（要用 useActionState 处理）。
- 配套：`not-found.js` 处理 notFound() 主动抛出的 404；未命中路由的 404 也走它。

```jsx
// app/products/error.tsx
'use client';
export default function Error({ error, reset }) {
  return (
    <div>
      <h2>商品加载失败</h2>
      {/* 生产环境 error.message 为脱敏信息，digest 用于日志检索 */}
      <p>错误码：{error.digest}</p>
      <button onClick={() => reset()}>重试</button>
    </div>
  );
}
```

```jsx
// app/global-error.tsx —— 根级兜底，替换整个文档
'use client';
export default function GlobalError({ error, reset }) {
  return (
    <html lang="zh">
      <body style={{ fontFamily: 'sans-serif', textAlign: 'center' }}>
        <h1>应用出错了</h1>
        <button onClick={() => reset()}>刷新重试</button>
      </body>
    </html>
  );
}
```

```jsx
// app/products/page.tsx —— 分段隔离：一个组件挂了不影响另一个
import { Suspense } from 'react';
export default async function Page() {
  return (
    <>
      <Suspense fallback={<p>加载榜单…</p>}>
        <Ranking /> {/* 内部抛错只影响此边界 */}
      </Suspense>
      <Ads /> {/* 仍然正常渲染 */}
    </>
  );
}
```
