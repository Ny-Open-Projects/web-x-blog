---
title: [WCN-424] 笔试：computed 错误的恢复语义实现。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-424：笔试：computed 错误的恢复语义实现。
**题目**：computed 抛错：错误缓存（下次读取重算）；提供 `retry(node)` 手动重算；订阅者通过 try/catch 或 error 回调感知恢复。

```javascript
function safeComputed(fn) {
  const node = computed(fn);
  node.retry = () => { node.dirty = true; node.get(); };
  // 依赖写入时：node.dirty = true（错误态自动清除，下读重算）
  return node;
}
// effect 侧：
effect(() => { try { render(data.get()); } catch (e) { renderError(e); } });

```

**评分点**：
- 错误缓存字段（error/hasError）。
- 写入依赖任一信号 → 清除错误态（下读重算）。
- retry：强制重算（清 error）。
- 恢复传播：重算成功 → 订阅 effect 收到新值。
