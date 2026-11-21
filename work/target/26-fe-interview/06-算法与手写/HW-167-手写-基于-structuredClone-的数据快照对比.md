---
title: [HW-167] 手写表单快照对比——structuredClone 快照 + 增量 diff + dirty 字段列表驱动提交
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：提交优化（只提交变更字段）：进入编辑时 structuredClone 快照 → 提交时浅 diff（顶层字段比对，嵌套字段走 JSON 比较）→ 产出 dirty 列表 → 请求只带变更字段（带宽省 + 冲突检测粒度细——乐观锁按字段版本）。

```javascript
function createSnapshot(values) {
  const snap = structuredClone(values);                   // 深快照（嵌套对象独立副本）
  return {
    diff(current) {
      const dirty = {};
      for (const k of new Set([...Object.keys(snap), ...Object.keys(current)])) {
        const a = snap[k], b = current[k];
        const same = a === b
          || (typeof a === 'object' && typeof b === 'object'
              && a !== null && b !== null && JSON.stringify(a) === JSON.stringify(b));
        if (!same) dirty[k] = b;
      }
      return dirty;                                       // 只含变更字段
    },
    isDirty(current) { return Object.keys(this.diff(current)).length > 0; },
    restore(current) { Object.assign(current, structuredClone(snap)); },   // Esc 还原（HW-127）
  };
}
// 用法：
// const snap = createSnapshot(initial);
// on submit: const dirty = snap.diff(current);
//   Object.keys(dirty).length ? api.patch(id, dirty) : skip();
// dirty 粒度价值：PATCH 语义 + 乐观锁按字段版本（两个用户改不同字段互不冲突）
```

**评分点**：
- structuredClone 深快照 + diff 产出变更字段集（PATCH 语义）。
- 嵌套对象 JSON 比较的取舍（性能：大嵌套对象可限制深度）。
- restore 与 isDirty 的配套（Esc/未变更短路，HW-127 语义）。
- 字段级乐观锁的冲突检测价值（不同字段并行编辑不冲突）。
