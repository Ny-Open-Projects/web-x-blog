---
title: [HW-178] 手写后台任务标记——页面离开前的任务续跑声明（sendBeacon + Background Sync 分级）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：用户离开时"任务还能不能跑完"的分级：① 同步快任务（<1s）——页面 hidden 前直接跑完（visibilitychange 内同步逻辑）；② 短任务（<10s）——sendBeacon/fetch keepalive 移交给浏览器排队续传（PER-252）；③ 长任务（>10s）——Background Sync（SW sync 事件，浏览器保证有网时唤醒，页面可关闭，PER-330）；④ 不可续任务——明确提示用户（"离开将中断导出"确认框）。

```javascript
const taskLevels = {
  sync(fn) { return fn(); },                              // <1s：hidden 内同步完成
  short(url, body, key) {                                  // <10s：浏览器排队续传
    const ok = navigator.sendBeacon?.(url, new Blob([JSON.stringify({ ...body, key })], { type: 'application/json' }));
    if (!ok) fetch(url, { method: 'POST', body: JSON.stringify(body), keepalive: true });
    return 'beacon';
  },
  async long(tag, enqueue) {                               // >10s：SW sync（页面可关）
    await enqueue();                                       // 任务入 IDB（PER-330 outbox）
    const reg = await navigator.serviceWorker?.ready;
    await reg.sync?.register(tag);                         // 浏览器保证有网时唤醒 SW 重放
    return 'background-sync';
  },
  requiresStay(fn) {                                       // 不可续：离开前确认
    addEventListener('beforeunload', (e) => { e.preventDefault(); e.returnValue = ''; });
    return fn();
  },
};
// 分级决策表：
// <1s    → 同步跑完（统计上报）
// <10s   → beacon/keepalive（埋点批量 flush）
// >10s   → Background Sync（导出后的上报/离线写操作）
// 不可续 → beforeunload 确认（长导出/长编辑会话）
// 兼容性：Background Sync 仅 Chrome 系 —— 降级链：sync → 页面 online 事件重放（PER-330）
```

**评分点**：
- 四级任务分级（同步/beacon/Sync/确认）与时间阈值语义——本题核心。
- Background Sync 的"页面可关浏览器保证唤醒"能力与降级链。
- 不可续任务的 beforeunload 明示（欺骗用户"离开没事"是最差实践）。
- 幂等键贯穿（重放安全）。
