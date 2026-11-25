---
title: [RBL-062] 从 Rollup 迁移 Rolldown 有哪些行为差异需要回归？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-062：从 Rollup 迁移 Rolldown 有哪些行为差异需要回归？
**答**：
- 插件面：依赖 acorn AST 的插件（rollup-plugin-*）拿到的是不同 AST 形态，需要换 oxc 等价插件或用 rolldown 的兼容桥；操作 bundle 对象内部字段的插件要逐个验证。
- 解析细节：exports/条件导入的解析由 oxc_resolver 承载，极端 symlinks/浏览器字段组合可能有差异；主要入口 mainFields 默认序与 rollup 不同要检查。
- 压缩差异：rollup 默认不压缩（配 terser），rolldown 默认 oxc 压缩，产物 diff 时要先统一压缩开关。
- chunk 边界：同名 chunk 的模块归属在边角 case（如 preserveModules + 多 entry）可能不同，对产物 hash diff 一次。
- 警告体系：rollup 的大量 warnings（未使用导出、循环依赖）在 rolldown 中部分未实现或文案不同，CI 依赖警告数量的脚本要调整。
- 追问钩子：迁移公式 = 高频插件换原生 + 配置平移 + 产物 diff 门禁。

```javascript
// 迁移验证：双构建产物 diff
const { execSync } = require('child_process');
const a = buildDist('rollup -c');   // 产物目录 A
const b = buildDist('rolldown -c'); // 产物目录 B（统一 minify=false）
// 对比文件清单与内容
console.log('清单一致? ', sameFiles(a, b));
console.log('模块归属 diff: ', diffChunkMembers(a, b));
```
