---
title: [DP-332] 笔试题：手写 Table 跨页选中保持？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-332：笔试题：手写 Table 跨页选中保持？
**题目**：实现分页表格选中：1) 跨页选中集合保持（翻页不丢）；2) 全选语义（当页全选 vs 跨页全量，半选态）；3) 反选/清空；4) 禁用行不参与。
**评分点**：
- 选中集合用 Map/Set 按 id 维护。
- 半选态推导正确（当页部分选中）。
- "全量选择"模式（选所有数据而非当页）的区分。
- 禁用行过滤。
```tsx
function useSelection(rows, { getRowId, disabled }) {
  const [selected, setSelected] = useState(new Map());     // id → row（跨页保持）
  const pageIds = rows.filter(r => !disabled?.(r)).map(getRowId);
  const pageSelected = pageIds.filter(id => selected.has(id));
  const allPage = pageSelected.length === pageIds.length && pageIds.length > 0;
  const somePage = pageSelected.length > 0 && !allPage;    // 2) 半选
  const togglePage = (checked) => setSelected(prev => {
    const next = new Map(prev);
    pageIds.forEach(id => checked ? next.set(id, rows.find(r => getRowId(r) === id)) : next.delete(id));
    return next;
  });
  const toggleAll = () => {                                // 全量模式：标记 allFlag
    setSelected(prev => new Map(rows.filter(r => !disabled?.(r)).map(r => [getRowId(r), r])));
  };
  const clear = () => setSelected(new Map());
  return { selected: [...selected.values()], allPage, somePage, togglePage, toggleAll, clear,
    isSelected: (r) => selected.has(getRowId(r)) };
}
```
