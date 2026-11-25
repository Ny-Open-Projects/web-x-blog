---
title: [WCN-977] 手写无障碍违规扫描器：img 缺 alt / 按钮无文本 / input 无 label / 重复 id
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-977：手写无障碍违规扫描器：img 缺 alt / 按钮无文本 / input 无 label / 重复 id

**题目**：实现 `scanA11y(html)`，用正则解析（不依赖 DOM）。要求检测四类违规并返回 `{ violations:[{type, snippet}], passed }`：① img 标签缺 alt 属性；② button 标签内无文本且无 aria-label（简单处理：匹配 `<button...>文本</button>` 是否有非空文本）；③ input 标签无 aria-label 且无 aria-labelledby（简化：不要求真实 label 关联）；④ 同一 html 中 id 重复（记录重复 id 值）。要求：snippet 取违规标签的前 60 字符；无违规 violations 为空、passed=true；输入非字符串按空串处理。请自足实现并给出可运行示例。

**答**：

```javascript
function scanA11y(html) {
  if (typeof html !== 'string') html = '';
  const violations = [];
  const push = (type, m) => violations.push({ type, snippet: m[0].slice(0, 60) });
  let m;
  // img 缺 alt
  const imgRe = /<img\b[^>]*>/gi;
  while ((m = imgRe.exec(html))) if (!/\balt\s*=/.test(m[0])) push('img-missing-alt', m);
  // button 无文本无 aria-label
  const btnRe = /<button\b([^>]*)>([\s\S]*?)<\/button>/gi;
  while ((m = btnRe.exec(html)))
    if (!/aria-label\s*=/.test(m[1]) && !m[2].replace(/<[^>]*>/g, '').trim()) push('button-no-text', m);
  // input 无 aria-label / labelledby
  const inputRe = /<input\b[^>]*>/gi;
  while ((m = inputRe.exec(html)))
    if (!/aria-label\s*=|aria-labelledby\s*=/.test(m[0])) push('input-no-label', m);
  // 重复 id
  const ids = {}, idRe = /\bid\s*=\s*["']([^"']+)["']/gi;
  while ((m = idRe.exec(html))) {
    if (ids[m[1]]) violations.push({ type: 'duplicate-id', snippet: `id="${m[1]}"` });
    ids[m[1]] = true;
  }
  return { violations, passed: violations.length === 0 };
}
console.log(scanA11y('<img src="a"><button></button><input><div id="x"></div><div id="x"></div>'));
```

**评分点**：
- img 缺 alt、button 无文本、input 无 label 三类检查正确。
- 重复 id 检测正确。
- snippet 截取前 60 字符，结构 { type, snippet } 正确。
- 非字符串输入健壮、无违规 passed=true。
- 示例可运行、违规类型输出正确。
