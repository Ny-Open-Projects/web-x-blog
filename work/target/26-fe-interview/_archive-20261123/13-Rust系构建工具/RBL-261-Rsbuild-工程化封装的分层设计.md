---
title: [RBL-261] Rsbuild 工程化封装的分层设计
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-261：Rsbuild 工程化封装的分层设计

**答**:
- 三层封装：Rsbuild（引擎层，Rspack 之上的最佳实践配置）→ 团队 preset 包（统一 plugins/output/优化策略）→ 业务侧零配置启动——每层职责单一，升级只动 preset
- preset 内容：输出结构（多环境）、内置分析（bundle:stats）、代理/Mock 约定、性能预算默认值——「团队规范配置化」是核心价值
- 扩展模型：rsbuild.config 里通过 plugins 与 tools.rspack 透传定制；团队 preset 提供 hooks（beforeBuild/afterBuild）给业务埋钩子
- 升级治理：preset 版本 semver，业务锁 minor；preset 升级 PR 带「构建产物 diff 报告」作为 review 材料

```javascript
// preset 包：@team/rsbuild-preset
export const preset = {
  output: { distPath: { root: 'dist' }, assetPrefix: '/cdn/' },
  performance: { bundleAnalyze: { analyzerMode: 'stats' } },
  dev: { client: { overlay: true } },
}
// 业务侧 rsbuild.config.ts
export default { plugins: [presetPlugin()] }   // 一行接入团队规范
```
