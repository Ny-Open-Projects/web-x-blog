---
title: [NODE-148] 服务间通信如何选型并保证韧性（超时/重试/透传）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-148：服务间通信如何选型并保证韧性（超时/重试/透传）？
**答**：
- 选型速记：内部高频强契约 → gRPC（protobuf 二进制快 + 接口即文档）；对外/快迭代 → REST；异步解耦/削峰/事件通知 → MQ（NODE-092 有完整对比）。
- 韧性三件套比选型更重要：**deadline 必设**（防无限等待）、重试只对幂等且明确可重试的错误（UNAVAILABLE，不重试 INVALID_ARGUMENT）、退避 + 抖动防重试风暴。
- 全链路透传：traceparent（NODE-136）、灰度染色头、租户信息——通信层封装统一注入，业务无感。
- MQ 侧契约：序列化 schema 注册中心统一管理，消费幂等 + DLQ 兜底。

```javascript
const grpc = require('@grpc/grpc-js');

const client = new orderPkg.OrderService('order:50051',
  grpc.credentials.createInsecure(), {
    'grpc.enable_retries': 1,
    'grpc.service_config': JSON.stringify({
      methodConfig: [{
        name: [{ service: 'order.OrderService' }],
        timeout: '0.3s',                     // deadline 必设
        retryPolicy: {
          maxAttempts: 3,
          initialBackoff: '0.1s', maxBackoff: '1s', backoffMultiplier: 2,
          retryableStatusCodes: ['UNAVAILABLE'], // 只重试明确可重试错误
        },
      }],
    }),
  });

const meta = new grpc.Metadata();
meta.set('traceparent', currentTraceparent());  // 链路透传（NODE-136）
const reply = await new Promise((res, rej) =>
  client.getOrder({ orderId }, meta, { deadline: Date.now() + 300 },
    (e, r) => (e ? rej(e) : res(r))));
```
