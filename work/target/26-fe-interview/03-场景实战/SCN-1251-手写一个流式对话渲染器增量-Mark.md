---
title: [SCN-1251] 手写一个流式对话渲染器（增量 Markdown + 中断）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1251：手写一个流式对话渲染器（增量 Markdown + 中断）

**答**：
- 需求：implement StreamRenderer(container)。push(delta) 增量渲染（Markdown 分块），stop() 中断保留部分内容，finish() 返回全文；代码块未闭合时显示"生成中"。
- 边界：delta 可能为空串；超大回复（> 100KB）分块渲染防卡；reduced-motion 直出。
- 评分点：增量分块；未完标记；中断保留；reduced 直出

```javascript
class StreamRenderer {
  constructor(container, { reduced = false } = {}) {
    this.el = container; this.md = new IncrementalMD();  // 1204
    this.reduced = reduced; this.stopped = false;
  }
  push(delta) {
    if (this.stopped || !delta) return;
    const { done, partial } = this.md.append(delta);
    this.render(done, partial);
  }
  render(done, partial) {
    this.el.innerHTML = '';
    done.forEach(b => this.el.appendChild(b));
    if (partial) {
      const el = document.createElement('div');
      el.className = 'streaming';
      el.textContent = partial.textContent ?? '';
      this.el.appendChild(el);                         // 未完块标记
    }
  }
  stop() { this.stopped = true; return this.md.finish(); }
  finish() { return this.md.finish(); }
}
```
