---
title: [NODE-804] 笔试题——实现 BFF 字段裁剪引擎（schema 驱动 + 端 profile）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-804：手写裁剪引擎

**需求与边界**：
- 需求：字段裁剪引擎（SCN-NODE-712）——① schema 声明裁剪（per 端 profile 字段白名单）；② 深层裁剪（嵌套对象/列表项——递归）；③ 必留字段保护（id/语义字段不裁——SCN-NODE-712 语义单源）；④ 裁剪率统计（字段裁剪率——带宽收益度量）。
- 边界：① profile 优先级（端版本 > 端类型 > 默认——SCN-NODE-712 端探测）；② 裁剪的性能（大响应深层递归——编译 schema 缓存，SCN-FIN-773 同构）；③ 裁剪后的一致性校验（必留字段缺失告警——裁剪 bug 哨兵）。

**答**：
```javascript
function createTrimmer(profiles) {
  const compiled = new Map();                          // profile → 编译后规则（性能）
  return (data, profileName) => {
    const rules = compiled.get(profileName) ?? compile(profiles[profileName]);
    const out = deepTrim(data, rules, { dropped: 0 });
    if (!PROTECTED.every(f => out[f] !== undefined))    // 必留字段哨兵（SCN-NODE-712 语义单源）
      alert({ type: 'TRIM_LOST_SEMANTIC', profile: profileName });
    telemetry.push({ profile: profileName, droppedPct: out.droppedPct });   // 裁剪率（带宽收益）
    return out;
  };
  function deepTrim(obj, rules, stat) {
    if (Array.isArray(obj)) return obj.map(x => deepTrim(x, rules, stat));
    if (typeof obj !== 'object' || !obj) return obj;
    const out = {};
    for (const [k, v] of Object.entries(obj)) {
      const r = rules[k];
      if (r === false || (r === undefined && rules['*'] === false)) { stat.dropped++; continue; }   // 白名单裁剪
      out[k] = r?.children ? deepTrim(v, r.children, stat) : v;
    }
    return out;
  }
}
// profiles 声明
{ 'app-ios:3.2': { fields: { id: true, title: true, price: true, cover: true, desc: false } },
  pc: { fields: { '*': true } } }
```

**评分点**:
- schema 声明裁剪 + 编译缓存（SCN-FIN-773 同构性能）。
- 深层递归（嵌套/列表全覆盖）。
- 必留字段哨兵（语义单源保护——SCN-NODE-712）。
- 裁剪率统计（带宽收益可度量）。
