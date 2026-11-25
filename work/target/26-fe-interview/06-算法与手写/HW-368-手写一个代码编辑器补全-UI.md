---
title: [HW-368] 手写一个代码编辑器补全 UI：触发、过滤与排序
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-368：手写一个代码编辑器补全 UI：触发、过滤与排序

**答**：
- 需求：实现 CompletionUI：触发（输入字母/点号后 2 字符起提示）；候选项 {label, kind, score}；过滤（前缀匹配优先，其次子串，fuzzy 加分）；排序（得分 + kind 权重 + 最近使用加权）；键盘导航与选中插入（替换当前词）。
- 边界：fuzzy 匹配（子序列连续加分）；中文输入法组合期不触发；候选去重（同 label 不同 kind 保留高分）；弹窗定位跟随光标。
- 评分点：fuzzy 打分；MRU 加权；组合期抑制。

```javascript
class CompletionUI {
  constructor(editor, providers) { this.ed = editor; this.providers = providers; this.mru = new Map(); }
  async trigger(char) {
    if (this.ed.composing) return;                           // IME 组合期抑制
    const word = this.ed.wordBeforeCursor();
    if (!word || word.length < (char === '.' ? 0 : 2)) return this.hide();
    const items = (await Promise.all(this.providers.map(p => p(word)))).flat();
    const seen = new Set();
    const cands = items.filter(i => {
      const k = i.label + i.kind;
      if (seen.has(k)) return false;                         // 去重
      seen.add(k);
      return fuzzyMatch(word, i.label);
    }).map(i => ({ ...i, score: this.score(word, i) }))
      .sort((a, b) => b.score - a.score).slice(0, 20);
    this.show(cands);
  }
  score(word, item) {
    let s = 0;
    if (item.label.startsWith(word)) s += 50;                // 前缀最优先
    else if (item.label.toLowerCase().includes(word.toLowerCase())) s += 20;
    else s += fuzzyScore(word, item.label);                  // 子序列得分
    s += KIND_WEIGHT[item.kind] ?? 0;
    s += (this.mru.get(item.label) ?? 0) * 5;                // 最近使用加权
    return s;
  }
  accept(item) {                                             // 选中插入：替换当前词
    this.mru.set(item.label, (this.mru.get(item.label) ?? 0) + 1);
    this.ed.replaceCurrentWord(item.label);
    this.hide();
  }
  onKey(e) {                                                 // 键盘导航
    if (!this.open) return 'none';
    if (e.key === 'ArrowDown') { this.select(this.idx + 1); return 'handled'; }
    if (e.key === 'ArrowUp') { this.select(this.idx - 1); return 'handled'; }
    if (e.key === 'Enter' || e.key === 'Tab') { this.accept(this.cands[this.idx]); return 'handled'; }
    if (e.key === 'Escape') { this.hide(); return 'handled'; }
    return 'none';
  }
}
const KIND_WEIGHT = { field: 10, function: 8, variable: 5, snippet: 3 };
function fuzzyMatch(pattern, text) { let i = 0;
  for (const c of text.toLowerCase()) if (c === pattern[i]) i++;
  return i === pattern.length; }
function fuzzyScore(p, t) { let s = 0, run = 0;
  let i = 0;
  for (const c of t.toLowerCase()) {
    if (c === p[i]) { run++; s += 2 + run; i++; }           // 连续命中加分
    else run = 0;
    if (i >= p.length) break;
  }
  return s; }
```
