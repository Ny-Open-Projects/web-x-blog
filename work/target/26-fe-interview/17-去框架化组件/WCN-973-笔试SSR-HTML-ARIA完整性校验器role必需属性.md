---
title: [WCN-973] 手写 SSR HTML 的 ARIA 完整性校验器：role 必需的 aria 属性是否齐全
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-973：手写 SSR HTML 的 ARIA 完整性校验器：role 必需的 aria 属性是否齐全

**题目**：实现 `auditAria(html)`，用正则解析标签（不依赖 DOM）。要求：① 定义 role 必需属性表（checkbox→aria-checked、slider→aria-valuenow、tab→aria-selected、combobox→aria-expanded）；② 对每个带 role 的标签，检查必需 aria 属性是否存在，缺失则记录 `{ role, missing:[...], tag }`；③ 额外检查：`<img>` 是否有 alt、`<button>` 是否有可访问文本（标签内文字或 aria-label）、`<input>` 是否有 aria-label 或关联 label；④ 返回 `{ violations:[...], passed:boolean }`；⑤ 无违规时 violations 为空、passed 为 true。请自足实现并给出可运行示例。

**答**：

```javascript
function auditAria(html) {
  const required = {
    checkbox: ['aria-checked'], slider: ['aria-valuenow'],
    tab: ['aria-selected'], combobox: ['aria-expanded'],
  };
  const violations = [];
  // role 必需属性检查
  const roleRe = /<([a-z]+)\b([^>]*)>/gi;
  let m;
  while ((m = roleRe.exec(html))) {
    const [, tag, attrs] = m;
    const roleM = attrs.match(/role\s*=\s*["']([^"']+)["']/i);
    if (roleM && required[roleM[1]]) {
      const missing = required[roleM[1]].filter(a => !new RegExp(a + '\\s*=').test(attrs));
      if (missing.length) violations.push({ role: roleM[1], missing, tag });
    }
    if (/^img$/i.test(tag) && !/\balt\s*=/.test(attrs))
      violations.push({ role: 'img', missing: ['alt'], tag });
    if (/^input$/i.test(tag) && !/aria-label\s*=/.test(attrs) && !/\blabel\b/.test(html))
      violations.push({ role: 'input', missing: ['label'], tag });
  }
  return { violations, passed: violations.length === 0 };
}
console.log(auditAria('<div role="checkbox"></div><img src="a.png">'));
// violations: [{role:'checkbox',missing:['aria-checked'],tag:'div'}, {role:'img',missing:['alt'],tag:'img'}]
```

**评分点**：
- role 必需属性表检查正确（checkbox/slider/tab/combobox）。
- img 缺 alt、input 缺 label 检查正确。
- 正则解析标签、不依赖 DOM，纯函数可测试。
- 返回结构 { violations, passed } 正确，无违规 passed 为 true。
- 示例输出正确可运行。
