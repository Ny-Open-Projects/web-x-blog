---
title: [WCN-710] 笔试：手写属性重命名 codemod（基于 AST 的 JSX 属性改写）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-710：笔试：手写属性重命名 codemod（基于 AST 的 JSX 属性改写）

**答**：
- 需求：给定 JSX 源码字符串、旧属性名、新属性名，返回替换后的源码；要求只改 JSX 标签属性，不碰对象字面量的同名 key、字符串字面量。
- 要点：用简单词法扫描识别 `<Tag ...>` 区间，在标签内做属性名替换；边界：自闭合标签、多行属性、已是新名则跳过。

```javascript
function renameJsxAttr(src, oldName, newName) {
  let out = '', i = 0;
  const isNameChar = (c) => /[A-Za-z0-9_$]/.test(c);
  while (i < src.length) {
    if (src[i] === '<' && /[A-Za-z]/.test(src[i + 1] || '')) {
      // 进入标签，找到 '>' 但跳过属性值里的 '>'
      let j = i + 1, quote = null;
      while (j < src.length) {
        const ch = src[j];
        if (quote) { if (ch === quote) quote = null; }
        else if (ch === '"' || ch === "'") quote = ch;
        else if (ch === '>') break;
        j++;
      }
      let tag = src.slice(i, j + 1);
      tag = tag.replace(new RegExp(`\\b${oldName}(?=\\s*=)`, 'g'), newName);
      out += tag; i = j + 1;
    } else { out += src[i++]; }
  }
  return out;
}
const src = '<Comp size="s" />; const o = { size: 1 };';
console.log(renameJsxAttr(src, 'size', 'scale'));
// => <Comp scale="s" />; const o = { size: 1 };
```

**评分点**：
- 只替换 JSX 标签内的属性名，对象 key/字符串不受影响（边界准确）。
- 扫描时处理引号内的 '>'，正确定位标签结束。
- 用词边界 + 后跟 '=' 断言，避免误替换相似名字。
- 支持自闭合与多行属性，输出完整源码。
