---
title: [NODE-800] 笔试题——实现 Node 服务自检清单（三级收束可执行版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-800：手写服务自检清单

**需求与边界**：
- 需求：把 NODE-633~700 的方法论变成可执行自检（CI/上线前跑）——① 运行时检查（ELD 采样/heap 基线/GC 频率——SCN-NODE-671/635）；② 可靠性检查（优雅关闭演练/探针语义/池水位——SCN-NODE-738/743/726）；③ 一致性检查（幂等中间件存在/对账任务注册/缓存键维度——SCN-NODE-709/682/718）；④ 输出体检报告（分数 + 短板——SCN-ENG-330 成熟度模型复用）。
- 边界：① 检查项自动可执行（非人工勾选——每项有脚本断言）；② 检查分级（阻断/建议——SCN-OPS-229 分级）；③ 清单版本化（新方法论加入清单——演进）。

**答**：
```javascript
const CHECKS = {
  runtime: [
    { name: 'eld-p99', run: () => eldP99() < 100, level: 'warn' },          // SCN-NODE-721
    { name: 'heap-baseline', run: () => heapAfterGCStable(), level: 'warn' },   // SCN-NODE-672
    { name: 'graceful-drill', run: () => lastDrill('graceful') < 90, level: 'block' },   // SCN-NODE-722 演练
  ],
  reliability: [
    { name: 'probe-semantics', run: () => livenessNotCheckingDeps(), level: 'block' },   // SCN-NODE-743
    { name: 'pool-leak', run: () => leakedConns() === 0, level: 'warn' },    // SCN-NODE-726
  ],
  consistency: [
    { name: 'idempotent-middleware', run: () => hasIdempotent('/pay'), level: 'block' },   // SCN-NODE-735
    { name: 'recon-task', run: () => hasReconciliation(), level: 'block' },  // SCN-NODE-755
    { name: 'cache-key-dims', run: () => cacheKeysComplete(), level: 'warn' },   // SCN-NODE-718
  ],
};
async function selfCheck() {
  const results = [];
  for (const [dim, checks] of Object.entries(CHECKS))
    for (const c of checks) {
      const ok = await Promise.resolve(c.run()).catch(() => false);
      results.push({ dim, ...c, ok });
    }
  const blocked = results.filter(r => !r.ok && r.level === 'block');
  return { score: results.filter(r => r.ok).length / results.length,
    blocked,                                            // 阻断项（SCN-OPS-229）
    weakest: worstDim(results) };                       // 短板（SCN-ENG-330 木桶）
}
```

**评分点**:
- 方法论 → 可执行检查（每项有脚本断言——非人工勾选）。
- 三维检查（运行时/可靠性/一致性）+ 分级（block/warn——SCN-OPS-229）。
- 阻断项语义（不通过不发布）。
- 短板输出（木桶——SCN-ENG-330）。

## 变体与延伸（补充）

**变体与延伸**：

1. 检查项依赖真实 DB 与 Redis，CI 里怎么隔离 → 用 docker-compose 起依赖跑轻量项，重依赖项降级为夜间任务，绝不允许自检脚本连生产实例。
2. 阻断级检查误报导致发版卡住怎么办 → 每条检查支持豁免注解，需 owner 审批且带过期时间，豁免记录进报告留痕，禁止永久豁免。
3. 清单越加越多、跑一次 20 分钟怎么优化 → 按变更影响面选跑（改了缓存层只跑一致性组），全量留夜间，结果缓存后做 diff 只报新增失败。
