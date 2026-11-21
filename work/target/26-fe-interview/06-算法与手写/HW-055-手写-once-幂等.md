---
title: [HW-055] 手写 once 幂等
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-055：手写 once 幂等

**答**：
- 评分点：第一次调用执行并**缓存结果**（包括返回值），之后所有调用直接返回第一次的结果——即使参数不同；this 取第一次调用时的 this（要说清这个约定，因为后续调用不执行）；错误处理策略要明确——**执行抛错后是否允许重试**（lodash once 不重试，可提供 retryOnError 选项是加分）；典型场景：支付按钮防重复提交、单例初始化、DOM 事件一次性回调；与 `Promise` 结合（幂等请求）是常见追问。

```javascript
// ===== 5 分钟速写版 =====
function once(fn) {
  let called = false;
  let result;
  return function (...args) {
    if (!called) {
      called = true;
      result = fn.apply(this, args); // 缓存首次结果
    }
    return result;
  };
}
// const pay = once(doPay); pay(100); pay(100) → 只扣一次款，两次拿到同一结果

// ===== 标准完整版（含边界处理）=====
function oncePro(fn, { retryOnError = false } = {}) {
  if (typeof fn !== 'function') throw new TypeError('fn must be a function');
  let called = false;
  let result;
  return function (...args) {
    if (called && !(result instanceof Error && retryOnError)) {
      return result; // 已执行且（无错或不可重试）→ 直接返回缓存
    }
    try {
      result = fn.apply(this, args); // this 取首次调用者
    } catch (e) {
      if (retryOnError) {
        called = false;       // 失败允许重试：重置状态
        throw e;
      }
      called = true;          // 不重试：错误结果也被「记住」，避免反复尝试副作用
      result = e;
      throw e;
    }
    called = true;
    return result;
  };
}
// 异步版：请求进行中再次调用要复用同一个 Promise（去重并发）
function onceAsync(fn) {
  let pending = null;
  return function (...args) {
    if (!pending) {
      pending = Promise.resolve().then(() => fn.apply(this, args))
        .finally(() => { pending = null; }); // 失败后允许下次重新发起
    }
    return pending; // 并发调用共享同一 Promise
  };
}
// 追问：once 与 lodash once 差异、与 memoize(fn)（key 固定为 undefined）的关系、
// 与幂等性的区别 —— once 是代码层拦截，幂等是服务端语义（同一操作多次执行结果一致）。
```

---
