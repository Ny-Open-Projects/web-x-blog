---
title: [V3-417] 笔试：手写迷你 renderToString（组件树 → HTML）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-417：笔试：手写迷你 renderToString（组件树 → HTML）
**答**：实现 `renderToString(node)`：node 为 `{ tag, props, children }`（children 可含文本/子节点/异步函数）；props 转属性（class 数组拼接、style 对象转串、布尔 true 输出属性名、false/null 省略）；children 为 Promise 时等待后渲染（简单流式不支持，要求全量等待）；HTML 转义文本内容。

```javascript
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
function renderProps(props = {}) {
  return Object.entries(props).filter(([, v]) => v !== false && v != null)
    .map(([k, v]) => {
      if (v === true) return ` ${k}`
      if (k === 'class' && Array.isArray(v)) return ` class="${esc(v.join(' '))}"`
      if (k === 'style' && typeof v === 'object') return ` style="${esc(Object.entries(v).map(([p, val]) => `${p}:${val}`).join(';'))}"`
      return ` ${k}="${esc(v)}"`
    }).join('')
}
async function renderToString(node) {
  if (node == null) return ''
  if (typeof node === 'string' || typeof node === 'number') return esc(node)
  if (typeof node.then === 'function') return renderToString(await node) // 异步子树
  const children = Array.isArray(node.children) || typeof node.children === 'object'
    ? (await Promise.all((node.children || []).map(renderToString))).join('')
    : renderToString(node.children)
  return `<${node.tag}${renderProps(node.props)}>${children}</${node.tag}>`
}
```
**评分点**：
- 布尔/空值属性的 HTML 语义（true 只出属性名）。
- class/style 特殊处理。
- 文本转义防 XSS（核心安全点）。
- 异步子节点 Promise.all 并行等待。
