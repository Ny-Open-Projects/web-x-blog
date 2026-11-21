---
title: [R19-099] React.lazy 组件如何做 hover 预取？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-099：React.lazy 组件如何做 hover 预取？
**答**：
- 懒加载的痛点：点击后才发起 chunk 请求，Suspense fallback 闪烁一次。
- 原理：import() 是单例缓存——hover 时提前调用一次 import 触发下载，点击时命中模块缓存立即 resolve。
- 实现：把 import 提成独立函数，绑到 onMouseEnter/onFocus；lazy 的工厂里同样调用，两个入口共享缓存。
- 更进一步：路由级预取在空闲时间（requestIdleCallback）预热高概率跳转的页面。

```jsx
// Nav.tsx —— lazy + hover 预取
import { lazy, Suspense, useState } from 'react';

// 路由级组件默认不加载
const HeavyReport = lazy(() => import('./HeavyReport'));

// 关键技巧：import() 有模块缓存，重复调用只下载一次
function preloadReport() {
  import('./HeavyReport');        // 触发网络加载并写入 module cache
}

function Nav() {
  const [show, setShow] = useState(false);
  return (
    <nav>
      {/* hover 时预取，点击时大概率已就绪，Suspense 无 loading 闪烁 */}
      <button
        onMouseEnter={preloadReport}
        onFocus={preloadReport}
        onClick={() => setShow(true)}
      >
        数据报表
      </button>
      {show && (
        <Suspense fallback={<div>加载中...</div>}>
          <HeavyReport />
        </Suspense>
      )}
    </nav>
  );
}
```
