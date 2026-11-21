---
title: [WEB-443] postMessage 的安全要点：targetOrigin 与 origin 校验
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-443：postMessage 的安全要点：targetOrigin 与 origin 校验

**答**：
- 发送方：`postMessage(data, targetOrigin)` 的 targetOrigin 千万不要写 `*`，写 `*` 意味着任何嵌套你的页面都能收到数据
- 接收方：handler 里必须先校验 `event.origin`，再消费数据；来源不明的消息直接丢弃
- 还要校验 event.source 与预期 iframe/window 一致，防多 iframe 混杂时串台
- 数据本身不可信：来自跨域的消息可能是攻击者伪造的，按「外部输入」处理（校验 schema、不要直接 innerHTML）
- 典型场景：iframe 嵌套的支付组件、编辑器插件、微前端跨域通信，都是高危面

```javascript
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://pay.partner.com') return; // 第一道闸
  if (event.source !== payFrame.contentWindow) return;    // 第二道闸
  const { type, payload } = JSON.parse(event.data);
  if (type === 'PAY_RESULT') handlePay(payload);          // payload 仍按外部输入校验
});
```
