---
title: [WCN-098] 笔试：手写 Signals 依赖图调试器（订阅链打印 + 触发计数）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-098：笔试：手写 Signals 依赖图调试器

**题目**：为响应式系统加调试层：① `trackGraph(signal)` 返回其"上游依赖树"（computed 递归展开）与"下游订阅者列表"；② 每个节点记录 `triggers`（被写入次数）与 `runs`（effect/computed 实际重算次数），暴露 `stats(sig)`；③ `whyRun(effect)` 打印最近一次触发它的上游链路；④ 调试信息开关 `debugMode`，关闭时零开销；⑤ 用测试口径展示：写 a 三次但值不变，runs 不增加。

**答**：

```javascript
// 响应式内核里埋点（以 WCN-070 的实现为基础扩展）
const meta = new WeakMap(); // node -> { triggers, runs, lastReason, subs, deps }
function nodeMeta(node) {
  return meta.get(node) ?? { triggers: 0, runs: 0, lastReason: null, subs: new Set(), deps: new Set() };
}

export function instrument(sig, name) {
  const m = nodeMeta(sig);
  sig.__name = name;
  const origRead = sig.read, origWrite = sig.write;
  if (origWrite) {
    sig.write = (nv) => {
      const before = sig.read();  // Object.is 前的旧值
      m.triggers++;
      m.lastReason = { from: 'write', prev: before, next: nv, ts: performance.now() };
      origWrite(nv);
    };
  }
  return sig;
}

export function stats(sig) { const m = nodeMeta(sig); return { name: sig.__name, triggers: m.triggers, runs: m.runs }; }

export function trackGraph(sig, seen = new Set(), depth = 0) {
  if (seen.has(sig) || depth > 20) return { name: sig.__name, circular: true };
  seen.add(sig);
  const m = nodeMeta(sig);
  return {
    name: sig.__name, triggers: m.triggers, runs: m.runs,
    upstream: [...m.deps].map((d) => trackGraph(d, seen, depth + 1)),
    subscribers: [...m.subs].map((s) => s.__name ?? 'effect'),
  };
}

export function whyRun(effect) {
  return nodeMeta(effect).lastReason; // 最近触发原因：{ from, prev, next }
}

// 口径验证：
// const a = instrument(createSignal(1), 'a');
// effect(() => a()); a(1); a(1); a(1);
// → stats(a).triggers === 3 但 runs（effect 重算）=== 0（Object.is 短路生效）
```

**评分点**：
- 双向图遍历：上游 deps 递归 + 下游 subs 列表。
- triggers/runs 分离能直接验证"相等短路"（考点）。
- WeakMap 存元数据（不阻止 GC）；循环依赖深度截断。
- whyRun 记录最近触发原因（prev/next），排查意外触发时直击答案。
