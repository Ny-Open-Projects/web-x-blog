---
title: [V3-264] 手写：迷你 renderToString（组件树 → HTML 字符串）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-264：手写：迷你 renderToString（组件树 → HTML 字符串）
**答**：实现 `renderToString(vnode)`：支持元素节点（attrs 序列化含 class/style/布尔属性）、文本、子组件（setup 函数返回渲染函数）、数组 children、props 内函数属性忽略、事件忽略；HTML 转义文本节点；支持 Fragment 输出为子元素序列。
**评分点**：
- attrs 序列化：布尔 true 属性只写名、null/undefined 跳过、函数跳过
- 文本与属性值的 HTML 转义（& < > "）
- 组件递归（setup 返回函数再调用）
- 注释锚点或 Fragment 处理策略说明

```javascript
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
function attrsToString(props = {}) {
  return Object.entries(props)
    .filter(([k, v]) => k !== 'children' && typeof v !== 'function' && v !== null && v !== undefined && v !== false)
    .map(([k, v]) => v === true ? ` ${k}` : ` ${k}="${esc(v)}"`).join('');
}
function renderToString(vnode) {
  if (vnode == null || typeof vnode === 'boolean') return '';
  if (typeof vnode === 'string' || typeof vnode === 'number') return esc(vnode);
  if (Array.isArray(vnode)) return vnode.map(renderToString).join('');
  const { type, props = {}, children } = vnode;
  if (typeof type === 'function') {              // 组件：setup 返回渲染函数
    const view = type(props) || (() => null);
    return renderToString(view(props));
  }
  if (type === Fragment) return renderToString(children); // Fragment：只输出子级
  const inner = renderToString(children);
  return `<${type}${attrsToString(props)}>${inner}</${type}>`;
}
// 验证
function Greet({ name }) { return () => h('p', `hi, ${name}`); }
console.log(renderToString(h('div', { class: 'wrap', title: 'a<b' }, [
  h(Greet, { name: 'Tom' }), 'plain & <safe>', h(Fragment, null, [h('span', 'x')]),
])));
// <div class="wrap" title="a&lt;b"><p>hi, Tom</p>plain &amp; &lt;safe&gt;<span>x</span></div>
```
