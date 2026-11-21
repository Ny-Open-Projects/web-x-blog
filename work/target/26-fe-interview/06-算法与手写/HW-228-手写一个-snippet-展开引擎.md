---
title: [HW-228] 手写一个 snippet 展开引擎：占位符与 tab stop 跳转
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-228：手写一个 snippet 展开引擎：占位符与 tab stop 跳转

**答**：
- 需求：实现 SnippetEngine：expand(template) 解析模板（$1/$2 占位符、${1:default} 默认值、$0 终点），生成插入文本与 tabstop 列表；tab() 按序跳到下一个占位符并选中其内容；全部跳过后 tab 到 $0 退出。
- 边界：同名占位符（$1 出现两次）联动编辑（一处改全部同步）；嵌套占位符按平铺处理；模板中转义 \$ 输出字面 $。
- 评分点：占位符解析；联动占位符；$0 终点。

```javascript
function parseSnippet(tpl) {
  let text = '', stops = [], i = 0, n = 1;
  while (i < tpl.length) {
    if (tpl[i] === '\\' && tpl[i + 1] === '$') { text += '$'; i += 2; continue; }   // 转义
    if (tpl[i] === '$' && /\d/.test(tpl[i + 1] ?? '')) {
      let j = i + 1, num = '';
      while (/\d/.test(tpl[j] ?? '')) num += tpl[j++];
      const k = +num;
      stops[k] ??= { id: k, ranges: [] };
      stops[k].ranges.push({ start: [...text].length, end: [...text].length });   // 同号联动
      i = j; continue;
    }
    if (tpl[i] === '$' && tpl[i + 1] === '0') { stops[0] = { id: 0, ranges: [{ start: [...text].length, end: [...text].length }] }; i += 2; continue; }
    text += tpl[i++];
  }
  return { text, stops: stops.filter(Boolean) };
}
class SnippetEngine {
  expand(tpl) {
    const { text, stops } = parseSnippet(tpl);
    editor.insert(text);
    this.stops = stops; this.idx = 1;
    return this.stops[1] ? this.select(this.stops[1]) : this.select(this.stops[0] ?? null);
  }
  select(stop) { stop && editor.selectRange(stop.ranges[0]); }
  tab() {                                                      // 下一占位符
    const next = this.stops[++this.idx];
    if (!next) { this.exit(); return 'done'; }
    this.select(next); return 'move';
  }
  exit() { editor.clearStops(); }
}
```
