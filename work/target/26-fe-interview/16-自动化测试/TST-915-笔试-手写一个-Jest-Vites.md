---
title: [TST-915] 笔试：手写一个 Jest→Vitest 快照头与转义的迁移转换器，保证内容语义不变
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-915：笔试：手写一个 Jest→Vitest 快照头与转义的迁移转换器，保证内容语义不变
**答**：
- 需求：实现 convertSnap(src)，输入 Jest 的 .snap 文件字符串，输出 Vitest 兼容字符串。
- 规则：Jest 头部为 `// Jest Snapshot v1, https://goo.gl/...`，Vitest 需替换为自己的版本头；把 \\" 转义规范化；导出形式 exports[`x 1`] 保持键名不变。
- 边界：内容中出现非快照注释需原样保留；键名含中文/emoji 不破坏；检测已转换过的文件直接返回。

```javascript
function convertSnap(src) {
  if (src.includes('Vitest Snapshot v1')) return src; // 幂等
  const lines = src.split('\n');
  const out = lines.map(line => {
    if (line.startsWith('// Jest Snapshot v1')) return '// Vitest Snapshot v1, https://vitest.dev/';
    // 统一转义：Jest 用 \" 表示双引号，Vitest 同样支持，保留但去掉多余反斜杠
    return line.replace(/\\{3,}"/g, '\\"');
  });
  // 保留非快照注释（以 // 开头且不是 Jest 头）
  const comments = lines.filter(l => l.startsWith('//') && !l.startsWith('// Jest Snapshot'));
  return [...out, ...(comments.length ? ['// preserved:', ...comments] : [])].join('\n');
}
const jestSnap = '// Jest Snapshot v1, https://goo.gl/fbAQLP\n\nexports[`sum 1`] = `3`;';
console.log(convertSnap(jestSnap));
// // Vitest Snapshot v1, https://vitest.dev/

exports[`sum 1`] = `3`;
```
**评分点**：
- 正确替换 Jest 版本头为 Vitest 版本头，且幂等（已转换直接返回）。
- 导出键名 exports[`xxx`] 原样保留，中文/emoji 不破坏。
- 非快照注释原样保留，转义规范化不丢失语义。
- 输出可被 Vitest 直接读取，不引入假 diff。
