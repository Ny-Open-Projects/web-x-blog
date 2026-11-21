---
title: [TST-051] 笔试：手写深度比较（toEqual 内核，含循环引用与特殊类型）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-051：笔试：手写深度比较（toEqual 内核，含循环引用与特殊类型）
**答**：
- 需求：`deepEqual(a, b)` 支持：原始值（Object.is 语义）、数组/普通对象递归、键集合一致、Date 按时间值比较、循环引用不爆栈、NaN 相等、+0/-0 不等。
- 核心：先 Object.is 短路（天然处理 NaN/-0）；对象分支用 WeakMap 记录「a→b」配对，遇到已配对引用直接视为相等（打破循环）。
- 边界：原型不一致直接不等（class 实例 vs 字面量）；键数不同不等；Symbol 键是否参与要说明（真实实现参与）。

```javascript
function deepEqual(a, b, pairs = new Map()) {
  if (Object.is(a, b)) return true;                    // 处理 NaN、+0/-0
  if (a === null || b === null) return false;
  if (typeof a !== 'object' || typeof b !== 'object') return false;
  if (Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;

  if (a instanceof Date && b instanceof Date) return a.getTime() === b.getTime();
  if (a instanceof Date || b instanceof Date) return false;

  if (pairs.has(a)) return pairs.get(a) === b;         // 循环引用：已配对即相等
  pairs.set(a, b);

  const ka = [...Object.keys(a), ...Object.getOwnPropertySymbols(a)];
  const kb = [...Object.keys(b), ...Object.getOwnPropertySymbols(b)];
  if (ka.length !== kb.length) return false;

  return ka.every((k) => Object.prototype.hasOwnProperty.call(b, k)
    && deepEqual(a[k], b[k], pairs));
}

// ---- 用例 ----
expect(deepEqual({ a: NaN }, { a: NaN })).toBe(true);      // Object.is
expect(deepEqual(0, -0)).toBe(false);
expect(deepEqual(new Date('2026-01-01'), new Date('2026-01-01'))).toBe(true);
expect(deepEqual([1, { b: 2 }], [1, { b: 2 }])).toBe(true);
expect(deepEqual({ a: 1 }, { a: 1, b: undefined })).toBe(false); // 键数敏感（toEqual 语义）

const cyc = { name: 'x' }; cyc.self = cyc;
const cyc2 = { name: 'x' }; cyc2.self = cyc2;
expect(deepEqual(cyc, cyc2)).toBe(true);                   // 循环引用不爆栈
class A { } expect(deepEqual(new A(), {})).toBe(false);    // 原型不同
```
**评分点**：
- Object.is 短路（NaN 相等、-0 区分）是基础分。
- WeakMap 配对打破循环引用（JSON.stringify 方案此处直接扣分）。
- 原型一致性 + Date 特判 + Symbol 键考虑。
- 能区分 toEqual 与 toStrictEqual（class/undefined 键差异）。
