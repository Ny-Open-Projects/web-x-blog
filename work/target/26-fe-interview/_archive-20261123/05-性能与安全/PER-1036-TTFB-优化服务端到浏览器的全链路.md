---
title: [PER-1036] TTFB 优化：服务端到浏览器的全链路提速
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1036：TTFB 优化：服务端到浏览器的全链路提速

**答**：
- TTFB = 重定向 + DNS + TLS + 请求排队 + 服务端处理 + 响应首字节传输；前端能控制的是"排队"与重定向，其余靠架构。
- 手段：边缘缓存 HTML（对匿名用户 s-maxage）、SSR 流式输出（尽早 flush 首屏骨架）、后端接口并行化与预计算、连接复用与 keepalive。
- 流式响应：HTML 分段传输让浏览器尽早开始解析（head 先到先渲染），配合 103 Early Hints 效果更佳。
- 度量：TTFB 拆分归因（1021 的 timing 分解），区分网络段与服务器段再治理。

```javascript
// 流式 SSR：尽早输出
app.get('/page', async (req, res) => {
  res.write('<!doctype html><head><link rel=stylesheet href=/c.css></head><body>');
  res.write('<div id=shell>骨架</div>');           // 先 flush 骨架
  const data = await heavyQuery(req);               // 慢数据后到
  res.end(`<script>window.__DATA__=${JSON.stringify(data)}</script>
    <div id=app>...</div>`);
});
// 浏览器在骨架阶段即可绘制，TTFB 之后的首绘时间被压缩
```
