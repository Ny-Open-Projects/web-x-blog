---
title: [NODE-703] 服务发现与健康检查联动怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-703：服务发现怎么联动？
**答**：
- K8s 模式：Service DNS + kube-proxy 负载均衡—— readiness 探针控制 endpoint 摘流（SCN-NODE-664 联动）；客户端 DNS 缓存的摘流延迟（DNS TTL——长 TTL 让摘流慢，短 TTL 加 DNS 压力）。
- 客户端负载均衡：gRPC 的 client-side LB（实例列表直连——更均衡，DNS 单 VIP 的负载不均问题）；服务发现缓存 + 订阅更新（Nacos/Consul watch）。
- 摘流传播链：Pod 摘流（readiness fail）→ endpoint 更新 → 客户端发现更新——传播窗口内仍有流量打到坏实例（重试/熔断兜底——SCN-NODE-669）。
- 追问钩子：为什么「客户端负载均衡」在 gRPC 场景优于 DNS 轮询——DNS 解析一个 VIP 后 kube-proxy 均匀分发，但长连接场景（gRPC HTTP/2）连接建立后固定——所有流量压到少数 Pod（连接复用导致负载不均）；客户端 LB 持有全实例列表按请求/按连接轮询——长连接场景的负载均衡必须客户端感知实例列表。

```javascript
// gRPC 客户端 LB
const client = new OrderClient('order-svc:50051', null, {
  'grpc.loadbalancing_policy': 'round_robin',          // 客户端持有实例列表
});
// 服务发现订阅
discovery.watch('order-svc', (instances) => client.updateInstances(instances));
```
