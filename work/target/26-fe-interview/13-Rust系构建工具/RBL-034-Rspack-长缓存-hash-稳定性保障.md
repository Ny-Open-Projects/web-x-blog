---
title: [RBL-034] Rspack 如何保障产物 hash 稳定以支持长效缓存？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-034：Rspack 如何保障产物 hash 稳定以支持长效缓存？
**答**：
- 三个 hash 稳定性前提：模块 ID 稳定（optimization.moduleIds: deterministic，默认）、chunk ID 稳定（chunkIds: deterministic）、内容哈希只含该 chunk 的最终内容（contenthash）。
- 常见破稳点：非确定性的模块排序（动态 require 顺序）、插件运行时注入顺序不定、日期/随机值进 DefinePlugin、路径带构建机绝对路径参与 hash。
- 迁移验证法：连续两次无改动构建，diff 两份产物 manifest 的 hash 是否全等；改动一个业务文件，确认未受影响 vendor 的 hash 不变。
- Rspack 对齐度：与 webpack 5 的 deterministic 语义对齐，历史上对齐过程中有过 chunk 模块顺序差异的修复案例，灰度期务必跑双构建 diff。
- 收益量级：vendor 稳定意味着发版只下发变更 chunk，用户二次访问命中率 90%+。
- 追问钩子：hash 稳定性还依赖"sourcemap 注释位置一致性"这类细节，CDN 层缓存策略要配合 immutable。

```javascript
// hash 稳定性自检脚本
const { execSync } = require('child_process');
const h1 = manifestOf(execSync('rspack build --json').toString());
const h2 = manifestOf(execSync('rspack build --json').toString());
for (const k of Object.keys(h1)) {
  if (h1[k] !== h2[k]) console.log('不稳定:', k, h1[k], '->', h2[k]);
}
function manifestOf(json) {
  const s = JSON.parse(json);
  return Object.fromEntries(s.assets.map(a => [a.name, a.hash]));
}
```
