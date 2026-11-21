---
title: [R19-114] Hooks 编写规范与 exhaustive-deps 治理？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-114：Hooks 编写规范与 exhaustive-deps 治理？
**答**：
- 原则：不批量禁用 react-hooks/exhaustive-deps；依赖缺失要么补依赖，要么把回调用 useMemoizedFn 稳定后纳入依赖。
- "只想跑一次"的挂载逻辑，effect 依赖写 [] 且内部不引用响应式值；确实要引用又不想重跑的用 ref 记录初始化标记。
- effect 拆分：一个 effect 只做一件事，依赖列表自然清晰；把"事件"与"响应"分开——用户点击触发的逻辑不要塞进 effect。
- 自定义 hook 必须以 use 开头，否则 lint 失明、规则失效。

```jsx
// exhaustive-deps 治理示例
import { useEffect, useRef, useState } from 'react';
import { useMemoizedFn } from './useMemoizedFn';

function LivePrice({ symbol }) {
  const [price, setPrice] = useState(null);

  // 姿势 1：回调用 useMemoizedFn 稳定引用，纳入依赖也不会导致重连
  const onMessage = useMemoizedFn((msg) => {
    setPrice(msg.data[symbol]);
  });

  useEffect(() => {
    const ws = createSocket();
    ws.on('price', onMessage);
    return () => ws.close();
  }, [onMessage]);        // onMessage 引用稳定，effect 不会反复重连

  // 姿势 2：只想跑一次的逻辑，用 ref 记录而不是骗 lint
  const initializedRef = useRef(false);
  useEffect(() => {
    if (initializedRef.current) return;
    initializedRef.current = true;
    initTracking(symbol);
  }, [symbol]);

  return <div>{price}</div>;
}
```
