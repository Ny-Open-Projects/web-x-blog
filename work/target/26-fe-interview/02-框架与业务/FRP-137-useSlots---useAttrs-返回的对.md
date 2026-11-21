---
title: [FRP-137] useSlots / useAttrs 返回的对象有什么特性？与编译优化如何配合？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-137：useSlots / useAttrs 返回的对象有什么特性？与编译优化如何配合？

**答**：
- `instance.slots / instance.attrs` 在初始化时被 Proxy 包装成**浅只读**对象：dev 模式下 get 未声明的属性会给告警，set 直接拦截（attrs 是"运行时兜底属性"不该被改）。
- `useSlots()/useAttrs()` 只是返回这两个内部对象的**稳定引用**——更新时框架替换的是对象内部字段而不是对象本身，所以组件里拿到的引用永远有效。
- attrs 的更新走 `updateProps`：未在 props 中声明的 key 会整体搬进 attrs（同一个对象、替换 inner 值），这保证 `$attrs` 的 v-bind 透传能继续工作。
- 编译优化配合：模板中 `$attrs` / `$slots` 编译为 `_ctx.$attrs`，v-for 具名插槽会生成稳定的 slot 函数 + `_` 编译标记，让子组件能跳过"内容没变"的插槽更新（见 FRP-131）。

```javascript
// 简化实现，帮助理解 slots/attrs 的 Proxy 包装与稳定引用
function initSlots(instance, children) {
  const rawSlots = normalizeSlots(children);
  instance.slots = new Proxy(rawSlots, {
    get(target, key) {
      if (key === '_') return rawSlots._;              // 编译标记原样透传
      warnWhenNoSlot(key, target);                     // dev：访问不存在的插槽告警
      return target[key];
    },
    set() { warn('slots 是只读的，请通过父组件更新内容'); return false; }
  });
}

function initAttrs(instance, rawProps, declaredProps) {
  const attrs = {};
  // 未声明的 key 归入 attrs（排除 class/style/事件等特殊 key 的处理）
  for (const key in rawProps) {
    if (!(key in declaredProps) && key !== 'class' && key !== 'style') {
      attrs[key] = rawProps[key];
    }
  }
  instance.attrs = attrs;
}

// updateProps 时 attrs 的"稳定引用"策略：
function updateAttrs(instance, nextProps, declaredProps) {
  const attrs = instance.attrs;            // 引用不变！
  const next = pickAttrs(nextProps, declaredProps);
  // 替换内部字段而不是换对象 —— 外部持有的 useAttrs() 引用保持有效
  for (const key in attrs) if (!(key in next)) delete attrs[key];
  Object.assign(attrs, next);
}

// 编译配合验证：
// <Child v-bind="$attrs" /> 编译产物：h(Child, toHandlers(_ctx.$attrs))
// <template #header="s"> 编译产物：createSlots(_, { header: (s) => [vnodes] , _: 1 })
//  ——— _: 1 是"稳定插槽标记"，子组件凭它跳过内容未变的插槽重渲染
```
