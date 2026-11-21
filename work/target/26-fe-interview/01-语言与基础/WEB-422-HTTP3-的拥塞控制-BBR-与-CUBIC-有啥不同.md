---
title: [WEB-422] HTTP/3 的拥塞控制：BBR 与 CUBIC 有啥不同
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-422：HTTP/3 的拥塞控制：BBR 与 CUBIC 有啥不同

**答**：
- CUBIC：传统基于丢包的算法——丢包=拥塞，窗口指数退避；在长肥管道或轻微随机丢包（4G/5G、跨境）下被误伤
- BBR：基于带宽与 RTT 估测建模，不依赖丢包信号，主动控制发送节奏贴近瓶颈带宽
- QUIC 的优势：拥塞控制在用户态实现（内核不管），可以热升级换算法，BBR 在 QUIC 栈里落地更快
- 前端感知：弱网、高丢包链路下 HTTP/3 + BBR 的吞吐和卡顿明显更好；这是「HTTP/3 弱网快」的底层原因之一
- 钩子：服务端/CDN 可配置算法，前端测速时若 HTTP/3 与 HTTP/2 差距异常，可先确认对端是否开了 BBR

```javascript
// 前端用 Navigation Timing 对比 H2/H3 的真实下载时间
const nav = performance.getEntriesByType('navigation')[0];
console.log('响应体下载(ms):', nav.responseEnd - nav.responseStart);
// 弱网下 H3 明显更稳，是测试 HTTP/3 收益的关键指标
```
