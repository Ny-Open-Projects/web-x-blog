---
title: [R19-010] Server Components 与 Client Components 的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-010：Server Components 与 Client Components 的区别？
**答**：
- Server Components 默认只在服务端运行：可以 async、直接访问数据库和文件系统、产物不进客户端 bundle。
- 需要 useState、useEffect、事件监听的组件必须 `'use client'` 声明为 Client Components。
- 两者可以组合：Client 组件可以作为 props（children）接收 Server 组件渲染的静态内容。
- Server Components 传给 Client Components 的 props 必须可序列化，函数（除 Server Action）不能传递。

```jsx
// 默认是 Server Component：支持 async，直接查库，不进客户端 bundle
async function UserList() {
  const users = await db.user.findMany();
  return <ul>{users.map((u) => <li key={u.id}>{u.name}</li>)}</ul>;
}

// 'use client' 声明 Client Component：拥有状态与事件能力
'use client';
import { useState } from 'react';

function Counter() {
  const [n, setN] = useState(0);
  return <button onClick={() => setN(n + 1)}>{n}</button>;
}

// 组合：把 Server 组件作为 children 传给 Client 布局
export default function Page() {
  return (
    <Panel>
      <UserList />
      <Counter />
    </Panel>
  );
}
```

---

## 第二章 JSX 本质与函数组件（R19-011 ~ R19-015）
