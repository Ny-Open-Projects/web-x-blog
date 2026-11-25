---
title: [MFW-690] Server Actions 的 rate limit
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-690：Server Actions 的 rate limit

**答**:
- Action 的限流需求：Action = 可编程的 server 端点（无天然限流——POST 端点的滥用面 RBL-690）；限流的维度：1) **per-user**（session 维度——登录用户的频率限制）；2) **per-IP**（匿名——IP 限流；但 IP 可伪造/NAT 共享）；3) **per-action**（不同 action 的限流不同——下单 10/min、评论 1/min）；4) **全局**（action 总 QPS——集群保护）。
- 实现的存储：token bucket（Redis——跨实例共享限流状态；Edge KV 的限流（读快写慢——限流的写密集不合适）；DO（RBL-612 单实例串行——天然限流器）。
- 限流的响应：429 + Retry-After header（client 可感知——重试延迟 RBL-672）；「限流的错误语义」与业务错误区分。
- 追问钩子：为什么「Action 的限流」比「API 限流」更难做？——Action = 编译生成的内部端点（URL 是 framework 管理的——middleware 可拦截（RBL-514 粗限流））；但 per-action 限流需要「action id 维度」（每个 action 的独立桶——middleware 拿到 action id（header）→ 按 id 限流）；「限流的维度组合」：userId × actionId 的复合键——Redis token bucket 的 key 设计；API 限流（URL 维度）vs Action 限流（action id 维度）——粒度更细但实现相同。

```typescript
// Action 限流（middleware + per-action 维度）
// middleware.ts
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';
const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.tokenBucket(10, '10 m'),            // 10 次/10 分钟
  prefix: 'action-rl',
});
export async function middleware(req) {
  const actionId = req.headers.get('next-action');
  if (!actionId) return NextResponse.next();             // 非 action 请求
  const session = req.cookies.get('session')?.value;
  const key = `${actionId}:${session ?? ip(req)}`;       // action × user 复合键
  const { success, reset } = await ratelimit.limit(key);
  if (!success)
    return NextResponse.json({ error: 'rate-limited' }, {
      status: 429, headers: { 'retry-after': Math.ceil((reset - Date.now()) / 1000) } });
  return NextResponse.next();
}
// token bucket 的语义：突发容忍 + 平均速率（RBL-872）
```
