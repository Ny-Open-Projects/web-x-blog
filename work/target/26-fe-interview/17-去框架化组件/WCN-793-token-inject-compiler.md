---
title: [WCN-793] 笔试：手写编译期把设计 token 注入模板样式的转换器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-793：笔试：手写编译期把设计 token 注入模板样式的转换器

**答**：
- 需求：实现 `injectTokens(code, tokens)`，code 中含形如 `token('path.to.token')` 或 `token("path")` 的调用，tokens 为 `{ 'path.to.token': { value, cssVar } }`。把每个调用替换为 `var(--cssVar, value)`；若 token 不存在则保留原调用并在末尾追加注释 `/* missing: PATH */`。边界：无 token 调用原样返回；重复调用都替换。
- 要点：正则匹配 token('...') 两种引号；查 tokens 映射；缺失收集到 comments；拼接返回。

```javascript
function injectTokens(code, tokens) {
  const missing = [];
  const out = code.replace(/token\((['"])([\w.]+)\1\)/g, (m, _q, path) => {
    const t = tokens[path];
    if (!t) { missing.push(path); return m; }         // 缺失保留原样
    return `var(--${t.cssVar}, ${t.value})`;
  });
  const tail = missing.length ? '\n/* missing: ' + missing.join(', ') + ' */' : '';
  return out + tail;
}
console.log(injectTokens(
  `color: token('color.primary'); border: token('space.md'); bg: token('no.such')`,
  { 'color.primary': { value: '#06f', cssVar: 'primary' },
    'space.md': { value: '16px', cssVar: 'space-md' } }
));
```

**评分点**：
- 正确匹配两种引号与 token 路径语法。
- 存在时替换为 var(--cssVar, value)，保留运行时换肤能力。
- 缺失 token 保留原调用并追加 missing 注释，不丢信息。
- 重复调用全部替换，边界（无调用）原样返回。

## 变体与延伸（补充）

**变体与延伸**：

1. token 路径含 `-` 或 `@` 时 `[\w.]` 会漏匹配怎么办 → 放宽为 `[^'"]+`，或按 tokens 表反向构建精确 pattern，避免路径语法与正则脱节。
2. 注释和字符串里出现 `token('x')` 会被误替换吗 → 会，纯正则分不清上下文；应先剥离注释与字符串，或改用 PostCSS 值解析按 AST 替换。
3. 希望缺失 token 在构建期直接失败而不是留注释怎么办 → 加 `strict` 选项，`missing` 非空时 throw 并打印文件与行号，注释模式只留给灰度迁移期。
