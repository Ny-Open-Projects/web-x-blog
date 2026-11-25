---
title: [WEB-424] QUIC 的流控和 TCP 有什么不同
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-424：QUIC 的流控和 TCP 有什么不同

**答**：
- TCP 的流控窗口是整条连接一个；QUIC 分两层：每条流一个流级窗口 + 连接级总窗口
- 好处：某条流被消费端拖慢（如用户暂停了一路下载）时，只堵这条流，其他流照常满速
- 流控是「信用制」：接收方通过 MAX_DATA/MAX_STREAM_DATA 帧告知可用额度，发送方不能超发
- 前端关联：HTTP/3 下若某资源响应很慢但占着窗口，其他资源不受影响——这是 H3 多路复用体验更好的细节原因
- 钩子：面试可延伸到「QUIC 流控是应用层实现的，所以窗口策略可以按业务定制」

```javascript
// HTTP/3 的流式读取示例（fetch streams 本身协议无关，但底层受益于流级流控）
const res = await fetch('/big-file');
const reader = res.body.getReader();
let total = 0;
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  total += value.length; // 消费得快，对端流控窗口才会扩大
}
```
