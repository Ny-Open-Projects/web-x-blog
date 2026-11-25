---
title: [MFW-847] 笔试：手写 Suspense 边界独立超时隔离调度器
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-847：笔试：手写 Suspense 边界独立超时隔离调度器

**答**：
- 结论：每个 Suspense 边界用独立超时（Promise.race），超时即返回 fallback 并 flush，不阻塞其他边界——这是流式渲染「部分可用」的基础。
- 关键：慢边界超时后仍可后台完成，但结果已被丢弃（因为已 flush），不能覆盖。
- 追问钩子：超时时间怎么设？——按数据与用户体验分级，关键内容长、次要内容短。

```javascript
function withTimeout(promise, ms, fallback) {
  let timer;
  return Promise.race([
    promise.finally(() => clearTimeout(timer)),
    new Promise(res => { timer = setTimeout(() => res(fallback), ms); })
  ]);
}
function createBoundaryScheduler() {
  const done = new Set();
  return {
    async add(name, promise, timeout, fallback) {
      const html = await withTimeout(promise, timeout, fallback);
      done.add(name);                                // 就绪，可 flush
      return html;
    },
    flushReady() { return [...done]; }
  };
}

// 自测：快边界先完成，慢边界超时兜底，互不阻塞
const s = createBoundaryScheduler();
s.add('fast', Promise.resolve('<fast>'), 100, '<fb>');
s.add('slow', new Promise(r => setTimeout(() => r('<slow>'), 500)), 80, '<fb>');
setTimeout(() => console.log(s.flushReady().sort()), 150); // ['fast','slow']
```

**评分点**：
- 每个边界独立超时（Promise.race），不互相阻塞
- 超时返回 fallback，保证 UI 完整与部分可用
- 超时后慢结果到达被丢弃（已 flush，不覆盖）
- 清理定时器避免泄漏；能讨论超时分级设置（加分）
