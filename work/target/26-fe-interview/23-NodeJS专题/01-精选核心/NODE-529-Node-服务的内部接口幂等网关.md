---
title: [NODE-529] Node 服务的内部调用幂等网关（BFF→下游自动防重）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-529：内部调用幂等网关
**答**:
- 问题：BFF 重试/编排重放导致下游收到重复写调用——每个下游自己实现幂等是重复劳动。方案：内部幂等网关（BFF 出站统一层：按幂等键去重，下游可透明获得幂等性）。
- 实现：出站拦截（写请求自动生成/继承幂等键——NODE-476 派生协议）、键记录（发送前记录"进行中"，响应后记录结果 TTL——重放时返回缓存响应或等待进行中结果）、分布式键存储（Redis——多实例共享去重视图）。
- 边界与取舍：网关幂等是"调用方视角"（同一键同响应）——下游业务幂等仍需自保（键丢失/网关重部署——下游唯一索引兜底 NODE-381 双保险）；只对幂等声明接口启用（下游接口声明幂等性——未声明的不过网关去重）。
- 语义细节：进行中请求的重放处理（等待原请求结果——singleflight 语义 NODE-378）、响应过大（缓存响应截断——重放返回摘要 + 重新调用提示）。
- 观测：拦截率/键冲突率（同键不同参数——客户端实现错误信号）、去重节省的下游调用量。
```javascript
// 幂等网关拦截
async function idempotentCall(url, init, { key }) {
  const rec = await idemStore.get(key);
  if (rec?.status === 'done') return rec.response;               // 重放返回原响应
  if (rec?.status === 'processing') return waitSame(key);        // 等待进行中
  await idemStore.mark(key, 'processing');
  try { const r = await call(url, { ...init, headers: { 'x-idempotency-key': key } });
        await idemStore.save(key, r); return r; }
  catch (e) { await idemStore.release(key); throw e; }           // 失败释放可重试
}
```

**追问**：

1. `mark(processing)` 之后进程崩了，键永久停在 processing 会怎样？→ 重放会一直等待悬挂；processing 必须带 TTL 和 owner，超时后允许新请求接管。
2. 重试时怎么保证还是同一把幂等键？→ 键进入重试循环前就算好（业务 id 派生），每次重试重新生成 uuid 等于没做幂等。
3. 下游不支持幂等键会怎样？→ 网关只减少重复调用，真重发仍会重复写；所以只对声明幂等的接口启用，且下游仍需唯一索引兜底。
