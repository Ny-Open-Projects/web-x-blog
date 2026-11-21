---
title: [HW-061] 手写可取消的 Promise（CancelToken）——组件卸载后回调不再执行
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-061：手写可取消的 Promise（CancelToken）——组件卸载后回调不再执行

**答**：Promise 本身不可取消，只能"包装"：CancelToken 持有一个 cancel 回调；包装函数 race 原 Promise 与"取消 Promise"，取消后 resolve 一个哨兵并让后续 then 不再触发。边界：取消后不执行用户回调、不吞原 Promise 的结果（资源本身照常结束）。

```javascript
class CancelToken {
  constructor() {
    this.cancelled = false;
    this._promise = new Promise((r) => (this._cancel = r));
  }
  cancel(reason = 'cancelled') { if (!this.cancelled) { this.cancelled = true; this._cancel({ __cancelled: true, reason }); } }
}

function withCancel(promise, token) {
  return new Promise((resolve, reject) => {
    const settled = (fn, val) => { if (!token.cancelled) fn(val); };   // 取消后不再走用户路径
    token._promise.then((v) => resolve(v));                            // 取消信号直接结算（调用方可识别 __cancelled）
    promise.then((v) => settled(resolve, v)).catch((e) => settled(reject, e));
  });
}

// 用法：组件卸载时 token.cancel()
const token = new CancelToken();
const p = withCancel(fetch('/api/list').then(r => r.json()), token);
p.then((data) => { if (data?.__cancelled) return; renderList(data); });
token.cancel();   // 之后即便 fetch 返回，renderList 也不会执行
```

**评分点**：
- 理解"Promise 不能被外部取消，只能包装竞速"这一本质。
- 取消后不再触发用户回调（settled 里查 token.cancelled），且取消信号本身可被调用方识别。
- 原 Promise 不被吞（fetch 照常完成，只是结果被忽略）。
- 多次 cancel 幂等。
