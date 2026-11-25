---
title: [RBL-786] 笔试：手写 stats.json 消费方 lint（废弃字段检测 + 版本适配建议）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-786：笔试：手写 stats.json 消费方 lint（废弃字段 + 版本适配）

**答**：实现 `lintConsumer(code, schema)`。schema: `{ version, deprecated: Record<fieldPath, { use, since, removal }>, experimental: string[] }`. 规则：1) 代码访问 deprecated 字段路径（支持点路径与可选链形式 `stats.outputs` / `stats?.outputs`）→ warn `{ field, use, removal }`；2) 访问 experimental 字段 → info 'unstable-field'；3) 代码含 `schemaVersion` 判断 → ok 提示 'version-aware'（好实践）；4) fieldPath 支持通配 `chunks[].size`（匹配任意中间下标访问 `.chunks[i].size` 与 `.map(c => c.size)` 形式简化为文本 includes）；5) 返回 `{ findings: Array<{ level, field?, message }>, versionAware }`。边界：无 deprecated；schema 缺 experimental。

```javascript
function lintConsumer(code, schema = {}) {
  const findings = [];
  const norm = (s) => s.replace(/\?\./g, '.').replace(/\[\d+\]/g, '[]');
  const ncode = norm(code);

  for (const [field, meta] of Object.entries(schema.deprecated ?? {})) {
    const patterns = [field, field.replace('[]', '')];
    if (patterns.some(p => ncode.includes(p)))
      findings.push({ level: 'warn', field,
        message: `已废弃（${meta.since} 弃用，${meta.removal} 移除）——改用 ${meta.use}` });
  }
  for (const exp of schema.experimental ?? [])
    if (ncode.includes(exp))
      findings.push({ level: 'info', field: exp, message: 'unstable-field：实验字段不承诺兼容' });
  const versionAware = /schemaVersion/.test(code);
  if (versionAware) findings.push({ level: 'info', message: 'version-aware：已做版本适配（好实践）' });
  return { findings, versionAware };
}

// 自测
const schema = {
  version: '2.1',
  deprecated: { 'chunks[].size': { use: 'outputs[].bytes', since: '2.0', removal: '3.0' } },
  experimental: ['phaseTimings'],
};
let r = lintConsumer('const size = stats.chunks[0].size;', schema);
console.log(r.findings[0].field === 'chunks[].size' && r.findings[0].level === 'warn');
console.log(r.versionAware === false);

r = lintConsumer('const s = stats?.chunks?.size ?? 0; if (stats.schemaVersion === 2) {...}', schema);
console.log(r.findings.some(f => f.field === 'chunks[].size'));
console.log(r.versionAware === true);

r = lintConsumer('console.log(stats.experimental.phaseTimings)', schema);
console.log(r.findings.some(f => f.level === 'info' && f.field === 'phaseTimings'));

r = lintConsumer('const a = stats.outputs.bytes;', schema);
console.log(r.findings.length === 1 && r.findings[0].message.includes('version-aware'));  // 仅 versionAware 提示? 无——outputs 无废弃
console.log(lintConsumer('x.y', schema).findings.length === 0);
```

**评分点**：
- 废弃字段检测（点路径 + 可选链规范化）；通配下标形式兼容
- experimental 字段 info 级、versionAware 好实践提示
- 边界：无废弃字段、无匹配安全
- 能说清「宽容读取 + 严格生成的 Postel 法则在 stats.json 生态的应用」属于加分
