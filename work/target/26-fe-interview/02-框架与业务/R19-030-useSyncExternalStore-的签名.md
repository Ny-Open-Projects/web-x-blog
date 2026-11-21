---
title: [R19-030] useSyncExternalStore 的签名和典型用法？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-030：useSyncExternalStore 的签名和典型用法？
**答**：
- 专门订阅 React 之外的数据源（浏览器 API、第三方 store、WebSocket 状态），签名三段：subscribe、getSnapshot、getServerSnapshot。
- subscribe 注册监听并返回取消函数；getSnapshot 必须返回不可变的快照值，值变了 React 才重渲染。
- getServerSnapshot 用于 SSR，返回服务端的初始值，避免 hydration mismatch。
- 相比手写 useEffect 订阅，它保证读取和订阅的原子性，不会出现 tearing（撕裂）。

```jsx
import { useSyncExternalStore } from 'react';

function subscribe(callback) {
  window.addEventListener('online', callback);
  window.addEventListener('offline', callback);
  return () => {
    window.removeEventListener('online', callback);
    window.removeEventListener('offline', callback);
  };
}

export default function NetStatus() {
  const isOnline = useSyncExternalStore(
    subscribe,
    () => navigator.onLine, // 客户端快照
    () => true              // 服务端快照
  );

  return <p>{isOnline ? '在线' : '离线'}</p>;
}
```

---

## 第四章 自定义 Hook 受控非受控与列表 key（R19-031 ~ R19-036）
