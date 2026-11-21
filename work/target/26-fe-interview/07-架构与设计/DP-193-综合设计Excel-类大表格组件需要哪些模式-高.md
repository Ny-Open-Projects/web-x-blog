---
title: [DP-193] 综合设计：Excel 类大表格组件需要哪些模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-193：综合设计：Excel 类大表格组件需要哪些模式？（高频）
**答**：
- 组合：享元（可视区单元格 DOM 池复用，百万行只渲染可视 40 行 × 20 列）、组合模式（workbook → sheet → row → cell 树）、策略（列类型渲染器：text/number/date/select 各自编辑与格式化策略）、命令（单元格编辑可撤销，宏命令支持批量粘贴）、备忘录（编辑前快照 + 撤销栈）、观察者（选区/滚动/数据变更广播）。
- 性能三支柱：虚拟滚动（享元池）+ 脏区域重绘（备忘录对比）+ requestAnimationFrame 合帧。

```javascript
class DataGrid {
  #pool = []; #undoStack = []; #listeners = new Set(); #types = new Map();   // 享元池 / 命令栈 / 观察者 / 渲染策略
  registerCellType(name, strategy) { this.#types.set(name, strategy); }      // 策略：列类型注册
  on(fn) { this.#listeners.add(fn); return () => this.#listeners.delete(fn); }
  render(viewport) {                                           // 虚拟滚动：只渲染可视区
    const { rowStart, rowEnd, colStart, colEnd } = this.#calcRange(viewport);
    const frag = document.createDocumentFragment();
    for (let r = rowStart; r <= rowEnd; r++)
      for (let c = colStart; c <= colEnd; c++) {
        const cell = this.#pool.pop() ?? document.createElement('div');       // 享元：取池或建
        const strategy = this.#types.get(this.schema[c]?.type ?? 'text');
        cell.textContent = strategy.format(this.data[r][c]);   // 策略：格式化
        cell.className = strategy.cls;
        cell.dataset.rc = `${r}:${c}`;
        frag.appendChild(cell);
      }
    viewport.replaceChildren(frag);                            // 整批替换，剩余回池
    this.#pool.push(...[...viewport.children].slice(rowEnd - rowStart + 1).slice(colEnd - colStart + 1));
  }
  editCell(r, c, value) {                                      // 命令 + 备忘录
    const prev = this.data[r][c];
    const cmd = { do: () => { this.data[r][c] = value; this.#emit(r, c); },
                  undo: () => { this.data[r][c] = prev; this.#emit(r, c); } };
    cmd.do();
    this.#undoStack.push(cmd);
  }
  pasteBlock(startRC, matrix) {                                // 宏命令：批量粘贴一次撤销
    const cmds = matrix.flatMap((row, dr) => row.map((v, dc) => ({ r: startRC.r + dr, c: startRC.c + dc, v })));
    this.#undoStack.push({ do: () => cmds.forEach((x) => (this.data[x.r][x.c] = x.v)),
                           undo: () => cmds.forEach((x) => (this.data[x.r][x.c] = x.prev)) });
    this.#undoStack.at(-1).do();
  }
  undo() { this.#undoStack.pop()?.undo(); }
  #emit(r, c) { this.#listeners.forEach((f) => f({ r, c })); }
  #calcRange = (v) => ({ rowStart: Math.floor(v.scrollTop / ROW_H), rowEnd: Math.floor((v.scrollTop + v.height) / ROW_H), colStart: Math.floor(v.scrollLeft / COL_W), colEnd: Math.floor((v.scrollLeft + v.width) / COL_W) });
}
grid.registerCellType('date', { format: (v) => dayjs(v).format('YYYY-MM-DD'), cls: 'cell-date' });   // 策略注册
grid.registerCellType('number', { format: (v) => Number(v).toLocaleString(), cls: 'cell-num' });
```
