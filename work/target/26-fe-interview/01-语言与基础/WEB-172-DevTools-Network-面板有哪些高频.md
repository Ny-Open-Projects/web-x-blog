---
title: [WEB-172] DevTools Network 面板有哪些高频功能？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-172：DevTools Network 面板有哪些高频功能？
**答**：
- 瀑布图逐列定位：Queueing（连接数限制）、Stalled（代理/磁盘）、TTFB（服务端慢）、Content Download（体积大）。
- 状态识别：灰色的 from cache/304、红色的 blocked: cors、紫色的 pending；勾选 Disable cache 排除缓存干扰，配 throttling 预设（Slow 4G）模拟弱网。
- 过滤器支持语法：-domain:cdn、method:POST、larger-than:100kB；Block request URL 验证资源缺失时的降级表现。
- 右键 Copy as fetch/cURL 一键复现请求；导出 HAR（json 格式）给他人离线分析，timings 字段与瀑布图各列一一对应，dns/connect/ssl 为 -1 表示复用已有连接。

```json
{
  "log": {
    "entries": [{
      "_resourceType": "xhr",
      "request": { "method": "GET", "url": "https://api.example.com/list?page=1" },
      "response": { "status": 200, "headersSize": 312, "bodySize": 18204 },
      "timings": {
        "blocked": 12, "dns": -1, "connect": -1, "ssl": -1,
        "send": 0, "wait": 388, "receive": 24, "_blocked_queueing": 3
      }
    }]
  }
}
```
