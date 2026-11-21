---
title: [PER-330] 离线写操作如何安全重放？Background Sync 与幂等设计要点？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-330：离线写操作如何安全重放？Background Sync 与幂等设计要点？

**答**：
- 写队列四要素：① 入队持久化——失败请求连体（URL/方法/体/幂等键）存 IndexedDB，页面关闭也不丢；② 幂等键——客户端生成（UUID）随请求发送，服务端按键去重（重放不会重复下单/点赞）；③ 重放时机——SW 的 `sync` 事件（Background Sync API，浏览器保证"有网时触发，即使页面已关闭"，Chrome 支持；Safari 不支持则退化为 visibilitychange/online 事件时页面内重放）；④ 顺序依赖——同实体的操作按序重放（队列分组），跨实体可并行。
- 冲突处理：重放时服务端可能已变（离线期间别人改了）——按业务定义策略：版本号检测冲突报错、服务端合并（最后写赢）、或强制覆盖前提示用户。离线时间越长冲突概率越大，UI 要有"同步失败需手动处理"清单。
- UI 联动：队列状态可见（"2 条操作待同步"），成功/失败逐条反馈。

```javascript
// SW：sync 触发重放
self.addEventListener('sync', (event) => {
  if (event.tag === 'outbox') event.waitUntil(replayOutbox());
});
async function replayOutbox() {
  const db = await openOutboxDB();
  const items = await db.getAll('outbox');                  // 按序
  for (const item of items) {
    try {
      const res = await fetch(item.url, { method: item.method,
        body: JSON.stringify({ ...item.body, idempotencyKey: item.key }),
        headers: { 'Idempotency-Key': item.key, 'Content-Type': 'application/json' } });
      if (res.ok || res.status === 409) await db.delete('outbox', item.key);  // 409=已处理（幂等命中）
      else if (res.status >= 500) break;                    // 服务端故障：停住等下次 sync
      else await db.put('failed', item);                    // 4xx：进失败清单人工处理
    } catch { break; }                                      // 还没网：等下次
  }
}
// 页面兜底（Safari 无 Background Sync）：
addEventListener('online', () => navigator.serviceWorker.controller?.postMessage({ type: 'replay' }));
```
