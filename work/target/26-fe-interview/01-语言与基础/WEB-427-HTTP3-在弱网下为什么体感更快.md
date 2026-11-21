---
title: [WEB-427] HTTP/3 在弱网下为什么体感更快
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-427：HTTP/3 在弱网下为什么体感更快

**答**：
- 握手快：0-RTT/1-RTT vs TCP+TLS 2-3 RTT，弱网下每个 RTT 都几百毫秒，差距被放大
- 队头阻塞消除：丢包率 2% 时 TCP 下 H2 全连接停摆，H3 只有丢的那条流受影响
- 更准确的丢包恢复：QUIC 有单调递增包号，能精确区分重传与原始包，RTT 估测更准，避免 TCP 的 RTO 超时等待
- 拥塞控制升级：常配 BBR，高丢包链路不激进退让
- 面试收尾：弱网优化建议开启 H3 + 0-RTT（幂等资源），配合图片降级/骨架屏做体验兜底

```javascript
// 弱网分级：结合 effectiveType 与资源加载时间动态降级
const slow = (navigator.connection?.effectiveType ?? '4g') === '2g'
  || performance.getEntriesByType('resource').some(r => r.responseEnd - r.startTime > 3000);
if (slow) document.documentElement.dataset.mode = 'lite'; // CSS/JS 读取后走降级渲染
```
