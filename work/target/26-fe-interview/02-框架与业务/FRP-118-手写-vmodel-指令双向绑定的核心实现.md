---
title: [FRP-118] 手写 v-model 指令：双向绑定的核心实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-118：手写 v-model 指令：双向绑定的核心实现？

**答**：
- 双向绑定 = **数据 → 视图**（响应式 effect 重渲染属性）+ **视图 → 数据**（input 事件把 DOM 值写回 state），两边都经过同一个响应式对象，天然同步。
- 自定义指令形态（Vue 3）：`mounted`（初始同步 + 绑事件）与 `updated`（父重渲染时同步值）两个钩子；核心代码 30 行内。
- 关键细节：事件回调里**防止循环触发**（写回 state 后 effect 又把同样的值写回 DOM，需值比较短路）；select/checkbox 需要不同的取值路径（`checked`/`selectedOptions`），所以 v-model 按元素类型分派（呼应 FRP-064）。
- 无框架版同理：一个 `bind(el, state, key)` 函数 = 读方向 effect + 写方向 listener。

```javascript
// 简化实现，帮助理解：v-model 指令的双向同步核心（30 行）
// 依赖：reactive/effect 来自 FRP-113
function vModel(el, state, key) {
  // 方向 1：数据 -> 视图（初始 + 每次数据变化）
  const render = () => {
    if (el.value !== state[key]) el.value = state[key] ?? ''; // 值相同短路，防循环
  };
  effect(render);

  // 方向 2：视图 -> 数据
  el.addEventListener('input', () => { state[key] = el.value; });
}

// Vue 3 自定义指令等价形态
const vModelDirective = {
  mounted(el, { value, instance }) {
    // value 是表达式对应的 setupState key 的 getter/setter 封装
    el.value = value();
    el.addEventListener('input', (e) => instance.proxy.$emit?.('update') ?? (el.__set?.(e.target.value)));
  },
  updated(el, { value }) {
    if (el.value !== value()) el.value = value(); // 父组件重渲染时同步
  },
};

// 组合验证：输入框 <-> state 双向
const state = reactive({ msg: 'hello' });
const input = document.createElement('input');
vModel(input, state, 'msg');
console.log(input.value);        // hello：数据 -> 视图

input.value = 'world';
input.dispatchEvent(new Event('input')); // 模拟用户输入
console.log(state.msg);          // world：视图 -> 数据

state.msg = 'changed';           // 外部改数据（如接口回填）
console.log(input.value);        // changed：effect 自动同步回视图
// 循环防护验证：state.msg === input.value 时 render 短路，不会死循环
```
