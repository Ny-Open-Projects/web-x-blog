---
title: [R19-023] useRef 的两大用途分别是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-023：useRef 的两大用途分别是什么？
**答**：
- 用途一：挂载 DOM 或组件实例，配合 ref prop 获取节点做聚焦、测量、播放控制等命令式操作。
- 用途二：跨渲染保存可变值（定时器 id、上一次的值、是否已初始化），修改 current 不触发重渲染。
- 不要在渲染期间读写 ref.current 参与渲染逻辑，那会让渲染结果不可预测。
- 与 useState 的核心区别：ref 变化不触发渲染，state 变化触发渲染。

```jsx
function Stopwatch() {
  const inputRef = useRef(null);  // 用途一：拿 DOM
  const timerIdRef = useRef(0);   // 用途二：存定时器 id
  const [elapsed, setElapsed] = useState(0);

  const start = () => {
    timerIdRef.current = setInterval(() => setElapsed((s) => s + 1), 1000);
    inputRef.current?.focus();
  };

  const stop = () => {
    clearInterval(timerIdRef.current); // 改 ref 不触发重渲染
  };

  return (
    <>
      <input ref={inputRef} />
      <p>{elapsed}s</p>
      <button onClick={start}>开始</button>
      <button onClick={stop}>停止</button>
    </>
  );
}
```
