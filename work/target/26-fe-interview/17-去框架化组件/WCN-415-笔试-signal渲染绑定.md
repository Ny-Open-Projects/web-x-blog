---
title: [WCN-415] 笔试：实现 signal → DOM 文本节点的直绑（细粒度更新原语）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-415：笔试：实现 signal → DOM 文本节点的直绑（细粒度更新原语）。
**题目**：`bindText(node, sigOrFn)`：信号变化直接写 textContent（不重建 DOM）；支持函数表达式（自动追踪）。返回 dispose。

```javascript
function bindText(node, src) {
  return effect(() => {
    const v = typeof src === 'function' ? src() : src.get();
    const s = String(v);
    if (node.textContent !== s) node.textContent = s;   // 值比对省写
  });
}
// <span data-el> 中：bindText(span, () => `${count()} 件`)
r
```

**评分点**：
- effect 建立依赖 → 直接写 textContent。
- 表达式形式（fn）同样适用（依赖自动收集）。
- 值比对（String 化相等跳过——省无效写）。
- dispose 断开。
