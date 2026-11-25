---
title: [NODE-809] 笔试题——实现 BFF 协议适配层（老 App 字段兼容映射）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-809：手写协议适配

**需求与边界**：
- 需求：老版本 App 协议兼容（SCN-NODE-712/694）——① 字段映射（新字段 → 老字段名——schema 版本映射表）；② 值转换（枚举值变更——v2 状态 → v1 状态映射）；③ 删字段的降级（老版本依赖的字段被删——降级值填充）；④ 版本检测（x-client-ver 路由适配器）。
- 边界：① 映射表版本化（每个 App 版本的映射——SCN-OPS-694 版本治理）；② 映射的 CI 校验（fixture 快照——SCN-BLD-299）；③ 降级值的声明（哪些字段能降级——语义单源约束，SCN-NODE-712）。

**答**：
```javascript
// 兼容映射表（per App 版本）
const COMPAT = {
  '3.1': { fields: { discount: { from: 'promo', transform: v => v.amount },
    status: { from: 'state', map: { ACTIVE: 'ON', CLOSED: 'OFF' } },   // 枚举值映射
    removedField: { default: null } } },               // 删字段降级（SCN-NODE-809）
  '3.2': null,                                         // 无需兼容
};
function adaptForClient(data, clientVer) {
  const rules = COMPAT[clientVer];
  if (!rules) return data;                             // 新版本直通
  return deepMap(data, (k, v) => {
    const rule = rules.fields[k];
    if (rule?.from) return [rule.from ?? k, rule.map ? rule.map[v] ?? rule.default : v];   // 改名+转换
    if (rule && rule.default !== undefined) return [k, rule.default];   // 删字段降级
    return [k, v];
  });
}
```

**评分点**:
- 映射表 per 版本（SCN-OPS-694 版本治理）。
- 枚举值映射（状态转换——语义兼容）。
- 删字段降级声明（default——SCN-NODE-712 语义单源约束）。
- deepMap 深层适配（嵌套/列表全覆盖）。
