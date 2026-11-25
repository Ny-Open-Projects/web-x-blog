---
title: [BLD-293] 笔试题——实现 tree-shaking 标记器（导出使用分析）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-293：手写 tree-shaking 标记器

**需求与边界**：
- 需求：对 ESM 模块集做「导出使用分析」——① 从入口的 named imports 收集「已使用的导出」；② 沿 re-export 链传递（桶文件解引用）；③ 未使用导出标记 shake；④ 有副作用声明的模块豁免。
- 边界：① 动态访问（obj[key]）标记「不可分析」保守保留；② re-export 链跨模块追踪（export { a } from './b'）；③ 副作用豁免（sideEffects 白名单匹配）。

**答**：
```javascript
function shakeMark(modules, entries, sideEffectsWhitelist) {
  const usedExports = new Map();                       // moduleId -> Set(exportName)
  const queue = entries.map(id => ({ id, names: '*' }));   // 入口全量使用
  while (queue.length) {
    const { id, names } = queue.shift();
    const mod = modules[id];
    if (sideEffectsWhitelist.some(p => mod.path.includes(p))) {
      usedExports.set(id, new Set(['*']));             // 副作用模块全量保留（SCN-BLD-203）
      continue;
    }
    usedExports.set(id, new Set(names === '*' ? Object.keys(mod.exports) : names));
    for (const name of usedExports.get(id)) {
      const exp = mod.exports[name];
      if (!exp) continue;
      if (exp.reExport)                                // re-export 解引用（桶文件）
        queue.push({ id: exp.fromModule, names: exp.originalNames });
      if (exp.dynamicAccess)                           // 动态访问 → 保守保留
        usedExports.get(id).add('*');
    }
  }
  const shaken = Object.keys(modules).map(id => ({
    id, path: modules[id].path,
    shaken: [...(mod.exports ? Object.keys(modules[id].exports) : [])]
      .filter(n => !(usedExports.get(id)?.has(n) || usedExports.get(id)?.has('*'))),
  }));
  return shaken;
}
```

**评分点**:
- 使用分析传播（入口→named import→re-export 解引用）。
- 副作用白名单豁免（sideEffects 语义正确）。
- 动态访问保守保留（不可分析 fail-safe）。
- 输出 shaken 清单（摇树效果可度量——SCN-BLD-276）。
