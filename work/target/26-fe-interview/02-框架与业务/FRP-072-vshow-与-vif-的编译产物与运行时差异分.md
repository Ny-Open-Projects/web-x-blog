---
title: [FRP-072] v-show 与 v-if 的编译产物与运行时差异分别是什么？各自适用什么场景？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-072：v-show 与 v-if 的编译产物与运行时差异分别是什么？各自适用什么场景？

**答**：
- 编译产物：v-if 是**编译期三分支**——生成三元表达式，条件为真创建元素 vnode、为假建注释 vnode `createCommentVNode("v-if")`，切换即**卸载/重建**整棵子树（走完整 create/destroy 流程，含组件重挂载）。
- v-show 只是**一个指令**：编译产物里元素始终被创建，vShow 指令的 mounted/updated 钩子执行 `el.style.display = value ? originalDisplay : 'none'`，切换只是改一行样式，开销 O(1)。
- 运行时差异：v-if 有**惰性**（初始 false 不渲染）与真实销毁（组件状态丢失、生命周期重走）；v-show 无惰性（初始就渲染）、状态保留、无生命周期开销。
- 选型：频繁切换用 v-show（如 tab 内容、tooltip），条件很少变或初始不需要渲染用 v-if（如权限块、重组件按需加载）；v-show 不支持 template/多根，因为它要挂在真实元素上。

```javascript
// 简化实现，帮助理解两者的编译产物与运行时行为
// v-if 编译产物形态：<div v-if="ok">hi</div>
function renderWithVIf(_ctx) {
  return _ctx.ok
    ? createElementBlock('div', null, 'hi')            // 真实元素
    : createCommentVNode('v-if');                       // 注释占位节点
}
// 切换 ok = true 时：从注释节点 patch 到元素节点 -> 完整 mount（重建 DOM）
// 切换 ok = false 时：完整 unmount，组件实例销毁、生命周期走 unmounted

// v-show 编译产物形态：元素恒存在 + withDirectives 包装
function renderWithVShow(_ctx) {
  return withDirectives(
    createElementBlock('div', null, 'hi'),
    [[vShow, _ctx.ok]],                                 // 指令携带当前布尔值
  );
}
// vShow 指令实现：只操作 display
const vShow = {
  beforeMount(el, { value }) {
    el._vod = el.style.display === 'none' ? '' : el.style.display; // 记录原 display
    el.style.display = value ? el._vod : 'none';
  },
  updated(el, { value, oldValue }) {
    if (value === oldValue) return;                     // O(1) 短路
    el.style.display = value ? el._vod : 'none';
  },
};

// 验证行为差异
const state = reactive({ ok: false });
let mountCount = 0;
const comp = { render: () => { mountCount++; return renderWithVIf(state); } };
state.ok = true;  // v-if：DOM 重建，组件重新走 setup（若为组件）
state.ok = false; // v-if：DOM 销毁
console.log('v-if 切换触发渲染次数:', mountCount);      // 每次切换都参与渲染
const el = document.createElement('div');
vShow.beforeMount(el, { value: true });
console.log('v-show 初始渲染即便 false 也存在 DOM:', !!el._vod !== undefined); // true
```

## 十一、Vue Router 与 Pinia 原理
