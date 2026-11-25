---
title: [SCN-1204] 流式 Markdown 增量渲染的技术难点
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1204：流式 Markdown 增量渲染的技术难点

**答**：
- 难点：流式 token 切断 Markdown 语法（代码块未闭合/表格半行/公式未完成）。
- 方案：增量解析器（容忍未闭合语法，闭合后重渲染该块）或分段缓冲（按块渲染）。
- 性能：每次 delta 只重渲染受影响块（非全文重渲）。

```javascript
// 增量 Markdown 渲染
class IncrementalMD {
  constructor() { this.blocks = []; this.current = ''; }
  append(delta) {
    this.current += delta;
    const parts = this.current.split('\n\n');       // 空行分块
    this.current = parts.pop();                        // 最后块可能未完
    parts.forEach(p => this.blocks.push(renderMD(p))); // 完整块渲染
    return { done: this.blocks, partial: renderMD(this.current) };
  }
  finish() {
    if (this.current) this.blocks.push(renderMD(this.current));
    return this.blocks;
  }
}
function renderMD(s) { return s; }
```
