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

## 八、DNS 与 CDN
