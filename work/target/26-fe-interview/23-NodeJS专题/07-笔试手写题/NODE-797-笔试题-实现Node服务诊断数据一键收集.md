---
title: [NODE-797] 笔试题——实现诊断一键收集（heap/profile/状态快照）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-797：手写一键诊断

**需求与边界**：
- 需求：一键诊断收集（SCN-NODE-704）——① 全量快照（heap dump/CPU profile 10s/运行时状态/最近错误——SCN-NODE-704 一键全貌）；② 摘流执行（诊断期间 readiness off——SCN-NODE-743 纪律）；③ 快照上传（对象存储——值班拉取分析）；④ 收集超时与失败兜底（诊断本身不挂服务）。
- 边界：① CPU profile 的时长控制（10s 采样——开销可控）；② heap dump 的内存峰值（dump 过程内存翻倍——大堆风险，分片 dump）；③ 收集任务的幂等（同实例 5 分钟内不重复——SCN-NODE-691）。

**答**：
```javascript
app.post('/internal/diag', internalOnly, singleFlight5m, async (req, res) => {
  const prevReady = state.ready;
  state.ready = false;                                 // 摘流执行（SCN-NODE-743 纪律）
  try {
    const [heap, cpu, runtime, errors] = await Promise.all([
      heapdumpAsync({ timeout: 30_000 }).catch(e => ({ err: e.message })),   // 失败兜底（不挂服务）
      cpuProfile(10_000),                              // 10s CPU 采样
      runtimeSnapshot(),                               // ELD/池/队列（SCN-NODE-704）
      ringBuffer.last(50),
    ]);
    const url = await uploadDiag({ heap, cpu, runtime, errors }, req.user);   // 上传（值班拉取）
    audit({ action: 'diag', by: req.user, url });
    res.json({ url });                                 // 签名直链（SCN-FIN-791）
  } finally { state.ready = prevReady; }               // 恢复流量
});
```

**评分点**:
- 摘流执行（诊断期间 readiness off——SCN-NODE-743 纪律）。
- 四件套收集（heap/CPU/runtime/errors——SCN-NODE-704）。
- 失败兜底（诊断不挂服务——catch 每项）。
- 上传签名直链 + 审计（值班拉取——SCN-FIN-791/OPS-220）。
