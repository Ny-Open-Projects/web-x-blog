---
title: [FRP-121] 数组索引与 length 的响应式在 Vue3 源码里有哪些细节处理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-121：数组索引与 length 的响应式在 Vue3 源码里有哪些细节处理？

**答**：
- Proxy 天然拦截 `arr[i] = x` 和 `arr.length = n`，所以 Vue3 中**索引与 length 都是响应式的**（Vue2 必须用 `Vue.set` 补丁）。
- 新增索引（如 `arr[100] = 1`）时除了 trigger 该 key，还要 trigger `length`（源码：key 不存在时对 length 额外触发 ADD）。
- 缩短 length 时被截掉的索引要清理：源码对 `newLength` 以下的旧索引做 delete 并逐个 trigger。
- 迭代类 key（`Symbol.iterator` / `forEach` / `keys` / `values`）读取时统一 track 到 **ITERATE_KEY**，数组增删（无 key 的 trigger）就依赖它通知所有迭代副作用。

```javascript
// 简化实现，帮助理解数组索引与 length 的 trigger 细节
const ITERATE_KEY = Symbol('iterate');

function createArrayReactive(target) {
  return new Proxy(target, {
    get(target, key, receiver) {
      // 迭代 key 统一 track 到 ITERATE_KEY
      track(key === Symbol.iterator || typeof key === 'symbol' ? ITERATE_KEY : key);
      return Reflect.get(target, key, receiver);
    },
    set(target, key, value, receiver) {
      const oldVal = target[key];
      const oldLen = target.length;              // 先记录旧长度，Reflect.set 之后再对比
      const hadKey = Object.prototype.hasOwnProperty.call(target, key);
      const type = key === 'length' ? 'length' : (hadKey ? 'set' : 'add');
      const result = Reflect.set(target, key, value, receiver);
      if (type === 'add') {
        trigger(key, 'add');          // 新索引本身
        trigger('length', 'add');     // 源码细节：新增 key 时联动 length
        trigger(ITERATE_KEY, 'add');  // 迭代依赖（v-for）
      } else if (type === 'length' && value !== oldLen) {
        // 缩短 length：清理被截断的索引并逐个触发
        for (let i = value; i < oldLen; i++) trigger(i, 'delete');
        trigger(ITERATE_KEY, 'delete');
      } else if (value !== oldVal) {
        trigger(key, 'set');
      }
      return result;
    },
    deleteProperty(target, key) {
      const hadKey = key in target;
      const result = Reflect.deleteProperty(target, key);
      if (hadKey) { trigger(key, 'delete'); trigger(ITERATE_KEY, 'delete'); }
      return result;
    }
  });
}

// 验证
const deps = new Map();
function track(key)  { if (active) { (deps.get(key) ?? deps.set(key, new Set()).get(key)).add(active); } }
function trigger(key, type) { (deps.get(key) || []).forEach(f => f()); }
let active = null;

const arr = createArrayReactive([1, 2, 3]);
active = () => console.log('list =', arr.join(','));
track(Symbol.iterator); deps.get(Symbol.iterator).add(active);
arr[5] = 9;      // 触发迭代依赖：list = 1,2,3,,,9
arr.length = 2;  // 截断：list = 1,2
```
