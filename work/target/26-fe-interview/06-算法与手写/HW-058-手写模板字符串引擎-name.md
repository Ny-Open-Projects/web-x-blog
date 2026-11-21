---
title: [HW-058] 手写模板字符串引擎（{{name}}）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-058：手写模板字符串引擎（{{name}}）

**答**：
- 评分点：基础正则替换 `/\{\{\s*([\w.]+)\s*\}\}/g`（支持空白、点路径 `user.name`）；路径取值短路（任一层 null/undefined 返回空串，不抛错）；**XSS 防护**是亮点——提供 escape 选项对 `& < > " '` 转义（HTML 场景默认转义）；进阶：**预编译**——把模板编译成函数（new Function 或 AST），重复渲染时不再跑正则，性能好得多；非法模板（未闭合 `{{`）要兜底（原样保留或抛错，说清约定）。

```javascript
// ===== 5 分钟速写版 =====
function renderTemplate(tpl, data) {
  return tpl.replace(/\{\{\s*([\w.]+)\s*\}\}/g, (_, path) => {
    const value = path.split('.').reduce((o, k) => (o == null ? o : o[k]), data);
    return value === undefined || value === null ? '' : String(value);
  });
}
// renderTemplate('你好，{{user.name}}，积分 {{score}}', { user: { name: 'Tom' }, score: 99 })

// ===== 标准完整版（含边界处理）=====
const escapeHtml = str => String(str)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
function renderTemplatePro(tpl, data, { escape = true } = {}) {
  if (typeof tpl !== 'string') throw new TypeError('tpl must be a string');
  const getValue = path => {
    // 支持点路径与数组下标：a.b[0].c
    const keys = path.replace(/\[(\d+)\]/g, '.$1').split('.');
    let cur = data;
    for (const k of keys) {
      if (cur === null || cur === undefined) return undefined; // 短路不抛错
      cur = cur[k];
    }
    return cur;
  };
  return tpl.replace(/\{\{\s*([\w.[\]]+)\s*\}\}/g, (_, path) => {
    const value = getValue(path);
    if (value === undefined || value === null) return ''; // 缺失字段留空而不是 undefined 字样
    return escape ? escapeHtml(value) : String(value);
  }).replace(/\{\{([^}]*)$/g, '$1'); // 未闭合的 {{ 原样保留（兜底，不打坏模板）
}
// 预编译版：模板重复渲染上千次时，编译一次成函数，渲染只剩拼接
function compileTemplate(tpl) {
  const exprs = [];
  const code = tpl.replace(/\{\{\s*([\w.[\]]+)\s*\}\}/g, (_, path) => {
    exprs.push(path);
    return `\u0000${exprs.length - 1}\u0000`; // 占位符隔离表达式与文本
  });
  const parts = code.split(/\u0000\d+\u0000/);
  return function (data) {
    let out = '';
    exprs.forEach((path, i) => {
      out += parts[i];
      const v = path.split('.').reduce((o, k) => (o == null ? o : o[k]), data);
      out += v === undefined || v === null ? '' : String(v);
    });
    return out + parts[parts.length - 1];
  };
}
// 追问：为什么不直接 new Function('data', 'return `' + tpl + '`') ——
// 会把用户模板当代码执行，模板注入 = XSS/RCE 风险；预编译必须只做「取值拼接」。
```

---
