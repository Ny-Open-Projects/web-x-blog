---
title: [PER-986] Early Hints（103）如何缩短关键资源发现时间
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-986：Early Hints（103）如何缩短关键资源发现时间

**答**：
- 问题：服务器生成动态 HTML 慢（如 500ms），期间浏览器只能干等，CSS/JS 的链接藏在 HTML 里发现不了。
- Early Hints：服务器先发 103 响应携带 Link 头（preload/preconnect），浏览器提前发起关键资源请求，HTML 到达后再正常处理。
- 收益：TTFB 期间完成 DNS/TLS/部分下载，LCP 资源更早就绪；对 SSR 重页面收益最大。
- 配合：CDN 支持 103 透传；注意不要 hints 与 HTML 实际内容冲突（preload 未使用资源会浪费带宽并触发告警）。

```javascript
// Node 服务器发出 Early Hints
app.get('/product/:id', async (req, res) => {
  res.writeHead(103, {
    Link: '</css/critical.css>; rel=preload; as=style,' +
          '</img/hero.avif>; rel=preload; as=image; fetchpriority=high,' +
          '<//cdn.example.com>; rel=preconnect',
  });
  const html = await renderProduct(req.params.id);   // 慢的动态渲染
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end(html);
});
// 收益验证：Network 面板中 critical.css 应早于 HTML 完成时间开始
```
