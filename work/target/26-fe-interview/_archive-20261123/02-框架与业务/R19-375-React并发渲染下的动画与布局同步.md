---
title: [R19-375] React 并发渲染下的动画与布局同步
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-375：React 并发渲染下的动画与布局同步

**答**：
- 布局读取时机：useLayoutEffect 在 commit 内同步读——并发渲染下 commit 仍是同步原子，布局读取安全；useEffect 异步（下一宏任务）布局可能已变
- 动画驱动模式：状态驱动动画（CSS transition 由 class 切换）优于 JS 驱动（rAF 里 setState 会走完整渲染）——React 并发下「每帧 setState」是反模式（即使低优先级也产生渲染队列）
- rAF 与 React 的结合：动画值放外部系统（WAAPI/ref 直接操作 DOM），React 只管「动画结束」的状态同步——view transition API 的 React 集成（React 19 的 experimental）
- flushSync 的布局读：需要「DOM 更新后立刻测量」的拖拽场景用 flushSync 包 setState——同步 commit 后立刻读布局
- React 19 的 useAnimationFrame 探索与 View Transitions 实验支持——声明式转场是方向

```jsx
function Draggable() {
  const ref = useRef();
  const [pos, setPos] = useState({ x: 0, y: 0 });
  const onMove = (e) => {
    // 高频: 直接操作 DOM, 不 setState
    ref.current.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
  };
  const onEnd = () => {
    flushSync(() => setPos(readDomPos(ref.current)));  // 结束时同步状态
  };
}
```
