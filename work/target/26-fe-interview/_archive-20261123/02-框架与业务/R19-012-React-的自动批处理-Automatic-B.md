---
title: [R19-012] React 的自动批处理 Automatic Batching 是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-012：React 的自动批处理 Automatic Batching 是什么？
**答**：
- React 18 起，同一个事件回调、Promise、setTimeout、原生事件里的多次 setState 会合并为一次重渲染。
- React 16 只在事件处理器内批处理，异步上下文里每次 setState 都触发一次渲染。
- 想强制立即提交 DOM 可以用 `flushSync`（刻意逃逸批处理）。
- 批处理只影响渲染次数，不影响最终 state 正确性，函数式更新始终按顺序执行。

```jsx
import { flushSync } from 'react-dom';

function Profile() {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);

  function handleClick() {
    // 多个 setState 合并为一次渲染
    setName('Wang');
    setAge(18);
    // Promise 等异步上下文同样自动批处理
    fetch('/api/log').then(() => {
      setName('Li');
      setAge(20);
    });
    // 需要在下次 DOM 读取前强制同步提交时才用 flushSync
    flushSync(() => setAge(19));
  }

  return (
    <p onClick={handleClick}>
      {name} {age}
    </p>
  );
}
```
