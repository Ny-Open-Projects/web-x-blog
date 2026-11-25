---
title: [NODE-801] 笔试题——实现 BFF 协议转换层（REST↔gRPC 双桥）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-801：手写协议转换层

**需求与边界**：
- 需求：REST↔gRPC 双桥（SCN-NODE-702）——① REST 请求转 gRPC 调用（字段映射 schema 化）；② gRPC 响应转 REST（驼峰/嵌套展开）；③ 错误码映射（gRPC status → HTTP——SCN-NODE-676 错误码联动）；④ deadline 传播（SCN-NODE-728 双协议贯穿）。
- 边界：① 字段映射表驱动（配置化——非硬编码 per 接口）；② streaming gRPC 的 REST 降级（SSE 转换——SCN-NODE-716）；③ 错误映射表完整（16 个 gRPC status 全覆盖）。

**答**：
```javascript
const GRPC_TO_HTTP = {
  [grpc.status.OK]: 200, [grpc.status.INVALID_ARGUMENT]: 400,
  [grpc.status.NOT_FOUND]: 404, [grpc.status.PERMISSION_DENIED]: 403,
  [grpc.status.RESOURCE_EXHAUSTED]: 429, [grpc.status.UNAVAILABLE]: 503,
  [grpc.status.DEADLINE_EXCEEDED]: 504, [grpc.status.INTERNAL]: 500,
  [grpc.status.UNAUTHENTICATED]: 401,
};
function restToGrpc(route, req) {
  const msg = mapFields(req.body, route.reqMap);       // schema 映射（配置驱动）
  const deadline = remaining();                        // SCN-NODE-728
  return new Promise((resolve, reject) => {
    const call = client[route.method](msg, { deadline: Date.now() + deadline });
    call.on('data', (chunk) => resolve(mapFields(chunk, route.resMap)));   // 响应映射
    call.on('error', (e) => {
      const http = GRPC_TO_HTTP[e.code] ?? 500;
      reject(new AppError(`RPC-${e.code}`, e.details, { http, retryable: e.code === grpc.status.UNAVAILABLE }));
    });
  });
}
```

**评分点**:
- 映射表 schema 化驱动（非硬编码——SCN-ENG-247 契约）。
- 错误码映射表完整 + retryable 语义（SCN-NODE-676）。
- deadline 双协议贯穿（SCN-NODE-728）。
- 响应字段反向映射（驼峰/嵌套——客户端友好）。
