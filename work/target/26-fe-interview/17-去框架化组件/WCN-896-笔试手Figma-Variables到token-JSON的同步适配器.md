---
title: [WCN-896] 笔试：手写 Figma Variables → token JSON 的同步适配器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-896：笔试：手写 Figma Variables → token JSON 的同步适配器

**题目**：实现 `figmaToTokens(figmaData, { mode = 'Light' })`。Figma Variables API 返回形如 `{ variables: { [id]: { name, variableCollectionId, valuesByMode: { [modeId]: value }, resolvedType } }, collections: { [id]: { name, modes: { [modeId]: modeName } } } }`。要求：① 找到 modeName 等于入参 mode 的 modeId（跨集合）；② 把每个 variable 转成扁平 token key（name 中 `/` 转 `.`，小写，如 `Color/Brand/500` → `color.brand.500`），值为该 modeId 对应的值；③ 处理别名——若值是 `{ type: 'VARIABLE_ALIAS', id }`，解析为被引用变量的 token key（输出形如 `'{color.brand.500}'` 的引用字符串），支持一层与链式别名（需防循环）；④ 按 resolvedType 做值规范化（COLOR 转 `#rrggbb`，FLOAT 转数值）。边界：mode 找不到时用第一个集合的默认模式；别名指向不存在的变量保留原样并标记。

**答**：

```javascript
function figmaToTokens(data, { mode = 'Light' } = {}) {
  const { variables = {}, collections = {} } = data;
  // 找到目标 modeId（取第一个匹配）
  let targetModeId = null;
  for (const col of Object.values(collections)) {
    for (const [mid, mname] of Object.entries(col.modes || {})) {
      if (mname === mode && !targetModeId) targetModeId = mid;
    }
  }
  if (!targetModeId) { // 兜底：第一个集合的默认模式
    const first = Object.values(collections)[0];
    targetModeId = first ? Object.keys(first.modes || {})[0] : null;
  }
  const keyOf = (name) => name.replace(/\//g, '.').toLowerCase();
  const idToKey = new Map(Object.values(variables).map(v => [v.id, keyOf(v.name)]));
  function normColor(c) {
    if (!c) return c;
    const hex = (n) => Math.round(n * 255).toString(16).padStart(2, '0');
    return `#${hex(c.r)}${hex(c.g)}${hex(c.b)}`;
  }
  function resolve(v, seen = new Set(), depth = 0) {
    if (depth > 20 || seen.has(v.id)) return '{CIRCULAR}'; // 防循环
    seen.add(v.id);
    const raw = v.valuesByMode?.[targetModeId];
    if (raw && raw.type === 'VARIABLE_ALIAS') {
      const target = variables[raw.id];
      return target ? `{${idToKey.get(raw.id) || resolve(target, seen, depth + 1)}}` : '{UNRESOLVED}';
    }
    if (v.resolvedType === 'COLOR') return normColor(raw);
    return raw; // FLOAT / STRING 直接返回
  }
  const tokens = {};
  for (const v of Object.values(variables)) tokens[keyOf(v.name)] = resolve(v);
  return tokens;
}
// 用法：figmaToTokens(figmaResponse, { mode: 'Dark' }) → { 'color.brand.500': '#2563eb', ... }
```

**评分点**：
- modeName → modeId 映射 + 默认模式兜底（正确定位主题值）。
- key 扁平化与别名解析（含 `{引用}` 语义），链式别名防循环（核心难点）。
- COLOR/FLOAT 值规范化（对齐 DTCG token 格式）。
- 未解析别名/循环的边界处理（健壮性）。
