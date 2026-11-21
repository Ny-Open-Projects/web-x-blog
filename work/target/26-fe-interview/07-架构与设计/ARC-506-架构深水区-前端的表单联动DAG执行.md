---
title: [ARC-506] 复杂表单联动的 DAG 执行引擎如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-506：表单联动 DAG 执行引擎
**答**:
- 问题：字段间联动（A 变 → B 重算 → C 级联）写散乱时序代码，循环依赖与重复计算难控。解法：依赖关系声明为 DAG（字段为节点，依赖为边），变更沿图传播。
- 引擎设计：依赖图静态构建（schema 声明 dependsOn）→ 变更入队 → 拓扑序批处理（一个事件循环内收集所有 dirty 节点按依赖序计算一次——合并联动风暴）→ 循环依赖在构建期拒绝。
- 计算语义：计算字段（derived）不可直接编辑；异步联动（远端选项加载）作为惰性节点（需要时取数 + 竞态保护 ARC-383）。
- 与校验集成：依赖变更自动触发关联字段重校验（ARC-384 联动校验）。
- 调试：联动链可视化（变更传播路径回放，ARC-491）、计算次数统计（防过度联动）。
```javascript
class FormDag {
  #deps = new Map();   // field -> [deps]
  #computed = new Map();
  onChange(field) {
    const dirty = topoSort(collectDownstream(field, this.#deps));  // 收集下游并排序
    const batch = new Set(dirty);                                  // 本 tick 合并
    for (const f of batch) this.#computed.get(f)?.recompute();
  }
  static validateAcyclic(deps) {                                   // 构建期防环
    try { topoSort(Object.keys(deps)); } catch { throw new Error('联动循环依赖'); }
  }
}
```
