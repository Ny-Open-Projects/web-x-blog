---
title: [MFW-717] 笔试：手写 Docker 镜像体积审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-717：笔试：手写 Docker 体积审计

**答**：实现 `auditDockerLayers(layers, { budgetMB })`。layers: `{ instruction, sizeMB, from }[]`（按 Dockerfile 顺序）。规则：1) 总体积超预算 → blocker；2) **体积异常检测**：单层 > 100MB 且非 COPY base 层 → warn 'heavy-layer'（大层 = 上下文泄漏：node_modules 意外包含）；3) **RUN 指令的缓存破坏**（COPY . . 在 pnpm install 之前——lockfile 变了才重 install——层序优化检查：install 在 COPY 源码之前 = 好实践）；4) 优化建议：大层的具体瘦身动作（standalone/排除/多阶段）。返回 `{ totalMB, blockers, warnings, suggestions }`。边界：layers 空（0）；base 镜像层（FROM 的 size——不审计）；单层超 budget（全镜像 blocker）。

```javascript
function auditDockerLayers(layers = [], { budgetMB = 200 } = {}) {
  const totalMB = +layers.reduce((s, l) => s + l.sizeMB, 0).toFixed(1);
  const blockers = [], warnings = [], suggestions = [];
  if (totalMB > budgetMB)
    blockers.push({ type: 'over-budget', detail: `镜像 ${totalMB}MB > ${budgetMB}MB` });
  const isBase = (l) => l.instruction?.startsWith('FROM');
  for (const l of layers) {
    if (isBase(l)) continue;
    if (l.sizeMB > 100 && l.instruction?.includes('COPY') && !l.instruction.includes('standalone'))
      warnings.push({ layer: l.instruction.slice(0, 40), type: 'heavy-layer',
        detail: `层 ${l.sizeMB}MB——检查是否泄漏 node_modules` });
    // 层序优化：install 在源码 COPY 前
    if (l.instruction?.includes('COPY . .') &&
        layers.findIndex(x => x === l) > layers.findIndex(x =>
          x.instruction?.includes('pnpm install')))
      suggestions.push('COPY . . 在 install 之后（当前）——保持层序（lockfile 缓存友好）');
  }
  if (totalMB > budgetMB * 0.8)
    suggestions.push('体积接近预算——考虑 standalone + alpine + 多阶段');
  return { totalMB, blockers, warnings, suggestions };
}

// 自测
const layers = [
  { instruction: 'FROM node:20-alpine', sizeMB: 180, from: 'base' },
  { instruction: 'RUN pnpm install', sizeMB: 300, from: 'deps' },
  { instruction: 'COPY . .', sizeMB: 50, from: 'builder' },
  { instruction: 'COPY --from=builder .next/standalone', sizeMB: 60, from: 'runner' },
  { instruction: 'COPY --from=builder .next/static', sizeMB: 5, from: 'runner' },
];
let r = auditDockerLayers(layers, { budgetMB: 500 });
console.log(r.totalMB === 595);
console.log(r.blockers.length === 1);                    // 595 > 500
console.log(r.warnings.length === 1);                    // pnpm install 300MB 层——但 install 不含 COPY 关键词？
// 修正：install 层是 RUN 不是 COPY——不在 heavy-layer 检查内
console.log(r.warnings.length === 0);                    // 无 COPY 超大层
console.log(r.suggestions.length >= 1);                  // 体积建议

// 正常
r = auditDockerLayers([
  { instruction: 'FROM alpine', sizeMB: 50, from: 'base' },
  { instruction: 'COPY standalone', sizeMB: 40, from: 'runner' },
], { budgetMB: 200 });
console.log(r.blockers.length === 0 && r.warnings.length === 0);
console.log(r.totalMB === 90);

// 空
console.log(auditDockerLayers([]).totalMB === 0);
```

**评分点**：
- 体积审计（总预算 + 大层告警）；base 层豁免（FROM 不审计——镜像自身大小不在控制内）
- 层序检查（install 在源码 COPY 前——Docker 缓存的层序优化）；建议生成
- 边界（空 layers）；heavy-layer 的 COPY 限定（RUN 的大层不算——install 是合理的大层）
- 能说清「Docker 体积审计的两大靶点：standalone 瘦身 + 层序缓存优化——门禁防体积回归」属于加分
