---
title: [TST-038] 笔试：手写断言库 expect（toBe / toEqual / toThrow / 链式 not）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-038：笔试：手写断言库 expect（toBe / toEqual / toThrow / 链式 not）
**答**：
- 需求：实现 `expect(x).toBe(y) / toEqual(y) / toThrow() / toBeCloseTo(y, n)`，支持 `.not` 取反，失败抛出带 diff 信息的 Error。
- 核心：断言函数统一 throw；`.not` 用代理或包装实现「结果取反」——把每个断言包一层 `invert(fn)`。
- 边界：toBe 用 Object.is（区分 +0/-0 和 NaN）；toEqual 深比较需处理数组/对象/null/Date；toBeCloseTo 用绝对差值 < 10^-n。

```javascript
function deepEqual(a, b) {
  if (Object.is(a, b)) return true;
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object') return false;
  if (Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) return false;
  return ka.every((k) => deepEqual(a[k], b[k]));
}

function expect(actual) {
  function make(fn, inverted) {
    return (...args) => {
      let ok = false, msg = '';
      try { ok = fn(...args); } catch (e) { ok = false; msg = e.message; }
      if (inverted ? ok : !ok) throw new Error(`assert failed: ${inverted ? 'not ' : ''}${msg || fn.name}`);
    };
  }
  const asserts = {
    toBe: make((exp) => Object.is(actual, exp) || (void 0, `expected ${actual} toBe ${exp}`, false), false),
    // 简化实现：toBe 直接写
  };
  const raw = {
    toBe(exp) { if (!Object.is(actual, exp)) throw new Error(`${actual} toBe ${exp}`); },
    toEqual(exp) { if (!deepEqual(actual, exp)) throw new Error(`${JSON.stringify(actual)} toEqual ${JSON.stringify(exp)}`); },
    toThrow(fn) {
      if (typeof actual !== 'function') throw new Error('toThrow target must be a function');
      try { actual(); } catch (e) { if (fn && !fn.test?.(e.message)) throw new Error(`message mismatch: ${e.message}`); return; }
      throw new Error('expected function to throw');
    },
    toBeCloseTo(exp, digits = 2) { if (Math.abs(actual - exp) >= Math.pow(10, -digits) / 2) throw new Error(`${actual} not close to ${exp}`); },
  };
  // not：包装每个断言，成功即失败、失败即通过
  const not = {};
  for (const [k, fn] of Object.entries(raw)) {
    not[k] = (...args) => {
      try { fn(...args); } catch { return; }          // 失败 → not 通过
      throw new Error(`expected NOT ${k}`);           // 成功 → not 失败
    };
  }
  return { ...raw, not };
}

// ---- 用法 ----
expect(1 + 1).toBe(2);
expect(NaN).toBe(NaN);                 // Object.is 使 NaN 通过
expect({ a: [1, 2] }).toEqual({ a: [1, 2] });
expect(() => { throw new Error('boom'); }).toThrow(/boom/);
expect(0.1 + 0.2).toBeCloseTo(0.3, 5);
expect(2).not.toBe(2);                 // 这行会抛错——not 取反生效
```
**评分点**：
- toBe 用 Object.is（NaN 案例是面试官落点）。
- deepEqual 递归 + 键数 + 原型一致性。
- not 通过「异常翻转」实现且链式可读。
- toThrow 支持正则并区分「没抛」与「抛错文案不符」。
