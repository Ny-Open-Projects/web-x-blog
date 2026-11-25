---
title: [V3-138] 手写 computed（懒执行 + 脏标记）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-138：手写 computed（懒执行 + 脏标记）？
**答**：
- 两个关键：dirty 脏标记 + value 缓存，被访问时若不脏直接返回缓存，实现"懒计算"。
- 内部用 effect 包 getter，把它的 scheduler 设为"标脏 + 通知订阅 computed 的 effect"，而不是立即重算。
- 数据变化 → scheduler 只置 dirty 为 true 并触发订阅者 → 订阅者读 value 时才真正重算。
- 链式传播：computedA 依赖 computedB 时，标脏会沿依赖链向上传递，源码里就是 computed 也持有自己的 dep。

```javascript
// mini-computed.js
let activeEffect = null;

// 支持 scheduler 的 effect（V3-136 的扩展版）
function createEffect(fn, { scheduler } = {}) {
  const run = () => {
    activeEffect = run;
    const result = fn();
    activeEffect = null;
    return result;
  };
  run.scheduler = scheduler;
  run(); // 首次执行仅为收集 getter 内的依赖
  return run;
}

function computed(getter) {
  let value;         // 缓存值
  let dirty = true;  // 脏标记：true 表示需要重算
  const subs = new Set(); // 订阅了此 computed 的外部 effect
  const runner = createEffect(getter, {
    scheduler() {
      if (!dirty) {
        dirty = true;                            // 先标脏，不立刻重算
        [...subs].forEach((fn) => (fn.scheduler || fn.run)()); // 再通知订阅者
      }
    },
  });
  return {
    get value() {
      if (dirty) {
        value = runner();   // 懒：被访问且脏了才重算
        dirty = false;
        if (activeEffect) subs.add(activeEffect); // 收集订阅者
      }
      return value;
    },
  };
}

// 验证
const state = reactive({ a: 1, b: 2 }); // reactive 同 V3-136
const sum = computed(() => {
  console.log("计算执行了");
  return state.a + state.b;
});
console.log(sum.value); // 打印"计算执行了"，输出 3
console.log(sum.value); // 直接输出 3，不打印：命中缓存
state.a = 10;           // 只标脏，不重算，无输出
console.log(sum.value); // 此时才重算，打印"计算执行了"，输出 12
```
