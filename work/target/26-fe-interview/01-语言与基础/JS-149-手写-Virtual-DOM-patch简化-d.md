---
title: [JS-149] 手写 Virtual DOM patch？简化 diff 的核心逻辑是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-149：手写 Virtual DOM patch？简化 diff 的核心逻辑是什么？

**答**：
- 三个核心函数：h 生成虚拟节点、render 把虚拟节点变成真实 DOM、patch 比较新旧虚拟节点并最小化更新。
- patch 四种情况：旧无新有→挂载；旧有新无→卸载；类型不同（tag/文本）→整节点替换；同类型→更新 props 后递归 diff 子节点。
- 同类型更新只改变化的属性：旧有新无的属性删除，值变化的设置，事件回调跳过 setAttribute。
- 简化版按位对比子节点；生产级实现（snabbdom/Vue）会引入 key 做 keyed diff，把复杂度降到 O(n)。

```javascript
function h(tag, props = {}, children = []) {
  return { tag, props, children, key: props.key ?? null };
}

function render(vnode) {
  if (typeof vnode === 'string' || typeof vnode === 'number') {
    return document.createTextNode(String(vnode));  // 文本节点
  }
  const el = document.createElement(vnode.tag);
  for (const [k, v] of Object.entries(vnode.props)) {
    if (k === 'key') continue;
    k.startsWith('on')
      ? el.addEventListener(k.slice(2).toLowerCase(), v)  // onClick → click
      : el.setAttribute(k, v);
  }
  vnode.children.forEach((c) => el.appendChild(render(c)));
  return el;
}

const isSame = (a, b) =>
  typeof a === typeof b &&
  (typeof a === 'string' ? a === b : a.tag === b.tag);  // 文本比内容，元素比 tag

function patch(parent, oldV, newV, index = 0) {
  if (oldV == null) return parent.appendChild(render(newV));        // 1. 挂载
  if (newV == null) return void parent.removeChild(parent.childNodes[index]); // 2. 卸载
  if (!isSame(oldV, newV)) {                                        // 3. 类型不同 → 替换
    return parent.replaceChild(render(newV), parent.childNodes[index]);
  }
  const el = parent.childNodes[index];                              // 4. 同类型 → 复用
  diffProps(el, oldV.props || {}, newV.props || {});
  const max = Math.max(oldV.children.length, newV.children.length); // 5. 递归 diff 子节点
  for (let i = 0; i < max; i++) patch(el, oldV.children[i], newV.children[i], i);
}

function diffProps(el, oldP, newP) {
  for (const k of Object.keys(oldP)) {
    if (!(k in newP) && !k.startsWith('on')) el.removeAttribute(k); // 删失效属性
  }
  for (const [k, v] of Object.entries(newP)) {
    if (oldP[k] !== v && k !== 'key' && !k.startsWith('on')) el.setAttribute(k, v); // 更新变化项
  }
}

// 验证
const container = document.getElementById('app');
let vOld = h('ul', { class: 'list' }, [h('li', {}, ['a']), h('li', {}, ['b'])]);
container.appendChild(render(vOld));
const vNew = h('ul', { class: 'list active' }, [h('li', {}, ['a']), h('li', {}, ['B'])]);
patch(container, vOld, vNew, 0);   // 只有第二个 li 的文本和 class 会更新
vOld = vNew;
```
