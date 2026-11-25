---
title: [DP-091] 虚拟 DOM 是哪些模式的组合？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-091：虚拟 DOM 是哪些模式的组合？（高频）
**答**：
- **工厂**：`h/createElement` 产出统一 VNode（DP-017）。
- **代理（数据层）**：Vue3 reactive 拦截数据变化驱动重新执行渲染函数（React 则是 setState 触发）。
- **策略**：diff 按"同类型/不同类型/列表"分派处理；列表 diff 的 key 算法（最长递增子序列）是核心策略。
- **备忘录/享元**：patchFlag/blockTree 记录动态节点（跳过静态内容，Vue3 优化）；**组合**：组件树递归 patch。

```javascript
// mini VNode diff：工厂 + 策略 + 备忘录组合
const h = (type, props, ...children) => ({          // 工厂
  type, props: props || {},
  children: children.flat().map((c) => (typeof c === 'object' ? c : { type: 'TEXT', props: { nodeValue: c } })),
});
function patch(container, vnode) {
  const el = (vnode.el = vnode.type === 'TEXT'
    ? document.createTextNode('')                   // 策略：文本节点
    : document.createElement(vnode.type));          // 策略：元素节点
  for (const [k, v] of Object.entries(vnode.props)) {
    if (k.startsWith('on')) el.addEventListener(k.slice(2).toLowerCase(), v);
    else el.setAttribute(k, v);
  }
  vnode.children.forEach((c) => { patch(el, c); });
  container.appendChild(el);
  return el;
}
// diff：同类型复用（备忘录：复用 el 引用与旧 props 快照）
function diff(n1, n2) {
  if (n1.type !== n2.type) {                         // 策略1：类型不同 -> 重建
    n1.el.replaceWith(patch(document.createElement('div'), n2).firstChild || n2.el);
    return;
  }
  n2.el = n1.el;                                     // 策略2：同类型 -> DOM 复用
  for (const [k, v] of Object.entries(n2.props)) {   // props 增量更新
    if (n1.props[k] !== v) n2.el.setAttribute(k, v);
  }
  const max = Math.max(n1.children.length, n2.children.length);
  for (let i = 0; i < max; i++) {
    const c1 = n1.children[i], c2 = n2.children[i];
    if (c1 && c2) diff(c1, c2);                      // 递归（组合）
    else if (c2) patch(n2.el, c2);                   // 新增
    else if (c1) c1.el?.remove?.() ?? n2.el.removeChild(c1.el); // 删除
  }
}
// 列表 diff 策略要点：key 标记身份，Vue3 用最长递增子序列最小化 DOM 移动
console.log(JSON.stringify(h('div', { id: 'a' }, 'hello', h('span', null, 'x'))));
// {"type":"div","props":{"id":"a"},"children":[{"type":"TEXT",...},{"type":"span",...}]}
```
