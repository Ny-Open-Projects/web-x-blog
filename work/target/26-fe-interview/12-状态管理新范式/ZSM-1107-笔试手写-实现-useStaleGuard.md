---
title: [1107] 笔试手写：实现 useStaleGuard
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Hook]
type: 笔试题
---

## 1107：笔试手写：实现 useStaleGuard

**答**：实现 useStaleGuard(data, { maxAgeMs, onBlock })：data 为 { value, fetchedAt }。 Hook 返回 { stale, guarded }：stale = Date.now() - fetchedAt > maxAgeMs；stale 时 guarded 包装器拦截「基于旧数据的写操作」——调用 guarded(fn) 时若 stale 则不执行并触发 onBlock({ ageMs })，否则执行 fn。笔试实现为纯函数工厂 createStaleGuard。

```js
function createStaleGuard(maxAgeMs, onBlock) {
  let current = { value: null, fetchedAt: 0 };
  return {
    set(data) { current = data; },
    isStale(now = Date.now()) {
      return now - current.fetchedAt > maxAgeMs;
    },
    guarded(fn) {
      const ageMs = Date.now() - current.fetchedAt;
      if (this.isStale()) {
        onBlock?.({ ageMs }); // 旧数据禁写：提示用户先刷新
        return { executed: false, ageMs };
      }
      return { executed: true, result: fn(current.value) };
    },
  };
}
```

**评分点**：
- stale 判定与写拦截分离（读不受限、写被门禁）
- onBlock 回调携带 ageMs（UI 可提示「数据已 5 分钟未刷新」）
- guarded 返回结构化结果（执行与否可观测）
- 能讨论：适用边界——展示类读永不拦、金额/提交类写必须拦
