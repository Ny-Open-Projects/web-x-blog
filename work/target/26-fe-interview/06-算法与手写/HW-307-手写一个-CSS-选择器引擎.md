---
title: [HW-307] 手写一个 CSS 选择器引擎：解析与元素匹配
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-307：手写一个 CSS 选择器引擎：解析与元素匹配

**答**：
- 需求：实现 SelectorEngine：支持标签/.class/#id/[attr=val]/后代空格/子代 >；parse 选择器为复合选择器序列；matches(el, selector) 判定（从右向左匹配：先匹配最右复合，再沿祖先验证其余）；queryAll(root, selector) 全量查找。
- 边界：从右向左性能（先筛小集合再上溯）；多 class 匹配（classList 包含全部）；[attr~=v] 简化支持 = 与存在两种。
- 评分点：从右向左；复合选择器解析；祖先验证。

```javascript
function parseSelector(sel) {
  return sel.split('\s*(>)\s*|\s+').filter(Boolean).reduce((out, tok, i, arr) => {
    if (tok === '>') out.comb[out.comb.length - 1] = 'child';
    else out.parts.push({ comb: out.comb.at(-1) ?? 'descendant', compound: parseCompound(tok) });
    return out;
  }, { parts: [], comb: [] }).parts;
}
function parseCompound(tok) {
  const re = /([.#]?)([\w-]+)|(\[[\w-]+(?:=.+?)?\])/g;
  const out = [];
  let m;
  while ((m = re.exec(tok))) {
    if (m[1] === '.') out.push({ t: 'class', v: m[2] });
    else if (m[1] === '#') out.push({ t: 'id', v: m[2] });
    else if (m[3]) { const [k, v] = m[3].slice(1, -1).split('='); out.push({ t: 'attr', k, v: v?.replace(/['"]/g, '') }); }
    else out.push({ t: 'tag', v: m[2].toLowerCase() });
  }
  return out;
}
function matchCompound(el, compound) {
  return compound.every(c => {
    if (c.t === 'tag') return el.tagName.toLowerCase() === c.v;
    if (c.t === 'class') return el.classList.contains(c.v);
    if (c.t === 'id') return el.id === c.v;
    if (c.t === 'attr') return c.v == null ? el.hasAttribute(c.k) : el.getAttribute(c.k) === c.v;
  });
}
function matches(el, selector) {
  const parts = parseSelector(selector);
  if (!matchCompound(el, parts.at(-1).compound)) return false;   // 从右向左：先匹配最右
  let cur = el.parentElement;
  for (let i = parts.length - 2; i >= 0; i--) {
    const p = parts[i + 1];
    if (p.comb === 'child') {
      if (!cur || !matchCompound(cur, parts[i].compound)) return false;
      cur = cur.parentElement;
    } else {                                                 // descendant：向上找任意祖先
      let found = false;
      for (let a = cur; a; a = a.parentElement)
        if (matchCompound(a, parts[i].compound)) { found = true; cur = a.parentElement; break; }
      if (!found) return false;
    }
  }
  return true;
}
```
