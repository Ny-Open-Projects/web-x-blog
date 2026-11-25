---
title: [HW-179] 手写模块耗时基线——mark/measure 包装 + 启动分阶段水位 + 版本对比基线固化
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-179：手写模块耗时基线——mark/measure 包装 + 启动分阶段水位 + 版本对比基线固化
**答**：启动分阶段耗时基线：按里程碑打 mark（HTML 解析完/核心 bundle 执行完/首屏组件挂载/交互就绪）→ measure 出各段时长 → 与固化基线（budgets.json 式）对比，CI 中回归即拦。包装器保证 mark 幂等（重复调用不重复计）与异常安全。

```javascript
const MILESTONES = ['html-parsed', 'core-executed', 'first-mounted', 'interactive'];
const marks = new Set();
function markStage(name) {
  if (marks.has(name)) return;                            // 幂等
  marks.add(name);
  try { performance.mark(`stage:${name}`); } catch {}
}
function measureStages() {
  const out = {};
  for (let i = 1; i < MILESTONES.length; i++) {
    const a = performance.getEntriesByName(`stage:${MILESTONES[i - 1]}`)[0];
    const b = performance.getEntriesByName(`stage:${MILESTONES[i]}`)[0];
    if (a && b) out[`${MILESTONES[i - 1]}→${MILESTONES[i]}`] = Math.round(b.startTime - a.startTime);
  }
  const t0 = performance.getEntriesByName('stage:html-parsed')[0];
  const tEnd = performance.getEntriesByName('stage:interactive')[0];
  if (t0 && tEnd) out.total = Math.round(tEnd.startTime - t0.startTime);
  return out;
}
// CI 基线对比（budgets.json 式）：
// { "stage.total": 1200, "core-executed→first-mounted": 400 } — 回归 > 10% 拦 PR（PER-339）
// 里程碑插桩位置：
//   html-parsed: DOMContentLoaded / core-executed: main.js 末尾 / first-mounted: 首屏组件 useEffect / interactive: PER-232 双条件
```

**评分点**：
- 分阶段里程碑（四段各对应真实插桩点）+ measure 段间时长。
- mark 幂等与异常安全。
- CI 基线对比（回归拦 PR，PER-339 语义）。
- interactive 里程碑复用 PER-232 双条件（mark+主线程空闲）。
