---
title: [AGT-191] 大规模 Agent 服务的容量规划怎么做？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-191：大规模 Agent 服务的容量规划怎么做？
**答**：
- 容量单元拆解：并发会话数 × 每会话 token 速率 × 每任务工具调用次数——Agent 服务的负载特征是「长连接 + 突发 LLM 调用 + 外部依赖放大」（一个任务可能扇出 10 个工具请求）。
- 三类瓶颈分别规划：LLM 上游配额（TPM/RPM 配额决定并发上限，按 429 率预估余量）、自有无状态层（CPU 主要耗在流式转发与解析，按连接数规划）、有状态层（会话存储/向量库按读写 QPS 与存储量规划）。
- 排队模型：上游配额不足时的正确行为是「排队而非丢弃」——用队列长度与等待时间 P95 做扩容触发条件，而不是 CPU 利用率。
- 容量演练：以 3 倍预估峰值做压测，验证「限流→排队→降级→拒绝」整条链路的行为符合 SLO，而不是只验证能扛住。

```typescript
// 容量规划计算器 + 扩容触发
interface CapacityInput {
  peakConcurrentSessions: number;
  avgTokensPerSessionPerSec: number;
  avgToolCallsPerTask: number;
  providerTpmQuota: number;               // 上游 token/min 配额
  sessionLayerQpsPerConn: number;         // 自有层每连接消耗
}

export function capacityPlan(c: CapacityInput) {
  const aggregateTpm = c.peakConcurrentSessions * c.avgTokensPerSessionPerSec * 60;
  const headroom = c.providerTpmQuota / aggregateTpm;
  if (headroom < 1.5) return { verdict: '上游配额不足', needQuota: Math.ceil(aggregateTpm * 1.5), detail: `当前配额仅 ${(headroom * 100).toFixed(0)}% 余量` };

  const toolQps = (c.peakConcurrentSessions * c.avgToolCallsPerTask) / 300;   // 假设任务平均 5 分钟
  const statelessPods = Math.ceil((c.peakConcurrentSessions * c.sessionLayerQpsPerConn) / 500); // 单 pod 500 QPS
  const queueSlots = Math.ceil(c.peakConcurrentSessions * 0.1);               // 排队容量 = 10% 并发
  return { verdict: 'OK', upstreamHeadroom: headroom.toFixed(2), toolQps: Math.ceil(toolQps), statelessPods, queueSlots,
    note: '扩容触发看队列等待 P95 而非 CPU' };
}

// 运行时扩容信号：队列深度 + 等待时间
export function autoscaleSignal(q: { depth: number; waitP95Ms: number }) {
  if (q.waitP95Ms > 5000) return 'scale_out_urgent';       // 等 5s 用户体验已崩，立即扩
  if (q.waitP95Ms > 2000 || q.depth > 500) return 'scale_out';
  if (q.waitP95Ms < 200 && q.depth < 50) return 'scale_in_candidates';
  return 'hold';
}
```
