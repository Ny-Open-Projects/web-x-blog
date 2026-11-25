---
title: [PER-994] 点击劫持的完整防御：frame-ancestors 与 JS 兜底
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-994：点击劫持的完整防御：frame-ancestors 与 JS 兜底

**答**：
- 原理：攻击页用透明 iframe 叠加诱导点击，受害者实际操作的是被嵌入的目标页。
- 主防线：CSP frame-ancestors none/self/白名单（现代浏览器生效，替代 X-Frame-Options）。
- 兜底：JS 断框脚本（top !== self 时跳出）——能被 sandbox 的 allow-top-navigation 限制，只能作补充。
- 深水：敏感操作再加二次确认（确认弹窗展示真实目标域名），防止其他 UI 重定向类攻击（如界面伪装 clickjacking 变体）。

```javascript
// 服务端
app.use((req, res, next) => {
  res.setHeader('Content-Security-Policy', "frame-ancestors 'self'");
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');   // 旧浏览器兜底
  next();
});
// 客户端兜底
if (self !== top) {
  try { top.location = self.location; }             // 跳出
  catch { document.body.style.display = 'none';     // 禁止操作
          report({ type: 'framing-detected', ref: document.referrer }); }
}
```
