---
title: [WCN-947] 手写编译模板调试元数据注入器：为生成代码注入 __tmplSource 与 sourceURL
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-947：手写编译模板调试元数据注入器：为生成代码注入 __tmplSource 与 sourceURL

**题目**：实现 `injectDebugMeta(code, meta)`，code 为编译生成的 JS 字符串，meta 形如 `{ component, file, line, column }`。要求：① 在 code 开头注入一行注释 `/* __tmplSource: {"component":"...","file":"...","line":N,"column":N} */`（JSON 序列化 meta，字段顺序固定）；② 在 code 末尾追加 `//# sourceURL=<file>`（用 meta.file）；③ 提供 `extractDebugMeta(injected)` 反向解析出 meta（从注释里 parse JSON），找不到返回 null；④ 若 code 已含 `__tmplSource` 注释则不重复注入（幂等）；⑤ 注入不改变 code 的执行语义（仅加注释）。请自足实现并给出可运行示例。

**答**：

```javascript
function injectDebugMeta(code, meta) {
  if (code.includes('__tmplSource:')) return code; // 幂等
  const payload = JSON.stringify({
    component: meta.component, file: meta.file,
    line: meta.line, column: meta.column,
  });
  const head = `/* __tmplSource: ${payload} */\n`;
  const tail = `\n//# sourceURL=${meta.file}`;
  return head + code + tail;
}
function extractDebugMeta(injected) {
  const m = injected.match(/\/\* __tmplSource: (\{[^}]*\}) \*\//);
  return m ? JSON.parse(m[1]) : null;
}
const code = 'return ctx.user.name;';
const injected = injectDebugMeta(code, { component: 'Card', file: 'Card.tmpl', line: 3, column: 8 });
console.log(injected);
// /* __tmplSource: {"component":"Card","file":"Card.tmpl","line":3,"column":8} */
// return ctx.user.name;
// //# sourceURL=Card.tmpl
console.log(extractDebugMeta(injected)); // { component:'Card', ... }
console.log(injectDebugMeta(injected, {}) === injected); // true（幂等）
```

**评分点**：
- 注入格式正确：开头注释含固定顺序 JSON、末尾 sourceURL。
- extractDebugMeta 正确反向解析，找不到返回 null。
- 幂等：已注入则不重复添加。
- 仅加注释不改变代码执行语义。
- 示例可运行、输出正确。
