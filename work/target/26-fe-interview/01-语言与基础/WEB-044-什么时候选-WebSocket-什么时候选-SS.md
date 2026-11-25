---
title: [WEB-044] 什么时候选 WebSocket，什么时候选 SSE？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-044：什么时候选 WebSocket，什么时候选 SSE？
**答**：
- 双向高频交互（聊天、协作编辑、游戏、多人光标）选 WebSocket；仅服务器单向推送选 SSE。
- 考虑运维成本：SSE 就是 HTTP，nginx/网关/LB 无需特殊配置；WebSocket 要处理 Upgrade、空闲超时、代理缓冲。
- 兼容与基础设施：企业内网代理常掐断 WebSocket，SSE 存活率更高。
- 混合方案也常见：SSE 做下行推送，普通 POST 做上行指令，省掉 WebSocket 长连接成本。

```javascript
// 同一业务的两种实现选型对比
// 场景一：股票行情只读推送 —— SSE 足够，简单可靠
function watchQuotesSSE(symbols) {
  const es = new EventSource(`/quotes?symbols=${symbols.join(',')}`);
  es.addEventListener('quote', (e) => renderQuote(JSON.parse(e.data)));
  return () => es.close();
}

// 场景二：交易员需要订阅行情 + 下单 —— 双向，用 WebSocket
function tradingWS() {
  const ws = new WebSocket('wss://api.example.com/trading');
  ws.addEventListener('open', () => {
    ws.send(JSON.stringify({ type: 'subscribe', symbols: ['AAPL'] }));
  });
  ws.addEventListener('message', (e) => renderQuote(JSON.parse(e.data)));
  return {
    unsubscribe: () => ws.send(JSON.stringify({ type: 'unsubscribe', symbols: ['AAPL'] })),
    placeOrder: (order) => ws.send(JSON.stringify({ type: 'order', ...order })), // 双向上行
    close: () => ws.close(),
  };
}
```

## 追问（补充）

**追问**：

1. EventSource 断线会自动重连，还需要自己做重连吗？ → 会自动重连并带上 `Last-Event-ID`；但服务端必须给消息写 `id:` 字段并按该 id 续发，否则重连后会重放或漏消息。
2. SSE 在 HTTP/1.1 下有什么连接数限制？ → 同域最多 6 个连接，多个标签页会互抢，长连接很容易被占满；应合并频道，或上 HTTP/2 多路复用。
3. 为什么经过 Nginx 后 SSE 会「攒一批才收到」？ → 代理默认开启响应缓冲，需要 `proxy_buffering off` 或 `X-Accel-Buffering: no`，并定期发心跳注释行防空闲超时断开。
