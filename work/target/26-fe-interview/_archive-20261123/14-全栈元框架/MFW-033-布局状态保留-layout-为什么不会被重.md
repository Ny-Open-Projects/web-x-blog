---
title: [MFW-033] App Router 导航时为什么 layout 状态不会丢失？template 和 layout 区别？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-033：App Router 导航时为什么 layout 状态不会丢失？template 和 layout 区别？
**答**：
- 导航只替换**变化的路由段**：从 /blog/a 到 /blog/b，root layout 与 blog layout 不重新渲染（组件实例保留、state/动画/输入焦点不丢），只有 page 换新——这是嵌套路由段模型的红利。
- `template.tsx` 与 layout 唯一区别：**每次导航都创建新实例**（不保留状态）——适合「页面进入动画」（每页重新触发 transition）。
- 相关文件族：layout（持久壳）、template（每次重建）、loading（挂起骨架）、error（错误边界，'use client'）、not-found、page（路由终点）。
- 跨页面共享状态要放在 layout 或全局 Provider（'use client' 的 store 在 layout 里，导航不卸载）。
- 注意：同一层级的兄弟路由切换（/a→/b）会卸载 page；layout 只有当**其子段变化但自身仍在路径上**时才保留。

```jsx
// app/blog/layout.tsx —— 跨 page 持久：导航不重渲染，state 保留
'use client';
import { useState } from 'react';

export default function BlogLayout({ children }) {
  const [keyword, setKeyword] = useState('');
  return (
    <>
      <input
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)} // 从 /blog/a 切到 /blog/b 输入框内容不丢
        placeholder="搜索文章…"
      />
      {children}
    </>
  );
}
```

```jsx
// app/blog/template.tsx —— 每次导航重建实例：进入动画每次都播
'use client';
import { motion } from 'framer-motion';

export default function Template({ children }) {
  return (
    <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}>
      {children}
    </motion.div>
  );
}
```
