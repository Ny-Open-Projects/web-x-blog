---
title: [BLD-317] 笔试题——实现构建配置 schema 校验器（防呆 + 建议修复）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-317：手写配置校验器

**需求与边界**：
- 需求：构建配置的 schema 校验（SCN-BLD-248）——① 未知字段检测（拼写建议——编辑距离最近字段）；② 互斥冲突检测（同一模块同时配 loader 与 plugins）；③ 值校验（路径存在/define 字面量——SCN-BLD-229）；④ 输出全部问题（非首个）+ 可行动修复。
- 边界：① 未知字段警告级（合法扩展不破坏——SCN-BLD-248 甜点）；② 路径校验延迟到运行时（构建时才解析）；③ 建议（did you mean）用编辑距离阈值（<3）。

**答**：
```javascript
function validateConfig(config, schema) {
  const issues = [];
  const walk = (obj, path) => {
    for (const [k, v] of Object.entries(obj)) {
      const p = [...path, k].join('.');
      const known = lookupSchema(schema, p);
      if (!known) {
        const nearest = nearestField(schema, k);       // 编辑距离最近字段
        issues.push({ path: p, type: 'UNKNOWN_FIELD', level: 'warn',
          suggest: nearest ? `是否想配 ${nearest}？（距离 ${lev(k, nearest)}）` : null });
        continue;                                      // 未知字段不深走（可能是插件自定义）
      }
      if (known.type === 'literal' && (typeof v !== 'string' && typeof v !== 'boolean' && typeof v !== 'number'))
        issues.push({ path: p, type: 'NOT_LITERAL', level: 'error',
          note: 'define 值必须字面量（否则 DCE 失效——SCN-BLD-229）' });
      if (known.pathExists && !fs.existsSync(v))
        issues.push({ path: p, type: 'PATH_MISSING', level: 'error', fix: `检查路径 ${v}` });
      if (typeof v === 'object' && !Array.isArray(v)) walk(v, [...path, k]);
    }
  };
  walk(config, []);
  for (const c of CONFLICT_RULES)                      // 互斥规则
    if (c.paths.every(p => lookup(config, p)))
      issues.push({ type: 'CONFLICT', paths: c.paths, level: 'warn', note: c.msg });
  return issues.sort((a, b) => LEVEL[a.level] - LEVEL[b.level]);
}
```

**评分点**:
- 四类校验（未知/字面量/路径/互斥）全输出。
- 拼写建议（编辑距离最近字段——可行动）。
- define 字面量约束（DCE 协作——SCN-BLD-229）。
- 未知字段警告级不阻断（扩展性平衡——SCN-BLD-248）。
