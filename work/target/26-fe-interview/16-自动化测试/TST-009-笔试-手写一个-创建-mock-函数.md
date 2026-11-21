---
title: [TST-009] 笔试：手写一个 mock 函数（记录调用 + 注入实现）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-009：笔试：手写一个 mock 函数（记录调用 + 注入实现）
**答**：
- 需求：实现 `createMock(impl?)`，返回可调用函数，且具备 `mock.calls`（每次调用参数）、`mock.results`（返回值）、`mockReturnValue(v)`、`mockImplementation(fn)`、`mockReset()`。
- 核心：闭包保存「当前实现」与调用记录；每次调用 push 参数与结果；默认实现为 `() => undefined`。
- 边界：实现抛异常时 results 要记 `type: 'throw'` 与异常值；mockReset 恢复默认空实现而非删除。

```javascript
function createMock(impl) {
  const state = {
    impl: impl || (() => undefined),
    calls: [],
    results: [],
  };

  const fn = function (...args) {
    state.calls.push(args);            // 先记调用
    try {
      const value = state.impl.apply(this, args);
      state.results.push({ type: 'return', value });
      return value;
    } catch (e) {
      state.results.push({ type: 'throw', value: e });
      throw e;
    }
  };

  fn.mock = state;
  fn.mock.calls = state.calls;
  fn.mock.results = state.results;
  fn.mockReturnValue = (v) => { state.impl = () => v; return fn; };
  fn.mockImplementation = (f) => { state.impl = f; return fn; };
  fn.mockReset = () => { state.impl = () => undefined; state.calls.length = 0; state.results.length = 0; };
  fn.toHaveBeenCalledWith = (...expected) =>
    state.calls.some((c) => JSON.stringify(c) === JSON.stringify(expected));

  return fn;
}

// ---- 用法 ----
const mockFetch = createMock();
mockFetch.mockReturnValue(Promise.resolve('ok'));
console.log(mockFetch('/api'));                       // Promise 'ok'
console.log(mockFetch.mock.calls[0]);                 // ['/api']
console.log(mockFetch.toHaveBeenCalledWith('/api'));  // true

const boom = createMock(() => { throw new Error('x'); });
try { boom(); } catch {}
console.log(boom.mock.results[0].type);               // 'throw'
```
**评分点**：
- calls/results 记录完整（参数先记、结果区分 return/throw）。
- mockReturnValue/mockImplementation 链式返回 fn。
- mockReset 语义正确（回默认空实现并清记录）。
- 能说出真实 vi.fn 还支持 onceReturnValue/调用 this 记录等扩展。
