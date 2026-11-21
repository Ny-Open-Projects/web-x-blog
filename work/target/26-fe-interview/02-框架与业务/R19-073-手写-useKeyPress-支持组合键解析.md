---
title: [R19-073] 手写 useKeyPress 支持组合键解析？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-073：手写 useKeyPress 支持组合键解析？
**答**：
- 组合键用字符串声明如 `ctrl.shift.s`，解析时把修饰键与主键统一小写排序后比对，顺序无关。
- Mac 上 Ctrl 与 Meta（Command）通常视为等价，用 `e.ctrlKey || e.metaKey` 归一。
- handler 同样走 useLatest，避免每次按键判定都拿到旧闭包。
- preventDefault 必须在业务回调里主动调用，浏览器默认行为（如 Ctrl+S 存网页）才会被拦住。

```jsx
// useKeyPress：解析组合键，如 ctrl.shift.s
import { useEffect, useRef } from 'react';

const normalize = (combo) => combo.toLowerCase().split('.').sort().join('.');

export function useKeyPress(keyFilter, handler) {
  const handlerRef = useRef(handler);
  handlerRef.current = handler;

  useEffect(() => {
    const onKeyDown = (e) => {
      const parts = [];
      if (e.ctrlKey || e.metaKey) parts.push('ctrl');
      if (e.shiftKey) parts.push('shift');
      if (e.altKey) parts.push('alt');
      parts.push(e.key.toLowerCase());
      const combo = parts.sort().join('.');

      const filter = typeof keyFilter === 'string' ? normalize(keyFilter) : keyFilter;
      const matched = typeof filter === 'string' ? filter === combo : filter(e);
      if (matched) handlerRef.current(e);
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [keyFilter]);
}

// 用法：保存快捷键
// useKeyPress('ctrl.s', e => { e.preventDefault(); save(); });
```
