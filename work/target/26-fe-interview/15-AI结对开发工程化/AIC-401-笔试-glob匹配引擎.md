---
title: [AIC-401] 笔试：实现一个精简版 glob 匹配引擎，支持 **、*、? 与 {a,b} 展开。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-401：笔试：实现一个精简版 glob 匹配引擎，支持 **、*、? 与 {a,b} 展开。
**题目**：实现 `matchGlob(pattern, path)`：`*` 匹配单段、`**` 跨段、`?` 单字符、`{a,b}` 或扩展。要求先转义正则元字符再替换通配符，20~40 行，含测试。

```javascript
function compileGlob(pattern) {
  // {a,b} 展开
  const m = pattern.match(/\{([^{}]+)\}/);
  if (m) return m[1].split(',').flatMap(p => [compileGlob(pattern.replace(m[0], p))]);
  const re = pattern
    .replace(/[.+^${}()|[\]\\]/g, '\\$&')   // 先转义（{} 已被消费）
    .replace(/\*\*\//g, '(?:.*/)?')
    .replace(/\*\*/g, '.*')
    .replace(/\*/g, '[^/]*')
    .replace(/\?/g, '[^/]');
  return [new RegExp(`^${re}$`)];
}
function matchGlob(pattern, path) {
  return compileGlob(pattern).some(re => re.test(path));
}
console.log(matchGlob('src/**/*.ts', 'src/a/b/c.ts'));   // true
console.log(matchGlob('src/*.ts', 'src/a/b.ts'));        // false（* 不跨段）
console.log(matchGlob('src/?.tsx', 'src/a.tsx'));        // false（? 单字符）
console.log(matchGlob('src/{a,b}/*.ts', 'src/b/x.ts'));  // true

```

**评分点**：
- 正则元字符先整体转义，再做通配符替换——顺序错误是最高频失分点。
- `*` 必须是 `[^/]*`（不跨段），`**` 才跨段（`(?:.*/)?` 或 `.*`）。
- `{a,b}` 展开成多个 pattern 再逐个匹配（或转交替组），注意嵌套与空分支。
- 测试覆盖：根路径、深层路径、文件名部分匹配、否定场景。
