---
title: [V3-110] 十万行大表格如何优化（shallowRef + 手动触发）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-110：十万行大表格如何优化（shallowRef + 手动触发）？
**答**：
- reactive 会深度代理整个数组，十万行数据的每个字段读写都走 Proxy，初始化和更新都慢。
- 用 shallowRef 只代理引用：内部字段改动不触发更新，整表替换或 triggerRef 才触发，把响应式成本从 O(n) 降到 O(1)。
- 单元格修改走不可变更新（新对象替换旧行）+ triggerRef 手动通知一次，避免逐字段多次触发渲染。
- 再配合虚拟滚动只渲染可视行，两个优化叠加才是完整方案。

```typescript
// composables/useBigTable.ts —— shallowRef + 手动触发
import { shallowRef, triggerRef } from "vue";

interface Row {
  id: number;
  name: string;
  score: number;
}

export function useBigTable(initialRows: Row[]) {
  // 只追踪引用，不对十万行做深度代理
  const rows = shallowRef<Row[]>(initialRows);

  // 单元格更新：不可变替换 + 手动触发一次
  function updateRow(id: number, patch: Partial<Row>) {
    const index = rows.value.findIndex((r) => r.id === id);
    if (index === -1) return;
    rows.value[index] = { ...rows.value[index], ...patch };
    triggerRef(rows); // 手动通知，一次渲染完成所有变更
  }

  // 排序：直接替换引用，天然触发
  function sortBy(key: keyof Row) {
    rows.value = [...rows.value].sort((a, b) => (a[key] > b[key] ? 1 : -1));
  }

  function addRow(row: Row) {
    rows.value = [...rows.value, row]; // 扩展运算符替代 push，避免手动 trigger
  }

  return { rows, updateRow, sortBy, addRow };
}
```
