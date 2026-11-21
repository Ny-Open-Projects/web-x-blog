---
title: [R19-008] ref 的 cleanup function 是什么？解决什么问题？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-008：ref 的 cleanup function 是什么？解决什么问题？
**答**：
- React 19 允许 ref 回调返回一个清理函数，节点卸载或 ref 变更时 React 会先执行清理。
- 解决了旧版 ref 回调无法表达"卸载逻辑"的问题，之前只能依赖 useEffect 或在回调里重置。
- 注意：ref 回调如果隐式返回了非函数值，React 19 会给出警告，箭头函数误写返回值是常见坑。
- cleanup 执行顺序在新的 ref 回调之前，保证先释放旧资源再挂新的。

```jsx
import { useRef } from 'react';

function VideoPlayer({ src }) {
  const videoRef = useRef(null);

  return (
    <video
      ref={(node) => {
        videoRef.current = node;
        // 返回清理函数：卸载或 ref 更换时调用
        return () => {
          videoRef.current = null;
        };
      }}
      src={src}
    />
  );
}
```
