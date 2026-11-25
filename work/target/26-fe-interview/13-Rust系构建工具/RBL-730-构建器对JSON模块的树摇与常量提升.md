---
title: [RBL-730] JSON 模块的打包优化：具名导入树摇、常量提升与大 JSON 懒解析
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-730：JSON 模块的打包优化：具名导入树摇、常量提升与大 JSON 懒解析

**答**:
- JSON 模块的优化点：1) **具名导入树摇**（`import { version } from './pkg.json'` → 只内嵌 version 字段，非整文件）；2) **常量提升**（JSON 是编译期已知值，字符串拼接/对象展开可常量折叠）；3) 大 JSON 懒解析（1MB+ 配置 JSON 转成「按需 getter 模块」——访问哪个字段才 parse 哪个子树）。
- 具名导入的实现：JSON → 虚拟 JS 模块（`export const version = "1.2"` 只保留被导入的路径）——需要「字段使用面收集」（点路径），动态访问 `obj[k]` 无法收集 → 保守保留全量并告警。
- 懒解析的权衡：懒解析把 parse 成本推迟到访问（首屏不用的配置 JSON 收益大），但 getter 包装增加体积与复杂度；阈值策略（>100KB 默认懒、小文件直接内联常量）。
- JSON 的 tree shaking 与 RBL-594 副作用语义一致：JSON 无副作用，未引用字段必然可删——这是 JSON 优化比 JS 激进的底气；但要警惕「JSON 参与运行时逻辑」（枚举完整性校验等）。
- 追问钩子：为什么大 JSON 的最佳答案常常是「别用 JSON」？——运行时只需要部分字段时，JSON 是「全部解析后取部分」的低效形态；构建期把 JSON 编译成按需模块/直接生成代码（codegen）才是终局——JSON import 是过渡态便利。

```javascript
// JSON 虚拟模块生成（具名导入树摇）
function jsonToModule(json, usedPaths) {
  if (!usedPaths) return `export default ${JSON.stringify(json)};`;   // 默认导入全量
  const lines = [];
  for (const p of usedPaths) {
    const v = get(json, p);
    if (v === undefined) warn(`JSON 字段不存在: ${p}`);
    else lines.push(`export const ${ident(p)} = ${JSON.stringify(v)};`);   // 只内嵌用到的路径
  }
  return lines.join('\n');
}
// 懒解析版本（大 JSON）
function jsonLazyModule(json) {
  return `const __data = () => JSON.parse(${JSON.stringify(JSON.stringify(json))});
export const __lazy = new Proxy({}, { get: (_, k) => __data()[k] });`;
}
// 使用面收集：扫描 import { a, b } from './x.json' 与属性访问 x.a.b
function collectJsonUsage(code, importName) {
  const paths = new Set();
  for (const m of code.matchAll(new RegExp(`${importName}\\.([\\w.]+)`, 'g')))
    paths.add(m[1]);
  return paths;
}
```
