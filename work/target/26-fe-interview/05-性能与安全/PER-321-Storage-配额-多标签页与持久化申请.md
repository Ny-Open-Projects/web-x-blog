---
title: [PER-321] navigator.storage.persist 什么时候该申请？多标签页共享配额如何协同？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-321：navigator.storage.persist 什么时候该申请？多标签页共享配额如何协同？

**答**：
- 申请时机：persist 不增加配额，只保证"不被整源淘汰"。该申请的场景——离线应用核心数据（离线包/草稿/本地优先数据库）；不该申请的——普通 HTTP 缓存镜像、可再生的 CDN 资源缓存（被淘汰也无损）。时机上"用户表达了依赖"（开了离线模式、添加到主屏、登录）后申请，成功率高（Chrome 按站点参与度信号判定）。
- persisted() 先查已授予；重复申请无意义。授予后仍要做用量自账——persist 只防淘汰，不防自己写爆。
- 多标签页协同：同源配额全局共享，多个标签页同时写 IndexedDB 会竞速。要点：① 用 Web Locks API 互斥关键写入段（`navigator.locks.request(key, cb)`）；② "主标签页"机制——BroadcastChannel 选主（最早会话做清理任务），避免多页同时触发 LRU 清理互相误删；③ 跨页通知配额事件（一个页面触发降级，广播其他页停写）。

```javascript
// persist 申请：带用户意图时机
async function maybePersist() {
  if (await navigator.storage.persisted?.()) return true;
  const granted = await navigator.storage.persist?.();
  return granted ?? false;      // false 则数据可能被配额压力淘汰，UI 提示用户
}

// 多标签页选主 + 互斥清理
const bc = new BroadcastChannel('storage-coord');
async function electAndClean() {
  const lock = await navigator.locks.request('cleanup-leader', { ifAvailable: true }, async (l) => {
    if (!l) return false;                       // 已有主，跳过
    bc.postMessage({ type: 'leader-elected' });
    await cleanupLRU();                         // 只有主页面做清理
    bc.postMessage({ type: 'cleanup-done', freedMB });
    return true;
  });
  bc.onmessage = ({ data }) => {                // 收到降级广播的其他页面停写
    if (data.type === 'quota-pressure') writePaused = true;
  };
}
```
