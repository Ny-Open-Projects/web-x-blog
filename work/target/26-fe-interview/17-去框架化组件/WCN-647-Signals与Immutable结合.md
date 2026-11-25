---
title: [WCN-647] Signals 与不可变数据（Immutable）结合时，如何处理「结构相等」与更新通知？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-647：Signals 与不可变数据（Immutable）结合时，如何处理「结构相等」与更新通知？

**答**：
- 结论：Signal 只做「引用是否变化」的浅比较；配合 Immutable 数据结构时，引用变化即代表内容变化，可直接通知；深层比较交给 computed 派生。
- 做法：用 Object.is 判断；对需要内容相等的场景用自定义 equals（如深比较/结构哈希）避免无谓更新。
- 追问钩子：自定义 equals 有什么坑？深比较本身有成本，大对象反而更慢——考察对「比较成本 vs 更新成本」的权衡。

```javascript
function signal(v, equals = Object.is) {
  let value = v;
  const subs = new Set();
  return {
    get() { if (active) subs.add(active); return value; },
    set(nv) {
      if (equals(nv, value)) return; // 相等则不通知
      value = nv; subs.forEach(f => f());
    },
  };
}
const shallowEq = (a, b) => a === b;
const arr = signal([1, 2], shallowEq);
arr.set([1, 2]); // 新引用 → 触发更新
const obj = signal({ a: 1 }, (a, b) => JSON.stringify(a) === JSON.stringify(b));
obj.set({ a: 1 }); // 内容相等 → 不触发（但深比较有成本）
```
