---
title: [JS-388] 笔试：手写 Promise.any 与带超时的竞速
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-388：笔试：手写 Promise.any 与带超时的竞速

**答**：实现：① `promiseAny(iterable)`：首个 fulfilled 即 resolve；全部失败时 reject AggregateError（errors 按输入顺序）；② `timeoutRace(p, ms)`：p 与超时竞速，超时 reject TimeoutError 并尝试让 p 中断（可选 onTimeout 回调清理）；③ 空输入 any reject AggregateError（空 errors）。写出实现。

```javascript
function promiseAny(iterable) {
  return new Promise((resolve, reject) => {
    const items = [...iterable];
    const errors = new Array(items.length);
    let pending = items.length;
    if (!pending) return reject(new AggregateError([], 'All promises were rejected'));
    items.forEach((it, i) => {
      Promise.resolve(it).then(resolve, (e) => {       // 首个成功直接 resolve
        errors[i] = e;
        if (--pending === 0)
          reject(new AggregateError(errors, 'All promises were rejected'));
      });
    });
  });
}

class TimeoutError extends Error { constructor() { super('operation timed out'); this.name = 'TimeoutError'; } }

function timeoutRace(p, ms, onTimeout) {
  let timer;
  const t = new Promise((_, reject) => {
    timer = setTimeout(() => { onTimeout?.(); reject(new TimeoutError()); }, ms);
  });
  return Promise.race([p, t]).finally(() => clearTimeout(timer));
}

// 用法: 多源容灾
const data = await promiseAny([fetchA(), fetchB(), fetchC()]).catch(e => {
  if (e instanceof AggregateError) console.error(e.errors);  // 全部失败
});
```

**评分点**：
- any 的「首个成功」分发与计数器收集全部错误
- AggregateError 按「输入顺序」收集错误（索引填充）
- 超时竞速的定时器清理（finally）
- 空输入语义（any 空即 reject）
