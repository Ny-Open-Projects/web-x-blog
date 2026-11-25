---
title: [R19-017] useEffect 中操作定时器时如何避免闭包陷阱？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-017：useEffect 中操作定时器时如何避免闭包陷阱？
**答**：
- 空依赖数组的 effect 只运行一次，回调闭包捕获的是首次渲染时的 state 值。
- 在闭包里读 `count` 永远是旧值，这是经典的 stale closure 问题。
- 解决方式一：函数式更新 `setCount((prev) => prev + 1)`。
- 解决方式二：把变量放进依赖数组重建定时器，或用 useRef 保存最新值。

```jsx
function StaleClosureDemo() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      // 错误写法：闭包里的 count 永远是首次渲染的 0
      // setCount(count + 1);

      // 正确写法：基于前值更新
      setCount((prev) => prev + 1);
    }, 1000);

    return () => clearInterval(timer);
  }, []); // 空依赖：只挂载时运行一次

  return <p>{count}</p>;
}
```
