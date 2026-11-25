---
title: [MFW-009] 笔试：手写 useIsClient 守卫与 NoSSR 包装组件
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-009：笔试：手写 useIsClient 守卫与 NoSSR 包装组件
**答**：不使用 next/dynamic，手写两个工具：`useIsClient()`（服务端渲染恒为 false，客户端 hydrate 后变 true，且不会造成 hydration mismatch 闪烁错误）和 `<NoSSR fallback>`（服务端与首帧渲染 fallback，挂载后渲染 children）。要求处理 StrictMode 双调用、SSR/CSR 输出一致性、卸载后状态清理。

```jsx
'use client';
import { useEffect, useState, useSyncExternalStore } from 'react';

// 方案一：useSyncExternalStore——SSR 快照固定为 false，hydrate 后自动校正
export function useIsClient() {
  const subscribe = (cb) => {
    // hydration 完成后 React 会重读 snapshot，此处订阅 store 变化（可空实现）
    return () => {};
  };
  const getSnapshot = () => true;   // 客户端已挂载
  const getServerSnapshot = () => false; // 服务端渲染时恒为 false
  return useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot);
}

// 方案二：经典 mounted 守卫（面试常写）
export function useMounted() {
  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
    return () => setMounted(false); // 严格模式下 effect 重跑也安全
  }, []);
  return mounted;
}

// NoSSR 包装：服务端 + 首帧渲染 fallback，挂载后切换 children
export function NoSSR({ children, fallback = null }) {
  const isClient = useIsClient();
  return isClient ? children : fallback;
}

// 用法：本地存储 / 时间戳 / 随机值等 SSR 与 CSR 必然不一致的场景
function Timestamp() {
  return <NoSSR fallback={<span>—</span>}>{new Date().toLocaleTimeString()}</NoSSR>;
}

// **评分点**
// 1. getServerSnapshot 固定 false：用 useSyncExternalStore 的服务端快照机制，天然无 hydration mismatch（比 useEffect+setState 方案更优，写出者加分）。
// 2. 首帧客户端渲染必须与服务端 HTML 一致（都渲染 fallback），只在 hydration 后切换。
// 3. 卸载清理/StrictMode 双调用不产生副作用。
// 4. 说明 useIsClient 与 typeof window === 'undefined' 的区别：后者在 hydration 首帧也会为 false 导致客户端首帧就不同——这是常见失分点。
```
