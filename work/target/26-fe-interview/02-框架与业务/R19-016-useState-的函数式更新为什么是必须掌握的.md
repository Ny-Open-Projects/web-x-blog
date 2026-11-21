---
title: [R19-016] useState 的函数式更新为什么是必须掌握的写法？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-016：useState 的函数式更新为什么是必须掌握的写法？
**答**：
- setState 传入函数时，React 把"当前最新值"作为参数传入，天然规避批处理导致的陈旧值问题。
- 同一事件里连续多次 setState 时，直接写 `setCount(count + 1)` 三次只会加 1。
- 函数式更新必须是纯函数，React 在 StrictMode 下可能调用两次来帮助暴露副作用。
- 如果新 state 依赖前 state，一律使用函数式更新。

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => setCount((prev) => prev + 1);

  const incrementThree = () => {
    // 三次函数式更新都会生效，结果为 3
    increment();
    increment();
    increment();
  };

  return (
    <>
      <button onClick={incrementThree}>加三</button>
      <p>{count}</p>
    </>
  );
}
```
