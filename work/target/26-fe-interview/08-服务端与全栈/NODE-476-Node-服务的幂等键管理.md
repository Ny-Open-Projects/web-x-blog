---
title: [NODE-476] Node 服务的幂等键生命周期管理（生成/传递/清理）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-476：幂等键生命周期管理
**答**:
- 全链路幂等键：前端生成（操作发起时 uuid，重试用同键 ARC-418）→ 网关透传 → BFF 传递（转发时键语义保持或派生：内部拆分为 N 个下游调用时派生键 = 原键 + 序号，保证重放时派生一致）→ 服务端记录。
- 生成规范：键 = 客户端随机（uuid）而非内容哈希（内容相同语义不同的两次操作要独立——哈希会误合并）；作用域（session 或操作上下文）；有效期 24h（幂等记录 TTL）。
- 存储：幂等记录表（键 + 响应 + 状态：processing/done——重放时返回原响应；processing 中重放 → 等待或拒绝）；键唯一索引防并发双插（NODE-412）。
- 清理：TTL 过期清理任务、成功响应可短期保留（客户端重查）、失败响应立即释放（可重试）。
- 验证：并发同键测试（NODE-381）、键丢失行为（无键请求按普通处理——幂等键是可选增强不是硬依赖；但核心资金接口强制键）。
```javascript
// BFF 派生传递
async function proxyWithIdem(ctx) {
  const root = ctx.get('x-idempotency-key');
  const calls = plan(ctx.body);                                  // 拆分为下游调用计划
  return Promise.all(calls.map((c, i) => call(c, {
    'x-idempotency-key': root ? `${root}:${i}` : undefined }))); // 派生键重放一致
}
// 服务端：insert into idem(key, resp, status) on conflict do nothing → 冲突则返回已有响应
```
