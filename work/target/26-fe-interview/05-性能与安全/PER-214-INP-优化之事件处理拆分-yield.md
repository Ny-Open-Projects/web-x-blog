---
title: [PER-214] 事件 handler 太长导致 INP 超标，如何拆分？yieldToMain 怎么写才正确？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-214：事件 handler 太长导致 INP 超标，如何拆分？yieldToMain 怎么写才正确？

**答**：
- 原则：handler 里先做"用户立即可感知"的最小工作（乐观 UI、表单校验反馈），把重计算/上报/列表渲染等拆成切片让出主线程，让浏览器有机会渲染下一帧。
- 切片工具：现代浏览器优先 `scheduler.yield()`（让出时保持优先级，不会被饿死）；降级链：`scheduler.postTask` → `setTimeout`（注意 setTimeout 会被低优先级排队）。封装 yieldToMain 统一处理。
- 拆分粒度：单个切片 ≤ 50ms；切片间通过 Promise 链传递中间状态；不要为 yield 而 yield——几毫秒的小 handler 直接跑完反而更快（yield 本身有调度成本）。
- 渲染侧配合：大列表渲染交给虚拟列表；强制同步布局（读 offsetTop 后立刻写样式）要在切片边界归并读写。

```javascript
const yieldToMain = () => {
  if ('scheduler' in window && 'yield' in scheduler) return scheduler.yield();
  return new Promise(r => setTimeout(r, 0));   // 降级（可能被降优先级，尽量少用）
};

async function onSubmit(e) {
  e.preventDefault();
  setLoading(true);                                  // 1. 同步最小反馈，用户立刻看到
  const form = new FormData(e.target);
  const chunks = chunk(validateAndBuild(form), 200); // 2. 把重活切成小片
  const results = [];
  for (const c of chunks) {
    results.push(...c());
    await yieldToMain();                             // 3. 每片让出，浏览器得以渲染/响应
  }
  setLoading(false); renderResults(results);
}
// 反例：await yieldToMain() 放在 setLoading 之前，用户仍会感觉"点了没反应"
```
