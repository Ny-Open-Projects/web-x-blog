---
title: [WCN-457] 笔试：实现迷你 SSR 渲染器（组件描述 → HTML 字符串）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-457：笔试：实现迷你 SSR 渲染器（组件描述 → HTML 字符串）。
**题目**：组件描述同 451（静态/动态绑定）：SSR 模式下信号读取直接求值（无 effect）；输出 HTML（属性转义/文本转义）；输出与客户端渲染 DOM 结构一致（同源函数）。

```javascript
function ssrRender(node, scope) {
  const attrs = Object.entries(node.static || {})
    .map(([k, v]) => ` ${k}="${esc(v)}"`).join('');
  const dyn = Object.entries(node.dynamic || {})
    .map(([k, expr]) => ` ${k}="${esc(evalIn(expr, scope))}"`).join('');
  const text = node.dynamic?.text ? esc(evalIn(node.dynamic.text, scope))
    : (node.staticText ?? '');
  return `<${node.tag}${attrs}${dyn}>${text}</${node.tag}>`;
}
// CSR 同一 node 描述 → 结构一致（水合语义成立）

```

**评分点**：
- 双模式：compileNode 的 SSR 版（直接求值拼接）。
- 转义（属性/文本全 escape）。
- 与 CSR 同源：同一描述对象两条管线（结构一致断言）。
- 性能：字符串拼接 + 数组 join。
