---
title: [NODE-668] Node 服务端的灰度与金丝雀发布怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-668：服务端灰度怎么做？
**答**：
- 服务端灰度分层：实例级（K8s 滚动副本——Deployment 双版本并存）+ 请求级（按 header/user 路由到金丝雀——网关路由规则，SCN-OPS-233 分层决策）。
- 金丝雀的指标对比：canary vs stable 的错误率/延迟/资源对比（SCN-OPS-239 看板——服务端版本是 hard 自动判定）。
- 数据兼容的准入：金丝雀版本写的数据（新 schema）必须兼容旧版本读（回滚安全——SCN-OPS-205 双向兼容在服务端的体现）。
- 服务端特有的验证：下游兼容（新版本调用的下游接口/消息格式——消费方兼容矩阵）、缓存兼容（新序列化格式 vs 旧缓存反序列化）。
- 追问钩子：为什么服务端金丝雀的「数据兼容检查」比前端更重要——前端回滚是切入口（数据无写入语义）；服务端金丝雀版本写 DB/写缓存/发消息，回滚后旧版本必须能处理这些数据（读新写旧降级——SCN-OPS-205）——不验证数据兼容的金丝雀，回滚时就是数据事故。

```javascript
// 请求级金丝雀路由（网关）
function route(user, versions) {
  const v = canarySplit(user, versions);               // 稳定哈希分流
  return v;                                            // header X-Canary 传递（全链标记）
}
// 数据兼容自检（canary 版本内置）
if (process.env.CANARY) monitorDualWrite(driftRate);   // 双写漂移检测（SCN-OPS-331）
```
