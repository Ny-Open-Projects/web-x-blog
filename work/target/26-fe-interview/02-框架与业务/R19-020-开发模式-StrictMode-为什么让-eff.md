---
title: [R19-020] 开发模式 StrictMode 为什么让 effect 执行两次？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-020：开发模式 StrictMode 为什么让 effect 执行两次？
**答**：
- StrictMode 在开发环境故意 mount -> unmount -> remount 一次组件，模拟快速切换场景。
- 目的是提前暴露没有正确清理的副作用，例如忘记取消订阅、忘记清定时器。
- 这只发生在开发模式，生产构建不会双重执行。
- 正确编写的 effect（幂等 + 完整清理）在双重执行下表现不变，这就是 React 想验证的。

```jsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

function EffectProbe() {
  useEffect(() => {
    console.log('副作用执行');
    return () => console.log('清理执行');
    // 控制台会依次出现：副作用执行 清理执行 副作用执行
  }, []);

  return <p>观察控制台</p>;
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <EffectProbe />
  </StrictMode>
);
```
