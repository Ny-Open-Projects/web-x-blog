---
title: [RBL-147] 笔试：手写 browserslist → .swcrc 配置生成器
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-147：笔试：手写 browserslist → .swcrc 配置生成器

**题目**：写 gen-swcrc.js：1) 输入 browserslist 字符串（如 "Chrome >= 80, Safari >= 13, node >= 16"）；2) 解析出各浏览器最低版本，映射为 SWC 的 `jsc.target`（规则：支持 es2022 语法的最低版本全满足→es2022；否则逐级降档 es2020/es2018/es2015）；3) 输出完整 .swcrc JSON（含 parser/typescript、module es6、env.mode=usage）；4) 无法识别的 query 打 warning 且忽略；5) 纯函数 + CLI 双入口。

```javascript
// gen-swcrc.js
const QUERIES = { chrome: 'chrome', safari: 'safari', firefox: 'firefox', node: 'node' };
// 粗粒度分档表：各 target 要求的最低版本（示例粒度，面试讲清思路即可）
const TARGET_MIN = [
  { target: 'es2022', min: { chrome: 94, safari: 15.4, firefox: 93, node: 16.14 } },
  { target: 'es2020', min: { chrome: 80, safari: 13.1, firefox: 80, node: 14.5 } },
  { target: 'es2018', min: { chrome: 63, safari: 11.1, firefox: 58, node: 10 } },
  { target: 'es2015', min: { chrome: 47, safari: 9, firefox: 43, node: 6 } },
];

function parseBrowserslist(str) {
  const req = {}; const warnings = [];
  for (const q of str.split(',').map(s => s.trim()).filter(Boolean)) {
    const m = q.match(/^(\w+)\s*>=\s*([\d.]+)$/i);
    if (!m || !QUERIES[m[1].toLowerCase()]) { warnings.push(q); continue; }
    const k = QUERIES[m[1].toLowerCase()];
    req[k] = Math.max(req[k] ?? -Infinity, parseFloat(m[2]));
  }
  return { req, warnings };
}

function pickTarget(req) {
  for (const { target, min } of TARGET_MIN) {
    const ok = Object.entries(req).every(([b, v]) => (min[b] ?? 0) <= v);
    if (ok) return target;
  }
  return 'es5';
}

function genSwcrc(str) {
  const { req, warnings } = parseBrowserslist(str);
  warnings.forEach(w => console.warn(`[warn] 无法识别的 query: ${w}`));
  return {
    jsc: {
      parser: { syntax: 'typescript', tsx: true },
      target: pickTarget(req),
    },
    module: { type: 'es6' },
    env: { targets: str, mode: 'usage', coreJs: '3.30' },
  };
}
module.exports = { genSwcrc, pickTarget, parseBrowserslist };

// CLI 入口：node gen-swcrc.js "Chrome >= 80, Safari >= 13"
if (require.main === module) {
  const input = process.argv.slice(2).join(' ') || 'Chrome >= 80';
  console.log(JSON.stringify(genSwcrc(input), null, 2));
}
```
**评分点**：
- 解析容错：非法/未知 query warning 且不抛错。
- target 选择取"所有目标都满足"的最高档（交集逻辑，不是并集）。
- 同浏览器多 query 取最高版本（Math.max）。
- 纯函数与 CLI 分离，可测试。
- 能指出生产实现应接 browserslist/browserslist-rs 包而非手写表。
