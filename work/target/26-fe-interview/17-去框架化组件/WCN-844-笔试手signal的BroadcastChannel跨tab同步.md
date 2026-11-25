---
title: [WCN-844] 笔试：手写 signal 的「结构化克隆 + BroadcastChannel」跨 tab 同步
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-844：笔试：手写 signal 的「结构化克隆 + BroadcastChannel」跨 tab 同步

**题目**：实现 `createSyncedSignal(key, initial)`，在普通 signal 基础上用 `BroadcastChannel` 实现同源多 tab 同步。要求：① 本地 set 时广播 message（含 key、value、唯一 tabId、递增 seq、时间戳）；② 收到消息时忽略自己发出的（按 tabId），只应用 key 匹配的值；③ 用「最后写入者胜」（seq 更大或时间戳更新）处理并发；④ 提供 `destroy()` 关闭 channel 并清理；⑤ 当 BroadcastChannel 不可用时降级到 localStorage 的 storage 事件。边界：结构化克隆不能序列化函数/DOM，set 时若值不可克隆要能降级或报错提示。

**答**：

```javascript
function createSyncedSignal(key, initial, { channelName = 'signals' } = {}) {
  let value = initial, seq = 0;
  const subs = new Set();
  const tabId = crypto.randomUUID?.() || String(Math.random());
  let lastTs = 0;
  const supportsBC = typeof BroadcastChannel !== 'undefined';
  const bc = supportsBC ? new BroadcastChannel(channelName) : null;

  function apply(v, from, s, ts) {
    if (from === tabId) return;                       // 忽略自己
    if (s < seq || (s === seq && ts <= lastTs)) return; // 过期消息
    seq = s; lastTs = ts; value = v;
    subs.forEach(fn => fn(value));
  }
  const api = {
    get() { return value; },
    set(v) {
      try { structuredClone(v); } catch { console.warn('值不可结构化克隆，同步可能失败'); }
      value = v; subs.forEach(fn => fn(value));       // 先更新本地
      const msg = { key, value: v, from: tabId, seq: ++seq, ts: Date.now() };
      if (bc) bc.postMessage(msg);
      else localStorage.setItem('__sig_' + key, JSON.stringify(msg)); // 降级
    },
    subscribe(fn) { subs.add(fn); return () => subs.delete(fn); },
    destroy() { bc?.close(); subs.clear(); },
  };
  if (bc) bc.onmessage = ({ data }) => { if (data.key === key) apply(data.value, data.from, data.seq, data.ts); };
  else window.addEventListener('storage', e => {
    if (e.key === '__sig_' + key && e.newValue) { const m = JSON.parse(e.newValue); apply(m.value, m.from, m.seq, m.ts); }
  });
  return api;
}
const s = createSyncedSignal('theme', 'light');
```

**评分点**：
- BroadcastChannel 广播含 tabId/seq/ts，收到时按 tabId 忽略自己，避免回声循环（核心）。
- 用 seq + 时间戳实现「最后写入者胜」，正确处理多 tab 并发写（正确性）。
- 提供 destroy 关闭 channel 并清理订阅，无内存泄漏（生命周期意识）。
- BroadcastChannel 不可用时降级到 localStorage storage 事件，并对不可克隆值做防御提示（兼容性与边界）。
