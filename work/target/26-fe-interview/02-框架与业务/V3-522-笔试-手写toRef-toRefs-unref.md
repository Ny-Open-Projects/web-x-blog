---
title: [V3-522] 笔试：手写 toRef / toRefs / unref / toValue
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-522：笔试：手写 toRef 系列

**答**：实现：① `toRef(obj, key)`：返回代理 ref，读写直通 obj[key]（保持响应式连接）；② `toRefs(obj)`：全字段转 ref（解构保响应式）；③ `unref(v)`：ref 则 .value 否则原值；④ `toValue(v)`：支持 getter（调用取值）；⑤ ref 判断（isRef 用 __v_isRef 标记）。写出实现与边界（toRef 对不存在的 key 行为）。

```javascript
const REF_FLAG = '__v_isRef';

function isRef(r) { return !!(r && r[REF_FLAG]); }
function unref(v) { return isRef(v) ? v.value : v; }
function toValue(v) { return isRef(v) ? v.value : (typeof v === 'function' ? v() : v); }

function ref(v) {
  return {
    get value() { trackRef(this); return v; },
    set value(nv) { v = nv; triggerRef(this); },
    [REF_FLAG]: true,
  };
}

function toRef(obj, key) {
  return {
    get value() { return obj[key]; },           // 直通: 保持与源对象的连接
    set value(nv) { obj[key] = nv; },
    [REF_FLAG]: true,
  };
  // 边界: key 不存在时 get 返回 undefined, set 会创建该属性(与源保持同步)
}

function toRefs(obj) {
  const out = {};
  for (const k of Object.keys(obj)) out[k] = toRef(obj, k);
  return out;
}
// 用法: 解构 reactive 不丢响应式
const state = reactive({ a: 1, b: 2 });
const { a, b } = toRefs(state);   // a.value ↔ state.a 双向同步
```

**评分点**：
- toRef 的 getter/setter 直通源对象（不是拷贝值）
- toRefs 遍历生成（解构保响应式的原理）
- toValue 统一 ref/getter/值三种输入
- isRef 标记位方案与不存在的 key 行为
