---
title: [WEB-140] gRPC-Web 是什么？为什么浏览器不能直接发 gRPC？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-140：gRPC-Web 是什么？为什么浏览器不能直接发 gRPC？
**答**：
- gRPC 基于 HTTP/2 的尾部头（trailers）与流式分帧，浏览器 fetch/XHR 拿不到 trailers，也不能裸控 HTTP/2 帧，所以原生 gRPC 在浏览器不可行。
- gRPC-Web 是浏览器侧的适配层：客户端把调用编码成 HTTP 请求，代理（Envoy 等）翻译成真正的 gRPC 转给后端。
- 与 REST+JSON 相比：二进制 Protobuf 体积小、接口契约严格、有代码生成；代价是调试不直观、需要代理层。
- 浏览器侧能力：一元调用与服务端流可用，双向流受限。

```javascript
// 由 .proto 生成的 grpc-web 客户端，浏览器侧像调用本地方法
const client = new EchoServicePromiseClient('https://api.example.com', null, {});
const req = new EchoRequest();
req.setMessage('hello');
const resp = await client.echo(req, { 'x-user-id': '42' });
console.log(resp.getMessage());
// 服务端流：逐帧回调，代理层把 gRPC 流翻译成浏览器可读的分帧响应
const stream = client.serverStream(req, {});
stream.on('data', (chunk) => console.log('frame:', chunk.getMessage()));
stream.on('end', () => console.log('done'));
```
