---
title: [WCN-413] 笔试：实现主线程代理信号与 Worker 权威图的桥接。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-413：笔试：实现主线程代理信号与 Worker 权威图的桥接。
**答**：Worker 内持权威信号图；主线程 `proxySignal(id)`：读走本地缓存，写 postMessage；Worker 变更广播回来更新缓存（且不再回写，防回环）。

```javascript
// main.js
function proxySignal(id, worker, cache) {
  return {
    get value() { return cache.get(id); },
    set value(v) { cache.set(id, v); worker.postMessage({ type: 'set', id, v }); },  // 乐观
  };
}
worker.onmessage = ({ data }) => {
  if (data.type === 'change') cache.set(data.id, data.v);   // 不回写 → 无回环
};
// worker.js
self.onmessage = ({ data }) => { graph[data.id].set(data.v); };  // set 内广播 change

```

**评分点**：
- 消息协议：{type: 'set'|'change', id, v}。
- 主线程乐观写（本地立即更新 + 异步同步）。
- change 消息更新缓存但不回写（回环防护）。
- 延迟预算：写→广播往返 < 10ms（同源 Worker）。
