---
title: [WEB-233] 点击劫持（Clickjacking）与 X-Frame-Options
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-233：点击劫持（Clickjacking）与 X-Frame-Options

**答**：
- 原理：攻击页用透明 iframe 叠在自己页面上，诱导用户点击看似无害的按钮，实际点的是 iframe 内目标站的「转账/删除」按钮——利用的是用户真实登录态。
- 服务端防御：`X-Frame-Options: DENY / SAMEORIGIN` 禁止被嵌入 iframe；现代用 CSP `frame-ancestors 'none'`，功能相同且更细（可指定白名单域名）。
- 前端兜底（历史方案）：`if (top !== self) top.location = self.location` 防嵌套，但攻击者可用 sandbox 属性拦住，只能算辅助。
- 交互层防御：敏感操作二次确认弹窗（弹窗不受 iframe 透明覆盖欺骗）+ SameSite cookie 使跨站 iframe 内请求不带登录态，从根上瓦解。

```nginx
# 双保险
add_header X-Frame-Options "DENY" always;
add_header Content-Security-Policy "frame-ancestors 'none'" always;

# 前端兜底（辅助）
if (window.top !== window.self) {
  try { window.top.location = window.self.location; }
  catch { document.body.innerHTML = '<h1>禁止嵌入访问</h1>'; }
}
```
