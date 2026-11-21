---
title: [R19-070] 手写 usePrevious 与 useUnmountedRef？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-070：手写 usePrevious 与 useUnmountedRef？
**答**：
- usePrevious：ref 在 render 阶段读取、在 effect 阶段写入，写入晚于读取一整个 commit，天然拿到"上一轮值"。
- useUnmountedRef：effect 的 cleanup 是卸载信号，用它翻转标记，异步回调回来前先检查。
- 典型组合场景：请求返回时组件可能已卸载，直接 setState 会产生泄漏警告。
- React 18+ 严格模式下 effect 双执行不影响正确性，因为 cleanup 会同步执行。

```jsx
import { useEffect, useRef, useState } from 'react';

// usePrevious：保存上一轮渲染的值
export function usePrevious(value) {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;   // effect 在 commit 后执行，读到的永远是上一轮
  }, [value]);
  return ref.current;
}

// useUnmountedRef：标记组件是否已卸载
export function useUnmountedRef() {
  const unmountedRef = useRef(false);
  useEffect(() => () => { unmountedRef.current = true; }, []);
  return unmountedRef;
}

// 组合使用
function UserPanel({ userId }) {
  const [user, setUser] = useState(null);
  const prevId = usePrevious(userId);
  const unmountedRef = useUnmountedRef();

  useEffect(() => {
    fetchUser(userId).then(data => {
      if (!unmountedRef.current) setUser(data);   // 卸载后不再 setState
    });
  }, [userId, unmountedRef]);

  return <div>上一轮 id 是 {prevId}，当前是 {user?.name}</div>;
}
```
