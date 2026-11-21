---
title: [R19-143] 并发渲染会带来哪些 effect 竞态问题？怎么系统性修复？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-143：并发渲染会带来哪些 effect 竞态问题？怎么系统性修复？
**答**：
- 竞态三源：StrictMode 双执行、并发可中断渲染导致的重复挂载、快速输入/路由切换导致的"慢请求后到"。
- 通用修复三板斧：cleanup 里取消（AbortController / 清定时器）、用忽略标志丢弃过期响应、依赖数组收紧并配合 `useRef` 保存最新闭包。
- 判断标准：effect 里的异步回调"回来的时候"，组件可能已经卸载或已经因新参数重新运行——每一处异步都要问这个问题。
- React 18+ 不再警告"卸载后 setState"，防泄漏的责任完全交给 cleanup。

```jsx
// RaceFix.jsx —— effect 竞态的系统性修复模式
import { useEffect, useRef, useState } from 'react';

// 模式一：AbortController —— 从源头取消过期请求（首选）
export function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    setUser(null);
    setError(null);

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then(r => r.json())
      .then(data => setUser(data))
      .catch(err => {
        if (err.name !== 'AbortError') setError(err); // 取消不算错误
      });

    return () => controller.abort(); // userId 变化/卸载时取消上一个请求
  }, [userId]);

  if (error) return <p>加载失败</p>;
  if (!user) return <p>加载中...</p>;
  return <h1>{user.name}</h1>;
}

// 模式二：忽略标志 —— 无法取消的场景（第三方库、WebSocket 回调）
export function LivePrice({ symbol }) {
  const [price, setPrice] = useState(null);
  const ignoreRef = useRef(false); // useRef 存标志，不影响渲染

  useEffect(() => {
    ignoreRef.current = false;
    subscribe(symbol, p => {
      if (!ignoreRef.current) setPrice(p); // 过期订阅直接丢弃
    });
    return () => {
      ignoreRef.current = true;            // 清理时置位，之后的回调全部忽略
    };
  }, [symbol]);

  return <span>{price ?? '-'}</span>;
}

// 模式三：防抖 + 最新闭包 —— 搜索框类输入竞态
export function useDebouncedSearch(search) {
  const [results, setResults] = useState([]);
  const latestRef = useRef(search);

  useEffect(() => {
    latestRef.current = search;
    const id = setTimeout(async () => {
      const data = await fetch(`/api/search?q=${encodeURIComponent(search)}`).then(r => r.json());
      if (latestRef.current === search) setResults(data); // 只接受最新关键字的响应
    }, 300);
    return () => clearTimeout(id); // 每次新输入清掉上一个定时器
  }, [search]);

  return results;
}
```

## 第二十一章 数据层工程（R19-144 ~ R19-150）
