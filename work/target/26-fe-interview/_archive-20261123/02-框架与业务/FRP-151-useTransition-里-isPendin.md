---
title: [FRP-151] useTransition 里 isPending 的"过渡未完成"状态是如何同步给组件的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-151：useTransition 里 isPending 的"过渡未完成"状态是如何同步给组件的？

**答**：
- `startTransition(fn)` 把 fn 内的更新标记为 transition lane，同时 root 进入"过渡进行中"计数（pending transitions）。
- `isPending` 不是普通 state，而是 React 在**过渡开始/结束**时通过内部的共享队列通知订阅组件：实现上是 `useSyncExternalStore` 式的订阅——React 内部 store 的值就是"当前过渡是否未决"。
- 过渡结束的时机 = 对应 lane 的**提交完成**（commitRoot 后清除该 lane），而不是 render 结束——isPending 覆盖"渲染中 + 已渲染未提交"的完整区间。
- 同一组件内多个并存的 transition 会让 isPending 保持 true，直到最后一个过渡提交。

```javascript
// 简化实现，帮助理解 isPending 的订阅机制
function useTransition() {
  const [isPending, setPending] = useState(false);
  const isMounted = useRef(true);

  function startTransition(fn) {
    setPending(true);                        // 立即同步置 true（sync lane，马上可见）
    React.startTransition(() => {
      fn();                                  // 内部更新进 transition lane
      // 真实实现：React 在 commit 后通过回调恢复，这里用微任务模拟
      scheduleCallback(() => {
        if (isMounted.current) setPending(false); // 提交完成后置 false
      });
    });
  }

  useEffect(() => () => { isMounted.current = false; }, []);
  return [isPending, startTransition];
}

// —— React 内部视角：过渡计数 ——
const transitionStore = { pending: 0, listeners: new Set() };

function startTransitionScope() {
  transitionStore.pending++;                 // 过渡开始
  transitionStore.listeners.forEach(f => f());
  return () => {                             // commitRoot 时调用
    transitionStore.pending--;
    transitionStore.listeners.forEach(f => f());
  };
}
// fiber 上挂着 transition 订阅：组件通过 useSyncExternalStore 读 pending > 0
// 这保证 isPending 的变化与过渡 lane 的提交严格同步

// 使用与验证
const [isPending, start] = useTransition();
function onTabClick(id) {
  start(() => setTab(id));   // setTab 是低优过渡更新
  // 界面立即表现：isPending = true -> 显示 spinner/禁用态
  // 旧 tab 仍可交互（没有被阻塞），过渡渲染完成提交后：
  // isPending = false，新 tab 内容一次性替换
}
```
