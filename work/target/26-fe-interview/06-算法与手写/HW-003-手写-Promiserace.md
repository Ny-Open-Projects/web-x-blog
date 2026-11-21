---
title: [HW-003] 手写 Promise.race
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-003：手写 Promise.race

**答**：
- 评分点：谁先落定（无论成功失败）谁决定最终状态；resolve 和 reject 都要传给同一个 then 的两个分支；非 Promise 值同样要 `Promise.resolve()` 包装；空数组边界：没有竞赛者则永远 pending（可作为考点反向提问「race 空数组会怎样」）；常与超时控制组合使用。

```javascript
// ===== 5 分钟速写版 =====
function promiseRace(promises) {
  return new Promise((resolve, reject) => {
    Array.from(promises).forEach(p => {
      // 成败都交给同一个出口，第一个落定的生效，后续调用无效（状态不可逆）
      Promise.resolve(p).then(resolve, reject);
    });
  });
}

// ===== 标准完整版（含边界处理）=====
function promiseRacePro(promises) {
  return new Promise((resolve, reject) => {
    if (promises === null || typeof promises[Symbol.iterator] !== 'function') {
      return reject(new TypeError('promises must be iterable'));
    }
    const list = Array.from(promises);
    let settled = false;
    if (list.length === 0) {
      // 边界说明：空数组没有任何竞赛者，与原生 Promise.race([]) 一致保持 pending
      // 生产中应配合外部超时兜底，这也是「race 空数组会怎样」的反向考点
      return;
    }
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        v => { if (!settled) { settled = true; resolve(v); } },
        e => { if (!settled) { settled = true; reject(e); } }
      );
    });
  });
}
// 典型组合：请求超时
// promiseRacePro([fetch(url), new Promise((_, rj) => setTimeout(() => rj(new Error('timeout')), 3000))])
```

---
