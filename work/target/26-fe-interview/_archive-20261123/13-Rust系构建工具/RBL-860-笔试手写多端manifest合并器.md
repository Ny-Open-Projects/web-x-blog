---
title: [RBL-860] 笔试：手写多端 manifest 合并器（优先级 + 冲突告警 + 跨端引用）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-860：笔试：手写多端 manifest 合并器（优先级 + 引用校验）

**需求**：实现 `mergeManifests(manifests)`。manifests: `Record<end, { buildId, files: Array<{ name, bytes, refs?: string[] }> }>`。规则：1) 按 PRECEDENCE（['ssr','edge','cdn','web']）顺序合并：同名冲突保留先到的（高优先端）并收集 warning；2) 输出 outputs: `Record<name, { end, bytes, refs }>` 与 deployments（各端 buildId）；3) 跨端引用校验：refs 指向不存在的输出 → fail（抛错列出缺失）；4) 未列在 PRECEDENCE 的端忽略 + warning。边界：manifests 空；files 空。

```javascript
const PRECEDENCE = ['ssr', 'edge', 'cdn', 'web'];

function mergeManifests(manifests = {}) {
  const warnings = [];
  const outputs = {}, deployments = [];
  for (const end of PRECEDENCE) {
    const m = manifests[end];
    if (!m) continue;
    for (const f of m.files ?? []) {
      if (outputs[f.name]) {
        warnings.push(`重名冲突: ${f.name} 属于 ${outputs[f.name].end} 与 ${end}——按优先级保留 ${outputs[f.name].end}`);
        continue;
      }
      outputs[f.name] = { end, bytes: f.bytes, refs: f.refs ?? [] };
    }
    deployments.push({ end, buildId: m.buildId });
  }
  for (const end of Object.keys(manifests))
    if (!PRECEDENCE.includes(end))
      warnings.push(`未知端 '${end}' 已忽略（PRECEDENCE 外）`);
  // 跨端引用校验
  const missing = [];
  for (const [name, o] of Object.entries(outputs))
    for (const ref of o.refs)
      if (!outputs[ref]) missing.push(`${name} -> ${ref}`);
  if (missing.length) throw new Error(`跨端引用缺失: ${missing.join(', ')}`);
  return { outputs, deployments, warnings };
}

// 自测
const manifests = {
  ssr: { buildId: 's1', files: [{ name: 'server.js', bytes: 100, refs: ['shared.js'] }] },
  web: { buildId: 'w1', files: [
    { name: 'index.html', bytes: 50, refs: ['main.js', 'server.js'] },   // server.js 跨端引用
    { name: 'main.js', bytes: 200 } ] },
  edge: { buildId: 'e1', files: [{ name: 'main.js', bytes: 999 }] },     // 冲突：web 先? precedence: edge 先
  cdn: { buildId: 'c1', files: [{ name: 'logo.png', bytes: 10 }] },
  weird: { buildId: '?', files: [] },                                    // 未知端
};
let r = mergeManifests(manifests);
console.log(r.outputs['main.js'].end === 'edge');        // edge 优先于 web
console.log(r.outputs['server.js'].end === 'ssr');       // 跨端引用 ssr 的输出存在
console.log(r.deployments.length === 4);
console.log(r.warnings.some(w => w.includes('重名冲突')));
console.log(r.warnings.some(w => w.includes("未知端 'weird'")));

// 引用缺失
let e; try {
  mergeManifests({ web: { buildId: 'w', files: [{ name: 'a.js', bytes: 1, refs: ['ghost.js'] }] } });
} catch (x) { e = x; }
console.log(/引用缺失.*ghost\.js/.test(e.message));

console.log(mergeManifests({}).outputs);
console.log(mergeManifests({ web: { buildId: 'w', files: [] } }).deployments.length === 1);
```

**评分点**：
- 优先级序合并正确（先到先得 + 冲突告警收集）；未列端忽略 + warning
- 跨端引用完整性校验（缺失聚合抛错）；deployments 记录各端 buildId（跨端原子性 RBL-700）
- 边界：空 manifests/files 安全
- 能说清「文件名空间分端隔离是结构性预防，优于执行层仲裁」属于加分
