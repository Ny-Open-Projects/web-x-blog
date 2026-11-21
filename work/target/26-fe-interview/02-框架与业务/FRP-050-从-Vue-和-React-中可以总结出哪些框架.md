---
title: [FRP-050] 从 Vue 和 React 中可以总结出哪些框架通用设计？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-050：从 Vue 和 React 中可以总结出哪些框架通用设计？

**答**：
- **状态变更通知**：push（Vue 的依赖收集）或 pull（React 的 setState）——核心是框架要能感知"数据变了"，感知粒度决定默认性能。
- **批量更新调度**：无论哪个框架，同一事件循环的多次变更都合并为一次渲染（Vue 队列 + nextTick，React 队列 + 微任务 flush），并提供 nextTick/flushSync 式的插队 API。
- **最小化差异更新**： vnode diff + key、编译期 patchFlag、双缓冲 Fiber 都服务于"只改必须改的 DOM"。
- **两阶段划分**：把"计算差异"（可中断/可重放）与"应用变更"（同步提交）分开，是所有现代框架实现并发能力的基础结构。
- 面试收尾话术：框架演进 = 让开发者写声明式代码的同时，框架在运行时/编译期自动逼近手写最优 DOM 操作的性能。

```javascript
// 一一对应：一个 60 行的迷你框架，串起三大通用设计
// 简化实现，帮助理解：状态通知 -> 批量调度 -> 差异更新
function createApp() {
  // ===== 1. 状态通知：Proxy 响应式（push 模型） =====
  let activeEffect = null;
  const deps = new Map(); // key -> Set<effect>

  const state = new Proxy(
    { count: 0 },
    {
      get: (t, k) => { if (activeEffect) { let s = deps.get(k); if (!s) deps.set(k, (s = new Set())); s.add(activeEffect); } return t[k]; },
      set: (t, k, v) => { t[k] = v; deps.get(k)?.forEach((e) => schedule(e)); return true; },
    }
  );

  // ===== 2. 批量调度：微任务去重 flush（Vue nextTick / React 自动批处理） =====
  const queue = new Set();
  let flushing = false;
  function schedule(job) {
    queue.add(job); // Set 去重：多次变更一次渲染
    if (flushing) return;
    flushing = true;
    Promise.resolve().then(() => { flushing = false; queue.forEach((j) => j()); queue.clear(); });
  }

  // ===== 3. 差异更新：文本节点最小化 patch（vnode diff 的最简形态） =====
  function render(rootEl, getTemplate) {
    let oldVnode = null;
    const job = () => {
      activeEffect = job;
      const newVnode = getTemplate(state); // 声明式模板：描述目标 UI
      activeEffect = null;
      if (oldVnode === null) {
        rootEl.textContent = newVnode;     // 首次挂载
      } else if (oldVnode !== newVnode) {
        rootEl.textContent = newVnode;     // diff 后仅更新变化的部分（此处简化为文本）
      }
      oldVnode = newVnode;
    };
    job(); // 首次执行即收集依赖
  }

  return { state, render };
}

// 用法：数据驱动 UI，多次修改自动批处理
const app = createApp();
app.render(document.querySelector('#app'), (s) => `count is ${s.count}`);
app.state.count++; // 微任务后 UI 变为 1
app.state.count++; // 批处理合并，本轮也只渲染一次
```

## 八、Vue 响应式源码再深入
