---
title: [PER-1039] 移动端弱网下的 DNS 与连接预热
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1039：移动端弱网下的 DNS 与连接预热

**答**：
- 移动网络建连成本高于桌面：DNS 100~300ms + TCP/TLS 各一个 RTT，弱网下首字节前开销可超 1s。
- 预热时机：App 启动/页面进入时 preconnect 核心域；用户登录成功后预热下单域；推送到达后预热详情域。
- QUIC 优势：0-RTT 恢复 + 连接迁移，移动端弱网收益最大，网关需保证 UDP 通畅（部分运营商限制）。

```javascript
// 登录成功后的预热编排
const PREWARM = ['https://api.example.com', 'https://pay.example.com'];
function prewarm(list = PREWARM) {
  list.forEach(u => {
    const l = document.createElement('link');
    l.rel = 'preconnect'; l.href = u; l.crossOrigin = 'anonymous';
    document.head.appendChild(l);
  });
}
// 在小程序/RN 容器中对应：启动期预热原生网络栈
// 验证：对比预热开关的 TTFB 分位差
```
