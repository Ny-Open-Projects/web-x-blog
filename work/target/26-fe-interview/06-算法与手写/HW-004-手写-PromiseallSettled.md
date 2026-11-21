---
title: [HW-004] 手写 Promise.allSettled
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-004：手写 Promise.allSettled

**答**：
- 评分点：**不会 fail-fast**，等全部落定；结果格式必须是 `{ status: 'fulfilled', value }` / `{ status: 'rejected', reason }`（注意字段名 value 与 reason 不同）；顺序保序；空数组 resolve `[]`；适合批量请求「部分失败不影响整体」的场景，是 all 的补集。

```javascript
// ===== 5 分钟速写版 =====
function promiseAllSettled(promises) {
  return new Promise(resolve => {
    const list = Array.from(promises);
    const results = [];
    let count = 0;
    if (list.length === 0) return resolve([]);
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        value => { results[i] = { status: 'fulfilled', value }; },
        reason => { results[i] = { status: 'rejected', reason }; }
      ).finally(() => { if (++count === list.length) resolve(results); });
    });
  });
}

// ===== 标准完整版（含边界处理）=====
function promiseAllSettledPro(promises) {
  return new Promise(resolve => {
    if (promises === null || typeof promises[Symbol.iterator] !== 'function') {
      throw new TypeError('promises must be iterable');
    }
    const list = Array.from(promises);
    const len = list.length;
    if (len === 0) return resolve([]);
    const results = new Array(len);
    let count = 0;
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        value => { results[i] = { status: 'fulfilled', value }; },
        reason => { results[i] = { status: 'rejected', reason }; }
      ).finally(() => {
        // 全部落定才 resolve，无论成功失败
        if (++count === len) resolve(results);
      });
    });
  });
}
// 业务用法：批量上报 / 多源数据聚合，失败项单独过滤
// const rs = await promiseAllSettledPro(tasks);
// const ok = rs.filter(r => r.status === 'fulfilled').map(r => r.value);
```

---
