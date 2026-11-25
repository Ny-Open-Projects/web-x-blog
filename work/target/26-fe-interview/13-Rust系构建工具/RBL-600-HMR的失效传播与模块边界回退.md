---
title: [RBL-600] HMR 的失效传播算法：接受边界与向上冒泡的终止条件
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-600：HMR 的失效传播算法：接受边界与向上冒泡的终止条件

**答**：
- HMR 的传播模型：文件失效 → 所在模块失效 → 沿**导入反向边**向上传播，直到遇到「接受边界」（`import.meta.hot.accept`）或 entry。遇到边界：只重跑边界与失效模块之间的模块（子树重执行）；到 entry 未被接受 → 整页 reload 兜底。
- accept 的三种粒度：1) 自接受（模块声明自己可热更，CSS/组件文件典型）；2) 接受指定依赖（父模块处理子模块更新——组件文件更新由父页面 accept 处理）；3) acceptExports（细粒度：只重执行受影响导出，配合导出级依赖图，是 RSC/Fast Refresh 的基础）。
- 无关性剪枝是性能关键：失效传播只在「受影响闭包」内做——用反向可达性（从失效模块沿导入反边向上）而非全图重算；同时利用「同 chunk 无关模块」信息避免整个 chunk 失效（RBL-598 级联 hash 是产物层，HMR 是内存层，粒度更细）。
- 状态保持难题：模块重执行后旧状态丢失——Fast Refresh 类方案靠「组件身份比对 + state 保留」（React 元素树重新协调），纯 ESM HMR 靠开发者手动在 accept 回调里搬运状态；「可热更的模块设计」本身就是架构约束（状态外置到 store/持久层）。
- 追问钩子：为什么 CSS 天然可自接受而 JS 难？——CSS 无模块级状态、副作用幂等（替换 style 即可）；JS 的执行副作用（注册/监听/定时器）不清理就泄漏——HMR 框架要求模块提供 dispose 回调（cleanup 契约），这是「热更安全」的工程化表达。

```javascript
// HMR 失效传播（概念实现）
function invalidate(startId, graph) {
  const stale = new Set([startId]);
  const boundaries = [];
  const visit = (id, chain) => {
    for (const parent of graph.importersOf(id)) {       // 反向边向上
      if (chain.has(parent)) continue;                  // 环保护
      if (graph.accepts(parent, id)) {                  // 接受边界
        boundaries.push({ boundary: parent, affected: [...chain, id] });
        continue;                                       // 不再向上冒泡
      }
      if (parent === 'entry') { boundaries.push({ boundary: 'reload' }); continue; }
      stale.add(parent);
      visit(parent, new Set([...chain, parent]));
    }
  };
  visit(startId, new Set([startId]));
  return { stale, boundaries };
}

// 模块侧契约
if (import.meta.hot) {
  import.meta.hot.accept((newMod) => { /* 用新导出更新视图 */ });
  import.meta.hot.dispose(() => {                       // 清理副作用契约
    clearInterval(timer); unlistenEvents();
  });
}
// 自接受（CSS）：
// import.meta.hot.accept() —— 直接替换 style，无状态搬运
```
