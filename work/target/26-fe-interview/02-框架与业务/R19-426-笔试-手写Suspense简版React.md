---
title: [R19-426] 笔试：手写 Suspense 简版（throw promise 捕获）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, Suspense]
type: 笔试题
---

## R19-426：笔试：手写 Suspense 简版

**答**：实现 Suspense 语义：① 组件渲染时 throw promise → 最近 Suspense 捕获；② Suspense 显示 fallback，promise resolve 后强制子树重渲染显示内容；③ 多个组件同时 throw（收集所有 promise，全部 resolve 才重渲染）；④ reject → 由 Error Boundary 处理；⑤ 用「渲染期 throw + 全局捕获器」简化实现。写出实现。

```javascript
let suspenseHandler = null;   // 当前渲染的 Suspense(栈顶)

class MySuspense {
  constructor({ fallback, children }) { this.fallback = fallback; this.children = children; }
  render(container) {
    const prev = suspenseHandler;
    suspenseHandler = this;
    this.pending = new Set();
    let result;
    try { result = renderChildren(this.children, container); }
    catch (thrown) {
      if (thrown && typeof thrown.then === 'function') {
        this.pending.add(thrown);
        container.innerHTML = '';
        container.appendChild(renderEl(this.fallback));
        Promise.all([...this.pending].map(p => p.catch(() => {}))).then(() => {
          // 全部 resolve → 重渲染真实内容
          container.innerHTML = '';
          this.render(container);
        });
        suspenseHandler = prev;
        return;
      }
      throw thrown;                                  // 非 promise: 交给 ErrorBoundary
    }
    suspenseHandler = prev;
    return result;
  }
}

// 组件侧: 数据未就绪时 throw promise
function Detail({ id }) {
  const p = fetchDetail(id);
  if (p.status === 'pending') throw p.promise;      // Suspense 捕获
  return h('div', null, p.value.name);
}
```

**评分点**：
- throw promise 的捕获协议（Suspense 核心机制）
- pending 集合全 resolve 才重渲染（多依赖原子出现）
- fallback 渲染与 resolve 后重渲染
- reject 交 Error Boundary 的分层
