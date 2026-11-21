---
title: [FRP-138] Vapor Mode 是什么？"无 VDOM"的编译目标是怎么工作的？（高频）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-138：Vapor Mode 是什么？"无 VDOM"的编译目标是怎么工作的？（高频）

**答**：
- Vapor Mode 是 Vue 的第三种编译产物形态：模板直接编译成**精确的 DOM 创建与更新代码**——没有 vnode 树、没有 diff，思路与 Solid 一致，但复用 Vue 的响应式系统。
- 更新点的生成规则：编译器在**每个动态绑定处**创建一个小 effect——文本绑定生成 `setText`，属性绑定生成 `setAttr/setProp`，事件绑定缓存 handler，条件/列表编译为专用 helper（`createIf/createFor`）。
- 收益：bundle 更小（不需要完整 renderer 与 diff 算法）、内存更低（没有 vnode 树常驻）、更新更快（改一个绑定 = 跑一个最小 effect，不经过任何比较）。
- 与现有体系的关系：VDOM 模式和 Vapor 模式可以**逐组件共存**（同一应用里混用），这是它区别于 Svelte 的工程取舍——不要求整体迁移。

```javascript
// 简化实现，帮助理解 Vapor 的编译产物形态
// 模板：
//   <button :class="cls" @click="inc">{{ count }}</button>
//   <div v-if="show">hi</div>
// Vapor 产物（伪代码）：
function setup() {
  const count = ref(0);
  const cls = computed(() => count.value > 3 ? 'big' : 'small');
  const show = ref(true);

  const n0 = t0();               // t0 = 模板克隆：<button><span></span></button>
  const n1 = single(n0);         // button
  const n2 = child(n1);          // span

  // —— 每个动态绑定一个小 effect：没有 vnode，没有 diff ——
  effect(() => setProp(n1, 'class', cls.value));      // class 绑定
  effect(() => setText(n2, count.value));             // 文本绑定
  n1.addEventListener('click', inc);                  // 事件：静态缓存

  const n3 = createIf(() => show.value, () => {       // v-if 编译为 helper
    const b = t1();                                    // <div>hi</div>
    return b;
  });

  function inc() { count.value++; }                   // 只触发上面两个 effect，无组件级重渲

  return [n0, n3];
}

// —— 对照 VDOM 模式产物 ——
function renderVDOM() {
  return (_openBlock(), _createElementBlock('div', null, [
    _createElementVNode('button', {
      class: _normalizeClass(_unref(cls)),
      onClick: inc
    }, _toDisplayString(_unref(count)), 1 /* TEXT | CLASS */),
    _unref(show) ? (_openBlock(), _createElementBlock('div', { key: 0 }, 'hi')) : _createCommentVNode('v-if', true),
  ]));
  // 差异一目了然：VDOM 版每次 count 变化要重跑整个 render + diff；
  // Vapor 版只跑 setText/ setProp 两个最小 effect。
}
```
