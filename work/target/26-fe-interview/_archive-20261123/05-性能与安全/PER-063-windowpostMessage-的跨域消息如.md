---
title: [PER-063] window.postMessage 的跨域消息如何校验？缺失 origin 验证有什么后果？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-063：window.postMessage 的跨域消息如何校验？缺失 origin 验证有什么后果？

**答**：
- postMessage 两条铁律：**发送方**始终显式指定目标 origin（不用 `*`），**接收方**必须校验 `event.origin` 在白名单内，且对 `event.data` 做结构校验后再使用。
- 缺失校验的后果：恶意页面 iframe 你的站点后发送伪造消息（“支付成功”“管理员模式”），或诱导你的页面把敏感数据 postMessage 给任意窗口。
- data 不能是裸字符串直接 eval/innerHTML，优先 JSON 结构化 + 字段类型校验；消息里带 token 等敏感字段属于设计错误。
- 建议封装统一消息通道，集中做 origin 白名单、schema 校验、审计日志，业务方只注册带类型的 handler。

```javascript
// 统一的跨域消息通道：origin 白名单 + 数据结构校验
const TRUSTED_ORIGINS = new Set(['https://pay.example.com', 'https://embed.partner.com']);

function createMessageChannel(win) {
  const handlers = new Map();
  window.addEventListener('message', (event) => {
    if (!TRUSTED_ORIGINS.has(event.origin)) return; // 铁律 1：来源白名单
    let data;
    try { data = JSON.parse(event.data); } catch { return; }
    if (typeof data?.type !== 'string' || !handlers.has(data.type)) return;
    // 铁律 2：结构校验后再交给业务 handler
    handlers.get(data.type)(data.payload);
  });
  return {
    on(type, fn) { handlers.set(type, fn); },
    send(type, payload) {
      win.postMessage(JSON.stringify({ type, payload }), 'https://pay.example.com'); // 铁律 3：不使用 *
    },
  };
}

// 业务使用：iframe 支付回执
const payFrame = document.querySelector('iframe#pay');
const channel = createMessageChannel(payFrame.contentWindow);
channel.on('pay:success', (p) => {
  if (typeof p.orderId !== 'string') return;
  showPaid(p.orderId);
});
```
