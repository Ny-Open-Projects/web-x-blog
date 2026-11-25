---
title: [PER-995] 前端如何防 SSRF 态势：客户端不可信与 URL 校验责任
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-995：前端如何防 SSRF 态势：客户端不可信与 URL 校验责任

**答**：
- SSRF 通常在后端，但前端是"入口守门员"：任何把用户输入 URL 传给后端代理抓取的功能（预览/导入/水印）都可能成为 SSRF 跳板。
- 前端防线：上传/提交前校验 URL 协议白名单（仅 http/https）、禁止内网域名特征（localhost/10./192.168./内网 hostname）。
- 责任声明：前端校验只是 UX 层，服务端必须独立做 DNS 解析后 IP 黑名单 + 重定向跟随之禁，不能信任前端。
- 案例：Markdown 图片预览、网页转 PDF、RSS 导入都是经典 SSRF 漏洞场景。

```javascript
// 前端 URL 预检（UX 层，非安全边界）
const BLOCK_HOST = /^(localhost|127\.|10\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|\[::1\])/;
const BLOCK_TLD = /\.(local|internal|lan|corp)$/i;
function precheckURL(url) {
  try {
    const u = new URL(url);
    if (!['http:', 'https:'].includes(u.protocol)) return '协议不允许';
    if (BLOCK_HOST.test(u.hostname) || BLOCK_TLD.test(u.hostname))
      return '疑似内网地址';
    return null;                                  // 仍需后端二次校验
  } catch { return 'URL 非法'; }
}
```
