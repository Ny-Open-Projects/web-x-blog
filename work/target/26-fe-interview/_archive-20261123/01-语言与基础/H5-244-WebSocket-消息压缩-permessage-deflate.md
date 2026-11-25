---
title: [H5-244] WebSocket 消息压缩：permessage-deflate
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, WebSocket]
type: 面试题
---

## H5-244：WebSocket 消息压缩：permessage-deflate

**答**：
- permessage-deflate：WS 握手时的扩展协商，对每条消息做 DEFLATE 压缩，文本类消息体积可降 60%~90%
- 前提：客户端在握手 Sec-WebSocket-Extensions 里声明，服务端 ws 库开启 `perMessageDeflate: true`
- 两个关键参数：server_no_context_takeover / client_no_context_takeover（控制压缩上下文跨消息保留，影响压缩率与内存）
- 何时不开：高频小消息（心跳、游戏坐标）压缩反而增加 CPU 且收益小；大 JSON（日志、批量数据）收益明显
- 坑：压缩可能引发内存膨胀（历史压缩上下文），内存受限的网关要限制 windowBits；开启后注意 CPU 监控

```javascript
new WebSocket.Server({
  server,
  perMessageDeflate: {
    threshold: 1024,               // 小于 1KB 不压缩
    serverNoContextTakeover: true, // 每消息独立，省内存
    windowBits: 12,
  },
});
```
