---
title: [PER-1100] 如何防御"界面伪装"（UI Redressing）之外的会话级攻击
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1100：如何防御"界面伪装"（UI Redressing）之外的会话级攻击

**答**：
- 会话固定（登录重签）、会话劫持（XSS 窃取/网络窃听——HTTPS 解决）、跨标签会话滥用。
- 会话绑定：会话绑定设备指纹 + UA，异常变化要求重认证；多标签页操作日志合并审计。
- 闲置超时：敏感应用 idle 超时自动登出（前端提醒 + 服务端强制过期）。
- 登出完备性：单点登出（SSO 广播）、本地状态清理、token 服务端吊销（1098）。

```javascript
// 闲置超时管理
let lastActive = Date.now();
['click', 'keydown', 'mousemove'].forEach(e =>
  addEventListener(e, () => lastActive = Date.now(), { passive: true }));
setInterval(() => {
  const idle = Date.now() - lastActive;
  if (idle > 25 * 60_000) warnLogout();              // 25 分钟警告
  if (idle > 30 * 60_000) forceLogout();             // 30 分钟强制登出
}, 30_000);
function forceLogout() {
  clearLocalState();
  fetch('/auth/logout', { method: 'POST', credentials: 'include' });
  location.href = '/login?reason=idle';
}
```
