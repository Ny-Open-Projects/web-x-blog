---
title: [HW-264] 手写一个 OT 与 CRDT 选型压测：并发场景确定性对比
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-264：手写一个 OT 与 CRDT 选型压测：并发场景确定性对比

**答**：
- 需求：实现 AlgoBench：同一并发场景（N 站点 × M ops）分别跑 OT（经 server 仲裁）与 CRDT（P2P 合并），断言：最终文本一致（各自内部）、跨算法结果可不同（记录差异）；统计耗时与消息量；输出对比报告。
- 边界：OT 依赖服务器顺序（中心化），CRDT 无中心（消息量更大）；压测轮次可配；报告含收敛时间与消息字节数。
- 评分点：双算法同场景对拍；指标维度完整；差异解释。

```javascript
function algoBench({ sites = 5, opsPer = 50, rounds = 10 } = {}) {
  const report = { ot: [], crdt: [] };
  for (let r = 0; r < rounds; r++) {
    const seed = r;
    // OT 路径：所有 op 提交服务器仲裁
    const t0 = performance.now();
    const otDocs = runOT(sites, opsPer, seed);
    report.ot.push({ ms: performance.now() - t0,
      msgs: sites * opsPer * 2,                              // 提交+广播
      converged: otDocs.every(d => d === otDocs[0]) });
    // CRDT 路径：P2P 全量交换合并
    const t1 = performance.now();
    const crdtDocs = runCRDT(sites, opsPer, seed);
    report.crdt.push({ ms: performance.now() - t1,
      msgs: sites * sites,                                   // 全量状态交换
      converged: crdtDocs.every(d => d === crdtDocs[0]) });
  }
  return {
    summary: {
      otAvgMs: avg(report.ot.map(x => x.ms)),
      crdtAvgMs: avg(report.crdt.map(x => x.ms)),
      note: 'OT 消息少但中心化；CRDT 去中心但状态量大——弱网/离线场景 CRDT 优势',
    },
  };
}
const avg = a => +(a.reduce((s, x) => s + x, 0) / a.length).toFixed(1);
```
