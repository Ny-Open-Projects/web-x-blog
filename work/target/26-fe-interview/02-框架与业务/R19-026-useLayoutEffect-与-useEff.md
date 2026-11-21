---
title: [R19-026] useLayoutEffect 与 useEffect 的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-026：useLayoutEffect 与 useEffect 的区别？
**答**：
- useEffect 异步执行：在浏览器绘制之后运行，不阻塞渲染。
- useLayoutEffect 同步执行：在 DOM 变更后、浏览器绘制前运行，适合测量 DOM 并立即修改布局。
- 用它测量再 setState 可以避免"先画错再修正"的闪烁，代价是阻塞绘制，滥用会拖慢首屏。
- SSR 环境下 useLayoutEffect 会告警，服务端无法执行 DOM 测量。

```jsx
function Tooltip({ text }) {
  const ref = useRef(null);
  const [top, setTop] = useState(0);

  useLayoutEffect(() => {
    // 绘制前测量高度并修正位置，用户看不到跳动
    const rect = ref.current.getBoundingClientRect();
    setTop(window.innerHeight / 2 - rect.height / 2);
  }, [text]);

  return (
    <div ref={ref} style={{ position: 'fixed', top }}>
      {text}
    </div>
  );
}
```
