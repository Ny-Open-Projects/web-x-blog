---
title: [PER-039] 什么是全链路监控？前端如何用 traceId 串起前后端日志？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-039：什么是全链路监控？前端如何用 traceId 串起前后端日志？

**答**：
- 全链路监控：一个请求从前端发起，经过网关、多个后端服务到数据库的每一跳都有日志，用同一个 traceId 串联。
- 前端职责：进入页面生成（或沿用）traceId，注入每个请求的 header（如 `X-Trace-Id`），后端逐层透传并写进访问日志。
- 排障时用户报障只需提供 traceId，即可在日志平台拉出该请求经过的所有服务的完整日志链。
- 前端自身的事件（路由跳转、用户点击）也可带上 traceId 上报，实现端到端的操作轨迹还原。

```javascript
// 全链路监控：前端生成 traceId 并注入请求头，串起页面 -> 网关 -> 后端各服务
let traceId = sessionStorage.getItem('traceId');
if (!traceId) {
  traceId = crypto.randomUUID();
  sessionStorage.setItem('traceId', traceId);
}

const originalFetch = window.fetch;
window.fetch = function (input, init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set('X-Trace-Id', traceId);          // 后端逐层透传并写入访问日志
  headers.set('X-Page-Url', location.pathname);
  return originalFetch(input, { ...init, headers });
};

// 排障时拿用户提供的 traceId，即可在日志平台拉出该请求的全链路日志
```

## 七、Web 安全
