---
title: [TST-534] CI 流水线中的测试任务如何编排
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-534：CI 流水线中的测试任务如何编排

**答**：
- 结论：按「反馈速度」分层编排——提交级跑 lint/类型/单测（分钟级），合入级跑契约/组件/受影响 E2E（十分钟级），夜间跑全量/性能/安全（小时级）。
- 做法：快任务前置、慢任务后置且并行；用 needs/dependencies 表达依赖；关键路径用缓存与分片加速；失败分层回报，不因慢任务失败阻塞快反馈。
- 追问钩子：E2E 环境准备慢拖累整条流水线怎么办？——把环境准备做成可复用 service 或预热池，用「环境快照」秒级恢复，而非每次重装。

```javascript
// 流水线阶段编排：依赖关系 + 并行组
const pipeline = {
  stages: [
    { name: 'static', jobs: ['lint', 'tsc'], parallel: true },
    { name: 'unit', jobs: ['unit'], needs: ['static'] },
    { name: 'integration', jobs: ['contract', 'component', 'e2e-smoke'], needs: ['unit'], parallel: true },
    { name: 'nightly', jobs: ['e2e-full', 'perf', 'security'], needs: ['integration'], schedule: '0 2 * * *' },
  ],
};
function order(stages) { const seen = new Set(), out = [];
  const visit = s => { if (seen.has(s.name)) return; (s.needs || []).forEach(n =>
    visit(stages.find(x => x.name === n))); seen.add(s.name); out.push(s.name); };
  stages.forEach(visit); return out;
}
```
