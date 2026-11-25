---
title: [AV-412] 协作内容的安全边界：输入净化与 XSS 防护
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-412：协作内容的安全边界：输入净化与 XSS 防护

**答**：
- 风险：协作内容是 UGC——富文本/文本注入可打其他协作者（存储型 XSS 的实时版）。
- 防线：渲染端 sanitize（1080 白名单）、emoji/图片 URL 白名单、Trusted Types（989）。
- 审计：恶意内容上报走审核队列（1094）。

```javascript
// 协作内容净化
function renderCollabText(text, sinks) {
  const clean = DOMPurify.sanitize(text, {
    ALLOWED_TAGS: ['b', 'i', 'br'],                    // 极简白名单
    ALLOWED_ATTR: [],
  });
  sinks.innerHTML = clean;
}
// 图片协作对象：src 必须走代理域名 + 白名单校验
function validateShapeImage(url) {
  return /^https:\/\/media\.example\.com\//.test(url) ? url : null;
}
```
