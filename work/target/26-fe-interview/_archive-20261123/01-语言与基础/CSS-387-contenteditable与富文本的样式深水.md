---
title: [CSS-387] contenteditable 与富文本：编辑区样式深水
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 交互]
type: 面试题
---

## CSS-387：contenteditable 与富文本：编辑区样式深水

**答**：
- 编辑区样式主体：caret-color（光标色）、::selection（选中态）、user-modify/read-write-plaintext-only（限制纯文本输入，兼容性注意）、placeholder 用 :empty + content 模拟或 :before
- 白纸化：浏览器对 contenteditable 自带行为（粘贴带样式/列表自动缩进）——CSS 只能关部分（caret/selection），行为控制要 execCommand 废弃后的自研模型（contenteditable=false 冻结块 + 自研 DOM 状态机），成熟方案 Slate/ProseMirror/lexical
- IME 深水：中文输入法 composition 期间不要打断 DOM（校验/格式化推迟到 compositionend）——编辑器样式无关但样式引发的 reflow 会打断 IME，输入法卡顿排查常落在「input 时同步改样式」
- 撤销与样式：浏览器默认撤销栈会被 JS DOM 改动打断（改样式属性不破坏，改结构破坏）——富文本高亮样式尽量用 <mark> 包裹（结构变更走自研撤销）
- 性能：长文档编辑的样式失效面——编辑区局部 containment（contain: layout）+ 虚拟分页（长文分段渲染）

```css
.editor {
  caret-color: var(--primary);
  contain: layout;
}
.editor:empty::before { content: attr(data-placeholder); color: #999; }
.editor::selection, .editor *::selection { background: color-mix(in oklab, var(--primary) 30%, transparent); }
.editor:focus { outline: none; }
```
