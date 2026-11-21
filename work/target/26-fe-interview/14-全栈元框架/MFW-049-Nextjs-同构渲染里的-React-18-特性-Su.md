---
title: [MFW-049] React 18 的并发特性在 Next.js 元框架里怎么被使用？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-049：React 18 的并发特性在 Next.js 元框架里怎么被使用？
**答**：
- **Suspense/流式**：并发渲染的招牌——服务端按边界流式下发，客户端 useTransition 把降级变非阻塞，Next 把两者串成了完整链路。
- **useTransition / useDeferredValue**：客户端导航时 React 保持旧页面可交互、新页面后台准备——App Router 导航「不白屏」的机制之一。
- **自动批处理**：事件、timeout、Promise 回调里的多次 setState 合并渲染；Server Action 返回后的更新同样批处理。
- **useSyncExternalStore**：第三方 store 接入同构渲染的正确姿势（SSR 快照机制），client store 与 RSC 共存的基础。
- 元框架视角：React 提供「可中断、可挂起」的渲染原语，Next 负责「服务端数据流、缓存、路由」把它们落到实处。

```jsx
'use client';
import { useTransition, useDeferredValue, useState } from 'react';

function ProductSearch({ initial }) {
  const [keyword, setKeyword] = useState(initial);
  const [isPending, startTransition] = useTransition();
  const deferred = useDeferredValue(keyword); // 输入不被搜索结果拖慢

  function onChange(e) {
    const v = e.target.value;
    setKeyword(v);                              // 立即更新输入框（高优先级）
    startTransition(() => {
      // router.push 触发的 RSC 拉取是可中断的 transition 更新：
      // 新页面数据没到之前，旧页面保持可交互
      window.__router.push(`/search?q=${encodeURIComponent(v)}`);
    });
  }

  return (
    <>
      <input value={keyword} onChange={onChange} />
      {isPending && <span>搜索中…</span>}
      <ResultList keyword={deferred} />
    </>
  );
}
```
