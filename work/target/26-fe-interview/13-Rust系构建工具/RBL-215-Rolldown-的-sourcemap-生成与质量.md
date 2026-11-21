---
title: [RBL-215] Rolldown 的 sourcemap 链怎么保证正确性
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-215：Rolldown 的 sourcemap 链怎么保证正确性

**答**:
- 多级转换链（源码 → 转译 → 压缩 → chunk 合并）每级生成 map 并级联合并（remapping），Rolldown 在 Rust 内完成链合并保证一致性
- 验证工具：sourcemap-validator / 手动断点映射（浏览器 devtools 里看压缩产物断点是否落在原始源码正确行）
- 库打包注意：sourcemap true 输出 .map 与 sourceMappingURL 注释；对外发布带 map 提升 debug 体验但增加包体积（权衡）
- 与 Oxc 转换器的配合：转换器输出高保真 map（token 级），是链路质量的地基

```javascript
export default {
  input: 'src/index.ts',
  output: { file: 'dist/index.js', sourcemap: true, sourcemapFile: 'dist/index.js.map' },
}
// 验证：devtools 断点 → 原始 .ts 源码正确行；或用 source-map lib 逐点校验
```
