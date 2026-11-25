---
title: [TST-404] 笔试：手写 vi.fn 风格的 mock 函数（记录调用/可设返回/可断言）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-404：笔试：手写 vi.fn 风格的 mock 函数（记录调用/可设返回/可断言）。
**题目**：`mockFn`：记录每次调用参数与 this；可 `mockReturnValue/mockImplementation`；提供 `calls` 与 `calledWith(...args)` 断言；`mockReset` 清空。

```javascript
export function fn(impl) {
  const state = { calls: [], results: [], impl: impl ?? (() => undefined) };
  const f = function (...args) {
    state.calls.push(args);
    try { const r = state.impl.apply(this, args); state.results.push({ ok: true, r }); return r; }
    catch (e) { state.results.push({ ok: false, e }); throw e; }
  };
  f.calls = state.calls;
  f.mockReturnValue = (v) => { state.impl = () => v; return f; };
  f.calledWith = (...exp) => state.calls.some(c => JSON.stringify(c) === JSON.stringify(exp));
  f.mockReset = () => { state.calls.length = 0; state.impl = impl ?? (() => undefined); };
  return f;
}
const spy = fn((x) => x * 2);
spy(3); spy(4);
console.log(spy.calls);            // [[3],[4]]
console.log(spy.calledWith(3));    // true

```

**评分点**：
- 调用记录（参数数组 + 返回值 + 异常）。
- 实现切换：显式设置优先，未设置返回 undefined。
- calledWith 语义：任意一次调用匹配即可。
- mockReset 同时清记录与实现。
