---
title: [RBL-931] 笔试：手写 HTML 内嵌数据安全序列化器（闭合注入 + 行终止符）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-931：笔试：手写 HTML 内嵌数据安全序列化器（注入防护）

**答**：实现 `serializeForHtml(data)`。规则：1) JSON.stringify 后转义：`<` → `\u003c`、`>` → `\u003e`、`&` → `\u0026`（防 HTML 实体上下文）；2) U+2028/U+2029（JS 行终止符——JSON 合法但 JS 字符串非法）→ `\u2028`/`\u2029` 转义；3) `<!--` 序列转义（HTML 注释打开会让 script 内容进入注释态——`<\u0021--`）；4) 返回可直接嵌入 `<script>` 的字符串；5) 嵌套对象/数组/字符串全部生效（stringify 后统一替换即可）。提供 `inject(data)` 返回完整 script 标签。边界：data 含所有恶意 payload 组合；null/undefined。

```javascript
function serializeForHtml(data) {
  return JSON.stringify(data ?? null)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026')
    .replace(/\u2028/g, '\\u2028')
    .replace(/\u2029/g, '\\u2029');
}
const inject = (data) =>
  `<script>window.__DATA__ = ${serializeForHtml(data)};</script>`;

// 自测
const evil = {
  close: '</script><script>alert(1)</script>',
  comment: '<!-- -->',
  lineSep: 'a\u2028b\u2029c',
  entity: '<b>&</b>',
};
let s = serializeForHtml(evil);
console.log(!s.includes('</') && !s.includes('<b>'));    // 所有 < 已转义
console.log(s.includes('\\u003c/script\\u003e'));
console.log(s.includes('--\\u003e') || !s.includes('-->'));
console.log(!s.includes('\u2028') && s.includes('\\u2028'));
console.log(s.includes('\\u0026'));

// 注入后解析回读（roundtrip）
const html = inject({ ok: true, name: '张三<b>' });
const m = /window\.__DATA__ = ([\s\S]+?);<\/script>/.exec(html);
const back = JSON.parse(m[1].replace(/\\u003c/g, '<').replace(/\\u003e/g, '>')
  .replace(/\\u0026/g, '&').replace(/\\u2028/g, '\u2028').replace(/\\u2029/g, '\u2029'));
console.log(back.name === '张三<b>');                    // 数据无损
console.log(html.includes('alert(1)') === false);

console.log(serializeForHtml(null) === 'null');
console.log(inject(undefined).includes('null'));
```

**评分点**：
- 四类转义齐全（</> & / U+2028/2029——闭合注入与 JS 语法非法字符都覆盖）；stringify 后统一替换（嵌套生效）
- roundtrip 数据无损验证（转义可逆）；恶意 payload 贯穿断言（无 alert(1) 原文）
- null/undefined 兜底
- 能说清「内嵌 JSON 的 XSS 向量是 </script> 闭合，转义契约要贯穿测试锁定（框架升级换序列化器最易丢失）」属于加分
