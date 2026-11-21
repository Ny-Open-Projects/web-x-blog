---
title: [SCN-052] 线上偶现 5xx 接口报错，后端说前端也有问题，前端如何自证清白？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-052：线上偶现 5xx 接口报错，后端说前端也有问题，前端如何自证清白？
**答**：
- 自证核心是"证据链"：请求发了什么（参数、headers）、收到什么（状态码、耗时）、能不能对上后端日志，全部要有据可查。
- 每个请求注入 X-Trace-Id，报错时把 traceId、URL、参数、耗时一起上报，后端按 traceId 反查网关日志即可归责到具体节点。
- 归因边界：请求未到达（CORS/DNS/被取消）属前端或网络层；到达后 500 属服务端；502/504 属网关与上游，拿到 traceId 一查便知。

```javascript
// 接口证据链：每次请求记录 traceId 与耗时，5xx 时上报完整现场
import axios from 'axios';

const http = axios.create({ timeout: 10000 });

http.interceptors.request.use((config) => {
  config.metadata = { start: performance.now() };
  config.headers['X-Trace-Id'] = crypto.randomUUID();   // 后端日志可按此反查
  return config;
});

http.interceptors.response.use(undefined, (error) => {
  const { response, config } = error;
  if (response?.status >= 500) {
    navigator.sendBeacon('/api/monitor', JSON.stringify({
      type: 'api-5xx',
      url: config.url,
      traceId: config.headers['X-Trace-Id'],   // 归责到具体网关节点的钥匙
      status: response.status,
      cost: Math.round(performance.now() - config.metadata.start),
      body: JSON.stringify(config.data).slice(0, 500),
    }));
  }
  return Promise.reject(error);
});
```
