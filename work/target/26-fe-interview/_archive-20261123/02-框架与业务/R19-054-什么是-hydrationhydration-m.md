---
title: [R19-054] 什么是 hydration？hydration mismatch 怎么来的？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-054：什么是 hydration？hydration mismatch 怎么来的？
**答**：
- hydration 是客户端 React "接管"服务端返回的 HTML 的过程：比对结构并绑定事件与状态。
- 服务端与客户端渲染结果不一致就会产生 hydration mismatch，React 19 会直接报错并回退客户端渲染。
- 常见原因：随机数、Date.now、window 判断、locale 相关的格式化直接出现在首帧渲染里。
- 解决：把仅客户端的值放进 useEffect 里更新，或用 useId 保证 id 一致。

```jsx
'use client';

import { useEffect, useState } from 'react';

export default function Clock() {
  const [now, setNow] = useState(null);

  useEffect(() => {
    // 只在客户端更新，服务端首帧输出占位，避免 mismatch
    setNow(Date.now());
  }, []);

  // 错误示例：初始 state 直接写 new Date().toLocaleTimeString()
  // 服务端和客户端时间不同，必然 hydration mismatch
  return <p>{now ? new Date(now).toLocaleTimeString() : '--'}</p>;
}
```
