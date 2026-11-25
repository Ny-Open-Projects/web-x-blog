---
title: [RBL-105] 笔试：手写懒评估值对象（Lazy Vc 模拟）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-105：笔试：手写懒评估值对象（Lazy Vc 模拟）
**答**：实现 lazy(factory)：1) 返回 { get } ——首次 get 才执行 factory，之后返回缓存值；2) 支持链式 map(fn)：延迟到 get 时才逐级求值（中间不产生中间值对象）；3) 多处引用同一 lazy 实例只算一次（单飞：并发 get 合并）；4) 失效 invalidate() 后重新惰性求值；5) 统计 evaluations 次数验证惰性。

```javascript
function lazy(factory) {
  let value, done = false, promise = null;
  const state = { evaluations: 0 };

  const cell = {
    state,
    async get() {
      if (done) return value;
      if (!promise) {                    // 单飞：并发 get 共享同一次求值
        promise = (async () => {
          state.evaluations++;
          value = await factory();
          done = true;
          promise = null;
          return value;
        })();
      }
      return promise;
    },
    map(fn) {
      // 链式惰性：本 cell 之上包一层新 cell，get 时才级联求值
      return lazy(async () => fn(await cell.get()));
    },
    invalidate() { done = false; value = undefined; },
  };
  return cell;
}
module.exports = { lazy };

// 验证
// const a = lazy(() => { console.log('compute a'); return 42; });
// const b = a.map(x => x * 2);
// // 此处未打印 —— 完全惰性
// await b.get(); // 打印 compute a，得 84
// await b.get(); // 不再打印（缓存）
// a.invalidate(); b.get(); // 重算
```
**评分点**：
- 首次 get 才求值 + 缓存（惰性语义）。
- 单飞：并发 get 合并为一次 factory 执行（promise 复用）。
- map 链式惰性（不产生中间求值）。
- invalidate 重置状态。
- 能类比 turbo-tasks 的 Vc<T>：值 + 惰性 + 可失效正是该抽象，evaluations 计数验证"未消费不计算"。
