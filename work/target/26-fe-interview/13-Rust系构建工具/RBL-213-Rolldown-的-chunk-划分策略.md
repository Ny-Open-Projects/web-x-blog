---
title: [RBL-213] Rolldown 的 chunk 划分策略与 advancedChunks
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-213：Rolldown 的 chunk 划分策略与 advancedChunks

**答**:
- 默认策略：入口 chunk + 动态导入 chunk；共享模块按引用关系抽公共 chunk（最小化重复加载）
- `advancedChunks`：按分组规则（test 匹配 + minShareCount/minSize）手动划 chunk——vendor 大包（echarts/lodash）单独成 chunk 控缓存
- 与 Rollup 的 manualChunks 差异：advancedChunks 是声明式分组（更可控），语义接近 webpack splitChunks
- 划分原则：变化频率分层（业务代码频繁变、vendor 稳定）→ 长缓存友好；避免过碎（请求开销）与过粗（缓存失效面大）

```javascript
export default {
  input: './src/main.tsx',
  advancedChunks: {
    groups: [
      { name: 'vendor-react', test: /node_modules[\\/](react|react-dom)/, priority: 10 },
      { name: 'vendor-charts', test: /node_modules[\\/]echarts/, priority: 9 },
      { name: 'common', minShareCount: 2, minSize: 20_000 },
    ],
  },
}
```
