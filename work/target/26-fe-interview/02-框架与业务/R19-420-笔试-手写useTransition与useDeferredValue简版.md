---
title: [R19-420] 笔试：手写 useTransition / useDeferredValue 简版
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## R19-420：笔试：手写 useTransition / useDeferredValue

**答**：在简化渲染器上模拟并发语义：① useTransition：startTransition 内的 setState 标记 low 优先级——渲染队列里 low 任务用 setTimeout 延后（可被 high 插队）；② isPending：low 渲染未完成时为 true；③ useDeferredValue(v)：内部用 useTransition 包装——值更新先返回旧值，下一轮更新新值；④ 高优更新打断低优（排队清除重排）。写出实现。

```javascript
const renderQueue = [];   // { fiber, priority }

function scheduleRender(fiber, priority = 'high') {
  renderQueue.push({ fiber, priority });
  setTimeout(flush, 0);
}
function flush() {
  const high = renderQueue.filter(t => t.priority === 'high');
  const low = renderQueue.filter(t => t.priority === 'low');
  renderQueue.length = 0;
  // 高优: 立即渲染; 低优: 延后(期间可被新高优插队)
  high.forEach(t => doRender(t));
  if (low.length) setTimeout(() => {
    // 若期间有新高优入队 → 本轮 low 被打断(简化: 重新入队)
    if (renderQueue.some(t => t.priority === 'high')) return;
    low.forEach(t => doRender(t));
    pendingLow.value = false;
  }, 200);
}

function useTransition() {
  const hook = currentFiber.hookList[hookIndex] ??= { pending: ref(false) };
  hookIndex++;
  const startTransition = (fn) => {
    hook.pending.value = true;
    const prev = currentPriority;
    currentPriority = 'low';
    try { fn(); } finally { currentPriority = prev; }
    // setState 内读取 currentPriority 决定 lane → 渲染队列按优先级调度
    setTimeout(() => { if (!renderQueue.some(t => t.priority === 'low')) hook.pending.value = false; }, 250);
  };
  return [hook.pending.value, startTransition];
}

function useDeferredValue(v) {
  const [prev, setPrev] = useState(v);
  useEffect(() => {                                  // 值变化: 先保持旧值, 低优更新
    startTransition(() => setPrev(v));
  }, [v]);
  return prev;                                       // 首轮返回旧值, 低优轮返回新值
}
```

**评分点**：
- 双优先级队列与高优打断低优（插队重排）
- isPending 与低优渲染未完成绑定
- startTransition 的优先级上下文切换（currentPriority）
- useDeferredValue 的「先旧后新」两轮语义
