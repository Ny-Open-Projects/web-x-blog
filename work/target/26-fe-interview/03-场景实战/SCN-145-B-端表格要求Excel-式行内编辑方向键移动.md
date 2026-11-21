---
title: [SCN-145] B 端表格要求"Excel 式"行内编辑：方向键移动、Enter 确认换行进下一格、Esc 还原，怎么实现？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-145：B 端表格要求"Excel 式"行内编辑：方向键移动、Enter 确认换行进下一格、Esc 还原，怎么实现？
**答**：
- 维护一个焦点坐标 `[rowIndex, colIndex]` 与编辑态，全局 keydown 按 Excel 语义分发：方向键移动、Enter 提交并下移、Tab 横移、Esc 还原、双击或直接输入进入编辑。
- 校验失败阻止移动并标红单元格，保证"错误数据不离开当前格"。
- 大表配合虚拟滚动：滚动后按记录的坐标重新聚焦对应单元格（数据坐标而非 DOM 索引）。
- 编辑控件按列类型分发（文本/数字/日期/选择器），Tab 键默认行为要 preventDefault。

```jsx
// 行内编辑：焦点坐标 + Excel 语义键盘分发
export function EditableGrid({ rows, columns, onCellCommit }) {
  const [pos, setPos] = useState({ r: 0, c: 0 });
  const [editing, setEditing] = useState(false);
  const gridRef = useRef();

  const move = (dr, dc) => setPos(p => ({
    r: Math.min(rows.length - 1, Math.max(0, p.r + dr)),
    c: Math.min(columns.length - 1, Math.max(0, p.c + dc)),
  }));

  const onKeyDown = e => {
    if (editing) {
      if (e.key === 'Enter') { commit(); move(1, 0); }        // Enter 提交并下移
      else if (e.key === 'Escape') setEditing(false);         // Esc 还原
      else if (e.key === 'Tab') { e.preventDefault(); commit(); move(0, 1); }
      return;                                          // 编辑态其余按键交给输入框
    }
    const nav = { ArrowUp: [-1, 0], ArrowDown: [1, 0], ArrowLeft: [0, -1], ArrowRight: [0, 1] };
    if (nav[e.key]) { e.preventDefault(); move(...nav[e.key]); }
    else if (e.key === 'Enter') setEditing(true);
    else if (e.key.length === 1) setEditing(true);     // 直接输入即进入编辑
  };

  const commit = () => {
    const cell = getCellValue(rows[pos.r], columns[pos.c]);
    const err = columns[pos.c].validate?.(cell);
    if (err) return markCellError(gridRef.current, pos, err); // 校验失败不移动
    setEditing(false);
  };

  // 虚拟滚动后按数据坐标恢复焦点
  useEffect(() => {
    if (editing) focusCell(gridRef.current, pos);      // 定位 [data-r][data-c]
  }, [pos, editing]);

  return <div ref={gridRef} tabIndex={0} onKeyDown={onKeyDown}>{/* 渲染 rows/columns */}</div>;
}
```
