---
title: [V3-233] 手写：useTemplateRef 的实现原理（按名寻址的模板引用桥）
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-233：手写：useTemplateRef 的实现原理（按名寻址的模板引用桥）
**需求**：实现 `useTemplateRef(name)`：返回一个 ref；要求实例维护 `templateRefs` 注册表，`ref="name"` 挂载/卸载时自动写入/清空注册表与对应 ref，同名多次出现时收集为数组，useTemplateRef 返回的 ref 与注册表双向一致。
**评分点**：
- 注册表与实例生命周期绑定（组件卸载清理）
- 数组语义正确（v-for 场景）
- 同名 ref 挂载/卸载的读写时机（mounted 后才可访问）
- 手写层能讲清"编译器只是传名字，运行时靠 setTemplateRef 桥接"

```javascript
// 迷你运行时
function useTemplateRef(name) {
  const instance = currentInstance;
  const r = ref(null);
  instance.templateRefMap.set(name, r); // 编译器把 <div ref="name"> 编译为 setTemplateRef(el,'name')
  return r;
}
function setTemplateRef(instance, el, name) {
  const r = instance.templateRefMap.get(name);
  if (Array.isArray(r?.value)) {       // v-for 收集场景
    const idx = r.value.indexOf(el);
    if (el) { if (idx === -1) r.value.push(el); }
    else if (idx > -1) r.value.splice(idx, 1);
  } else {
    r && (r.value = el);               // 单元素：卸载时 el=null 自动清空
  }
}
// mountElement 流程中的挂接点
function mountElement(vnode, parent) {
  const el = document.createElement(vnode.type);
  if (vnode.ref) setTemplateRef(vnode.instance, el, vnode.ref); // 挂载时写入
  parent.appendChild(el);
}
function unmountElement(vnode) {
  if (vnode.ref) setTemplateRef(vnode.instance, null, vnode.ref);
  vnode.el?.remove();
}
```
