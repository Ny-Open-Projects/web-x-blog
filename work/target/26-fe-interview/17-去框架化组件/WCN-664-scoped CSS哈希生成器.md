---
title: [WCN-664] 笔试：实现 scoped CSS 哈希生成器（基于文件内容生成稳定 scopeId + 选择器改写 + 深度选择器）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-664：笔试：实现 scoped CSS 哈希生成器（基于文件内容生成稳定 scopeId + 选择器改写 + 深度选择器）

**答**：
- 需求：实现 scopeStyle(css, content)：① 用简单哈希（如 djb2）对 content 生成 scopeId ② 改写普通选择器追加 [data-s-id] ③ 识别 :deep(...) 语法，保留内部选择器不加属性 ④ 幂等（已有属性不重复加）。
- 思路：djb2 哈希；按选择器逗号分割逐个处理；:deep(X) → X 去掉 deep 包裹且只给 X 前半段加属性（实际 deep 让后半段不受限）。
- 边界：@media/@keyframes 内的选择器不改写；属性选择器已含 data-s-id 则跳过。

```javascript
function hash(content) {
  let h = 5381;
  for (let i = 0; i < content.length; i++) h = ((h << 5) + h + content.charCodeAt(i)) >>> 0;
  return h.toString(36).slice(0, 8);
}
function rewrite(sel, id) {
  if (sel.includes('data-s-')) return sel; // 幂等
  if (sel.includes(':deep(')) {
    const [before, rest] = sel.split(':deep(');
    const inner = rest.replace(/\)$/, '');
    return `${before}[data-s-${id}] ${inner}`; // deep 内不加属性
  }
  return `${sel}[data-s-${id}]`;
}
export function scopeStyle(css, content) {
  const id = hash(content);
  return css.replace(/([^{}]+)\{/g, (m, sels) => {
    if (/^@/.test(sels.trim())) return m; // 忽略 at-rule
    return sels.split(',').map(s => rewrite(s.trim(), id)).join(',') + '{';
  });
}
console.log(scopeStyle('.btn:hover{color:red}.a :deep(.b){x:y}', 'file-content'));
```

**评分点**：
- djb2 哈希对相同内容生成稳定 id（可重复构建）。
- 普通选择器正确追加属性选择器，逗号分隔逐个处理。
- :deep() 语法识别正确（内部选择器不被限制）。
- 幂等 + at-rule（@media/@keyframes）不改写。
