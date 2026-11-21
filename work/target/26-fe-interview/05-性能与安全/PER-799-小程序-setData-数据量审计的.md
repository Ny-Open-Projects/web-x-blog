---
title: [PER-799] 小程序 setData 数据量审计的指标与阈值：从数据通信成本出发定审计口径
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-799：小程序 setData 数据量审计的指标与阈值：从数据通信成本出发定审计口径

**答**：
- 通信成本模型：setData 的开销 ≈ 数据序列化 + 跨线程传输 + 渲染层 diff，量级敏感指标是单次调用的数据量（KB）与调用频次（次/秒），二者相乘才是真实压力。
- 核心审计指标：单次 setData 数据量（阈值建议 < 256KB 绝对红线，< 100KB 建议线）；高频调用（1 秒内 > 5 次）；与上一次调用的时间间隔 < 16ms（可合并）；冗余字段率（本次传输数据中与视图无关的比例）。
- 口径坑：data 路径写法（setData 带 a.b 路径 key）只传输增量，整对象写法全量传输——审计必须区分路径更新与全量更新，分别设阈值。
- 产出：审计报告要能落到"哪个页面哪个函数哪一行"，静态扫描 + 运行时采样结合。

```javascript
const AUDIT_RULES = {
  singleKB: { warn: 100, fail: 256 },                        // 单次数据量阈值
  freqPerSec: { warn: 5, fail: 20 },                         // 调用频次
  minIntervalMs: 16,                                         // 间隔 < 1 帧可合并
  redundantRatio: { warn: 0.3 },                             // 与视图无关字段占比
};
function auditSetData(logs) {                                 // logs: {page, fn, sizeKB, t, isPath}
  const byPage = {};
  for (const l of logs) {
    const s = byPage[l.page] ??= { calls: 0, kb: 0, pathCalls: 0, tooBig: [], burst: 0 };
    s.calls++; s.kb += l.sizeKB;
    if (l.isPath) s.pathCalls++;                             // 路径更新占比（越高越好）
    if (l.sizeKB > AUDIT_RULES.singleKB.fail) s.tooBig.push(l);
  }
  return Object.entries(byPage).map(([page, s]) => ({
    page, avgKB: +(s.kb / s.calls).toFixed(1), calls: s.calls,
    pathRatio: s.pathCalls / s.calls,
    burst: countBurst(logs.filter(l => l.page === page), AUDIT_RULES.minIntervalMs),
    issues: s.tooBig.length ? `超标 ${s.tooBig.length} 次` : null,
  }));
}
function countBurst(list, minMs) {                            // 相邻间隔 < minMs 的连续次数
  let n = 0; for (let i = 1; i < list.length; i++)
    if (list[i].t - list[i - 1].t < minMs) n++;
  return n;
}
```
