---
title: [PER-992] postMessage 的安全边界怎么设
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-992：postMessage 的安全边界怎么设

**答**：
- 风险：监听端不校验 origin 即处理消息 → 任意窗口可发消息操纵业务；发送端用 * 泛目标 → 数据泄露到任意嵌入方。
- 规范：接收端校验 event.origin 白名单 + 校验消息 schema；发送端 targetOrigin 精确到来源。
- 深水：iframe 场景 sandbox 属性限制子页能力（allow-scripts 不与 allow-same-origin 同用，否则 sandbox 失效）。
- 消息协议：所有跨窗口消息走统一信封 { type, payload, nonce }，type 白名单分发，未注册类型丢弃并上报。

```javascript
// 安全的 postMessage 通道
const TRUSTED = new Set(['https://parent.example.com']);
addEventListener('message', e => {
  if (!TRUSTED.has(e.origin)) return;              // 来源校验
  const { type, payload } = e.data ?? {};
  const handler = HANDLERS[type];
  if (!handler) { report({ type: 'unknown-msg', type }); return; }
  handler(payload);
});
const HANDLERS = {
  resize: p => iframe.style.height = p.height + 'px',   // 只开已注册能力
};
// 发送端：parent.postMessage(data, 'https://parent.example.com')  // 禁用 '*'
```
