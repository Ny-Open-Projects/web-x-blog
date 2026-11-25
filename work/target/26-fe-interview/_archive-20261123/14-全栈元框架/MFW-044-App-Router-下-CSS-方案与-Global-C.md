---
title: [MFW-044] App Router 下 CSS 方案怎么选？Global CSS、CSS Modules 与 Tailwind 各怎么用？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-044：App Router 下 CSS 方案怎么选？Global CSS、CSS Modules 与 Tailwind 各怎么用？
**答**：
- Global CSS：任意组件可 import，但**只在根 layout import 一次**最稳（其他位置重复 import 会产生全局副作用）；CSS Modules（`*.module.css`）自动局部作用域，Server/Client Component 都能用。
- Tailwind：App Router 事实标准——无运行时、类名即样式、与 RSC 天然兼容（类名作为普通 props 穿边界无序列化问题）。
- CSS-in-JS（styled-components/emotion）在 RSC 下受限：需要运行时 + 必须在 Client Component，且服务端渲染要额外配置 registry——RSC 项目一般不选。
- 选择建议：后台/工具类用 Tailwind 一把梭；视觉重设计系统用 CSS Modules + design tokens；Global CSS 只留 reset 与主题变量。
- 组件库（如 Radix/shadcn）与 RSC 协作良好：无头逻辑放 client，结构服务端渲染。

```jsx
// app/layout.tsx —— Global CSS 只在根引入
import './globals.css'; // reset + CSS 变量
import styles from './page.module.css';

export default function RootLayout({ children }) {
  return (
    <html>
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
```

```jsx
// app/products/page.module.css —— 局部作用域
.card { border: 1px solid var(--color-border); border-radius: 8px; }
```

```jsx
// app/products/page.tsx —— Server Component 直接用 module 与 tailwind 类
import s from './page.module.css';

export default async function Page() {
  const items = await getProducts();
  return (
    <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {items.map((p) => (
        <li key={p.id} className={s.card}>
          <h3 className="text-lg font-medium">{p.title}</h3>
        </li>
      ))}
    </ul>
  );
}
```
