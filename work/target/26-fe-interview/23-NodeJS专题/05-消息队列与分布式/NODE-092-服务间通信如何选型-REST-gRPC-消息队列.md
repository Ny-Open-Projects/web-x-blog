---
title: [NODE-092] 服务间通信如何选型（REST/gRPC/消息队列）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-092：服务间通信如何选型（REST/gRPC/消息队列）？
**答**：
- **REST/JSON**：通用、可调试、生态广，适合对外 API 与 BFF→前端；性能一般（文本序列化）。
- **gRPC**：HTTP/2 + Protobuf 二进制序列化（体积小 5-10 倍、编解码快），强类型 IDL 契约、原生支持流式与双向流；适合**内部服务间高频调用**。Node 用 `@grpc/grpc-js`；缺点：浏览器不能直连（需 grpc-web/Connect）、调试门槛高。
- **消息队列**：异步解耦、削峰，不要求即时响应的场景。
- 决策树：浏览器→服务用 REST/BFF；服务→服务同步调用、低延迟高性能用 gRPC；不需要同步结果用 MQ。

```protobuf
// proto/user.proto：IDL 契约（强类型，前后端代码生成）
syntax = "proto3";
package user.v1;

service UserService {
  rpc GetUser (GetUserRequest) returns (GetUserResponse);
  rpc StreamOrders (StreamOrdersRequest) returns (stream OrderEvent);  // 服务端流式
}

message GetUserRequest { int64 uid = 1; }
message GetUserResponse {
  int64 uid = 1;
  string name = 2;
  repeated string roles = 3;
}
message OrderEvent {
  int64 order_id = 1;
  string status = 2;
  int64 updated_at = 3;
}
```

```javascript
// gRPC 服务端
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const def = protoLoader.loadSync('user.proto');
const proto = grpc.loadPackageDefinition(def);

const server = new grpc.Server();
server.addService(proto.user.v1.UserService.service, {
  GetUser: async (call, callback) => {
    const user = await userService.find(call.request.uid);
    if (!user) return callback({ code: grpc.status.NOT_FOUND, message: '用户不存在' });
    callback(null, { uid: user.id, name: user.name, roles: user.roles });
  },
  StreamOrders: (call) => {                       // 服务端流式：持续推送订单状态
    const stream = orderService.watchByUser(call.request.uid);
    stream.on('data', (order) => call.write({ order_id: order.id, status: order.status, updated_at: order.ts }));
    stream.on('end', () => call.end());
    call.on('cancelled', () => stream.close());   // 客户端断开清理
  },
});
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => server.start());

// 客户端（BFF 调用下游）
const client = new proto.user.v1.UserService('user-service:50051',
  grpc.credentials.createInsecure());
const user = await new Promise((resolve, reject) =>
  client.GetUser({ uid: 42 }, (err, res) => (err ? reject(err) : resolve(res))));
```
