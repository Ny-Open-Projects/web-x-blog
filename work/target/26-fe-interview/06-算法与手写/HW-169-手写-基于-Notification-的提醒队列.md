---
title: [HW-169] 手写通知提醒队列——Notification 权限状态机、页面可见性分流（前台 toast/后台推送）与去重
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：提醒分流：页面可见 → 应用内 toast（不打扰）；页面隐藏 → 系统通知（Notification，需权限状态机：default 引导授权/denied 静默跳过/granted 发送）；去重（同 key 提醒 5 分钟内只发一次）；SW 场景用 showNotification（页面关闭也能送达）。

```javascript
class NotifyHub {
  #seen = new Map();                                    // key -> lastAt（去重窗口）
  constructor({ dedupeMs = 5 * 60000 } = {}) { this.dedupeMs = dedupeMs; }
  async push(key, { title, body, tag = key } = {}) {
    const last = this.#seen.get(key);
    if (last && Date.now() - last < this.dedupeMs) return 'deduped';
    this.#seen.set(key, Date.now());
    if (document.visibilityState === 'visible') {        // 前台：应用内 toast（不打扰）
      return showToast(title, body), 'toast';
    }
    if (!('Notification' in window)) return 'unsupported';
    if (Notification.permission === 'granted') {
      navigator.serviceWorker?.controller
        ? navigator.serviceWorker.controller.postMessage({ type: 'notify', title, body, tag })   // SW 送达
        : new Notification(title, { body, tag });        // tag 同 key：系统级去重合并
      return 'notification';
    }
    return Notification.permission === 'denied' ? 'denied' : 'need-permission';
  }
  async requestPermission() {                            // 授权引导：仅在用户上下文（点击）中调用
    if (Notification.permission === 'default') {
      const r = await Notification.requestPermission();
      return r;                                          // granted/denied
    }
    return Notification.permission;
  }
}
// 权限状态机：default（引导，必须在用户手势中请求）/ granted（发）/ denied（静默降级 toast-only）
// 去重双层：应用层 key 窗口 + Notification tag（系统合并同 tag 通知）
// 后台送达优先 SW showNotification（页面关闭仍可达）—— 直接 new Notification 只在页面存活时有效
```

**评分点**：
- 可见性分流（前台 toast / 后台系统通知）的打扰最小化语义。
- 权限状态机（default 手势内引导 / denied 静默降级）——本题核心。
- 双层去重（应用 key 窗口 + Notification tag）。
- SW showNotification 的后台送达优先级。
