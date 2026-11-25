---
title: [WEB-554] HTTP/3 迁移的 AB 对照实验怎么做才可信
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-554：HTTP/3 迁移的 AB 对照实验怎么做才可信

**答**：
- 对照单位是「用户」不是「请求」：同一用户要么走 h3 要么走 h2，按请求随机分流会让同一连接/缓存状态串组，数据全废
- 分流实现：按用户 ID 哈希决定是否对该用户下发 Alt-Svc，CDN 侧按 cookie/ua 自定义头路由，而不是网络层随机
- 关键护栏：分桶后先做 SRM 检查（两组流量占比是否符合预期）、剔除爬虫与公司内网 IP、区分新老用户（新用户必然 h2 首连）
- 指标分层看：整体 TTFB/页面加载时间按 RTT 分桶、按地区分桶、按首连/重连分桶——整体均值经常被弱网长尾掩盖
- 观察周期覆盖一周并做周内对齐（周一对比周一），避免流量结构差异；结论附置信区间而不是只报均值

```javascript
// 前端实验埋点: 协议 + 分组 + RTT 一起上报
beacon({
  exp: 'h3-rollout',
  group: window.__EXP_GROUP__,          // 'h3' | 'h2'
  proto: performance.getEntriesByType('navigation')[0]?.nextHopProtocol,
  rtt: navigator.connection?.rtt,       // 用于分桶
  ttfb: performance.getEntriesByType('navigation')[0]?.responseStart,
});
```
