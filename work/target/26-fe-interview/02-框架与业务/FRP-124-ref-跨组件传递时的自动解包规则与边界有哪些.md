---
title: [FRP-124] ref 跨组件传递时的自动解包规则与边界有哪些？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-124：ref 跨组件传递时的自动解包规则与边界有哪些？

**答**：
- **模板顶层**：ref 自动解包（编译器对 setup 返回值做 isRef 判断 + 渲染时 unref）；**reactive 对象内部**的 ref 读写都自动解包（Proxy get/set trap 里处理）。
- 边界 1：ref 放进**数组或原生集合**不解包——`[ref][0]`、`map.get('k')` 拿到的是 ref 对象本身（数组索引没有"属性访问 trap 可挂解包逻辑"的设计取舍）。
- 边界 2：解构 reactive 之后的 ref 不会解包（已经离开了代理对象）；`shallowReactive` 的嵌套层也不解包。
- 边界 3：props 传递时，子组件在 props 里拿到的是 ref **对象本身**，只在子组件模板顶层使用时才解包；事件里 `props.count + 1` 会出错，要 `.value`。

```javascript
// 简化实现，帮助理解自动解包的规则
function isRef(r) { return !!(r && r.__isRef); }

// 规则 1：reactive 内部 ref 自动解包（get/set trap）
function reactive(obj) {
  const targetIsArray = Array.isArray(obj);
  return new Proxy(obj, {
    get(target, key) {
      const v = Reflect.get(target, key);
      if (isRef(v)) {
        // 核心判断（源码同款）：数组 + 整数索引时【跳过】解包
        const isIndexKey = targetIsArray && typeof key === 'string' && /^\d+$/.test(key);
        return isIndexKey ? v : v.value;
      }
      return (typeof v === 'object' && v !== null) ? reactive(v) : v;
    },
    set(target, key, nv) {
      const old = Reflect.get(target, key);
      // 赋普通值给已有 ref 属性：解包写入 old.value（保持同一个 ref 被更新）
      if (isRef(old) && !isRef(nv)) { old.value = nv; return true; }
      return Reflect.set(target, key, nv); // 赋 ref 本身则整体替换属性
    }
  });
}

const count = { __isRef: true, value: 0, set value(nv) { this._v = nv; }, get value() { return this._v ?? 0; } };
const state = reactive({ count });
console.log(state.count); // 0 —— 解包了，不需要 .value
state.count = 5;          // 写回 count.value = 5
console.log(count.value); // 5 —— 同一个 ref 被更新

// 边界验证
const list = reactive([count]);            // 数组
console.log(list[0].__isRef, list[0].value); // true 5 —— 数组索引不解包！要 .value
const { count: c2 } = reactive({ count }); // 解构
console.log(c2.__isRef);                   // true —— 解构后是 ref 本身，要用 c2.value

// props 场景：子组件里 props.count 是 ref 本身
function childSetup(props) {
  // props.count + 1        // "[object Object]1" —— 对象参与运算，错
  return () => props.count.value + 1; // 正确（模板中 {{ count }} 会自动解包）
}
```
