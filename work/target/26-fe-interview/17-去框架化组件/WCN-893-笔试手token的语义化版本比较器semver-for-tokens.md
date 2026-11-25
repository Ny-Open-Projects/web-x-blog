---
title: [WCN-893] 笔试：手写 token 的「语义化版本比较器」（semver for tokens）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-893：笔试：手写 token 的「语义化版本比较器」（semver for tokens）

**题目**：实现 `compareTokenSchemas(oldSchema, newSchema)`，比较两个 token schema（形如 `{ 'color.primary': '#06c', 'spacing.md': '8px' }`），返回建议的版本变更。要求：① 删除或重命名 token（旧 key 不在新 schema）→ `{ level: 'major', ... }`；② 新增 token（新 key 不在旧 schema）→ `minor`；③ 仅值变化（key 都在但值不同）→ `patch`；④ 无变化 → `none`；⑤ 多条同时存在时取最高级别（major > minor > patch > none），并列出所有 change 明细（每条 `{ type, key, from, to }`）。边界：值为 0/false/空字符串也算有效变化（不能用 truthy 判断）；嵌套扁平化的 key（用 `.` 分隔）；schema 为 null 按空对象处理。

**答**：

```javascript
const LEVEL = { none: 0, patch: 1, minor: 2, major: 3 };
function compareTokenSchemas(oldSchema, newSchema) {
  const a = oldSchema || {}, b = newSchema || {};
  const changes = [];
  let maxLevel = 'none';
  const bump = (lvl) => { if (LEVEL[lvl] > LEVEL[maxLevel]) maxLevel = lvl; };

  for (const key of Object.keys(a)) {
    if (!(key in b)) {
      changes.push({ type: 'removed', key, from: a[key], to: undefined }); bump('major');
    }
  }
  for (const key of Object.keys(b)) {
    if (!(key in a)) {
      changes.push({ type: 'added', key, from: undefined, to: b[key] }); bump('minor');
    } else if (!Object.is(a[key], b[key])) {
      changes.push({ type: 'changed', key, from: a[key], to: b[key] }); bump('patch');
    }
  }
  return { level: maxLevel, changes };
}
console.log(compareTokenSchemas(
  { 'color.primary': '#06c', 'spacing.md': '8px', 'flag': false },
  { 'color.primary': '#06f', 'flag': true, 'radius.sm': '4px' },
)); // level: minor（有新增），changes 含 changed×2 + added×1
console.log(compareTokenSchemas({ a: '1' }, {}).level); // major
```

**评分点**：
- 删除=major、新增=minor、值变=patch 的语义判定正确（核心）。
- 多变更取最高级别（LEVEL 权重比较），逻辑清晰。
- 用 `in`/`Object.is` 而非 truthy 判断，正确处理 false/0/空串（边界易错点）。
- changes 明细完整、null schema 兜底（健壮性/可用性）。
