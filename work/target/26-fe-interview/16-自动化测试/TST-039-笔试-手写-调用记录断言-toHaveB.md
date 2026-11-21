---
title: [TST-039] 笔试：手写 spy 断言 toHaveBeenCalledWith / toHaveBeenCalledTimes
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-039：笔试：手写 spy 断言 toHaveBeenCalledWith / toHaveBeenCalledTimes
**答**：
- 需求：实现 `createSpy(impl?)`：包装原函数，记录每次调用参数与返回值；提供断言 `toHaveBeenCalledWith(...args)`（任意一次匹配即可）、`toHaveBeenCalledTimes(n)`、`toHaveBeenCalledWithLast`。
- 核心：闭包数组存 calls；参数比较用「逐项 Object.is + 对象 toEqual 兜底」；未匹配时错误信息要打印实际调用列表（可调试性）。
- 边界：原实现抛异常也要记录（calls 已 push）；断言不匹配抛 Error 而非返回 false（与 expect 体系一致）。

```javascript
function isSameArgs(a, b) {
  return a.length === b.length &&
    a.every((v, i) => typeof v === 'object' && v !== null
      ? JSON.stringify(v) === JSON.stringify(b[i])
      : Object.is(v, b[i]));
}

function createSpy(impl = () => undefined) {
  const calls = [], results = [];
  const fn = function (...args) {
    calls.push(args);
    try {
      const r = impl.apply(this, args);
      results.push({ type: 'return', value: r });
      return r;
    } catch (e) {
      results.push({ type: 'throw', value: e });
      throw e;
    }
  };
  fn.calls = calls;
  fn.toHaveBeenCalledTimes = (n) => {
    if (calls.length !== n) throw new Error(`expected ${n} calls, got ${calls.length}`);
  };
  fn.toHaveBeenCalledWith = (...args) => {
    if (!calls.some((c) => isSameArgs(c, args)))
      throw new Error(`not called with ${JSON.stringify(args)}\nactual: ${JSON.stringify(calls)}`);
  };
  fn.toHaveBeenCalledWithLast = (...args) => {
    if (!calls.length || !isSameArgs(calls.at(-1), args)) throw new Error('last call mismatch');
  };
  return fn;
}

// ---- 用法 ----
const onPay = createSpy((orderId) => `paid:${orderId}`);
onPay('A1'); onPay('B2', { amount: 100 });
onPay.toHaveBeenCalledTimes(2);
onPay.toHaveBeenCalledWith('A1');
onPay.toHaveBeenCalledWith('B2', { amount: 100 });
onPay.toHaveBeenCalledWithLast('B2', { amount: 100 });
try { onPay.toHaveBeenCalledWith('X'); } catch (e) { console.log(e.message); } // 带实际调用列表
```
**评分点**：
- calls/results 双记录，抛异常也留痕。
- 参数匹配覆盖普通值（Object.is）与对象（深度比较）。
- 失败信息包含实际调用列表（可调试性是加分项）。
- 知道 Jest/Vitest 还记录 this/返回顺序（instances/results）。
