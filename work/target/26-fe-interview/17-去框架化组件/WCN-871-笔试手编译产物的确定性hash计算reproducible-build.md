---
title: [WCN-871] 笔试：手写编译产物的「确定性 hash」计算（reproducible build 核心）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-871：笔试：手写编译产物的「确定性 hash」计算（reproducible build 核心）

**题目**：实现 `stableHash(bundle, options)`，对一组产物文件计算稳定的内容哈希。输入 `bundle` 是文件数组 `[{ path, code, imports: [...] }]`（顺序可能被打乱）。要求：① 忽略输入数组顺序——先按 path 字典序排序；② 对每个文件计算「规范化内容」：path 转相对路径（去掉绝对路径前缀）、code 中固定时间戳占位（把 `/* build:<数字> */` 替换为统一标记）、行尾统一为 `\n`；③ 把每个文件的 `{相对path, 规范化code, 排序后的imports}` 序列化后做 FNV-1a 32 位哈希（不用 crypto，纯 JS 实现可运行）；④ 把各文件哈希排序后合并再哈希，得到 bundle 级 hash（16 进制）。边界：空 bundle 返回固定值；相同内容不同顺序必须得到相同 hash。

**答**：

```javascript
function fnv1a(str) {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return (h >>> 0).toString(16).padStart(8, '0');
}
function stableHash(bundle, { root = '' } = {}) {
  if (!bundle || !bundle.length) return fnv1a('empty');
  const normalize = (f) => {
    const rel = f.path.replace(root, '').replace(/^\/+/, '');
    const code = f.code.replace(/\r\n/g, '\n')
      .replace(/\/\*\s*build:\d+\s*\*\//g, '/* build:X */'); // 固定时间戳
    const imports = [...(f.imports || [])].sort();
    return JSON.stringify({ rel, code, imports });
  };
  const perFile = [...bundle].sort((a, b) => a.path.localeCompare(b.path))
    .map(f => fnv1a(normalize(f))).sort();     // 文件哈希排序，忽略输入顺序
  return fnv1a(perFile.join('|'));
}
const b1 = [
  { path: '/proj/src/b.js', code: '/* build:123 */\nb', imports: ['x'] },
  { path: '/proj/src/a.js', code: 'a\r\n', imports: [] },
];
const b2 = [b1[1], b1[0]];                      // 顺序不同
console.log(stableHash(b1, { root: '/proj/' }) === stableHash(b2, { root: '/proj/' })); // true
```

**评分点**：
- 排序消除输入顺序影响，保证确定性（核心）。
- 规范化处理时间戳/路径/行尾，消除非确定性来源（关键细节）。
- 纯 JS FNV-1a 实现正确（无 crypto 依赖，可运行）。
- 分层哈希（文件→bundle）+ 空值兜底（结构与边界）。
