---
title: [H5-290] IM 输入中状态（typing）怎么做：节流与协议
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-290：IM 输入中状态（typing）怎么做：节流与协议

**答**：
- 语义：对方正在输入…的实时提示；轻量但高频，协议设计重点是「幂等 + 自动超时」
- 发送节流：input 事件 500ms 节流发送 TYPING 消息；输入停止 3s 后发 STOP——用「状态 + 过期时间」而非事件流
- 接收方处理：显示 typing 提示并启动 5s 过期自动隐藏（消息丢了也能自愈）；同会话去重
- 带宽考量：typing 消息不要走可靠重传（丢了就丢，下一轮会刷新）；不要存库
- 群聊优化：大群不广播 typing（消息风暴），只在小群/单聊开启

```javascript
let typingTimer;
input.addEventListener('input', () => {
  ws.send(JSON.stringify({ type: 'TYPING', convId })); // 500ms 节流包装
  clearTimeout(typingTimer);
  typingTimer = setTimeout(() => ws.send(JSON.stringify({ type: 'TYPING_STOP', convId })), 3000);
});
// 接收
function onTyping({ convId }) {
  showTypingIndicator(convId);
  setTimeout(() => hideTypingIndicator(convId), 5000); // 过期自愈
}
```
