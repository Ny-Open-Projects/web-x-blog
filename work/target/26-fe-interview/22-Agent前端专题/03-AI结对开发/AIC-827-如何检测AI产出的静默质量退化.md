---
title: [AIC-827] 答案依然流畅但越来越不准，如何检测「静默质量退化」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-827：答案依然流畅但越来越不准，如何检测「静默质量退化」？
**答**：
- 静默退化的危险在于没有报错、延迟正常、格式正确，传统监控（错误率/延迟）全绿，但答案事实错误率悄悄上升。它通常由模型静默升级、prompt 微调、RAG 语料过期引起。
- 检测要引入「**质量探针**」：一组答案已知且可自动核验的固定问题（如检索固定文档回答、数学题、代码执行题），高频定时运行，结果可确定性比对——这是 AI 系统的「健康检查端点」。
- 用户行为代理指标：复制率下降、重试率上升、点了「没帮助」、会话提前结束——单个信号噪声大，多个信号组合异常才触发复核。
- 关键：**固定版本对照**。同时跑线上版本和一个冻结的基线版本在同一批探针上，比较相对差异，能抵消流量结构变化带来的干扰。
- 追问钩子：能说出「质量探针必须可确定性自动核验，不能又用一个模型去判另一个模型」的候选人，理解评估链的可靠性问题。

```typescript
// 质量探针：答案可确定性核验，定时运行
type Probe = { id: string; input: string; verify: (out: string) => boolean };

const probes: Probe[] = [
  { id: 'math', input: '17 × 23 = ?', verify: o => o.includes('391') },
  { id: 'retrieve', input: '退款政策第 3 条？', verify: o => o.includes('7 天无理由') },
  { id: 'code', input: '写一个函数返回数组长度（执行验证）', verify: o => runCode(o) === 3 },
];

async function runProbes(call: (p: string) => Promise<string>) {
  const results = await Promise.all(probes.map(async p => ({
    id: p.id, ok: p.verify(await call(p.input)),
  })));
  const passRate = results.filter(r => r.ok).length / results.length;
  return { passRate, failed: results.filter(r => !r.ok).map(r => r.id) };
}

// 线上版本 vs 冻结基线版本对照，抵消流量变化干扰
const [online, baseline] = await Promise.all([
  runProbes(p => onlineModel.chat(p)),
  runProbes(p => frozenBaseline.chat(p)),
]);
if (baseline.passRate - online.passRate > 0.05) {
  console.log('WARN: 疑似静默退化', online.failed); // 触发人工复核
}
```
