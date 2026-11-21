---
title: [WEB-153] 点击劫持怎么防？frame busters 为什么不够？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-153：点击劫持怎么防？frame busters 为什么不够？
**答**：
- 攻击：把目标页面塞进透明 iframe 叠在诱导按钮上，用户"点红包"实际点到"转账确认"。
- 服务端防御（首选）：X-Frame-Options 的 DENY/SAMEORIGIN，或 CSP 的 frame-ancestors（更现代，可精确到来源白名单）。
- JS frame buster（if top !== self 跳出）是历史方案：可被 iframe 的 sandbox、204 响应等绕过，只能做兜底。
- 需要被合作方嵌入的页面用 frame-ancestors https://partner.com 精确放行。
- 敏感操作再加二次确认（输入密码/验证码），把"点错"的损失拦住。

```html
<!-- 服务端配置是主力（X-Frame-Options 或 CSP frame-ancestors），这里是页面侧兜底 -->
<script>
  // 兜底 frame buster：被嵌套即尝试跳出（可能被 sandbox 阻止，故只作补充）
  if (window.top !== window.self) {
    try { window.top.location = window.self.location; }
    catch (e) { document.body.innerHTML = '<h1>请在原始站点打开本页</h1>'; }
  }
</script>
```
