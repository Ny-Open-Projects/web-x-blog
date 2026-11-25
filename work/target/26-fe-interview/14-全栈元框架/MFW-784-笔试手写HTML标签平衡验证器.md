---
title: [MFW-784] 笔试：手写 HTML 标签平衡验证
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-784：笔试：手写 HTML 标签平衡

**答**：实现 `validateHtmlBalance(html)`。规则：1) 标签提取（`<tag>`/`</tag>`/`<tag/>`）；2) 自闭合豁免（img/br/hr/input/meta/link + `/>` 结尾）；3) 栈匹配（open pop close——不匹配 = UNMATCHED）；4) **非法嵌套检测**：p 内 block 元素（div/h1-h6/ul/table）→ INVALID_NEST；5) 返回 `{ balanced: boolean, unclosed: string[], invalidNests: string[], errors: string[] }`。边界：空 html（balanced）；纯文本（无标签——balanced）；自闭合标签（不入栈）；注释（`<!-- -->` 跳过）；未闭合标签（unclosed 非空）。

```javascript
function validateHtmlBalance(html = '') {
  const SELF_CLOSING = new Set(['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'track']);
  const BLOCK_IN_P = new Set(['div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'table', 'section']);
  const stack = []; const errors = []; const invalidNests = [];
  let inComment = false;
  // 清除注释
  html = html.replace(/<!--[\s\S]*?-->/g, '');
  const tags = html.match(/<\/?(\w+)[^>]*?(\/)?>/g) ?? [];
  for (const tag of tags) {
    const name = tag.match(/<\/?(\w+)/)?.[1]?.toLowerCase();
    if (!name) continue;
    if (SELF_CLOSING.has(name) || tag.endsWith('/>')) continue;
    if (tag.startsWith('</')) {
      const top = stack.pop();
      if (top !== name)
        errors.push(`UNMATCHED: </${name}> 但期望 </${top ?? 'none'}>`);
    } else {
      // p 内 block 检测
      const parent = stack.at(-1);
      if (parent === 'p' && BLOCK_IN_P.has(name))
        invalidNests.push(`${name}-in-p`);
      stack.push(name);
    }
  }
  return {
    balanced: stack.length === 0 && errors.length === 0,
    unclosed: stack,
    invalidNests,
    errors,
  };
}

// 自测
// 平衡
console.log(validateHtmlBalance('<div><p>text</p></div>').balanced === true);
console.log(validateHtmlBalance('<div><img src="x"><br></div>').balanced === true);   // 自闭合
// 不平衡
let r = validateHtmlBalance('<div><span>text');
console.log(r.balanced === false && r.unclosed.join(',') === 'div,span');
// 不匹配的关闭
r = validateHtmlBalance('<div></span></div>');
console.log(r.errors[0].includes('UNMATCHED'));
// p 内 block → invalid nest
r = validateHtmlBalance('<p><div>text</div></p>');
console.log(r.invalidNests.includes('div-in-p'));
console.log(r.balanced === false);                       // invalid nest 也算 fail
// p 内 inline → 合法
r = validateHtmlBalance('<p><span>text</span></p>');
console.log(r.balanced === true && r.invalidNests.length === 0);
// 注释跳过
r = validateHtmlBalance('<!-- <div> -->');
console.log(r.balanced === true);                        // 注释内容忽略
// 自闭合标签
r = validateHtmlBalance('<img src="x"/><br/>');
console.log(r.balanced === true);                        // 自闭合不入栈
// 空
console.log(validateHtmlBalance('').balanced === true);
console.log(validateHtmlBalance('纯文本').balanced === true);
```

**评分点**：
- 栈匹配正确（open/pop close 不匹配 = UNMATCHED）；自闭合豁免（img/br/hr + /> 结尾）
- p 内 block 的非法嵌套检测（HTML5 规范——浏览器容错修复导致水合 mismatch 的源头）；注释清除
- 边界（纯文本/空/自闭合/注释）；balanced 的语义 = 栈空 + 无 error + 无 invalid
- 能说清「HTML 合法性 = 水合的前提：非法嵌套被浏览器容错修复后 DOM 结构变化 → React 水合 mismatch」属于加分
