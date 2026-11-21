---
title: [AGT-188] Agent 服务的故障演练（混沌工程）怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-188：Agent 服务的故障演练（混沌工程）怎么设计？
**答**：
- 故障注入场景清单：模型上游 5xx/超时/限流、工具全挂（依赖的第三方 API 宕机）、向量库不可用、网络分区（Agent 与队列失联）、模型降级到弱模型后的质量塌方、流量突增 10 倍。
- 演练目标分层：容灾正确性（降级链是否按设计触发、错误是否被吞掉）、用户可感知性（降级时用户看到什么——优雅提示 vs 白屏转圈）、恢复正确性（上游恢复后是否自动切回、半途任务是否正确续跑）。
- 生产演练原则：从影子流量开始（灰度用户的 1% 注入故障）、爆炸半径可控（一键终止注入）、演练窗口避开高峰、事先通知值班。
- 演练产物：每个场景一份「实际表现 vs 预期」报告，差异项变成 bug 单与新增告警规则——没有产出的演练是表演。

```typescript
// 故障注入框架：按场景注入 + 验证降级行为
import { z } from 'zod';

const FaultSpec = z.object({
  target: z.enum(['llm_upstream', 'tool_layer', 'vector_store', 'queue']),
  fault: z.enum(['timeout', '5xx', '429', 'network_partition', 'slow_response']),
  ratio: z.number().min(0).max(1).default(0.1),      // 影子流量比例
  durationMs: z.number(),
});
type FaultSpec = z.infer<typeof FaultSpec>;

export class ChaosAgent {
  private active = new Map<string, FaultSpec>();

  inject(spec: FaultSpec) { this.active.set(spec.target, spec); metrics.inc(`chaos.inject.${spec.target}`); }
  stopAll() { this.active.clear(); }

  // 包装真实调用：注入层不影响业务代码
  async wrap<T>(target: FaultSpec['target'], real: () => Promise<T>): Promise<T> {
    const spec = this.active.get(target);
    if (!spec || Math.random() > spec.ratio) return real();
    switch (spec.fault) {
      case 'timeout':    return new Promise<never>((_, rej) => setTimeout(() => rej(new DOMException('chaos timeout', 'TimeoutError')), 60_000));
      case '5xx':        throw new UpstreamError('chaos 500');
      case '429':        throw new UpstreamError('chaos 429', 429);
      case 'network_partition': return new Promise<never>(() => {});   // 永不 resolve，测挂死防护
      case 'slow_response': return new Promise<T>((r) => setTimeout(() => r(real() as any), 15_000));
    }
  }
}

export async function drill(scenario: FaultSpec[], runTask: (chaos: ChaosAgent) => Promise<DrillReport>) {
  const chaos = new ChaosAgent();
  try {
    for (const s of scenario) chaos.inject(s);
    const report = await runTask(chaos);
    const gaps = report.expectations.filter((e) => !e.met);          // 实际 vs 预期差异 → bug 单
    for (const g of gaps) issueTracker.create({ title: `演练缺口：${g.name}`, detail: g.actual, priority: 'high' });
    return { passed: gaps.length === 0, gaps };
  } finally {
    chaos.stopAll();                                                  // 一键终止注入，爆炸半径可控
  }
}
class UpstreamError extends Error { constructor(m: string, public status = 500) { super(m); } }
type DrillReport = { expectations: { name: string; met: boolean; actual: string }[] };
const metrics = { inc: (n: string) => { void n; } };
const issueTracker = { create: (x: unknown) => { void x; } };
```
