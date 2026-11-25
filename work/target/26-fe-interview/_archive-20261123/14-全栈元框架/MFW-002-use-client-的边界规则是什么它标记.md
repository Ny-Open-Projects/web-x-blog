---
title: [MFW-002] 'use client' 的边界规则是什么？它标记的是入口还是整个子树？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-002：'use client' 的边界规则是什么？它标记的是入口还是整个子树？
**答**：
- `'use client'` 是**边界入口声明**：从该文件开始，它 import 的**整个子树**都进入客户端图——子文件不需要重复声明。
- 反向不成立：Client Component 里 import 一个 Server Component 是**不允许**的（Client 无法引用 Server 代码）；要把 Server Component 当 children/props 从上层「穿」进 Client Component。
- 默认 everything-in-server：**不写 `'use client'` 的文件都是 Server Component**，所以边界应该尽量下推（只在叶子交互组件声明），让上面的布局、数据获取留在服务端。
- 判断要不要 `'use client'`：用到 useState/useEffect/事件监听/浏览器 API/第三方只跑在浏览器的库——任一命中才声明。
- 追问钩子：'use client' 不等于「只渲染在客户端」——Client Component 依然会在服务端做 SSR 首屏，只是之后要 hydration。

```jsx
// app/layout.tsx（Server，无需声明）
import ClientNav from './client-nav';
import Analytics from './analytics';

export default function Layout({ children }) {
  return (
    <html>
      <body>
        <ClientNav>
          {/* Server Component 作为 children 从服务端传入 Client 子树 */}
          {children}
        </ClientNav>
        <Analytics />
      </body>
    </html>
  );
}
```

```jsx
// app/client-nav.tsx —— 边界入口
'use client';
import NavItem from './nav-item'; // 子文件自动进入 client 图，无需再写 'use client'

export default function ClientNav({ children }) {
  return <nav>{NavItem({ label: '首页' })}{children}</nav>;
}

// ❌ 错误示范：在 Client 文件里 import 服务端能力
// import { db } from '@/lib/db';  // 打包报错：db 不能进入浏览器
```
