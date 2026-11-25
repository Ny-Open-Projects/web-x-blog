---
title: [HW-220] 手写一个 Markdown 快捷输入解析器：行首语法即时转换
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-220：手写一个 Markdown 快捷输入解析器：行首语法即时转换

**答**：
- 需求：实现 mdAutoFormat：监听输入，当 block 文本匹配行首语法（# → h1、## → h2、- / * → 列表、> → 引用、``` → 代码块）且触发键为 Space/Enter 时，把该 block 类型转换并去掉前缀，返回转换动作（或 null）。
- 边界：前缀后必须紧跟空格或文本（# 单独不算）；代码块开关状态机（``` 开、再次 ``` 关）；在 block 中间输入前缀不转换。
- 评分点：状态机（代码块开关）；仅行首判定。

```javascript
const FENCE = '\u0060'.repeat(3);   // 三反引号围栏（码点构造，避免源码内出现字面围栏）
const MD_RULES = [
  { re: /^###\s/, type: 'h3' }, { re: /^##\s/, type: 'h2' },
  { re: /^#\s/, type: 'h1' },
  { re: /^[-*]\s/, type: 'li' },
  { re: /^>\s/, type: 'quote' },
];
function mdAutoFormat(block, key, codeState) {
  if (key === 'Enter' && new RegExp('^' + FENCE + '\\s*$').test(block.text))
    return { action: codeState.open ? 'close-code' : 'open-code', consume: true };
  if (key !== ' ') return null;
  for (const r of MD_RULES) {
    if (r.re.test(block.text)) {                               // 行首语法
      block.type = r.type;
      block.text = block.text.replace(r.re, '');
      block.marks = block.marks.map(m => ({ ...m, start: Math.max(0, m.start - r.re.source.length - 1) }));
      return { action: 'transform', type: r.type };
    }
  }
  return null;
}
```
