---
title: [NODE-773] 笔试题——实现响应脱敏序列化器（出口统一）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-773：手写出口脱敏

**需求与边界**：
- 需求：出口统一脱敏（SCN-NODE-698）——① schema 驱动（PII 字段标记——SCN-联想-584）；② 场景策略（partial/full/hidden——SCN-FIN-544）；③ 深层对象递归脱敏（嵌套对象/数组——列表项内也要）；④ 性能（大响应的脱敏开销——懒序列化/缓存 schema 编译）。
- 边界：① 未知字段默认 hidden（fail-closed——SCN-FIN-544 安全默认）；② 白名单放行（某些场景需要明文——显式声明 + 审计）；③ schema 与 PII 标记对齐（CI 校验——SCN-联想-584）。

**答**：
```javascript
function maskSerializer(schema, { scene = 'partial' } = {}) {
  const compiled = compileMask(schema, scene);         // schema 编译缓存（性能）
  return (data) => deepMask(data, compiled);           // 深层递归
}
function deepMask(obj, rules) {
  if (Array.isArray(obj)) return obj.map(x => deepMask(x, rules));   // 数组项脱敏
  if (typeof obj !== 'object' || !obj) return obj;
  const out = {};
  for (const [k, v] of Object.entries(obj)) {
    const rule = rules[k];
    if (rule === undefined) { out[k] = '******'; continue; }   // 未知字段 hidden（fail-closed——SCN-FIN-544）
    if (rule.type === 'hidden') { out[k] = '******'; continue; }
    out[k] = rule.children ? deepMask(v, rule.children) : rule.mask(v);
  }
  return out;
}
// CI：schema PII 标记与脱敏规则对齐（SCN-联想-584）
test('schema PII 与脱敏规则对齐', () => {
  for (const f of piiFields(UserSchema))
    assert(rules[f.name], `字段 ${f.name} 缺脱敏规则`);
});
```

**评分点**:
- schema 编译驱动（性能——SCN-FIN-544）。
- 深层递归脱敏（数组/嵌套全覆盖）。
- 未知字段 fail-closed hidden（安全默认值）。
- CI 对齐校验（schema PII 与规则——SCN-联想-584）。
