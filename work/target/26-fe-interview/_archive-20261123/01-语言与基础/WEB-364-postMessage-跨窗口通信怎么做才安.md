---
title: [WEB-364] postMessage 跨窗口通信怎么做才安全？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-364：postMessage 跨窗口通信怎么做才安全？
**答**：
- 发送方：postMessage(data, targetOrigin) 必须写精确 origin，不用 *，防数据发到伪装窗口。
- 接收方：event.origin 白名单校验后才处理；event.source 校验；不信任 message 内容（字符串要净化，对象当不可信输入）。
- 典型漏洞：接收端直接 eval(message) 或 innerHTML=message → 任意窗口（iframe 埋入）可注入脚本。

```javascript
// 接收端
window.addEventListener('message', (e) => {
  if (!['https://pay.partner.com'].includes(e.origin)) return; // 白名单
  const { type, payload } = JSON.parse(e.data);
  if (type === 'PAY_RESULT') render(textContentSafe(payload));
});
// 发送端
iframe.contentWindow.postMessage(JSON.stringify({ type: 'QUERY' }), 'https://pay.partner.com');
console.log('双向都要校验 origin，内容当不可信');
```
