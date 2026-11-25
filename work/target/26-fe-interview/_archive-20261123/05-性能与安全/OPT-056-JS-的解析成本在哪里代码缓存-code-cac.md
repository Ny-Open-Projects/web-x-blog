---
title: [OPT-056] JS 的解析成本在哪里？代码缓存（code cache）怎么利用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-056：JS 的解析成本在哪里？代码缓存（code cache）怎么利用？

**答**：
- JS 到执行要经过 下载 → 解析成 AST → 编译字节码 → 优化编译；大包的"解析耗时"在低端机上能到几百 ms，是 TBT 的重要来源。
- V8 有 **code cache**：首次执行后把编译好的字节码随脚本 URL/版本缓存（Chrome 存 8 小时、要求资源可缓存且同 URL），二次访问免解析。
- 利用要点：**脚本 URL 稳定**（hash 命名而非每次变）、响应头允许强缓存、避免 eval/new Function（永远走全量编译）、大依赖别内联进 HTML。
- 两个警惕：JSON 的大对象字面量脚本比同体积 JSON.parse 慢很多（解析成本高）；`<script>` 每次内容变化就失去缓存资格。

```html
<!-- 一一对应：让 V8 code cache 生效的脚本投放方式 -->
<head>
  <!-- 1. 资源必须可强缓存且 URL 带 hash 稳定：code cache 按 URL 命中 -->
  <link rel="modulepreload" href="/assets/app.8f2a1c.js" />
  <!-- 2. modulepreload 让解析提前到空闲期，也给 code cache 留出编译时间 -->
  <script type="module" src="/assets/app.8f2a1c.js"></script>
</head>

<script>
// 3. 反例与正例对比：静态大 JSON
// 反例：把 JSON 转成 JS 对象字面量打包进脚本 —— 走全量 JS 解析
//   import bigData from './data.json'  ->  data.js " [ {...10万条...} ] "
// 正例：保持 .json 原样 fetch + JSON.parse —— V8 对 JSON 有专门快路径
async function loadBigData() {
  const res = await fetch('/data.json', { cache: 'force-cache' }); // 命中 HTTP 缓存零传输
  return res.json(); // JSON.parse 比等价 JS 字面量脚本解析快数倍
}

// 4. eval / new Function 每次都全量编译且禁用 code cache，热路径禁止使用
// 反例：new Function('a', 'return a * ' + factor) 在循环里反复构造
// 正例：先构造一次复用
const factor = 2;
const multiply = new Function('a', `return a * ${factor}`); // 只编译一次
[1, 2, 3].forEach((n) => multiply(n));
</script>
```
