---
title: [WCN-706] 笔试：手写 tag 名作用域化转换器（前缀重写工具）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-706：笔试：手写 tag 名作用域化转换器（前缀重写工具）

**答**：
- 需求：输入一段含自定义元素标签的 HTML 字符串与前缀，把开始/结束标签、以及 `is=` 属性里的自定义元素名都加上前缀；保留原生 HTML 标签（含连字符判断）。
- 要点：用正则匹配标签名，含连字符的视为自定义元素；跳过 script/style 内容；边界：空串、无标签、已带前缀。

```javascript
function scopeTags(html, prefix) {
  if (!html) return '';
  // 先用占位保护 script/style 内容，避免误改
  const protectedBlocks = [];
  let out = html.replace(/<(script|style)\b[\s\S]*?<\/\1>/gi, (m) => {
    protectedBlocks.push(m);
    return `\u0000PB${protectedBlocks.length - 1}\u0000`;
  });
  const isCustom = (name) => name.includes('-') && /^[a-z]/.test(name);
  out = out.replace(/<(\/?)([a-z][a-z0-9-]*)(\b)/gi, (m, slash, name, tail) => {
    return `<${slash}${isCustom(name) ? prefix + name : name}${tail}`;
  });
  out = out.replace(/\b(is=["'])([a-z][a-z0-9-]*)(["'])/gi, (m, a, name, c) =>
    isCustom(name) ? a + prefix + name + c : m);
  out = out.replace(/\u0000PB(\d+)\u0000/g, (_, i) => protectedBlocks[Number(i)]);
  return out;
}
console.log(scopeTags('<ds-button is="ds-base">x</ds-button><div>y</div>', 'app1-'));
```

**评分点**：
- 只重写含连字符的自定义元素，原生标签保持不变。
- 同时处理开始标签、结束标签与 is 属性三种位置。
- 用占位符保护 script/style 内容不被误改。
- 对空串与边界情况有防御。
