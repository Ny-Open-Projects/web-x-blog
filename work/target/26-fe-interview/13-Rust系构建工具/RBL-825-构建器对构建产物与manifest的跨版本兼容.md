---
title: [RBL-825] manifest 跨版本兼容：新旧构建器并存期的产物互认
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-825：manifest 跨版本兼容：新旧构建器并存期的产物互认

**答**:
- 并存期（迁移影子构建 RBL-667）两份 manifest（旧 webpack 的 stats / 新 rolldown 的 manifest）要被同一套下游工具消费——互认层的核心：**语义字段映射表**（webpack.stats 的 assets → manifest.outputs；chunks → closure），映射器版本化（旧/新各一版 adapter）——下游工具只认「统一 manifest 格式」。
- 映射的语义陷阱：webpack 的 chunks 与 rolldown 的 chunk 概念不等价（webpack 有 runtime chunk/child chunks）；映射不是字段重命名而是「语义对齐」——统一 schema 里用「角色」（entry/vendor/async）而非工具专有概念。
- 互认层的校验：两个 manifest 对同一构建任务的「语义等价断言」（入口集合/资源清单一致）——不一致即映射器 bug 或构建差异，CI 阻断（RBL-649 的 manifest 级 diff）。
- 并存期结束的收敛：统一 schema 成为唯一格式，旧 adapter 退役（RBL-768 退役清单加一项）；schema 版本化（RBL-785）保证未来演进。
- 追问钩子：为什么互认层要「统一 schema + 双 adapter」而不是「下游同时支持两种格式」？——下游工具的适配是 N×M 组合（N 个下游 × M 个构建器），统一 schema 是 N+M——总线化的经典收益；且 schema 是稳定契约（版本化演进），下游不因构建器升级而改——适配层的存在让「构建器可替换」成为架构属性。

```javascript
// 统一 manifest schema 与双 adapter
const UNIFIED = {
  version: '1.0',
  outputs: [],      // { name, role: entry|vendor|async|asset, bytes, hash }
  closures: {},     // entry -> { name, role }[]
};
const fromWebpack = (stats) => ({
  version: '1.0',
  outputs: stats.assets.map(a => ({ name: a.name,
    role: a.isEntry ? 'entry' : a.chunks?.some(c => /vendor|runtime/.test(c)) ? 'vendor' : 'async',
    bytes: a.size, hash: a.contenthash })),
  closures: Object.fromEntries(stats.entrypoints &&
    Object.entries(stats.entrypoints).map(([e, v]) => [e,
      v.assets.map(n => ({ name: n, role: roleOf(stats, n) }))])),
});
const fromRolldown = (manifest) => ({ version: '1.0',
  outputs: manifest.files.map(f => ({ name: f.name, role: f.role, bytes: f.size, hash: f.hash })),
  closures: manifest.closures });
// 下游只认 UNIFIED——构建器可替换
function semanticEq(m1, m2) {
  const names = (m) => m.outputs.map(o => o.name).sort().join(',');
  if (names(m1) !== names(m2)) fail('manifest 语义不等——映射器 bug 或构建差异');
  return true;
}
```
