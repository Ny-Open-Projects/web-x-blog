---
title: [AIC-697] AI 平台的 SLA 该怎么设计？可用性和质量怎么承诺？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-697：AI 平台的 SLA 该怎么设计？可用性和质量怎么承诺？

**答**：
- 结论先行：**AI 平台的 SLA 不能只承诺「可用性」，必须分层承诺「可用性 + 延迟 + 质量」——因为 AI 服务「返回了但答得很差」比「挂了」更隐蔽、更有害**（AIC-050 度量看板）。
- 三层 SLA：1) **可用性**：服务可用率（如 99.9%）、错误率上限——这是传统 SLA；2) **延迟**：P50/P95/P99 响应时间，分任务类型（补全要 <100ms，Agent 任务可分钟级）；3) **质量**：这是 AI 特有——评测集通过率下限、接受率/存活率下限、误报率上限（对审查类）。
- 质量 SLA 的特殊性：质量是概率的、波动的，不能承诺「100% 正确」——要承诺「统计下限」（如「评测通过率 ≥ 85%，连续 3 天低于则触发整改」），并用灰度门禁保障（AIC-695）。
- 降级与赔偿：SLA 要写明「不达标时的降级策略」（切备用模型/降级为静态检查，AIC-643）和责任边界——AI 是辅助工具，最终质量责任在使用方，SLA 不能承诺「替代人审」。
- 度量支撑：SLA 的每项都要能测量（网关埋点 AIC-684 + 链路追踪 AIC-693），不能测量的承诺是空话。
- 追问钩子：为什么「质量 SLA」不能像可用性那样承诺 99.9%？——因为 LLM 输出本质是概率的，即使最好的模型也有错误率；承诺接近 100% 必然违约。务实的做法是承诺「统计下限 + 持续监控 + 退化熔断」，承认概率性并用流程兜底，而不是自欺欺人地承诺确定性。

```typescript
type SLA = {
  availability: number;   // 0.999
  p95LatencyMs: number;
  minEvalPassRate: number;
  minAcceptance: number;
};

function checkSLA(actual: { availability: number; p95Ms: number; evalRate: number; acceptance: number }, sla: SLA) {
  const breaches = [];
  if (actual.availability < sla.availability) breaches.push('availability');
  if (actual.p95Ms > sla.p95LatencyMs) breaches.push('latency');
  if (actual.evalRate < sla.minEvalPassRate) breaches.push('quality-eval');
  if (actual.acceptance < sla.minAcceptance) breaches.push('quality-acceptance');
  return { met: breaches.length === 0, breaches, action: breaches.length ? '触发降级+整改' : '正常' };
}

const sla: SLA = { availability: 0.999, p95LatencyMs: 3000, minEvalPassRate: 0.85, minAcceptance: 0.6 };
const actual = { availability: 0.9995, p95Ms: 2500, evalRate: 0.82, acceptance: 0.65 };
console.log(checkSLA(actual, sla).breaches.includes('quality-eval')); // 质量不达标
console.log(checkSLA({ ...actual, evalRate: 0.9 }, sla).met === true);
```
