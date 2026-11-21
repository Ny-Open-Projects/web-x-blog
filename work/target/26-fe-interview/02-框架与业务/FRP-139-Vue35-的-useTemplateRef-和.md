---
title: [FRP-139] Vue3.5 的 useTemplateRef 和响应式 props 解构分别是什么原理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-139：Vue3.5 的 useTemplateRef 和响应式 props 解构分别是什么原理？

**答**：
- `useTemplateRef('box')`：框架内部维护一个 `Map<key, ref>`，模板 ref 挂载时（setRef）同时写入这个 map；`useTemplateRef` 返回一个绑定到 map 条目的 **shallowRef**——挂载/卸载时值自动变成 DOM/实例/null。
- 它解决的痛点：模板里 `ref="box"` 的 key 必须与 setup 变量**同名**（隐式耦合）；useTemplateRef 用字符串 key 解耦，支持动态 key 与循环引用。
- 响应式 props 解构：编译器把 `const { title } = defineProps()` 的所有读取**重写为 props.title**（见 FRP-123），默认值并入 runtime props——运行时不存在局部变量。
- 两者都体现 3.5 的主线：把"魔法约定"（同名变量、不能解构）换成显式 API 与编译器转换，降低心智负担。

```javascript
// 简化实现，帮助理解 useTemplateRef
const templateRefMap = new Map();   // key -> 当前 DOM/实例（setRef 时写入）

function setRef(key, el) {
  templateRefMap.set(key, el);      // 挂载/卸载时都会调用：el 为 null 表示卸载
  notify(key);
}

const keySubs = new Map();
function notify(key) {
  (keySubs.get(key) || []).forEach(f => f());
}

function useTemplateRef(key) {
  // 返回 shallowRef：DOM 节点不需要深层响应式（浅引用即可）
  const r = shallowRef(null);
  const update = () => { r.value = templateRefMap.get(key) ?? null; };
  update();
  // 订阅该 key 的变化（真实实现由框架在 ref 设置时同步触发）
  if (!keySubs.has(key)) keySubs.set(key, new Set());
  keySubs.get(key).add(update);
  return r;
}

// 使用：
// <template><input ref="box" /></template>
// const box = useTemplateRef('box');   // 挂载后 box.value 是 input 元素
// 动态 key 也支持：useTemplateRef(dynamicKey)

// —— 响应式 props 解构：编译器重写 ——
// 源码：
//   const { title = '默认', count } = defineProps<{ title?: string; count: number }>()
//   watchEffect(() => console.log(title, count))
// 产物：
function compiled(props) {
  // 没有 const title = ...！所有 title/count 读取被替换为 props.title/props.count
  watchEffect(() => console.log(props.title, props.count));
}
// 默认值 '默认' 并入 runtime props：{ title: { type: String, default: '默认' } }
// 因此 watchEffect 能正常收集 props.title 的依赖 —— 解构后依然是响应式的
```

## 二十一、React Server Components 深入
