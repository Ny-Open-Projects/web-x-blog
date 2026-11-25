---
title: [RBL-074] 笔试：手写简化 Tree Shaking（导出标记 + 未引用剔除）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-074：笔试：手写简化 Tree Shaking（导出标记 + 未引用剔除）
**答**：给定模块 { id, exports: ['a','b'], imports: [{ from: 1, names: ['a'] }] }，实现 treeShake(modules)：1) 从入口模块的具名导入反向传播"被使用导出"标记；2) 未被标记的导出从模块的导出清单剔除；3) 一个模块所有导出都未被引用且声明无副作用时整模块剔除；4) sideEffects: false 语义支持（未导入即剔除）；5) re-export 链（A re-export B 的 a）正确传播。

```javascript
function treeShake(modules) { // modules: [{id, imports:[{from,names}], exports:[...], sideEffectsFree}]
  const used = new Map();                  // moduleId -> Set<被使用的导出名>
  for (const m of modules) used.set(m.id, new Set());

  // 1) 入口的 imports 反向传播（简化：所有模块的 import 视为"使用"）
  const queue = [];
  for (const m of modules) {
    for (const imp of m.imports) {
      for (const name of imp.names) {
        const target = modules.find(x => x.id === imp.from);
        if (target && target.exports.includes(name)) {
          if (!used.get(imp.from).has(name)) { used.get(imp.from).add(name); queue.push(imp.from); }
        } else if (target && !target.exports.includes(name)) {
          // re-export：A 模块 re-export 了 name（从其 import 透传），继续向下游传播
          const inner = target.imports.find(i => i.names.includes(name));
          if (inner) { used.get(inner.from).add(name); queue.push(inner.from); }
          used.get(target.id).add(name); // re-export 语句本身算使用
        }
      }
    }
  }
  // 2) 剔除未使用导出 / 整模块
  const result = [];
  for (const m of modules) {
    const usedNames = used.get(m.id);
    const keptExports = m.exports.filter(n => usedNames.has(n));
    if (keptExports.length === 0) {
      if (m.sideEffectsFree) continue;      // 无副作用且全未用 → 整模块摇除
      result.push({ ...m, exports: [], reason: 'side-effect' });
    } else {
      result.push({ ...m, exports: keptExports });
    }
  }
  return result;
}
module.exports = { treeShake };
```
**评分点**：
- 反向标记：从"被导入的名字"反推导出使用（方向正确性）。
- re-export 链传播（A→B→C 的名字透传，易漏）。
- 全未用 + sideEffectsFree → 整模块剔除（两条条件缺一不可）。
- 有副作用模块保留但剔除未用导出（分层语义）。
- 能说出 /*#__PURE__*/ 与动态访问是标记分析的边界。
