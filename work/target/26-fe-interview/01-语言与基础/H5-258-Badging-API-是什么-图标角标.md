---
title: [H5-258] Badging API 是什么：图标角标
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-258：Badging API 是什么：图标角标

**答**：
- Badging：给已安装 PWA 的桌面/任务栏图标显示数字角标或圆点，如未读消息数
- API 极简：`navigator.setAppBadge(3)` 设置数字、`clearAppBadge()` 清除
- 支持面：Chromium 系桌面端支持好，iOS Safari 17+ 支持；未支持平台调用静默失败（不抛错）
- 使用纪律：角标数必须真实（用户点开后立即清除），滥用虚假角标唤起用户是骚扰行为
- 联动场景：WS 推送未读计数 → 页面可见时更新角标；页面不可见时靠 push 通知 + SW 更新角标

```javascript
function syncBadge(unread) {
  if ('setAppBadge' in navigator) {
    unread > 0 ? navigator.setAppBadge(unread) : navigator.clearAppBadge();
  }
}
ws.onmessage = (e) => { const m = JSON.parse(e.data); m.type === 'UNREAD' && syncBadge(m.count); };
```
