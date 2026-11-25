---
title: [MP-380] 笔试：手写埋点 SDK（flush 时机 + 恢复）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## MP-380：笔试：手写埋点 SDK

**答**：实现 `createTracker({ url })`：① 队列（满 20/定时 15s 双触发）+ 上限 500 丢最旧；② flush 时机全覆盖：定时、满量、App onHide、onError——「小程序无 pagehide」的时机场枚举；③ 失败落盘（storage 恢复——下次启动 requeue）；④ 上报通道（wx.request POST + keepalive 不可用——「退出即丢」的现实与缓解）；⑤ 丢弃计数入下一批。写出实现。

```javascript
export function createTracker({ url, maxSize = 500, flushMs = 15000 } = {}) {
  const q = []; let dropped = 0, flushing = false;
  function track(event) {
    if (q.length >= maxSize) { q.shift(); dropped++; }
    q.push({ ...event, t: Date.now(), seq: seq++ });
    if (q.length >= 20) flush();
  }
  function flush(urgent = false) {
    if (!q.length || flushing) return;
    flushing = true;
    const batch = { events: q.splice(0), dropped };
    dropped = 0;
    wx.request({
      url, method: 'POST', data: batch,
      fail: () => {                                   // 失败落盘恢复
        const prev = wx.getStorageSync('track:pending') || [];
        wx.setStorageSync('track:pending', [...prev, batch]);
      },
      complete: () => { flushing = false; },
    });
  }
  function requeue() {
    const prev = wx.getStorageSync('track:pending');
    if (prev?.length) { wx.removeStorageSync('track:pending'); q.push(...prev.flat()); }
  }
  setInterval(flush, flushMs);                        // 定时
  return { track, flush, requeue };
}
// App 接入:
App({
  onLaunch() { getApp().tracker.requeue(); },         // 启动恢复
  onHide() { tracker.flush(true); },                  // 切后台 flush(无 pagehide)
  onError() { tracker.flush(true); },
});
// 现实: 小程序被杀时未 flush 的数据丢失 → onHide flush + 高频 flush 降低丢失窗口
```

**评分点**：
- 小程序 flush 时机场枚举（无 pagehide——onHide/onError 替代）
- 失败落盘 + 启动 requeue（恢复链）
- 上限丢最旧 + 丢弃计数
- 「退出即丢」的现实认知与缓解策略
