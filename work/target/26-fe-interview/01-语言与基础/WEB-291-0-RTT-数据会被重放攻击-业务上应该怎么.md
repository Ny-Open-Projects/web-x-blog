---
title: [WEB-291] 0-RTT 数据会被重放攻击，业务上应该怎么防？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 笔试题
---

## WEB-291：0-RTT 数据会被重放攻击，业务上应该怎么防？
**答**：
- 0-RTT 的早数据没有防重放保护：攻击者抓到 ClientHello 里的 early data 可以原样重发，服务器会当成"新请求"执行。
- 规范约束：0-RTT 只允许发送幂等请求（GET/无副作用的查询），写操作禁止进 0-RTT。
- 业务加固：服务端对 0-RTT 请求做去重窗口（token/nonce）；下单、支付等接口显式拒绝早数据（TLS 配置层或网关标记）。

```javascript
// 网关侧拦截示意：0-RTT 标记的请求只放行幂等方法
function handle(req) {
  if (req.isEarlyData && !['GET', 'HEAD'].includes(req.method)) {
    return { status: 425, msg: 'Too Early：写请求不接受 0-RTT' };
  }
  if (req.isEarlyData && seenNonces.has(req.nonce)) {
    return { status: 409, msg: '疑似重放' };   // 去重窗口
  }
  seenNonces.add(req.nonce);
  return proxy(req);
}
console.log('425 Too Early 是专门为 0-RTT 设计的状态码');
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
