---
title: [MFW-007] Server Component 给 Client Component 传 props 有什么限制？怎么绕？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-007：Server Component 给 Client Component 传 props 有什么限制？怎么绕？
**答**：
- 只能传**可序列化**值：字符串/数字/布尔/数组/普通对象/Date/Promise/BigInt；不能传函数（除 Server Action）、class 实例、Symbol、Map/Set（Flight 已支持部分，稳妥做法是转数组）。
- 绕法一：**children 模式**——把 Server Component 写成 Client Component 的 `children`，由服务端渲染好后「塞」进去，绕开序列化。
- 绕法二：**序列化时机前移**——class 实例在服务端先 `toJSON()` 摊平；`Date` 可直传（Flight 支持）。
- 绕法三：把回调改为 **Server Action**（服务端函数引用，客户端可以安全调用）。
- 大对象要谨慎：props 都要走 Flight 序列化进 HTML，几十 KB 的 props 会拖慢 TTFB——优先在服务端裁剪字段。

```jsx
// app/page.tsx（Server）
import Table from './table';
import Toolbar from './toolbar';

export default async function Page() {
  const rows = await db.order.findMany({ take: 100 });
  return (
    <main>
      {/* ✅ children：Server 端渲染好的内容直接穿过 Client 边界 */}
      <Toolbar>
        <h1>订单报表（共 {rows.length} 条）</h1>
      </Toolbar>
      {/* ❌ <Table rows={rows} onSelect={...} /> 回调不能传 */}
      <Table rows={rows.map((r) => ({ id: r.id, amount: r.amount }))} />
    </main>
  );
}
```

```jsx
// app/table.tsx
'use client';
import { useState } from 'react';

export default function Table({ rows }) {
  const [sortKey, setSortKey] = useState('id');
  const sorted = [...rows].sort((a, b) => a[sortKey] - b[sortKey]);
  return (
    <table>
      <thead><tr><th onClick={() => setSortKey('id')}>ID</th><th onClick={() => setSortKey('amount')}>金额</th></tr></thead>
      <tbody>{sorted.map((r) => <tr key={r.id}><td>{r.id}</td><td>{r.amount}</td></tr>)}</tbody>
    </table>
  );
}
```
