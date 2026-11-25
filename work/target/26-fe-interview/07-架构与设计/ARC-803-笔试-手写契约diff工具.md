---
title: [ARC-803] 笔试：手写契约 diff 工具
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 笔试题, 协作]
type: 笔试题
---

## ARC-803：笔试：手写契约 diff

**答**：实现 API 契约 diff 工具 `diffContract(oldSpec, newSpec)`：① 输入 OpenAPI 风格契约：{ paths: { '/api/x': { get: { params, response } } } }；② 变更分类：breaking（删除字段/改必填/改类型）、non-breaking（新增可选字段/新增接口）、deprecation（标记弃用）；③ 输出变更清单：{ path, method, change, breaking }——breaking 变更需要版本号升级的校验；④ 消费方影响分析：传入「消费方清单」（哪些前端用哪些接口）→ 标注受影响团队；⑤ CI 集成：breaking 变更无版本号升级 → exit 1。写出实现。

```javascript
function diffContract(oldSpec, newSpec, consumers = []) {
  const changes = [];
  const oldPaths = oldSpec.paths, newPaths = newSpec.paths;
  // 删除的接口/方法 = breaking
  for (const [path, methods] of Object.entries(oldPaths)) {
    if (!newPaths[path]) { changes.push({ path, change: 'removed', breaking: true }); continue; }
    for (const method of Object.keys(methods)) {
      const oldM = methods[method], newM = newPaths[path]?.[method];
      if (!newM) { changes.push({ path, method, change: 'method-removed', breaking: true }); continue; }
      // response 字段 diff
      for (const f of Object.keys(oldM.response ?? {})) {
        if (!(f in (newM.response ?? {})))
          changes.push({ path, method, change: `response-field-removed: ${f}`, breaking: true });
        else if (oldM.response[f] !== newM.response[f])
          changes.push({ path, method, change: `response-type-changed: ${f} ${oldM.response[f]}→${newM.response[f]}`, breaking: true });
      }
      for (const f of Object.keys(newM.response ?? {}))
        if (!(f in (oldM.response ?? {})))
          changes.push({ path, method, change: `response-field-added: ${f}`, breaking: false });
      if (newM.deprecated) changes.push({ path, method, change: 'deprecated', breaking: false });
    }
  }
  // 新增接口
  for (const path of Object.keys(newPaths))
    if (!oldPaths[path]) changes.push({ path, change: 'added', breaking: false });

  const hasBreaking = changes.some((c) => c.breaking);
  const affectedTeams = [...new Set(consumers
    .filter((c) => changes.some((ch) => c.uses.includes(ch.path)))
    .map((c) => c.team))];
  const versionOk = !hasBreaking || newSpec.version > oldSpec.version;
  if (hasBreaking && !versionOk) { console.error('BREAKING 变更未升级版本号'); process.exit(1); }
  return { changes, hasBreaking, affectedTeams, versionOk };
}
```

**评分点**：
- 三类变更分类（breaking/non-breaking/deprecation）
- response 字段级 diff（删除/类型变化 = breaking）
- 消费方影响分析（变更 → 受影响团队标注）
- CI 集成（breaking 无版本升级 exit 1）
