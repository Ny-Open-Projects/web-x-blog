---
title: [BLD-171] 构建配置的分层组织：presets、工厂函数、配置即 npm 包怎么设计？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-171：构建配置的分层组织：presets、工厂函数、配置即 npm 包怎么设计？
**答**：
- 三层结构：**内核层**（组织内 npm 包，如 `@org/webpack-preset`，封装 90% 默认值与插件链）→ **应用层**（各项目配置文件只声明差异：入口、代理、feature flag）→ **覆盖层**（本地 env/命令行参数，不改包配置就能临时覆盖）。
- 工厂函数优于"配置对象平铺"：`(options) => webpackConfig` 支持组合（spread 合并多 preset）、条件分支（env/mode）、类型提示（TS 定义 PresetOptions）；merge 策略要显式（webpack-merge 或自定义 rules 合并函数，避免数组覆盖丢 loader）。
- 版本化与治理：内核包 semver + 各项目锁版本（lockfile）； breaking 变更走 codemod（CLI 工具批量升级各仓配置文件）。
- 面试要点：说出"配置漂移"问题（各仓手改配置导致行为不一致）与"包化后灵活性损失"的权衡——preset 必须提供 escape hatch（`config.webpackConfigOverride` 钩子）。

```javascript
// packages/build-preset/index.js：组织级构建内核（工厂函数 + 组合）
const { mergeWithRules, merge } = require('webpack-merge');

// 基础 preset：所有应用共享
const base = ({ name }) => ({
  output: { filename: 'js/[name].[contenthash:8].js', publicPath: 'auto' },
  module: { rules: [
    { test: /\.(png|jpe?g|svg)$/, type: 'asset', parser: { dataUrlCondition: { maxSize: 4096 } } },
  ]},
  optimization: { runtimeChunk: 'single', splitChunks: { chunks: 'all' } },
});

// 能力 preset：按需叠加（组合而非继承）
const withTS = () => ({ module: { rules: [{ test: /\.tsx?$/, use: 'builtin:swc-loader' }] } });
const withLess = (vars) => ({ module: { rules: [{ test: /\.less$/, use: ['style-loader', 'css-loader', {
  loader: 'less-loader', options: { lessOptions: { modifyVars: vars } } }] }] } });

// 应用层最终 API：一行组装
function createAppConfig({ name, features = {}, overrides, env = {} }) {
  let config = base({ name });
  if (features.typescript !== false) config = merge(config, withTS());
  if (features.theme) config = merge(config, withLess(features.theme));
  // escape hatch：应用侧最后一次覆盖机会（审计日志保证可控）
  config = mergeWithRules({ module: { rules: { test: 'match', use: 'replace' } } })(config, overrides ?? {});
  return config;
}
// 应用项目里只剩：
// module.exports = createAppConfig({ name: 'checkout', features: { theme: { 'brand-color': '#f60' } },
//   overrides: { devServer: { port: 8001 } } });
```
