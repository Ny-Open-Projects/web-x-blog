---
title: [PER-409] Service Worker 的内存与生命周期：SW 长驻的内存占用、事件时序与被杀恢复？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-409：Service Worker 的内存占用、事件时序与被杀恢复？

**答**:
- SW 生命周期：**没有页面在用就会被终止**（浏览器空闲杀掉 SW 进程，内存释放）——SW 不是常驻服务，不能假设全局状态跨事件存活。每次事件（fetch/sync/push）可能伴随 SW 冷启动（数十 ms），事件必须幂等、状态必须持久化到 IDB（内存变量在重启后消失）。
- 内存占用来源：SW 内的缓存引用、大响应的 clone、全局 Map——SW 被杀前这些都在其进程内；fetch handler 里 response.clone() 的两份内存要尽快消费（clone 后不读会滞留）。
- 被杀恢复要点：事件处理必须 `event.waitUntil(promise)` 包住异步（否则 SW 提前被杀、处理中断）；跨事件状态（重放队列游标、版本号）存 IDB；warm-up 成本——SW 冷启动影响第一个 fetch 的延迟，可接受但要知晓（关键资源可让页面直接 fetch 不走 SW）。
- 调试：chrome://serviceworker-internals 看运行状态；Application 面板强制 stop 验证"状态持久化"是否完备（杀掉 SW 后功能应自动恢复）。

```javascript
// SW：状态持久化 + waitUntil 纪律
let cacheCursor = 0;                    // ❌ 内存变量：SW 重启后丢失
async function initCursor() {           // ✔ 从 IDB 恢复
  cacheCursor = (await idbGet('sw-state', 'cursor')) ?? 0;
}
self.addEventListener('fetch', (event) => {
  event.waitUntil((async () => {        // 必须包住异步，否则 SW 被提前终止
    if (cacheCursor === null) await initCursor();
    // ... 缓存逻辑
  })());
});
// response.clone() 的双份内存：clone 后必须消费两者
const cached = res.clone();             // 一份给缓存
event.respondWith(res);                 // 一份给页面 —— 两份都会被消费，无滞留
// 验证：Application 面板 Stop → 再触发 fetch → 功能自动恢复（状态从 IDB 回来）
```
