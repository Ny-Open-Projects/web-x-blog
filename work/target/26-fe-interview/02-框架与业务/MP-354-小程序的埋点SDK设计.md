---
title: [MP-354] 小程序埋点 SDK 设计：通道与生命周期适配
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 可观测]
type: 面试题
---

## MP-354：小程序埋点 SDK 设计：通道与生命周期适配

**答**：
- SDK 分层：采集（自动 PV/点击/曝光声明式）、缓冲（队列 + onHide/pagehide flush——小程序无 pagehide 用 onHide + wx.onAppHide）、传输（wx.request 批量——sendBeacon 不存在）
- 自动 PV 的接入：页面工厂（MP-352）里 onShow 记录时间戳 + 路由——「进入/停留/离开」三事件自动采集
- 曝光声明式：组件 Behavior（MP-307 模式）+ IO observer（createIntersectionObserver）——slot 标记触发
- 通道差异：小程序 request 需要域名白名单——埋点域名也要配置；「退出时机丢失」的兜底（onAppHide 强制 flush + storage 落盘恢复）
- 深水点：多端埋点一致性——同一 schema（FRP-334 协议）双端接入——「事件命名/字段对齐」是双端埋点的核心治理

```javascript
// SDK 缓冲: 小程序版 flush 时机
App({
  onHide() { tracker.flush(true); },               // 切后台强制上报
  onError() { tracker.flush(true); },
});
// storage 兜底: flush 失败落盘, 下次启动恢复
tracker.onFlushFail((batch) => wx.setStorageSync('track:pending', batch));
App({ onLaunch() { const p = wx.getStorageSync('track:pending'); p && tracker.requeue(p); } });
// 自动 PV: createPage 工厂注入 onShow → track('pv', { route, scene })
```
