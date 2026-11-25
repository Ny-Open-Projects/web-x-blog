---
title: [PER-1264] 手写一个权限点 diff 评审器：路由变更的权限一致性
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1264：手写一个权限点 diff 评审器：路由变更的权限一致性

**答**：
- 需求：实现 permRouteDiff(before, after)。before/after 为 { route: perm }；输出 { added, removed, changed }；added/changed 的路由必须已在 PERM_REGISTRY 中注册（否则违规 unregistered）；changed 需说明旧->新；输出 { ok, report }。
- 边界：删除路由若在 REGISTRY 中标记 deprecated 正常，否则提示清理注册表；空 diff 直接 ok。
- 评分点：三类 diff；注册校验；删除提示；报告生成

```javascript
function permRouteDiff(before, after, registry) {
  const added = [], removed = [], changed = [], unregistered = [];
  const routes = new Set([...Object.keys(before), ...Object.keys(after)]);
  for (const r of routes) {
    const b = before[r], a = after[r];
    if (b === a) continue;
    if (b === undefined) {
      added.push({ route: r, perm: a });
      if (!registry[a]) unregistered.push({ route: r, perm: a });
    } else if (a === undefined) removed.push({ route: r, perm: b });
    else {
      changed.push({ route: r, from: b, to: a });
      if (!registry[a]) unregistered.push({ route: r, perm: a });
    }
  }
  return { ok: !unregistered.length, added, removed, changed, unregistered,
    report: unregistered.length
      ? `新增权限点未注册: ${unregistered.map(u => u.perm).join(',')}` : '权限一致' };
}
```
