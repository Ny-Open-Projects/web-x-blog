---
title: [ENG-291] 笔试题——实现 Ratchet 基线管理器（只紧不松的预算机制）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-291：手写 Ratchet 基线管理器

**需求与边界**：
- 需求：维护多指标基线（bundle size/build 时长/错误数）；当前值优于基线时自动下调（棘轮收紧），劣于基线时拒绝并提示需显式提额；提额需 PR 说明（记录在基线文件历史）。
- 边界：① 下调自动（改进即收紧）；② 上调必须带 reason 与 PR 引用；③ 基线文件进 Git 可评审；④ 指标方向感知（越小越好 vs 越大越好，如覆盖率越大越好）。

**答**：
```javascript
const DIRECTION = { 'bundle-gzip': 'down', 'build-ms': 'down', 'coverage': 'up', 'ts-errors': 'down' };
function ratchet(file, metric, current, { reason, prRef } = {}) {
  const baselines = readJson(file);                  // { metric: { value, history: [] } }
  const dir = DIRECTION[metric];
  if (!dir) throw new Error(`未注册指标 ${metric}`);
  const base = baselines[metric]?.value ?? current;
  const improved = dir === 'down' ? current < base : current > base;
  const regressed = dir === 'down' ? current > base : current < base;
  if (improved) {                                    // 改进：自动收紧
    baselines[metric] = { value: current,
      history: [...(baselines[metric]?.history ?? []), { to: current, auto: true, at: Date.now() }] };
    writeJson(file, baselines);
    return { ok: true, tightened: base - current };
  }
  if (regressed) {
    if (!reason || !prRef)                           // 上调必须显式
      return { ok: false, msg: `${metric} 劣化 ${current} vs 基线 ${base}，需提额 PR（reason + prRef）` };
    baselines[metric] = { value: current,
      history: [...(baselines[metric]?.history ?? []), { to: current, reason, prRef, at: Date.now() }] };
    writeJson(file, baselines);
    return { ok: true, raised: true };
  }
  return { ok: true };
}
```

**评分点**:
- 方向感知（down/up 双向棘轮）。
- 收紧自动化 + 提额显式化（reason+prRef 审计）。
- 基线历史记录（谁/何时/为何调整可追溯）。
- 基线文件进 Git（变更可评审）。
