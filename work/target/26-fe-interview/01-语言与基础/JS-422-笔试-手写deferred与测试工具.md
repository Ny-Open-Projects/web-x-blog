---
title: [JS-422] 笔试：手写 deferred 工具与测试桩
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-422：笔试：手写 deferred 工具与测试桩

**答**：实现：① `deferred()`：返回 { promise, resolve, reject, status }——status 实时反映 pending/fulfilled/rejected；② `deferredAll(n)`：批量管理 n 个 deferred（`get(i)`、`resolveAll(v)`、`rejectOne(i, e)`）——测试中按任意顺序结算用；③ status 通过 Promise 不可直接同步读取的限制——用 then 注册更新；④ promise 完成后重复 resolve 忽略。写出实现。

```javascript
function deferred() {
  let resolve, reject;
  const p = new Promise((res, rej) => { resolve = res; reject = rej; });
  const d = { promise: p, resolve, reject, status: 'pending' };
  p.then(
    (v) => { d.status = 'fulfilled'; d.value = v; },
    (e) => { d.status = 'rejected'; d.reason = e; });
  return d;
}

function deferredAll(n) {
  const ds = Array.from({ length: n }, deferred);
  return {
    get: (i) => ds[i],
    all: () => Promise.all(ds.map(d => d.promise)),
    resolveAll: (v) => ds.forEach(d => d.resolve(v)),
    resolveOne: (i, v) => ds[i].resolve(v),
    rejectOne: (i, e) => ds[i].reject(e),
    get statusList() { return ds.map(d => d.status); },
  };
}

// 测试用法: 模拟旧请求后到
it('竞态: 旧响应不覆盖', async () => {
  const d = deferredAll(2);
  const fetchMock = vi.fn()
    .mockReturnValueOnce(d.get(0).promise)   // 请求1(慢)
    .mockReturnValueOnce(d.get(1).promise);  // 请求2(快)
  const r1 = search('a', fetchMock);
  const r2 = search('ab', fetchMock);
  d.resolveOne(1, ['ab']);                   // 先结算快的
  d.resolveOne(0, ['a']);                    // 旧的后到
  await Promise.all([r1, r2]);
  expect(rendered).toEqual(['ab']);
});
```

**评分点**：
- deferred 三件套（promise + resolve/reject 外提）
- status 用 then 注册同步更新（Promise 状态不可直接读的绕行）
- deferredAll 批量管理按任意顺序结算
- 重复 resolve 被引擎忽略的语义（无需手动防）
