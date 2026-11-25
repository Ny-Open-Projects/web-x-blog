---
title: [WCN-732] 笔试：手写 signal 状态快照与回放器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-732：笔试：手写 signal 状态快照与回放器

**答**：
- 需求：实现 `createRecorder(initial)`，返回 `{ setValue(k,v), snapshot(), restore(snap), history() }`。每次 setValue 记录变更到历史；snapshot 返回当前状态深拷贝；restore 用快照恢复状态并记录一条恢复事件；history 返回变更列表。
- 要点：用 structuredClone 做快照；restore 也进历史保证可追溯；边界：非法 key、循环引用（structuredClone 可处理但函数不可克隆需跳过）。

```javascript
function createRecorder(initial) {
  let state = { ...initial };
  const historyLog = [];
  const safeClone = (o) => {
    try { return structuredClone(o); }
    catch { return JSON.parse(JSON.stringify(o)); }
  };
  return {
    setValue(k, v) {
      if (k == null) return;                       // 边界：非法 key
      historyLog.push({ type: 'set', key: k, value: safeClone(v), t: Date.now() });
      state[k] = v;
    },
    snapshot() { return safeClone(state); },
    restore(snap) {
      if (!snap || typeof snap !== 'object') return;
      historyLog.push({ type: 'restore', t: Date.now() });
      state = safeClone(snap);
    },
    history() { return safeClone(historyLog); },
  };
}
const r = createRecorder({ a: 1 });
r.setValue('b', 2); const s = r.snapshot(); r.setValue('b', 3); r.restore(s);
console.log(r.snapshot(), r.history().length);
```

**评分点**：
- snapshot 用深拷贝隔离，避免外部修改污染内部状态。
- restore 也记入 history，保证变更全程可追溯。
- setValue/restore 对非法输入有边界防御。
- 克隆失败（函数/循环引用）有降级策略，健壮性好。
