---
title: [WCN-635] 大型应用里 Signal 依赖链变复杂后，如何做可观测性与调试？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-635：大型应用里 Signal 依赖链变复杂后，如何做可观测性与调试？

**答**：
- 结论：给每个 signal/effect 加可追踪元数据（名字/创建栈），运行时采集依赖图与更新次数，用 devtools 或日志面板可视化。
- 做法：dev 模式包装 signal，记录 name 和 set 次数；effect 记录重算次数与耗时；提供 graph() 导出依赖边。
- 追问钩子：如何定位「谁改了这个值」？在 set 时记录调用栈（Error().stack）——但仅 dev 开启，避免生产性能损耗。

```javascript
const graph = { nodes: new Map(), edges: [] };
function debugSignal(name, value) {
  const s = signal(value);
  graph.nodes.set(name, { sets: 0 });
  return {
    get: s.get,
    set(v) {
      graph.nodes.get(name).sets++;
      if (process.env.NODE_ENV !== 'production') {
        console.debug(`[signal] ${name} <-`, new Error().stack.split('\n')[2]);
      }
      s.set(v);
    },
  };
}
const cart = debugSignal('cart', 0);
cart.set(1); cart.set(2);
console.log(graph.nodes.get('cart').sets); // 2：看到更新次数
```
