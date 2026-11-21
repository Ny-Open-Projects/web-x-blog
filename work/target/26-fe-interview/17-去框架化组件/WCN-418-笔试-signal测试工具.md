---
title: [WCN-418] 笔试：信号系统的确定性测试工具（同步 flush/断言执行序列）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-418：笔试：信号系统的确定性测试工具（同步 flush/断言执行序列）。
**题目**：`testScheduler()`：替换为同步 flush + 效果执行记录器。API：`flushAll()`、`log()` 返回 effect 执行顺序名数组。

```javascript
function testScheduler() {
  const log = [];
  let queue = new Set();
  configureScheduler({
    schedule: e => { queue.add(e); },
    flushAll() { const l = [...queue].sort((a, b) => a.depth - b.depth);
      queue.clear();
      for (const e of l) { e.dirty && e.run(); log.push(e.name); } },
  });
  return { flushAll, log: () => log };
}
// 测试：sig.set(1); s.flushAll(); expect(s.log()).toEqual(['render']);

```

**评分点**：
- 调度器注入（schedule 换同步）。
- 执行记录（effect.name 顺序）。
- 断言：写后 log 精确匹配（顺序敏感）。
- 恢复默认调度（测试隔离）。
